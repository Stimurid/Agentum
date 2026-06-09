# WAVE_01_OFFICIAL_FORMATS

This wave captured how official agent-facing surfaces are structured and where their authority stops.

Key takeaways:

- `AGENTS.md` and `CLAUDE.md` are context surfaces, not hard enforcement.
- Hook lifecycles, settings, sandboxing, and approvals are stronger operational guard points.
- Runtime files must stay compact enough to survive real agent loading without turning into archive dumps.

What this wave contributed to the repo:

- separation between context layer and runtime guard layer;
- decision to keep root manifests short and move long explanation into theory/docs;
- design basis for `04_KITS/v0_minimal/.claude/settings.json` as a conservative template, not a fantasy schema.

Operational consequence:

Never mistake elegant markdown for enforcement.
