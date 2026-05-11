# Guiding Patterns

# Patterns

Default pattern set:

- **Phase 1: Context Map:** Every quest starts here. Define objective, danger, and proof.
- **The Mirror of Galadriel:** Mandatory self-audit against a quality rubric before commit.
- **The Fellowship Contract:** Signed API/interface contract between agents or services before implementation.
- **Mithril Armor:** Automated security scanning for secrets and dangerous functions.
- **The Archive Consultation:** Consult the Palantír Map (`docs/archive/PALANTIR.md`) to understand the layout and pillars of the realm.
- **Token-Economic Budgeting:** Every token is a resource. Prefer high-signal structural data over raw file reads.
- **The Lembas Protocol:** High-density reasoning. Reason silently, speak exact. Minimal filler.
- **The Eye of Sauron:** Mandatory Vision Transcription. Describe UI components, colors, and layout textually before writing any CSS.
- **The Gates of Argonath:** Automated guardrails (Git Hooks) that prevent commit if the Harness is broken or out of sync.
- **The Red Book of Westmarch:** Persistent retrospectives. Record lessons and anti-patterns after every quest to prevent recurrence.
- **The Eagle's Flight:** Swift Quest for low-risk tasks (UI text, single-line fixes). Bypasses heavy ceremony but keeps security active.
- **Narsil Reforged:** Legacy Refactoring protocol. Use the 'Strangler Fig' pattern to safely modernize technical debt.
- **The Phial of Galadriel:** Shadow Hunt. Hypothesize and mitigate 3 critical edge cases before quest completion.
- **Harness Probe:** Check project health (Git, Progress, Bootstrap) before action.
- **BDD:** Define behavior before build (Given/When/Then).
- **TDD:** Proof before alloy. Protect behavior with tests while building.
- **SOLID:** Keep design changeable and responsibilities clear.
- **ADR:** Record decisions that matter.
- **Wizard Harness:** Keep memory (Progress) and bootstrap in project.
- **Refactoring:** Change structure without changing behavior.
- **Testing:** Smallest honest feedback loop. Exit code is the judge.
- **Code Review:** Find risk before merge.
- **Caveman:** Compress language, keep substance.

Best default stack for non-trivial engineering work:

1. **Context Phase:** Map the quest and name the danger in `docs/contexto.md`.
2. **Archive Consultation:** Read the Palantír Map to understand dependencies and pillars.
3. **Token Scarcity Check:** Can the Palantír or Grep answer this without a full file read?
4. **Harness Probe:** Ensure project has Mandates and Progress logs.
5. **BDD:** Frame behavior scenarios.
6. **ADR:** If design choice matters, record it.
7. **SOLID:** Shape boundaries and dependencies.
8. **TDD:** Write the test that proves the scenario.
9. **Implementation:** Code under the protection of the test.
10. **Refactor:** Only under protection.
11. **Shadow Hunt:** Hypothesize 3 failure scenarios (Shadows) and prove resilience.
12. **Review:** Check for surgical runes and risk.
