# AGENT_SURFACE_AUDIT

This audit describes how the active projects currently implement agent/prompt surfaces, root governance files, and local operating contracts.

## Agentum

- folder: `C:\projects\protected-agent-kit`
- root files:
  - `AGENTS.md`
  - `CLAUDE.md`
  - `README.md`
  - `START_HERE_AGENTUM.md`
- agent surface:
  - root governance is explicit and now self-hosting
  - theory, kits, profiles, evals, handoff prompts, and ecosystem registries are all first-class product parts
- assessment:
  - strongest central governance repo
  - still library-shaped rather than runtime-app-shaped
  - canonical source of the model, not a product target

## WhiteCrow + Litops

- folder: `C:\projects\conceptarticle`
- root files:
  - `AGENTS.md`
  - `CLAUDE.md`
  - `README.md`
- agent surface:
  - strongest existing live agent surface in the ecosystem
  - `.claude/settings.json`
  - `.claude/hooks/prompt_guard.py`
  - `.claude/hooks/pretool_guard.py`
  - `.claude/hooks/stop_guard.py`
  - `.claude/commands/`
  - large `docs/` corpus with agent constitution, ontology, control plane, prompt audit, runtime matrix
  - prompt-body governance explicitly routes broad work to guarded review
- special note:
  - root `README.md` is stale/misaligned and currently reads like an export pack, not like the live project identity
  - root `AGENTS.md` and `CLAUDE.md` carry the real live contract much better than the README
- assessment:
  - highest maturity of existing agent governance
  - most important source of real operating practice
  - prime candidate for careful extraction into Agentum without flattening

## ModerBober

- folder: `C:\projects\moderbober-recovery-clean`
- root files:
  - `AGENTS.md`
  - `README.md`
- agent surface:
  - root governance exists and is product-aware
  - repo has explicit `agents/` directory
  - repo has explicit `prompts/` directory
  - docs include product law, ops gates, architecture, classification and UX audits
  - root contract includes production URL rules, secret discipline, model discipline, and manual-test gating
- missing / weaker parts:
  - no root `CLAUDE.md` observed
  - no visible `.claude/hooks` or root Claude settings surface in this pass
- assessment:
  - active agent-aware runtime product
  - governance is present but less unified than WhiteCrow+Litops
  - strong candidate for Agentum profile alignment

## Quinta

- folder: `C:\projects\quinta`
- root files:
  - `CLAUDE.md`
  - `README.md`
- agent surface:
  - root `CLAUDE.md` is quite informative and already names the project, working root, legacy archive, and accepted documentation base
  - there is a `.claude/` directory, but in this pass it exposes only `launch.json`
  - root docs strongly frame identity as FifthConstraint / quint rather than generic TRIZ bot
- missing / weaker parts:
  - no root `AGENTS.md` observed
  - no visible root hook/settings/commands layer comparable to WhiteCrow+Litops
- assessment:
  - identity is strong, but governance surface is incomplete
  - should receive a cleaner Agentum-grade root governance layer

## Kairoskopion

- folder: `C:\projects\kairoskopion\Kairoskopion`
- root files:
  - `CLAUDE.md`
  - `README.md`
- agent surface:
  - project identity is explicit and bounded
  - `CLAUDE.md` already frames ecosystem position and what the project is not
  - docs corpus is strong and includes architecture, compatibility, spec, validation, and operator-manual materials
  - no root `AGENTS.md` observed in this pass
- assessment:
  - already ontology-aware and ecosystem-aware
  - needs stronger root governance symmetry if it is to align fully with Agentum standards

## Paideia

- folder: `C:\projects\Paideia`
- root files:
  - none of `AGENTS.md`, `CLAUDE.md`, `README.md` were observed in this pass
- agent surface:
  - current visible surface is a live document corpus
  - filenames indicate agentic orchestration, deep research, cartography, structural filtering, cases, prompts, and meta-audit
  - no formal runtime guard or structured root governance was observed
- assessment:
  - active project in content terms
  - not yet shaped as a standardized agent-runtime repo
  - would require a bootstrap pass before full Agentum alignment

## Cross-project comparison

### Strongest current agent-governance surface

1. `C:\projects\conceptarticle`
2. `C:\projects\protected-agent-kit`

### Medium but incomplete

1. `C:\projects\moderbober-recovery-clean`
2. `C:\projects\quinta`
3. `C:\projects\kairoskopion\Kairoskopion`

### Content-active but governance-light

1. `C:\projects\Paideia`

## First-wave standardization priority

1. Agentum
2. WhiteCrow + Litops
3. ModerBober
4. Quinta
5. Kairoskopion
6. Paideia
