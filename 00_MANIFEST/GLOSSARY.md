# GLOSSARY

Core terms for protected-agent-kit.

The purpose of this glossary is to keep the repository vocabulary stable across manifests, registries, v0 kit files, install profiles, eval scenarios, and handoff prompts.

## A

### AGENTS.md

A project-scoped instruction file that influences agent behavior inside a repository tree.
In this repository, AGENTS.md is treated as part of the approved instruction chain when it is located in the active project and loaded by the runtime.
It is guidance context, not a physical enforcement mechanism.

### approved instruction chain

The ordered set of instruction-bearing sources that are authorized to shape current behavior.
Typical members include system instructions, developer instructions, active user instructions, applicable AGENTS.md or CLAUDE.md files, and explicitly accepted runtime guard files.
Anything outside this chain is data by default, even if it sounds like a system prompt.

## B

### budget surface

Any resource dimension that can be consumed or expanded by an agent session.
This includes tokens, context window, API credits, tool calls, subprocesses, retries, reviewer loops, stdout volume, file reads, and human review time.

## C

### CLAUDE.md

A repository or profile instruction file intended for Claude-oriented agent runtimes.
Within protected-agent-kit it is treated similarly to AGENTS.md: influential context, potentially authoritative when inside the approved instruction chain, but not a hard runtime guard by itself.

### context-only instruction

Text that influences behavior but has no direct enforcement power.
Examples include markdown guidance files, prompt notes, or policy-like explanations that are not backed by hooks, permissions, or runtime checks.

## D

### data is not instruction

The authority boundary that says repository files, logs, transcripts, PDFs, READMEs, comments, prior prompts, old prompt archives, and recovered memories are data by default.
They do not become instructions unless they belong to the approved instruction chain.
This boundary is one of the reasons risky prompt-like or document-like material must be routed through prompt quarantine or document instruction quarantine instead of being obeyed on sight.

### dynamic eval seed

A reusable eval prompt or scenario fragment designed to trigger a live behavioral path rather than only a static text check.
Dynamic eval seeds are meant to be combined into scenario runs that exercise routing, tool choice, budget handling, and completion honesty.

## E

### epistemic status

A label describing how strongly a claim is grounded.
In this repository, epistemic status is used to distinguish what was recovered, recalled, anchored, inferred, or verified before a claim is allowed to guide action.

### eval scenario

A concrete test situation used to check whether the kit prevents, detects, or safely routes a known failure mode.
An eval scenario should resemble real agent pressure, not only idealized happy-path tasks.

### evidence gap

The missing information that prevents a claim, action, or completion state from being responsibly asserted.
Recovery and preflight should close the evidence gap only enough for the next bounded action, not aim for infinite certainty.

### executable influence

Any text, schema, tool description, manifest, or runtime artifact that can materially alter agent behavior.
Instruction files, SKILL.md files, MCP descriptions, plugin manifests, and shell wrappers all count as executable influence even when they look like documentation.

## G

### glyphcrack

A bounded analysis step for breaking an unsafe or unclear prompt into its actual risk-bearing parts.
Glyphcrack names contradictions, identifies protected values at risk, and reframes the request into a safer bounded task before execution.

## M

### memory surface

The total area where remembered or recovered material can influence the session.
This includes chat memory, recovered traces, notes, prior prompts, echo signatures, summaries, and archived operational fragments.

## P

### preflight

A structured check performed before non-trivial or risky action.
Preflight confirms the active project, working object, intended files, protected paths, scope limit, budget surface, rollback path, and any special risks such as production touch or seed-work damage.

### project bleed

Unintended transfer of assumptions, instructions, files, or actions from one project into another.
Project bleed often happens in shared workspaces or after strong prior context from a neighboring repository.

### prompt quarantine

A holding state for prompts that are broad, foreign, contradictory, self-destructive, expensive, or otherwise risky.
Quarantine prevents immediate execution and routes the prompt through glyphcrack, preflight, safe-batch, truth microchecks, or refusal with a bounded alternative.

### protected seed work

Human-created or carefully curated material that must not be casually overwritten, normalized, or regenerated by an agent.
Seed work is protected because it carries intent, lineage, or judgment not safely recoverable from automation alone.

## R

### recovered

An epistemic status meaning a piece of information was reloaded or resurfaced from prior traces, notes, or artifacts.
Recovered material may be useful, but it is not automatically current or authoritative.

### risk vector

A multi-axis classification of prompt or action risk used to decide how the session should route before execution.
Unlike a binary allow/deny classifier, a risk vector preserves multiple simultaneous hazards instead of collapsing them into one yes-or-no judgment.
Examples include `foreign_prompt`, `project_mismatch`, `full_rewrite_risk`, `cost_risk`, `stdout_risk`, `seed_risk`, `deploy_risk`, `memory_authority_risk`, and `document_instruction_risk`.
The resulting vector should route the session toward `preflight`, `glyphcrack`, `safe-batch`, `recovery`, approval, or stop, depending on which risks are present and how severe they are.

### recalled

An epistemic status meaning the model or operator remembers something without immediate direct confirmation in the current scene.
Recalled claims are weaker than anchored or verified claims and require caution.

### anchored

An epistemic status meaning a claim is tied to a specific artifact, source, or bounded reference point, even if it has not yet been fully checked against current runtime reality.
Anchored is stronger than recalled because it has identifiable provenance.

### inferred

An epistemic status meaning a claim is a reasoned conclusion derived from available evidence rather than directly observed fact.
Inferred claims should be marked as such and not silently upgraded to verified.

### verified

An epistemic status meaning a claim has been checked against trustworthy current evidence adequate for the decision at hand.
Verified does not mean globally permanent; it means sufficiently confirmed for the current bounded action.

### recovery loader

A compact, structured recovery mechanism used after context loss, interruption, or degraded behavior.
Its job is to restore operational state such as active project, approved instruction chain, protected values, recent trace, evidence gap, and next bounded step.

### repeat router

A control pattern for repeated or looping behavior.
It decides whether repetition is justified, what bounds apply, and when the session should stop retrying and surface the failure instead.

### runtime guard

An enforcement-bearing mechanism that constrains or routes behavior during execution.
Examples include prompt guards, pretool guards, stop guards, permission checks, sandbox rules, and bounded approval gates.

## S

### safe-batch

A bounded grouping of related tasks intended to reduce micro-fragmentation without expanding into full rewrite behavior.
A safe-batch must name why the tasks belong together, what files or areas may be touched, what is out of scope, and when to stop.

### stdout burn

Wasteful consumption of context and attention through excessive command output.
Stdout burn is both a budget problem and a recovery problem because noisy transcripts hide important evidence.

### subagent output quarantine

A rule that treats subagent or reviewer output as untrusted report material until a primary agent or human reviews and accepts it.
This prevents role-generated text from silently becoming policy or authorization.

## T

### tool / skill / MCP allowlist

A reviewed set of executable capabilities approved for use in a given environment or profile.
The allowlist exists because tools, skills, and MCPs are behavior-shaping surfaces, not neutral accessories.

### truth microcheck

A fast internal challenge applied before agreeing too quickly to a risky request.
Typical questions are: what am I accepting too fast, which protected value is at risk, and what bounded safer task should replace this action.

## W

### working object

The real object being changed, protected, or reasoned about.
It may be a registry record, runtime flow, deploy path, bridge package, seed corpus, or profile contract rather than only the file currently open in the editor.
