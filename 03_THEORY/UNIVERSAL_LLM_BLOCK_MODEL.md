# UNIVERSAL_LLM_BLOCK_MODEL

## Purpose

This document defines the universal LLM block for the Agentum ecosystem.

The goal is not to force all projects into one app shape.

The goal is to give every project the same conceptual and operational skeleton for:

- provider choice
- runtime mode
- agent/prompt assembly
- retrieval/evidence use
- tool execution boundary
- budget and stdout discipline
- observability and rollback

This model must be wide enough to cover:

- WhiteCrow + Litops
- ModerBober
- Quinta
- Kairoskopion
- future generic coding repos
- future persona-agent or subject-agent environments

## What the LLM block is

The LLM block is not just "call a model."

It is the bounded layer that turns:

- user input
- project context
- prompt assets
- retrieval/evidence context
- tool permissions
- provider configuration

into:

- a governed model interaction
- a bounded agent run
- a traceable output
- an observable cost/risk event

The stronger ecosystem reading is:

the LLM block is one organ system inside a larger cognitive organism.

It works together with:

- memory substrate;
- prompt and agent library;
- critic layers;
- orchestration surfaces;
- project-specific organs.

It is therefore not only a provider/router stack.

It is also where:

- a scene is assembled;
- memory is selected and reconstructed;
- agents are placed into relation;
- traceability and rollback remain possible after synthesis.

## Universal block structure

Every serious project should be describable through these eleven surfaces.

These surfaces can also be read as an organism stack:

1. membrane;
2. digestion;
3. memory;
4. assembly;
5. critique;
6. synthesis;
7. orchestration;
8. governance.

### 1. Identity surface

Answers:

- what project is active
- what working object is active
- what repo/root path is active
- what neighboring projects must not be touched
- what protected paths exist

This surface prevents project bleed before any model call.

### 2. Intent surface

Answers:

- what the user is asking
- whether the request is narrow or broad
- whether it is coding, writing, moderation, research, recovery, or planning
- whether it is direct execution or needs preflight

This is where the risk vector begins.

But it is also where active context assembly begins.

The system should not only classify the user ask.

It should start answering:

- what must enter the working field now;
- what should stay outside;
- what is likely to overload or derail the run;
- what memory regime this task actually needs.

### 3. Runtime mode surface

Every project should explicitly name its runtime mode.

Minimum universal modes:

- `mock`
- `offline`
- `draft`
- `live`
- `auto`
- `recovery`

Meaning:

- `mock` = no real provider call; deterministic or simulated path
- `offline` = local evidence/process path without network model dependency
- `draft` = bounded draft generation with no autonomous tool follow-through
- `live` = real provider execution
- `auto` = policy-routed choice among modes
- `recovery` = state reconstruction / truth-check / bounded continuation mode

### 4. Provider surface

This is the model access layer.

The universal model must support at least these provider families:

- `anthropic_native`
- `openai_native`
- `openai_compatible`
- `litellm_router`
- `ollama_local`
- `none`

Notes:

- `openai_compatible` covers 302.ai and similar gateways
- `litellm_router` covers future brokered/provider-switched setups
- `ollama_local` covers local/private execution
- `none` is a valid state for deterministic or evidence-only runs

Minimum provider fields:

- provider family
- base URL if applicable
- model name
- API credential source
- embedding provider if separate
- reasoning/latency tier if relevant
- timeout policy
- retry policy
- streaming yes/no

### 5. Gateway surface

Some projects call a provider directly.
Some call a local server-side gateway.
Some call a worker queue.

The universal block must support:

- `direct_client`
- `local_gateway`
- `backend_service`
- `worker_queue`
- `manual_operator_injection`

Examples:

- Quinta uses gateway logic
- Litops can use direct/provider abstraction
- ModerBober uses backend/worker orchestration shape
- some future repos may require human-reviewed operator injection

### 6. Prompt and agent assembly surface

This is where the "agent" becomes a concrete runtime composition.

The universal block must support all of these prompt asset types:

- root operating files
- persona fragments
- method fragments
- prompt bodies
- stage/mode modifiers
- project identity fragments
- recovery fragments
- eval prompts

The universal agent assembly pipeline should be representable as:

1. root project contract
2. active role/agent selection
3. active task mode
4. project-local method fragments
5. bounded user task
6. optional evidence injection
7. optional guard modifiers

Important:

- AGENTS/CLAUDE are context, not hard enforcement
- persona layer must stay separable from runtime guard layer
- broad prompt must not directly rewrite prompt assets

The stronger version of this surface is not "assemble one prompt."

It is "assemble a working organ inside an active scene."

### 6.1. Prompt macroforms

The ecosystem already shows that prompt bodies are not only "long text."

Some of them behave as repeatable macroforms for assembling a working agent.

Useful observed macroforms include:

- seven-part forms
- eight-part forms

These are not sacred fixed numerologies.

They are compact assembly scaffolds that help keep an agent operationally complete.

Typical sections that recur across these forms are:

1. role / purpose / status
2. anti-role or forbidden modes
3. positive function
4. operational definitions
5. analysis dimensions or evaluation axes
6. autonomy and boundary rules
7. output format and reporting mode
8. memory / self-check / versioning

Implication:

- Agentum should treat such forms as reusable prompt skeletons
- but should not hard-code one mandatory count for every project
- the invariant is not "seven" or "eight"
- the invariant is coverage of role, boundary, method, memory, and output discipline

### 7. Evidence and retrieval surface

The LLM block must distinguish between:

- free generation
- evidence-conditioned generation
- retrieval-augmented synthesis
- provenance-preserving transformation
- publication/evaluation pipeline use

Universal retrieval/evidence modes:

- `none`
- `document_load`
- `structured_corpus`
- `fts_search`
- `vector_search`
- `hybrid_search`
- `external_adapter`

Examples:

- Litops leans toward corpus/provenance/vector shape
- ModerBober leans toward fragment/provenance/full-text shape
- Kairoskopion leans toward evidence/external-adapter/publication shape
- Quinta may use knowledge corpus without full RAG centrality

This surface must also answer a stronger memory question:

retrieval is not the same thing as memory.

Retrieval fetches candidate material.

Memory decides what kind of past is being reconstructed for the active task.

So the block should distinguish at least these memory regimes:

- factual recall;
- provenance recall;
- project continuity recall;
- role or stylistic recall;
- review or critic recall;
- scene-memory recall;
- suppressed or quarantined memory that must not silently return as authority.

The practical memory stack emerging across this ecosystem is:

- verbatim memory
- compressed memory
- normalized memory
- linked memory
- narrative memory
- graph or relation memory
- task-packet memory
- method memory

### 8. Tool execution surface

The LLM block must name whether the model:

- only writes text
- proposes commands
- executes tools through an agent runtime
- routes to subagents
- touches deployment/runtime surfaces

Minimum tool modes:

- `text_only`
- `propose_only`
- `bounded_tools`
- `review_required_tools`
- `runtime_mutation_blocked`

This surface connects directly to runtime guards, hooks, permissions, and approval gates.

### 9. Budget surface

The universal block must expose budget as a first-class project resource.

Budget is not only tokens.

Budget includes:

- prompt size
- retrieved context size
- model price tier
- expected number of calls
- retries
- subagent multiplication
- stdout volume
- review overhead
- operator time

Minimum budget flags:

- `cost_risk`
- `stdout_risk`
- `loop_risk`
- `context_bloat_risk`
- `subagent_amplification_risk`

### 10. Observability surface

Every project should be able to answer:

- what prompt assembly was used
- what provider/model was used
- what evidence was loaded
- what tools were proposed/executed
- what output was produced
- what cost/risk state was observed
- what failed

Minimum observability objects:

- run record
- provider record
- prompt version or layer signature
- evidence set reference
- tool trace
- status result

The stronger version required by this ecosystem is not only trace observability.

It is also context observability:

- which fragments entered the working field;
- which fragments were excluded;
- which attractors dominated the run;
- where interference between lines started;
- what compressed memory replaced verbatim evidence.

This should be understood not merely as debugging.

It is visibility of the fate of meaning fragments inside the run:

- used
- dropped
- distorted
- became dominant
- got suppressed
- generated a new candidate organ

For stronger scene-aware orchestration, observability should also include:

- what scene core or working object was active;
- what positions or agents entered the scene;
- what unresolved glyphs or ambiguities were carried forward;
- what outer environment or evidence shell bounded the run.

### 11. Output and rollback surface

The LLM block must name what kind of output it emits.

Universal output classes:

- suggestion
- draft
- patch
- report
- extraction
- synthesis
- decision support
- routed stop

Every nontrivial output should also answer:

- can it be rolled back
- did it mutate files/state
- does it require review
- is it final or partial

## Universal risk routing inside the LLM block

The LLM block is governed by the risk vector, not by a childish allow/deny switch.

Minimum shared flags:

- `foreign_prompt`
- `project_mismatch`
- `full_rewrite_risk`
- `cost_risk`
- `stdout_risk`
- `seed_risk`
- `deploy_risk`
- `memory_authority_risk`
- `document_instruction_risk`
- `weak_prompt_or_pressure`
- `safe_batch_requested`

Minimum universal routes:

- `preflight`
- `glyphcrack`
- `safe-batch`
- `recovery`
- `truth-check`
- `approval`
- `stop`

## Universal deployment shapes

The same LLM block must support multiple project deployment shapes.

### Shape A — direct guarded coding-agent runtime

Used when:

- the agent runs inside Claude Code / Codex
- hooks and command routing are local
- files are the main working object

Typical projects:

- generic coding repos
- Agentum install profiles
- WhiteCrow guard layer

### Shape B — app + provider + operator panel

Used when:

- there is a live frontend
- provider settings are operator-visible
- model runs are part of an app workflow

Typical projects:

- Quinta
- WhiteCrow MVP surface

### Shape C — backend/worker orchestration

Used when:

- agent runs are queued
- backend policies gate execution
- multiple agents or reviewers participate

Typical projects:

- ModerBober

### Shape D — evidence-first CLI/runtime

Used when:

- evidence pipeline matters more than chat UX
- model use is bounded and auditable
- external scholarly adapters matter

Typical projects:

- Kairoskopion

### Shape E — corpus-first / research-first / not yet embodied

Used when:

- ontology and research exist
- runtime shell is still weak or absent

Typical projects:

- Paideia for now

### Shape F — diagnostic or pedagogical analysis agent

Used when:

- the agent evaluates structured traces of work
- the output must stay analytic rather than assistive
- memory, versioning, and self-check are first-class
- the result must remain comparable across participants, sessions, or iterations

Typical donors:

- seven-part and eight-part diagnostic prompt forms
- educational analysis materials
- MemoryWorkbench-style review and memory routing logic

### Shape G — cognitive organism workbench

Used when:

- multiple specialized organs cooperate across one ecology;
- memory is reconstructive rather than merely persistent;
- prompt bodies, modules, and roles are treated as versioned working objects;
- the system may later generate new organs from recurring deficits.

Typical local contour:

- Litops;
- MemoryWorkbench;
- WhiteCrow;
- Kairoskopion;
- ModerBober;
- Quinta;
- Mindlock;
- Agentum.

## Universal model families by project need

The LLM block should not pretend one model family fits every task.

Use model families by job:

### Fast cheap operational model

Use for:

- routing
- classification
- extraction
- formatting
- first-pass draft work

### Strong reasoning model

Use for:

- difficult synthesis
- critique
- methodological resolution
- contradiction handling
- recovery planning

### Long-context model

Use for:

- large corpus reads
- prompt-body inspection
- evidence comparison
- transcript-heavy work

### Local/private model

Use for:

- privacy-sensitive drafts
- low-stakes local iteration
- fallback when external provider should not be used

### No-model mode

Use for:

- deterministic transformation
- archive navigation
- state inspection
- recovery indexing
- validation steps that do not require generation

## What each active project wants from the universal block

### Agentum

Needs:

- vocabulary
- install profiles
- risk routing
- sync/update contract
- eval coverage

It does not need a product-facing panel as a core requirement.

### WhiteCrow + Litops

Needs:

- strongest prompt-body governance
- provenance-aware retrieval
- provider flexibility
- layered prompt assembly
- guarded operator routing

### ModerBober

Needs:

- backend/worker shape
- run records
- mock/live/auto clarity
- agent contract discipline
- provenance and review queue integration

### Quinta

Needs:

- gateway/provider abstraction
- app-visible provider state
- method-agent workbench
- bounded direct/live execution

### Kairoskopion

Needs:

- evidence-first mode
- openai-compatible path
- offline bounded mode
- adapter-aware retrieval
- strong observability honesty

### Paideia

Needs:

- first a runtime shell
- then provider vocabulary
- then corpus-to-runtime translation

It is also a likely donor of pedagogical and orchestration prompt forms rather than only a future target repo.

## Orchestration principle

The universal LLM block should not treat orchestration as mere command-and-control.

A stronger working definition is:

orchestration = organization of interaction among semi-autonomous agents, spaces, and representations so that they can enter productive relation without collapsing into one rigid command chain

This means:

- not every agent is centrally scripted
- not every interaction is free swarm chaos
- the system needs interfaces, screens, bundles, and shared objects that let agents "see" one another
- coordination can be achieved through common spaces, common artifacts, and mutual visibility, not only through top-down dispatch

It also means the block should be able to host a working scene, not only a queue.

A serious run may need:

- a scene core;
- a bounded goal structure;
- a visible subject-object crossing;
- an outer evidence environment;
- a mnemonic shell that preserves what the scene has already become.

This distinction matters especially for:

- multi-agent moderation
- university-orchestration concepts
- subject-bearing agent ecologies
- future agent-generation and agent-selection layers

## Canonical config skeleton

Every project should be able to map its LLM block into a compact config skeleton like this:

```text
project_identity
runtime_mode
provider_family
provider_endpoint
model_name
embedding_provider
gateway_shape
agent_assembly_profile
retrieval_mode
tool_mode
budget_policy
approval_policy
observability_target
output_class
rollback_class
```

This is not a demand for one literal file format.

It is the minimum conceptual schema that lets Agentum compare different repos without flattening them.

## Canonical organism objects

The ecosystem is now converging on two central cross-project objects.

### AgentOrgan

This is the stable record of an operational organ.

Minimum fields:

```text
id
name
project_scope
deficit_origin
function
input_contract
output_contract
memory_dependencies
context_requirements
tools_allowed
test_scenes
evaluation_criteria
failure_modes
lineage
parent_organs
child_organs
mutation_history
activation_policy
observability_hooks
provenance_policy
quarantine_status
```

### Deficit

This is the stable record of recurrent project pressure that may require a new organ.

Minimum fields:

```text
id
observed_in_project
source_fragment
failure_type
semantic_loss
repeated_count
suspected_cause
required_capability
candidate_organs
test_scene
resolved_by
unresolved_status
```

These are not yet mandatory file formats.

They are the clearest current schema for turning this ecosystem from prompt folklore into organ-level engineering.

## What must not happen

The universal block must not collapse into:

- "just use one model everywhere"
- "just dump the big prompt"
- "just let the agent figure it out"
- "just attach every archive file"
- "just use mock until someone notices"
- "just wire tools directly with no routing"
- "just upgrade all projects at once from memory"

## Practical conclusion

The universal LLM block is a federation schema.

It lets different projects keep different embodiments:

- coding-agent shell
- app workbench
- backend worker system
- evidence CLI
- research corpus awaiting embodiment

while still sharing one operational language for:

- provider choice
- runtime mode
- agent assembly
- evidence use
- tool boundaries
- risk routing
- budget visibility
- traceability
- rollback

That is the right level of unification for the current ecosystem.

The more exact current formula is:

Agentum is becoming the governance and evolution library for a multi-project cognitive organism, not only a protected-agent runtime kit.
