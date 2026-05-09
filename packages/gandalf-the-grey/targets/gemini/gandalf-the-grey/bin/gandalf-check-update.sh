#!/usr/bin/env bash
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
