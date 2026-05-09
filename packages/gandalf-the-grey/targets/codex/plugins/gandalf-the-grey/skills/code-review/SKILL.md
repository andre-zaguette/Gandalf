---
name: code-review
description: Risk-focused code review. Use before merging. Finds correctness gaps, boundary violations, missing test coverage, and design pressure — not style.
---

# Code Review

## Purpose

Find risk before it ships. Not style. Risk.

## Review sequence

1. **Understand intent**: what is this change supposed to do? If unclear, stop and ask.
2. **Correctness**: does the code do what it claims? Check edge cases, failure paths, concurrent access.
3. **Behavior coverage**: is the new behavior tested? Is the failure path tested?
4. **Boundary integrity**: does the change respect layer boundaries? Does it introduce wrong dependencies?
5. **Design pressure**: is there a growing smell that signals a structural problem ahead?
6. **Operability**: can this be monitored, debugged, and rolled back by whoever will own it?

## Risk checklist

- [ ] Unhandled failure path in critical operation
- [ ] Silent error swallowed without log or alert
- [ ] External call without timeout or retry boundary
- [ ] State mutation without transaction protection
- [ ] Business rule living in the wrong layer
- [ ] Missing idempotency in a message consumer
- [ ] Hardcoded secret, credential, or environment assumption
- [ ] Migration without rollback plan
- [ ] Test that mocks the thing it is supposed to test
- [ ] API contract change without versioning

## What not to comment on

- formatting (let the linter own it)
- naming preferences with no correctness impact
- style disagreements without a rule
- "I would have done it differently" without a concrete risk

## Output shape

- Intent understood: yes / no / partially
- Risks found (severity: high / medium / low)
- Missing coverage gaps
- Design pressure (if any)
- Blocking issues vs suggestions
