---
name: solution-topic-auto-link
description: Use when the user gives one or more `solutions/...md` files and asks to add each problem into a suitable section under `topics/` based on problem nature (algorithm/data-structure pattern), creating a new section when none fits, while strictly following `.ai_docs/rules.md`.
---

# Solution Topic Auto Link

## Environment

- Use `.venv/bin/python` for Python scripts.
- If `.venv/bin/python` is missing, stop and report that virtual environment is required.

## Hard Rules

- Do not create files under `solutions/`; they must come from `scripts/fetch_problem.py`.
- Keep complexity format as `$O(x)$` if edited.
- A solution is mapped to **one** topic section by default. Map to **two** only when the problem genuinely requires two distinct algorithmic ideas as co-primary techniques (e.g., binary search + DP); never more than two.
- Do not create new `topics/*.md` files unless the user explicitly asks.
- Topic titles are normalized by script; do not manually enforce numbering style.

## Workflow

1. **Parse solution metadata**
   - Extract `id`, `title`, and slug URL from `## 题目链接`.
   - Confirm relative note path for the topic bullet.

2. **Determine best topic placement**
   - Search existing topic files (`binary-search.md`, `dynamic-programming.md`, `graph-algorithms.md`, `sliding-window-and-two-pointers.md`, etc.).
   - Inside a topic file, prefer `## 模板与子方法` → most suitable `### 子方法 ...` block.
   - Match by method keywords (双指针, 二分, 动态规划, 图论, 回溯, 贪心, 前缀和, 单调栈/队列, 滑动窗口, 并查集, 最短路, 拓扑排序, 树形 DP, …).
   - If the problem co-equally involves two techniques, select two sections (one per topic file at most).

3. **Create subsection when needed**
   - If no suitable `### 子方法` block exists, create a concise new one under `## 模板与子方法`.

4. **Insert topic bullet** (exact format required)
   ```
   - 0000 - 题目名 ｜ [LeetCode 链接](https://leetcode.cn/problems/xxx/) ｜ [题解笔记](../solutions/xxxx-xxxx/xxxx-slug.md)
   ```
   - Zero-padded 4-digit id; full-width `｜`; leetcode.cn URL with trailing slash.
   - In `#### 模板题目` entries, `题目名` must use Chinese.
   - Avoid duplicate entries; preserve id-sorted order where present.

5. **Sync solution backlink**
   - Ensure `## 相关专题` section exists in the solution file.
   - Add one backlink per mapped topic (one or two, matching step 2).
   - Avoid duplicate backlink lines.
   - Backlink format: `- [专题显示名](../../topics/xxx.md)`
   - `专题显示名` follows README topic name convention (remove Chinese parenthetical text).

6. **Normalize (when caller requests)**
   - If caller explicitly requests normalization, run `.venv/bin/python scripts/normalize_topics.py`.
   - Do not run full repository CI by default; final validation should be handled by the orchestrating workflow.

## Final Output

Report:
- Processed solution path(s).
- Topic file(s) and section(s) used/created.
- Exact inserted topic line(s).
- Backlink changes: solution files where `## 相关专题` was added or updated, with the exact lines inserted.
- Normalization result (if executed).
