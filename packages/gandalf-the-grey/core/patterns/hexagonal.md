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
