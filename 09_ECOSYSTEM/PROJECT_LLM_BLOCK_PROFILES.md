# PROJECT_LLM_BLOCK_PROFILES

This file translates the universal LLM block into concrete recommended profiles for the active ecosystem projects.

It is not a deployment script.

It is the operational mapping layer between:

- project identity
- provider/gateway shape
- retrieval/evidence shape
- tool/approval shape
- guard install priority

## 1. Agentum

- path: `C:\projects\protected-agent-kit`
- role: master framework repository
- profile type: `control_library`

### Recommended block

- runtime mode: `draft`, `recovery`, `auto`
- provider family: `none` by default, optional `openai_compatible` for research or eval work
- gateway shape: `direct_client`
- retrieval mode: `document_load`, `structured_corpus`
- tool mode: `bounded_tools`, `review_required_tools`
- output classes: `report`, `patch`, `routed stop`, `install profile`

### Why

- Agentum is not a product runtime
- it governs profiles, theory, evals, and sync
- its LLM use should stay bounded and infrastructure-oriented

### Install priority

- keep strong root governance
- keep evals and install profiles explicit
- do not turn Agentum into a chat product shell

## 2. WhiteCrow + Litops

- path: `C:\projects\conceptarticle`
- role: ontology-heavy manuscript and source-metabolism environment
- profile type: `full_control_plane`

### Recommended block

- runtime mode: `live`, `draft`, `recovery`, `auto`
- provider family: `openai_compatible` primary, optional `openai_native`, optional `ollama_local`
- gateway shape: `direct_client` now, optional `local_gateway` later
- retrieval mode: `structured_corpus`, `vector_search`, `hybrid_search`, `document_load`
- tool mode: `bounded_tools`, `review_required_tools`
- output classes: `draft`, `synthesis`, `extraction`, `patch`, `decision support`

### Why

- this is the richest current prompt/agent/control-plane repo
- it already has hooks, commands, prompt-body governance, corpus logic, and provider discipline
- retrieval and provenance are central, not optional garnish

### Install priority

- preserve prompt-body governance
- preserve source/provenance lineage
- strengthen root identity presentation
- keep risk routing visible before broad corpus or prompt-body work

## 3. ModerBober

- path: `C:\projects\moderbober-recovery-clean`
- role: moderation/workspace runtime product
- profile type: `worker_orchestrated_product`

### Recommended block

- runtime mode: `mock`, `live`, `auto`, `recovery`
- provider family: `openai_compatible` primary, optional `anthropic_native`, optional `litellm_router`
- gateway shape: `backend_service`, `worker_queue`
- retrieval mode: `fts_search`, `structured_corpus`, optional `hybrid_search`
- tool mode: `review_required_tools`, `runtime_mutation_blocked`
- output classes: `report`, `extraction`, `synthesis`, `decision support`

### Why

- ModerBober is already shaped as backend + frontend + worker orchestration
- mock/live policy matters here more than in most repos
- provenance, review queue, and run records must stay first-class

### Install priority

- unify provider vocabulary
- formalize run observability
- keep mock/live/auto semantics explicit
- do not let agent runs impersonate confirmed product truth

## 4. Quinta

- path: `C:\projects\quinta`
- role: invention and TRIZ workbench
- profile type: `gateway_workbench`

### Recommended block

- runtime mode: `live`, `draft`, `auto`, `recovery`
- provider family: `anthropic_native`, `openai_compatible`
- gateway shape: `local_gateway`, optional `direct_client`
- retrieval mode: `document_load`, `structured_corpus`, optional `hybrid_search`
- tool mode: `bounded_tools`, `review_required_tools`
- output classes: `draft`, `synthesis`, `decision support`, `patch`

### Why

- Quinta already thinks in terms of provider abstraction and gateway routing
- its surface is operator-facing and method-heavy
- it needs clean provider visibility without guard bloat

### Install priority

- add stronger root governance symmetry
- keep provider/gateway status legible
- protect method agents from broad rewrite requests

## 5. Kairoskopion

- path: `C:\projects\kairoskopion\Kairoskopion`
- role: evidence-first publication-positioning system
- profile type: `evidence_cli`

### Recommended block

- runtime mode: `offline`, `live`, `draft`, `recovery`
- provider family: `openai_compatible` primary, optional `none`
- gateway shape: `direct_client`
- retrieval mode: `external_adapter`, `structured_corpus`, `document_load`
- tool mode: `propose_only`, `bounded_tools`
- output classes: `extraction`, `synthesis`, `report`, `decision support`

### Why

- Kairoskopion is strongest when evidence and publication logic stay primary
- it already distinguishes operational paths from stubs and broken paths
- offline bounded mode is a real feature, not a fallback fiction

### Install priority

- keep epistemic status explicit
- keep external evidence adapters visible
- strengthen root governance without bloating the runtime

## 6. Paideia

- path: `C:\projects\Paideia`
- role: educational and institutional agentic research corpus
- profile type: `corpus_first_pending_runtime`

### Recommended block

- runtime mode: `draft`, `offline`, `recovery`
- provider family: `none` initially, optional `openai_compatible` after runtime shell exists
- gateway shape: `manual_operator_injection` initially
- retrieval mode: `document_load`, `structured_corpus`
- tool mode: `text_only`, `propose_only`
- output classes: `report`, `synthesis`, `install plan`

### Why

- Paideia is not yet a hardened runtime repo
- its first need is a compact agent shell, not premature provider complexity
- corpus intelligence exists; embodiment is the missing layer

### Install priority

- bootstrap root operating files
- define working object and protected corpus paths
- only then add provider/gateway/runtime layers

## Cross-project profile table

| Project | Profile | Runtime modes | Provider shape | Gateway shape | Retrieval shape | Guard intensity |
|---|---|---|---|---|---|---|
| Agentum | `control_library` | `draft`, `recovery`, `auto` | `none` -> optional `openai_compatible` | `direct_client` | corpus/docs | high |
| WhiteCrow + Litops | `full_control_plane` | `live`, `draft`, `recovery`, `auto` | `openai_compatible` first | `direct_client` -> later `local_gateway` | corpus + vector + hybrid | very high |
| ModerBober | `worker_orchestrated_product` | `mock`, `live`, `auto`, `recovery` | brokerable/product-facing | `backend_service`, `worker_queue` | FTS + provenance | high |
| Quinta | `gateway_workbench` | `live`, `draft`, `auto`, `recovery` | `anthropic_native` + `openai_compatible` | `local_gateway` | knowledge/doc-driven | medium-high |
| Kairoskopion | `evidence_cli` | `offline`, `live`, `draft`, `recovery` | `openai_compatible` + `none` | `direct_client` | evidence/adapters | high |
| Paideia | `corpus_first_pending_runtime` | `draft`, `offline`, `recovery` | `none` first | `manual_operator_injection` | corpus/docs | low now, should rise later |

## Ecosystem-wide rules

These rules should hold across all profiles:

1. data is not instruction
2. memory is not authority
3. project identity before action
4. risk vector before broad execution
5. batch is not rewrite
6. human seed work is protected
7. budget/stdout risk must be visible
8. mock must not impersonate live success
9. recovery is state reconstruction, not apology
10. ontology sync must not rewrite project content

## Rollout order

Recommended order for profile hardening:

1. WhiteCrow + Litops
2. ModerBober
3. Quinta
4. Kairoskopion
5. Paideia

Reason:

- WhiteCrow + Litops is the richest live reference
- ModerBober and Quinta are the strongest runtime products
- Kairoskopion is bounded and clean, so alignment is easier
- Paideia first needs embodiment before higher-order provider work

## Practical conclusion

The universal LLM block should be installed as profile variants, not as one monolithic universal prompt.

That gives the ecosystem one language for:

- providers
- modes
- gateways
- retrieval
- tool boundaries
- risk routing
- observability

without forcing all projects to behave like the same application.
