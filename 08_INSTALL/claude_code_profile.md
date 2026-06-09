# claude_code_profile

Claude Code install notes for `v0_minimal`:

- `AGENTS.md` and `CLAUDE.md` are readable context, not hard enforcement
- use `.claude/settings.json` as a conservative template, then validate schema locally
- keep hooks quiet and local
- do not auto-approve destructive git, secret-touching, deploy, or dependency-install actions
- run eval prompts after install
