# 项目结构

个人 LeetCode 算法知识库，以 Markdown 文件管理题解，配套 Python 脚本实现从力扣平台批量拉取、导入、校验的自动化流程。

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
│   │   ├── check_competition_promotions.py # 竞赛题转正检查
│   │   ├── check_id_integrity.py           # 题号/标题一致性检查
│   │   └── ci.py                           # CI 总入口
│   └── auto/
│       ├── auto_git.py       # 自动收集可提交改动并生成提交信息
│       └── auto_git.sh       # 调用 .venv Python 的包装脚本
├── artifacts/          # 中间产物（由脚本生成，不手写）
│   ├── ac_with_code.jsonl    # 批量拉取的 AC 提交记录
│   ├── imported_paths.txt    # 上次 import_ac_to_solutions 写入的文件路径列表
│   ├── migrated_competition_paths.txt # 上次竞赛题迁移写入的文件路径列表
│   └── id_integrity_report.jsonl      # 题号一致性检查报告
├── .github/workflows/
│   ├── solutions-check.yml   # CI：push/PR 时执行主校验
│   └── id-integrity-check.yml # 定时/手动执行 ID 一致性检查
├── .env                      # 本地鉴权（不提交），LC_SESSION / LC_CSRF
└── AGENTS.md                 # 给 AI Agent 看的项目规范说明
```
