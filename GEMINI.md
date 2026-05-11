# Wizard Mandates: Gandalf Repository

These principles are foundational for all wizard-engineering operations in this workspace.

## 1. Map the Quest (Clarity & Context)
- **Sharp Questions First:** Before coding, uncover hidden assumptions.
- **Context Validation:** Every non-trivial change requires a validated `docs/contexto.md`.
- **Name the Danger:** Explicitly state what could go wrong before proceeding.

## 2. Proof Before Alloy (TDD & Verification)
- **Test-First:** Define success with a test before writing logic.
- **Evidence Over Vibes:** No change is "done" without automated proof.
- **Small Loops:** Deliver working increments every 5-20 minutes.

## 3. Surgical Runes (Precision & Style)
- **Minimal Footprint:** Change only what is required for the quest.
- **Style Harmony:** Rigorously follow existing patterns and naming.
- **Cleanup:** Remove only the dead code your changes made obsolete.

## 4. Persistent Memory (Harness & Progress)
- **Quest Log:** Update `QUEST_PROGRESS.md` at the end of every session.
- **Automated Bootstrap:** Use `scripts/wizard-bootstrap.sh` to load context.
- **Harness Integrity:** If the project lacks a harness, build it before coding features.
