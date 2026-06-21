#!/bin/sh
# Sisyphus pre-commit hook (M0 capa anti-olvido)
# Verifica que .sisyphus/progress.json sea consistente antes de cada commit.
# Si una tarea se marca 'done' sin evidence_file commiteado o sin SHA, bloquea.
#
# Instalacion:
#   cp scripts/pre-commit-hook.sh .git/hooks/pre-commit
#   chmod +x .git/hooks/pre-commit
# (En worktrees, instala el hook en el git-common-dir para que aplique a todos.)
#
# Resolver el interprete python es delicado en Windows: el alias de Microsoft
# Store (WindowsApps/python.exe) intercepta 'python' pero no es un interprete
# real. Por eso probamos candidatos ejecutando --version y nos quedamos con el
# primero que funcione. Se puede forzar con: git config sisyphus.python <path>
# o la variable de entorno SISYPHUS_PYTHON.

set -e

_find_python() {
  # 1. Explicito via env o git config.
  if [ -n "$SISYPHUS_PYTHON" ]; then
    echo "$SISYPHUS_PYTHON"; return 0
  fi
  cfg=$(git config sisyphus.python 2>/dev/null || true)
  if [ -n "$cfg" ]; then echo "$cfg"; return 0; fi
  # 2. Probar candidatos ejecutando --version (filtra el stub de WindowsApps).
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
  echo "[pre-commit] No se encontro un interprete python utilizable."
  echo "  Define: git config sisyphus.python 'C:/path/python.exe'"
  echo "  o:      export SISYPHUS_PYTHON=C:/path/python.exe"
  exit 1
}

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
