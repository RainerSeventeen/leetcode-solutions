"""
Load .env file from project root into os.environ (if not already set).

Usage:
    import env  # must be imported before reading os.environ

.env format:
    LC_SESSION=your_leetcode_session_value
    LC_CSRF=your_csrftoken_value
    # lines starting with # are ignored
"""
from __future__ import annotations

import os
import pathlib

_ROOT = pathlib.Path(__file__).parent.parent
_ENV_FILE = _ROOT / ".env"


def load(path: pathlib.Path = _ENV_FILE) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


load()
