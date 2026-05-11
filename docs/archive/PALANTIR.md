# The Palantír Map: Gandalf

## 🏰 Citadel Pillars (God Nodes)
These files are central to the realm's architecture:
- `sys`
- `re`
- `os`
- `pathlib`
- `Path`

## 🗺️ Territory Map
- **Root**: README.md, .gitignore, DEVELOPER.md, QUEST_PROGRESS.md, GEMINI.md
- **agents/**: 
  - **agents/gandalf-the-white/**: AGENT.md
    - **agents/gandalf-the-white/references/**: operating-model.md
- **docs/**: contexto.md
  - **docs/archive/**: PALANTIR.md, MAP.json
- **packages/**: 
  - **packages/gandalf-the-grey/**: manifest.json
    - **packages/gandalf-the-grey/core/**: patterns.md, dialogue.md, routing.md, persona.md
      - **packages/gandalf-the-grey/core/assets/**: gandalf-grey-small.svg, gandalf-grey.svg
        - **packages/gandalf-the-grey/core/assets/templates/**: CONTRACT.yaml, gates-of-argonath.sh, wizard-archivist.py, wizard-mirror.py, RED_BOOK.md, wizard-bootstrap.sh, mithril-armor.py, QUEST_PROGRESS.md, WIZARD.md
    - **packages/gandalf-the-grey/plugin/**: 
      - **packages/gandalf-the-grey/plugin/skills/**: 
        - **packages/gandalf-the-grey/plugin/skills/gandalf-the-grey/**: SKILL.md
          - **packages/gandalf-the-grey/plugin/skills/gandalf-the-grey/agents/**: openai.yaml
          - **packages/gandalf-the-grey/plugin/skills/gandalf-the-grey/assets/**: gandalf-grey-small.svg, gandalf-grey.svg
            - **packages/gandalf-the-grey/plugin/skills/gandalf-the-grey/assets/templates/**: CONTRACT.yaml, gates-of-argonath.sh, wizard-archivist.py, wizard-mirror.py, RED_BOOK.md, wizard-bootstrap.sh, mithril-armor.py, QUEST_PROGRESS.md, WIZARD.md
          - **packages/gandalf-the-grey/plugin/skills/gandalf-the-grey/references/**: dialogue-style.md, guiding-patterns.md, routing-map.md
    - **packages/gandalf-the-grey/targets/**: 
      - **packages/gandalf-the-grey/targets/claude/**: 
        - **packages/gandalf-the-grey/targets/claude/.claude-plugin/**: plugin.json, marketplace.json
        - **packages/gandalf-the-grey/targets/claude/gandalf-the-grey/**: SKILL.md
          - **packages/gandalf-the-grey/targets/claude/gandalf-the-grey/assets/**: gandalf-grey-small.svg, gandalf-grey.svg
            - **packages/gandalf-the-grey/targets/claude/gandalf-the-grey/assets/templates/**: CONTRACT.yaml, gates-of-argonath.sh, wizard-archivist.py, wizard-mirror.py, RED_BOOK.md, wizard-bootstrap.sh, mithril-armor.py, QUEST_PROGRESS.md, WIZARD.md
          - **packages/gandalf-the-grey/targets/claude/gandalf-the-grey/references/**: dialogue-style.md, guiding-patterns.md, routing-map.md
      - **packages/gandalf-the-grey/targets/codex/**: 
        - **packages/gandalf-the-grey/targets/codex/.agents/**: 
          - **packages/gandalf-the-grey/targets/codex/.agents/plugins/**: marketplace.json
        - **packages/gandalf-the-grey/targets/codex/plugins/**: 
          - **packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/**: 
            - **packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/.codex-plugin/**: plugin.json
            - **packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/assets/**: gandalf-grey-small.svg, gandalf-grey.svg
              - **packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/assets/templates/**: CONTRACT.yaml, gates-of-argonath.sh, wizard-archivist.py, wizard-mirror.py, RED_BOOK.md, wizard-bootstrap.sh, mithril-armor.py, QUEST_PROGRESS.md, WIZARD.md
            - **packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/skills/**: 
              - **packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/skills/gandalf-the-grey/**: SKILL.md
                - **packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/skills/gandalf-the-grey/agents/**: openai.yaml
                - **packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/skills/gandalf-the-grey/assets/**: gandalf-grey-small.svg, gandalf-grey.svg
                  - **packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/skills/gandalf-the-grey/assets/templates/**: CONTRACT.yaml, gates-of-argonath.sh, wizard-archivist.py, wizard-mirror.py, RED_BOOK.md, wizard-bootstrap.sh, mithril-armor.py, QUEST_PROGRESS.md, WIZARD.md
                - **packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/skills/gandalf-the-grey/references/**: dialogue-style.md, guiding-patterns.md, routing-map.md
      - **packages/gandalf-the-grey/targets/gemini/**: README.md, DEVELOPER.md
        - **packages/gandalf-the-grey/targets/gemini/gandalf-the-grey/**: SKILL.md
          - **packages/gandalf-the-grey/targets/gemini/gandalf-the-grey/assets/**: 
            - **packages/gandalf-the-grey/targets/gemini/gandalf-the-grey/assets/templates/**: CONTRACT.yaml, gates-of-argonath.sh, wizard-archivist.py, wizard-mirror.py, RED_BOOK.md, wizard-bootstrap.sh, mithril-armor.py, QUEST_PROGRESS.md, WIZARD.md
          - **packages/gandalf-the-grey/targets/gemini/gandalf-the-grey/bin/**: gandalf-check-update.sh
          - **packages/gandalf-the-grey/targets/gemini/gandalf-the-grey/references/**: dialogue-style.md, guiding-patterns.md, routing-map.md
- **scripts/**: wizard-bootstrap.sh, build-gandalf.py

## ⛓️ Ley Lines (Dependencies)
- `packages/gandalf-the-grey/core/assets/templates/wizard-archivist.py` depends on: sys, pathlib, re, Path, detection...
- `packages/gandalf-the-grey/core/assets/templates/wizard-mirror.py` depends on: sys
- `packages/gandalf-the-grey/core/assets/templates/mithril-armor.py` depends on: sys, re, os
- `packages/gandalf-the-grey/plugin/skills/gandalf-the-grey/assets/templates/wizard-archivist.py` depends on: sys, pathlib, re, Path, detection...
- `packages/gandalf-the-grey/plugin/skills/gandalf-the-grey/assets/templates/wizard-mirror.py` depends on: sys
- `packages/gandalf-the-grey/plugin/skills/gandalf-the-grey/assets/templates/mithril-armor.py` depends on: sys, re, os
- `packages/gandalf-the-grey/targets/gemini/gandalf-the-grey/assets/templates/wizard-archivist.py` depends on: sys, pathlib, re, Path, detection...
- `packages/gandalf-the-grey/targets/gemini/gandalf-the-grey/assets/templates/wizard-mirror.py` depends on: sys
- `packages/gandalf-the-grey/targets/gemini/gandalf-the-grey/assets/templates/mithril-armor.py` depends on: sys, re, os
- `packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/assets/templates/wizard-archivist.py` depends on: sys, pathlib, re, Path, detection...
- `packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/assets/templates/wizard-mirror.py` depends on: sys
- `packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/assets/templates/mithril-armor.py` depends on: sys, re, os
- `packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/skills/gandalf-the-grey/assets/templates/wizard-archivist.py` depends on: sys, pathlib, re, Path, detection...
- `packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/skills/gandalf-the-grey/assets/templates/wizard-mirror.py` depends on: sys
- `packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/skills/gandalf-the-grey/assets/templates/mithril-armor.py` depends on: sys, re, os
- `packages/gandalf-the-grey/targets/claude/gandalf-the-grey/assets/templates/wizard-archivist.py` depends on: sys, pathlib, re, Path, detection...
- `packages/gandalf-the-grey/targets/claude/gandalf-the-grey/assets/templates/wizard-mirror.py` depends on: sys
- `packages/gandalf-the-grey/targets/claude/gandalf-the-grey/assets/templates/mithril-armor.py` depends on: sys, re, os
- `scripts/build-gandalf.py` depends on: the, shutil, __future__, pathlib, annotations...

## 📜 Rune Signatures (APIs)
### `packages/gandalf-the-grey/core/assets/templates/wizard-archivist.py`
- `class WizardArchivist:`
- `def __init__(self, root_dir)`
- `def should_ignore(self, path)`
- `def scan(self)`
- `def analyze_file(self, rel_path)`
- `def identify_god_nodes(self)`
- `def generate_reports(self)`

### `packages/gandalf-the-grey/core/assets/templates/wizard-mirror.py`
- `def self_audit()`

### `packages/gandalf-the-grey/core/assets/templates/mithril-armor.py`
- `def scan_for_shadows(directory=".")`

### `packages/gandalf-the-grey/plugin/skills/gandalf-the-grey/assets/templates/wizard-archivist.py`
- `class WizardArchivist:`
- `def __init__(self, root_dir)`
- `def should_ignore(self, path)`
- `def scan(self)`
- `def analyze_file(self, rel_path)`
- `def identify_god_nodes(self)`
- `def generate_reports(self)`

### `packages/gandalf-the-grey/plugin/skills/gandalf-the-grey/assets/templates/wizard-mirror.py`
- `def self_audit()`

### `packages/gandalf-the-grey/plugin/skills/gandalf-the-grey/assets/templates/mithril-armor.py`
- `def scan_for_shadows(directory=".")`

### `packages/gandalf-the-grey/targets/gemini/gandalf-the-grey/assets/templates/wizard-archivist.py`
- `class WizardArchivist:`
- `def __init__(self, root_dir)`
- `def should_ignore(self, path)`
- `def scan(self)`
- `def analyze_file(self, rel_path)`
- `def identify_god_nodes(self)`
- `def generate_reports(self)`

### `packages/gandalf-the-grey/targets/gemini/gandalf-the-grey/assets/templates/wizard-mirror.py`
- `def self_audit()`

### `packages/gandalf-the-grey/targets/gemini/gandalf-the-grey/assets/templates/mithril-armor.py`
- `def scan_for_shadows(directory=".")`

### `packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/assets/templates/wizard-archivist.py`
- `class WizardArchivist:`
- `def __init__(self, root_dir)`
- `def should_ignore(self, path)`
- `def scan(self)`
- `def analyze_file(self, rel_path)`
- `def identify_god_nodes(self)`
- `def generate_reports(self)`

### `packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/assets/templates/wizard-mirror.py`
- `def self_audit()`

### `packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/assets/templates/mithril-armor.py`
- `def scan_for_shadows(directory=".")`

### `packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/skills/gandalf-the-grey/assets/templates/wizard-archivist.py`
- `class WizardArchivist:`
- `def __init__(self, root_dir)`
- `def should_ignore(self, path)`
- `def scan(self)`
- `def analyze_file(self, rel_path)`
- `def identify_god_nodes(self)`
- `def generate_reports(self)`

### `packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/skills/gandalf-the-grey/assets/templates/wizard-mirror.py`
- `def self_audit()`

### `packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/skills/gandalf-the-grey/assets/templates/mithril-armor.py`
- `def scan_for_shadows(directory=".")`

### `packages/gandalf-the-grey/targets/claude/gandalf-the-grey/assets/templates/wizard-archivist.py`
- `class WizardArchivist:`
- `def __init__(self, root_dir)`
- `def should_ignore(self, path)`
- `def scan(self)`
- `def analyze_file(self, rel_path)`
- `def identify_god_nodes(self)`
- `def generate_reports(self)`

### `packages/gandalf-the-grey/targets/claude/gandalf-the-grey/assets/templates/wizard-mirror.py`
- `def self_audit()`

### `packages/gandalf-the-grey/targets/claude/gandalf-the-grey/assets/templates/mithril-armor.py`
- `def scan_for_shadows(directory=".")`

### `scripts/build-gandalf.py`
- `def read_text(path: Path) -> str`
- `def write_text(path: Path, content: str) -> None`
- `def copy_file(src: Path, dst: Path) -> None`
- `def build_skill_md(meta: dict[str, str]) -> str`
- `def build_openai_yaml(meta: dict[str, str]) -> str`
- `def build_codex_plugin_json(meta: dict[str, str]) -> str`
- `def build_codex_marketplace() -> str`
- `def build_claude_plugin_json(meta: dict[str, str]) -> str`
- `def build_claude_marketplace(meta: dict[str, str]) -> str`
- `def build_gemini_readme() -> str`
- `def build_gemini_developer() -> str`
- `def build_gemini_update_script() -> str`
- `def generate()`

