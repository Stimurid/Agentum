# PROJECT_CHARTER

## Project name

protected-agent-kit

## Purpose

protected-agent-kit is a standalone infrastructure repository for protected coding-agent work.

Its purpose is to preserve and operationalize research, patterns, failure modes, runtime guards, install profiles, and evaluation scenarios for Claude Code, Codex, and compatible coding-agent environments.

The project exists because agent configuration must not live only in a chat, in memory, or inside a single target project. It must be portable, versioned, inspectable, and reusable across projects.

## Core problem

A coding agent can receive a broad, foreign, expensive, destructive, or context-contaminated prompt and execute it directly.

The observed failure class is:

bad / broad / foreign / expensive prompt
→ immediate agent execution
→ token burn / destructive edits / project drift / seed-work damage / false completion

protected-agent-kit replaces this with:

prompt
→ risk vector
→ preflight / glyphcrack / safe-batch / recovery
→ bounded action or honest stop

## Scope

This repository stores:

- research archive from the investigation waves;
- source registry;
- pattern registry;
- failure-mode registry;
- golden formulations;
- anti-patterns;
- theory notes;
- v0 portable protected-agent kit;
- install profiles for target projects;
- eval scenarios and test prompts;
- handoff prompts for installing the kit into projects.

## Non-goals

This repository is not:

- a target application repository;
- a runtime product;
- a generic prompt dump;
- a marketplace of unreviewed skills, MCPs, subagents, or hooks;
- a place to install project-specific secrets or deployment configuration;
- a replacement for project-level AGENTS.md / CLAUDE.md;
- a reason to inject the whole research archive into every agent context.

## Canonical location

Local canonical path:

C:\projects\protected-agent-kit

## First intended install targets

1. Litops
2. ModerBober
3. WhiteCrow
4. Quinta / FifthConstraint
5. Generic coding repositories

## Main distinction

This repository stores the full research and design corpus.

Target repositories should receive only selected install profiles and compact runtime files.

Do not copy the whole research archive into a target project's runtime agent context.

## Protected values

protected-agent-kit protects:

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
- non-servile architectural judgment.

## Success criterion

The project is successful when a bad, broad, foreign, or budget-dangerous prompt cannot directly become an expensive agentic session.

It must be routed through quarantine, preflight, bounded batching, recovery, or refusal with a safe alternative.

## First implementation phase

The first phase is archival and structural:

- create the repository skeleton;
- backfill research waves;
- backfill source, pattern, and failure registries;
- create the minimal v0 kit;
- create install profiles;
- create eval scenarios.

No target project installation happens until the corpus and v0 kit are explicit.
