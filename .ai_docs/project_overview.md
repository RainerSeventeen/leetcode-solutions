# 项目概览

个人 LeetCode 算法知识库，以 Markdown 文件管理题解，配套 Python 脚本实现从力扣平台批量拉取、导入、校验的自动化流程。

---

## 目录结构

```
.
├── solutions/          # 题解，按题号分段目录
│   ├── 0001-0100/
│   │   └── 0001-two-sum.md
│   ├── 0101-0200/
│   └── ...
├── topics/             # 算法专题笔记（Markdown）
│   ├── dynamic-programming.md
│   ├── graph-algorithms.md
│   └── ...
├── scripts/            # Python 工具脚本
│   ├── ci/
│   │   ├── check_solutions.py  # solutions 规则检查
│   │   ├── check_topics.py     # topics 规则检查（含重复题号）
│   │   └── ci.py               # CI 总入口
├── artifacts/          # 中间产物（由脚本生成，不手写）
│   ├── ac_with_code.jsonl    # 批量拉取的 AC 提交记录
│   └── imported_paths.txt    # 上次 import_ac_to_solutions 写入的文件路径列表
├── .github/workflows/
│   └── solutions-check.yml   # CI：push/PR 时自动校验 solutions + topics 规则
├── .env                      # 本地鉴权（不提交），LC_SESSION / LC_CSRF
└── AGENTS.md                 # 给 AI Agent 看的项目规范说明
```

---

## 题解文件格式

**路径规则**：`solutions/<低-高>/<题号四位>-<slug>.md`
- 例：`solutions/0001-0100/0001-two-sum.md`
- 目录范围按每 100 题一段，如 `0001-0100`、`0101-0200`

**Front Matter**（YAML，必须完整）：
```yaml
---
id: 1                    # LeetCode 真实题号（与文件名一致）
title: Two Sum           # 英文标题（来自 API）
difficulty: Easy         # Easy | Medium | Hard
tags: [array, hash-table]
created: 2026-02-20      # YYYY-MM-DD
---
```

**必须包含的四个 Section**：
```markdown
## 题目链接
## 题目描述
## 解题思路   ← 需含时间/空间复杂度（格式：$O(n)$）
## 代码       ← 代码块，语言标签需正确（如 ```python）
```

**CI 校验规则**：
- `scripts/ci/check_solutions.py`
- 文件路径/名格式合法
- Front matter 四个 key 均存在且非空
- `id` 与文件名中的题号一致，与 H1 标题中的题号一致
- `difficulty` 只能是 `Easy/Medium/Hard`
- `created` 是合法的 `YYYY-MM-DD`
- 包含全部四个必需 Section
- 不能含占位符 `O()`（时间/空间复杂度必须填实际值）
- 不能有重复 `id`
- `scripts/ci/check_topics.py`
- 检查 `topics/*.md` 中重复题号（同一题号出现两次及以上会失败，并输出重复题号清单）
- `scripts/ci/ci.py`
- 串行执行 `check_solutions.py` + `check_topics.py`，作为 workflow 入口

---

## 脚本说明

### `scripts/env.py`
加载项目根目录的 `.env` 文件到 `os.environ`（副作用 import，其他脚本 `import env` 即可）。

### `scripts/fetch_problem.py`
按题号或直接指定 slug 拉取单道题，生成 Markdown 模板（空代码块，解题思路待填）。
```bash
python scripts/fetch_problem.py 1584                                     # 普通题：按题号
python scripts/fetch_problem.py 1584 --overwrite
python scripts/fetch_problem.py --slug count-sequences-with-given-sum   # 竞赛题或直接指定 slug
```
两种模式：
- **按题号**：先查 `https://leetcode.cn/api/problems/all/` 找 slug，再调 GraphQL 拿详情，以传入的题号命名文件
- **按 slug**（`--slug`）：直接调 GraphQL，用返回的 `questionId` 命名文件；竞赛期间也可用

### `scripts/fetch_ac_submissions.py`
**批量**从力扣 CN 拉取个人 AC 提交（含代码），写入 `artifacts/ac_with_code.jsonl`。
```bash
python scripts/fetch_ac_submissions.py
python scripts/fetch_ac_submissions.py --delay 0.8 --days 365
```
特性：同题只保留最新一次 AC；断点续传（`code=null` 的记录自动重拉）；限流退避（30→60→120→180→300s）；竞赛题与普通题统一处理。

> ⚠️ JSONL 中 `frontendId` 是力扣前端题号，对普通题与 `questionId` 相同，竞赛题可能不一致。
> `import_ac_to_solutions.py` 始终通过 GraphQL `questionId` 字段命名文件，不直接依赖 `frontendId`。

### `scripts/filter_ac_with_code.py`
从 `ac_with_code.jsonl` 中删除已归档到 `solutions/` 的题目（原地覆写 JSONL）。
```bash
python scripts/filter_ac_with_code.py --dry-run
python scripts/filter_ac_with_code.py
```
匹配逻辑：以 `{frontendId:04d}-{titleSlug}` 与 `solutions/**/*.md` 的文件名（stem）对比。

### `scripts/import_ac_to_solutions.py`
将 `ac_with_code.jsonl` 中**尚未归档**的题目批量导入 `solutions/`。
```bash
python scripts/import_ac_to_solutions.py --dry-run
python scripts/import_ac_to_solutions.py --delay 0.8
```
流程：
1. 扫描 `solutions/**/*.md`，提取已有 slug 集合
2. 遍历 JSONL，跳过已有 slug（含同 slug 重复行）
3. 对未有的题目调 GraphQL 拿 `questionId`（真实题号）、标题、难度、标签、题目描述
4. 生成完整 Markdown（含 AC 代码，语言标签从 `lang` 字段映射）
5. 写入 `solutions/<range>/<id>-<slug>.md`
6. 将本次新建的文件路径列表写入 `artifacts/imported_paths.txt`

**lang → 代码块标签映射**：`python3→python`、`golang→go`、`cpp→cpp`、`mysql/mssql/oraclesql→sql` 等。

### `scripts/ci/check_solutions.py`
校验全部 `solutions/**/*.md`。
```bash
python scripts/ci/check_solutions.py
```

### `scripts/ci/check_topics.py`
校验全部 `topics/*.md`（含重复题号检查）。
```bash
python scripts/ci/check_topics.py
```

### `scripts/ci/ci.py`
CI 总入口，串行执行 solutions + topics 校验。
```bash
python scripts/ci/ci.py
```

### `scripts/normalize_topics_title.py`
为 `topics/*.md` 的 H2-H6 标题添加/移除层级数字前缀（如 `## 1.2 xxx`）。
```bash
python scripts/normalize_topics_title.py
python scripts/normalize_topics_title.py --strip
python scripts/normalize_topics_title.py --dry-run
```

---

## 典型工作流

### 手动归档单题
```bash
python scripts/fetch_problem.py <题号>         # 普通题：生成模板
python scripts/fetch_problem.py --slug <slug>  # 竞赛题或已知 slug 时
# 手写解题思路 + 代码
python scripts/ci/check_solutions.py           # 本地校验（仅 solutions）
```

### 从 AC 记录批量导入
```bash
# 1. 拉取 AC 提交（需 .env 鉴权）
python scripts/fetch_ac_submissions.py

# 2. 预览哪些题需要导入
python scripts/import_ac_to_solutions.py --dry-run

# 3. 正式导入
python scripts/import_ac_to_solutions.py

# 4. 补写解题思路后校验（solutions + topics）
python scripts/ci/ci.py
```
---

## CI
`.github/workflows/solutions-check.yml`：push 或 PR 时自动运行 `python scripts/ci/ci.py`，校验失败则 PR 无法合并。
