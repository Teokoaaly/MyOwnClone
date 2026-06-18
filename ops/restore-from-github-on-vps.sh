#!/usr/bin/env bash
set -Eeuo pipefail

# Restore/deploy MyOwnClone from GitHub while running directly on the VPS.
#
# Usage on VPS:
#   BRANCH=audit/vps-sync-and-docs bash ops/restore-from-github-on-vps.sh
#
# Requirements:
# - Run as root or a user with sudo/systemctl/docker access.
# - Existing production env files in /opt/myownclone/shared:
#   - frontend.env.production
#   - backend.env.production
# - Network access to GitHub and npm registry.

REPO_URL="${REPO_URL:-https://github.com/Teokoaaly/MyOwnClone.git}"
BRANCH="${BRANCH:-audit/vps-sync-and-docs}"
REMOTE_ROOT="${REMOTE_ROOT:-/opt/myownclone}"
RELEASES_DIR="${REMOTE_ROOT}/releases"
SHARED_DIR="${REMOTE_ROOT}/shared"
RELEASE_ID="${RELEASE_ID:-$(date +%Y%m%d%H%M%S)-github-restore}"
RELEASE_DIR="${RELEASES_DIR}/${RELEASE_ID}"
CURRENT_LINK="${REMOTE_ROOT}/current"
FRONTEND_SERVICE="${FRONTEND_SERVICE:-myownclone-frontend}"

log() {
  printf '[restore-vps] %s\n' "$*"
}

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || {
    printf 'Missing required command: %s\n' "$1" >&2
    exit 1
  }
}

require_file() {
  [[ -f "$1" ]] || {
    printf 'Missing required file: %s\n' "$1" >&2
    exit 1
  }
}

require_cmd git
require_cmd tar
require_cmd node
require_cmd npm
require_cmd python3
require_cmd systemctl
require_cmd docker

require_file "${SHARED_DIR}/frontend.env.production"
require_file "${SHARED_DIR}/backend.env.production"

log "Preparing release ${RELEASE_DIR} from ${REPO_URL}#${BRANCH}"
mkdir -p "${RELEASES_DIR}" "${SHARED_DIR}" "${RELEASE_DIR}"

TMP_REPO="$(mktemp -d)"
trap 'rm -rf "${TMP_REPO}"' EXIT

git -C "${TMP_REPO}" init -q
git -C "${TMP_REPO}" remote add origin "${REPO_URL}"
git -C "${TMP_REPO}" fetch --depth=1 origin "${BRANCH}"
git -C "${TMP_REPO}" archive FETCH_HEAD | tar -x -C "${RELEASE_DIR}"

log "Preparing frontend .env.production"
python3 - <<PY
from pathlib import Path

source = Path("${SHARED_DIR}/frontend.env.production")
target = Path("${RELEASE_DIR}/MyOwnClone/.env.production")
lines = []
for line in source.read_text().splitlines():
    if not line or line.lstrip().startswith("#") or "=" not in line:
        lines.append(line)
        continue
    key, value = line.split("=", 1)
    # Keep bcrypt/platform-admin env only in systemd EnvironmentFile.
    if key in {"PLATFORM_ADMIN_EMAIL", "PLATFORM_ADMIN_PASSWORD_HASH"}:
        continue
    lines.append(f"{key}={value.replace('$', r'\$')}")
target.write_text("\\n".join(lines) + "\\n")
PY

log "Setting permissions"
id -u myownclone >/dev/null 2>&1 || useradd --system --create-home --shell /bin/bash myownclone
chown -R myownclone:myownclone "${RELEASE_DIR}" "${SHARED_DIR}"
chmod 0600 "${RELEASE_DIR}/MyOwnClone/.env.production"

log "Installing frontend dependencies and building"
cd "${RELEASE_DIR}/MyOwnClone"
sudo -u myownclone npm install --legacy-peer-deps --no-audit --no-fund
sudo -u myownclone npm run build

log "Activating release"
ln -sfn "${RELEASE_DIR}" "${CURRENT_LINK}"
install -m 0644 "${RELEASE_DIR}/ops/myownclone-frontend.service" /etc/systemd/system/myownclone-frontend.service
systemctl daemon-reload
systemctl enable --now "${FRONTEND_SERVICE}.service"
systemctl restart "${FRONTEND_SERVICE}.service"

log "Restoring backend compose from release"
cd "${CURRENT_LINK}/ops"
cp "${SHARED_DIR}/backend.env.production" ./backend.env.production
chmod 0600 ./backend.env.production
set -a
. ./backend.env.production
set +a

log "Preparing Redis TLS certificates"
REDIS_TLS_SHARED="${SHARED_DIR}/redis-tls"
REDIS_TLS_RELEASE="${CURRENT_LINK}/ops/tls/redis"
mkdir -p "${REDIS_TLS_SHARED}" "${REDIS_TLS_RELEASE}"
if [[ ! -s "${REDIS_TLS_SHARED}/ca.crt" || ! -s "${REDIS_TLS_SHARED}/redis.crt" || ! -s "${REDIS_TLS_SHARED}/redis.key" ]]; then
  openssl genrsa -out "${REDIS_TLS_SHARED}/ca.key" 4096 >/dev/null 2>&1
  openssl req -x509 -new -nodes -key "${REDIS_TLS_SHARED}/ca.key" -sha256 -days 3650 -subj '/CN=myownclone-redis-ca' -out "${REDIS_TLS_SHARED}/ca.crt" >/dev/null 2>&1
  openssl genrsa -out "${REDIS_TLS_SHARED}/redis.key" 2048 >/dev/null 2>&1
  openssl req -new -key "${REDIS_TLS_SHARED}/redis.key" -subj '/CN=localhost' -out "${REDIS_TLS_SHARED}/redis.csr" >/dev/null 2>&1
  printf 'subjectAltName=DNS:localhost,IP:127.0.0.1\n' > "${REDIS_TLS_SHARED}/redis.ext"
  openssl x509 -req -in "${REDIS_TLS_SHARED}/redis.csr" -CA "${REDIS_TLS_SHARED}/ca.crt" -CAkey "${REDIS_TLS_SHARED}/ca.key" -CAcreateserial -out "${REDIS_TLS_SHARED}/redis.crt" -days 3650 -sha256 -extfile "${REDIS_TLS_SHARED}/redis.ext" >/dev/null 2>&1
  chmod 0600 "${REDIS_TLS_SHARED}"/*.key
  chmod 0644 "${REDIS_TLS_SHARED}"/*.crt
fi
cp "${REDIS_TLS_SHARED}/ca.crt" "${REDIS_TLS_SHARED}/redis.crt" "${REDIS_TLS_SHARED}/redis.key" "${REDIS_TLS_RELEASE}/"
chmod 0600 "${REDIS_TLS_RELEASE}/redis.key"
chmod 0644 "${REDIS_TLS_RELEASE}/ca.crt" "${REDIS_TLS_RELEASE}/redis.crt"

if docker compose version >/dev/null 2>&1; then
  COMPOSE_CMD=(docker compose)
elif command -v docker-compose >/dev/null 2>&1; then
  COMPOSE_CMD=(docker-compose)
else
  echo 'Neither docker compose nor docker-compose is installed.' >&2
  exit 1
fi

COMPOSE_BAKE=true "${COMPOSE_CMD[@]}" -f docker-compose.backend.prod.yml up -d --build --remove-orphans

log "Checking services"
systemctl --no-pager --full status "${FRONTEND_SERVICE}.service" | sed -n '1,16p'
"${COMPOSE_CMD[@]}" -f docker-compose.backend.prod.yml ps

log "Smoke checks"
curl -fsS http://127.0.0.1:5001/healthz >/dev/null
curl -fsS http://127.0.0.1:5001/readyz >/dev/null
curl -fsS http://127.0.0.1:3000/ >/dev/null

log "Restore completed"
log "Active release: ${RELEASE_DIR}"
log "Commit: $(git -C "${TMP_REPO}" rev-parse --short FETCH_HEAD)"
