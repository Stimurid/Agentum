# PROJECT_SYNC_WORKFLOW

## Goal

Provide a repeatable bounded workflow for synchronizing agent layers into a target repository.

## Workflow

### 1. Identity

Name:

- active repository;
- root path;
- install profile;
- protected paths;
- neighboring projects.

### 2. Registry lookup

Read:

- `09_ECOSYSTEM/PROJECT_AGENT_REGISTRY.yaml`
- `09_ECOSYSTEM/LAYER_LIBRARY_REGISTRY.yaml`

Confirm:

- target is registered;
- intended layer exists;
- status is not blocked or archived.

### 3. Layer selection

Choose the smallest needed set:

- runtime guard only;
- runtime guard + subject ecology;
- runtime guard + subject ecology + persona.

### 4. Bounded patching

Patch only the local agent contour:

- local `AGENTS.md` / `CLAUDE.md`;
- local agent docs;
- local profile files;
- local eval prompts;
- local hooks if explicitly in scope.

### 5. Validation

Check:

- routing still works;
- project identity stayed intact;
- persona layer did not leak into dry enforcement;
- local divergence is documented.

### 6. Registry update

Record:

- installed layer versions;
- divergence status;
- review notes;
- blocked follow-ups if any.
