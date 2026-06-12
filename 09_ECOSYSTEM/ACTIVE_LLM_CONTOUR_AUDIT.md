# ACTIVE_LLM_CONTOUR_AUDIT

This audit maps the active project ecosystem by real LLM contour, not by folder noise.

Focus:

- provider surface
- runtime surface
- agent and prompt surface
- service/control-plane surface
- search/retrieval/evidence pipeline surface
- root operating files (`AGENTS.md`, `CLAUDE.md`, hooks, settings, install-like docs)

This is not a UI beauty audit. It is an operational map of where the agentic and LLM machinery actually lives.

## 1. Agentum

- path: `C:\projects\protected-agent-kit`
- role: master library for protected coding-agent and persona-agent practice
- LLM shape:
  - no end-product provider runtime at root
  - no app panel or live gateway as product surface
  - repository acts as ontology / guard / install / eval authority
- agent surface:
  - root `AGENTS.md`
  - root `CLAUDE.md`
  - kits, profiles, handoff prompts, evals, ecosystem registries
  - separate persona-fragment layer
- service surface:
  - install profiles
  - runtime-readable guard kits
  - ecosystem sync documents
  - project registries
- search / retrieval / pipeline:
  - no local product RAG service
  - retrieval logic is preserved as theory, profile, and install material rather than app code
- assessment:
  - this is the control library, not the application runtime
  - it should govern the ecosystem, not impersonate a target repo

## 2. WhiteCrow + Litops

- path: `C:\projects\conceptarticle`
- role:
  - WhiteCrow = ontology-heavy field/manuscript agent ecology
  - Litops = corpus / provenance / source-metabolism subsystem inside the same repo
- root operating layer:
  - `AGENTS.md`
  - `CLAUDE.md`
  - `.claude/settings.json`
  - `.claude/hooks/`
  - `.claude/commands/`
- provider surface:
  - `.env`
  - `.env.example`
  - `.env.local`
  - `.env.mai.local`
  - `litops_config.json`
  - `litops/llm.py`
- provider model:
  - explicit `openai_compatible` path
  - 302.ai documented as the confirmed working route
  - embedding provider is separately named for vector RAG
  - preset logic is already present in the app surface
- runtime surface:
  - `litops/` Python runtime
  - `mvp/` app/runtime shell
  - `deploy/`
  - `litops_data/`
  - `workbench/`
  - `tests/`
- agent and prompt surface:
  - `prompt_bodies/` with bodies, templates, generated, activation policy, registry
  - `prompts/`
  - large live agent registry and mode/stage system
  - over-agent strip
  - prompt inspector and layered prompt assembly
- service/control-plane surface:
  - Claude hooks for prompt/pretool/stop routing
  - explicit command surface for `preflight`, `glyphcrack`, `safe-batch`, `recover-agent`, `truth-check`, `repeat-router`
  - protected-path and seed-work awareness
  - runtime profile docs in `docs/agent/`
- search / retrieval / provenance surface:
  - corpus and extracted fragments directories
  - source/provenance logic is a first-class project concern
  - vector/RAG path is named in env surface
  - Litops acts as source metabolism, not just text generation
- actual shape:
  - this is the strongest existing LLM control plane in the ecosystem
  - it already combines provider config, agent registry, prompt assembly, runtime hooks, corpus handling, and guarded operator commands
- main weakness:
  - root presentation is historically noisy
  - live logic is richer than the top-level repo story

## 3. ModerBober

- path: `C:\projects\moderbober-recovery-clean`
- role: active moderation/workbench runtime product
- root operating layer:
  - `AGENTS.md`
  - `README`-family docs
  - extensive architecture and contract documents
- provider surface:
  - `docker-compose.yml`
  - backend worker/provider policy endpoints
  - model/provider fields in run manifests and run objects
- runtime surface:
  - `backend/`
  - `frontend/`
  - `agents/`
  - `prompts/`
  - `scripts/`
  - `artifacts/`
- agent and prompt surface:
  - explicit `agents/` directory with named agent units
  - explicit `prompts/` directory
  - pipeline templates define ordered multi-agent flows
  - agent contract files define types, schemas, review requirements, runtime fields
- service/control-plane surface:
  - worker loop runtime
  - execution request flow
  - provider capabilities seeding
  - provider policies seeding
  - moderator workspace / cockpit framing
- search / retrieval / evidence surface:
  - object model includes fragments, analytical units, provenance, review history, run logs
  - declared search path is PostgreSQL full text first
  - pgvector is prepared conceptually but not foundational
- actual shape:
  - this is a real application runtime with an agent workspace and orchestration logic
  - however much of current execution is still mock-oriented or review-gated
  - LLM infrastructure exists as a product skeleton rather than as a fully mature live provider plane
- main weakness:
  - weaker Claude-specific root guard surface than WhiteCrow + Litops
  - less compact central operating memory

## 4. Quinta

- path: `C:\projects\quinta`
- role: FifthConstraint / TRIZ invention workbench
- root operating layer:
  - `CLAUDE.md`
  - `README.md`
  - knowledge and architecture docs
  - no comparable root `AGENTS.md` observed in this pass
- provider surface:
  - `.env.example`
  - `.env.local`
  - `server/llmGateway.ts`
  - `server/standaloneGateway.ts`
  - frontend provider settings logic in `src/`
- provider model:
  - supports `anthropic`
  - supports `openai-compatible`
  - includes gateway/direct mode logic
  - supports fallback from Anthropic to openai-compatible when key reality requires it
  - UI-managed settings are explicitly acknowledged
- runtime surface:
  - `src/`
  - `server/`
  - `deploy/`
  - `product/`
  - `knowledge/`
  - `scripts/`
- agent and prompt surface:
  - agent methods live in app code and knowledge docs
  - prompt import / prompt handling exists in `src/`
  - project is already built as a multi-view, multi-method analytical workbench
- service/control-plane surface:
  - HTTP LLM gateway
  - status endpoint
  - provider settings routed through frontend and server
  - deployment documents and provider audits show repeated runtime iteration
- search / retrieval / evidence surface:
  - knowledge corpus is strong
  - more emphasis on method and workbench flow than on source-metabolism/RAG
  - evidence handling exists, but not as explicitly central as in Litops or Kairoskopion
- actual shape:
  - strong live LLM application surface
  - closer to a real operator tool than to a prompt folder
  - already thinks in terms of runtime/provider separation
- main weakness:
  - root guard/governance layer is thinner than the app itself
  - Claude runtime contract is informative but not yet symmetrical with Agentum-grade root enforcement vocabulary

## 5. Kairoskopion

- path: `C:\projects\kairoskopion\Kairoskopion`
- role: evidence-first publication-positioning system
- root operating layer:
  - `CLAUDE.md`
  - `README.md`
  - docs and knowledge corpus
  - no root `AGENTS.md` observed in this pass
- provider surface:
  - `.env.example`
  - `pyproject.toml`
  - Python package/CLI structure
- provider model:
  - explicit openai-compatible provider path
  - 302.ai-compatible base URL naming
  - optional external academic adapters
  - can run bounded/offline paths without live provider
- runtime surface:
  - `src/`
  - `scripts/`
  - `tests/`
  - `examples/`
  - `private_inputs/`
- agent and prompt surface:
  - multiple agent roles are named in audit/spec docs
  - project distinguishes real operational agents from useful stubs and broken paths
  - strong honesty about what is implemented, offline, gated, or incomplete
- service/control-plane surface:
  - Python CLI/runtime rather than browser-first app
  - evidence pipeline and academic integration points are part of the actual operating shape
  - ecosystem links to Litops/WhiteCrow are explicit
- search / retrieval / evidence surface:
  - this is where Kairoskopion is strongest
  - publication/evidence/venue logic is central
  - external adapters and validation docs matter more than chat-style assistant posture
- actual shape:
  - smaller runtime surface than Quinta or ModerBober
  - much stronger evidence honesty than generic prompt repos
  - one of the easiest projects to align cleanly with Agentum because it already thinks in bounded contour terms
- main weakness:
  - root governance symmetry is incomplete
  - operator contract is more documented than enforced

## 6. Paideia

- path: `C:\projects\Paideia`
- role: educational/research corpus around LLMs, agentic orchestration, gateways, and institutional use
- root operating layer:
  - no formal runtime repo layer observed
  - no root `AGENTS.md`
  - no root `CLAUDE.md`
  - no root `README.md` observed in this pass
- provider surface:
  - no local app/runtime provider config surface observed
- runtime surface:
  - none clearly productized in this pass
- agent and prompt surface:
  - strong prompt/research corpus
  - many documents about agentic orchestration, gateways, prompt libraries, secure institutional AI access, and multi-agent educational patterns
- service/control-plane surface:
  - described conceptually inside the research corpus
  - not yet concretized as local runtime, hooks, settings, or deployment surface
- search / retrieval / evidence surface:
  - rich document corpus
  - not yet shaped as an executable evidence pipeline or governed application surface
- actual shape:
  - conceptually important
  - operationally still a corpus, not a standardized runtime project
- main weakness:
  - everything important is still mostly in documents
  - no local operator guard shell for coding agents yet

## Cross-project shape map

### A. Full control-plane project

- `C:\projects\conceptarticle`

This is the only active project that already combines:

- root agent files
- Claude settings
- Claude hooks
- Claude commands
- provider configuration
- prompt-body governance
- app/runtime surface
- corpus/provenance metabolism

### B. Runtime products with real LLM surfaces but thinner root governance

- `C:\projects\moderbober-recovery-clean`
- `C:\projects\quinta`

These are not just prompt folders. They already have live runtime logic, services, and multi-part operator surfaces. Their weakness is not absence of LLM machinery; it is weaker guard unification.

### C. Bounded evidence system with honest partiality

- `C:\projects\kairoskopion\Kairoskopion`

This is the cleanest evidence-first contour. It is less panel-heavy, but more epistemically disciplined than most app-shaped repos.

### D. Corpus-first project without hardened runtime shell

- `C:\projects\Paideia`

This is strategically important material, but not yet an operational agent-runtime repo.

## What the ecosystem actually has

Across the active projects, the LLM contour is not one thing. It currently exists as at least five different layers:

1. **Provider layer**
   - env files
   - gateway code
   - model/provider policy
   - mock/live/auto switching

2. **Agent/prompt layer**
   - prompt bodies
   - agent registries
   - method libraries
   - pipeline templates
   - persona/method framing docs

3. **Runtime/service layer**
   - browser app shells
   - backend workers
   - CLI runtimes
   - local gateways
   - deployment skeletons

4. **Evidence/search/provenance layer**
   - corpus fragments
   - analytical units
   - provenance links
   - retrieval/search paths
   - publication/evidence adapters

5. **Guard/governance layer**
   - `AGENTS.md`
   - `CLAUDE.md`
   - Claude hooks/settings/commands
   - install profiles
   - evals
   - handoff prompts

## The real integration problem

The problem is not "some projects have agents and some do not."

The real problem is that these layers are unevenly distributed:

- WhiteCrow + Litops has the strongest guard/control-plane layer
- ModerBober and Quinta have stronger live product runtime than formalized root governance
- Kairoskopion has stronger epistemic discipline than flashy operator shell
- Paideia has conceptual intelligence but not runtime embodiment
- Agentum has the clearest governance library but is not itself a target runtime

## What Agentum should standardize next

Agentum should not flatten all projects into one prompt format.

It should standardize the following across active projects:

1. root operating files
   - compact `AGENTS.md`
   - compact `CLAUDE.md`
   - project identity and protected values docs

2. provider contract vocabulary
   - provider mode
   - gateway/direct shape
   - mock/live/auto semantics
   - budget/stdout/provider-risk visibility

3. agent surface vocabulary
   - what counts as agent
   - what counts as prompt body
   - what counts as working object
   - what must not be regenerated blindly

4. evidence and provenance contract
   - source lineage
   - traceability
   - retrieval/search honesty
   - memory is not authority

5. install/sync model
   - central ontology evolution in Agentum
   - local profile install into active repos
   - update path that changes agent contour without rewriting project substance

## First practical conclusion

If the goal is unified control over agents, prompts, ontology, and LLM services across the ecosystem, then the right model is:

- Agentum = central ontology, guard library, profile library, sync authority
- WhiteCrow + Litops = richest live reference implementation
- ModerBober = runtime moderation/workspace branch
- Quinta = invention/workbench branch
- Kairoskopion = evidence/publication branch
- Paideia = conceptual-research branch awaiting runtime shell

That is already enough to move from vague "many projects with AI somewhere inside" to a concrete ecosystem architecture.
