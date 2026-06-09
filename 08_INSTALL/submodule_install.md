# submodule_install

Use submodule install only when the target repo can tolerate explicit coupling to this repository.

## Pros

- keeps provenance explicit
- easier to audit source revision

## Cons

- higher operational coupling
- target runtime assumptions may drift from the submodule
- teams may falsely assume install is “automatic”

## Rules

- pin revision
- audit target environment first
- keep runtime references compact
- rerun proving-ground after linking
- do not treat submodule presence as permission to skip human review
