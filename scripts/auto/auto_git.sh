#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
cd "${REPO_ROOT}"

LOG_DIR="${REPO_ROOT}/scripts/auto/log"
LOG_FILE="${LOG_DIR}/leetcode.log"
DRY_RUN=false

usage() {
  cat <<'USAGE'
Usage: auto_git.sh [--dry-run] [--log-file <path>]
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run)
      DRY_RUN=true
      shift
      ;;
    --log-file)
      if [[ $# -lt 2 ]]; then
        echo "Missing value for --log-file" >&2
        exit 2
      fi
      LOG_FILE="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

mkdir -p "$(dirname "${LOG_FILE}")"

ts() { date '+%Y-%m-%d %H:%M:%S'; }
log() {
  local msg="$1"
  local level="INFO"
  if [[ "$msg" == ERROR:* ]]; then
    level="ERROR"
    msg="${msg#ERROR: }"
  elif [[ "$msg" == WARN:* ]]; then
    level="WARN"
    msg="${msg#WARN: }"
  fi
  echo "[$(ts)] [${level}] ${msg}" >> "${LOG_FILE}"
}

PYTHON_BIN="${REPO_ROOT}/.venv/bin/python"
META_SCRIPT="${REPO_ROOT}/scripts/auto/collect_commit.py"

if [[ ! -x "${PYTHON_BIN}" ]]; then
  log "ERROR: missing virtual environment interpreter: ${PYTHON_BIN}"
  exit 1
fi

TMP_META_FILE="$(mktemp)"
TMP_ERR_FILE="$(mktemp)"
trap 'rm -f "${TMP_META_FILE}" "${TMP_ERR_FILE}"' EXIT

log "run started (dry-run=${DRY_RUN})"
log "collecting commit metadata via ${META_SCRIPT}"

set +e
"${PYTHON_BIN}" "${META_SCRIPT}" >"${TMP_META_FILE}" 2>"${TMP_ERR_FILE}"
META_RC=$?
set -e

if [[ -s "${TMP_ERR_FILE}" ]]; then
  while IFS= read -r err_line; do
    log "ERROR: ${err_line}"
  done < "${TMP_ERR_FILE}"
fi

if [[ ${META_RC} -eq 2 ]]; then
  log "no eligible files found; skip commit"
  exit 0
fi

if [[ ${META_RC} -eq 3 ]]; then
  log "WARN: eligible files found but none are new solutions with 4-digit id; skip commit"
  exit 1
fi

if [[ ${META_RC} -ne 0 ]]; then
  log "ERROR: metadata collection failed with exit code ${META_RC}"
  exit "${META_RC}"
fi

mapfile -t META_LINES <"${TMP_META_FILE}"
if [[ ${#META_LINES[@]} -lt 2 ]]; then
  log "ERROR: invalid commit metadata output from ${META_SCRIPT}"
  exit 1
fi

COMMIT_MESSAGE="${META_LINES[0]}"
FILES_TO_STAGE=("${META_LINES[@]:1}")

log "commit message: ${COMMIT_MESSAGE}"
log "files to stage:"
for f in "${FILES_TO_STAGE[@]}"; do
  log "- ${f}"
done

if [[ "${DRY_RUN}" == "true" ]]; then
  log "dry run mode; skip git add/commit/push"
  exit 0
fi

log "running git add on eligible files"
git add -- "${FILES_TO_STAGE[@]}" >> "${LOG_FILE}" 2>&1

if git diff --cached --quiet; then
  log "no staged changes to commit; skip commit"
  exit 0
fi

log "running git commit"
git commit -m "${COMMIT_MESSAGE}" >> "${LOG_FILE}" 2>&1
log "commit completed"
log "running git push"
git push >> "${LOG_FILE}" 2>&1
log "push completed"
