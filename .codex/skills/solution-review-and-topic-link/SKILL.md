---
name: solution-review-and-topic-link
description: Use when the user provides a `solutions/...md` file and wants format checks, minimal content improvements, and insertion of a compliant topic link under the right module, with escalation proposal when no suitable module exists.
---

# Solution Review And Topic Link

When the user provides a solution file under `solutions/`, execute this end-to-end workflow:
1. Check and fix format compliance.
2. Add minimal necessary content improvements.
3. Insert a compliant link into the best matching section under `topics/`.

## Scope Trigger

Use this skill when the user asks to process one or more solution files and expects:
- format validation/fix,
- concise quality补充 (complexity or explanation),
- topic mapping + link insertion.

## Workflow

1. Locate and read the target file in `solutions/<range>/<id>-<slug>.md`.

2. Run repository validation:
- Execute `python3 scripts/check_solutions.py`.
- Fix violations related to the target file first.

3. Enforce required solution structure:
- Keep front matter keys: `id`, `title`, `difficulty`, `tags`, `created`.
- Keep required sections:
  - `## 题目链接`
  - `## 题目描述`
  - `## 解题思路`
  - `## 代码`
- Remove placeholders such as `O()` and empty code blocks.

4. Apply minimal necessary补充:
- If missing, add concrete:
  - `- 时间复杂度: ...`
  - `- 空间复杂度: ...`
- If `## 解题思路` is too薄弱, add only concise key logic:
  - state definition,
  - transition/decision point,
  - boundary/initialization.
- Preserve original writing style and language where possible.
- Prefer small edits over rewriting.

5. Map to topic module:
- Search `topics/*.md` for matching methodology/category.
- Prefer existing subcategory blocks ending with `相关题目`.
- Default policy: single ownership (one best topic link only).
- Do not duplicate the same problem link across topics unless user asks.

6. Insert link with strict format:
- Single bullet, exact style:
  - `- 0001 - 题目名 ｜ [LeetCode 链接](https://leetcode.cn/problems/<slug>/) ｜ [题解笔记](../solutions/xxxx-xxxx/0001-<slug>.md)`
- Keep id as 4-digit zero-padded.
- Ensure local relative path is correct from the topic file.
- Insert at semantically correct subsection, not random append.

7. If no suitable topic section exists:
- Do not silently invent final placement.
- Prepare and report a proposal to the user first, including:
  - preferred target file (existing `topics/<name>.md` or a new file),
  - proposed new subsection title (prefer `xxx相关题目` pattern),
  - why current topics are not suitable.
- Wait for confirmation before creating a new topic file or new category block.

8. Re-run `python3 scripts/check_solutions.py` after edits and fix issues.

## Decision Rules

- Minimal-change rule:
  - Only edit what is required for compliance/readability/linking.
- Style-preservation rule:
  - Keep user’s original narrative style; avoid large refactors.
- Single-topic default:
  - Put a problem in one most appropriate topic by default.
- Escalation-before-creation:
  - Any new `topics/*.md` file or new major category must be proposed first.

## Final Report Template

When finishing, include:
- Updated solution file path and what was fixed.
- Updated topic file path and inserted subsection/location.
- If proposed-only (no insertion yet), list proposed file + subsection and rationale.
- Validation result summary from `scripts/check_solutions.py`.
