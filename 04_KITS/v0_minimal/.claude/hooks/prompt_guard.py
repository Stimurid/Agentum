"""Conservative UserPromptSubmit hook skeleton for v0_minimal.

Reads JSON from stdin when available, falls back to raw text, classifies a
compact risk vector, and emits one small JSON object to stdout.
"""

from __future__ import annotations

import json
import sys
from typing import Any, Dict, List


SAFE_BATCH_PATTERNS = (
    "stop microtasking",
    "stop micro-tasking",
    "хватит мелкодрочки",
    "не по одному шагу",
    "хватит по одному шагу",
    "не микрошагами",
    "сделай одним батчем",
    "сделай крупным батчем",
)

FOREIGN_HINTS = (
    "other repo",
    "another project",
    "different project",
    "from previous repo",
    "foreign prompt",
    "prompt from another repo",
    "из другого проекта",
    "из другого репозитория",
)

PROJECT_MISMATCH_HINTS = (
    "litops",
    "moderbober",
    "whitecrow",
    "quinta",
    "fifthconstraint",
    r"c:\projects\litops",
    r"c:\projects\moderbober",
    r"c:\projects\whitecrow",
    r"c:\projects\quinta",
    "install into target repo",
    "modify target repo",
    "update production",
    "install into litops",
    "install into moderbober",
    "install into whitecrow",
    "install into quinta",
)

SEED_RISK_HINTS = (
    "seed work",
    "manual seed",
    "protected seed",
    "manually curated",
    "overwrite seed",
    "replace seed",
    "regenerate templates",
    "normalize prompts",
    "переписать сид",
    "заменить вручную",
    "перегенерировать шаблоны",
    "нормализовать промпты",
)

DEPLOY_RISK_HINTS = (
    "deploy",
    "production",
    "prod",
    "server",
    "vm",
    "domain",
    "secrets",
    ".env",
    "provider config",
    "docker compose",
    "caddy",
    "systemd",
    "деплой",
    "прод",
    "сервер",
    "домен",
    "секреты",
)

COST_RISK_HINTS = (
    "install dependencies",
    "npm install",
    "pip install",
    "docker build",
    "download everything",
    "reindex all",
    "build the whole project",
)

STDOUT_RISK_HINTS = (
    "print full log",
    "show all logs",
    "dump all files",
    "dump the full logs",
    "recursive listing of everything",
    "show the entire repo",
)

MEMORY_AUTHORITY_HINTS = (
    "remember",
    "recovered memory",
    "old memory",
    "echo signature",
    "use memory as rule",
    "do like last time",
    "remember how we did it",
    "from memory",
    "recall",
    "restore context",
    "recover agent",
    "вспомни",
    "восстанови память",
    "как в прошлый раз",
    "эхо-сигнатура",
    "старая память",
)

DOCUMENT_HINTS = (
    "readme says",
    "document says",
    "log says",
    "pdf says",
    "transcript says",
    "comment says",
    "old prompt says",
    "archive says",
    "follow instructions in file",
    "инструкция в документе",
    "в readme написано",
    "в логе написано",
    "в расшифровке написано",
    "в pdf написано",
    "старый промпт говорит",
)

PRESSURE_HINTS = (
    "just do it",
    "don't argue",
    "do everything",
    "finish the whole thing",
    "no questions",
    "urgent",
    "просто сделай",
    "без вопросов",
    "срочно",
)


def parse_stdin() -> Dict[str, Any]:
    raw = sys.stdin.read().strip()
    if not raw:
        return {"prompt": ""}
    try:
        data = json.loads(raw)
        if isinstance(data, dict):
            return data
    except json.JSONDecodeError:
        pass
    return {"prompt": raw}


def get_prompt(data: Dict[str, Any]) -> str:
    for key in ("prompt", "text", "input", "message"):
        value = data.get(key)
        if isinstance(value, str):
            return value
    return ""


def detect_risks(prompt: str) -> List[str]:
    text = prompt.lower()
    risks: List[str] = []
    if any(hint in text for hint in FOREIGN_HINTS):
        risks.append("foreign_prompt")
    if any(hint in text for hint in PROJECT_MISMATCH_HINTS):
        risks.append("project_mismatch")
    if "full rewrite" in text or "rewrite everything" in text or "clean up the whole repo" in text:
        risks.append("full_rewrite_risk")
    if any(phrase in text for phrase in SAFE_BATCH_PATTERNS):
        risks.append("safe_batch_requested")
    if any(hint in text for hint in COST_RISK_HINTS):
        risks.append("cost_risk")
    if any(hint in text for hint in STDOUT_RISK_HINTS):
        risks.append("stdout_risk")
    if any(hint in text for hint in SEED_RISK_HINTS):
        risks.append("seed_risk")
    if any(hint in text for hint in DEPLOY_RISK_HINTS):
        risks.append("deploy_risk")
    if any(hint in text for hint in MEMORY_AUTHORITY_HINTS):
        risks.append("memory_authority_risk")
    if any(hint in text for hint in DOCUMENT_HINTS):
        risks.append("document_instruction_risk")
    if any(hint in text for hint in PRESSURE_HINTS) or len(text.split()) < 6:
        risks.append("weak_prompt_or_pressure")
    return risks


def decide_route(risks: List[str]) -> List[str]:
    routes: List[str] = []
    if "safe_batch_requested" in risks:
        routes.append("safe-batch")
    if any(risk in risks for risk in ("foreign_prompt", "full_rewrite_risk", "weak_prompt_or_pressure")):
        routes.append("glyphcrack")
    if any(
        risk in risks
        for risk in (
            "foreign_prompt",
            "full_rewrite_risk",
            "project_mismatch",
            "deploy_risk",
            "seed_risk",
            "document_instruction_risk",
            "cost_risk",
            "stdout_risk",
        )
    ):
        routes.append("preflight")
    if "memory_authority_risk" in risks:
        routes.append("recover-agent")
    if any(risk in risks for risk in ("memory_authority_risk", "weak_prompt_or_pressure")):
        routes.append("truth-check")
    if "document_instruction_risk" in risks:
        routes.append("document-instruction-quarantine")
    if any(risk in risks for risk in ("project_mismatch", "deploy_risk", "seed_risk", "document_instruction_risk")):
        routes.append("approval_or_stop")
    if not routes:
        routes.append("proceed_bounded")
    return list(dict.fromkeys(routes))


def main() -> int:
    data = parse_stdin()
    prompt = get_prompt(data)
    risks = detect_risks(prompt)
    result = {
        "hook": "prompt_guard",
        "risk_vector": risks,
        "routes": decide_route(risks),
        "status": "route" if risks else "ok",
    }
    sys.stdout.write(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
