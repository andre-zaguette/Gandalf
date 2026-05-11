#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GREY = ROOT / "packages" / "gandalf-the-grey"
CORE = GREY / "core"
PLUGIN = GREY / "plugin"
TARGETS = GREY / "targets"


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
name: {meta['name']}
description: Gandalf the Grey, plugin guide layer. Use when you want senior guidance, pattern selection, and disciplined engineering. Grey enforces the 'Wizard Harness' (Quest Progress, Bootstrap), performs 'Harness Probes', and uses 'Socratic Interrogation' to reveal risk. Applies BDD, TDD (Proof before Alloy), SOLID, ADR, and Surgical Runes. Communication style: Gandalf from Tolkien with caveman compression: wise, sparse, exact, probing.
---

# Gandalf the Grey

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
6. Leave trace where lesson repeats.

## Output shape

- Quest
- Risk
- Chosen path
- Skill or pattern
- Next step
"""


def build_openai_yaml(meta: dict[str, str]) -> str:
    return f"""interface:
  display_name: \"{meta['display_name']}\"
  short_description: \"{meta['short_description']}\"
  icon_small: \"./assets/gandalf-grey-small.svg\"
  icon_large: \"./assets/gandalf-grey.svg\"
  brand_color: \"{meta['brand_color']}\"
  default_prompt: \"{meta['default_prompt']}\"
"""


def build_codex_plugin_json(meta: dict[str, str]) -> str:
    data = {
        "name": meta["name"],
        "version": meta["version"],
        "description": meta["codex_plugin_description"],
        "author": {"name": meta["author_name"], "url": meta["author_url"]},
        "homepage": meta["homepage"],
        "repository": meta["repository"],
        "license": meta["license"],
        "keywords": ["guidance", "architecture", "solid", "productivity"],
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
            "defaultPrompt": [meta["default_prompt"].replace("$gandalf-the-grey", "Gandalf the Grey")],
            "composerIcon": "./assets/gandalf-grey-small.svg",
            "logo": "./assets/gandalf-grey.svg",
            "screenshots": [],
            "brandColor": meta["brand_color"],
        },
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


def build_codex_marketplace() -> str:
    data = {
        "name": "gandalf-the-grey-repo",
        "interface": {"displayName": "Gandalf the Grey Repo"},
        "plugins": [{
            "name": "gandalf-the-grey",
            "source": {"source": "local", "path": "./plugins/gandalf-the-grey"},
            "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
            "category": "Productivity",
        }],
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


def build_claude_plugin_json(meta: dict[str, str]) -> str:
    data = {"name": meta["name"], "description": meta["claude_plugin_description"], "author": {"name": meta["author_name"], "url": meta["author_url"]}}
    return json.dumps(data, indent=2, ensure_ascii=False)


def build_claude_marketplace(meta: dict[str, str]) -> str:
    data = {
        "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
        "name": "gandalf-the-grey",
        "description": meta["claude_plugin_description"],
        "owner": {"name": meta["author_name"], "url": meta["author_url"]},
        "plugins": [{"name": "gandalf-the-grey", "description": "Gandalf the Grey plugin. Wise, sparse, sharp engineering judgment.", "source": "./", "category": "productivity"}],
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


def build_gemini_readme() -> str:
    return """# Gandalf the Grey

Gandalf the Grey is a Gemini-compatible guide plugin packaged from the shared Grey core.

Purpose:

- question before wrong action
- route broad asks to the right method
- apply BDD, TDD, SOLID, ADR, Harness, Refactoring, Testing, Review
- speak with Gandalf gravitas plus caveman brevity
"""


def build_gemini_developer() -> str:
    return """# Developer Guide

This Gemini target is generated from `packages/gandalf-the-grey/core/` by `scripts/build-gandalf.py`.

Edit core. Rebuild. Do not hand-edit generated target files first.
"""


def build_gemini_update_script() -> str:
    return """#!/usr/bin/env bash
set -euo pipefail
CACHE_DIR="${XDG_CACHE_HOME:-$HOME/.cache}/gandalf-the-grey"
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
  SHA=$(gh api repos/andre-zaguette/Gandalf/commits/main --jq '.sha' 2>/dev/null || true)
fi
if [ -z "$SHA" ] && command -v curl >/dev/null 2>&1; then
  SHA=$(curl -s -m 5 https://api.github.com/repos/andre-zaguette/Gandalf/commits/main 2>/dev/null | grep -oE '"sha":[[:space:]]*"[a-f0-9]+"' | head -1 | cut -d'"' -f4 || true)
fi
if [ -z "$SHA" ]; then
  : > "$CACHE_FILE"
  exit 0
fi
REPORT="🧙 Grey: source repo seen at ${SHA:0:7}. Rebuild or reinstall if local package is older."
echo "$REPORT" > "$CACHE_FILE"
echo "$REPORT"
"""


def generate():
    meta = json.loads((GREY / 'manifest.json').read_text(encoding='utf-8'))
    skill_md = build_skill_md(meta)
    openai_yaml = build_openai_yaml(meta)
    guiding = '# Guiding Patterns\n\n' + read_text(CORE / 'patterns.md')
    routing = '# Routing Map\n\n' + read_text(CORE / 'routing.md')
    dialogue = '# Dialogue Style\n\n' + read_text(CORE / 'dialogue.md')

    templates = CORE / 'assets' / 'templates'
    template_files = ['WIZARD.md', 'QUEST_PROGRESS.md', 'wizard-bootstrap.sh', 'wizard-archivist.py', 'RED_BOOK.md', 'gates-of-argonath.sh', 'wizard-mirror.py', 'CONTRACT.yaml', 'mithril-armor.py', 'CHRONICLE.md']

    skill_root = PLUGIN / 'skills' / 'gandalf-the-grey'
    write_text(skill_root / 'SKILL.md', skill_md)
    write_text(skill_root / 'agents' / 'openai.yaml', openai_yaml)
    write_text(skill_root / 'references' / 'guiding-patterns.md', guiding)
    write_text(skill_root / 'references' / 'routing-map.md', routing)
    write_text(skill_root / 'references' / 'dialogue-style.md', dialogue)
    copy_file(CORE / 'assets' / 'gandalf-grey-small.svg', skill_root / 'assets' / 'gandalf-grey-small.svg')
    copy_file(CORE / 'assets' / 'gandalf-grey.svg', skill_root / 'assets' / 'gandalf-grey.svg')
    for f in template_files:
        copy_file(templates / f, skill_root / 'assets' / 'templates' / f)

    codex_root = TARGETS / 'codex'
    codex_plugin = codex_root / 'plugins' / 'gandalf-the-grey'
    write_text(codex_root / '.agents' / 'plugins' / 'marketplace.json', build_codex_marketplace())
    write_text(codex_plugin / '.codex-plugin' / 'plugin.json', build_codex_plugin_json(meta))
    write_text(codex_plugin / 'skills' / 'gandalf-the-grey' / 'SKILL.md', skill_md)
    write_text(codex_plugin / 'skills' / 'gandalf-the-grey' / 'agents' / 'openai.yaml', openai_yaml)
    write_text(codex_plugin / 'skills' / 'gandalf-the-grey' / 'references' / 'guiding-patterns.md', guiding)
    write_text(codex_plugin / 'skills' / 'gandalf-the-grey' / 'references' / 'routing-map.md', routing)
    write_text(codex_plugin / 'skills' / 'gandalf-the-grey' / 'references' / 'dialogue-style.md', dialogue)
    copy_file(CORE / 'assets' / 'gandalf-grey-small.svg', codex_plugin / 'assets' / 'gandalf-grey-small.svg')
    copy_file(CORE / 'assets' / 'gandalf-grey.svg', codex_plugin / 'assets' / 'gandalf-grey.svg')
    copy_file(CORE / 'assets' / 'gandalf-grey-small.svg', codex_plugin / 'skills' / 'gandalf-the-grey' / 'assets' / 'gandalf-grey-small.svg')
    copy_file(CORE / 'assets' / 'gandalf-grey.svg', codex_plugin / 'skills' / 'gandalf-the-grey' / 'assets' / 'gandalf-grey.svg')
    for f in template_files:
        copy_file(templates / f, codex_plugin / 'assets' / 'templates' / f)
        copy_file(templates / f, codex_plugin / 'skills' / 'gandalf-the-grey' / 'assets' / 'templates' / f)

    claude_root = TARGETS / 'claude'
    write_text(claude_root / '.claude-plugin' / 'plugin.json', build_claude_plugin_json(meta))
    write_text(claude_root / '.claude-plugin' / 'marketplace.json', build_claude_marketplace(meta))
    write_text(claude_root / 'gandalf-the-grey' / 'SKILL.md', skill_md)
    write_text(claude_root / 'gandalf-the-grey' / 'references' / 'guiding-patterns.md', guiding)
    write_text(claude_root / 'gandalf-the-grey' / 'references' / 'routing-map.md', routing)
    write_text(claude_root / 'gandalf-the-grey' / 'references' / 'dialogue-style.md', dialogue)
    copy_file(CORE / 'assets' / 'gandalf-grey-small.svg', claude_root / 'gandalf-the-grey' / 'assets' / 'gandalf-grey-small.svg')
    copy_file(CORE / 'assets' / 'gandalf-grey.svg', claude_root / 'gandalf-the-grey' / 'assets' / 'gandalf-grey.svg')
    for f in template_files:
        copy_file(templates / f, claude_root / 'gandalf-the-grey' / 'assets' / 'templates' / f)

    gemini_root = TARGETS / 'gemini'
    write_text(gemini_root / 'README.md', build_gemini_readme())
    write_text(gemini_root / 'DEVELOPER.md', build_gemini_developer())
    write_text(gemini_root / 'gandalf-the-grey' / 'SKILL.md', skill_md)
    write_text(gemini_root / 'gandalf-the-grey' / 'bin' / 'gandalf-check-update.sh', build_gemini_update_script())
    write_text(gemini_root / 'gandalf-the-grey' / 'references' / 'guiding-patterns.md', guiding)
    write_text(gemini_root / 'gandalf-the-grey' / 'references' / 'routing-map.md', routing)
    write_text(gemini_root / 'gandalf-the-grey' / 'references' / 'dialogue-style.md', dialogue)
    (gemini_root / 'gandalf-the-grey' / 'bin' / 'gandalf-check-update.sh').chmod(0o755)
    for f in template_files:
        copy_file(templates / f, gemini_root / 'gandalf-the-grey' / 'assets' / 'templates' / f)

if __name__ == '__main__':
    generate()
    print('Generated Gandalf the Grey plugin and targets')
