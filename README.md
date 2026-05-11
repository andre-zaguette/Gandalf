# 🧙 Gandalf

Gandalf is a high-discipline software engineering framework for AI agents. It decouples **Methodology** (*Gandalf the Grey*) from **Orchestration** (*Gandalf the White*), allowing agents to operate with "Wizard-level" technical rigor, security, and cost efficiency.

---

## 🏛️ Architecture

- **Gandalf the Grey (The Soul):** A portable methodology package (plugin/skill). It contains the persona, patterns (BDD, TDD, SOLID), dialogue policies, and engineering artifacts.
- **Gandalf the White (The Hand):** The operational agent layer. It consumes the "Grey" package to classify tasks, enforce guardrails, and lead quests from ambiguity to execution.

---

## 🛠️ High Wizardry Artifacts

Gandalf comes equipped with several "Artes Arcanas" to protect and guide your project:

- **The Palantír Map (Second Brain):** A structural codebase index (`docs/archive/PALANTIR.md`) that maps dependencies and API signatures to minimize token usage.
- **The Mirror of Galadriel (Self-Audit):** A quality rubric (`wizard-mirror.py`) that forces the agent to grade its own code before committing.
- **Mithril Armor (Security):** An automated scanner (`mithril-armor.py`) that detects secrets and vulnerabilities.
- **The Gates of Argonath (Git Hooks):** Enforcement scripts (`gates-of-argonath.sh`) that prevent commits if the harness or progress log is out of sync.
- **The Red Book of Westmarch (Retrospectives):** A persistent log (`RED_BOOK.md`) for recording hard-won lessons and anti-patterns.
- **The Fellowship Contract:** A negotiation template (`CONTRACT.yaml`) for cross-repo or multi-agent interface agreements.

---

## 🚀 Getting Started

### 1. Installation
Clone the repository and build the targets:
```bash
git clone https://github.com/andre-zaguette/Gandalf
cd Gandalf
python3 scripts/build-gandalf.py
```

### 2. Initializing a Project (The Wizard Harness)
To bring Gandalf's discipline to a new project, you must build the **Arreio (Harness)**. Gandalf the White will offer to do this automatically, but you can also manually copy the templates:

1. Copy `WIZARD.md`, `QUEST_PROGRESS.md`, and `wizard-bootstrap.sh` from `assets/templates/` to your project root.
2. Run the **Archivist** to create your first Palantír Map:
   ```bash
   python3 scripts/wizard-archivist.py .
   ```
3. Initialize the **Gates of Argonath** (Optional but recommended):
   ```bash
   cp scripts/gates-of-argonath.sh .git/hooks/pre-commit
   chmod +x .git/hooks/pre-commit
   ```

### 3. Running a Quest
Once the harness is set, every session should follow the **Wizard Workflow**:

1. **Bootstrap:** Run `./scripts/wizard-bootstrap.sh` to load context.
2. **Context:** Define the objective and danger in `docs/contexto.md`.
3. **Execution:** Proceed with TDD and Surgical Runes.
4. **Finalize:** Run the **Mirror of Galadriel** and **Mithril Armor** before committing.
5. **Record:** Update the `QUEST_PROGRESS.md` and the **Red Book** if lessons were learned.

---

## 📜 Core Law: The Lembas Protocol

Gandalf is designed for **Token Efficiency**:
- **Palantír-First:** Never read raw files if the Palantír Map can provide the answer.
- **Lembas Density:** High-density reasoning, zero-filler dialogue.
- **Surgical Reads:** Never ingest more than 100 lines at once. Use `grep_search` and line ranges.

---

## 🦅 Advanced Protocols

- **The Eagle's Flight (Swift Quest):** For low-risk, trivial fixes. Bypasses heavy ceremony but keeps Mithril Armor active.
- **Narsil Reforged (Legacy Refactoring):** A "Strangler Fig" protocol for safely modernizing technical debt.
- **The Phial of Galadriel (Shadow Hunt):** A mandatory phase to identify and mitigate 3 critical edge cases before completion.

---

*"Im Gandalf. Hain echant — stays written what I have done."*
