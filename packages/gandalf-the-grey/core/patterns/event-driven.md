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
