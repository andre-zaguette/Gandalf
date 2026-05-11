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
