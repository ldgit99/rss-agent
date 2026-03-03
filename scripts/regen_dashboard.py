"""Regenerate dashboard.html from existing embedded PAPERS data using the updated template."""
import sys
import re
import json
from pathlib import Path

# Ensure src is importable
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from arxiv_agent import Paper, render_dashboard_html  # noqa: E402

html_path = Path(__file__).parent.parent / "obsidian" / "00-Inbox" / "dashboard.html"
html_content = html_path.read_text(encoding="utf-8")

match = re.search(r"const PAPERS = (\[.*?\]);", html_content, re.DOTALL)
if not match:
    print("ERROR: Could not find PAPERS data in dashboard.html")
    sys.exit(1)

cards_data = json.loads(match.group(1))
print(f"Found {len(cards_data)} papers in existing dashboard.html")

papers = []
for idx, card in enumerate(cards_data):
    source_raw = str(card.get("source", "ARXIV")).lower()
    has_review = bool(card.get("hasReview", False))
    content = str(card.get("content", ""))
    paper = Paper(
        source=source_raw,
        paper_id=str(card.get("id", str(idx))),
        title=str(card.get("title", "")),
        summary=content if not has_review else "",
        link=str(card.get("link", "")),
        pdf_link="",
        doi="",
        published=str(card.get("day", "")),
        authors=card.get("authors", []),
        categories=card.get("categories", []),
        score=int(card.get("score", 0)),
        review=content if has_review else "",
    )
    papers.append(paper)

new_html = render_dashboard_html(papers)
html_path.write_text(new_html, encoding="utf-8")
print(f"Dashboard regenerated successfully with {len(papers)} papers -> {html_path}")
