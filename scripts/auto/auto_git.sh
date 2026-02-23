#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"

PYTHON_BIN="${REPO_ROOT}/.venv/bin/python"
if [[ ! -x "${PYTHON_BIN}" ]]; then
  echo "ERROR: missing virtual environment: ${PYTHON_BIN}" >&2
  exit 1
fi

exec "${PYTHON_BIN}" "${SCRIPT_DIR}/auto_git.py" "$@"
