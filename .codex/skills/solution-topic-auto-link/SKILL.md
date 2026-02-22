---
name: solution-topic-auto-link
description: Use when the user gives one or more `solutions/...md` files and asks to add each problem into a suitable section under `topics/` based on problem nature (algorithm/data-structure pattern), creating a new section when none fits, while strictly following `.ai_docs/rules.md`.
---

# Solution Topic Auto Link

Execute this workflow when processing solution files for topic mapping:
1. Read target solution file(s) under `solutions/`.
2. Infer problem nature from title, tags, and solution approach.
3. Insert a compliant item into the best matching topic section.
4. Create a new subsection when none fits.
5. Run required validation/normalization commands.

## Hard Rules

Follow `.ai_docs/rules.md` strictly:
- Do not create files under `solutions/`; they must come from `scripts/fetch_problem.py`.
- Keep complexity format as `$O(x)$` if edited.
- Each solution can be linked to exactly one topic section only. Never add the same problem to multiple sections/files in one run.
- When a topic bullet is added/updated, sync backlink in the same `solutions/...md`:
  - Ensure `## 相关专题` exists.
  - Ensure exactly one backlink to the selected topic file in this run (single ownership).
  - Backlink format must be exactly `- [专题显示名](../../topics/xxx.md)`.
  - `专题显示名` must match README topic name convention (remove Chinese parenthetical text).
- Topic bullet format must be exactly:
  - `- 0000 - 题目名 ｜ [LeetCode 链接](https://leetcode.cn/problems/xxx/) ｜ [题解笔记](../solutions/xxxx-xxxx/xxxx-slug.md)`
- In `#### 模板题目` entries, `题目名` must use Chinese.
- After topic edits, run:
  - `python3 scripts/ci/check_solutions.py`
  - `python3 scripts/normalize_topics_title.py`

## Workflow

1. Parse solution metadata:
- Extract `id`, `title`, and slug URL from `## 题目链接`.
- Confirm note path for topic bullet.

2. Determine best topic placement:
- Search existing topic files first (current structure uses fixed topic files such as `binary-search.md`, `dynamic-programming.md`, `graph-algorithms.md`, `sliding-window-and-two-pointers.md`).
- Inside a topic file, prefer placement under `## 模板与子方法` and then the most suitable `### 子方法 ...` block.
- Match by method keywords (e.g., 双指针, 二分, 动态规划, 图论, 回溯, 贪心, 前缀和, 单调栈/队列, 滑动窗口, 并查集, 最短路, 拓扑排序, 树形 DP).
- Default to single ownership (one best section) unless user asks for multi-topic mapping.

3. Create subsection when needed:
- If no suitable `### 子方法` block exists, create one concise new `### 子方法 ...` block under the target topic file's `## 模板与子方法`.
- Do not create new `topics/*.md` files unless the user explicitly asks.
- Follow `.ai_docs/rules.md`: topic titles should be normalized by script, so do not manually enforce numbering style; always run normalization command after edits.

4. Insert item with strict format:
- Use zero-padded 4-digit id.
- Keep full-width separator `｜`.
- Use leetcode.cn URL with trailing slash.
- Use correct relative note path.

5. Sync solution backlink:
- In the processed solution file, update `## 相关专题` to include backlink to the selected topic.
- Keep one topic backlink per solution in this workflow (consistent with single ownership).
- Avoid duplicate backlink lines.
- Follow `.ai_docs/format.md` display-name mapping (README topic name, remove Chinese parenthetical text).

6. De-dup and ordering:
- Avoid duplicate problem entries in same section/file.
- If section is id-sorted, keep sorting; otherwise follow local list style.

7. Validate and normalize:
- Run `python3 scripts/ci/check_solutions.py`.
- Run `python3 scripts/normalize_topics_title.py`.
- If many solution backlinks are inconsistent, optionally run `python3 scripts/backlink_solutions.py` and include resulting changes.
- Include normalization changes if produced.

## Final Output Template

Report:
- Processed solution path(s).
- Topic file and section used/created.
- Exact inserted topic line(s).
- Validation results.
