# SUBJECT_LAYER_VS_RUNTIME_LAYER

## The distinction

This repository now carries both:

- a subject layer;
- a runtime layer.

They are coupled, but they are not the same thing.

## Subject layer

The subject layer defines:

- who or what the agent is;
- what kind of role it inhabits;
- what false form it resists;
- what kind of mutation it can undergo;
- what style of presence is proper to it.

Typical files:

- constitution fragments;
- ontology docs;
- role patches;
- lineage patches;
- persona fragments.

## Runtime layer

The runtime layer defines:

- what the agent may execute;
- what routes to preflight;
- what counts as foreign prompt;
- what needs approval;
- how budget and stdout are bounded;
- what stop condition applies.

Typical files:

- `AGENTS.md`;
- `CLAUDE.md`;
- hooks;
- settings;
- eval prompts;
- install profiles.

## Failure if confused

If subject layer is mistaken for runtime layer:

- the system becomes poetic but unsafe.

If runtime layer is mistaken for subject layer:

- the system becomes safe-looking but spiritually empty and brittle.

## Correct relation

The runtime layer constrains action.

The subject layer shapes presence, role, and quality of intervention.

Both must be installed intentionally.
