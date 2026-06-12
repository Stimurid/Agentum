# AGENT_ORGAN_RECORD_SPEC

## Purpose

This document defines the canonical record for a stable agent organ in the Agentum ecosystem.

The goal is not to worship records.

The goal is to stop confusing:

- a prompt body;
- a runtime role;
- a skill;
- a one-off helper;
- a durable organ in the wider organism.

An `AgentOrgan Record` exists to make an organ:

- comparable across projects;
- reviewable before deployment;
- traceable through mutations;
- testable through scenes;
- legible to neighboring organs.

## Core claim

An organ is not real in this ecosystem because it has a name.

It becomes real when it has:

- a deficit origin;
- a bounded function;
- a contract;
- a memory dependency profile;
- a test scene set;
- a failure surface;
- a lineage.

The record is the minimum object that holds those together.

## What this record is for

Use an `AgentOrgan Record` when at least one of these is true:

- the same role recurs across tasks or projects;
- the organ has a stable input/output contract;
- the organ needs named memory dependencies;
- the organ is worth testing in scenes;
- the organ may evolve, fork, or be retired;
- the organ should be installable into more than one local contour.

Do not use it for:

- a one-line local helper;
- a transient branch experiment with no stable role;
- decorative persona flourishes;
- unbounded swarm fantasies.

## Canonical fields

The record should be able to hold at least these fields.

### Identity

- `id`
- `name`
- `status`
- `version`
- `project_scope`

Meaning:

- `id` = stable machine-readable organ id
- `name` = human-readable name
- `status` = draft / candidate / selected / active / quarantined / retired
- `version` = current revision marker
- `project_scope` = where the organ may operate

### Origin

- `deficit_origin`
- `parent_organs`
- `child_organs`
- `mutation_history`
- `lineage`

Meaning:

- `deficit_origin` = the recurrent pressure that justified birth
- `parent_organs` = ancestor organs or fragments
- `child_organs` = later descendants or specializations
- `mutation_history` = material changes across versions
- `lineage` = the compact ancestry story

### Function

- `function`
- `non_function`
- `working_object`
- `output_class`

Meaning:

- `function` = what transformation this organ performs
- `non_function` = what it must not pretend to do
- `working_object` = what it primarily acts upon
- `output_class` = report / patch / draft / extraction / routing / critique / synthesis

### Contracts

- `input_contract`
- `output_contract`
- `context_requirements`
- `activation_policy`

Meaning:

- `input_contract` = required inputs and admissible forms
- `output_contract` = expected output form and guarantees
- `context_requirements` = what must be present in the working field
- `activation_policy` = when this organ may be invoked

### Memory

- `memory_dependencies`
- `memory_regimes_used`
- `memory_authority_limits`

Meaning:

- `memory_dependencies` = what memory layers the organ depends on
- `memory_regimes_used` = verbatim / compressed / normalized / linked / narrative / graph / task-packet / method
- `memory_authority_limits` = what remembered material may not silently become instruction

### Runtime boundary

- `tools_allowed`
- `write_surface`
- `approval_boundary`
- `runtime_risks`

Meaning:

- `tools_allowed` = which tool classes are allowed, if any
- `write_surface` = what the organ may mutate
- `approval_boundary` = what needs explicit review
- `runtime_risks` = budget, stdout, deploy, seed, project bleed, or similar risks

### Validation

- `test_scenes`
- `evaluation_criteria`
- `failure_modes`
- `critic_links`

Meaning:

- `test_scenes` = bounded scenes where the organ is exercised
- `evaluation_criteria` = what counts as success
- `failure_modes` = expected characteristic failures
- `critic_links` = what critic organs or eval surfaces must review it

### Governance

- `observability_hooks`
- `provenance_policy`
- `quarantine_status`
- `install_scope`

Meaning:

- `observability_hooks` = how the organ becomes visible in traces and context observability
- `provenance_policy` = how evidence/source lineage must be preserved
- `quarantine_status` = whether the organ is isolated, constrained, or safe for reuse
- `install_scope` = where it may be installed or copied

## Minimal record shape

This is a conceptual skeleton, not a mandatory syntax.

```text
AgentOrgan:
  id
  name
  status
  version
  project_scope
  deficit_origin
  function
  non_function
  working_object
  input_contract
  output_contract
  context_requirements
  memory_dependencies
  memory_regimes_used
  memory_authority_limits
  tools_allowed
  write_surface
  approval_boundary
  runtime_risks
  test_scenes
  evaluation_criteria
  failure_modes
  critic_links
  lineage
  parent_organs
  child_organs
  mutation_history
  activation_policy
  observability_hooks
  provenance_policy
  quarantine_status
  install_scope
```

## Status model

The record should support at least these states:

- `draft`
- `candidate`
- `selected`
- `active`
- `quarantined`
- `retired`

Use them like this:

- `draft` = described but not yet scene-tested
- `candidate` = bounded and under evaluation
- `selected` = passed the main critic gate and is ready for controlled use
- `active` = accepted into live ecology
- `quarantined` = useful but risky, unstable, or currently constrained
- `retired` = superseded or intentionally removed from active use

## Required relations

An `AgentOrgan Record` should be connected to:

- at least one `Deficit Record`
- at least one test scene
- at least one failure mode cluster
- at least one installation scope

If these links are absent, the record is probably folklore, not infrastructure.

## Review questions

Before an organ is selected, review it with these questions:

- What recurrent deficit made this necessary?
- What does this organ do that current organs do not?
- What would make this organ false, redundant, or dangerous?
- What memory regimes does it need?
- What kinds of prompt/data confusion could corrupt it?
- What scene proves it adds value?
- What neighboring organs does it overlap with?
- What is the rollback path if it degrades the organism?

## Anti-patterns

Reject or quarantine the record if it shows one of these:

- role inflation without deficit origin;
- one organ pretending to solve everything;
- no scene tests;
- no failure surface;
- persona theater standing in for contract;
- memory dependency named vaguely as just "context";
- install scope not bounded;
- no provenance policy for evidence-sensitive work;
- fake lineage invented after the fact.

## Relation to other objects

The `AgentOrgan Record` is not:

- the prompt file itself;
- the runtime guard itself;
- the eval scenario itself;
- the install profile itself.

It is the coordinating object that lets those surfaces refer to the same organ without confusion.

## Practical rule

If an organ cannot be described in this form without hand-waving, it is not ready for stable library status.

It may still be a useful experiment.

But it is not yet a durable organ of the ecosystem.
