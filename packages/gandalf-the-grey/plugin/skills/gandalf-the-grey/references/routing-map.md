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
- Cross-System Impact / "Who depends on this?" -> Narvi -> Alliance Map (SIGNAL_CRAFT_FORGE).
- Harness missing / BDD setup / No tests -> Narvi -> Craft Audit (SIGNAL_CRAFT_FORGE).

## Fellowship Routing

| Task type | Agent | Signal |
|-----------|-------|--------|
| New project, requirements, scope, docs | Bilbo | `SIGNAL_SCOPE_QUEST` |
| Design, CSS, Tailwind, a11y, Figma | Galadriel | `SIGNAL_UI_TASK` |
| Python, FastAPI, Django, data, ML | Radagast | `SIGNAL_PYTHON_TASK` |
| Vue, Nuxt, Pinia, Vue Router | Elrond | `SIGNAL_VUE_TASK` |
| React, Next.js, RSC, Server Actions | Celebrimbor | `SIGNAL_REACT_TASK` |
| Node, NestJS, REST API, queues | Beorn | `SIGNAL_NODE_TASK` |
| Tests, CI, quality gate | Boromir | `SIGNAL_BREACH_DEFENSE` |
| Harness audit, BDD setup, cross-project impact map | Narvi | `SIGNAL_CRAFT_FORGE` |
| Cross-stack (UI + backend) | Gandalf coordinates multiple agents | — |

Palantír is consulted first on every non-trivial quest. No agent acts without archive check.
