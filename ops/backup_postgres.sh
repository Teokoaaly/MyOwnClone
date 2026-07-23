#!/usr/bin/env bash
set -Eeuo pipefail
umask 077

KEEP_DAYS="${1:-7}"
BACKUP_DIR="${BACKUP_DIR:-/opt/myownclone/backups}"
BACKEND_CURRENT="${BACKEND_CURRENT:-/opt/myownclone/backend-current}"
CONTAINER="${POSTGRES_CONTAINER:-myownclone_postgres}"
DB_NAME="${POSTGRES_DB:-myownclone}"
BACKUP_TIMEOUT_SECONDS="${BACKUP_TIMEOUT_SECONDS:-300}"
BACKUP_B2_ENV_FILE="${BACKUP_B2_ENV_FILE:-/etc/myownclone/backup-b2.env}"
TIMESTAMP="${BACKUP_TIMESTAMP:-$(date -u +%Y%m%d_%H%M%S)}"

[[ "$KEEP_DAYS" =~ ^[1-9][0-9]*$ ]] || { printf 'KEEP_DAYS must be a positive integer\n' >&2; exit 64; }
[[ "$BACKUP_TIMEOUT_SECONDS" =~ ^[1-9][0-9]*$ ]] || { printf 'BACKUP_TIMEOUT_SECONDS must be a positive integer\n' >&2; exit 64; }
[[ "$TIMESTAMP" =~ ^[0-9]{8}_[0-9]{6}$ ]] || { printf 'BACKUP_TIMESTAMP must be YYYYMMDD_HHMMSS\n' >&2; exit 64; }

release_dir="$(readlink -f -- "$BACKEND_CURRENT")"
[[ -d "$release_dir" ]] || { printf 'backend-current does not resolve to a release directory\n' >&2; exit 1; }
mkdir -p -- "$BACKUP_DIR"

file="$BACKUP_DIR/${DB_NAME}_${TIMESTAMP}.sql.gz"
checksum_file="$file.sha256"
manifest_file="$file.manifest"
tmp_dump="$(mktemp "$BACKUP_DIR/.${DB_NAME}_${TIMESTAMP}.XXXXXX.sql.gz")"
tmp_checksum="$(mktemp "$BACKUP_DIR/.${DB_NAME}_${TIMESTAMP}.XXXXXX.sha256")"
tmp_manifest="$(mktemp "$BACKUP_DIR/.${DB_NAME}_${TIMESTAMP}.XXXXXX.manifest")"

pipeline_pid=""
publication_started=0
backup_complete=0
cleanup() {
  rm -f -- "$tmp_dump" "$tmp_checksum" "$tmp_manifest"
  if [[ "$publication_started" -eq 1 && "$backup_complete" -eq 0 ]]; then
    rm -f -- "$file" "$checksum_file" "$manifest_file"
  fi
}
cancel() {
  [[ -z "$pipeline_pid" ]] || kill -- "-$pipeline_pid" 2>/dev/null || true
  exit 143
}
trap cleanup EXIT
trap cancel INT TERM HUP

printf '[%s] backup release=%s db=%s\n' "$(date -Iseconds)" "$release_dir" "$DB_NAME" >&2
setsid bash -o pipefail -c '
  timeout "$1" docker exec "$2" pg_dump -U postgres -d "$3" --format=plain --no-owner --no-privileges \
    | timeout "$1" gzip -c
' bash "$BACKUP_TIMEOUT_SECONDS" "$CONTAINER" "$DB_NAME" > "$tmp_dump" &
pipeline_pid=$!
wait "$pipeline_pid"
pipeline_pid=""
gzip -t -- "$tmp_dump"
printf '%s  %s\n' "$(sha256sum -- "$tmp_dump" | cut -d' ' -f1)" "$(basename -- "$file")" > "$tmp_checksum"
{
  printf 'format=postgresql-plain-gzip\n'
  printf 'database=%s\n' "$DB_NAME"
  printf 'created_at_utc=%s\n' "$(date -u -Iseconds)"
  printf 'release_dir=%s\n' "$release_dir"
  printf 'dump_file=%s\n' "$(basename -- "$file")"
  printf 'sha256_file=%s\n' "$(basename -- "$checksum_file")"
} > "$tmp_manifest"

[[ ! -e "$file" && ! -e "$checksum_file" && ! -e "$manifest_file" ]] || {
  printf 'backup artifact already exists for timestamp %s\n' "$TIMESTAMP" >&2
  exit 1
}
publication_started=1
mv -- "$tmp_dump" "$file"
mv -- "$tmp_checksum" "$checksum_file"
mv -- "$tmp_manifest" "$manifest_file"
backup_complete=1

if [[ -r "$BACKUP_B2_ENV_FILE" ]]; then
  . "$BACKUP_B2_ENV_FILE"
  [[ -n "${B2_REMOTE:-}" ]] || { printf 'B2_REMOTE is required in backup B2 environment\n' >&2; exit 1; }
  command -v rclone >/dev/null 2>&1 || { printf 'rclone is required for configured B2 upload\n' >&2; exit 1; }
  remote_base="${B2_REMOTE%/}/$(basename -- "$file")"
  timeout "$BACKUP_TIMEOUT_SECONDS" rclone copyto --immutable "$file" "$remote_base"
  timeout "$BACKUP_TIMEOUT_SECONDS" rclone copyto --immutable "$checksum_file" "$remote_base.sha256"
  timeout "$BACKUP_TIMEOUT_SECONDS" rclone copyto --immutable "$manifest_file" "$remote_base.manifest"
fi

mapfile -t backups < <(find "$BACKUP_DIR" -maxdepth 1 -type f -name "${DB_NAME}_*.sql.gz" -printf '%T@ %p\n' | sort -nr | cut -d' ' -f2-)
for ((index = KEEP_DAYS; index < ${#backups[@]}; index++)); do
  old="${backups[$index]}"
  rm -f -- "$old" "$old.sha256" "$old.manifest"
done

printf '%s\n' "$file"
