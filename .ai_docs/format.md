# 文件格式规范

## solutions 题解格式

### 路径规则

`solutions/<低-高>/<题号四位>-<slug>.md`
- 例：`solutions/0001-0100/0001-two-sum.md`
- 目录范围按每 100 题一段，如 `0001-0100`、`0101-0200`
- **不允许手动创建**，必须通过 `scripts/fetch_problem.py` 生成

### Front Matter

```yaml
---
id: 1                    # LeetCode 真实题号（与文件名一致）
title: Two Sum           # 英文标题（来自 API）
difficulty: Easy         # Easy | Medium | Hard
tags: [array, hash-table]
created: 2026-02-20      # YYYY-MM-DD
---
```

### 必须包含的五个 Section

```markdown
## 题目链接
## 题目描述
## 解题思路   ← 须含时间/空间复杂度，格式：$O(n)$，可在后面追加说明文本，不能留 $O()$ 占位符
## 相关专题   ← 至少一条回链接，格式见下方
## 代码       ← 代码块语言标签必须正确（如 ```python）
```

> **CI 校验规则**（`scripts/ci/check_solutions.py`）：
> - 文件路径/名格式合法
> - Front matter 五个 key 均存在且非空
> - `id` 与文件名题号、H1 标题题号三者一致；全库 `id` 不得重复
> - `difficulty` 只能是 `Easy / Medium / Hard`
> - `created` 是合法的 `YYYY-MM-DD`
> - 包含全部五个必需 section
> - `## 解题思路` 不含占位符 `O()`，时/空复杂度格式以 `$O(...)$` 开头（后面可追加说明文本）
> - `## 相关专题` 至少含一条回链接，链接格式与显示名须符合规范

### ## 相关专题 格式

每条回链接独占一行，显示名为 README 专题章节名（**去掉中文括号内容**）：

```markdown
## 相关专题
- [贪心与思维](../../topics/greedy-and-thinking.md)
- [动态规划](../../topics/dynamic-programming.md)
```

映射约束：
- `solution -> topics` 可多条回链（一个 solution 可以对应多个 topics）。
- `topics -> solution` 按专题侧单向维护，不因 solution 回链自动反向新增题目条目。

| 文件 | 显示名 |
|---|---|
| `sliding-window-and-two-pointers.md` | 滑动窗口与双指针 |
| `binary-search.md` | 二分算法 |
| `monotonic-stack.md` | 单调栈 |
| `grid-graph.md` | 网格图 |
| `bit-operations.md` | 位运算 |
| `graph-algorithms.md` | 图论算法 |
| `dynamic-programming.md` | 动态规划 |
| `common-data-structures.md` | 常用数据结构 |
| `math-algorithms.md` | 数学算法 |
| `greedy-and-thinking.md` | 贪心与思维 |
| `linked-list-tree-backtracking.md` | 链表、树与回溯 |
| `string-algorithms.md` | 字符串 |

---

## topics 专题笔记格式

### 文件命名

`topics/<kebab-case-专题名>.md`，并与 `0x3f_problems_list/<同名文件>.md` 对齐章节结构。

### 结构规则

1. 以 `0x3f_problems_list` 的同名文档为结构参考，优先对齐“一级分类/二级分类”层次。
2. 不要求照搬原文叙述，可根据仓库题解覆盖情况保留、合并或标注 `待补充...`。
3. 标题以语义化命名为主，手工不写编号；若需要编号，交由 `scripts/normalize_topics.py` 自动维护。

### 子章节推荐最小结构

每个承载题目链接的子章节，建议包含：

模板：

```python
...
```

模板题目：
- 0000 - 题目中文名 ｜ [LeetCode 链接](https://leetcode.cn/problems/xxx/) ｜ [题解笔记](../solutions/xxxx-xxxx/xxxx-slug.md)


题目条目硬约束（由 `scripts/ci/check_topics.py` 校验）：
- `id` 固定 4 位数字（不足补零）
- `LeetCode` 链接需与 `题解笔记` 文件名 slug 一致
- `题解笔记` 路径必须存在
- `题目中文名` 与题解文件 H1 标题一致
- 同一题号不得跨 `topics/*.md` 重复
- `0x3f` 标题覆盖：同名 `0x3f` 题单要求的分类标题可新增但不可缺失
- 分类一致性：若某题在 `topics` 中出现且该题在对应 `0x3f` 题单中存在，则归档分类位置必须与 `0x3f` 索引一致

`check_topics` 依赖静态索引文件 `0x3f_problems_list/index.json`。如索引不存在或 0x3f 基准更新，先执行：

```bash
python scripts/build_0x3f_index.py
```

### 格式化

撰写或修改完成后执行：
```bash
python scripts/normalize_topics.py
```
该脚本会统一处理标题编号（可选）并确保非代码块中“冒号结尾行”后有一个真正空行。
