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

# DDD Tactical Patterns

Model the domain. Not the database. Not the API.

## Core vocabulary

- **Bounded Context**: a named boundary where a model is valid and consistent. One team, one language, one model.
- **Aggregate**: a cluster of objects treated as one unit for data changes. Has a root. Enforces invariants.
- **Aggregate Root**: the only public entry point into the cluster. External objects hold only its identity.
- **Entity**: has identity that persists through state changes.
- **Value Object**: defined by its attributes alone. No identity. Immutable. Replace, don't mutate.
- **Domain Event**: something that happened in the domain. Past tense. Fact, not instruction.
- **Repository**: abstracts persistence. One per aggregate root. Interface lives in domain. Implementation lives in infrastructure.
- **Domain Service**: stateless logic that belongs to the domain but fits no single entity or value object.
- **Application Service**: orchestrates use case. Coordinates domain objects and infrastructure. Owns transaction boundary.
- **Anti-Corruption Layer**: translation layer between two bounded contexts. Keeps foreign model from poisoning yours.

## Decision rules

- If behavior enforces a business invariant → belongs in aggregate or domain service.
- If behavior coordinates workflow without business rule → belongs in application service.
- If two contexts share a concept but not a model → use ACL, not shared class.
- If an object has no identity beyond its attributes → value object, not entity.
- Aggregate size rule: smallest aggregate that can enforce its invariants.

## Smells

- aggregate with hundreds of fields
- repository that loads child aggregates directly
- domain service that touches the database
- application service that contains business rules
- shared kernel used as a shortcut when ACL was the right call
- anaemic domain: entities with only getters and setters, logic in services

# Hexagonal Architecture — Ports and Adapters

Domain owns nothing from infrastructure. Infrastructure knows the domain. Domain does not know infrastructure.

## Structure

- **Domain**: pure business logic. No framework. No ORM. No HTTP.
- **Port**: interface defined by the domain. Contract the domain needs fulfilled.
  - Primary port (driving): entry into the domain. Called by the outside.
  - Secondary port (driven): exit from the domain. Called by the domain, fulfilled by infrastructure.
- **Adapter**: implements a port. Lives in infrastructure. Swappable.
  - Primary adapter: REST controller, CLI handler, event consumer.
  - Secondary adapter: database repository, email sender, message publisher.

## Dependency rule

All dependency arrows point inward. Domain has no outward arrow.

```
[Primary Adapter] → [Primary Port] → [Domain] → [Secondary Port] ← [Secondary Adapter]
```

## Decision rules

- If domain logic needs the clock → inject a port, not `datetime.now()`.
- If domain logic needs persistence → inject a repository port, not the ORM.
- If a use case needs to send email → secondary port. Domain calls the interface. Adapter sends.
- If you cannot test domain logic without starting a server or a database → the boundary is broken.

## Smells

- domain class that imports Flask, Django, or SQLAlchemy directly
- repository method that returns ORM model instead of domain object
- use case that constructs HTTP responses
- unit test that requires a running database to test a business rule
- adapter that contains business logic

# Event-Driven and Messaging Patterns

Events decouple producers from consumers. Use with intention, not as default.

## Core vocabulary

- **Command**: instruction to do something. Directed at one handler. May be rejected.
- **Event**: fact that something happened. Past tense. Published to many. Cannot be rejected.
- **Message**: envelope for command or event. Carries payload, metadata, and routing info.
- **Queue**: point-to-point. One consumer. Load distribution.
- **Topic / Exchange**: broadcast. Many consumers. Fan-out.
- **Dead Letter Queue (DLQ)**: receives messages that failed after max retries. Failure path is not optional.
- **Idempotency key**: unique identifier per message. Consumer uses it to detect and skip duplicates safely.
- **Outbox pattern**: write event to the same database transaction as the state change. Worker publishes after commit. Prevents lost events.

## Decision rules

- Command when: one service owns the action, caller needs to know it was accepted or rejected.
- Event when: multiple services care, producer should not know or wait for consumers.
- Synchronous call when: response is needed in the same user-facing request.
- Async message when: work can be deferred, decoupling matters, or load needs smoothing.
- Outbox pattern when: publishing and state change must be atomic.

## Guarantees to design for explicitly

- At-least-once delivery → consumers must be idempotent.
- Ordering guarantees → partition by entity identity when order matters.
- Schema evolution → never break existing consumers. Add fields. Never remove.

## Smells

- event that contains a command embedded inside it
- consumer that performs destructive action without idempotency check
- publishing event before transaction commits
- event schema changed in a breaking way without versioning
- no dead letter strategy — failure path undefined
- event handlers containing business logic that belongs in the domain

# Functional Core, Imperative Shell

Push decisions to the center. Push side effects to the edge.

## Structure

- **Functional core**: pure functions. Input in, output out. No IO. No state mutation. No clock. No randomness.
- **Imperative shell**: reads from the world (DB, API, clock, user input), calls the core, writes results back.

The shell is thin. The core is thick. All interesting logic lives in the core.

## Properties of the core

- Given same input, always same output.
- No exception thrown for business decisions. Return result types instead.
- Fully testable without mocks, databases, or network.

## Properties of the shell

- Performs IO.
- Passes real data to the core.
- Writes core output to the world.
- Handles infrastructure errors.

## Decision rules

- Business rule that transforms data → core.
- Database read or write → shell.
- Sending email or publishing event → shell.
- Decision based on current time → pass the time as parameter into the core.
- Random value needed → generate in shell, pass into core.
- If a function cannot be tested without mocking → it has IO that belongs in the shell.

## Smells

- business logic inside a function that also calls the database
- core function that calls `datetime.now()` or `random.uuid()` internally
- unit test that requires mocks to test a business rule
- shell so thick it contains decisions that belong in the core
- result of pure computation buried inside a try/except that catches infrastructure errors

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
