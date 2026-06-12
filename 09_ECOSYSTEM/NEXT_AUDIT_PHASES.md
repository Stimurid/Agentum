# NEXT_AUDIT_PHASES

This file defines the next audit phases after the first active-project registry and the first agent/LLM surface pass.

## Phase 2 — standardization wave planning

Target projects:

- WhiteCrow + Litops
- ModerBober
- Quinta
- Kairoskopion
- Paideia

Questions:

- which root files must be normalized first;
- which projects already have strong local governance worth preserving;
- which projects need bootstrap rather than replacement;
- which local contracts must stay project-specific.

## Phase 3 — UI / operator experience audit

Target projects:

- WhiteCrow + Litops
- ModerBober
- Quinta
- Kairoskopion

Questions:

- what are the current main operator workflows;
- where are the interface anti-patterns;
- which projects suffer from layout sludge, state opacity, or unusable density;
- where do we need canvas/workbench discipline;
- what screens need redesign before more features.

## Phase 4 — provider and access normalization

Questions:

- which projects use Anthropic / OpenAI-compatible / mock / local providers;
- where keys and env assumptions live;
- where provider settings are UI-driven vs file-driven;
- where there is secret-risk or operator-confusion risk.

## Phase 5 — install profile hardening

Questions:

- does each active project need its own Agentum profile revision;
- what layers are runtime-only vs subject-layer vs persona-layer;
- what should never be auto-installed.

## Phase 6 — eval wave

Questions:

- which current projects need UI/UX eval prompts;
- which need provider/runtime guard prompts;
- which need ontology/persona drift prompts.

## Immediate next move

The most valuable immediate next move is:

1. UI / operator experience audit across the active runtime projects;
2. then project-by-project standardization wave planning.
