# UI_AND_OPERATOR_GUARD

Use this document when a coding agent is about to create or significantly change an interface.

## Rule

Do not build UI from vibes.

Before UI work, state:

- operator;
- working object;
- primary workflow;
- three most important actions;
- state model;
- error model;
- why this layout beats at least one alternative.

## Must preserve

- visible workflow;
- explicit active state;
- cheap primary actions;
- understandable navigation;
- operator trust;
- usable density;
- honest error handling.

## Must avoid

- landing-page sludge instead of workbench;
- decorative panels with no operational role;
- hidden core controls;
- giant settings dumps;
- unexplained mode switching;
- random visual hierarchy;
- “functional but unusable” surfaces.

## If unclear

If the agent cannot justify the interaction model, it should stop and produce:

1. operator model;
2. workflow map;
3. two layout options;
4. recommendation with tradeoffs.
