---
name: daily-ac-summary
description: "Use when user asks to run daily LeetCode summary/archive workflow: fetch recent 1-day AC submissions, import them into `solutions/`, fill solution idea/complexity sections from code for this run's files, then start a subagent to run `solution-topic-auto-link`."
---

# Daily AC Summary

Execute this workflow for daily synchronization:
1. Run `.venv/bin/python scripts/fetch_ac_submissions.py --days 1` to fetch latest one-day submissions.
2. Run `.venv/bin/python scripts/import_ac_to_solutions.py` to import code/problem metadata into `solutions/`.
3. Fill `## 解题思路` and complexity fields in imported solutions based on the `## 代码` section.
4. Start a subagent and apply `solution-topic-auto-link` to all solutions imported in this run.

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
   - If `artifacts/imported_paths.txt` is empty or missing, treat as "no new solutions imported" and skip the topic-linking step.

3. Fill idea + complexity for imported solutions:
   - Read solution paths from `artifacts/imported_paths.txt`.
   - For each imported file, parse the code in `## 代码` and fill:
     - `## 解题思路` with a concise, code-consistent explanation,
     - `时间复杂度：$O(xxx)$` and `空间复杂度：$O(xxx)$` with concrete expressions (no placeholders).
   - Keep style concise and consistent with existing solution files.
   - After filling, run `.venv/bin/python scripts/check_solutions.py`.
   - If check fails, fix the imported files and rerun check until pass or a hard blocker is found.
   - If hard blocker remains, stop and report failing files + exact errors.

4. Start subagent for topic linking:
   - Read solution paths from `artifacts/imported_paths.txt`.
   - Spawn one subagent for topic-linking execution.
   - In the subagent prompt, explicitly require using skill `solution-topic-auto-link`.
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
- Never leave placeholders such as `O()` in imported solution files.

## Final Report

Include:
- Fetch result summary (records fetched / retry notes if any).
- Imported solution paths for this run.
- Idea/complexity fill result (files updated, complexity expressions added).
- Topic files/sections touched by subagent.
- Validation command results.
