---
name: daily-ac-summary
description: "Use when user asks to run daily LeetCode summary/archive workflow: fetch recent 1-day AC submissions, import them into `solutions/`, fill solution idea/complexity sections from code for this run's files, then start a subagent to run `solution-topic-auto-link`."
---

# Daily AC Summary

## Environment

- Execute all Python scripts with the project virtual environment interpreter: `.venv/bin/python`.
- If `.venv/bin/python` does not exist, stop and report that virtual environment is required.

## Source of truth

- This-run solution list comes from `artifacts/imported_paths.txt`.
- If `artifacts/imported_paths.txt` is missing/empty, treat as "no new solutions imported", skip topic-linking.
- Only if user explicitly requests it, use `artifacts/ac_with_code.jsonl` as fallback when `imported_paths.txt` is unavailable.

## Workflow

1. Fetch daily submissions:
   - Run: `.venv/bin/python scripts/fetch_ac_submissions.py --days 1`
   - Always keep scope to one day (`--days 1`).
   - If fetch fails, stop and report stderr.

2. Import into solutions:
   - Run: `.venv/bin/python scripts/import_ac_to_solutions.py`
   - Use `artifacts/imported_paths.txt` as this-run file list.

3. Fill idea + complexity for imported solutions:
   - For each imported file, parse the code in `## 代码` and fill:
     - `## 解题思路` with a concise, code-consistent explanation,
     - `时间复杂度：$O(xxx)$` and `空间复杂度：$O(xxx)$` with concrete expressions (no placeholders).
   - Keep style concise and consistent with existing solution files.
   - After filling, run `.venv/bin/python scripts/ci/check_solutions.py`.
   - If check fails, fix the imported files and rerun check until pass or a hard blocker is found.
   - If hard blocker remains, stop and report failing files + exact errors.

4. Start subagent for topic linking:
   - Spawn one subagent for topic-linking execution.
   - In the subagent prompt, explicitly require using skill `solution-topic-auto-link`.
   - Pass all imported `solutions/...md` paths and ask it to:
     - insert topic links,
     - create subsection when needed,
     - run `.venv/bin/python scripts/ci/check_solutions.py` and `.venv/bin/python scripts/normalize_topics_title.py`,
     - return changed files and inserted lines.
   - Wait for subagent completion.
   - If subagent fails, surface failure reason and partial progress.

## Guardrails

- Do not create solution files manually; only use repository scripts.
- Never leave placeholders such as `O()` in imported solution files.

## Final Report

Include:
- Fetch result summary (records fetched / retry notes if any).
- Imported solution paths for this run.
- Idea/complexity fill result (files updated, complexity expressions added).
- Topic files/sections touched by subagent.
- Validation command results.
