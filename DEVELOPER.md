# Developer Guide

## Rule

`gandalf-core/` is source of truth.

Targets are generated artifacts:

- `gandalf/`
- `targets/codex/`
- `targets/claude/`
- `targets/gemini/`

## Workflow

1. Edit core files in `gandalf-core/`
2. Run:

```bash
python3 scripts/build-gandalf.py
```

3. Review generated targets
4. Commit only when core and targets match

## Main files

- `gandalf-core/manifest.json`
- `gandalf-core/persona.md`
- `gandalf-core/patterns.md`
- `gandalf-core/routing.md`
- `gandalf-core/dialogue.md`
- `scripts/build-gandalf.py`

## Notes

- Gandalf is intentionally platform-agnostic at the core
- platform-specific packaging lives only under `targets/`
- the local `gandalf/` folder exists as a direct skill shape for local use and testing
