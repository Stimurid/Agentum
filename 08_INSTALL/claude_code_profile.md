# claude_code_profile

This document explains how `v0_minimal` should be adapted for Claude Code.

## Main distinction

`AGENTS.md` and `CLAUDE.md` are context surfaces.
Hooks, settings, permissions, sandboxing, and evals are stronger runtime guard surfaces.

## Use

- keep root files compact
- use `.claude/settings.json` as template-only unless schema is validated locally
- keep hooks quiet, dependency-free, and local
- do not auto-approve destructive git, secret, deploy, or dependency-install actions

## Limits

Claude Code markdown instructions are not hard enforcement by themselves.

## Validation

- hook syntax check
- proving-ground prompts
- local approval review before target install
