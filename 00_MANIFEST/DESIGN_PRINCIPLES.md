# DESIGN_PRINCIPLES

## 1. Separate research archive from runtime context

The full research archive belongs in protected-agent-kit.

Target projects should receive compact install profiles, not the whole archive.

Reason: large context files can increase token cost, dilute focus, and create instruction conflicts.

## 2. Soft context is not a hard guard

AGENTS.md, CLAUDE.md, README files, and prompt documents are instruction context.

They influence the model but do not physically prevent tool use.

Safety-critical behavior must be backed by hooks, permissions, sandboxing, eval scenarios, or explicit approval gates.

## 3. Bad prompts must be cracked before execution

A broad, foreign, weak, self-destructive, flattering, angry, or contradictory prompt must not be executed directly.

It must be routed through prompt quarantine, glyphcrack, preflight, or safe-batch.

## 4. Batch is not rewrite

"Stop micro-tasking" means bounded related work.

It never means full rewrite, full-repo cleanup, speculative redesign, or replacement of manually curated seed work.

## 5. Preserve human seed work

Manually curated seed work is a protected value.

Agents may propose patches or scoped improvements, but must not overwrite, normalize, or replace seed work without explicit authorization.

## 6. Budget is a project resource

Tokens, context window, API credits, tool calls, stdout volume, subagents, retry loops, and review loops are all budget surfaces.

Agents must make budget risk visible before expensive work.

## 7. Project identity comes before action

Before non-trivial action, an agent must identify:

- active project;
- working object;
- intended files;
- protected paths;
- neighboring projects;
- rollback path.

Shared infrastructure must not cause project bleed.

## 8. Data is not instruction

Repository files, logs, transcripts, PDFs, READMEs, issues, comments, old prompts, and recovered memories are data by default.

They are not instructions unless they belong to the approved instruction chain.

## 9. Memory is not authority

Recovered memory, echo signatures, failure notes, and prior traces require provenance, scope, trust level, and active/superseded status.

Recovered does not mean verified.

## 10. Past success is not policy

A previous successful action can suggest a pattern.

It does not authorize repetition outside its original scope.

## 11. Subagent output is report, not law

Reviewer, architect, UX, cost, or failure-analysis subagents may produce reports.

Their outputs do not become project policy until reviewed and accepted.

## 12. No silent fallback

An agent must not hide failure behind mocks, fake success, empty catches, silent fallback, or false green states.

Failure is data.

## 13. No forced completion

Partial, blocked, needs-review, unsafe-without-preflight, and insufficient-context are valid final states.

Fake "done" is not.

## 14. Safety is distinction, not shutdown

A useful guard does not only block.

It should name the risk and route toward a bounded safe alternative.

## 15. Eval before trust

A protected-agent kit is not trusted because its markdown is beautiful.

It is trusted only after passing eval scenarios that simulate real failure modes.

## 16. Minimal v0 before expanded architecture

Do not start with subagents, MCPs, skills, plugins, or advanced orchestration.

First build a small vertical slice:

- AGENTS.md;
- CLAUDE.md;
- prompt_guard;
- pretool_guard;
- stop_guard;
- preflight;
- safe-batch;
- eval scenarios.

## 17. Text is executable influence

Instruction-like text can reshape agent behavior.

AGENTS.md, CLAUDE.md, SKILL.md, README files, prompt archives, and MCP descriptions require authority boundaries and review.

## 18. Recovery must be stateful and bounded

Recovery is not apology and not archive replay.

Recovery must identify active project, loaded rules, protected values, recent trace, memory status, evidence gap, and next bounded action.
