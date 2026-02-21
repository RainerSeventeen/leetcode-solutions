# LeetCode Solution

个人构建的 leetcode 算法平台知识库

---

## 拉取 AC 提交记录

`scripts/fetch_ac_submissions.py` 从力扣中文站批量拉取个人 AC 提交代码，边拉边写入，支持断点续传。

### 前置条件

1. 安装依赖：`pip install requests`
2. 配置 Cookie（从浏览器 DevTools → Application → Cookies → `leetcode.cn` 获取）：

```bash
cp .env.example .env
# 编辑 .env，填入 LC_SESSION 和 LC_CSRF 的值
```

### 拉取代码

```bash
python scripts/fetch_ac_submissions.py
python scripts/fetch_ac_submissions.py --delay 0.8   # 调整请求间隔（秒）
python scripts/fetch_ac_submissions.py --days 365    # 只拉最近 N 天
```

输出：`artifacts/ac_with_code.jsonl`（JSONL 格式，每行一条记录）

- **去重**：同一道题只拉最新的一次 AC，旧提交无需请求直接跳过
- **断点续传**：中断后重跑，已成功写入的题目自动跳过；`code=null` 的记录自动清除并重拉
- **限流退避**：遇到「超出访问限制」按 30→60→120→180→300 秒退避重试

### 过滤已归档题目

```bash
python scripts/filter_ac_with_code.py --dry-run  # 预览将删除哪些条目
python scripts/filter_ac_with_code.py            # 正式过滤，删除 solutions/ 中已存在的题目
```

输出：原地更新 `artifacts/ac_with_code.jsonl`