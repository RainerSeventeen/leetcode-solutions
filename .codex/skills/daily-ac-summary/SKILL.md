---
name: daily-ac-summary
description: Use when user asks to run daily LeetCode summary/archive workflow: fetch recent 1-day AC submissions, import them into `solutions/`, then start a subagent to run `solution-topic-auto-link` for this run's solutions.
---

# Daily AC Summary

Execute this workflow for daily synchronization:
1. Run `.venv/bin/python scripts/fetch_ac_submissions.py --days 1` to fetch latest one-day submissions.
2. Run `.venv/bin/python scripts/import_ac_to_solutions.py` to import code/problem metadata into `solutions/`.
3. Start a subagent and apply `solution-topic-auto-link` to all solutions imported in this run.

## Environment

- Execute all Python scripts with the project virtual environment interpreter: `.venv/bin/python`.
- If `.venv/bin/python` does not exist, stop and report that virtual environment is required.

## Workflow

1. Fetch daily submissions:
- Run: `.venv/bin/python scripts/fetch_ac_submissions.py --days 1`
- If fetch fails, stop and report stderr.

2. Import into solutions:
- Run: `.venv/bin/python scripts/import_ac_to_solutions.py`
- Primary source of this-run files: `artifacts/imported_paths.txt`.
- If `artifacts/imported_paths.txt` is empty or missing, treat as "no new solutions imported" and stop topic-linking step.

3. Start subagent for topic linking:
- Read solution paths from `artifacts/imported_paths.txt`.
- Spawn one subagent for topic-linking execution.
- In subagent prompt, explicitly require using skill `solution-topic-auto-link`.
- Pass all imported `solutions/...md` paths and ask it to:
  - insert topic links,
  - create subsection when needed,
  - run `.venv/bin/python scripts/check_solutions.py` and `.venv/bin/python scripts/normalize_topics_title.py`,
  - return changed files and inserted lines.
- Wait for subagent completion.
- If subagent fails, surface failure reason and partial progress.

## Guardrails

- Do not create solution files manually; only use repository scripts.
- Keep import scope to last day by always using `--days 1` in fetch step.
- Prefer `artifacts/imported_paths.txt` over parsing `artifacts/ac_with_code.jsonl` for this-run solution list.
- If user explicitly asks to use `artifacts/ac_with_code.jsonl`, use it as fallback only when `imported_paths.txt` is unavailable.

## Final Report

Include:
- Fetch result summary (records fetched / retry notes if any).
- Imported solution paths for this run.
- Topic files/sections touched by subagent.
- Validation command results.
