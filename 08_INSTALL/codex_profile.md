# codex_profile

This document explains how `v0_minimal` should be adapted for Codex-like environments.

## Main distinction

Portable `AGENTS.md` gives context.
Sandbox, approvals, wrappers, and local validation provide harder constraints.

## Use

- keep runtime files compact
- keep repo-specific install profile explicit
- adapt hook/command concepts to available local tooling
- do not pretend a copied Claude-oriented settings file is automatic Codex enforcement

## Limits

Context-only files do not block unsafe action on their own.

## Validation

- verify local command model
- run proving-ground prompts manually
- inspect bounded batch behavior before trusting the install
