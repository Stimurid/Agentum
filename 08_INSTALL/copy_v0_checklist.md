# copy_v0_checklist

Use this checklist before copying `v0_minimal` into any target repo.

## Before copy

- confirm active target repo and root path
- choose a reviewed project profile
- confirm this is not a production/deploy action
- decide Claude Code or Codex target

## Copy scope

- copy compact runtime files only
- copy only the profile slice needed by the target repo
- do not copy the whole research archive
- do not copy persona humor into dry runtime guard prompts

## Organ-set choice

Before copying, name the organ set explicitly:

- minimum generic set = `ORGAN-001`, `ORGAN-005`, `ORGAN-006`
- Litops set adds `ORGAN-002`, `ORGAN-003`
- WhiteCrow set adds `ORGAN-003`, `ORGAN-004`
- ModerBober starts with the minimum generic set
- Quinta starts with the minimum generic set and may later add persona layer separately

## Validation

- verify settings template against target runtime
- compile hooks if Python is present
- run proving-ground prompts manually
- inspect `git status`

## Human review

No automatic install from `Agentum` without human review.
