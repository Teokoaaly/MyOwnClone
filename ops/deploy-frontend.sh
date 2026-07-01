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
REMOTE_CURRENT_LINK="${REMOTE_ROOT}/current"
LOCAL_REPO="${LOCAL_REPO:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
FRONTEND_ENV_FILE="${FRONTEND_ENV_FILE:-}"
BASE_SSH_OPTS=(-p "$SSH_PORT" -o StrictHostKeyChecking=strict)

log() {
  printf '[deploy-frontend] %s\n' "$*"
}

# Rollback state
PREV_RELEASE_LINK=""

capture_previous_release() {
  PREV_RELEASE_LINK="$("${SSH_CMD[@]}" "${SSH_USER}@${HOST}" \
    "readlink '${REMOTE_CURRENT_LINK}' 2>/dev/null || true")"
  if [[ -n "$PREV_RELEASE_LINK" ]]; then
    log "Captured previous release: ${PREV_RELEASE_LINK}"
  else
    log "No previous release found (first deploy?)"
  fi
}

rollback_frontend() {
  log "ROLLBACK: Restoring previous frontend release"
  if [[ -z "$PREV_RELEASE_LINK" ]]; then
    log "ROLLBACK ABORTED: No previous release to restore"
    return 1
  fi
  "${SSH_CMD[@]}" "${SSH_USER}@${HOST}" bash <<'ROLLBACK_EOF'
set -Eeuo pipefail
ln -sfn '${PREV_RELEASE_LINK}' '${REMOTE_CURRENT_LINK}'
systemctl restart myownclone-frontend.service
systemctl --no-pager --full status myownclone-frontend.service
ROLLBACK_EOF
  log "ROLLBACK: Completed - restored ${PREV_RELEASE_LINK}"
}

rollback_on_error() {
  local exit_code=$?
  if [[ $exit_code -ne 0 ]]; then
    log "Deployment failed (exit ${exit_code}) - initiating rollback"
    rollback_frontend || true
    exit $exit_code
  fi
}

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || {
    printf 'Falta comando requerido: %s\n' "$1" >&2
    exit 1
  }
}

SSH_CMD=(ssh "${BASE_SSH_OPTS[@]}")
RSYNC_RSH="ssh -p $SSH_PORT -o StrictHostKeyChecking=accept-new"

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

# Capture previous release for rollback before making any changes
capture_previous_release

# Set trap for rollback on error
trap rollback_on_error ERR

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
sudo -u myownclone npm ci --legacy-peer-deps --no-audit --no-fund
# Load env from shared, export only valid KEY=VAL lines (skip comments/blanks)
set -a
. '${_REMOTE_SHARED_DIR}/frontend.env.production'
set +a
sudo -u myownclone env npm run build
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

# Remove trap on success
trap - ERR

log "Deploy frontend completado: release ${RELEASE_ID}"

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
# 3. Restart the service:
#    ssh root@<host> systemctl restart myownclone-frontend.service
#
# 4. Verify the service is running:
#    ssh root@<host> systemctl status myownclone-frontend.service
#
# To list available releases:
#    ssh root@<host> ls -la /opt/myownclone/releases/
# =============================================================================
