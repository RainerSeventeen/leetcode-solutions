# LeetCode Solutions

个人 LeetCode 算法知识库，以 Markdown 文件管理题解，配套 Python 脚本实现从力扣平台批量拉取、导入、校验的自动化流程，配合 AI Agent 完成解题思路归纳与专题知识整理。

## 特性

- **自动拉取**：从力扣 CN 批量获取个人 AC 提交记录（含代码），支持断点续传与限流退避
- **自动导入**：将 AC 记录转换为标准 Markdown 题解模板，自动填充题目描述、标签、难度
- **格式校验**：CI 自动校验所有题解文件的格式规范，确保知识库质量
- **专题归纳**：`topics/` 目录存放算法专题笔记，通过跨题链接构建知识体系

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
│   └── check_solutions.py
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

### 配置鉴权（批量拉取 AC 记录时需要）

从浏览器 DevTools → Application → Cookies → `leetcode.cn` 获取 Cookie：

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
# 1. 按题号生成模板
python scripts/fetch_problem.py 1

# 2. 手写解题思路 + 检查
python scripts/check_solutions.py
```

### 从 AC 记录批量导入

```bash
# 1. 拉取个人 AC 提交（需 .env 鉴权）
python scripts/fetch_ac_submissions.py

# 2. 导入到题解库
python scripts/import_ac_to_solutions.py

# 3. (可选) 使用 skill 执行 link 以及扩充  工作
# .codex/skills/solution-topic-auto-link
```

### 脚本说明

| 脚本 | 说明 |
|------|------|
| `fetch_problem.py <题号>` | 按题号拉取单题，生成 Markdown 模板 |
| `fetch_ac_submissions.py` | 批量拉取 AC 提交，写入 `artifacts/ac_with_code.jsonl` |
| `filter_ac_with_code.py` | 从 JSONL 中删除已归档到 `solutions/` 的题目 |
| `import_ac_to_solutions.py` | 将 JSONL 中未归档的题目批量导入 `solutions/` |
| `check_solutions.py` |（同 CI） |
