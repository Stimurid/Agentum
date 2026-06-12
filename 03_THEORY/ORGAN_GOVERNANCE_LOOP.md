# ORGAN_GOVERNANCE_LOOP

## Purpose

This document defines the minimal operating loop for keeping organ records, deficit records, eval bindings, and install scopes aligned.

The goal is not committee theater.

The goal is to keep the ecosystem from drifting back into:

- undocumented pressure;
- orphan organs;
- eval-free promotion;
- profile/install drift.

## Core loop

The minimal governance loop is:

1. observe pressure
2. write or update `Deficit Record`
3. decide whether a non-organ fix is enough
4. if not, generate bounded candidate set
5. run scene test and critic pass
6. promote / reject / quarantine
7. update organ registry
8. update eval matrix
9. update affected profiles and install scopes

## Trigger conditions

Run the loop when any of these happens:

- a deficit repeats;
- an organ is proposed;
- an organ boundary changes;
- an eval gap becomes visible;
- a profile needs a new organ set;
- a target install exposes a missing guard or false organ assumption.

## Required artifacts per pass

Each pass should leave behind, at minimum:

- one updated `Deficit Record` or explicit no-deficit result
- one candidate note or explicit non-organ decision
- one critic result
- one registry or matrix update if promotion occurs

No invisible governance.

## Decision outputs

The loop may end in only a small number of lawful states:

- `reject`
- `revise`
- `quarantine`
- `select`
- `profile_only_fix`
- `guard_only_fix`

This keeps the ecosystem from pretending every pressure needs a new organ.

## Cross-layer updates

If an organ is selected, check these surfaces:

- `02_REGISTRIES/AGENT_ORGAN_REGISTRY.yaml`
- `02_REGISTRIES/DEFICIT_REGISTRY.yaml`
- `06_EVALS/ORGAN_DEFICIT_EVAL_MATRIX.md`
- affected `05_PROFILES/*`
- affected `08_INSTALL/*`

If these are not considered, governance is incomplete.

## Anti-patterns

Watch for:

- theory update with no registry consequence;
- registry update with no eval consequence;
- install change with no named active organ set;
- profile claiming an organ without its deficit or boundary;
- organ proliferation with no retirement path.

## Practical rule

The governance loop should stay boringly explicit.

If the ecosystem cannot say:

- what pressure appeared,
- what answered it,
- how it was tested,
- where it may be installed,

then governance has failed, even if the prose sounds grand.
