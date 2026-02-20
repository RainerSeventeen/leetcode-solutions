---
name: topic-to-solutions
description: Use when refactoring a user-specified topic note file (for example `topics/dp.md`) by extracting problem-specific sections (with LeetCode ids) into `solutions/<range>/<id>-<slug>.md`, while keeping only abstract summary content in the original topic file and replacing removed sections with links to solution files.
---

# Topic To Solutions

Refactor the user-provided topic note file (usually under `topics/`) into two layers:
- Keep abstract, reusable methodology in the same topic file.
- Move problem-specific writeups into per-problem files under `solutions/`.

## Workflow

1. Read the user-specified topic file and split content into:
- Abstract summary content (methodology, patterns, reusable templates).
- Problem-specific content (sections with explicit id signals such as `LeetCode <id>`, `LC <id>`, `题号 <id>` plus concrete solution/code).

2. Activate virtual environment before running repository scripts:
- Run `source .venv/bin/activate` from repo root.

3. For every detected id, ensure the target solution file exists:
- Run `python scripts/fetch_problem.py <id>`.
- `solutions/` files must be created by this script first, then edited in-place.
- Never manually create solution markdown files.
- If file already exists, do not overwrite unless the user explicitly requests `--overwrite`.
- Use repo id-range output paths (for example `solutions/0001-0100/`, `solutions/0101-0200/`).
- If script execution is blocked by permission or sandbox limits, request privilege escalation before proceeding.

4. Delegate per-problem fill-in work to a subagent (mandatory):
- Subagent edits each corresponding `solutions/.../<id>-<slug>.md`.
- After generation, migration and completion must be done by subagent, not main agent.
- Subagent migrates problem-specific code/content from topic file to solution file and completes missing template parts.
- Required completion in each solution file:
  - `## 解题思路` concise and clear, written as normal prose paragraphs (not `-` bullet lists).
  - `时间复杂度` and `空间复杂度` with concrete Big-O.
  - Complexity lines should remain list-style bullets (for example `- 时间复杂度: ...`, `- 空间复杂度: ...`).
  - Runnable code in `## 代码` fenced block.
  - Code language rule: do not force Python. If the original topic uses C++ for that problem, keep a `cpp` fenced block in the solution file; preserve original language unless the user explicitly asks to rewrite.

5. After subagent completion, clean the same topic file:
- Remove detailed problem-specific explanation/code for extracted ids.
- Keep only a short reference line for each extracted problem linking to the solution file.
- Use repo-relative links from the topic file, e.g. `../solutions/0001-0100/0070-climbing-stairs.md`.
- Preserve overall article structure and abstract learning notes.
- If abstract categories already exist, place links under corresponding categories, not a centralized index.

## Topic Link Placement and Format (User-Specified)

1. Place links by abstract category:
- Place each extracted problem under the matching abstract methodology category in the same file.
- Example mapping (DP): knapsack -> `背包...`, stock -> `股票...`, sequence/string -> `子序列...`.
- Avoid a separate aggregated index list when category placement is possible.

2. Use section title pattern:
- Any subsection that lists problem links should use the pattern:
  - `xxx相关题目`

3. Follow strict bullet format:
- Every problem entry should be a single bullet in this exact style:
  - `- 0015 - <题目名> ｜ [LeetCode 链接](https://.../) ｜ [题解笔记](./path/to/md.md)`
- Requirements: id is 4-digit zero-padded; include display title; include both official LeetCode link and local solution link; keep local path valid relative to current file.

## Extraction Rules

- Treat a section as problem-specific only when both exist:
  - Explicit problem id signal (`LeetCode <number>`, `LC <number>`, `力扣 <number>`).
  - Concrete solution details tied to that problem (state definition, derivation, or code).
- Keep generalized patterns even if they include tiny illustrative snippets, as long as they do not depend on a specific problem id section.
- If one section contains multiple ids, split and link each id separately when possible.

## Output Quality Checklist

- The topic file keeps abstract methodology and no long code blocks tied to specific ids.
- Every extracted id has exactly one link in the same topic file.
- Every linked solution file contains:
  - `## 解题思路`
  - non-empty complexity bullets
  - non-empty code block
- Run `python scripts/check_solutions.py` when possible and fix format issues before finishing.
