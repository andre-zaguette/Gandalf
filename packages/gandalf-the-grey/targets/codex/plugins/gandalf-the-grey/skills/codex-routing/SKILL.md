---
name: codex-routing
description: Broad skill selection for Codex. Use when the task is clear but the right entry skill is not. Maps task type to the most precise available skill or agent path.
---

# Codex Routing

## Purpose

Route to the right skill before work starts. Wrong entry → wasted effort.

## Routing map

| Task type | Route to |
|---|---|
| Need architecture or tradeoff decision | `architecture` skill |
| Need safe structural change | `refactoring` skill |
| Need test strategy or coverage decision | `testing` skill |
| Need to review risk before merge | `code-review` skill |
| Need to find root cause of a bug | `debugging` skill |
| Vague or unclear task | ask one question to clarify, then route |
| Backend implementation | `backend-engineering` agent |
| Frontend implementation | `frontend-engineering` agent |
| Python implementation | `python-engineering` agent |
| Domain modeling | `ddd-tactical-patterns` agent |
| Test level decision | `unit-vs-integration-testing` agent |
| Framework-specific work | `fastapi`, `django`, `nestjs`, `react`, `nextjs`, `vue` agents |
| UI verification | `playwright` or `playwright-interactive` agent |
| Figma design work | `figma`, `figma-use`, `figma-generate-design`, `figma-implement-design` agents |

## Decision rules

- If the task has architectural pressure → architecture before implementation.
- If the task touches existing behavior without tests → refactoring + testing before change.
- If the task is a bug → debugging first, fix second.
- If the scope is cross-cutting (backend + frontend + DB) → clarify ownership boundary first.
- If the task is vague → one question, not five.

## Output shape

- Task classified
- Chosen route and reason
- What to clarify if route is uncertain
