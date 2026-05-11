#!/bin/bash
# Wizard Bootstrap: [PROJECT_NAME] Context Loader

echo "=== WIZARD BOOTSTRAP ==="
echo "Branch: $(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo 'not a git repo')"
echo "Last Quest: $(git log -1 --pretty=format:'%s' 2>/dev/null || echo 'no commits')"

echo ""
echo "--- Current Harness State ---"
[ -d .git ] && echo "Git: ✓" || echo "Git: ✗"
[ -f WIZARD.md ] || [ -f GEMINI.md ] && echo "Mandates: ✓" || echo "Mandates: ✗"
[ -f QUEST_PROGRESS.md ] && echo "Progress: ✓" || echo "Progress: ✗"
[ -f docs/contexto.md ] && echo "Context: ✓" || echo "Context: ✗"
[ -f docs/archive/PALANTIR.md ] && echo "Archive: ✓" || echo "Archive: ✗ (Run wizard-archivist.py)"

echo ""
echo "--- Current Archive Pillars ---"
grep -A 5 "Citadel Pillars" docs/archive/PALANTIR.md 2>/dev/null | grep "\- "

echo ""
echo "--- Recent Decisions ---"
grep "ADR-" QUEST_PROGRESS.md 2>/dev/null | tail -n 5

echo ""
echo "--- Next Actions ---"
grep -A 5 "## Next Steps" QUEST_PROGRESS.md 2>/dev/null | grep "\- \[ \]"

echo "=== BOOTSTRAP COMPLETE ==="
