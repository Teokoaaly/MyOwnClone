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
BACKEND_ENV_FILE="${BACKEND_ENV_FILE:-}"
BASE_SSH_OPTS=(-p "$SSH_PORT" -o StrictHostKeyChecking=accept-new)

log() {
  printf '[deploy-backend] %s\n' "$*"
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

if [[ ! -f "${LOCAL_REPO}/ops/docker-compose.backend.prod.yml" ]]; then
  printf 'No existe %s\n' "${LOCAL_REPO}/ops/docker-compose.backend.prod.yml" >&2
  exit 1
fi

if [[ -n "$BACKEND_ENV_FILE" && ! -f "$BACKEND_ENV_FILE" ]]; then
  printf 'No existe BACKEND_ENV_FILE=%s\n' "$BACKEND_ENV_FILE" >&2
  exit 1
fi

log "Preparando directorios remotos en ${SSH_USER}@${HOST}:${REMOTE_ROOT}"
"${SSH_CMD[@]}" "${SSH_USER}@${HOST}" \
  "mkdir -p '${REMOTE_RELEASES_DIR}' '${REMOTE_SHARED_DIR}'"

if [[ -n "$BACKEND_ENV_FILE" ]]; then
  log "Subiendo backend env file"
  RSYNC_RSH="$RSYNC_RSH" rsync -az --chmod=F600 \
    "$BACKEND_ENV_FILE" \
    "${SSH_USER}@${HOST}:${REMOTE_SHARED_DIR}/backend.env.production"
else
  log "No se subió env local; se reutiliza ${REMOTE_SHARED_DIR}/backend.env.production"
fi

log "Sincronizando código backend y artefactos ops hacia ${REMOTE_RELEASE_DIR}"
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
  --exclude 'instance/*' \
  --include '/api/***' \
  --include '/ops/***' \
  --include '/.dockerignore' \
  --exclude '*' \
  "${LOCAL_REPO}/" "${SSH_USER}@${HOST}:${REMOTE_RELEASE_DIR}/"

log "Activando release ${RELEASE_ID} y levantando backend Docker"
"${SSH_CMD[@]}" "${SSH_USER}@${HOST}" bash <<EOF
set -Eeuo pipefail
ln -sfn '${REMOTE_RELEASE_DIR}' '${REMOTE_CURRENT_LINK}'
cd '${REMOTE_CURRENT_LINK}/ops'
cp '${REMOTE_SHARED_DIR}/backend.env.production' './backend.env.production'
# Auto-load secrets so \${DB_PASSWORD} etc. resolve in the compose file
set -a
. './backend.env.production'
set +a
if docker compose version >/dev/null 2>&1; then
  COMPOSE_CMD='docker compose'
elif command -v docker-compose >/dev/null 2>&1; then
  COMPOSE_CMD='docker-compose'
else
  echo 'No se encontró docker compose ni docker-compose en el host remoto' >&2
  exit 1
fi
eval "\${COMPOSE_CMD} -f docker-compose.backend.prod.yml pull --ignore-pull-failures"
COMPOSE_BAKE=true eval "\${COMPOSE_CMD} -f docker-compose.backend.prod.yml up -d --build --remove-orphans"
eval "\${COMPOSE_CMD} -f docker-compose.backend.prod.yml ps"
for attempt in 1 2 3 4 5 6 7 8 9 10; do
  if curl -fsS http://127.0.0.1:5001/console/api/ >/dev/null; then
    echo 'Backend respondió OK en /console/api/'
    exit 0
  fi
  sleep 3
done
printf 'Backend no respondió sano tras el despliegue\n' >&2
exit 1
EOF

log "Deploy backend completado: release ${RELEASE_ID}"
