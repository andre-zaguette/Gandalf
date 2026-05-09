# Gandalf

Gandalf is split into two layers.

- `gandalf-the-grey`: plugin and method package
- `gandalf-the-white`: agent that consumes the Grey package

This lets teams choose:

- plugin only
- full agent orchestration

## Design

### Gandalf the Grey

Grey is source of method and behavior:

- persona
- voice
- patterns
- routing
- questioning policy
- multi-target packaging for Codex, Claude, and Gemini

### Gandalf the White

White is the agent layer:

- classify task
- choose path
- ask sharp questions first
- decide backend, frontend, or cross-repo ownership
- consume Grey instead of redefining method

## Repository layout

- `packages/gandalf-the-grey/`
- `agents/gandalf-the-white/`
- `scripts/build-gandalf.py`

## Build

```bash
python3 scripts/build-gandalf.py
```

Edit Grey core first. Rebuild after.
