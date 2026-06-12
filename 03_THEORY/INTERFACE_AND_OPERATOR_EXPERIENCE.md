# INTERFACE_AND_OPERATOR_EXPERIENCE

## Core claim

Interface work is not decoration after architecture.

For agentic systems, interface work is part of architecture itself.

If the operator cannot understand, trust, navigate, or control the system, the runtime may be technically alive but operationally dead.

## What goes wrong across projects

The repeated failure pattern is:

runtime or ontology enthusiasm
→ random panels, drawers, tabs, buttons, and blocks
→ zero workflow discipline
→ ugly, overloaded, low-trust surface
→ operator cannot actually use the system

This is not a cosmetic bug.

It is a product and control failure.

## Interface as operator contract

An interface is a contract between:

- the operator;
- the working object;
- the system state;
- the allowed actions;
- the consequences of those actions.

Bad UI breaks that contract by making one or more of these opaque.

## Mandatory pre-build pass

Before a serious UI change, the agent must state:

- operator type;
- main working object;
- primary scenario;
- most frequent actions;
- critical irreversible actions;
- visibility requirements;
- state model;
- error model;
- why this layout is better than at least one alternative.

No answer means no interface pass yet.

## Practical laws

### 1. Workflow before components

Do not begin with buttons, cards, tabs, or drawers.

Begin with the working scenario.

### 2. Canvas or workbench before landing-page sludge

If the system is operational, the interface should privilege doing the work, not telling a story about itself.

### 3. Primary actions must be cheap

The most frequent high-value actions must be visible and low-friction.

### 4. Hidden state is poison

If users cannot tell what mode, layer, step, or selection is active, the system is already failing.

### 5. Error states are part of the design

Do not design only the happy path.

### 6. Information density must be argued, not accidental

High density is allowed if it supports expert operation.

Chaos is not density.

### 7. Operator attention is a budget

Clicks, eye travel, memory load, scroll hunting, and mode confusion are all costs.

### 8. Beautiful nonsense is still failure

Visual polish without usability does not save the interface.

### 9. Functional ugliness still matters

If the system “works” but looks clumsy, badly grouped, or low-trust, operator confidence and precision degrade.

### 10. Compare at least two layouts

An unopposed first layout is usually just untested intuition.

## Anti-patterns

Typical interface anti-patterns:

- scrolling landing page instead of workbench;
- decorative side panels with no unique role;
- modal hell;
- hidden primary actions;
- overloaded top bars;
- state that exists only in the agent’s head;
- giant unstructured settings dumps;
- elegant-looking but untraceable workflows;
- mixed interaction grammars across screens;
- “we’ll make it clearer later”.

## Where books fit

When this theory is not enough, agents should consult:

- `01_RESEARCH_ARCHIVE/UX_UI_CANONICAL_READING.md`

The books are not there for prestige.

They are there to stop recurrent interface failure.
