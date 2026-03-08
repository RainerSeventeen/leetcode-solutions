# 撰写规则

> 下面所有 python 都在虚拟环境下运行

## `solutions/*.md` 规则
1. `solutions` 下的文件不允许自行创建，必须调用 `scripts/fetch_problem.py` 脚本创建。
2. `## 解题思路` 需要简要介绍代码用到的方法。
3. 复杂度内容必须使用 `$O(x)$` 这种格式；可在同一行追加说明文本（如 `m 代表边数, n 代表节点数`），建议对出现的变量补充含义。
4. `solutions` 与 `topics` 的关系约束：
   - `solution -> topics` 允许多对多（一个 solution 可以在 `## 相关专题` 中链接多个 topic）。
   - `topics -> solution` 作为专题侧单向映射维护，不要求因 solution 的回链自动反向补录到 topics。

## `topics/*.md` 结构与格式

### 1. 结构基线
1. `topics/*.md` 的章节架构应优先对齐同名 `0x3f_problems_list/*.md` 文档（例如 `topics/dynamic-programming.md` 对齐 `0x3f_problems_list/dynamic-programming.md`）。
2. 对齐的是“分类与层级结构”，不是原文逐字搬运：可结合仓库实际题解覆盖情况做裁剪。
3. `## 概览 / ## 核心思想 / ## 解题流程` 这类通用段落可以保留，但不再作为所有专题的强制固定骨架。

### 2. 标题与编号规则
1. 标题使用语义化文本，不手写 `4.1 / 4.1.1` 等数字编号。
2. 如需统一编号，仅通过 `scripts/normalize_topics.py` 自动处理。
3. 允许保留 `0x3f` 风格章节名（如“零、常用枚举技巧”“专题：XXX”），但应避免同一文件内混用多套命名风格。

### 3. 模板区块建议
1. 子章节下建议按以下顺序组织：`模板：` → 代码块 → `模板题目：` → 题目条目。
2. `模板题目` 可以用段落标题（`模板题目：`）或小节标题（如 `#### 模板题目`）表达，但同一文件内应尽量统一。
3. 若某小节暂无内容，可写 `待补充...`，但不允许伪造占位链接。

### 4. 题目条目固定格式
题目条目统一写成：

- `- 0000 - 题目名 ｜ [LeetCode 链接](https://leetcode.cn/problems/xxx/) ｜ [题解笔记](../solutions/xxxx-xxxx/xxxx-slug.md)`

约束：
1. `id` 固定 4 位数字（不足补零）。
2. `题解笔记` 路径必须指向实际存在的 `solutions/*.md` 文件，不允许保留占位符路径。
3. `题目名` 必须与对应 `solutions/*.md` 的 H1 中文标题一致。
4. `LeetCode` 链接必须与 `题解笔记` 文件名中的 slug 一致。
5. 同一题号不能在全量 `topics/*.md` 中重复出现。
6. 归档到 `topics` 时，优先按题号查询 `0x3f` 索引：
   - 先执行 `python scripts/query_0x3f_index.py <id>`。
   - 若命中，按查询结果对应的专题与分类位置归档。
   - 若未命中，再按题目方法自行选择归档位置。
7. 若归档过程中新增了分区/子分区（如新增 `###`/`####` 小节），必须在变更汇报中显式说明。

## 检验与自动化
1. `solutions` / `topics` 常规变更必须通过 `scripts/ci/ci.py` 校验。
2. `topics` 相关变更需要通过 `scripts/ci/check_topics.py`。
3. 若改动涉及 `solutions/competition_problems/`，还需关注 `scripts/ci/check_competition_promotions.py` 是否提示迁移。
4. 需要核对题号与中文标题时，可执行 `scripts/ci/check_id_integrity.py`。
5. 撰写完成后建议执行 `scripts/normalize_topics.py` 做标题与空行规范化。
