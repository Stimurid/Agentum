# quinta INSTALL

## Preflight checklist

- confirm target repo is Quinta
- identify workbench, persona, TRIZ, and seed-prompt surfaces
- decide whether persona fragments are actually needed
- confirm rollback path

## Files to copy or adapt

- compact runtime guard files
- selected project identity and status docs
- persona fragments only if explicitly wanted in persona prompts

## Organ set

Install this split set:

- dry guard set = `ORGAN-001`, `ORGAN-005`, `ORGAN-006`
- memory-sensitive extension = `ORGAN-003`

Keep persona fragments outside the dry guard set.

## Files not to copy

- archive and registries as runtime files
- persona humor into dry guard prompts

## Target identity confirmation

Name which target files are runtime guard, which are persona/style, and which are workbench logic.

## Dry run

Show insertion points separately for guard layer and persona layer.

## Approval gate

Do not install automatically from `Agentum` without human review.

## Rollback plan

Keep guard and persona additions in separate reversible commits if both are installed.

## Validation commands

- hook syntax check
- target `git status`
- manual proving-ground on project bleed, safe-batch, memory, and persona/guard separation

## First commit recommendation

Start with dry guard slice. Add persona style layer only after that boundary is stable.
