---
name: architecture
description: Architecture analysis and tradeoff evaluation. Use when the task involves structural decisions, layer boundaries, coupling concerns, or design alternatives that will be expensive to undo.
---

# Architecture

## Purpose

Evaluate structural decisions before they harden into debt.

## Operating sequence

1. Name the constraint driving the decision (scale, team boundary, compliance, speed).
2. Name the two or three realistic options. Not ideal options. Realistic ones.
3. For each option: state what it buys and what it costs.
4. Name which cost hurts most given current context.
5. Recommend one path. State what would change the recommendation.

## Lenses to apply

- **Coupling**: what breaks if this component changes?
- **Cohesion**: does this module have one reason to change?
- **Reversibility**: how expensive to undo this decision in six months?
- **Team boundary**: does the boundary match how the team actually works?
- **Operability**: can this be deployed, monitored, and debugged by the people who will own it?

## When to record an ADR

- decision affects more than one team or service
- decision is hard to reverse
- decision rejects a path that will seem obvious later

## Smells that trigger this skill

- "just add a service for that"
- adding abstraction before the third use case
- layer that imports from the layer two levels below it
- decision made by convention, not by tradeoff analysis

## Output shape

- Constraint
- Options (2–3 max)
- Cost per option
- Recommendation
- What changes the recommendation
