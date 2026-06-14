#!/usr/bin/env bash
set -Eeuo pipefail

HOST="${HOST:-100.99.222.101}"
SSH_USER="${SSH_USER:-root}"
SSH_PORT="${SSH_PORT:-22}"
SSH_PASSWORD="${SSH_PASSWORD:-}"
REMOTE_ROOT="${REMOTE_ROOT:-/opt/myownclone}"
REMOTE_RELEASES_DIR="${REMOTE_ROOT}/releases"
REMOTE_SHARED_DIR="${REMOTE_ROOT}/shared"
RELEASE_ID="${RELEASE_ID:-$(date +%Y%m%d%H%M%S)}"
REMOTE_RELEASE_DIR="${REMOTE_RELEASES_DIR}/${RELEASE_ID}"
REMOTE_CURRENT_LINK="${REMOTE_ROOT}/current"
LOCAL_REPO="${LOCAL_REPO:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
FRONTEND_ENV_FILE="${FRONTEND_ENV_FILE:-}"
BASE_SSH_OPTS=(-p "$SSH_PORT" -o StrictHostKeyChecking=accept-new)

log() {
  printf '[deploy-frontend] %s\n' "$*"
}

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || {
    printf 'Falta comando requerido: %s\n' "$1" >&2
    exit 1
  }
}

if [[ -n "$SSH_PASSWORD" ]]; then
  require_cmd sshpass
  SSH_CMD=(sshpass -p "$SSH_PASSWORD" ssh "${BASE_SSH_OPTS[@]}")
  RSYNC_RSH="sshpass -p '$SSH_PASSWORD' ssh -p $SSH_PORT -o StrictHostKeyChecking=accept-new"
else
  SSH_CMD=(ssh "${BASE_SSH_OPTS[@]}")
  RSYNC_RSH="ssh -p $SSH_PORT -o StrictHostKeyChecking=accept-new"
fi

require_cmd ssh
require_cmd rsync

for file in \
  "${LOCAL_REPO}/MyOwnClone/package.json" \
  "${LOCAL_REPO}/ops/myownclone-frontend.service"; do
  [[ -f "$file" ]] || {
    printf 'No existe %s\n' "$file" >&2
    exit 1
  }
done

if [[ -n "$FRONTEND_ENV_FILE" && ! -f "$FRONTEND_ENV_FILE" ]]; then
  printf 'No existe FRONTEND_ENV_FILE=%s\n' "$FRONTEND_ENV_FILE" >&2
  exit 1
fi

log "Preparando directorios remotos en ${SSH_USER}@${HOST}:${REMOTE_ROOT}"
"${SSH_CMD[@]}" "${SSH_USER}@${HOST}" \
  "id -u myownclone >/dev/null 2>&1 || useradd --system --create-home --shell /bin/bash myownclone; mkdir -p '${REMOTE_RELEASES_DIR}' '${REMOTE_SHARED_DIR}'"

if [[ -n "$FRONTEND_ENV_FILE" ]]; then
  log "Subiendo frontend env file"
  RSYNC_RSH="$RSYNC_RSH" rsync -az --chmod=F600 \
    "$FRONTEND_ENV_FILE" \
    "${SSH_USER}@${HOST}:${REMOTE_SHARED_DIR}/frontend.env.production"
else
  log "No se subió env local; se reutiliza ${REMOTE_SHARED_DIR}/frontend.env.production"
fi

log "Sincronizando frontend y artefactos ops hacia ${REMOTE_RELEASE_DIR}"
"${SSH_CMD[@]}" "${SSH_USER}@${HOST}" "mkdir -p '${REMOTE_RELEASE_DIR}'"
RSYNC_RSH="$RSYNC_RSH" rsync -az --delete \
  --exclude '.git' \
  --exclude '.venv' \
  --exclude '.pytest_cache' \
  --exclude '__pycache__' \
  --exclude '.mypy_cache' \
  --exclude '.ruff_cache' \
  --exclude '.next' \
  --exclude 'node_modules' \
  --exclude '.env' \
  --exclude '.env.local' \
  --exclude '.env.*.local' \
  --include '/MyOwnClone/***' \
  --include '/ops/***' \
  --exclude '*' \
  "${LOCAL_REPO}/" "${SSH_USER}@${HOST}:${REMOTE_RELEASE_DIR}/"

log "Instalando dependencias, build y servicio systemd"
# Pre-expand local vars so heredoc can stay single-quoted (no remote expansion)
_REMOTE_SHARED_DIR="${REMOTE_SHARED_DIR}"
_REMOTE_RELEASE_DIR="${REMOTE_RELEASE_DIR}"
_REMOTE_CURRENT_LINK="${REMOTE_ROOT}/current"
"${SSH_CMD[@]}" "${SSH_USER}@${HOST}" bash <<EOF
set -Eeuo pipefail
ln -sfn '${_REMOTE_RELEASE_DIR}' '${_REMOTE_CURRENT_LINK}'
chown -R myownclone:myownclone '${_REMOTE_RELEASE_DIR}' '${_REMOTE_SHARED_DIR}'
cd '${_REMOTE_CURRENT_LINK}/MyOwnClone'
command -v node >/dev/null 2>&1 || { echo 'Node.js no está instalado en el VPS' >&2; exit 1; }
command -v npm >/dev/null 2>&1 || { echo 'npm no está instalado en el VPS' >&2; exit 1; }
sudo -u myownclone npm install --legacy-peer-deps --no-audit --no-fund
# Keep Next.js' local production env readable by the service user. Escape dollar
# signs for Next's dotenv expansion while systemd keeps the raw shared env.
python3 - <<'PY'
from pathlib import Path

source = Path('${_REMOTE_SHARED_DIR}/frontend.env.production')
target = Path('./.env.production')
lines = []
for line in source.read_text().splitlines():
    if not line or line.lstrip().startswith('#') or '=' not in line:
        lines.append(line)
        continue
    key, value = line.split('=', 1)
    lines.append(f"{key}={value.replace('$', r'\$')}")
target.write_text('\n'.join(lines) + '\n')
PY
chown myownclone:myownclone './.env.production'
chmod 0600 './.env.production'
sudo -u myownclone npm run build
install -m 0644 '${_REMOTE_CURRENT_LINK}/ops/myownclone-frontend.service' /etc/systemd/system/myownclone-frontend.service
systemctl daemon-reload
systemctl enable --now myownclone-frontend.service
systemctl restart myownclone-frontend.service
systemctl --no-pager --full status myownclone-frontend.service
EOF

log "Esperando respuesta del frontend en http://127.0.0.1:3000/"
"${SSH_CMD[@]}" "${SSH_USER}@${HOST}" bash <<'EOF'
set -Eeuo pipefail
for attempt in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20; do
  if curl -fsS http://127.0.0.1:3000/ >/dev/null; then
    echo 'Frontend respondió OK en /'
    exit 0
  fi
  sleep 3
done
printf 'Frontend no respondió sano tras el despliegue\n' >&2
exit 1
EOF

log "Deploy frontend completado: release ${RELEASE_ID}"
