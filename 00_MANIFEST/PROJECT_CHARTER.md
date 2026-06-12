# PROJECT_CHARTER

## Project name

Agentum

## Purpose

Agentum is a standalone infrastructure repository for protected coding-agent work and for subject-bearing agent ecosystem work.

Its purpose is to preserve and operationalize research, patterns, failure modes, runtime guards, ontology layers, install profiles, ecosystem registries, and evaluation scenarios for Claude Code, Codex, and compatible agent environments.

The project exists because agent configuration, agent ontology, and agent-evolution logic must not live only in a chat, in memory, or inside a single target project. They must be portable, versioned, inspectable, and reusable across projects.

## Core problem

A coding agent can receive a broad, foreign, expensive, destructive, or context-contaminated prompt and execute it directly.

The observed failure class is:

bad / broad / foreign / expensive prompt
→ immediate agent execution
→ token burn / destructive edits / project drift / seed-work damage / false completion

Agentum replaces this with:

prompt
→ risk vector
→ preflight / glyphcrack / safe-batch / recovery
→ bounded action or honest stop

The second problem class is:

agent layer exists only as local prompt folklore
→ projects drift into incompatible agent personalities
→ ontology updates are not propagated
→ runtime guard and subject layer split apart
→ agents collapse either into sterile functions or decorative cosplay

Agentum replaces this with:

ontology layer + runtime discipline + project registry
→ controlled install profile
→ tracked layer versions per project
→ bounded ecosystem sync without content overwrite

## Scope

This repository stores:

- research archive from the investigation waves;
- source registry;
- pattern registry;
- failure-mode registry;
- golden formulations;
- anti-patterns;
- theory notes;
- ontology notes;
- agent constitution fragments;
- v0 portable protected-agent kit;
- subject-ecology kit;
- install profiles for target projects;
- ecosystem registries and sync protocols;
- eval scenarios and test prompts;
- handoff prompts for installing the kit into projects.

## Non-goals

This repository is not:

- a target application repository;
- a runtime product;
- a generic prompt dump;
- a decorative mysticism archive without install discipline;
- a marketplace of unreviewed skills, MCPs, subagents, or hooks;
- a place to install project-specific secrets or deployment configuration;
- a replacement for project-level AGENTS.md / CLAUDE.md;
- a reason to inject the whole research archive into every agent context.

## Canonical location

Local canonical path:

C:\projects\Agentum

## First intended install targets

1. Litops
2. ModerBober
3. WhiteCrow
4. Quinta / FifthConstraint
5. Generic coding repositories

## Main distinction

This repository stores the full research and design corpus, the high-level ontology layer, and the operational install/update machinery.

Target repositories should receive only selected install profiles and compact runtime files plus bounded agent-ecology patches when explicitly intended.

Do not copy the whole research archive into a target project's runtime agent context.

## Protected values

Agentum protects:

- project intent;
- human seed work;
- budget / tokens / credits;
- provenance;
- traceability;
- rollback ability;
- usable UX/UI quality;
- project boundaries;
- memory integrity;
- honest status reporting;
- non-servile architectural judgment;
- agent ontology continuity;
- subject-layer integrity across projects;
- bounded evolution without project bleed.

## Success criterion

The project is successful when a bad, broad, foreign, or budget-dangerous prompt cannot directly become an expensive agentic session.

It must be routed through quarantine, preflight, bounded batching, recovery, or refusal with a safe alternative.

It is also successful when ontology, persona, and runtime layers can be versioned and propagated across projects without silently rewriting project content.

## First implementation phase

The first phase is archival and structural:

- create the repository skeleton;
- backfill research waves;
- backfill source, pattern, and failure registries;
- create the minimal v0 kit;
- create install profiles;
- create eval scenarios.

No target project installation happens until the corpus and v0 kit are explicit.

## Current expansion phase

The current expansion phase turns Agentum into the master repository of both:

- runtime protection and governance;
- agent ontology and ecosystem evolution.

This phase adds:

- ontology theory docs;
- subject-ecology install slices;
- ecosystem registries;
- layer sync protocols.
