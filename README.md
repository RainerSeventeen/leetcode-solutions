# LeetCode Solutions

个人 LeetCode 算法知识库

以 Markdown 文件管理题解，使用 Python 脚本实现从力扣平台批量拉取、导入、校验的自动化流程

使用配合 Agent  Skills 完成解题思路归纳, 知识链接

## 特性

- **自动拉取**：从力扣 CN 批量获取个人 AC 提交记录（含代码），支持断点续传与限流退避
- **自动导入**：将 AC 记录转换为标准 Markdown 题解模板，自动填充题目描述、标签、难度
- **格式校验**：CI 自动校验 `solutions/*.md` 与 `topics/*.md` 规则，确保知识库质量
- **专题归纳**：`topics/` 目录存放算法专题笔记，通过跨题链接构建知识体系

## 算法分类

> 分类方案主要参考灵神的[《如何科学刷题？》](https://leetcode.cn/discuss/post/3141566/ru-he-ke-xue-shua-ti-by-endlesscheng-q3yd/), 也加入了一些 《代码随想录》的内容

1. [滑动窗口与双指针（定长/不定长/单序列/双序列/三指针/分组循环）](topics/sliding-window-and-two-pointers.md)

2. [二分算法（二分答案/最小化最大值/最大化最小值/第K小）](topics/binary-search.md)

3. [单调栈（基础/矩形面积/贡献法/最小字典序）](topics/monotonic-stack.md)

4. [网格图（DFS/BFS/综合应用）](topics/grid-graph.md)

5. [位运算（基础/性质/拆位/试填/恒等式/思维）](topics/bit-operations.md)

6. [图论算法（DFS/BFS/拓扑排序/基环树/最短路/最小生成树/网络流）](topics/graph-algorithms.md)

7. [动态规划（入门/背包/划分/状态机/区间/状压/数位/数据结构优化/树形/博弈/概率期望）](topics/dynamic-programming.md)

8. [常用数据结构（枚举技巧/前缀和/差分/栈/队列/堆/字典树/并查集/树状数组/线段树）](topics/common-data-structures.md)

9. [数学算法（数论/组合/概率期望/博弈/计算几何/随机算法）](topics/math-algorithms.md)

10. [贪心与思维（基本贪心策略/反悔/区间/字典序/数学/思维/脑筋急转弯/构造）](topics/greedy-and-thinking.md)

11. [链表、树与回溯（前后指针/快慢指针/DFS/BFS/直径/LCA）](topics/linked-list-tree-backtracking.md)

12. [字符串（KMP/Z函数/Manacher/字符串哈希/AC自动机/后缀数组/子序列自动机）](topics/string-algorithms.md)

## 目录结构

```
.
├── solutions/              # 题解，按题号每 100 题一段
│   ├── 0001-0100/
│   │   └── 0001-two-sum.md
│   ├── 0101-0200/
│   └── ...
├── topics/                 # 算法专题笔记
│   ├── dynamic-programming.md
│   └── ...
├── scripts/                # Python 工具脚本
│   ├── fetch_problem.py
│   ├── fetch_ac_submissions.py
│   ├── filter_ac_with_code.py
│   ├── import_ac_to_solutions.py
│   ├── normalize_topics_title.py
│   └── ci/
│       ├── check_solutions.py
│       ├── check_topics.py
│       └── ci.py
├── artifacts/              # 脚本中间产物（自动生成，不手写）
│   ├── ac_with_code.jsonl
│   └── imported_paths.txt
└── .github/workflows/
    └── solutions-check.yml
```

## 快速开始

> 如果你想从零搭建属于自己的知识库, 建议 fork 一份到自己的仓库, 然后删除 solutions/ 下所有内容
> 
> 同时删除 topics/ 下结构中的链接(如果想完全从零写 topics 也可以全删了)
> 
> 随后开始使用脚本自动化拉取题目 + AC 代码
### 环境准备

```bash
pip install requests
```

### 配置鉴权 (用于获取具体的提交代码)

> [!WARNING]
> 不要泄露你的 cookies（`LEETCODE_SESSION` / `csrftoken`），也不要把它们提交到 Git 仓库、截图或发到聊天记录中。


从浏览器打开 LeetCode F12 进入开发者模式

DevTools → Application → Cookies → `leetcode.cn` 

获取两个 Cookies: `LEETCODE_SESSION`, `csrftoken`

![](./asset/cookies.png)

```bash
cp .env.example .env
# 编辑 .env，填入以下两个字段：
# LC_SESSION=xxx # 原名 LEETCODE_SESSION
# LC_CSRF=xxx   # 原名 csrftoken
```

> `fetch_problem.py` 拉取公开题目信息，**不需要**鉴权。

## 使用方法

### 手动归档单题

```bash
# 1. 按题号生成模板（普通题）
python scripts/fetch_problem.py 1584

# 1. 竞赛题或已知 slug 时，直接指定 slug（跳过 problems/all 查找）
python scripts/fetch_problem.py --slug count-sequences-with-given-sum

# 2. 手写解题思路 + 检查
python scripts/ci/check_solutions.py

# 3. (可选) 使用 skill 执行 link 以及扩充工作
```

### 从 AC 记录批量导入

```bash
# 1. 拉取个人 AC 提交（需 .env 鉴权）
python scripts/fetch_ac_submissions.py

# 2. 导入到题解库
python scripts/import_ac_to_solutions.py

# 3. (可选) 使用 skill 执行 link 以及扩充工作
```

### 脚本说明

| 脚本 | 说明 |
|------|------|
| `fetch_problem.py <题号>` / `--slug` | 按题号或 slug 拉取单题，生成 Markdown 模板（竞赛题用 `--slug`） |
| `fetch_ac_submissions.py` | 批量拉取 AC 提交，写入 `artifacts/ac_with_code.jsonl` |
| `filter_ac_with_code.py` | 从 JSONL 中删除已归档到 `solutions/` 的题目 |
| `import_ac_to_solutions.py` | 将 JSONL 中未归档的题目批量导入 `solutions/` |
| `scripts/ci/check_solutions.py` | 仅检查 `solutions/*.md` 规则 |
| `scripts/ci/check_topics.py` | 仅检查 `topics/*.md` 规则（含重复题号） |
| `scripts/ci/ci.py` | CI 总入口（串行执行 solutions + topics 检查） |

### skill 说明

仓库内置的自动化 skill 位于 `.codex/skills/`，当前有以下两个：

#### 1) `daily-ac-summary`: 适用于全流程自动化
  - 拉取最近 1 天 AC 提交, 并自动导入到 `solutions/` 模板中,
  - 自动补齐本次新导入题解的 `## 解题思路`、时间复杂度、空间复杂度
  - 拉起子 agent 执行 `solution-topic-auto-link`，把新题挂到 `topics/`
#### 2) `solution-topic-auto-link`: 单题链接工作
  - 读取指定 `solutions/...md` 文件，按题目方法归类到合适的 `topics/*.md`
  - 若现有小节不匹配，在对应专题下新建 `### 子方法 ...`
  - 在题解文件的 `## 相关专题` 中写入回链接，与 topics 双向绑定
  - 插入规范化条目，并执行校验与标题规范化

#### 推荐使用顺序

1. 日常归档：优先用 `daily-ac-summary`（包含 topic 自动链接）。
2. 单独补某个题目：用 `solution-topic-auto-link`（输入一个或多个 `solutions/...md` 路径）。
