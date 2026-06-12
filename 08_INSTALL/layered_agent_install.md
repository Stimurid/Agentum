# layered_agent_install

## Purpose

This repository now supports layered installation.

A target project does not have to receive the same full package every time.

## Layers

### Layer 1 — Runtime guard

Minimum safety slice:

- `04_KITS/v0_minimal`
- selected project profile
- install checklist

### Layer 2 — Subject ecology

Optional upper layer:

- `04_KITS/subject_ecology`
- project-local constitution fragment
- lineage / role patch

### Layer 3 — Persona fragments

Optional style layer:

- `04_KITS/persona_fragments`

This layer stays out of dry enforcement files.

## Recommended rollout order

1. Install runtime guard.
2. Validate routing and hook behavior.
3. Install subject ecology only where the project actually benefits from it.
4. Add persona fragments last.
5. Register the installed layers in `09_ECOSYSTEM`.

## Hard boundary

Updating layer 2 or 3 must not silently rewrite project content.

It may update only the agent-evolution contour.
