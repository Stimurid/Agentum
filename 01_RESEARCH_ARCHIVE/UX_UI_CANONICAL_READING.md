# UX_UI_CANONICAL_READING

This is the canonical reading archive index for interface, operator-experience, interaction-design, and information-architecture work inside Agentum.

It is an archive of what agents should consult when our own theory is not enough.

## Legal note

This repository does not bundle pirated full-text copies of copyrighted books.

Instead it stores:

- canonical titles;
- why each title matters;
- what design failures it helps prevent;
- legal acquisition pointers;
- the exact questions an agent should take to the book.

If the owner later adds legally obtained files, they should be placed in a separate local reading folder and linked from this index.

## Tier 1 — must-read canon

### 1. Steve Krug — *Don’t Make Me Think*

- why it matters:
  - kills interface self-indulgence
  - restores obviousness, scanability, and operator flow
- use when:
  - screens feel noisy
  - navigation is unclear
  - the user has to guess what to click
- fights:
  - interface slop
  - decorative complexity
  - hidden primary actions
- acquisition:
  - author/publisher page

### 2. Alan Cooper et al. — *About Face: The Essentials of Interaction Design*

- why it matters:
  - strongest core text for interaction design as a discipline
  - forces role, goals, flows, states, and behavior models
- use when:
  - an agent wants to place components before defining operator goals
  - the system has many modes, states, and workflows
- fights:
  - screen-first design
  - component cargo cult
  - state confusion
- acquisition:
  - publisher page

### 3. Don Norman — *The Design of Everyday Things*

- why it matters:
  - restores affordances, feedback, mapping, constraints, and error-thinking
- use when:
  - interaction feels “technically possible” but humanly wrong
  - a UI seems clever but produces mistakes
- fights:
  - invisible affordances
  - ambiguous controls
  - bad error ergonomics
- acquisition:
  - author/publisher page

### 4. Jenifer Tidwell, Charles Brewer, Aynne Valencia — *Designing Interfaces*

- why it matters:
  - concrete interface patterns without reducing design to empty pattern worship
  - useful bridge between UX theory and actual screen structure
- use when:
  - an interface needs pattern vocabulary
  - a layout needs comparison against known interaction patterns
- fights:
  - reinventing solved interaction problems badly
  - inconsistent screen structures
- acquisition:
  - O’Reilly page

### 5. Rosenfeld, Morville, Arango — *Information Architecture for the Web and Beyond*

- why it matters:
  - essential for information structures, labeling, findability, navigation, and content shape
- use when:
  - the system contains many objects, views, documents, filters, or navigation layers
- fights:
  - taxonomic chaos
  - content dumps
  - broken navigational meaning
- acquisition:
  - Rosenfeld Media page

## Tier 2 — strong practical operators

### 6. Steve Krug — *Rocket Surgery Made Easy*

- why it matters:
  - forces fast, practical usability testing instead of abstract UI theorizing
- use when:
  - the interface exists but nobody has validated usability
- fights:
  - “looks fine to me” delusion
  - zero-user-check design
- acquisition:
  - author/publisher page

### 7. Luke Wroblewski — *Web Form Design: Filling in the Blanks*

- why it matters:
  - indispensable whenever forms, input flows, settings, filters, and confirmations exist
- use when:
  - a product has forms
  - a project has settings panels
  - an agent is designing any structured operator input
- fights:
  - broken forms
  - friction-heavy settings
  - validation pain
- acquisition:
  - Rosenfeld Media / A Book Apart family pages

### 8. Jeff Johnson — *Designing with the Mind in Mind*

- why it matters:
  - translates cognitive psychology into concrete interface decisions
- use when:
  - agents need reasons for attention, memory, chunking, recognition, and visual hierarchy decisions
- fights:
  - cognitive overload
  - unreadable information density
  - memory-hostile UI
- acquisition:
  - publisher page

### 9. Refactoring UI — Adam Wathan, Steve Schoger

- why it matters:
  - practical visual refinement for engineers who build ugly but functional products
- use when:
  - the product works but looks clumsy, flat, or badly prioritized
- fights:
  - low-contrast chaos
  - accidental ugliness
  - weak visual hierarchy
- acquisition:
  - official Refactoring UI page

### 10. Alla Kholmatova — *Design Systems*

- why it matters:
  - useful for system-level consistency when products accumulate repeated UI parts
- use when:
  - there are multiple surfaces, repeated components, or cross-screen consistency problems
- fights:
  - component drift
  - inconsistent product language
  - pseudo-systems
- acquisition:
  - official/publisher page

## Tier 3 — what agents should extract from the books

An agent reading this canon should extract:

- primary workflow logic;
- operator goal models;
- state and transition discipline;
- affordance and feedback rules;
- information density and attention cost rules;
- navigation and labeling discipline;
- form ergonomics;
- usability validation methods;
- visual hierarchy repair principles;
- design-system consistency rules.

## Mandatory questions before UI work

Before doing serious interface work, an agent should be able to answer:

1. Who is the operator?
2. What is the primary working object?
3. What are the three most frequent high-value actions?
4. What must be visible without hunting?
5. What states, empty states, loading states, and error states exist?
6. Why is this layout better than at least one alternative?

If the agent cannot answer these, it is not ready to build UI.
