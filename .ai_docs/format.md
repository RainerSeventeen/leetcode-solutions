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
## 解题思路   ← 须含时间/空间复杂度，格式：$O(n)$，不能留 $O()$ 占位符
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
> - `## 解题思路` 不含占位符 `O()`，时/空复杂度格式为 `$O(...)$`
> - `## 相关专题` 至少含一条回链接，链接格式与显示名须符合规范

### ## 相关专题 格式

每条回链接独占一行，显示名为 README 专题章节名（**去掉中文括号内容**）：

```markdown
## 相关专题
- [贪心与思维](../../topics/greedy-and-thinking.md)
- [动态规划](../../topics/dynamic-programming.md)
```

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

`topics/<kebab-case-专题名>.md`，例：`dynamic-programming.md`、`binary-search.md`

### 整体骨架

每个文件统一分四个顶层章节，章节前有数字编号：

```markdown
# 专题名称

## 1 概览
简要说明该专题的适用场景与核心价值（2-4 句）。

## 2 核心思想
- 要点一
- 要点二

## 3 解题流程
1. 步骤一
2. 步骤二

## 4 模板与子方法
### 4.1 子方法名（语义化名称，如"右侧第一个更大元素"）
方法说明：
...

模板代码：
```python
...
```

#### 4.1.1 模板题目
- 0000 - 题目中文名 ｜ [LeetCode 链接](https://leetcode.cn/problems/xxx/) ｜ [题解笔记](../solutions/xxxx-xxxx/xxxx-slug.md)
```

题目条目约束：`id` 固定 4 位数字（不足补零）；题目名用中文；`题解笔记` 路径须指向真实文件，不允许占位符；同一题号不得跨 topics 文件重复。

### 格式化

撰写或修改完成后执行：
```bash
python scripts/normalize_topics_title.py
```
