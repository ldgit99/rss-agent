import argparse
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
    lines = [f"# arXiv Daily Picks ({now})", ""]
    if not papers:
        lines.append("- No papers matched your keyword filters today.")
        return "\n".join(lines) + "\n"

    lines.append("## Top 10 by Keyword Score")
    lines.append("")
    for idx, paper in enumerate(papers, start=1):
        short_summary = paper.summary[:350] + ("..." if len(paper.summary) > 350 else "")
        authors = ", ".join(paper.authors[:6])
        lines.extend(
            [
                f"## {idx}. {paper.title}",
                f"- Score: {paper.score}",
                f"- Published: {paper.published}",
                f"- Authors: {authors}",
                f"- Categories: {', '.join(paper.categories)}",
                f"- Link: {paper.link}",
                "",
                short_summary,
                "",
            ]
        )

    reviewed = [p for p in papers if p.review]
    if reviewed:
        lines.append("## OpenAI Reviews (Top 5)")
        lines.append("")
        for idx, paper in enumerate(reviewed, start=1):
            lines.extend(
                [
                    f"### Review {idx}: {paper.title}",
                    f"- Link: {paper.link}",
                    "",
                    paper.review,
                    "",
                ]
            )
    return "\n".join(lines)


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
    email_markdown = render_email_markdown(selected)

    obsidian_path = os.getenv("OBSIDIAN_VAULT_PATH")
    output_root = Path(obsidian_path) if obsidian_path else Path("output")
    subfolder = os.getenv("OBSIDIAN_SUBFOLDER", "Arxiv-Daily")
    saved_paths = save_obsidian_notes(selected, output_root=output_root, subfolder=subfolder)
    print(f"[INFO] Saved {len(saved_paths)} Obsidian notes in: {output_root / subfolder}")

    if not dry_run:
        selected_ids = {p.paper_id for p in selected if p.paper_id}
        save_seen_ids(state_path, seen_ids.union(selected_ids))

    if not dry_run:
        send_email(
            subject=f"[arXiv] Daily Picks {datetime.now().strftime('%Y-%m-%d')}",
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
