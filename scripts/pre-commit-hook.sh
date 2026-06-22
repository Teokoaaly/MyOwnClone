#!/bin/sh
# Sisyphus pre-commit hook

set -e

_find_python() {
  if [ -n "$SISYPHUS_PYTHON" ]; then
    echo "$SISYPHUS_PYTHON"; return 0
  fi
  cfg=$(git config sisyphus.python 2>/dev/null || true)
  if [ -n "$cfg" ]; then
    echo "$cfg"; return 0
  fi
  for cand in python3 python py python.exe py.exe; do
    if command -v "$cand" >/dev/null 2>&1; then
      if "$cand" --version >/dev/null 2>&1; then
        echo "$cand"; return 0
      fi
    fi
  done
  return 1
}

PY=$(_find_python) || {
  echo "[pre-commit] No usable python interpreter found."
  echo "  Set: git config sisyphus.python 'C:/path/python.exe'"
  echo "  or:  export SISYPHUS_PYTHON=C:/path/python.exe"
  exit 1
}

REPO_ROOT=$(git rev-parse --show-toplevel)
PROGRESS="$REPO_ROOT/.sisyphus/progress.json"

if [ ! -f "$PROGRESS" ]; then
  exit 0
fi

"$PY" "$REPO_ROOT/scripts/check-plan-progress.py" || {
  echo ""
  echo "[pre-commit] Blocked: inconsistent Sisyphus progress."
  echo "  Fix .sisyphus/progress.json or use --no-verify only for"
  echo "  unrelated commits, and document why."
  exit 1
}

exit 0
