"""Conservative PreToolUse hook skeleton for v0_minimal.

Performs small, Windows-aware checks for destructive git, secret paths,
high-stdout shell usage, dependency installs, and deploy/runtime risk.
"""

from __future__ import annotations

import json
import re
import sys
from typing import Any, Dict, List


SECRET_PATTERNS = (
    ".env",
    "secret",
    "secrets",
    "credential",
    "token",
    "password",
    "key",
)

DEPLOY_HINTS = (
    "deploy",
    "production",
    "systemctl",
    "kubectl",
    "terraform",
    "docker compose up",
)

HIGH_STDOUT_HINTS = (
    "Get-ChildItem -Recurse",
    "dir /s",
    "rg ",
    "grep -R",
    "docker logs",
    "npm install",
    "pip install",
)

DESTRUCTIVE_GIT_PATTERNS = (
    "git reset --hard",
    "git clean -fd",
    "git checkout --",
    "git restore --source",
)

INSTALL_HINTS = (
    "npm install",
    "pnpm install",
    "yarn install",
    "pip install",
    "poetry install",
    "cargo install",
)


def parse_stdin() -> Dict[str, Any]:
    raw = sys.stdin.read().strip()
    if not raw:
        return {}
    try:
        data = json.loads(raw)
        if isinstance(data, dict):
            return data
    except json.JSONDecodeError:
        return {"raw": raw}
    return {}


def first_string(data: Dict[str, Any], keys: List[str]) -> str:
    for key in keys:
        value = data.get(key)
        if isinstance(value, str):
            return value
    return ""


def split_segments(command: str) -> List[str]:
    parts = re.split(r"\|\||&&|;|\||\r?\n", command)
    return [part.strip() for part in parts if part.strip()]


def inspect(command: str, path_hint: str) -> Dict[str, Any]:
    risks: List[str] = []
    lower = command.lower()
    for pattern in DESTRUCTIVE_GIT_PATTERNS:
        if pattern in lower:
            risks.append("destructive_git")
            break
    if any(hint in lower for hint in DEPLOY_HINTS):
        risks.append("deploy_runtime_risk")
    if any(hint in lower for hint in INSTALL_HINTS):
        risks.append("dependency_install")
    if any(hint.lower() in command.lower() for hint in HIGH_STDOUT_HINTS) and "head" not in lower and "tail" not in lower and "select-object -first" not in lower:
        risks.append("stdout_risk")
    if any(secret in path_hint.lower() for secret in SECRET_PATTERNS) or any(secret in lower for secret in SECRET_PATTERNS):
        risks.append("secret_path")
    if len(split_segments(command)) > 1:
        risks.append("compound_command")
    status = "ask_or_deny" if risks else "ok"
    return {"status": status, "risk_vector": risks}


def main() -> int:
    data = parse_stdin()
    command = first_string(data, ["command", "tool_input", "input", "raw"])
    path_hint = first_string(data, ["path", "cwd", "target_path"])
    result = {
        "hook": "pretool_guard",
        "tool": first_string(data, ["tool_name", "tool"]),
        "segments": len(split_segments(command)) if command else 0,
    }
    result.update(inspect(command, path_hint))
    sys.stdout.write(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
