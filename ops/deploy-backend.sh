#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ -z "${HOST:-}" && -f "${SCRIPT_DIR}/vars.sh" ]]; then
  . "${SCRIPT_DIR}/vars.sh"
fi

HOST="${HOST:-${VPS_HOST}}"
SSH_USER="${SSH_USER:-root}"
SSH_PORT="${SSH_PORT:-22}"
REMOTE_ROOT="${REMOTE_ROOT:-/opt/myownclone}"
REMOTE_BACKEND_RELEASES_DIR="${REMOTE_ROOT}/backend-releases"
REMOTE_SHARED_DIR="${REMOTE_SHARED_DIR:-${REMOTE_ROOT}/shared}"
REMOTE_BACKEND_CURRENT_LINK="${REMOTE_ROOT}/backend-current"
RELEASE_ID="${RELEASE_ID:-$(date +%Y%m%d%H%M%S)}"
REMOTE_RELEASE_DIR="${REMOTE_BACKEND_RELEASES_DIR}/${RELEASE_ID}"
LOCAL_REPO="${LOCAL_REPO:-$(cd "${SCRIPT_DIR}/.." && pwd)}"
BACKEND_ENV_FILE="${BACKEND_ENV_FILE:-}"
PREV_RELEASE_LINK="${PREV_RELEASE_LINK:-}"
ACTIVATION_STARTED=0
SSH_BIN="${SSH_BIN:-ssh}"
SSH_CMD=("$SSH_BIN" -p "$SSH_PORT" -o BatchMode=yes -o StrictHostKeyChecking=strict)
RSYNC_RSH="ssh -p $SSH_PORT -o BatchMode=yes -o StrictHostKeyChecking=strict"

log() {
  printf '[deploy-backend] %s\n' "$*"
}

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || {
    printf 'Missing required command: %s\n' "$1" >&2
    exit 1
  }
}

capture_previous_release() {
  PREV_RELEASE_LINK="$("${SSH_CMD[@]}" "${SSH_USER}@${HOST}" bash -s -- \
    "$REMOTE_BACKEND_CURRENT_LINK" "$REMOTE_ROOT/current" <<'CAPTURE_EOF'
set -Eeuo pipefail
backend_link=$1
legacy_link=$2
if [[ -L "$backend_link" ]]; then
  readlink -f -- "$backend_link"
else
  readlink -f -- "$legacy_link"
fi
CAPTURE_EOF
)"
  [[ -n "$PREV_RELEASE_LINK" ]] || {
    printf 'No previous backend release is available for rollback\n' >&2
    exit 1
  }
  log "Captured previous backend release: ${PREV_RELEASE_LINK}"
}

rollback_backend() {
  [[ -n "$PREV_RELEASE_LINK" ]] || return 1
  log "ROLLBACK: restoring previous API and worker release"
  "${SSH_CMD[@]}" "${SSH_USER}@${HOST}" bash -s -- \
    "$PREV_RELEASE_LINK" "$REMOTE_BACKEND_CURRENT_LINK" "$REMOTE_SHARED_DIR" <<'ROLLBACK_EOF'
set -Eeuo pipefail
previous_release=$1
backend_link=$2
shared_dir=$3
ln -sfn -- "$previous_release" "$backend_link"
cp "$shared_dir/backend.env.production" "$previous_release/ops/backend.env.production"
cd -- "$previous_release/ops"
set -a
. ./backend.env.production
set +a
docker compose --project-name ops -f docker-compose.backend.prod.yml \
  up -d --build --no-deps api api_worker
for attempt in {1..20}; do
  curl -fsS http://127.0.0.1:5001/readyz >/dev/null && exit 0
  sleep 3
done
exit 1
ROLLBACK_EOF
  log "ROLLBACK: previous API and worker are healthy"
}

rollback_on_error() {
  exit_code=$?
  if [[ "$ACTIVATION_STARTED" -eq 1 ]]; then
    rollback_backend || true
  fi
  exit "$exit_code"
}

for command in ssh rsync python3 git; do
  require_cmd "$command"
done

if [[ "${DEPLOY_BACKEND_ROLLBACK_ONLY:-0}" == "1" ]]; then
  rollback_backend
  exit 0
fi

[[ -f "${LOCAL_REPO}/ops/docker-compose.backend.prod.yml" ]]
[[ -f "${LOCAL_REPO}/ops/docker-compose.schema-migrator.yml" ]]
[[ -z "$BACKEND_ENV_FILE" || -f "$BACKEND_ENV_FILE" ]]
git -C "$LOCAL_REPO" diff --quiet -- api ops .github/workflows MyOwnClone/drizzle MyOwnClone/drizzle.config.ts MyOwnClone/package.json MyOwnClone/package-lock.json MyOwnClone/src/lib/db/schema tests
git -C "$LOCAL_REPO" diff --cached --quiet -- api ops .github/workflows MyOwnClone/drizzle MyOwnClone/drizzle.config.ts MyOwnClone/package.json MyOwnClone/package-lock.json MyOwnClone/src/lib/db/schema tests
if [[ -n "$(git -C "$LOCAL_REPO" status --porcelain -- api ops .github/workflows MyOwnClone/drizzle MyOwnClone/drizzle.config.ts MyOwnClone/package.json MyOwnClone/package-lock.json MyOwnClone/src/lib/db/schema tests)" ]]; then
  printf 'Release inputs must not contain untracked files or local changes\n' >&2
  exit 1
fi
bash "$LOCAL_REPO/ops/scan_tracked_secrets.sh" "$LOCAL_REPO"

SOURCE_COMMIT="$(git -C "$LOCAL_REPO" rev-parse HEAD)"
RELEASE_MANIFEST_FILE="$(mktemp)"
cleanup_manifest() {
  rm -f -- "$RELEASE_MANIFEST_FILE"
}
trap cleanup_manifest EXIT
python3 "$LOCAL_REPO/ops/release_manifest.py" --root "$LOCAL_REPO" create \
  --source-commit "$SOURCE_COMMIT" --output "$RELEASE_MANIFEST_FILE"
python3 "$LOCAL_REPO/ops/release_manifest.py" --root "$LOCAL_REPO" verify \
  --manifest "$RELEASE_MANIFEST_FILE"

capture_previous_release
trap rollback_on_error ERR

"${SSH_CMD[@]}" "${SSH_USER}@${HOST}" \
  "mkdir -p '${REMOTE_BACKEND_RELEASES_DIR}' '${REMOTE_SHARED_DIR}' '${REMOTE_RELEASE_DIR}'"

if [[ -n "$BACKEND_ENV_FILE" ]]; then
  RSYNC_RSH="$RSYNC_RSH" rsync -az --chmod=F600 "$BACKEND_ENV_FILE" \
    "${SSH_USER}@${HOST}:${REMOTE_SHARED_DIR}/backend.env.production"
fi

RSYNC_RSH="$RSYNC_RSH" rsync -az --delete \
  --exclude '.git' --exclude '.venv' --exclude '.pytest_cache' \
  --exclude '__pycache__' --exclude '.ruff_cache' --exclude '.env*' \
  --include '/api/***' --include '/ops/***' \
  --include '/.github/' --include '/.github/workflows/***' \
  --include '/MyOwnClone/' --include '/MyOwnClone/drizzle/***' \
  --include '/MyOwnClone/drizzle.config.ts' --include '/MyOwnClone/package.json' \
  --include '/MyOwnClone/package-lock.json' --include '/MyOwnClone/src/' \
  --include '/MyOwnClone/src/lib/' --include '/MyOwnClone/src/lib/db/' \
  --include '/MyOwnClone/src/lib/db/schema/***' \
  --include '/.dockerignore' --exclude '*' \
  "${LOCAL_REPO}/" "${SSH_USER}@${HOST}:${REMOTE_RELEASE_DIR}/"
RSYNC_RSH="$RSYNC_RSH" rsync -az --chmod=F444 "$RELEASE_MANIFEST_FILE" \
  "${SSH_USER}@${HOST}:${REMOTE_RELEASE_DIR}/release-manifest.json"

"${SSH_CMD[@]}" "${SSH_USER}@${HOST}" bash -s -- \
  "$REMOTE_RELEASE_DIR" "$REMOTE_SHARED_DIR" <<'PREFLIGHT_EOF'
set -Eeuo pipefail
release_dir=$1
shared_dir=$2
python3 "$release_dir/ops/release_manifest.py" --root "$release_dir" verify \
  --manifest "$release_dir/release-manifest.json" --no-head-check
[[ -s "$shared_dir/backend.env.production" ]]
backup_file="$(/bin/bash "$release_dir/ops/backup_postgres.sh" 14 | tail -n 1)"
/bin/bash "$release_dir/ops/verify_postgres_backup.sh" "$backup_file"
PREFLIGHT_EOF

ACTIVATION_STARTED=1
"${SSH_CMD[@]}" "${SSH_USER}@${HOST}" bash -s -- \
  "$REMOTE_RELEASE_DIR" "$REMOTE_BACKEND_CURRENT_LINK" "$REMOTE_SHARED_DIR" <<'ACTIVATE_EOF'
set -Eeuo pipefail
release_dir=$1
backend_link=$2
shared_dir=$3
cp "$shared_dir/backend.env.production" "$release_dir/ops/backend.env.production"
cd -- "$release_dir/ops"
set -a
. ./backend.env.production
set +a
# Ensure the `myownclone_app` role can create the `drizzle` bookkeeping
# schema before invoking the schema_migrator service. Idempotent.
bash "$release_dir/ops/bootstrap-drizzle-migrator.sh"
docker compose --project-name ops -f docker-compose.schema-migrator.yml \
  run --rm --no-deps schema_migrator
docker compose --project-name ops -f docker-compose.backend.prod.yml build api api_worker
docker compose --project-name ops -f docker-compose.backend.prod.yml \
  run --rm --no-deps api flask --app api.app_factory db --directory /app/api/migrations upgrade
docker compose --project-name ops -f docker-compose.backend.prod.yml \
  run --rm --no-deps api flask --app api.app_factory db --directory /app/api/migrations current
ln -sfn -- "$release_dir" "$backend_link"
docker compose --project-name ops -f docker-compose.backend.prod.yml \
  up -d --build --no-deps api api_worker
for attempt in {1..20}; do
  curl -fsS http://127.0.0.1:5001/readyz >/dev/null && exit 0
  sleep 3
done
exit 1
ACTIVATE_EOF

ACTIVATION_STARTED=0
trap - ERR
log "Backend deployment completed: ${RELEASE_ID} (${SOURCE_COMMIT})"
