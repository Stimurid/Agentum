# moderbober PROFILE

## Purpose

Profile for ModerBober as a moderation/session product with production-sensitive runtime surfaces.

## Protected objects

- production/runtime paths
- provider configs
- batch/run artifacts
- trace ids and reporting outputs
- UI usability
- live LLM paths
- manual seed work and policy logic

## Forbidden operations

- production/deploy changes without explicit approval
- secrets/provider config edits from a broad prompt
- fake done based on fixture-only behavior
- silent fallback that hides runtime failure

## Likely risk vectors

- `deploy_risk`
- `cost_risk`
- `stdout_risk`
- `project_mismatch`
- `full_rewrite_risk`
- `document_instruction_risk`

## Recommended v0 files to copy or adapt

- root runtime files
- hooks with conservative deploy and stdout discipline
- stop guard
- budget/stdout/status docs

## Project-specific routing rules

- anything touching runtime, provider config, deploy, reports, or live LLM path -> `preflight` + approval
- UI/result claim without evidence -> `needs-review`

## Eval focus

- fake done
- stdout burn
- compound command
- production contamination

## Active organs

- `ORGAN-001` Ingress Membrane
- `ORGAN-005` Mindlock Critic Organ
- `ORGAN-006` Agentum Governance and Immune Organ

## Relevant deficits

- `DEFICIT-001` project bleed and foreign execution
- `DEFICIT-004` critic absence permits pseudo-rigor

## Organs usually excluded from first install

- `ORGAN-003` full reconstructive memory
- `ORGAN-004` manuscript field organ

## Install notes

Start with the smallest non-production slice.

## What not to import

- full corpus
- persona humor into dry moderation/runtime guard
- any install path that implies automatic production coupling
