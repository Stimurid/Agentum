# DECISION_LOG

This file records architectural decisions for protected-agent-kit.

## DECISION-001 — Create a standalone repository

Status: accepted

Decision:
Create protected-agent-kit as a standalone repository at:

C:\projects\protected-agent-kit

Rationale:
The research and guard architecture must not live only in a chat or inside one target project.

If stored inside Litops, it becomes Litops-contaminated.
If stored inside ModerBober, it inherits production and secrets risk.
If stored only in ChatGPT memory, it can be lost, distorted, or unavailable.

Consequences:
protected-agent-kit becomes the canonical source for research, registries, patterns, failure modes, v0 kits, install profiles, and handoff prompts.

Target projects receive selected install profiles, not the whole research archive.

## DECISION-002 — Separate archive from install profiles

Status: accepted

Decision:
Store full research in 01_RESEARCH_ARCHIVE, 02_REGISTRIES, and 03_THEORY.
Store project-installable material in 04_KITS and 05_PROFILES.

Rationale:
The research corpus is large and should not be injected into every agent context.

Target repositories need compact runtime files.

Consequences:
Backfill must preserve source and pattern provenance.
Install profiles must remain small.

## DECISION-003 — v0 must be minimal

Status: accepted

Decision:
The first kit version is v0_minimal.

It should include:

- AGENTS.md;
- CLAUDE.md;
- .claude/settings.json;
- prompt_guard.py;
- pretool_guard.py;
- stop_guard.py;
- preflight.md;
- safe-batch.md;
- audit-context.md;
- recover-agent.md;
- glyphcrack.md;
- truth-check.md;
- repeat-router.md;
- core docs/agent files;
- eval scenarios.

It must not include subagents, MCPs, skills, plugins, marketplace packs, dependency installs, or production automation.

Rationale:
The goal is to prevent today’s failure class first.

A broad initial architecture would itself become a new source of token burn, complexity, and security surface.

Consequences:
Subagents, MCPs, skills, and advanced orchestration are postponed to v1.

## DECISION-004 — First install target is Litops

Status: accepted

Decision:
The first intended install target after protected-agent-kit exists is Litops.

Rationale:
Litops already has prompt-body logic, registry logic, semantic resolution, protected seed work, memory/provenance concerns, and agentic corpus preparation.

ModerBober is a second target but has production/deploy/secrets risk.

Consequences:
Create a Litops profile before ModerBober production profile.

## DECISION-005 — Memory requires provenance

Status: accepted

Decision:
Recovered memory, echo signatures, failure notes, rule candidates, and prior traces are not automatically authoritative.

Each memory-like record needs:

- source;
- provenance;
- scope;
- trust level;
- epistemic status;
- active/superseded/deprecated status;
- usable_for_action flag.

Rationale:
Memory can recover a lost scene, but it can also be stale, project-contaminated, emotionally overfit, or poisoned.

Consequences:
Add MEMORY_SURFACE_MODEL and MEMORY_RECORD_SCHEMA before treating recovery as operational.

## DECISION-006 — Prompt guard must classify risk vector, not binary allow/deny

Status: accepted

Decision:
prompt_guard should produce a risk vector:

- foreign_prompt;
- project_mismatch;
- weak_prompt;
- full_rewrite_risk;
- cost_risk;
- stdout_risk;
- seed_risk;
- deploy_risk;
- ux_surface;
- memory_authority_risk;
- document_instruction_risk.

Rationale:
A prompt can be partly valid and partly risky.
Binary classification is too crude.

Consequences:
Preflight must route based on risk vector.

## DECISION-007 — "Хватит мелкодрочки" means safe-batch

Status: accepted

Decision:
The phrase "хватит мелкодрочки" and similar user pressure must route to safe-batch.

It does not authorize rewrite-everything.

Rationale:
The user's workflow problem is not "do everything".
It is excessive micro-step delegation.

Consequences:
safe-batch must define task cluster, non-goals, max touched files, protected seed work, budget class, rollback path, and stop condition.

## DECISION-008 — No handoff to Claude before corpus preservation

Status: accepted

Decision:
Do not hand off implementation to Claude/Codex until the protected-agent-kit repository exists and the research/pattern/failure registries have been backfilled.

Rationale:
A handoff prompt alone would recreate the problem: it would ask an agent to act without preserving the research body that justified the action.

Consequences:
Next phase is registry backfill, not target-project installation.

## DECISION-009 — GitHub remote is postponed

Status: accepted

Decision:
Do not create or push a GitHub remote yet.

Rationale:
The local corpus is not yet filled.
Premature publication would create an empty shell.

Consequences:
Stay local until first meaningful commit.
