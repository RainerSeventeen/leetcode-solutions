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

### 必须包含的四个 Section

```markdown
## 题目链接
## 题目描述
## 解题思路   ← 须含时间/空间复杂度，格式：$O(n)$，不能留 $O()$ 占位符
## 代码       ← 代码块语言标签必须正确（如 ```python）
```

### CI 校验规则（`scripts/ci/check_solutions.py`）

- 文件路径/名格式合法
- Front matter 四个 key 均存在且非空
- `id` 与文件名题号、H1 标题题号三者一致
- `difficulty` 只能是 `Easy / Medium / Hard`
- `created` 是合法的 `YYYY-MM-DD`
- 包含全部四个必需 Section
- 不含占位符 `O()`
- 无重复 `id`

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
- ...

## 3 解题流程
1. 步骤一
2. 步骤二
3. ...

## 4 模板与子方法
### 4.1 子方法名
方法说明：
...

模板代码：
```python
...
```

#### 4.1.1 模板题目
- 0000 - 题目中文名 ｜ [LeetCode 链接](https://leetcode.cn/problems/xxx/) ｜ [题解笔记](../solutions/xxxx-xxxx/xxxx-slug.md)
```

### 子方法（`###`）规则

- 命名直接用语义化名称，如 `### 4.1 右侧第一个更大元素`，不写"子方法 A/B/C"
- 每个子方法包含三部分：**方法说明**、**模板代码**（代码块）、**`#### x.x.x 模板题目`**（题目列表）
- 不同子方法的题目不要混放，边界要清晰

### 题目条目格式

```
- 0000 - 题目中文名 ｜ [LeetCode 链接](https://leetcode.cn/problems/xxx/) ｜ [题解笔记](../solutions/xxxx-xxxx/xxxx-slug.md)
```

约束：
- `id` 固定 4 位数字（不足补零）
- 题目名使用中文
- `题解笔记` 路径必须指向实际存在的文件，不允许占位符

### CI 校验规则（`scripts/ci/check_topics.py`）

- 同一题号在全部 `topics/*.md` 中出现两次及以上视为失败，输出重复题号清单

### 格式化

撰写或修改完成后执行：
```bash
python scripts/normalize_topics_title.py
```
