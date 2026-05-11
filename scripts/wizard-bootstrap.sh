#!/bin/bash
# Wizard Bootstrap: Gandalf Context Loader

echo "=== WIZARD BOOTSTRAP ==="
echo "Branch: $(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo 'not a git repo')"
echo "Last Quest: $(git log -1 --pretty=format:'%s' 2>/dev/null || echo 'no commits')"

echo ""
echo "--- Current Harness State ---"
[ -d .git ] && echo "Git: ✓" || echo "Git: ✗"
[ -f GEMINI.md ] && echo "Mandates: ✓" || echo "Mandates: ✗"
[ -f QUEST_PROGRESS.md ] && echo "Progress: ✓" || echo "Progress: ✗"
[ -f docs/contexto.md ] && echo "Context: ✓" || echo "Context: ✗"

echo ""
echo "--- Recent Decisions ---"
grep "ADR-" QUEST_PROGRESS.md | tail -n 5

echo ""
echo "--- Next Actions ---"
grep -A 5 "## Next Steps" QUEST_PROGRESS.md | grep "\- \[ \]"

echo "=== BOOTSTRAP COMPLETE ==="
