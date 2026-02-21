#!/usr/bin/env python3
"""
Fetch LeetCode CN AC submission history in two steps.

Setup:
  export LC_SESSION="<value of LEETCODE_SESSION cookie>"
  export LC_CSRF="<value of csrftoken cookie>"
  (Get from: browser DevTools > Application > Cookies > leetcode.cn)

Step 1 — fetch submission metadata & deduplicate:
  python scripts/fetch_ac_submissions.py fetch-list
  python scripts/fetch_ac_submissions.py fetch-list --days 365
  Output: artifacts/ac_latest.json  (one entry per problem, latest AC only)

Step 2 — fetch code for each problem:
  python scripts/fetch_ac_submissions.py fetch-code
  python scripts/fetch_ac_submissions.py fetch-code --delay 0.8
  Output: artifacts/ac_with_code.json

Quick test (small batch, saves artifacts/ac_sample.json):
  python scripts/fetch_ac_submissions.py test
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import sys
import time
import datetime as dt

import env  # loads .env from project root into os.environ

try:
    import requests
except ModuleNotFoundError:
    print("Error: pip install requests", file=sys.stderr)
    sys.exit(1)

GRAPHQL_URL = "https://leetcode.cn/graphql/"
USERNAME = "RainerSeventeen"

ARTIFACTS = pathlib.Path("artifacts")
LIST_OUTPUT = ARTIFACTS / "ac_latest.json"
CODE_OUTPUT = ARTIFACTS / "ac_with_code.jsonl"   # JSONL: one record per line
SAMPLE_OUTPUT = ARTIFACTS / "ac_sample.json"


# ---------------------------------------------------------------------------
# Auth helpers
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
        print("Error: LC_SESSION and LC_CSRF env vars required.", file=sys.stderr)
        print("  export LC_SESSION='...'", file=sys.stderr)
        print("  export LC_CSRF='...'", file=sys.stderr)
        sys.exit(1)


def graphql(headers: dict, query: str, variables: dict) -> dict:
    resp = requests.post(
        GRAPHQL_URL, headers=headers, json={"query": query, "variables": variables}, timeout=15
    )
    resp.raise_for_status()
    data = resp.json()
    if data.get("errors"):
        raise RuntimeError(f"GraphQL errors: {data['errors']}")
    return data["data"]


# ---------------------------------------------------------------------------
# Step 0: public stats
# ---------------------------------------------------------------------------

AC_STATS_QUERY = """
query userSolvedCount($userSlug: String!) {
  userProfileUserQuestionProgress(userSlug: $userSlug) {
    numAcceptedQuestions { difficulty count }
  }
}
"""


def fetch_ac_stats(headers: dict) -> dict[str, int]:
    data = graphql(headers, AC_STATS_QUERY, {"userSlug": USERNAME})
    rows = data["userProfileUserQuestionProgress"]["numAcceptedQuestions"]
    return {r["difficulty"]: r["count"] for r in rows}


# ---------------------------------------------------------------------------
# Step 1: fetch all AC submission metadata, deduplicate
# ---------------------------------------------------------------------------

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


def extract_slug(url: str) -> str:
    """Extract titleSlug from url like /problems/<slug>/submissions/<id>/"""
    parts = url.strip("/").split("/")
    try:
        return parts[parts.index("problems") + 1]
    except (ValueError, IndexError):
        return ""


def fetch_all_ac_meta(headers: dict, days: int, page_size: int = 20, delay: float = 0.5) -> list[dict]:
    """Paginate submissionList (AC only), stop at cutoff date. Returns raw list."""
    cutoff_ts = int((dt.datetime.now() - dt.timedelta(days=days)).timestamp())
    results: list[dict] = []
    offset = 0
    last_key = None
    page = 1

    while True:
        data = graphql(headers, SUBMISSION_LIST_QUERY, {
            "offset": offset,
            "limit": page_size,
            "lastKey": last_key,
            "status": "AC",
        })
        sl = data["submissionList"]
        subs = sl["submissions"]
        has_next = sl["hasNext"]
        last_key = sl["lastKey"]

        in_range = []
        reached_cutoff = False
        for sub in subs:
            if int(sub["timestamp"]) >= cutoff_ts:
                in_range.append(sub)
            else:
                reached_cutoff = True
                break

        results.extend(in_range)
        oldest_ts = int(subs[-1]["timestamp"]) if subs else 0
        oldest_str = dt.datetime.fromtimestamp(oldest_ts).strftime("%Y-%m-%d") if oldest_ts else "?"
        status = "→ cutoff reached, stopping" if reached_cutoff else ""
        print(f"  Page {page}: +{len(in_range)} in range (oldest: {oldest_str}), total: {len(results)} {status}")

        if reached_cutoff or not has_next:
            break

        offset += page_size
        page += 1
        time.sleep(delay)

    return results


def deduplicate(subs: list[dict]) -> list[dict]:
    """Keep only the latest AC submission per problem (by frontendId)."""
    # submissionList is newest-first, so first occurrence = latest
    seen: set[str] = set()
    latest: list[dict] = []
    for sub in subs:
        key = sub.get("frontendId") or sub.get("id")
        if key not in seen:
            seen.add(key)
            sub["titleSlug"] = extract_slug(sub.get("url", ""))
            latest.append(sub)
    return latest


def cmd_fetch_list(args: argparse.Namespace) -> int:
    require_auth()
    headers = build_headers()

    stats = fetch_ac_stats(headers)
    total = sum(stats.values())
    print(f"Public stats — Easy: {stats.get('EASY',0)}  Medium: {stats.get('MEDIUM',0)}  Hard: {stats.get('HARD',0)}  Total: {total}")
    print(f"\nFetching AC submission metadata (past {args.days} days) ...")

    raw = fetch_all_ac_meta(headers, days=args.days, delay=args.delay)
    print(f"\nRaw AC submissions: {len(raw)}")

    latest = deduplicate(raw)
    print(f"After dedup (one per problem): {len(latest)}")

    ARTIFACTS.mkdir(exist_ok=True)
    LIST_OUTPUT.write_text(json.dumps(latest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved → {LIST_OUTPUT}")
    return 0


# ---------------------------------------------------------------------------
# Step 2: fetch code for each submission
# ---------------------------------------------------------------------------

SUBMISSION_DETAIL_QUERY = """
query submissionDetail($submissionId: ID!) {
  submissionDetail(submissionId: $submissionId) {
    id
    code
    lang
    langVerboseName
    runtime
    memory
    timestamp
    question {
      questionFrontendId
      titleSlug
      translatedTitle
    }
  }
}
"""


def fetch_code(headers: dict, submission_id: str) -> dict | None:
    try:
        data = graphql(headers, SUBMISSION_DETAIL_QUERY, {"submissionId": submission_id})
        return data.get("submissionDetail")
    except Exception as exc:
        print(f"    Warning: failed to fetch code for id={submission_id}: {exc}")
        return None


def cmd_fetch_code(args: argparse.Namespace) -> int:
    require_auth()
    headers = build_headers()

    input_path = pathlib.Path(args.input)
    if not input_path.exists():
        print(f"Error: {input_path} not found. Run 'fetch-list' first.", file=sys.stderr)
        return 1

    latest: list[dict] = json.loads(input_path.read_text(encoding="utf-8"))

    # Resume: load already-written submission ids from JSONL output
    ARTIFACTS.mkdir(exist_ok=True)
    done_ids: set[str] = set()
    if CODE_OUTPUT.exists():
        for line in CODE_OUTPUT.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line:
                try:
                    done_ids.add(json.loads(line)["id"])
                except Exception:
                    pass

    remaining = [s for s in latest if s["id"] not in done_ids]
    if done_ids:
        print(f"Resuming: {len(done_ids)} already done, {len(remaining)} remaining.")
    print(f"Fetching code for {len(remaining)}/{len(latest)} submissions (delay={args.delay}s) ...\n")

    ok = len(done_ids)
    with CODE_OUTPUT.open("a", encoding="utf-8") as f:
        for i, sub in enumerate(remaining, 1):
            sid = sub["id"]
            title = sub.get("title", "?")
            fid = sub.get("frontendId", "?")
            print(f"  [{i}/{len(remaining)}] #{fid} {title} (id={sid})", end=" ", flush=True)

            detail = fetch_code(headers, sid)
            entry = {**sub}
            if detail:
                entry["code"] = detail.get("code", "")
                q = detail.get("question") or {}
                if not entry.get("titleSlug"):
                    entry["titleSlug"] = q.get("titleSlug", "")
                if not entry.get("title"):
                    entry["title"] = q.get("translatedTitle", "")
                ok += 1
                lang = sub.get("langVerboseName") or sub.get("lang", "?")
                print(f"✓  ({lang}, {len(entry['code'])} chars)")
            else:
                entry["code"] = None
                print("✗ (no code)")

            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
            f.flush()

            if i < len(remaining):
                time.sleep(args.delay)

    total = len(latest)
    print(f"\nDone. {ok}/{total} with code.")
    print(f"Saved → {CODE_OUTPUT}  (JSONL format, one record per line)")
    return 0


# ---------------------------------------------------------------------------
# Test: small batch
# ---------------------------------------------------------------------------

def cmd_test(args: argparse.Namespace) -> int:
    headers = build_headers()

    print(f"[test] Public AC stats for: {USERNAME}")
    stats = fetch_ac_stats(headers)
    total = sum(stats.values())
    print(f"  Easy: {stats.get('EASY',0)}  Medium: {stats.get('MEDIUM',0)}  Hard: {stats.get('HARD',0)}  Total: {total}")

    if not (os.environ.get("LC_SESSION") and os.environ.get("LC_CSRF")):
        print("\nTip: set LC_SESSION and LC_CSRF to test authenticated fetch.")
        return 0

    print(f"\n[test] Fetching 5 AC submissions ...")
    data = graphql(headers, SUBMISSION_LIST_QUERY, {
        "offset": 0, "limit": 5, "lastKey": None, "status": "AC",
    })
    subs = data["submissionList"]["submissions"]
    for sub in subs:
        sub["titleSlug"] = extract_slug(sub.get("url", ""))

    print(f"  Got {len(subs)} submissions")

    if subs:
        sid = subs[0]["id"]
        title = subs[0].get("title", "?")
        print(f"\n[test] Fetching code for first submission: #{subs[0].get('frontendId')} {title} (id={sid}) ...")
        detail = fetch_code(headers, sid)
        if detail:
            code = detail.get("code", "")
            subs[0]["code"] = code
            print(f"  Code snippet ({len(code)} chars):\n  {code[:200].replace(chr(10), chr(10)+'  ')}")
        else:
            print("  Could not fetch code.")

    ARTIFACTS.mkdir(exist_ok=True)
    SAMPLE_OUTPUT.write_text(json.dumps(subs, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nSample saved → {SAMPLE_OUTPUT}")
    return 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch LeetCode CN AC submissions in two steps.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    # test
    sub.add_parser("test", help="Quick test: public stats + 5 submissions + 1 code sample")

    # fetch-list
    p1 = sub.add_parser("fetch-list", help="Step 1: fetch all AC metadata, deduplicate, save ac_latest.json")
    p1.add_argument("--days", type=int, default=365, help="Days to look back (default: 365)")
    p1.add_argument("--delay", type=float, default=0.5, help="Seconds between page requests (default: 0.5)")

    # fetch-code
    p2 = sub.add_parser("fetch-code", help="Step 2: fetch code for each entry in ac_latest.json")
    p2.add_argument("--input", default=str(LIST_OUTPUT), help=f"Input JSON (default: {LIST_OUTPUT})")
    p2.add_argument("--delay", type=float, default=0.6, help="Seconds between requests (default: 0.6)")

    return parser.parse_args()


def main() -> int:
    args = parse_args()
    dispatch = {"test": cmd_test, "fetch-list": cmd_fetch_list, "fetch-code": cmd_fetch_code}
    return dispatch[args.cmd](args)


if __name__ == "__main__":
    raise SystemExit(main())
