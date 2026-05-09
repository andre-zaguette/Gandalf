---
name: refactoring
description: Safe structural change without behavior change. Use when code needs reshaping but existing behavior must be preserved. Requires a protection strategy before touching structure.
---

# Refactoring

## Rule

No refactoring without protection. Protection first. Structure second.

## Operating sequence

1. Identify what behavior must be preserved.
2. Verify tests cover that behavior. If not, write characterization tests first.
3. Name the smell being removed (God class, long method, feature envy, shotgun surgery, etc.).
4. Choose the smallest refactoring move that addresses the smell.
5. Apply one move. Verify green. Commit. Repeat.

## Canonical moves

- **Extract method**: logic with a name and a single purpose.
- **Extract class**: responsibility that has its own data and behavior.
- **Move method**: method belongs closer to the data it uses.
- **Replace conditional with polymorphism**: type-based branching that grows.
- **Introduce parameter object**: method with too many related parameters.
- **Replace magic number/string with named constant**: literal with implicit meaning.
- **Inline**: remove indirection that adds no clarity.

## Smells and their moves

- Long method → extract method, extract class
- God class → extract class, move method
- Feature envy → move method to the class it envies
- Primitive obsession → introduce value object
- Shotgun surgery → consolidate into one class
- Divergent change → split class by reason to change

## Guardrails

- Never rename and restructure in the same commit.
- Never change behavior and structure in the same commit.
- If test coverage is below trust level, characterize first.
- If the move introduces a new dependency direction, stop and evaluate.

## Output shape

- Smell identified
- Behavior to protect
- Protection status (tests: yes / no / added now)
- Chosen move
- Sequence of steps
