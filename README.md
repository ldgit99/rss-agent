# Multi-Source Daily Recommendation Agent

This project fetches recent papers from arXiv, ERIC, and OpenAlex, scores them by your interest keywords, keeps the top 10, then generates OpenAI reviews for the top 5.
For reviewed papers, it attempts PDF full-text extraction first and falls back to abstract-only review if extraction fails.

Outputs:
- Save markdown into your Obsidian vault
- Send the same markdown by email
- Run automatically every day at 07:00 (Windows Task Scheduler)

## 1) Install

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 2) Configure

Create config files:

```powershell
Copy-Item config\interests.example.json config\interests.json
Copy-Item .env.example .env
```

Edit `.env`:
- `SMTP_*`, `EMAIL_*` for mail sending
- `OBSIDIAN_VAULT_PATH` and `OBSIDIAN_SUBFOLDER`
- `OPENAI_API_KEY`
- Optional: `OPENAI_MODEL` (default `gpt-4o-mini`)
- Optional: `OPENALEX_EMAIL` (recommended for OpenAlex polite pool)
- Optional: `REVIEW_MAX_PDF_PAGES`, `REVIEW_MAX_PDF_CHARS`, `REVIEW_PDF_TIMEOUT_SEC`

Edit `config/interests.json`:
- `categories`: arXiv categories to scan
- `include_keywords`: keywords for scoring
- `exclude_keywords`: optional filter
- `education_focus_keywords`: extra boost keywords for education-focused papers
- `min_education_hits`: minimum number of education-focus keyword hits required
- `seen_state_path`: local state file to prevent recommending duplicate papers across runs
- `source_limits`: fetch limits per source (`arxiv`, `eric`, `openalex`)
- `source_weights`: source-level score bias (e.g., ERIC higher for education relevance)
- `top_k`: number of selected papers (10)
- `review_top_k`: number of OpenAI-reviewed papers (5)

## 3) Test Run

```powershell
.venv\Scripts\python.exe src\arxiv_agent.py --dry-run
```

## 4) Register 07:00 Daily Task

```powershell
powershell -ExecutionPolicy Bypass -File scripts\register_task.ps1 -TaskName "ArxivDailyAgent" -Time "07:00"
```

Check task:

```powershell
schtasks /Query /TN "ArxivDailyAgent"
```

## 5) Run on GitHub Actions (PC off mode)

Add this repository secrets in GitHub:
- `OPENAI_API_KEY`
- `SMTP_HOST`
- `SMTP_PORT`
- `SMTP_USER`
- `SMTP_PASS`
- `EMAIL_FROM`
- `EMAIL_TO`
- `OPENALEX_EMAIL` (optional but recommended)

Workflow file:
- `.github/workflows/daily.yml`

Schedule note:
- The workflow uses UTC cron.
- `0 22 * * *` means 07:00 KST daily.
