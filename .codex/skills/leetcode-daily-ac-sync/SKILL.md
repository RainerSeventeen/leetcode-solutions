---
name: leetcode-daily-ac-sync
description: Sync a LeetCode user's AC submissions of today (starting at Beijing time) into repository notes. Use when the user asks to read username from USER_ID.txt, fetch today's AC problems and submitted code via LeetCode MCP, generate solution files through scripts/fetch_problem.py, fill `## 解题思路` and complexity, then link notes into suitable sections under topics/.
---

# LeetCode Daily AC Sync

Execute this workflow to convert today's LeetCode AC submissions into repo notes and topic links.

## Orchestration Model

Use one main agent with two subagents:
- `subagent-data`: collect AC data and generate note skeleton files.
- `subagent-content`: merge code and thinking text, then update topics and run checks.

Run stages in order: `subagent-data` -> `subagent-content`.

## Stage A: subagent-data

1. Read username from `USER_ID.txt`.
- Trim whitespace.
- If `USER_ID.txt` is missing or empty, ask the user for username, then suggest saving it into `USER_ID.txt` for future runs.

2. Query LeetCode MCP for recent AC submissions.
- Filter records to today's date in Beijing time (`Asia/Shanghai`, UTC+8).
- Deduplicate by problem; keep the latest accepted submission for each problem.
- Retrieve submitted code for each selected AC record.
- If MCP cannot provide code for a record, mark it as `code_unavailable` and continue.

3. Generate or update solution files with existing script.
- Call `python3 scripts/fetch_problem.py <problem_id>` for each selected problem.
- Do not create files under `solutions/` manually.

4. Write normalized artifact for handoff.
- Create `artifacts/today_ac_bundle.json` with fields:
  - `username`
  - `date_bj` (`YYYY-MM-DD`)
  - `problems[]`: `id`, `title`, `title_slug`, `submit_time_bj`, `submission_id`, `solution_path`, `code`, `code_unavailable`

## Stage B: subagent-content

1. Update each `solutions/*.md` from the bundle.
- Fill `## 代码` with the user's code block.
- Fill `## 解题思路` with concise method explanation.
- Add complexity lines in `$O(x)$` style.

2. Respect repository rules.
- Follow `.ai_docs/rules.md`.
- Preserve front matter and required section structure.

3. Link problems into `topics/`.
- Place each problem in the best matching topic subsection.
- Reuse the `solution-topic-auto-link` skill workflow when available.

4. Validate and normalize.
- Run `python3 scripts/check_solutions.py`.
- Run `python3 scripts/normalize_topics_title.py`.
- Include normalization edits.

## Failure Policy

- Continue on single-problem failure and record failures.
- Hard-stop only when prerequisites fail: missing username, MCP unavailable, or zero AC records for target day.

## Final Report Template

Report:
- `username` and `date_bj`
- processed problem count
- skipped/failure list with reason
- updated solution paths
- updated topic files
- validation command results
