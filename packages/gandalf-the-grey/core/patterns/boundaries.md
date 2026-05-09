# Repository and Service Boundary Heuristics

Wrong boundary = wrong place for logic. Identify the right container before coding.

## Repository heuristics

- One repository per aggregate root. Not per entity. Not per table.
- Repository returns domain objects. Not ORM models. Not raw dicts.
- Repository interface defined in domain. Implementation in infrastructure.
- No business logic inside a repository. Query logic only.
- If you need to load two aggregate roots in one query, the boundary may be wrong.

## Service heuristics

- **Domain service**: stateless. Enforces business rule that spans multiple entities. Lives in domain layer.
- **Application service**: orchestrates one use case. Coordinates domain, repository, and infrastructure. Owns transaction boundary. No business rules inside.
- **Infrastructure service**: adapts external system. Sends emails, calls APIs, publishes messages. Implements secondary port.

## Decision: where does this logic go?

Ask in order:

1. Does it enforce a business invariant on a single aggregate? → put it in the aggregate.
2. Does it enforce a rule that spans multiple aggregates? → domain service.
3. Does it coordinate a workflow without business logic? → application service.
4. Does it touch external systems? → infrastructure service or adapter.
5. Does it transform data with no side effects? → functional core.

## Boundary smells

- application service that calculates business rules instead of delegating to domain
- domain service that imports the ORM or repository implementation
- repository that contains `if` branches based on business rules
- one repository that loads entities across multiple aggregate roots
- service that grows beyond one responsibility because no clear owner was named upfront

## When to extract a new service

- two callers need the same logic independently
- the logic has a distinct lifecycle or deployment concern
- the team boundary aligns with the service boundary
- not before. Premature extraction is a boundary smell too.
