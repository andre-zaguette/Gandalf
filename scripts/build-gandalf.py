#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CORE = ROOT / "gandalf-core"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)


def build_skill_md(meta: dict[str, str]) -> str:
    persona = read_text(CORE / "persona.md")
    patterns = read_text(CORE / "patterns.md")
    routing = read_text(CORE / "routing.md")
    dialogue = read_text(CORE / "dialogue.md")

    return f"""---
name: {meta["name"]}
description: Gandalf, guide of this second brain. Use when the user wants senior guidance before coding, pattern selection, architecture judgment, assumption checks, or a more intentional workflow. Gandalf maps the request to the right local skill or platform path, asks pointed questions first, applies BDD, TDD, ADR, Refactoring, Code Review, Harness, Testing, and adds SOLID as a core design pattern. Communication style: Gandalf from Tolkien with caveman compression: wise, sparse, exact, probing, no filler.
---

# Gandalf

{persona}

## Core law

Context first. Then path. Then code.

If request is non-trivial:

1. state problem in one sentence
2. name main risk
3. choose pattern and workflow
4. route to right skill
5. only then implement

## Canonical patterns

Read `references/guiding-patterns.md` when pattern choice or method needs grounding.

{patterns}

## Routing

Read `references/routing-map.md` when task needs exact skill selection.

{routing}

## How to question

Read `references/dialogue-style.md` when user explicitly wants Gandalf mode.

{dialogue}

## Default operating sequence

1. Name the quest.
2. Name the danger.
3. Choose the road.
4. Invoke the right tool or skill.
5. Verify with evidence, not vibes.
6. Leave trace in the second brain if lesson repeats.

## Output shape

- Quest
- Risk
- Chosen path
- Skill or pattern
- Next step
"""


def build_openai_yaml(meta: dict[str, str]) -> str:
    return f"""interface:
  display_name: "{meta["display_name"]}"
  short_description: "{meta["short_description"]}"
  icon_small: "./assets/gandalf-small.svg"
  icon_large: "./assets/gandalf.svg"
  brand_color: "{meta["brand_color"]}"
  default_prompt: "{meta["default_prompt"]}"
"""


def build_codex_plugin_json(meta: dict[str, str]) -> str:
    data = {
        "name": meta["name"],
        "version": meta["version"],
        "description": meta["codex_plugin_description"],
        "author": {
            "name": meta["author_name"],
            "url": meta["author_url"],
        },
        "homepage": meta["homepage"],
        "repository": meta["repository"],
        "license": meta["license"],
        "keywords": [
            "guidance",
            "architecture",
            "solid",
            "productivity",
        ],
        "skills": "./skills/",
        "interface": {
            "displayName": meta["display_name"],
            "shortDescription": meta["short_description"],
            "longDescription": meta["codex_plugin_description"],
            "developerName": meta["author_name"],
            "category": "Productivity",
            "capabilities": ["Write"],
            "websiteURL": meta["homepage"],
            "privacyPolicyURL": meta["repository"],
            "termsOfServiceURL": meta["repository"],
            "defaultPrompt": [meta["default_prompt"].replace("$gandalf", "Gandalf")],
            "composerIcon": "./assets/gandalf-small.svg",
            "logo": "./assets/gandalf.svg",
            "screenshots": [],
            "brandColor": meta["brand_color"],
        },
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


def build_codex_marketplace() -> str:
    data = {
        "name": "gandalf-repo",
        "interface": {"displayName": "Gandalf Repo"},
        "plugins": [
            {
                "name": "gandalf",
                "source": {"source": "local", "path": "./plugins/gandalf"},
                "policy": {
                    "installation": "AVAILABLE",
                    "authentication": "ON_INSTALL",
                },
                "category": "Productivity",
            }
        ],
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


def build_claude_plugin_json(meta: dict[str, str]) -> str:
    data = {
        "name": meta["name"],
        "description": meta["claude_plugin_description"],
        "author": {
            "name": meta["author_name"],
            "url": meta["author_url"],
        },
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


def build_claude_marketplace(meta: dict[str, str]) -> str:
    data = {
        "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
        "name": "gandalf",
        "description": meta["claude_plugin_description"],
        "owner": {
            "name": meta["author_name"],
            "url": meta["author_url"],
        },
        "plugins": [
            {
                "name": "gandalf",
                "description": "Gandalf guide. Wise, sparse, sharp engineering judgment.",
                "source": "./",
                "category": "productivity",
            }
        ],
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


def build_gemini_readme() -> str:
    return """# Gandalf

Gandalf is a Gemini-compatible guide skill packaged from the shared Gandalf core.

Purpose:

- question before wrong action
- route broad asks to the right method
- apply BDD, TDD, SOLID, ADR, Harness, Refactoring, Testing, Review
- speak with Gandalf gravitas plus caveman brevity

Install shape:

- `gandalf/SKILL.md` is the skill brain
- `gandalf/bin/gandalf-check-update.sh` is an optional update sensor
"""


def build_gemini_developer() -> str:
    return """# Developer Guide

This Gemini target is generated from `gandalf-core/` by `scripts/build-gandalf.py`.

Rules:

- edit shared intent in `gandalf-core/`
- regenerate targets
- avoid manual edits in generated target files

Main generated files:

- `gandalf/SKILL.md`
- `gandalf/bin/gandalf-check-update.sh`
- target README and metadata files
"""


def build_gemini_update_script() -> str:
    return """#!/usr/bin/env bash
set -euo pipefail

# Silent best-effort update check for Gandalf.
# Repo is public-facing by default. If network or auth fails, stay silent.

CACHE_DIR="${XDG_CACHE_HOME:-$HOME/.cache}/gandalf"
CACHE_FILE="$CACHE_DIR/last-check"
mkdir -p "$CACHE_DIR"

FORCE=false
for arg in "$@"; do
  case "$arg" in
    --force) FORCE=true ;;
  esac
done

if [ "$FORCE" = false ] && [ -f "$CACHE_FILE" ]; then
  MTIME=$(stat -c %Y "$CACHE_FILE" 2>/dev/null || stat -f %m "$CACHE_FILE" 2>/dev/null || echo 0)
  AGE=$(( $(date +%s) - MTIME ))
  if [ "$AGE" -lt 21600 ]; then
    cat "$CACHE_FILE"
    exit 0
  fi
fi

SHA=""
if command -v gh >/dev/null 2>&1; then
  SHA=$(gh api repos/andre-zaguette/SecondBrain/commits/main --jq '.sha' 2>/dev/null || true)
fi

if [ -z "$SHA" ] && command -v curl >/dev/null 2>&1; then
  SHA=$(curl -s -m 5 https://api.github.com/repos/andre-zaguette/SecondBrain/commits/main 2>/dev/null | grep -oE '"sha":[[:space:]]*"[a-f0-9]+"' | head -1 | cut -d'"' -f4 || true)
fi

if [ -z "$SHA" ]; then
  : > "$CACHE_FILE"
  exit 0
fi

REPORT="🧙 Gandalf: source repo seen at ${SHA:0:7}. Rebuild or reinstall if local package is older."
echo "$REPORT" > "$CACHE_FILE"
echo "$REPORT"
"""


def build_targets() -> None:
    meta = json.loads((CORE / "manifest.json").read_text(encoding="utf-8"))
    skill_md = build_skill_md(meta)
    openai_yaml = build_openai_yaml(meta)
    guiding = read_text(CORE / "patterns.md")
    routing = read_text(CORE / "routing.md")
    dialogue = read_text(CORE / "dialogue.md")

    local_skill = ROOT / "gandalf"
    write_text(local_skill / "SKILL.md", skill_md)
    write_text(local_skill / "agents" / "openai.yaml", openai_yaml)
    write_text(local_skill / "references" / "guiding-patterns.md", "# Guiding Patterns\n\n" + guiding)
    write_text(local_skill / "references" / "routing-map.md", "# Routing Map\n\n" + routing)
    write_text(local_skill / "references" / "dialogue-style.md", "# Dialogue Style\n\n" + dialogue)
    copy_file(CORE / "assets" / "gandalf-small.svg", local_skill / "assets" / "gandalf-small.svg")
    copy_file(CORE / "assets" / "gandalf.svg", local_skill / "assets" / "gandalf.svg")

    codex_root = ROOT / "targets" / "codex"
    write_text(codex_root / ".agents" / "plugins" / "marketplace.json", build_codex_marketplace())
    codex_plugin = codex_root / "plugins" / "gandalf"
    write_text(codex_plugin / ".codex-plugin" / "plugin.json", build_codex_plugin_json(meta))
    write_text(codex_plugin / "skills" / "gandalf" / "SKILL.md", skill_md)
    write_text(codex_plugin / "skills" / "gandalf" / "agents" / "openai.yaml", openai_yaml)
    write_text(codex_plugin / "skills" / "gandalf" / "references" / "guiding-patterns.md", "# Guiding Patterns\n\n" + guiding)
    write_text(codex_plugin / "skills" / "gandalf" / "references" / "routing-map.md", "# Routing Map\n\n" + routing)
    write_text(codex_plugin / "skills" / "gandalf" / "references" / "dialogue-style.md", "# Dialogue Style\n\n" + dialogue)
    copy_file(CORE / "assets" / "gandalf-small.svg", codex_plugin / "assets" / "gandalf-small.svg")
    copy_file(CORE / "assets" / "gandalf.svg", codex_plugin / "assets" / "gandalf.svg")
    copy_file(CORE / "assets" / "gandalf-small.svg", codex_plugin / "skills" / "gandalf" / "assets" / "gandalf-small.svg")
    copy_file(CORE / "assets" / "gandalf.svg", codex_plugin / "skills" / "gandalf" / "assets" / "gandalf.svg")

    claude_root = ROOT / "targets" / "claude"
    write_text(claude_root / ".claude-plugin" / "plugin.json", build_claude_plugin_json(meta))
    write_text(claude_root / ".claude-plugin" / "marketplace.json", build_claude_marketplace(meta))
    write_text(claude_root / "gandalf" / "SKILL.md", skill_md)
    write_text(claude_root / "gandalf" / "references" / "guiding-patterns.md", "# Guiding Patterns\n\n" + guiding)
    write_text(claude_root / "gandalf" / "references" / "routing-map.md", "# Routing Map\n\n" + routing)
    write_text(claude_root / "gandalf" / "references" / "dialogue-style.md", "# Dialogue Style\n\n" + dialogue)
    copy_file(CORE / "assets" / "gandalf-small.svg", claude_root / "gandalf" / "assets" / "gandalf-small.svg")
    copy_file(CORE / "assets" / "gandalf.svg", claude_root / "gandalf" / "assets" / "gandalf.svg")

    gemini_root = ROOT / "targets" / "gemini"
    write_text(gemini_root / "README.md", build_gemini_readme())
    write_text(gemini_root / "DEVELOPER.md", build_gemini_developer())
    write_text(gemini_root / "gandalf" / "SKILL.md", skill_md)
    write_text(gemini_root / "gandalf" / "bin" / "gandalf-check-update.sh", build_gemini_update_script())
    write_text(gemini_root / "gandalf" / "references" / "guiding-patterns.md", "# Guiding Patterns\n\n" + guiding)
    write_text(gemini_root / "gandalf" / "references" / "routing-map.md", "# Routing Map\n\n" + routing)
    write_text(gemini_root / "gandalf" / "references" / "dialogue-style.md", "# Dialogue Style\n\n" + dialogue)
    (gemini_root / "gandalf" / "bin" / "gandalf-check-update.sh").chmod(0o755)


if __name__ == "__main__":
    build_targets()
    print("Generated Gandalf targets: local, codex, claude, gemini")
