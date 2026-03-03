import argparse
import html
import io
import json
import os
import re
import smtplib
from dataclasses import dataclass
from datetime import datetime
from email.mime.text import MIMEText
from pathlib import Path
from typing import List
from xml.etree import ElementTree as ET

import requests
try:
    from pypdf import PdfReader
except Exception:
    PdfReader = None

ARXIV_API_URL = "https://export.arxiv.org/api/query"
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}


@dataclass
class Paper:
    source: str
    paper_id: str
    title: str
    summary: str
    link: str
    pdf_link: str
    doi: str
    published: str
    authors: List[str]
    categories: List[str]
    score: int = 0
    review: str = ""


def load_env(path: Path = Path(".env")) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


def load_config(config_path: Path) -> dict:
    return json.loads(config_path.read_text(encoding="utf-8"))


def build_query(categories: List[str]) -> str:
    if not categories:
        raise ValueError("At least one arXiv category is required.")
    return " OR ".join(f"cat:{c}" for c in categories)


def fetch_papers(categories: List[str], max_results: int) -> List[Paper]:
    query = build_query(categories)
    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    response = requests.get(ARXIV_API_URL, params=params, timeout=30)
    response.raise_for_status()
    root = ET.fromstring(response.text)

    papers: List[Paper] = []
    for entry in root.findall("atom:entry", ATOM_NS):
        arxiv_id = _text(entry, "atom:id").strip()
        title = _text(entry, "atom:title").replace("\n", " ").strip()
        summary = _text(entry, "atom:summary").replace("\n", " ").strip()
        published = _text(entry, "atom:published").strip()
        link = ""
        pdf_link = ""
        for link_elem in entry.findall("atom:link", ATOM_NS):
            if link_elem.attrib.get("rel") == "alternate":
                link = link_elem.attrib.get("href", "")
            if link_elem.attrib.get("title") == "pdf":
                pdf_link = link_elem.attrib.get("href", "")
        if not pdf_link and link:
            pdf_link = f"{link}.pdf"
        authors = [a.find("atom:name", ATOM_NS).text.strip() for a in entry.findall("atom:author", ATOM_NS)]
        category_terms = [c.attrib.get("term", "").strip() for c in entry.findall("atom:category", ATOM_NS)]
        papers.append(
            Paper(
                source="arxiv",
                paper_id=arxiv_id,
                title=title,
                summary=summary,
                link=link,
                pdf_link=pdf_link,
                doi="",
                published=published,
                authors=authors,
                categories=category_terms,
            )
        )
    return papers


def extract_openalex_abstract(inverted_index: dict) -> str:
    if not isinstance(inverted_index, dict):
        return ""
    positions: List[tuple] = []
    for word, idx_list in inverted_index.items():
        if not isinstance(idx_list, list):
            continue
        for idx in idx_list:
            if isinstance(idx, int):
                positions.append((idx, word))
    positions.sort(key=lambda x: x[0])
    return " ".join(word for _, word in positions).strip()


def build_keyword_query(include_keywords: List[str], fallback: str = "education ai learning", use_or: bool = True) -> str:
    cleaned = [k.strip() for k in include_keywords if k.strip()]
    if not cleaned:
        return fallback
    if use_or:
        return " OR ".join(cleaned[:8])
    return " ".join(cleaned[:8])


def fetch_eric_papers(include_keywords: List[str], max_results: int = 100) -> List[Paper]:
    query = build_keyword_query(include_keywords, use_or=True)
    params = {
        "search": query,
        "format": "json",
        "start": 0,
        "rows": max(20, min(max_results, 200)),
    }
    try:
        response = requests.get("https://api.ies.ed.gov/eric/", params=params, timeout=30)
        response.raise_for_status()
        payload = response.json()
    except Exception:
        return []

    docs = payload.get("response", {}).get("docs", [])
    papers: List[Paper] = []
    for doc in docs:
        title = str(doc.get("title") or "").strip()
        if not title:
            continue
        summary = str(doc.get("description") or doc.get("abstract") or "").strip()
        raw_authors = doc.get("author", [])
        if isinstance(raw_authors, str):
            authors = [a.strip() for a in raw_authors.split(";") if a.strip()]
        elif isinstance(raw_authors, list):
            authors = [str(a).strip() for a in raw_authors if str(a).strip()]
        else:
            authors = []

        year = str(doc.get("publicationyear") or doc.get("pubyear") or "").strip()
        link = str(doc.get("url") or "").strip()
        eric_number = str(doc.get("ericNumber") or doc.get("id") or link or title).strip()
        source_name = str(doc.get("source") or "ERIC").strip()
        descriptor = doc.get("descriptor", [])
        categories = [str(x).strip() for x in descriptor] if isinstance(descriptor, list) else []
        papers.append(
            Paper(
                source="eric",
                paper_id=f"eric:{eric_number}",
                title=title,
                summary=summary if summary else "명시되지 않음",
                link=link if link else "https://eric.ed.gov/",
                pdf_link="",
                doi=str(doc.get("doi") or "").strip(),
                published=year if year else "명시되지 않음",
                authors=authors if authors else ["명시되지 않음"],
                categories=categories if categories else [source_name],
            )
        )
    return papers


def fetch_openalex_papers(include_keywords: List[str], max_results: int = 100) -> List[Paper]:
    query = build_keyword_query(include_keywords, use_or=False)
    params = {
        "search": query,
        "per-page": max(25, min(max_results, 200)),
        "sort": "publication_date:desc",
    }
    email = os.getenv("OPENALEX_EMAIL")
    if email:
        params["mailto"] = email
    try:
        response = requests.get("https://api.openalex.org/works", params=params, timeout=30)
        response.raise_for_status()
        payload = response.json()
    except Exception:
        return []

    results = payload.get("results", [])
    papers: List[Paper] = []
    for item in results:
        title = str(item.get("display_name") or "").strip()
        if not title:
            continue
        openalex_id = str(item.get("id") or title).strip()
        abstract = extract_openalex_abstract(item.get("abstract_inverted_index"))
        summary = abstract if abstract else "명시되지 않음"
        authorships = item.get("authorships", [])
        authors: List[str] = []
        for a in authorships[:10]:
            name = str((a or {}).get("author", {}).get("display_name") or "").strip()
            if name:
                authors.append(name)
        concepts = item.get("concepts", [])
        categories = [str(c.get("display_name")).strip() for c in concepts[:8] if c.get("display_name")]
        doi = str(item.get("doi") or "").replace("https://doi.org/", "").strip()
        publication_date = str(item.get("publication_date") or item.get("publication_year") or "").strip()
        primary_location = item.get("primary_location", {}) or {}
        pdf_link = str(((primary_location.get("pdf_url")) or "")).strip()
        landing = str(item.get("ids", {}).get("openalex") or openalex_id).strip()
        link = landing if landing else "https://openalex.org/"
        papers.append(
            Paper(
                source="openalex",
                paper_id=f"openalex:{openalex_id}",
                title=title,
                summary=summary,
                link=link,
                pdf_link=pdf_link,
                doi=doi,
                published=publication_date if publication_date else "명시되지 않음",
                authors=authors if authors else ["명시되지 않음"],
                categories=categories if categories else ["OpenAlex"],
            )
        )
    return papers


def normalize_title(value: str) -> str:
    lowered = (value or "").lower()
    lowered = re.sub(r"\s+", " ", lowered).strip()
    return re.sub(r"[^a-z0-9 ]", "", lowered)


def dedupe_papers(papers: List[Paper]) -> List[Paper]:
    seen_keys = set()
    deduped: List[Paper] = []
    for paper in papers:
        doi_key = f"doi:{paper.doi.lower().strip()}" if paper.doi else ""
        title_key = f"title:{normalize_title(paper.title)}"
        key = doi_key if doi_key else title_key
        if not key or key in seen_keys:
            continue
        seen_keys.add(key)
        deduped.append(paper)
    return deduped


def _text(entry: ET.Element, selector: str) -> str:
    node = entry.find(selector, ATOM_NS)
    return node.text if node is not None and node.text is not None else ""


def load_seen_ids(state_path: Path) -> set:
    if not state_path.exists():
        return set()
    try:
        payload = json.loads(state_path.read_text(encoding="utf-8"))
        if isinstance(payload, list):
            return {str(x) for x in payload}
    except Exception:
        pass
    return set()


def save_seen_ids(state_path: Path, seen_ids: set) -> None:
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(sorted(seen_ids), ensure_ascii=False, indent=2), encoding="utf-8")


def score_papers(
    papers: List[Paper],
    include_keywords: List[str],
    exclude_keywords: List[str],
    education_focus_keywords: List[str],
    min_education_hits: int,
    min_include_hits: int,
    source_weights: dict,
) -> List[Paper]:
    include = [k.lower() for k in include_keywords]
    exclude = [k.lower() for k in exclude_keywords]
    edu_focus = [k.lower() for k in education_focus_keywords]
    result: List[Paper] = []
    for paper in papers:
        title = paper.title.lower()
        summary = paper.summary.lower()

        if any(k in title or k in summary for k in exclude):
            continue

        score = 0
        edu_hits = 0
        include_hits = 0
        for kw in include:
            if kw in title:
                score += 3
                include_hits += 1
            if kw in summary:
                score += 1
                include_hits += 1
        for kw in edu_focus:
            hit_in_title = kw in title
            hit_in_summary = kw in summary
            if hit_in_title:
                score += 5
                edu_hits += 1
            elif hit_in_summary:
                score += 2
                edu_hits += 1
        if edu_hits < min_education_hits:
            continue
        if include_hits < min_include_hits:
            continue
        source_weight = int(source_weights.get(paper.source, 0))
        score += source_weight
        if score > 0:
            paper.score = score
            result.append(paper)
    result.sort(key=lambda p: (p.score, p.published), reverse=True)
    return result


def rank_by_similarity(
    papers: List[Paper],
    include_keywords: List[str],
    education_focus_keywords: List[str],
    exclude_keywords: List[str],
    min_education_hits: int,
    min_include_hits: int,
    source_weights: dict,
) -> List[Paper]:
    include = [k.lower() for k in include_keywords]
    edu_focus = [k.lower() for k in education_focus_keywords]
    exclude = [k.lower() for k in exclude_keywords]
    ranked: List[Paper] = []

    for paper in papers:
        title = paper.title.lower()
        summary = paper.summary.lower()
        if any(k in title or k in summary for k in exclude):
            continue

        score = 0
        edu_hits = 0
        include_hits = 0
        for kw in include:
            if kw in title:
                score += 3
                include_hits += 1
            elif kw in summary:
                score += 1
                include_hits += 1
        for kw in edu_focus:
            if kw in title:
                score += 4
                edu_hits += 1
            elif kw in summary:
                score += 2
                edu_hits += 1
        if edu_hits < min_education_hits:
            continue
        if include_hits < min_include_hits:
            continue
        source_weight = int(source_weights.get(paper.source, 0))
        score += source_weight
        paper.score = score
        ranked.append(paper)

    ranked.sort(key=lambda p: (p.score, p.published), reverse=True)
    return ranked


def extract_pdf_text(pdf_bytes: bytes, max_pages: int = 8, max_chars: int = 20000) -> str:
    if PdfReader is None:
        return ""
    try:
        reader = PdfReader(io.BytesIO(pdf_bytes))
    except Exception:
        return ""
    chunks: List[str] = []
    for page_idx, page in enumerate(reader.pages):
        if page_idx >= max_pages:
            break
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        if text:
            chunks.append(text)
        if sum(len(c) for c in chunks) >= max_chars:
            break
    combined = "\n\n".join(chunks).strip()
    return combined[:max_chars] if len(combined) > max_chars else combined


def download_pdf_text(paper: Paper, timeout_sec: int, max_pages: int, max_chars: int) -> str:
    if not paper.pdf_link:
        return ""
    try:
        response = requests.get(paper.pdf_link, timeout=timeout_sec)
        response.raise_for_status()
        return extract_pdf_text(response.content, max_pages=max_pages, max_chars=max_chars)
    except Exception:
        return ""


def generate_openai_reviews(papers: List[Paper], include_keywords: List[str], review_top_k: int) -> None:
    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    endpoint = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1/chat/completions")
    if not api_key:
        print("[WARN] OPENAI_API_KEY is missing. Skip OpenAI reviews.")
        return

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    review_max_pdf_pages = int(os.getenv("REVIEW_MAX_PDF_PAGES", "8"))
    review_max_pdf_chars = int(os.getenv("REVIEW_MAX_PDF_CHARS", "20000"))
    review_pdf_timeout_sec = int(os.getenv("REVIEW_PDF_TIMEOUT_SEC", "45"))

    for idx, paper in enumerate(papers[:review_top_k], start=1):
        full_text = download_pdf_text(
            paper=paper,
            timeout_sec=review_pdf_timeout_sec,
            max_pages=review_max_pdf_pages,
            max_chars=review_max_pdf_chars,
        )
        source_hint = "PDF 본문 기반" if full_text else "초록 기반(PDF 추출 실패 또는 미제공)"
        prompt = (
            "You are an educational technology PhD-level researcher.\n\n"
            "Your task is to analyze academic papers and produce a structured academic summary "
            "formatted for direct use in Obsidian.\n\n"
            "Always follow these rules strictly:\n"
            "1. All outputs must be written entirely in Korean.\n"
            "2. Output must be in Markdown format only.\n"
            "3. The output must begin with valid YAML frontmatter.\n"
            "4. Do not include explanations outside the requested structure.\n"
            "5. If information is not available in the paper, write \"명시되지 않음\".\n"
            "6. Maintain academic tone. Avoid exaggeration or praise.\n"
            "7. Focus on logical structure, theoretical alignment, and methodological rigor.\n"
            "8. If statistical values are important, include them clearly.\n"
            "9. Ensure the output is clean and directly copy-paste ready for Obsidian.\n\n"
            "Use the following exact structure:\n\n"
            "---\n"
            "title:\n"
            "authors:\n"
            "year:\n"
            "journal:\n"
            "doi:\n"
            "research_type:\n"
            "methodology:\n"
            "data_type:\n"
            "sample:\n"
            "context:\n"
            "theoretical_framework:\n"
            "keywords: []\n"
            "---\n\n"
            "# APA 7th style\n\n"
            "# Summary (5-10 sentences)\n\n"
            "# Research Logic\n"
            "## Problem\n"
            "## Theory\n"
            "## Design\n"
            "## Findings\n"
            "## Conclusion\n\n"
            "# Key Findings\n"
            "-\n"
            "-\n"
            "-\n\n"
            "# Contributions\n"
            "## Theoretical\n"
            "## Methodological\n"
            "## Practical\n\n"
            "# Limitations\n"
            "-\n"
            "-\n\n"
            "# Transferable Insights\n"
            "-\n"
            "-\n\n"
            "# Idea Seeds\n"
            "1.\n"
            "2.\n"
            "3.\n\n"
            "# Citation Snippets\n"
            ">\n\n"
            "tags: #keyword1, #keyword2, #keyword3, #keyword4, #keyword5, #keyword6, #keyword7\n\n"
            "태그는 논문의 키워드를 중심으로 작성해 줘.\n"
            "If the user asks for a shorter version, also provide a 3-5 sentence compressed summary after the main output (also in Korean).\n"
            "If the user asks for review-style feedback, add a section titled \"Reviewer Comments\" at the end (in Korean).\n\n"
            "아래 논문 정보를 기반으로 위 형식을 정확히 지켜 작성하세요.\n"
            f"리뷰 소스: {source_hint}\n"
            f"관심 키워드: {', '.join(include_keywords)}\n"
            f"제목: {paper.title}\n"
            f"초록: {paper.summary}\n"
            f"저자: {', '.join(paper.authors)}\n"
            f"출판일: {paper.published}\n"
            f"카테고리: {', '.join(paper.categories)}\n"
            f"링크: {paper.link}\n"
            f"PDF 링크: {paper.pdf_link if paper.pdf_link else '명시되지 않음'}\n\n"
            f"본문 텍스트(일부):\n{full_text if full_text else '명시되지 않음'}\n"
        )
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": "주어진 형식을 엄격히 준수하고, 한국어 마크다운만 출력하라."},
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.2,
        }

        try:
            response = requests.post(endpoint, headers=headers, json=payload, timeout=60)
            response.raise_for_status()
            data = response.json()
            paper.review = data["choices"][0]["message"]["content"].strip()
            print(f"[INFO] OpenAI review generated for #{idx}")
        except Exception as exc:
            paper.review = f"(OpenAI review failed: {exc})"
            print(f"[WARN] OpenAI review failed for #{idx}")


def render_email_markdown(papers: List[Paper]) -> str:
    now = datetime.now().strftime("%Y-%m-%d")
    lines = [f"# 교육공학 연구 리뷰 ({now})", ""]
    if not papers:
        lines.append("- 오늘 리뷰된 논문이 없습니다.")
        return "\n".join(lines) + "\n"

    for idx, paper in enumerate(papers, start=1):
        doi_link = f"https://doi.org/{paper.doi}" if paper.doi else paper.link
        lines.extend(
            [
                f"## {idx}. {paper.title}",
                f"- Published: {paper.published}",
                f"- Link: {doi_link}",
                "",
                paper.review or "",
                "",
            ]
        )
    return "\n".join(lines)


def normalize_day(published: str) -> str:
    if not published:
        return "명시되지 않음"
    val = published.strip()
    if len(val) >= 10 and val[4] == "-" and val[7] == "-":
        return val[:10]
    if len(val) >= 4 and val[:4].isdigit():
        return f"{val[:4]}-01-01"
    return "명시되지 않음"


def render_dashboard_html(papers: List[Paper]) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    all_cards_data = []
    for idx, paper in enumerate(papers):
        day = normalize_day(paper.published)
        content = (paper.review or paper.summary or "명시되지 않음").strip()
        doi_link = f"https://doi.org/{paper.doi}" if paper.doi else ""
        all_cards_data.append({
            "id": str(idx),
            "source": paper.source.upper(),
            "score": paper.score,
            "day": day,
            "title": paper.title,
            "content": content,
            "link": doi_link or paper.link,
            "altLink": paper.link if doi_link else "",
            "hasDoi": bool(paper.doi),
            "hasReview": bool(paper.review),
        })

    cards_json = json.dumps(all_cards_data, ensure_ascii=False).replace("</", "<\\/")

    css = """
:root {
  --bg: #f0f2f5;
  --card: #ffffff;
  --ink: #191f28;
  --muted: #6b7684;
  --sub: #4e5968;
  --line: #e5e8eb;
  --line-light: #f3f5f7;
  --brand: #3182f6;
  --brand-bg: #e8f3ff;
  --brand-hover: #1b64da;
  --green: #05c46b;
  --green-bg: #e6f9f0;
  --yellow: #f59e0b;
  --yellow-bg: #fef3c7;
  --radius-card: 20px;
  --shadow: 0 2px 12px rgba(25,31,40,0.07);
}
[data-theme="dark"] {
  --bg: #131722;
  --card: #1e2330;
  --ink: #e5e8eb;
  --muted: #8b95a1;
  --sub: #a0aab4;
  --line: #2c3444;
  --line-light: #1a2638;
  --brand: #4d9cf8;
  --brand-bg: #172340;
  --brand-hover: #70b4ff;
  --green: #0be881;
  --green-bg: #0d3325;
  --yellow: #fcd34d;
  --yellow-bg: #664400;
  --shadow: none;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  background: var(--bg); color: var(--ink);
  font-family: "Pretendard", "Noto Sans KR", "Segoe UI", sans-serif;
  transition: background 0.2s, color 0.2s;
  line-height: 1.5;
}
.wrap { max-width: 1400px; margin: 0 auto; padding: 28px 20px 64px; }

/* ── Header ── */
.site-header {
  display: flex; align-items: center; justify-content: space-between;
  margin-bottom: 24px; flex-wrap: wrap; gap: 12px;
}
.header-left { display: flex; flex-direction: column; gap: 2px; }
h1 { font-size: 28px; font-weight: 800; letter-spacing: -0.5px; margin-bottom: 4px; }
.subtitle { font-size: 13px; color: var(--muted); }
.header-right { display: flex; align-items: center; gap: 10px; }
.updated { font-size: 12px; color: var(--muted); white-space: nowrap; }
.btn-icon { 
  background: var(--card); border: 1px solid var(--line);
  border-radius: 8px; padding: 6px 10px; cursor: pointer;
  font-size: 18px; transition: all 0.15s; display: flex; align-items: center; justify-content: center;
}
.btn-icon:hover { border-color: var(--brand); color: var(--brand); }
.btn-theme { white-space: nowrap; padding: 6px 14px; }

/* ── Tabs ── */
.tabs-section {
  display: flex; gap: 8px; margin-bottom: 20px; border-bottom: 1px solid var(--line); overflow-x: auto;
  padding-bottom: 12px;
}
.tab-btn {
  border: none; background: transparent; padding: 6px 14px; 
  font-size: 13px; font-weight: 700; color: var(--muted);
  cursor: pointer; transition: all 0.15s; white-space: nowrap;
  border-bottom: 2px solid transparent; margin-bottom: -12px;
}
.tab-btn:hover { color: var(--brand); }
.tab-btn.active { color: var(--brand); border-bottom-color: var(--brand); }

/* ── Stats section ── */
.stats-container {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 12px; margin-bottom: 20px;
}
.stat-chip {
  background: var(--card); border: 1px solid var(--line);
  border-radius: 12px; padding: 12px 14px;
  font-size: 12px; font-weight: 600; color: var(--muted);
  display: flex; flex-direction: column; gap: 4px;
}
.stat-chip .num { color: var(--ink); font-size: 18px; font-weight: 800; }
.stat-chip.accent { border-color: var(--brand); background: var(--brand-bg); color: var(--brand); }
.stat-chip.accent .num { color: var(--brand); }

/* ── Chart Container ── */
.charts-container {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 16px; margin-bottom: 24px;
}
.chart-box {
  background: var(--card); border: 1px solid var(--line);
  border-radius: 14px; padding: 16px; min-height: 250px;
}
.chart-box h3 { font-size: 13px; font-weight: 700; margin-bottom: 12px; color: var(--ink); }
.chart-box canvas { max-width: 100%; }

/* ── Tags cloud ── */
.tags-section {
  margin-bottom: 20px; background: var(--card); border: 1px solid var(--line);
  border-radius: 14px; padding: 12px 14px;
}
.tags-label { font-size: 12px; font-weight: 700; color: var(--muted); margin-bottom: 8px; }
.tags-cloud { display: flex; flex-wrap: wrap; gap: 6px; }
.tag-item {
  background: var(--line-light); color: var(--sub); 
  border-radius: 12px; padding: 4px 10px; font-size: 11px;
  cursor: pointer; border: 1px solid transparent; transition: all 0.15s;
}
.tag-item:hover { border-color: var(--brand); color: var(--brand); }

/* ── Toolbar ── */
.toolbar {
  background: var(--card); border: 1px solid var(--line);
  border-radius: 14px; padding: 12px 16px; margin-bottom: 20px;
  display: flex; flex-wrap: wrap; gap: 10px; align-items: center;
}
.search-input {
  flex: 1; min-width: 160px; border: 1px solid var(--line);
  border-radius: 8px; padding: 8px 12px; font-size: 13px;
  background: var(--bg); color: var(--ink); outline: none;
  transition: border-color 0.15s;
}
.search-input:focus { border-color: var(--brand); }
.search-input::placeholder { color: var(--muted); }
.filter-group { display: flex; gap: 6px; flex-wrap: wrap; }
.filter-divider { width: 1px; height: 20px; background: var(--line); }
.btn-filter {
  border: 1px solid var(--line); border-radius: 999px;
  padding: 6px 12px; font-size: 12px; font-weight: 700;
  cursor: pointer; background: transparent; color: var(--muted);
  transition: all 0.15s; white-space: nowrap;
}
.btn-filter:hover { border-color: var(--brand); color: var(--brand); }
.btn-filter.active { background: var(--brand); border-color: var(--brand); color: #fff; }
.input-label { font-size: 12px; color: var(--muted); font-weight: 700; white-space: nowrap; }
.input-group {
  display: flex; gap: 6px; align-items: center;
}
.input-sm {
  border: 1px solid var(--line); border-radius: 8px;
  padding: 6px 10px; font-size: 12px; cursor: pointer;
  background: var(--bg); color: var(--ink); transition: border-color 0.15s;
}
.input-sm:focus { border-color: var(--brand); outline: none; }
.result-info { font-size: 12px; color: var(--muted); margin-bottom: 16px; padding-left: 2px; }

/* ── Action buttons ── */
.action-buttons {
  display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 16px;
}
.btn-action {
  background: var(--card); border: 1px solid var(--line);
  border-radius: 8px; padding: 7px 12px; font-size: 12px; font-weight: 600;
  cursor: pointer; color: var(--sub); transition: all 0.15s;
  display: flex; align-items: center; gap: 4px;
}
.btn-action:hover { border-color: var(--brand); color: var(--brand); }

/* ── Date section ── */
.row-block { margin-bottom: 32px; }
.row-block-head { display: flex; align-items: center; gap: 10px; margin-bottom: 12px; }
.day-label {
  font-size: 13px; font-weight: 800; color: var(--muted);
  text-transform: uppercase; letter-spacing: 0.6px;
}
.day-divider { flex: 1; height: 1px; background: var(--line); }

/* ── Grid layout ── */
.row-grid { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 14px; }
.row-grid.featured { 
  grid-template-columns: 2fr 1fr 1fr 1fr 1fr;
  gap: 14px;
}
.featured-card { 
  grid-row: span 2;
  min-height: auto;
}

/* ── Card ── */
.tile {
  background: var(--card); border: 1px solid var(--line);
  border-radius: var(--radius-card); padding: 16px;
  min-height: 300px; display: flex; flex-direction: column;
  box-shadow: var(--shadow);
  transition: transform 0.15s, box-shadow 0.15s;
  position: relative; cursor: pointer;
  overflow: hidden;
}
.tile::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
  background: linear-gradient(135deg, transparent 0%, rgba(49, 130, 246, 0.03) 100%);
  pointer-events: none;
}
.tile:hover { 
  transform: translateY(-4px); 
  box-shadow: 0 12px 24px rgba(49, 130, 246, 0.15);
  border-color: var(--brand);
}
[data-theme="dark"] .tile:hover { 
  box-shadow: 0 12px 24px rgba(77, 156, 248, 0.25);
}
.tile.visited { opacity: 0.85; }
.tile-head {
  display: flex; justify-content: space-between;
  align-items: flex-start; margin-bottom: 10px; gap: 6px; z-index: 1; position: relative;
}
.tile-actions {
  display: flex; gap: 6px;
}
.btn-star {
  background: none; border: none; font-size: 16px; cursor: pointer;
  transition: all 0.15s;
  filter: drop-shadow(0 1px 2px rgba(0,0,0,0.1));
}
.btn-star:hover { transform: scale(1.2); }
.btn-star.active { color: var(--yellow); }
.badge-wrap { display: flex; gap: 4px; align-items: center; flex-wrap: wrap; }
.badge {
  background: var(--brand-bg); color: var(--brand);
  border-radius: 999px; padding: 3px 9px;
  font-size: 11px; font-weight: 800; letter-spacing: 0.3px;
}
.review-tag {
  background: var(--green-bg); color: var(--green);
  border-radius: 999px; padding: 3px 8px;
  font-size: 11px; font-weight: 700;
}
.score {
  color: var(--muted); font-size: 11px; font-weight: 700;
  white-space: nowrap; padding-top: 2px;
}
.card-title {
  font-size: 14px; font-weight: 700; line-height: 1.4; margin-bottom: 10px;
  color: var(--ink);
  display: -webkit-box; -webkit-line-clamp: 3;
  -webkit-box-orient: vertical; overflow: hidden;
  position: relative; z-index: 1;
}
.featured-card .card-title {
  font-size: 16px; -webkit-line-clamp: 4;
}
.content-wrap {
  position: relative; flex: 1; overflow: hidden;
  max-height: 160px; margin-bottom: 12px;
}
.featured-card .content-wrap {
  max-height: 200px;
}
.content-wrap::after {
  content: ""; position: absolute; bottom: 0; left: 0; right: 0;
  height: 40px;
  background: linear-gradient(to bottom, transparent, var(--card));
  pointer-events: none;
}
.content {
  font-size: 12px; line-height: 1.6; color: var(--sub);
  position: relative; z-index: 1;
}
.content p { margin-bottom: 4px; }
.content h1, .content h2, .content h3,
.content h4, .content h5, .content h6 {
  font-size: 12px; font-weight: 700; margin: 6px 0 2px; color: var(--ink);
}
.content ul, .content ol { padding-left: 14px; margin-bottom: 4px; }
.content li { margin-bottom: 2px; }
.content blockquote {
  border-left: 3px solid var(--brand); padding-left: 8px;
  color: var(--muted); margin: 4px 0; font-style: italic;
}
.content code {
  background: var(--bg); border-radius: 4px;
  padding: 1px 4px; font-size: 11px; font-family: monospace;
}
.content strong { color: var(--ink); font-weight: 700; }

.card-footer { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; position: relative; z-index: 1; }
.card-link {
  text-decoration: none; color: var(--brand); font-size: 12px; font-weight: 700;
  padding: 5px 12px; border: 1px solid var(--brand);
  border-radius: 8px; transition: all 0.15s;
  white-space: nowrap;
}
.card-link:hover { background: var(--brand); color: #fff; }
.card-link.alt {
  color: var(--muted); border-color: var(--line); font-weight: 600;
}
.card-link.alt:hover { background: var(--line); color: var(--ink); }

/* ── Modal ── */
.modal-overlay {
  display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.5); z-index: 1000; animation: fadeIn 0.2s;
}
.modal-overlay.active { display: flex; align-items: flex-start; justify-content: center; padding-top: 40px; }
.modal-content {
  background: var(--card); border: 1px solid var(--line);
  border-radius: 16px; max-width: 700px; width: 90%; max-height: 85vh;
  overflow-y: auto; position: relative; animation: slideUp 0.3s;
}
.modal-close {
  position: sticky; top: 0; right: 0; padding: 12px 16px;
  background: var(--card); border: none; font-size: 24px; cursor: pointer;
  color: var(--muted); float: right; z-index: 10;
}
.modal-close:hover { color: var(--brand); }
.modal-body { padding: 20px; clear: both; }
.modal-body h3 { font-size: 18px; font-weight: 800; margin-bottom: 12px; color: var(--ink); }
.modal-body .content { font-size: 13px; }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
@keyframes slideUp { from { transform: translateY(20px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

/* ── Empty state ── */
.empty-state {
  text-align: center; padding: 64px 20px; color: var(--muted);
  background: var(--card); border: 1px dashed var(--line); border-radius: 16px;
}
.empty-state p { font-size: 15px; font-weight: 600; margin-bottom: 6px; }
.empty-state small { font-size: 13px; }

/* ── Pagination ── */
.pagination {
  display: flex; justify-content: center; align-items: center;
  gap: 6px; margin-top: 40px; flex-wrap: wrap;
}
.btn-page {
  border: 1px solid var(--line); border-radius: 8px;
  padding: 7px 14px; font-size: 13px; font-weight: 600;
  cursor: pointer; background: var(--card); color: var(--ink);
  transition: all 0.15s; min-width: 38px;
}
.btn-page:hover:not(:disabled) { border-color: var(--brand); color: var(--brand); }
.btn-page:disabled { opacity: 0.3; cursor: not-allowed; }
.btn-page.active { background: var(--brand); border-color: var(--brand); color: #fff; }

/* ── Responsive ── */
@media (max-width: 1200px) { 
  .row-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .row-grid.featured { grid-template-columns: 1.5fr 1fr 1fr; }
  .charts-container { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 860px) {
  .row-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .row-grid.featured { grid-template-columns: 1fr 1fr; }
  .charts-container { grid-template-columns: 1fr; }
  .tile:hover { transform: translateY(-2px); }
}
@media (max-width: 560px) {
  .wrap { padding: 16px 12px 40px; }
  .row-grid { grid-template-columns: 1fr; }
  .row-grid.featured { grid-template-columns: 1fr; }
  h1 { font-size: 22px; }
  .stats-container { grid-template-columns: repeat(2, 1fr); }
  .tabs-section { gap: 4px; }
  .toolbar { flex-direction: column; }
  .search-input { min-width: 100%; }
  .filter-group { width: 100%; }
  .modal-content { width: 95%; }
}
"""

    js = """
const PAPERS = __CARDS_JSON__;
const PAGE_SIZE = 10;
let currentTab = 'all';
let currentSource = 'ALL';
let currentSort = 'score';
let currentPage = 1;
let filtered = [];
let favorites = JSON.parse(localStorage.getItem('favorites')) || [];
let searchHistory = JSON.parse(localStorage.getItem('searchHistory')) || [];
let visited = JSON.parse(localStorage.getItem('visited')) || [];

function toggleTheme() {
  const html = document.documentElement;
  const next = html.dataset.theme === 'dark' ? 'light' : 'dark';
  html.dataset.theme = next;
  document.getElementById('themeBtn').textContent = next === 'dark' ? '☀️ 라이트 모드' : '🌙 다크 모드';
  localStorage.setItem('theme', next);
}

function toggleTab(tab) {
  currentTab = tab;
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  event.target.classList.add('active');
  currentPage = 1;
  applyFilters();
}

function setSource(btn) {
  currentSource = btn.dataset.source;
  document.querySelectorAll('#sourceFilters .btn-filter').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  currentPage = 1;
  applyFilters();
}

function setSort(btn) {
  currentSort = btn.dataset.sort;
  document.querySelectorAll('#sortGroup .btn-filter').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  currentPage = 1;
  render();
}

function toggleFavorite(id, e) {
  e.stopPropagation();
  const idx = favorites.indexOf(id);
  if (idx === -1) {
    favorites.push(id);
  } else {
    favorites.splice(idx, 1);
  }
  localStorage.setItem('favorites', JSON.stringify(favorites));
  applyFilters();
}

function recordVisit(id) {
  if (!visited.includes(id)) {
    visited.push(id);
  }
  localStorage.setItem('visited', JSON.stringify(visited));
}

function recordSearch(query) {
  if (query.trim() && !searchHistory.includes(query)) {
    searchHistory.unshift(query);
    if (searchHistory.length > 10) searchHistory.pop();
    localStorage.setItem('searchHistory', JSON.stringify(searchHistory));
  }
}

function downloadJSON() {
  const data = JSON.stringify(filtered, null, 2);
  const blob = new Blob([data], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'papers_' + new Date().toISOString().split('T')[0] + '.json';
  a.click();
  URL.revokeObjectURL(url);
}

function downloadCSV() {
  const headers = ['제목', '출처', '스코어', '리뷰여부', '링크'];
  const rows = filtered.map(p => [
    '"' + p.title.replace(/"/g, '""') + '"',
    p.source,
    p.score,
    p.hasReview ? '예' : '아니오',
    p.link
  ]);
  const csv = [headers.join(','), ...rows.map(r => r.join(','))].join('\\n');
  const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'papers_' + new Date().toISOString().split('T')[0] + '.csv';
  a.click();
  URL.revokeObjectURL(url);
}

function shareCurrentView() {
  const state = {
    tab: currentTab,
    source: currentSource,
    sort: currentSort,
    minScore: document.getElementById('scoreFilter').value,
    search: document.getElementById('searchInput').value
  };
  const url = window.location.href.split('#')[0] + '#' + btoa(JSON.stringify(state));
  const text = '현재 필터 상태: ' + url;
  if (navigator.clipboard) {
    navigator.clipboard.writeText(url).then(() => alert('링크가 복사되었습니다!'));
  } else {
    alert('공유 링크:\\n' + url);
  }
}

function applyFilters() {
  const query = (document.getElementById('searchInput').value || '').toLowerCase();
  const minScore = parseInt(document.getElementById('scoreFilter').value) || 0;
  
  recordSearch(query);
  
  filtered = PAPERS.filter(function(p) {
    if (currentTab === 'reviewed' && !p.hasReview) return false;
    if (currentTab === 'favorites' && !favorites.includes(p.id)) return false;
    if (currentSource !== 'ALL' && p.source !== currentSource) return false;
    if (p.score < minScore) return false;
    if (query && p.title.toLowerCase().indexOf(query) === -1) return false;
    return true;
  });
  currentPage = 1;
  renderStats();
  render();
}

function mdToHtml(text) {
  try {
    const parsed = marked.parse(text);
    return (typeof DOMPurify !== 'undefined') ? DOMPurify.sanitize(parsed) : parsed;
  } catch(e) {
    return String(text).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  }
}

function openModal(p, e) {
  if (e) e.preventDefault();
  recordVisit(p.id);
  const modal = document.getElementById('detailModal');
  document.getElementById('modalTitle').textContent = p.title;
  document.getElementById('modalBadges').innerHTML = '<span class="badge">' + p.source + '</span>' + (p.hasReview ? '<span class="review-tag">리뷰</span>' : '');
  document.getElementById('modalContent').innerHTML = mdToHtml(p.content);
  document.getElementById('modalScore').textContent = 'Score: ' + p.score;
  document.getElementById('modalLink').href = p.link;
  modal.classList.add('active');
}

function closeModal() {
  document.getElementById('detailModal').classList.remove('active');
}

function renderCard(p, isFeatured) {
  const article = document.createElement('article');
  article.className = 'tile' + (isFeatured ? ' featured-card' : '') + (visited.includes(p.id) ? ' visited' : '');
  article.title = p.title;
  article.style.cursor = 'pointer';
  article.onclick = function(e) { openModal(p, e); };

  const head = document.createElement('div');
  head.className = 'tile-head';

  const actions = document.createElement('div');
  actions.className = 'tile-actions';
  const starBtn = document.createElement('button');
  starBtn.className = 'btn-star' + (favorites.includes(p.id) ? ' active' : '');
  starBtn.textContent = '⭐';
  starBtn.title = favorites.includes(p.id) ? '즐겨찾기 제거' : '즐겨찾기';
  starBtn.onclick = function(e) { toggleFavorite(p.id, e); };
  actions.appendChild(starBtn);

  const badgeWrap = document.createElement('span');
  badgeWrap.className = 'badge-wrap';
  const badge = document.createElement('span');
  badge.className = 'badge';
  badge.textContent = p.source;
  badgeWrap.appendChild(badge);
  if (p.hasReview) {
    const rt = document.createElement('span');
    rt.className = 'review-tag';
    rt.textContent = '리뷰';
    badgeWrap.appendChild(rt);
  }

  const scoreEl = document.createElement('span');
  scoreEl.className = 'score';
  scoreEl.textContent = 'S' + p.score;

  head.appendChild(actions);
  head.appendChild(badgeWrap);
  head.appendChild(scoreEl);

  const titleEl = document.createElement('h3');
  titleEl.className = 'card-title';
  titleEl.textContent = p.title;

  const contentWrap = document.createElement('div');
  contentWrap.className = 'content-wrap';
  const contentEl = document.createElement('div');
  contentEl.className = 'content';
  contentEl.innerHTML = mdToHtml(p.content);
  contentWrap.appendChild(contentEl);

  const footer = document.createElement('div');
  footer.className = 'card-footer';

  const linkEl = document.createElement('a');
  linkEl.className = 'card-link';
  linkEl.href = p.link;
  linkEl.target = '_blank';
  linkEl.rel = 'noreferrer';
  linkEl.onclick = function(e) { e.stopPropagation(); recordVisit(p.id); };
  linkEl.textContent = p.hasDoi ? 'DOI' : '논문 보기';
  footer.appendChild(linkEl);

  if (p.altLink) {
    const altEl = document.createElement('a');
    altEl.className = 'card-link alt';
    altEl.href = p.altLink;
    altEl.target = '_blank';
    altEl.rel = 'noreferrer';
    altEl.onclick = function(e) { e.stopPropagation(); recordVisit(p.id); };
    altEl.textContent = '원문';
    footer.appendChild(altEl);
  }

  article.appendChild(head);
  article.appendChild(titleEl);
  article.appendChild(contentWrap);
  article.appendChild(footer);
  return article;
}

function renderStats() {
  const total = PAPERS.length;
  const reviewed = PAPERS.filter(p => p.hasReview).length;
  const sources = [...new Set(PAPERS.map(p => p.source))].length;
  const allFavs = PAPERS.filter(p => favorites.includes(p.id)).length;
  
  const sb = document.getElementById('statsBar');
  sb.innerHTML = '';
  const chips = [
    { num: total, label: '모든 논문' },
    { num: reviewed, label: '리뷰 완료', accent: true },
    { num: allFavs, label: '즐겨찾기' },
    { num: sources, label: '출처' },
  ];
  chips.forEach(c => {
    const el = document.createElement('div');
    el.className = 'stat-chip' + (c.accent ? ' accent' : '');
    const num = document.createElement('span');
    num.className = 'num';
    num.textContent = c.num;
    el.appendChild(num);
    el.appendChild(document.createTextNode(' ' + c.label));
    sb.appendChild(el);
  });

  renderSourceChart();
}

function renderSourceChart() {
  const sourceCounts = {};
  PAPERS.forEach(p => {
    sourceCounts[p.source] = (sourceCounts[p.source] || 0) + 1;
  });
  
  const canvas = document.getElementById('sourceChart');
  if (!canvas || typeof Chart === 'undefined') return;
  
  if (canvas.chart) canvas.chart.destroy();
  
  const isDark = document.documentElement.dataset.theme === 'dark';
  const textColor = isDark ? '#a0aab4' : '#6b7684';
  const borderColor = isDark ? '#2c3444' : '#e5e8eb';
  
  canvas.chart = new Chart(canvas, {
    type: 'doughnut',
    data: {
      labels: Object.keys(sourceCounts),
      datasets: [{
        data: Object.values(sourceCounts),
        backgroundColor: ['#3182f6', '#05c46b', '#f59e0b'],
        borderColor: [borderColor, borderColor, borderColor],
        borderWidth: 2
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      plugins: {
        legend: { labels: { color: textColor, font: { size: 11 } } }
      }
    }
  });
}

function render() {
  const start = (currentPage - 1) * PAGE_SIZE;
  const page = filtered.slice(start, start + PAGE_SIZE);
  const totalPages = Math.max(1, Math.ceil(filtered.length / PAGE_SIZE));
  const dashboard = document.getElementById('dashboard');

  document.getElementById('resultInfo').textContent =
    '총 ' + filtered.length + '편 · ' + currentPage + ' / ' + totalPages + ' 페이지';

  dashboard.innerHTML = '';
  if (filtered.length === 0) {
    const empty = document.createElement('div');
    empty.className = 'empty-state';
    const ep = document.createElement('p');
    ep.textContent = '검색 조건에 맞는 논문이 없습니다.';
    const es = document.createElement('small');
    es.textContent = '필터를 변경하거나 검색어를 확인해 주세요.';
    empty.appendChild(ep);
    empty.appendChild(es);
    dashboard.appendChild(empty);
    document.getElementById('pagination').innerHTML = '';
    return;
  }

  const sorted = page.slice().sort(function(a, b) {
    if (currentSort === 'review') {
      return (b.hasReview ? 1 : 0) - (a.hasReview ? 1 : 0) || b.score - a.score;
    }
    if (currentSort === 'date') {
      return b.day < a.day ? -1 : b.day > a.day ? 1 : b.score - a.score;
    }
    return b.score - a.score || (b.day < a.day ? -1 : b.day > a.day ? 1 : 0);
  });

  const groups = {};
  sorted.forEach((p, idx) => {
    if (!groups[p.day]) groups[p.day] = [];
    groups[p.day].push({...p, index: idx});
  });

  Object.keys(groups).sort().reverse().forEach(day => {
    const section = document.createElement('section');
    section.className = 'row-block';

    const rowHead = document.createElement('div');
    rowHead.className = 'row-block-head';
    const h2 = document.createElement('h2');
    h2.className = 'day-label';
    h2.textContent = day;
    const divider = document.createElement('span');
    divider.className = 'day-divider';
    rowHead.appendChild(h2);
    rowHead.appendChild(divider);

    const grid = document.createElement('div');
    grid.className = 'row-grid' + (start === 0 && groups[day][0].index === 0 ? ' featured' : '');
    groups[day].forEach((p, idx) => {
      grid.appendChild(renderCard(p, start === 0 && idx === 0));
    });

    section.appendChild(rowHead);
    section.appendChild(grid);
    dashboard.appendChild(section);
  });

  const pg = document.getElementById('pagination');
  pg.innerHTML = '';
  if (totalPages > 1) {
    const prev = document.createElement('button');
    prev.className = 'btn-page';
    prev.textContent = '← 이전';
    prev.disabled = currentPage === 1;
    prev.addEventListener('click', () => goPage(currentPage - 1));
    pg.appendChild(prev);

    for (let i = 1; i <= totalPages; i++) {
      (n => {
        const btn = document.createElement('button');
        btn.className = 'btn-page' + (n === currentPage ? ' active' : '');
        btn.textContent = n;
        btn.addEventListener('click', () => goPage(n));
        pg.appendChild(btn);
      })(i);
    }

    const next = document.createElement('button');
    next.className = 'btn-page';
    next.textContent = '다음 →';
    next.disabled = currentPage === totalPages;
    next.addEventListener('click', () => goPage(currentPage + 1));
    pg.appendChild(next);
  }
}

function goPage(p) {
  currentPage = p;
  render();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

(function() {
  const saved = localStorage.getItem('theme');
  if (saved) {
    document.documentElement.dataset.theme = saved;
    document.getElementById('themeBtn').textContent = saved === 'dark' ? '☀️ 라이트 모드' : '🌙 다크 모드';
  }
  filtered = PAPERS.slice();
  renderStats();
  render();
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') closeModal();
  });
  document.getElementById('detailModal').addEventListener('click', e => {
    if (e.target.id === 'detailModal') closeModal();
  });
})();
""".replace("__CARDS_JSON__", cards_json)

    return f"""<!doctype html>
<html lang="ko" data-theme="light">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>논문 요약 대시보드</title>
  <script src="https://cdn.jsdelivr.net/npm/marked@9/marked.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4/dist/chart.min.js"></script>
  <style>{css}</style>
</head>
<body>
  <main class="wrap">
    <header class="site-header">
      <div class="header-left">
        <h1>📚 논문 대시보드</h1>
        <span class="subtitle">AI &amp; Education 관련 최신 논문 큐레이션</span>
      </div>
      <div class="header-right">
        <span class="updated">✏️ {now}</span>
        <button class="btn-icon btn-theme" id="themeBtn" onclick="toggleTheme()" title="테마 전환">🌙 다크 모드</button>
      </div>
    </header>

    <div class="tabs-section">
      <button class="tab-btn active" data-tab="all" onclick="toggleTab('all')">전체</button>
      <button class="tab-btn" data-tab="reviewed" onclick="toggleTab('reviewed')">리뷰 완료</button>
      <button class="tab-btn" data-tab="favorites" onclick="toggleTab('favorites')">⭐ 즐겨찾기</button>
    </div>

    <div class="stats-container" id="statsBar"></div>

    <div class="charts-container">
      <div class="chart-box">
        <h3>출처별 분포</h3>
        <canvas id="sourceChart"></canvas>
      </div>
    </div>

    <div class="action-buttons">
      <button class="btn-action" onclick="downloadJSON()" title="JSON 다운로드">📥 JSON</button>
      <button class="btn-action" onclick="downloadCSV()" title="CSV 다운로드">📊 CSV</button>
      <button class="btn-action" onclick="shareCurrentView()" title="현재 필터 공유">🔗 공유</button>
    </div>

    <div class="toolbar">
      <input class="search-input" id="searchInput" type="search"
             placeholder="🔍 제목 검색..." oninput="applyFilters()" />
      <div class="filter-divider"></div>
      <div class="filter-group" id="sourceFilters">
        <button class="btn-filter active" data-source="ALL" onclick="setSource(this)">전체</button>
        <button class="btn-filter" data-source="ARXIV" onclick="setSource(this)">arXiv</button>
        <button class="btn-filter" data-source="ERIC" onclick="setSource(this)">ERIC</button>
        <button class="btn-filter" data-source="OPENALEX" onclick="setSource(this)">OpenAlex</button>
      </div>
      <div class="filter-divider"></div>
      <div class="filter-group" id="sortGroup">
        <button class="btn-filter active" data-sort="score" onclick="setSort(this)">점수순</button>
        <button class="btn-filter" data-sort="date" onclick="setSort(this)">최신순</button>
        <button class="btn-filter" data-sort="review" onclick="setSort(this)">리뷰순</button>
      </div>
      <div class="filter-divider"></div>
      <div class="input-group">
        <label class="input-label">최소 점수</label>
        <select class="input-sm" id="scoreFilter" onchange="applyFilters()">
          <option value="0">전체</option>
          <option value="5">5+</option>
          <option value="10">10+</option>
          <option value="15">15+</option>
          <option value="20">20+</option>
        </select>
      </div>
    </div>

    <p class="result-info" id="resultInfo"></p>
    <div id="dashboard"></div>
    <nav class="pagination" id="pagination"></nav>
  </main>

  <div class="modal-overlay" id="detailModal">
    <div class="modal-content">
      <button class="modal-close" onclick="closeModal()">&times;</button>
      <div class="modal-body">
        <div id="modalBadges" style="margin-bottom: 12px;"></div>
        <h3 id="modalTitle"></h3>
        <div id="modalContent" class="content" style="margin: 16px 0;"></div>
        <div id="modalScore" style="font-size: 12px; color: var(--muted); margin-bottom: 12px;"></div>
        <a id="modalLink" class="card-link" target="_blank" rel="noreferrer">논문 보기</a>
      </div>
    </div>
  </div>

  <script>{js}</script>
</body>
</html>"""


def save_dashboard_html(papers: List[Paper], output_root: Path, subfolder: str) -> Path:
    dashboard_dir = output_root / subfolder
    if not os.path.lexists(str(dashboard_dir)):
        dashboard_dir.mkdir(parents=True, exist_ok=True)
    dashboard_path = dashboard_dir / "dashboard.html"
    dashboard_path.write_text(render_dashboard_html(papers), encoding="utf-8")
    return dashboard_path


def sanitize_filename(name: str, max_len: int = 120) -> str:
    sanitized = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", name)
    sanitized = re.sub(r"\s+", " ", sanitized).strip().strip(".")
    return sanitized[:max_len] if len(sanitized) > max_len else sanitized


def render_obsidian_note(paper: Paper) -> str:
    review_section = paper.review if paper.review else "명시되지 않음"
    lines = [
        f"# {paper.title}",
        "",
        f"- Source: {paper.source}",
        f"- ID: {paper.paper_id}",
        f"- DOI: {paper.doi if paper.doi else '명시되지 않음'}",
        f"- Published: {paper.published}",
        f"- Authors: {', '.join(paper.authors)}",
        f"- Categories: {', '.join(paper.categories)}",
        f"- Link: {paper.link}",
        f"- PDF: {paper.pdf_link if paper.pdf_link else '명시되지 않음'}",
        f"- Keyword Score: {paper.score}",
        "",
        "## Abstract",
        paper.summary,
        "",
        "## OpenAI Review",
        review_section,
        "",
    ]
    return "\n".join(lines)


def save_obsidian_notes(papers: List[Paper], output_root: Path, subfolder: str) -> List[Path]:
    day = datetime.now().strftime("%Y-%m-%d")
    target_dir = output_root / subfolder
    # Handle junction/symlink paths on Windows: exists() can be False when target is missing.
    if not os.path.lexists(str(target_dir)):
        target_dir.mkdir(parents=True, exist_ok=True)

    saved_paths: List[Path] = []
    for paper in papers:
        if not paper.review:
            continue
        safe_title = sanitize_filename(paper.title)
        filename = f"{day}_{safe_title}.md"
        filepath = target_dir / filename
        filepath.write_text(render_obsidian_note(paper), encoding="utf-8")
        saved_paths.append(filepath)
    return saved_paths


def send_email(subject: str, body: str) -> None:
    host = os.getenv("SMTP_HOST")
    port = int(os.getenv("SMTP_PORT", "587"))
    user = os.getenv("SMTP_USER")
    password = os.getenv("SMTP_PASS")
    sender = os.getenv("EMAIL_FROM", user or "")
    recipient = os.getenv("EMAIL_TO")

    if not (host and user and password and recipient and sender):
        print("[WARN] SMTP/Email env is incomplete. Skip email.")
        return

    message = MIMEText(body, _charset="utf-8")
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = recipient

    with smtplib.SMTP(host, port, timeout=30) as server:
        server.starttls()
        server.login(user, password)
        server.sendmail(sender, [recipient], message.as_string())


def run(config_path: Path, dry_run: bool = False) -> List[Path]:
    load_env()
    config = load_config(config_path)
    include_keywords = config.get("include_keywords", [])
    source_limits = config.get("source_limits", {})
    arxiv_limit = int(source_limits.get("arxiv", config.get("max_results", 80)))
    eric_limit = int(source_limits.get("eric", 100))
    openalex_limit = int(source_limits.get("openalex", 100))

    arxiv_papers = fetch_papers(config["categories"], arxiv_limit)
    eric_papers = fetch_eric_papers(include_keywords=include_keywords, max_results=eric_limit)
    openalex_papers = fetch_openalex_papers(include_keywords=include_keywords, max_results=openalex_limit)
    papers = dedupe_papers(arxiv_papers + eric_papers + openalex_papers)
    print(
        f"[INFO] Source counts - arXiv: {len(arxiv_papers)}, ERIC: {len(eric_papers)}, "
        f"OpenAlex: {len(openalex_papers)}, Deduped total: {len(papers)}"
    )

    state_path = Path(config.get("seen_state_path", "data/seen_papers.json"))
    seen_ids = load_seen_ids(state_path)
    unseen_papers = [p for p in papers if p.paper_id and p.paper_id not in seen_ids]

    default_edu_focus = [
        "education",
        "classroom",
        "teacher",
        "student",
        "learning",
        "pedagogy",
        "instruction",
        "tutoring",
        "learning analytics",
        "ai literacy",
        "tpack",
        "scaffolding",
    ]
    exclude_keywords = config.get("exclude_keywords", [])
    edu_focus_keywords = config.get("education_focus_keywords", default_edu_focus)
    min_education_hits = int(config.get("min_education_hits", 1))
    min_include_hits = int(config.get("min_include_hits", 1))
    fallback_min_education_hits = int(config.get("fallback_min_education_hits", 1))
    source_weights = config.get("source_weights", {"arxiv": 0, "eric": 2, "openalex": 1})

    ranked = score_papers(
        papers=unseen_papers,
        include_keywords=include_keywords,
        exclude_keywords=exclude_keywords,
        education_focus_keywords=edu_focus_keywords,
        min_education_hits=min_education_hits,
        min_include_hits=min_include_hits,
        source_weights=source_weights,
    )
    if not ranked:
        print("[WARN] No papers matched strict filters. Relaxing education threshold for fallback.")
        ranked = score_papers(
            papers=unseen_papers,
            include_keywords=include_keywords,
            exclude_keywords=exclude_keywords,
            education_focus_keywords=edu_focus_keywords,
            min_education_hits=fallback_min_education_hits,
            min_include_hits=min_include_hits,
            source_weights=source_weights,
        )
    if not ranked:
        print("[WARN] No papers matched relaxed filters. Falling back to similarity ranking on unseen papers.")
        ranked = rank_by_similarity(
            papers=unseen_papers,
            include_keywords=include_keywords,
            education_focus_keywords=edu_focus_keywords,
            exclude_keywords=exclude_keywords,
            min_education_hits=fallback_min_education_hits,
            min_include_hits=min_include_hits,
            source_weights=source_weights,
        )
    if not ranked:
        print("[WARN] No unseen papers available. Falling back to similarity ranking including seen papers.")
        ranked = rank_by_similarity(
            papers=papers,
            include_keywords=include_keywords,
            education_focus_keywords=edu_focus_keywords,
            exclude_keywords=exclude_keywords,
            min_education_hits=fallback_min_education_hits,
            min_include_hits=min_include_hits,
            source_weights=source_weights,
        )

    top_k = int(config.get("top_k", 10))
    review_top_k = int(config.get("review_top_k", 5))
    selected = ranked[:top_k]
    generate_openai_reviews(
        papers=selected,
        include_keywords=include_keywords,
        review_top_k=review_top_k,
    )
    reviewed_papers = [p for p in selected if p.review][:review_top_k]
    email_markdown = render_email_markdown(reviewed_papers)

    obsidian_path = os.getenv("OBSIDIAN_VAULT_PATH")
    output_root = Path(obsidian_path) if obsidian_path else Path("output")
    subfolder = os.getenv("OBSIDIAN_SUBFOLDER", "Arxiv-Daily")
    saved_paths = save_obsidian_notes(selected, output_root=output_root, subfolder=subfolder)
    print(f"[INFO] Saved {len(saved_paths)} Obsidian notes in: {output_root / subfolder}")
    dashboard_path = save_dashboard_html(selected, output_root=output_root, subfolder=subfolder)
    print(f"[INFO] Saved dashboard: {dashboard_path}")

    if not dry_run:
        selected_ids = {p.paper_id for p in selected if p.paper_id}
        save_seen_ids(state_path, seen_ids.union(selected_ids))

    if not dry_run:
        send_email(
            subject=f"[RSS-AGENT] 교육공학 연구 리뷰-{datetime.now().strftime('%Y-%m-%d')}",
            body=email_markdown,
        )
    return saved_paths


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="arXiv daily recommendation agent")
    parser.add_argument("--config", default="config/interests.json", help="Path to interests json")
    parser.add_argument("--dry-run", action="store_true", help="Skip email and only save markdown")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    run(config_path=Path(args.config), dry_run=args.dry_run)
