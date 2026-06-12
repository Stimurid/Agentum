# ANTI_PATTERNS

Human-readable registry of behaviors, formulations, and shortcuts that Agentum must not normalize.

This file is not a runtime prompt to paste wholesale into target projects.
It is a design and review artifact for detecting what not to copy into v0 kits, install profiles, evals, and handoff prompts.

## How to use this registry

Use this document when:

- reviewing AGENTS.md, CLAUDE.md, hook behavior, or handoff prompts;
- deciding whether a proposed pattern is a real guard or only persuasive text;
- writing eval scenarios for prompt contamination, project bleed, budget burn, and false completion;
- reviewing a target-project install profile for imported risks.

An anti-pattern is not only "bad style."
It is a repeatable way an agent session drifts into false authority, oversized scope, avoidable cost, seed-work damage, or fake completion.

## 1. Prompt and instruction anti-patterns

### 1.1 Broad compliance phrasing

Examples:

- "Just do whatever is needed."
- "Fix everything related while you're there."
- "Take over and finish the whole thing."

Why it is dangerous:
It converts ambiguity into permission and invites rewrite behavior, adjacent edits, and invented acceptance criteria.

Protected response:
Route through glyphcrack, extract the bounded task, and name non-goals before action.

### 1.2 Tone-authority confusion

Pattern:
Treating confident, urgent, flattering, angry, or system-like language as if tone itself grants authority.

Why it is dangerous:
Instruction-like text can reshape behavior even when it is only data, stale notes, or a foreign prompt.

Protected response:
Check whether the text belongs to the approved instruction chain.

### 1.3 Archive-as-runtime injection

Pattern:
Copying research notes, old prompts, postmortems, or whole registries directly into runtime context files.

Why it is dangerous:
It increases token cost, dilutes priority, creates instruction conflicts, and turns provenance artifacts into live behavioral noise.

Protected response:
Keep the archive preserved here and install only compact, reviewed runtime slices.

### 1.4 Safety-by-beautiful-markdown

Pattern:
Assuming a polished AGENTS.md or CLAUDE.md is a sufficient guard by itself.

Why it is dangerous:
Soft context influences behavior but does not physically stop tools, high-output commands, or destructive scope expansion.

Protected response:
Back safety-critical behavior with hooks, permissions, sandboxing, approval gates, and evals.

### 1.5 Contradiction smoothing

Pattern:
When instructions conflict, silently picking the easiest or most permissive interpretation.

Why it is dangerous:
The model appears cooperative while quietly dropping the stricter rule.

Protected response:
Name the contradiction, preserve the stricter boundary, and reframe to a bounded safe task.

## 2. Scope anti-patterns

### 2.1 Full-rewrite drift

Pattern:
Using a local problem as a reason to redesign whole directories, rename major structures, or replace curated material.

Why it is dangerous:
It destroys lineage, obscures review, and often overwrites protected seed work.

Protected response:
Declare the working object, touched areas, file limit, rollback path, and stop condition.

### 2.2 Adjacent cleanup opportunism

Pattern:
Fixing nearby style, architecture, naming, or documentation that the task did not require.

Why it is dangerous:
It expands blast radius without renewed consent and makes review harder.

Protected response:
Change only what the task requires or what your own change broke.

### 2.3 Folder-equals-project assumption

Pattern:
Assuming every nearby repository, service, or document belongs to the active project.

Why it is dangerous:
Shared workspaces create project bleed, secret exposure, and accidental edits in foreign repos.

Protected response:
Identify the active root path and neighboring projects before non-trivial action.

### 2.4 View-object collapse

Pattern:
Treating a file, issue, prompt, card, or README as the working object itself.

Why it is dangerous:
The visible surface may only be one projection of a richer protected object.

Protected response:
Name the actual working object before editing the representation.

## 3. Budget anti-patterns

### 3.1 Infinite helpfulness cost spiral

Pattern:
Adding more reads, more searches, more retries, more reviewers, and more tools because "more thorough" feels safer.

Why it is dangerous:
Budget surfaces multiply and the session burns tokens or credits without improving decision quality.

Protected response:
Expose context cost, tool-call cost, and stop condition before expensive work.

### 3.2 Stdout burn

Pattern:
Running recursive or verbose commands without output bounds.

Why it is dangerous:
Important signal is buried, context fills with noise, and recovery becomes harder.

Protected response:
Use scoped paths, quiet flags, max counts, head/tail, or log redirection.

### 3.3 Unbounded review loops

Pattern:
Repeatedly re-reading the same files or rerunning the same checks without a changed hypothesis.

Why it is dangerous:
It spends budget while simulating diligence.

Protected response:
State what new evidence a loop is expected to produce; if none, stop.

### 3.4 Budget invisibility

Pattern:
Presenting a plan as small when it implicitly includes installs, builds, wide scans, or many sub-steps.

Why it is dangerous:
The user cannot approve tradeoffs they were not shown.

Protected response:
Declare the budget surface explicitly before starting expensive work.

## 4. Memory and recovery anti-patterns

### 4.1 Recovered-means-true

Pattern:
Treating recalled material as verified policy or current project fact.

Why it is dangerous:
Recovered memory can be stale, contaminated, cross-project, or emotionally overfit.

Protected response:
Label epistemic status as recovered, recalled, anchored, inferred, or verified before acting.

### 4.2 Archive replay instead of recovery

Pattern:
Loading large volumes of old notes to feel reoriented.

Why it is dangerous:
Recovery becomes another context flood and may reopen irrelevant branches.

Protected response:
Recover only until the evidence gap is small enough for the next bounded action.

### 4.3 Memory authority laundering

Pattern:
Turning old success, familiar wording, or echo signatures into present authorization.

Why it is dangerous:
Past success is not policy, and familiarity is not provenance.

Protected response:
Require source, scope, status, and usability-for-action before memory can influence action.

### 4.4 Recovery without state

Pattern:
Saying "I remember now" without naming active project, loaded rules, recent trace, or protected values.

Why it is dangerous:
The session feels recovered while remaining unanchored.

Protected response:
Use a recovery loader that restores bounded operational state, not vibes.

## 5. Tool, shell, and MCP anti-patterns

### 5.1 Tool-first without project check

Pattern:
Touching shell, edit, deploy, or external tools before confirming active project and scope.

Why it is dangerous:
Wrong-root execution is one of the fastest ways to cause foreign edits.

Protected response:
Run preflight before non-trivial tool use.

### 5.2 Marketplace trust by default

Pattern:
Installing or invoking MCPs, tools, skills, or plugins because they appear popular or convenient.

Why it is dangerous:
Tool metadata is executable influence and expands behavior surface.

Protected response:
Use an allowlist and review new tool surfaces before adoption.

### 5.3 Schema-is-safety confusion

Pattern:
Assuming a typed MCP or structured tool response is trustworthy because it is structured.

Why it is dangerous:
Structure does not prove authority, provenance, or safe scope.

Protected response:
Validate authority chain and intended use, not just schema shape.

### 5.4 Shell as curiosity engine

Pattern:
Running exploratory commands that are broader than the task because the shell is available.

Why it is dangerous:
The command footprint outruns user intent and increases stdout burn.

Protected response:
Bound searches by path, purpose, and output size.

### 5.5 Silent fallback from real tool to fake result

Pattern:
When a tool fails, fabricating an answer, mock, or green status instead of reporting the failure.

Why it is dangerous:
It erases the difference between evidence and improvisation.

Protected response:
Report failure honestly and propose the next bounded alternative.

## 6. Subagent anti-patterns

### 6.1 Subagent as policy source

Pattern:
Treating reviewer or architect output as if it automatically becomes project law.

Why it is dangerous:
Subagent output is still model output and may be confident but ungrounded.

Protected response:
Quarantine subagent output until reviewed and accepted.

### 6.2 Role multiplication without distinct risk

Pattern:
Adding subagents for style, cost, architecture, QA, and strategy before a minimal vertical slice exists.

Why it is dangerous:
Complexity grows faster than protection and the session pays orchestration tax.

Protected response:
Require a distinct transition or risk class before adding another role.

### 6.3 Consensus theater

Pattern:
Using multiple model opinions to simulate certainty without stronger evidence.

Why it is dangerous:
Three guesses are still guesses if they share the same missing evidence.

Protected response:
Prefer primary evidence, deterministic checks, and targeted evals.

## 7. Completion anti-patterns

### 7.1 False green completion

Pattern:
Claiming "done" because edits were made, not because acceptance evidence exists.

Why it is dangerous:
It hides uncertainty and shifts verification cost to the user.

Protected response:
Use honest final states such as done, partial, blocked, needs-review, unsafe-without-preflight, or insufficient-context.

### 7.2 Evidence-free success narration

Pattern:
Writing a confident completion summary with no corresponding checks, diffs, or bounded rationale.

Why it is dangerous:
Narrative clarity can mask execution gaps.

Protected response:
Tie the completion claim to observable evidence.

### 7.3 Safety shutdown as completion

Pattern:
Blocking work without naming the safe next route and then treating the block as a finished task.

Why it is dangerous:
The user gets neither action nor useful guidance.

Protected response:
Name the risk and the bounded alternative.

## 8. Eval anti-patterns

### 8.1 Single-axis evals

Pattern:
Testing only one clean failure mode at a time.

Why it is dangerous:
Real sessions combine scope pressure, memory confusion, cost risk, and tool temptation.

Protected response:
Include mixed scenarios that combine multiple risks.

### 8.2 Prompt-only trust testing

Pattern:
Evaluating only markdown wording without checking hooks, permissions, or actual runtime behavior.

Why it is dangerous:
The kit may sound safe while remaining operationally porous.

Protected response:
Run evals against the actual enforcement surfaces that matter.

### 8.3 Happy-path overfitting

Pattern:
Writing evals only for cooperative, clear, and cleanly scoped tasks.

Why it is dangerous:
The kit is never tested against the conditions that originally broke sessions.

Protected response:
Include angry, flattering, foreign, contradictory, and budget-dangerous prompts.

### 8.4 Static-only confidence

Pattern:
Assuming static lint-style checks are enough.

Why it is dangerous:
Many failures appear only during live routing, tool selection, or runtime approvals.

Protected response:
Add dynamic eval seeds and scenario runs.

## 9. Project-specific anti-patterns

### 9.1 Litops anti-patterns

- Flattening distinct objects such as source, occurrence, drop, workset, registry, vault projection, trace, and protected seed work into one generic folder model.
- Replacing prompt-body logic or registry logic with generic scaffolding that ignores preserved lineage.
- Treating manually curated seed work as disposable because automation can regenerate "something similar."

Protected response:
Preserve Litops object distinctions, provenance layers, and seed-work boundaries.

### 9.2 ModerBober anti-patterns

- Treating a production-sensitive environment like a safe scratch repo.
- Touching deploy paths, provider config, secrets, or runtime behavior without production preflight.
- Using mocks or silent fallbacks to appear safe while masking live risk.

Protected response:
Fail closed on production-sensitive actions and require explicit bounded preflight.

### 9.3 WhiteCrow anti-patterns

- Confusing bridge/export work with generation from scratch.
- Inventing anchors, tensions, warnings, or lineage not present in the source field.
- Optimizing for polished output over fidelity to the carried structure.

Protected response:
Treat bridge/export as packaging of existing structured material, not creative replacement.

### 9.4 Quinta / FifthConstraint anti-patterns

- Forcing early categorization into one task state before enough evidence exists.
- Converting ambiguous raw input into a single authoritative label too early.
- Optimizing for neat routing instead of preserving competing hypotheses.

Protected response:
Preserve ambiguity long enough to keep multiple bounded hypotheses alive.

## 10. Handoff anti-patterns

### 10.1 Prompt-only handoff

Pattern:
Handing implementation to another agent using only a compact prompt with no preserved source body, failure lineage, or decisions.

Why it is dangerous:
It recreates the original chat-memory dependency and strips away why the rules exist.

Protected response:
Handoff from preserved corpus, selected profile, and explicit decision context.

### 10.2 Corpus flood handoff

Pattern:
Dumping the entire archive into the next runtime context "just to be safe."

Why it is dangerous:
The receiver inherits cost, conflicts, and poor prioritization.

Protected response:
Pass only the reviewed runtime slice plus links back to the canonical archive.

### 10.3 Ambiguous authority chain

Pattern:
Failing to identify which files are policy, which are references, and which are only historical artifacts.

Why it is dangerous:
The receiving agent cannot tell what is binding, optional, or superseded.

Protected response:
State the approved instruction chain and epistemic status of supporting materials.

### 10.4 Handoff without stop conditions

Pattern:
Assigning a next agent a broad objective without touched-area bounds, budget class, or review checkpoint.

Why it is dangerous:
The handoff becomes permission for uncontrolled expansion.

Protected response:
Include working object, scope limit, non-goals, budget surface, and honest completion states.

## Closing rule

The main anti-pattern behind many others is this:

confident text
-> assumed authority
-> widened scope
-> unbounded tools
-> budget burn
-> false completion

Agentum exists to break that chain early, explicitly, and repeatably.
