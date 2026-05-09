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
