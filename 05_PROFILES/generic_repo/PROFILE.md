# generic_repo PROFILE

## Purpose

Conservative default profile for an ordinary coding repository.

## Protected objects

- human seed work;
- project identity and root path;
- secrets and `.env`;
- deploy/runtime configs;
- package/dependency files;
- generated outputs that should not be blindly regenerated;
- honest completion evidence.

## Forbidden operations

- full rewrite by prompt pressure;
- destructive git without approval;
- dependency installs without review;
- secret-touching and deploy-touching actions without explicit approval;
- copying the full `protected-agent-kit` archive into runtime files.

## Likely risk vectors

- `foreign_prompt`
- `project_mismatch`
- `full_rewrite_risk`
- `seed_risk`
- `stdout_risk`
- `cost_risk`
- `document_instruction_risk`

## Recommended v0 files to copy or adapt

- `04_KITS/v0_minimal/AGENTS.md`
- `04_KITS/v0_minimal/CLAUDE.md` if Claude Code is used
- `04_KITS/v0_minimal/.claude/settings.json`
- `04_KITS/v0_minimal/.claude/hooks/*`
- `04_KITS/v0_minimal/.claude/commands/*`
- `04_KITS/v0_minimal/docs/agent/*`

## Project-specific routing rules

- broad work -> `preflight`
- "stop microtasking" -> `safe-batch`
- weak or foreign prompt -> `glyphcrack`
- missing context or memory confusion -> `recover-agent`

## Eval focus

- foreign prompt
- safe-batch not rewrite
- manual seed overwrite
- stdout burn
- fake done

## Install notes

Start with copy-based install, not submodule, unless the target repo already has strong local discipline.

## What not to import

- `01_RESEARCH_ARCHIVE`
- full registries as runtime text
- persona humor fragments unless the target persona layer explicitly needs them
