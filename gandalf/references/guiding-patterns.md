# Guiding Patterns

# Patterns

Default pattern set:

- BDD: define behavior before build
- TDD: protect behavior while building
- SOLID: keep design changeable and responsibilities clear
- ADR: record decisions that matter
- Harness: keep agent memory and bootstrap in project
- Refactoring: change structure without changing behavior
- Testing: choose smallest honest feedback loop
- Code Review: find risk before merge
- Caveman: compress language, keep substance

SOLID notes:

- Single Responsibility: one reason to change
- Open/Closed: extend without rewriting stable core
- Liskov: subtype must behave as promised
- Interface Segregation: small contracts, not fat ones
- Dependency Inversion: depend on stable abstraction at volatile edges

SOLID smells:

- giant god modules
- controller owns business rules
- fake abstractions with no reason
- concrete dependency welded to domain logic

Best default stack for non-trivial engineering work:

1. BDD to frame behavior
2. ADR if design choice matters
3. SOLID to shape boundaries
4. TDD or targeted tests to protect work
5. Refactor only under protection
6. Review before merge
