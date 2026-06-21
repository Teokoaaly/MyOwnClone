#!/bin/sh
# Sisyphus pre-commit hook (M0 capa anti-olvido)
# Verifica que .sisyphus/progress.json sea consistente antes de cada commit.
# Si una tarea se marca 'done' sin evidence_file commiteado o sin SHA, bloquea.
#
# Instalacion:
#   cp scripts/pre-commit-hook.sh .git/hooks/pre-commit
#   chmod +x .git/hooks/pre-commit
# (En worktrees, instala el hook en el git-common-dir para que aplique a todos.)

set -e

PY="${PYTHON:-}"
if [ -z "$PY" ]; then
  command -v python3 >/dev/null 2>&1 && PY=python3 || PY=python
fi

REPO_ROOT=$(git rev-parse --show-toplevel)
PROGRESS="$REPO_ROOT/.sisyphus/progress.json"

# Si no hay progress.json (repo ajeno al plan), dejar pasar.
if [ ! -f "$PROGRESS" ]; then
  exit 0
fi

"$PY" "$REPO_ROOT/scripts/check-plan-progress.py" || {
  echo ""
  echo "[pre-commit] Bloqueado: progreso del plan Sisyphus inconsistente."
  echo "  Arregla .sisyphus/progress.json o usa --no-verify SOLO para commits"
  echo "  ajenos al plan (y documentalo)."
  exit 1
}

exit 0
