# ONTOLOGY_UPDATE_PROTOCOL

## Purpose

This protocol governs updates to the agent ontology and subject-ecology layers across projects.

## Rule zero

Ontology update does not mean target-project rewrite.

It means bounded propagation of the agent-evolution contour only.

## Update sequence

1. Identify the source layer in `LAYER_LIBRARY_REGISTRY.yaml`.
2. Identify target projects in `PROJECT_AGENT_REGISTRY.yaml`.
3. Check each target's profile, installed layer status, and divergence status.
4. Decide whether the change is:
   - constitution patch;
   - lineage patch;
   - role patch;
   - persona patch;
   - runtime-affecting patch.
5. If the patch touches runtime behavior, check compatibility with `v0_minimal`.
6. Prepare the smallest patch batch per project.
7. Run local validation or project-specific review.
8. Update the project registry entry after successful sync.

## Mandatory stop conditions

Stop if:

- target project identity is unclear;
- local divergence is not understood;
- sync would modify domain content;
- patch mixes persona layer with dry enforcement;
- runtime and ontology patches conflict;
- the project is not listed in the registry.

## Allowed outputs

Allowed outputs of ontology sync:

- updated project-level agent docs;
- updated local constitution note;
- updated persona patch;
- updated lineage note;
- updated install metadata.

## Forbidden outputs

Forbidden outputs of ontology sync:

- rewritten application logic;
- rewritten datasets;
- rewritten manuscripts or product copy unless separately requested;
- silent profile swapping;
- untracked prompt replacement.
