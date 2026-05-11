# Developer Guide

## Rule

`packages/gandalf-the-grey/core/` is source of truth for the plugin layer.

Generated artifacts live under:

- `packages/gandalf-the-grey/plugin/`
- `packages/gandalf-the-grey/targets/`

`agents/gandalf-the-white/` consumes Grey. It should not duplicate Grey method unless there is a strong reason.

## Workflow

1. Edit Grey core files
2. Run:

```bash
python3 scripts/build-gandalf.py
```

3. Review generated plugin and targets
4. Review White agent instructions
5. Commit when core, generated outputs, and agent stay aligned

## Responsibility split

### Grey

- method
- persona
- patterns
- routing
- packaging

### White

- orchestration
- questioning
- repo ownership decisions
- workflow leadership
- handoff decisions
