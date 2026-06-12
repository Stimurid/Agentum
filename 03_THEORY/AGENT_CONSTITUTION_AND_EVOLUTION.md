# AGENT_CONSTITUTION_AND_EVOLUTION

## Constitution

An agent constitution is the compact statement of what kind of being and worker the agent is allowed to be.

It is above:

- concrete prompts;
- local style choices;
- tool preferences;
- transient patches.

It defines invariants.

## What the constitution must answer

A usable constitution answers:

- what this agent protects;
- what it refuses to flatten;
- what it treats as data;
- what it treats as instruction;
- what kind of intervention it performs;
- what kind of mutation is permitted;
- what layer outranks it when conflict appears.

## Constitution levels

This repository uses three practical constitution levels.

### Full Constitution

For new architecture, new agent families, ecosystem redesign, and ontology changes.

### Operational Constitution

For working agent prompts, install slices, and profile-specific layers.

### Micro-Vow

For short frequent prompts where only the essential invariant can fit.

## Evolution

Agent evolution here does not mean uncontrolled self-rewrite.

It means tracked change in one or more of:

- constitution wording;
- role boundaries;
- lineage memory;
- mutation rules;
- persona layer;
- install profile;
- runtime routing.

## Mutation types

Useful mutation categories:

- `guard_patch` — safer boundary, same role;
- `role_refinement` — sharper intervention, same family;
- `lineage_patch` — better memory of prior distinctions;
- `persona_patch` — better form of presence;
- `ontology_patch` — changed high-level invariant;
- `profile_patch` — better project-specific installation behavior.

## What evolution must not become

Evolution must not become:

- silent drift;
- untracked repo-wide prompt rewrite;
- unauthorized persona replacement;
- seed overwrite disguised as modernization;
- global sync without project registry review.

## Evolution authority

In this framework, ontology is authored centrally in `Agentum`.

Target repositories may host installed slices, but they are not automatically the authority over the ontology itself.

Local divergence is allowed only when explicitly marked in ecosystem registries.
