# Gandalf

Gandalf is a multi-target guide plugin and skill pack for intentional engineering work.

It is designed to work across:

- Codex
- Claude
- Gemini

## Purpose

Gandalf acts as a guide before implementation:

- clarify quest
- challenge weak assumptions
- choose pattern
- route to the right skill or workflow
- keep language sparse and exact

Voice: Gandalf from Tolkien, compressed with caveman discipline.

## Method stack

- BDD
- TDD
- SOLID
- ADR
- Harness
- Refactoring
- Testing
- Code Review
- Caveman

## Repository layout

- `gandalf-core/`: source of truth
- `gandalf/`: local active skill shape
- `targets/codex/`: Codex plugin package
- `targets/claude/`: Claude plugin package
- `targets/gemini/`: Gemini skill package
- `scripts/build-gandalf.py`: regenerate all targets from core

## Build

```bash
python3 scripts/build-gandalf.py
```

## Current design

One core. Many targets.

Do not edit generated target files first.
Edit `gandalf-core/`, then rebuild.
