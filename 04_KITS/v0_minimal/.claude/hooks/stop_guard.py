"""Conservative Stop hook skeleton for v0_minimal.

Checks for unsupported done claims and reminds the honest status taxonomy.
Designed to stay cheap and quiet.
"""

from __future__ import annotations

import json
import sys
from typing import Any, Dict, List


DONE_WORDS = ("done", "completed", "finished", "all set", "resolved")
EVIDENCE_WORDS = ("tested", "verified", "diff", "status", "line count", "check", "validated")


def parse_stdin() -> Dict[str, Any]:
    raw = sys.stdin.read().strip()
    if not raw:
        return {}
    try:
        data = json.loads(raw)
        if isinstance(data, dict):
            return data
    except json.JSONDecodeError:
        return {"summary": raw}
    return {}


def get_summary(data: Dict[str, Any]) -> str:
    for key in ("summary", "message", "output", "final"):
        value = data.get(key)
        if isinstance(value, str):
            return value
    return ""


def needs_review(summary: str) -> bool:
    lower = summary.lower()
    claims_done = any(word in lower for word in DONE_WORDS)
    has_evidence = any(word in lower for word in EVIDENCE_WORDS)
    return claims_done and not has_evidence


def main() -> int:
    data = parse_stdin()
    summary = get_summary(data)
    result = {
        "hook": "stop_guard",
        "status": "needs-review" if needs_review(summary) else "ok",
        "allowed_statuses": [
            "done",
            "partial",
            "blocked",
            "needs-review",
            "unsafe-without-preflight",
            "insufficient-context",
        ],
    }
    sys.stdout.write(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
