# generic_repo INSTALL

## Preflight checklist

- confirm target repo identity and root path
- confirm this is not a production/deploy task
- confirm human review is present
- decide Claude Code or Codex target

## Files to copy or adapt

- `04_KITS/v0_minimal/AGENTS.md`
- `04_KITS/v0_minimal/CLAUDE.md` if needed
- `.claude/settings.json`
- hook skeletons
- command markdowns
- runtime docs

## Files not to copy

- `01_RESEARCH_ARCHIVE/**`
- `02_REGISTRIES/**`
- persona fragments by default

## Target identity confirmation

Write down active project, working object, protected paths, neighboring repos, and rollback path before copying anything.

## Dry run

List target paths, proposed copied files, and expected local modifications before touching the repo.

## Approval gate

Do not install automatically from `Agentum` without human review and target confirmation.

## Rollback plan

Keep the install in one bounded commit or one reversible staged batch.

## Validation commands

- run local hook syntax check if Python is present
- inspect copied files
- run manual proving-ground prompts from `06_EVALS`
- verify target `git status`

## First commit recommendation

Use a dedicated local commit for the first install slice before any target-specific tuning.
