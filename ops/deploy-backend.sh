#!/usr/bin/env bash
set -Eeuo pipefail

# Load centralized variables
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ -f "${SCRIPT_DIR}/vars.sh" ]]; then
  . "${SCRIPT_DIR}/vars.sh"
fi

HOST="${HOST:-${VPS_HOST}}"
SSH_USER="${SSH_USER:-root}"
SSH_PORT="${SSH_PORT:-22}"
REMOTE_ROOT="${REMOTE_ROOT:-/opt/myownclone}"
REMOTE_RELEASES_DIR="${REMOTE_ROOT}/releases"
REMOTE_SHARED_DIR="${REMOTE_ROOT}/shared"
RELEASE_ID="${RELEASE_ID:-$(date +%Y%m%d%H%M%S)}"
REMOTE_RELEASE_DIR="${REMOTE_RELEASES_DIR}/${RELEASE_ID}"
REMOTE_CURRENT_LINK="${REMOTE_CURRENT_LINK:-${REMOTE_ROOT}/current}"
LOCAL_REPO="${LOCAL_REPO:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
BACKEND_ENV_FILE="${BACKEND_ENV_FILE:-}"
BASE_SSH_OPTS=(-p "$SSH_PORT" -o StrictHostKeyChecking=strict)

log() {
  printf '[deploy-backend] %s\n' "$*"
}

PREV_RELEASE_LINK="${PREV_RELEASE_LINK:-}"

capture_previous_release() {
  PREV_RELEASE_LINK="$("${SSH_CMD[@]}" "${SSH_USER}@${HOST}" \
    "readlink '${REMOTE_CURRENT_LINK}' 2>/dev/null || true")"
  if [[ -n "$PREV_RELEASE_LINK" ]]; then
    log "Captured previous release: ${PREV_RELEASE_LINK}"
  else
    log "No previous release found (first deploy?)"
  fi
}

rollback_backend() {
  log "ROLLBACK: Restoring previous backend release"
  if [[ -z "$PREV_RELEASE_LINK" ]]; then
    log "ROLLBACK ABORTED: No previous release to restore"
    return 1
  fi
  "${SSH_CMD[@]}" "${SSH_USER}@${HOST}" bash -s -- \
    "$PREV_RELEASE_LINK" "$REMOTE_CURRENT_LINK" <<'ROLLBACK_EOF'
set -Eeuo pipefail
previous_release=$1
current_link=$2
ln -sfn -- "$previous_release" "$current_link"
cd -- "$current_link/ops"
if docker compose version >/dev/null 2>&1; then
  compose=(docker compose)
elif command -v docker-compose >/dev/null 2>&1; then
  compose=(docker-compose)
else
  printf 'No se encontró docker compose ni docker-compose\n' >&2
  exit 1
fi
"${compose[@]}" -f docker-compose.backend.prod.yml down
"${compose[@]}" -f docker-compose.backend.prod.yml up -d --build
"${compose[@]}" -f docker-compose.backend.prod.yml ps
ROLLBACK_EOF
  log "ROLLBACK: Completed - restored ${PREV_RELEASE_LINK}"
}

rollback_on_error() {
  local exit_code=$?
  if [[ $exit_code -ne 0 ]]; then
    log "Deployment failed (exit ${exit_code}) - initiating rollback"
    rollback_backend || true
    exit $exit_code
  fi
}

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || {
    printf 'Falta comando requerido: %s\n' "$1" >&2
    exit 1
  }
}

SSH_BIN="${SSH_BIN:-ssh}"
SSH_CMD=("$SSH_BIN" "${BASE_SSH_OPTS[@]}")
RSYNC_RSH="ssh -p $SSH_PORT -o StrictHostKeyChecking=accept-new"

if [[ "${DEPLOY_BACKEND_ROLLBACK_ONLY:-0}" == "1" ]]; then
  rollback_backend
  exit 0
fi

require_cmd ssh
require_cmd rsync
require_cmd python3
require_cmd git

if [[ ! -f "${LOCAL_REPO}/ops/docker-compose.backend.prod.yml" ]]; then
  printf 'No existe %s\n' "${LOCAL_REPO}/ops/docker-compose.backend.prod.yml" >&2
  exit 1
fi

if [[ -n "$BACKEND_ENV_FILE" && ! -f "$BACKEND_ENV_FILE" ]]; then
  printf 'No existe BACKEND_ENV_FILE=%s\n' "$BACKEND_ENV_FILE" >&2
  exit 1
fi

SOURCE_COMMIT="$(git -C "$LOCAL_REPO" rev-parse HEAD)"
git -C "$LOCAL_REPO" diff --quiet -- api ops .github/workflows
git -C "$LOCAL_REPO" diff --cached --quiet -- api ops .github/workflows
RELEASE_MANIFEST_FILE="$(mktemp)"
cleanup_manifest() {
  rm -f -- "$RELEASE_MANIFEST_FILE"
}
trap cleanup_manifest EXIT
python3 "$LOCAL_REPO/ops/release_manifest.py" --root "$LOCAL_REPO" create \
  --source-commit "$SOURCE_COMMIT" --output "$RELEASE_MANIFEST_FILE"
python3 "$LOCAL_REPO/ops/release_manifest.py" --root "$LOCAL_REPO" verify \
  --manifest "$RELEASE_MANIFEST_FILE"

# Capture previous release for rollback before making any changes
capture_previous_release

# Set trap for rollback on error
trap rollback_on_error ERR

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
  --include '/.github/' \
  --include '/.github/workflows/***' \
  --include '/.dockerignore' \
  --exclude '*' \
  "${LOCAL_REPO}/" "${SSH_USER}@${HOST}:${REMOTE_RELEASE_DIR}/"

RSYNC_RSH="$RSYNC_RSH" rsync -az --chmod=F444 \
  "$RELEASE_MANIFEST_FILE" \
  "${SSH_USER}@${HOST}:${REMOTE_RELEASE_DIR}/release-manifest.json"

"${SSH_CMD[@]}" "${SSH_USER}@${HOST}" bash -s -- \
  "$REMOTE_RELEASE_DIR" <<'VERIFY_EOF'
set -Eeuo pipefail
release_dir=$1
python3 "$release_dir/ops/release_manifest.py" --root "$release_dir" verify \
  --manifest "$release_dir/release-manifest.json" --no-head-check
VERIFY_EOF

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

trap - ERR

log "Deploy backend completado: release ${RELEASE_ID}"

# =============================================================================
# ROLLBACK PROCEDURE (Manual)
# =============================================================================
# If automatic rollback fails or you need to manually rollback:
#
# 1. Identify the previous release directory:
#    ssh root@<host> readlink /opt/myownclone/current
#
# 2. Manually restore the symlink:
#    ssh root@<host> ln -sfn <previous-release-path> /opt/myownclone/current
#
# 3. Restart the containers:
#    ssh root@<host>
#    cd /opt/myownclone/current/ops
#    docker compose -f docker-compose.backend.prod.yml down
#    docker compose -f docker-compose.backend.prod.yml up -d --build
#
# 4. Verify containers are running:
#    ssh root@<host> docker compose -f docker-compose.backend.prod.yml ps
#
# To list available releases:
#    ssh root@<host> ls -la /opt/myownclone/releases/
# =============================================================================
