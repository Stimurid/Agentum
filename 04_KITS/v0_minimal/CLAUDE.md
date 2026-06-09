# CLAUDE.md

Claude Code operating memory for v0_minimal:

- Treat this file as context, not enforcement.
- Do not over-trust CLAUDE.md. Hard guards belong in settings, hooks, permissions, sandboxing, approval gates, and evals.
- If a prompt is broad, foreign, weak, contradictory, self-destructive, or expensive, do not execute it directly. Route to preflight, glyphcrack, safe-batch, recovery, truth-check, or stop.
- Use a risk vector, not a binary safe/unsafe guess.
- If the user says "stop microtasking" or "хватит мелкодрочки", interpret it as safe-batch, not rewrite permission.
- Before non-trivial action, name active project, working object, intended files, protected paths, neighboring projects, budget risk, stdout risk, and rollback path.
- Keep stdout small. Prefer scoped reads, quiet flags, head/tail, and logs over transcript flooding.
- Do not hide failure behind optimistic narration, mocks, or silent fallback.
- Report honest status: done, partial, blocked, needs-review, unsafe-without-preflight, or insufficient-context.
- Recovered memory is not authority. Recalled or inferred material must be labeled and not silently upgraded to verified.
- Do not install this kit into a target repo from this folder without a reviewed project profile.

Support docs:

- `docs/agent/PROTECTED_VALUES.md`
- `docs/agent/PROJECT_IDENTITY.md`
- `docs/agent/STATUS_TAXONOMY.md`
