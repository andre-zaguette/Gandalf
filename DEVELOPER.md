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

## Installing Grey (plugin)

```bash
claude plugin marketplace add packages/gandalf-the-grey/targets/claude
claude plugin install gandalf-the-grey
```

Grey is then available as `$gandalf-the-grey` in any Claude Code session.

## Installing White (agent)

Copy `agents/gandalf-the-white/CLAUDE.md` into the root of the project you want to orchestrate:

```bash
cp agents/gandalf-the-white/CLAUDE.md /path/to/your-project/CLAUDE.md
```

Claude Code auto-discovers CLAUDE.md on startup. White will invoke `$gandalf-the-grey` from the installed plugin.

Or for a one-off session without copying:

```bash
claude --append-system-prompt "$(cat agents/gandalf-the-white/AGENT.md)"
```

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
