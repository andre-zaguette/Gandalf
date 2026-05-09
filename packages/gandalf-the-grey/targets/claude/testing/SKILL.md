---
name: testing
description: Test strategy selection and feedback loop design. Use when deciding what to test, at which layer, with which tool, and at what granularity.
---

# Testing

## Rule

Choose the smallest feedback loop that gives honest confidence.

## Test layers

- **Unit**: one function or class in isolation. Fast. No IO. Tests logic.
- **Integration**: two or more real components together. Tests contracts and wiring.
- **Contract**: verifies the interface between producer and consumer without full deployment.
- **End-to-end**: full system path from entry to exit. Slow. Catches wiring gaps. Use sparingly.
- **Characterization**: documents existing behavior before refactor. Not a design test. A safety net.

## Decision: which layer fits?

Ask in order:

1. Is this pure logic with no IO? → unit test.
2. Is this a boundary between components (DB, API, queue)? → integration test.
3. Is this a consumer-producer contract across teams? → contract test.
4. Is this a critical user path that no lower layer can fully verify? → one end-to-end test.
5. Is this existing untested code about to be refactored? → characterization test first.

## Coverage heuristics

- Cover the happy path.
- Cover the failure path that matters most (not all failures).
- Cover the edge case the code explicitly handles.
- Do not cover implementation details. Test behavior and outcomes.

## Smells

- unit test that mocks every dependency → not testing the real behavior
- test that tests the mock, not the code
- integration test used as a substitute for a missing unit test
- end-to-end test for every feature → slow, brittle, hard to diagnose
- no test for the failure path of a critical operation
- test that cannot be run without a full environment

## Output shape

- What behavior to protect
- Layer recommendation and reason
- Tool suggestion (if relevant)
- Edge cases worth covering
- What not to test (and why)
