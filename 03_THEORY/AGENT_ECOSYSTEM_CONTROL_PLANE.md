# AGENT_ECOSYSTEM_CONTROL_PLANE

## Purpose

If multiple repositories use agent layers, then the framework needs more than markdown files.

It needs a control plane.

The control plane is the layer that knows:

- which repositories exist;
- which agent layers each repository uses;
- which versions are active;
- which project is canonical for a given variation;
- which updates are safe to propagate.

## Why this matters

Without a control plane:

- ontology drifts silently;
- persona patches become folklore;
- runtime guards and subject layers desynchronize;
- projects start carrying incompatible agent selves;
- update attempts become project bleed.

## Minimum control-plane objects

### Project registry

List of known repositories, paths, profile types, and sync status.

### Layer library registry

List of centrally maintained installable layers and their versions.

### Sync protocol

The bounded sequence for updating a target project's agent contour.

### Divergence status

A way to mark:

- canonical;
- installed;
- local override;
- experimental;
- blocked;
- archived.

## Control-plane rule

No cross-project ontology or persona sync should happen from memory alone.

It must route through:

1. layer identification;
2. project registry lookup;
3. bounded install plan;
4. diff review;
5. post-install validation.

## What the control plane does not do

It does not:

- deploy the target product;
- rewrite business logic;
- rewrite domain content;
- overwrite protected seed work;
- pretend all projects should receive the same layer set.

The control plane updates only the agent-evolution contour.
