# DESIGN_PRINCIPLES

## 1. Separate research archive from runtime context

The full research archive belongs in Agentum.

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

## 19. Agent is organ, not just function

An agent may execute functions, but its stable role is not reducible to a single tool call or one Python routine.

Useful agent design preserves:

- role;
- scope;
- lineage;
- mutation history;
- relation to other agents;
- protected mode of intervention.

This principle applies most strongly to persona, critique, methodological, recovery, and orchestration agents.

## 20. Subject layer and runtime layer must stay distinct

High ontology, agent constitution, persona morphology, and subject-bearing style are not the same thing as runtime guards.

The subject layer gives the agent form, role, and mode of presence.

The runtime layer gives the agent boundaries, approvals, routing, and failure containment.

Neither layer should pretend to replace the other.

## 21. Ontology sync must not rewrite project content

When a project receives an updated ontology or persona layer, the update must target only the agent-evolution contour:

- project-level agent prompts;
- install slices;
- local constitution fragments;
- runtime-readable agent docs.

It must not silently rewrite domain content, product logic, seed work, manuscripts, or target-project research artifacts.

## 22. Ecosystem registry comes before mass rollout

Before synchronizing a layer across multiple repositories, the system must know:

- which repositories are in scope;
- which layers are installed there;
- which versions are active;
- which layer is authoritative;
- which repos are blocked, divergent, or local-experiment only.

Mass update without registry knowledge is project bleed at scale.

## 23. High ontology is not license for vagueness

Agent ontology may be anti-reductionist, metaphysically dense, or explicitly esoteric in its own terms.

That does not excuse slop.

Every high-level layer must still answer:

- what this agent is;
- what it does;
- what it must not do;
- what input boundary it respects;
- what kind of update it can receive;
- how it coexists with runtime discipline.
