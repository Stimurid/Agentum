# DEFICIT_RECORD_SPEC

## Purpose

This document defines the canonical record for recurrent deficit in the Agentum ecosystem.

The goal is to stop saying:

- "the system kind of struggles here"
- "we probably need another agent"
- "it often loses something"

without being able to name:

- what is missing;
- where it was observed;
- how often it recurs;
- what semantic damage it causes;
- what candidate organ might answer it.

The `Deficit Record` is the pressure-side twin of the `AgentOrgan Record`.

## Core claim

No serious organ should be born from vibe alone.

It should be traceable to a recurrent deficit.

A deficit is not merely a bug.

It can be:

- missing capability;
- repeated semantic loss;
- overload;
- distortion;
- routing mismatch;
- memory failure;
- scene collapse;
- critic absence;
- orchestration blindness.

The record makes this pressure durable enough to reason about.

## What this record is for

Use a `Deficit Record` when at least one of these is true:

- the same failure recurs across tasks;
- the same repair move keeps being improvised by hand;
- a project repeatedly loses continuity or provenance;
- a runtime pattern keeps burning budget or stdout;
- current organs overlap but still leave a stable gap;
- a scene repeatedly collapses in the same place.

Do not use it for:

- one accidental typo;
- one-off operator preference;
- purely aesthetic irritation with no functional cost;
- speculative agent shopping with no observed pressure.

## Canonical fields

The record should be able to hold at least these fields.

### Identity

- `id`
- `title`
- `status`
- `severity`

Meaning:

- `id` = stable machine-readable deficit id
- `title` = compact name of the deficit
- `status` = open / testing / mitigated / resolved / archived
- `severity` = low / medium / high / critical

### Observation

- `observed_in_project`
- `observed_in_layer`
- `source_fragment`
- `evidence_refs`
- `repeated_count`

Meaning:

- `observed_in_project` = where the deficit appears
- `observed_in_layer` = runtime / memory / prompt / retrieval / review / orchestration / install / other
- `source_fragment` = minimal local trace of the problem
- `evidence_refs` = run records, files, prompts, reports, or traces
- `repeated_count` = recurrence marker, exact or approximate

### Character

- `failure_type`
- `semantic_loss`
- `suspected_cause`
- `scene_signature`
- `memory_signature`

Meaning:

- `failure_type` = mismatch / omission / false confidence / drift / overload / bleed / collapse / other
- `semantic_loss` = what meaning or function gets damaged
- `suspected_cause` = current best explanation
- `scene_signature` = what kind of scene repeatedly produces it
- `memory_signature` = what memory regime confusion accompanies it

### Need

- `required_capability`
- `current_workaround`
- `candidate_organs`
- `candidate_non_organ_fix`

Meaning:

- `required_capability` = what capability is actually absent
- `current_workaround` = how humans or existing organs are compensating now
- `candidate_organs` = organs that may answer the deficit
- `candidate_non_organ_fix` = config, prompt, registry, or workflow fix that may solve it without a new organ

### Validation

- `test_scene`
- `evaluation_criteria`
- `resolved_by`
- `residual_risk`

Meaning:

- `test_scene` = where the proposed resolution should be tested
- `evaluation_criteria` = what counts as real mitigation
- `resolved_by` = selected organ, config change, guard change, or process change
- `residual_risk` = what danger remains even after mitigation

## Minimal record shape

This is a conceptual skeleton, not a mandatory syntax.

```text
Deficit:
  id
  title
  status
  severity
  observed_in_project
  observed_in_layer
  source_fragment
  evidence_refs
  repeated_count
  failure_type
  semantic_loss
  suspected_cause
  scene_signature
  memory_signature
  required_capability
  current_workaround
  candidate_organs
  candidate_non_organ_fix
  test_scene
  evaluation_criteria
  resolved_by
  residual_risk
```

## Status model

The record should support at least these states:

- `open`
- `testing`
- `mitigated`
- `resolved`
- `archived`

Use them like this:

- `open` = recurrent pressure observed and not yet answered
- `testing` = candidate mitigation is under scene evaluation
- `mitigated` = pressure is reduced but still active
- `resolved` = the main pressure path is closed with acceptable residual risk
- `archived` = obsolete, merged, or superseded by stronger framing

## Deficit classes

Useful recurring classes in this ecosystem include:

- evidence gap
- provenance break
- project bleed
- memory authority confusion
- document-as-instruction confusion
- scene collapse
- review overload
- routing mismatch
- stdout burn
- budget inflation
- seed overwrite pressure
- fake completion
- organ overlap with no real owner

These are not final ontology.

They are a practical starter lattice.

## Review questions

Before turning a deficit into a new organ, ask:

- Is this really recurrent?
- Is the problem semantic, operational, or both?
- Could a simpler guard/config/profile fix solve it?
- What exact capability is missing?
- What scene reproduces the pressure?
- What memory confusion accompanies it?
- Would a new organ reduce pressure or only add more moving parts?
- What counts as resolution rather than temporary sedation?

## Anti-patterns

Reject or rework the record if it shows one of these:

- "something feels off" with no evidence;
- no recurrence signal;
- conflation of symptom and cause;
- candidate organ listed before the deficit is described;
- no named semantic loss;
- no scene for testing;
- no alternative non-organ fix considered;
- severity inflated for drama.

## Relation to other objects

The `Deficit Record` should connect to:

- observed traces or artifacts;
- one or more candidate organs;
- one or more test scenes;
- one eventual resolution path.

It should also be visible to the wider Foundry process:

`pressure -> record -> candidate variants -> critique -> selection -> deployment or rejection`

## Practical rule

If the deficit cannot be named clearly enough to survive this record, do not spawn a new organ yet.

First clarify the pressure.

Otherwise the ecosystem will grow cardboard organs around vague discomfort.
