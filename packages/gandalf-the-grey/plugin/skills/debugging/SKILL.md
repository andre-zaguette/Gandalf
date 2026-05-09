---
name: debugging
description: Systematic bug investigation. Use when behavior is wrong and the cause is unknown. Drives from evidence to hypothesis to fix — not from guess to patch.
---

# Debugging

## Rule

Evidence first. Hypothesis second. Fix third. Never the reverse.

## Operating sequence

1. **Reproduce**: confirm the bug is reproducible. If not, the first job is isolation.
2. **Observe**: gather evidence. Logs, stack traces, failing tests, unexpected output.
3. **Constrain the search**: narrow to the layer or component where behavior diverges from expectation.
4. **Form one hypothesis**: specific, testable, falsifiable.
5. **Test the hypothesis**: add a log, write a failing test, or remove a dependency to confirm.
6. **Fix only what the evidence points to**: no opportunistic cleanup during bug investigation.
7. **Verify fix**: confirm the original reproduction case passes.
8. **Protect**: add a test that would have caught this bug.

## Search heuristics

- Binary search the call stack: find the last point where state was correct.
- Diff the environment: works locally, fails in CI → environment difference.
- Diff the data: works for one input, fails for another → data assumption broken.
- Diff the time: worked last week, fails now → recent change is the likely cause. `git bisect`.
- Simplify the reproduction: smallest input that triggers the bug is easier to reason about.

## Common traps

- patching the symptom, not the cause
- adding defensive code without understanding the root cause
- changing multiple things at once — can't know which fixed it
- assuming the bug is in your code when it could be in a dependency
- reading the code instead of running it — assumption beats observation

## When to stop and ask

- the failure is in infrastructure you don't own
- the bug requires a production environment to reproduce
- the fix touches a critical boundary (auth, payment, data integrity)

## Output shape

- Reproduction confirmed: yes / no
- Evidence gathered
- Hypothesis
- Test to validate hypothesis
- Fix scope
- Protection added
