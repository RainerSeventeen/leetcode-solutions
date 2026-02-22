#!/usr/bin/env python3
"""
从力扣中文站拉取个人 AC 提交代码。

用法:
  python scripts/fetch_ac_submissions.py
  python scripts/fetch_ac_submissions.py --resume
  python scripts/fetch_ac_submissions.py --resume artifacts/my_backup.jsonl
  python scripts/fetch_ac_submissions.py --days 365

去重规则: 同一道题只拉最新的一次 AC（提交列表从新到旧，首次见到该题立即拉，后续跳过）。
断点续传: 默认覆写输出文件重新拉取；--resume 不带路径时用默认输出文件续传；
          --resume <path> 指定文件路径后从该文件加载已完成题目并追加写入。
限流退避: 遇到「超出访问限制」按 30→60→120→180→300 秒退避重试。

输出: artifacts/ac_with_code.jsonl（JSONL 格式，每行一条记录）
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import sys
import time
import datetime as dt

import env  # noqa: F401 — side-effect import: loads .env into os.environ

try:
    import requests
except ModuleNotFoundError:
    print("Error: pip install requests", file=sys.stderr)
    sys.exit(1)

GRAPHQL_URL = "https://leetcode.cn/graphql/"

ARTIFACTS = pathlib.Path("artifacts")
CODE_OUTPUT = ARTIFACTS / "ac_with_code.jsonl"

REQUEST_DELAY = 0.6  # 每次请求间隔秒数

SUBMISSION_LIST_QUERY = """
query submissionList($offset: Int!, $limit: Int!, $lastKey: String, $status: SubmissionStatusEnum) {
  submissionList(offset: $offset, limit: $limit, lastKey: $lastKey, status: $status) {
    lastKey
    hasNext
    submissions {
      id
      title
      frontendId
      lang
      langVerboseName
      runtime
      memory
      timestamp
      url
    }
  }
}
"""

SUBMISSION_DETAIL_QUERY = """
query submissionDetail($submissionId: ID!) {
  submissionDetail(submissionId: $submissionId) {
    code
    question {
      titleSlug
      translatedTitle
    }
  }
}
"""


# ---------------------------------------------------------------------------
# Auth
# ---------------------------------------------------------------------------

def build_headers() -> dict[str, str]:
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; leetcode-fetcher/1.0)",
        "Referer": "https://leetcode.cn/",
        "Content-Type": "application/json",
    }
    session = os.environ.get("LC_SESSION")
    csrf = os.environ.get("LC_CSRF")
    if session and csrf:
        headers["Cookie"] = f"LEETCODE_SESSION={session}; csrftoken={csrf}"
        headers["x-csrftoken"] = csrf
    return headers


def require_auth() -> None:
    if not (os.environ.get("LC_SESSION") and os.environ.get("LC_CSRF")):
        print("Error: 需要设置 LC_SESSION 和 LC_CSRF 环境变量。", file=sys.stderr)
        print("  从浏览器 DevTools → Application → Cookies → leetcode.cn 获取，写入 .env 文件。", file=sys.stderr)
        sys.exit(1)


# ---------------------------------------------------------------------------
# GraphQL
# ---------------------------------------------------------------------------

class RateLimitError(Exception):
    """服务器返回限流响应时抛出。"""


def graphql(headers: dict, query: str, variables: dict) -> dict:
    resp = requests.post(
        GRAPHQL_URL, headers=headers,
        json={"query": query, "variables": variables}, timeout=15,
    )
    resp.raise_for_status()
    data = resp.json()
    if data.get("errors"):
        msg = str(data["errors"])
        if "超出访问限制" in msg or "rate" in msg.lower():
            raise RateLimitError(msg)
        raise RuntimeError(f"GraphQL errors: {data['errors']}")
    return data["data"]


def fetch_detail(headers: dict, sid: str) -> dict | None:
    """拉取单条提交详情，遇限流自动退避重试。"""
    BACKOFF = [30, 60, 120, 180, 300]
    for attempt, wait in enumerate([0] + BACKOFF):
        if wait:
            print(f"\n  [限流] 等待 {wait}s 后第 {attempt} 次重试 ...", flush=True)
            time.sleep(wait)
        try:
            data = graphql(headers, SUBMISSION_DETAIL_QUERY, {"submissionId": sid})
            return data.get("submissionDetail")
        except RateLimitError:
            if attempt == len(BACKOFF):
                print(f"\n  [限流] 重试 {len(BACKOFF)} 次后放弃，跳过。")
                return None
        except Exception as exc:
            print(f"  Warning: id={sid} 拉取失败: {exc}")
            return None
    return None


# ---------------------------------------------------------------------------
# Resume helpers
# ---------------------------------------------------------------------------

def load_done_fids(path: pathlib.Path) -> set[str]:
    """
    读取已有 JSONL，返回已成功拉取代码的 frontendId 集合。
    code 为 null 的条目视为失败，从文件中清除（下次重拉）。
    """
    if not path.exists():
        return set()

    done: set[str] = set()
    good_lines: list[str] = []
    null_count = 0

    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            entry = json.loads(line)
            if entry.get("code") is not None:
                done.add(str(entry["frontendId"]))
                good_lines.append(line)
            else:
                null_count += 1  # 丢弃，等待重拉
        except Exception:
            good_lines.append(line)

    if null_count:
        path.write_text(
            "\n".join(good_lines) + ("\n" if good_lines else ""),
            encoding="utf-8",
        )
        print(f"  清除 {null_count} 条 code=null 记录，将重新拉取。")

    return done


def extract_slug(url: str) -> str:
    parts = url.strip("/").split("/")
    try:
        return parts[parts.index("problems") + 1]
    except (ValueError, IndexError):
        return ""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--days", type=int, default=3650,
                        help="拉取最近 N 天内的提交（默认 3650，约 10 年）")
    parser.add_argument("--page-size", type=int, default=20,
                        help="翻页每页条数（默认 20）")
    parser.add_argument("--resume", nargs="?", const=str(CODE_OUTPUT), metavar="PATH",
                        help="断点续传：不带路径时用默认输出文件，带路径时用指定文件")
    args = parser.parse_args()

    require_auth()
    headers = build_headers()
    ARTIFACTS.mkdir(exist_ok=True)

    if args.resume:
        output_path = pathlib.Path(args.resume)
        done_fids = load_done_fids(output_path)
        file_mode = "a"
        if done_fids:
            print(f"断点续传：已有 {len(done_fids)} 道题，跳过。")
    else:
        output_path = CODE_OUTPUT
        done_fids = set()
        file_mode = "w"

    cutoff_ts = int((dt.datetime.now() - dt.timedelta(days=args.days)).timestamp())
    offset = 0
    last_key = None
    page = 1
    fetched = 0
    skipped = 0

    with output_path.open(file_mode, encoding="utf-8") as f:
        while True:
            sl = graphql(headers, SUBMISSION_LIST_QUERY, {
                "offset": offset,
                "limit": args.page_size,
                "lastKey": last_key,
                "status": "AC",
            })["submissionList"]

            subs = sl["submissions"]
            has_next = sl["hasNext"]
            last_key = sl["lastKey"]

            reached_cutoff = False
            for sub in subs:
                if int(sub["timestamp"]) < cutoff_ts:
                    reached_cutoff = True
                    break

                fid = str(sub.get("frontendId", ""))
                try:
                    fid_int = int(fid)
                except (ValueError, TypeError):
                    fid_int = 0

                if fid_int > 5000:
                    print(f"  跳过竞赛题 #{fid} {sub.get('title', '?')} (frontendId > 5000)", flush=True)
                    skipped += 1
                    continue

                if fid in done_fids:
                    skipped += 1
                    continue

                # 立即标记：同题的更旧提交在后续页中直接跳过，无需请求
                done_fids.add(fid)

                sid = sub["id"]
                title = sub.get("title", "?")
                print(f"  #{fid} {title} (id={sid})", end=" ", flush=True)

                detail = fetch_detail(headers, sid)
                entry = {**sub, "titleSlug": extract_slug(sub.get("url", ""))}

                if detail:
                    entry["code"] = detail.get("code", "")
                    q = detail.get("question") or {}
                    if not entry["titleSlug"]:
                        entry["titleSlug"] = q.get("titleSlug", "")
                    if not entry.get("title"):
                        entry["title"] = q.get("translatedTitle", "")
                    fetched += 1
                    lang = sub.get("langVerboseName") or sub.get("lang", "?")
                    print(f"✓  ({lang}, {len(entry['code'])} chars)")
                else:
                    entry["code"] = None
                    print("✗ (no code)")

                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
                f.flush()
                time.sleep(REQUEST_DELAY)

            oldest_ts = int(subs[-1]["timestamp"]) if subs else 0
            oldest_str = dt.datetime.fromtimestamp(oldest_ts).strftime("%Y-%m-%d") if oldest_ts else "?"
            print(f"  [page {page}] oldest={oldest_str}  本次拉取={fetched}  跳过={skipped}", flush=True)

            if reached_cutoff or not has_next:
                break

            offset += args.page_size
            page += 1
            time.sleep(REQUEST_DELAY)

    print(f"\n完成。本次拉取 {fetched} 道，跳过 {skipped} 道。")
    print(f"输出 → {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
