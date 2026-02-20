---
name: solution-topic-auto-link
description: Use when the user gives one or more `solutions/...md` files and asks to add each problem into a suitable section under `topics/` based on problem nature (algorithm/data-structure pattern), creating a new section when none fits, while strictly following `.ai_docs/rules.md`.
---

# Solution Topic Auto Link

Execute this workflow when processing solution files for topic mapping:
1. Read target solution file(s) under `solutions/`.
2. Infer problem nature from title, tags, and solution approach.
3. Insert a compliant item into the best matching topic section.
4. Create a new section when none fits.
5. Run required validation/normalization commands.

## Hard Rules

Follow `.ai_docs/rules.md` strictly:
- Do not create files under `solutions/`; they must come from `scripts/fetch_problem.py`.
- Keep complexity format as `$O(x)$` if edited.
- Topic bullet format must be exactly:
  - `- 0000 - 题目名 ｜ [LeetCode 链接](https://leetcode.cn/problems/xxx/) ｜ [题解笔记](../solutions/xxxx-xxxx/xxxx-slug.md)`
- After topic edits, run:
  - `python3 scripts/check_solutions.py`
  - `python3 scripts/normalize_topics_title.py`

## Workflow

1. Parse solution metadata:
- Extract `id`, `title`, and slug URL from `## 题目链接`.
- Confirm note path for topic bullet.

2. Determine best topic placement:
- Search `topics/*.md` for matching method keywords (e.g., 双指针, 二分, 动态规划, 图论, 回溯, 贪心, 前缀和, 单调栈/队列, 滑动窗口, 并查集, 最短路, 拓扑排序, 树形 DP).
- Prefer existing `xxx相关题目` sections.
- Default to single ownership (one best section) unless user asks for multi-topic mapping.

3. Create section when needed:
- If no suitable section exists, create a concise new section in the most relevant existing topic file.
- Section naming style: plain title without numbering/prefix, prefer `xxx相关题目`.
- Place near semantically related sections.

4. Insert item with strict format:
- Use zero-padded 4-digit id.
- Keep full-width separator `｜`.
- Use leetcode.cn URL with trailing slash.
- Use correct relative note path.

5. De-dup and ordering:
- Avoid duplicate problem entries in same section/file.
- If section is id-sorted, keep sorting; otherwise follow local list style.

6. Validate and normalize:
- Run `python3 scripts/check_solutions.py`.
- Run `python3 scripts/normalize_topics_title.py`.
- Include normalization changes if produced.

## Final Output Template

Report:
- Processed solution path(s).
- Topic file and section used/created.
- Exact inserted topic line(s).
- Validation results.
