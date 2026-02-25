---
name: daily-ac-summary
description: "Use when user asks to run the daily LeetCode AC archive workflow."
---

# Daily AC Summary

## Environment

- Use `.venv/bin/python` for all Python scripts.
- If `.venv/bin/python` is missing, stop and report that virtual environment is required.

## Source of truth

- This-run solution list is `artifacts/imported_paths.txt`.
- If it is missing/empty, treat as "no new solutions imported" and skip topic-linking.
- Use `artifacts/ac_with_code.jsonl` as fallback only when the user explicitly requests it.

## Workflow

1. Fetch daily submissions:
   - Run: `.venv/bin/python scripts/fetch_ac_submissions.py --days 1 --keep-per-problem 0`
   - If fetch fails, stop and report stderr.

2. Import into solutions:
   - Run: `.venv/bin/python scripts/import_ac_to_solutions.py`
   - Import is append/import-only: keep AC code blocks as collected; do not dedupe by method here.

3. Start subagent A for solution quality ranking + rewrite:
   - Spawn one subagent dedicated to imported `solutions/...md` files and explicitly require skill `solution-quality-ranker`.
   - Pass all imported solution paths as input.
   - Require structured return per file:
     - whether blocks were reordered,
     - kept variants / filtered same-method count,
     - whether latest submission is not best,
     - whether all AC are non-optimal,
     - complexity fill result.
   - Wait for subagent completion.
   - If subagent fails, surface failure reason and partial progress.

4. Start subagent B for topic linking:
   - Spawn one subagent and explicitly require skill `solution-topic-auto-link`.
   - Pass all imported `solutions/...md` paths as input.
   - Require return of touched topic files/sections and inserted topic lines/backlink changes.
   - Explicitly request normalization in subagent prompt: run `.venv/bin/python scripts/normalize_topics.py`.
   - Topic subagent runs after subagent A completes (avoid concurrent writes on the same solution files).
   - Wait for subagent completion.
   - If subagent fails, surface failure reason and partial progress.

5. Final validation:
   - Run `.venv/bin/python scripts/ci/ci.py`.
   - If format errors are reported, fix affected files and rerun once.
   - If errors remain, stop and report failing files with exact errors.

## Guardrails

- Do not create solution files manually; only use repository scripts.
- Never leave placeholders such as `O()` in imported solution files.

## Final Report

Include:
- Fetch result summary (records fetched / retry notes if any).
- Imported solution paths for this run.
- Subagent A result:
  - multi-submission merge result (kept variants / same-method filtered count),
  - solution ranking/reorder result,
  - idea/complexity fill result,
  - latest-not-best report,
  - problem-level optimality report (`all AC non-optimal` list).
- Subagent B result:
  - topic files/sections touched,
  - inserted topic lines / backlink changes.
- Validation command results.
