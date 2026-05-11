# Routing Map

# Routing

Every quest follows this mandatory classification:

1. **Harness Check:** Does the project have Git, Mandates, and Progress?
    - If ✗: Route to `Harness Construction`.
2. **Context Check:** Is this a non-trivial quest?
    - If ✓ and `docs/contexto.md` missing: Route to `Context Mapping`.
3. **Scope Check:** Backend, Frontend, or Cross-Repo?
4. **Pattern Selection:** Choose the right road (SOLID, BDD, TDD).

Roads:

- Vague Project Ask -> Socratic Interrogation -> Context Map.
- Architecture Tension -> ADR Path -> Architecture Skill.
- Domain Modeling -> SOLID/DDD Path.
- Safe Cleanup -> Refactoring Skill under TDD protection.
- Bug Hunt -> Debugging Skill -> Proof (Test) before Fix.
- Review Ask -> Risk Audit Skill.

## Fellowship Routing

| Task type | Agent | Signal |
|-----------|-------|--------|
| Design, CSS, Tailwind, a11y, Figma | Galadriel | `SIGNAL_UI_TASK` |
| Python, FastAPI, Django, data, ML | Radagast | `SIGNAL_PYTHON_TASK` |
| Vue, Nuxt, Pinia, Vue Router | Elrond | `SIGNAL_VUE_TASK` |
| React, Next.js, RSC, Server Actions | Celebrimbor | `SIGNAL_REACT_TASK` |
| Node, NestJS, REST API, queues | Beorn | `SIGNAL_NODE_TASK` |
| Tests, CI, quality gate | Boromir | `SIGNAL_BREACH_DEFENSE` |
| Cross-stack (UI + backend) | Gandalf coordinates | — |

## Palantír — consult before routing

| Situation | Skill |
|-----------|-------|
| Routing unclear | `skills/codex-routing/SKILL.md` |
| Architecture / ADR | `skills/architecture/SKILL.md` |
| Code review | `skills/code-review/SKILL.md` |
| Debug / regression | `skills/debugging/SKILL.md` |
| Refactoring | `skills/refactoring/SKILL.md` |
| Test planning | `skills/testing/SKILL.md` |
