#!/bin/bash
# The Gates of Argonath: Git Pre-commit Hook

echo "🛡️ The Gates of Argonath: Inspecting the Caravan..."

# 1. Check Progress Log
if [ ! -f QUEST_PROGRESS.md ]; then
    echo "❌ ERROR: QUEST_PROGRESS.md is missing. No code shall pass without a record."
    exit 1
fi

# 2. Check if Progress was updated in this commit (staged changes)
if ! git diff --cached --name-only | grep -q "QUEST_PROGRESS.md"; then
    echo "⚠️ WARNING: QUEST_PROGRESS.md not staged. Did you record this quest's steps?"
    # Optional: exit 1 to be strict
fi

# 3. Check Archive freshness (if docs/archive exists)
if [ -d docs/archive ]; then
    # Simple check if any code changed but archive didn't
    CODE_CHANGED=$(git diff --cached --name-only | grep -E "\.(py|js|ts|go|java)$")
    ARCHIVE_CHANGED=$(git diff --cached --name-only | grep "docs/archive/")
    
    if [ -n "$CODE_CHANGED" ] && [ -z "$ARCHIVE_CHANGED" ]; then
        echo "📜 The Palantír Map may be out of date. Consider running wizard-archivist.py."
    fi
fi

echo "✅ The Gates are open. Pass, traveler."
exit 0
