# 脚本说明

> 所有 Python 脚本在虚拟环境下运行。

## `scripts/env.py`
加载项目根目录的 `.env` 文件到 `os.environ`（副作用 import，其他脚本 `import env` 即可）。

## `scripts/fetch_problem.py`
按题号或直接指定 slug 拉取单道题，生成 Markdown 模板（空代码块，解题思路待填）。
```bash
python scripts/fetch_problem.py 1584                                     # 普通题：按题号
python scripts/fetch_problem.py 1584 --overwrite
python scripts/fetch_problem.py --slug count-sequences-with-given-sum   # 竞赛题或直接指定 slug
```
两种模式：
- **按题号**：先查 `https://leetcode.cn/api/problems/all/` 找 slug，再调 GraphQL 拿详情，以传入的题号命名文件
- **按 slug**（`--slug`）：直接调 GraphQL，用返回的 `questionFrontendId`（fallback `questionId`）命名文件；竞赛期间也可用

## `scripts/fetch_ac_submissions.py`
**批量**从力扣 CN 拉取个人 AC 提交（含代码），写入 `artifacts/ac_with_code.jsonl`。
```bash
python scripts/fetch_ac_submissions.py
python scripts/fetch_ac_submissions.py --delay 0.8 --days 365
python scripts/fetch_ac_submissions.py --days 1 --keep-per-problem 0
```
特性：支持按题保留条数（默认 `--keep-per-problem 1`，即同题只保留最新一次 AC；`0` 表示保留窗口内全部 AC）；断点续传（`code=null` 的记录自动重拉）；限流退避（30→60→120→180→300s）；竞赛题与普通题统一处理。

> ⚠️ LeetCode 对竞赛题有两个 ID：`questionFrontendId`（用户可见题号，如 3838）和 `questionId`（内部数据库 ID，如 4216）。
> 所有脚本均通过 GraphQL `questionFrontendId` 字段命名文件（fallback `questionId`），确保文件名与网站显示一致。

## `scripts/filter_ac_with_code.py`
从 `ac_with_code.jsonl` 中删除已归档到 `solutions/` 的题目（原地覆写 JSONL）。
```bash
python scripts/filter_ac_with_code.py --dry-run
python scripts/filter_ac_with_code.py
```
匹配逻辑：以 `{frontendId:04d}-{titleSlug}` 与 `solutions/**/*.md` 的文件名（stem）对比。

## `scripts/import_ac_to_solutions.py`
将 `ac_with_code.jsonl` 中**尚未归档**的题目批量导入 `solutions/`。
```bash
python scripts/import_ac_to_solutions.py --dry-run
python scripts/import_ac_to_solutions.py --delay 0.8
```
流程：
1. 扫描 `solutions/**/*.md`，提取已有 slug 集合
2. 读取并按 slug 归并 JSONL 记录（同题多提交合并为同一题）
3. 对未有的题目调 GraphQL 拿 `questionFrontendId`（用户可见题号）、标题、难度、标签、题目描述
4. 生成完整 Markdown（`## 代码` 下保留多段 AC 代码，默认按提交时间从新到旧）
5. 导入阶段不做“同方法去重”，仅原样导入（是否合并由后续 agent 决定）
6. 写入 `solutions/<range>/<id>-<slug>.md`
7. 将本次新建的文件路径列表写入 `artifacts/imported_paths.txt`

**lang → 代码块标签映射**：`python3→python`、`golang→go`、`cpp→cpp`、`mysql/mssql/oraclesql→sql` 等。

## `scripts/check_id_integrity.py`
扫描所有 `solutions/**/*.md`，查 GraphQL 获取 `questionFrontendId` 并与文件名 ID 比对，检测 ID 错位或目录错位问题。
```bash
python scripts/check_id_integrity.py              # 完整 API 检查（~0.5s/题）
python scripts/check_id_integrity.py --slug-only  # 只做本地文件名/front matter 对比，不调 API
```
输出：`artifacts/id_integrity_report.jsonl`，每行含 `file`、`file_id`、`api_id`、`status`（OK / MISMATCH）等字段。

## `scripts/fix_id_mismatches.py`
读取 `artifacts/id_integrity_report.jsonl`，批量修复所有 MISMATCH 条目：
- 更新 front matter `id` 和 H1 标题中的题号
- 将文件移动到正确路径（目录 + 文件名）
- 同步更新 `topics/*.md` 中的题号和路径引用
- 清理空目录
```bash
python scripts/fix_id_mismatches.py --dry-run   # 预览变更
python scripts/fix_id_mismatches.py              # 执行修复
```

## `scripts/normalize_topics.py`
为 `topics/*.md` 做统一格式化：
- H2-H6 标题添加/移除层级数字前缀（如 `## 1.2 xxx`）
- 非代码块中，若某行以 `:` 或 `：` 结尾，且下一行非空，则自动补一个真正空行
```bash
python scripts/normalize_topics.py
python scripts/normalize_topics.py --strip
python scripts/normalize_topics.py --dry-run
```

## CI 脚本

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
