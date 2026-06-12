# LLM_SURFACE_AUDIT

This audit describes how the active projects currently expose LLM runtime, provider, UI/panel, hooks, and related control surfaces.

## Agentum

- folder: `C:\projects\protected-agent-kit`
- LLM/runtime surface:
  - no direct product LLM runtime at the repository root
  - runtime logic is preserved as installable kit slices and eval material
- role:
  - central authority, not end-product LLM app

## WhiteCrow + Litops

- folder: `C:\projects\conceptarticle`
- provider / runtime signals:
  - `.env`
  - `.env.example`
  - `.env.local`
  - `.env.mai.local`
  - `litops_config.json`
  - `requirements.txt`
- app/runtime/UI surface:
  - `mvp/`
  - `litops/`
  - `deploy/`
  - `litops_data/`
- Claude control surface:
  - `.claude/settings.json`
  - `.claude/hooks/`
  - `.claude/commands/`
- observed settings behavior:
  - explicit deny/ask shell policy
  - hook-based advisory routing for prompt quarantine and protected-path mutation
  - strong secret-path and destructive-command awareness
- assessment:
  - richest LLM control plane among the active projects
  - already close to the kind of installable runtime policy that Agentum wants to generalize

## ModerBober

- folder: `C:\projects\moderbober-recovery-clean`
- provider / runtime signals:
  - `docker-compose.yml`
- app/runtime/UI surface:
  - `backend/`
  - `frontend/`
  - `scripts/`
  - `artifacts/`
- LLM/agent signals:
  - `agents/`
  - `prompts/`
  - docs repeatedly mention LLM runtime, model gate, manual review, moderator cockpit
- root contract signals:
  - production URL must stay canonical
  - model changes are guarded
  - manual testing is blocked under weak LLM gate states
- assessment:
  - real runtime product with explicit LLM concerns
  - less formalized Claude-specific guard surface than WhiteCrow+Litops

## Quinta

- folder: `C:\projects\quinta`
- provider / runtime signals:
  - `.env.example`
  - `.env.local`
  - `package.json`
  - `eslint.config.js`
- app/runtime/UI surface:
  - `src/`
  - `server/`
  - `deploy/`
  - `product/`
  - `knowledge/`
  - `scripts/`
- observed provider hints:
  - `VITE_LLM_PROVIDER`
  - `VITE_LLM_API_BASE`
  - `VITE_LLM_MODEL`
  - `VITE_LLM_API_KEY`
  - UI-managed provider settings noted in `.env.example`
- Claude control surface:
  - `.claude/launch.json`
  - no root hook/settings surface found in this pass
- assessment:
  - strong app/runtime LLM surface
  - governance and provider control are present but not yet elevated into a full root policy layer

## Kairoskopion

- folder: `C:\projects\kairoskopion\Kairoskopion`
- provider / runtime signals:
  - `.env.example`
  - `pyproject.toml`
- app/runtime/UI surface:
  - `src/`
  - `scripts/`
  - `tests/`
  - `examples/`
  - `private_inputs/`
- LLM/agent signals:
  - documentation frames the project as evidence-first and bounded
  - project is positioned inside the Litops–WhiteCrow ecosystem, not as an isolated generic assistant
- assessment:
  - runtime and evidence pipeline exist
  - provider surface is present but comparatively light
  - likely easier to align with Agentum than a heavily bespoke UI repo

## Paideia

- folder: `C:\projects\Paideia`
- provider / runtime signals:
  - none observed in this pass
- app/runtime/UI surface:
  - none observed in this pass
- LLM/agent signals:
  - document corpus contains prompts, agentic orchestration waves, cases, meta-audits, and deep research notes
  - this suggests conceptual/authoring LLM usage, but not a formalized runtime surface
- assessment:
  - active LLM-content project
  - not yet structured as a provider-governed application or bounded agent-runtime repo

## Cross-project comparison

### Strongest formal LLM control plane

1. `C:\projects\conceptarticle`

### Strongest active runtime products with LLM implications

1. `C:\projects\moderbober-recovery-clean`
2. `C:\projects\quinta`

### Bounded evidence/runtime project

1. `C:\projects\kairoskopion\Kairoskopion`

### Content-active but runtime-light

1. `C:\projects\Paideia`

## Main ecosystem implication

The active ecosystem is not homogeneous.

There are at least three different current LLM shapes:

1. **full Claude control-plane + hooks + commands + provider settings**
   - `C:\projects\conceptarticle`

2. **product runtime with providers/UI/deploy but weaker root guard formalization**
   - `C:\projects\moderbober-recovery-clean`
   - `C:\projects\quinta`

3. **content-heavy / bounded-context / research-heavy projects with partial runtime formalization**
   - `C:\projects\kairoskopion\Kairoskopion`
   - `C:\projects\Paideia`

Agentum should standardize these without forcing every project into the same surface shape.
