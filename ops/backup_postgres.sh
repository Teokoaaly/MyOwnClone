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
BACKUP_OFFSITE_REQUIRED="${BACKUP_OFFSITE_REQUIRED:-1}"
TIMESTAMP="${BACKUP_TIMESTAMP:-$(date -u +%Y%m%d_%H%M%S)}"

[[ "$KEEP_DAYS" =~ ^[1-9][0-9]*$ ]] || { printf 'KEEP_DAYS must be a positive integer\n' >&2; exit 64; }
[[ "$BACKUP_TIMEOUT_SECONDS" =~ ^[1-9][0-9]*$ ]] || { printf 'BACKUP_TIMEOUT_SECONDS must be a positive integer\n' >&2; exit 64; }
[[ "$BACKUP_OFFSITE_REQUIRED" =~ ^[01]$ ]] || { printf 'BACKUP_OFFSITE_REQUIRED must be 0 or 1\n' >&2; exit 64; }
[[ "$TIMESTAMP" =~ ^[0-9]{8}_[0-9]{6}$ ]] || { printf 'BACKUP_TIMESTAMP must be YYYYMMDD_HHMMSS\n' >&2; exit 64; }

release_dir="$(readlink -f -- "$BACKEND_CURRENT")"
[[ -d "$release_dir" ]] || { printf 'backend-current does not resolve to a release directory\n' >&2; exit 1; }
mkdir -p -- "$BACKUP_DIR"

offsite_enabled=0
if [[ -r "$BACKUP_B2_ENV_FILE" ]]; then
  [[ "$(stat -c '%u' "$BACKUP_B2_ENV_FILE")" -eq 0 ]] || { printf 'backup B2 environment must be owned by root\n' >&2; exit 1; }
  env_mode="$(stat -c '%a' "$BACKUP_B2_ENV_FILE")"
  (( (8#$env_mode & 077) == 0 )) || { printf 'backup B2 environment must not be accessible by group or others\n' >&2; exit 1; }
  . "$BACKUP_B2_ENV_FILE"
  RCLONE_CONFIG="${RCLONE_CONFIG:-/etc/myownclone/rclone.conf}"
  [[ -n "${B2_REMOTE:-}" ]] || { printf 'B2_REMOTE is required in backup B2 environment\n' >&2; exit 1; }
  [[ -n "${BACKUP_AGE_RECIPIENT:-}" ]] || { printf 'BACKUP_AGE_RECIPIENT is required in backup B2 environment\n' >&2; exit 1; }
  [[ -n "${RCLONE_CONFIG:-}" && -r "$RCLONE_CONFIG" ]] || { printf 'RCLONE_CONFIG must reference a readable root-only file\n' >&2; exit 1; }
  [[ "$(stat -c '%u' "$RCLONE_CONFIG")" -eq 0 ]] || { printf 'rclone config must be owned by root\n' >&2; exit 1; }
  rclone_mode="$(stat -c '%a' "$RCLONE_CONFIG")"
  (( (8#$rclone_mode & 077) == 0 )) || { printf 'rclone config must not be accessible by group or others\n' >&2; exit 1; }
  command -v rclone >/dev/null 2>&1 || { printf 'rclone is required for configured B2 upload\n' >&2; exit 1; }
  command -v age >/dev/null 2>&1 || { printf 'age is required for encrypted B2 upload\n' >&2; exit 1; }
  timeout "$BACKUP_TIMEOUT_SECONDS" rclone --config "$RCLONE_CONFIG" lsf --max-depth 1 "$B2_REMOTE" >/dev/null
  offsite_enabled=1
elif [[ "$BACKUP_OFFSITE_REQUIRED" -eq 1 ]]; then
  printf 'required backup B2 environment is not readable\n' >&2
  exit 1
fi

file="$BACKUP_DIR/${DB_NAME}_${TIMESTAMP}.sql.gz"
checksum_file="$file.sha256"
manifest_file="$file.manifest"
encrypted_file="$file.age"
encrypted_checksum_file="$encrypted_file.sha256"
tmp_dump="$(mktemp "$BACKUP_DIR/.${DB_NAME}_${TIMESTAMP}.XXXXXX.sql.gz")"
tmp_checksum="$(mktemp "$BACKUP_DIR/.${DB_NAME}_${TIMESTAMP}.XXXXXX.sha256")"
tmp_manifest="$(mktemp "$BACKUP_DIR/.${DB_NAME}_${TIMESTAMP}.XXXXXX.manifest")"
tmp_encrypted=""
tmp_encrypted_checksum=""
if [[ "$offsite_enabled" -eq 1 ]]; then
  tmp_encrypted="$(mktemp "$BACKUP_DIR/.${DB_NAME}_${TIMESTAMP}.XXXXXX.sql.gz.age")"
  tmp_encrypted_checksum="$(mktemp "$BACKUP_DIR/.${DB_NAME}_${TIMESTAMP}.XXXXXX.sql.gz.age.sha256")"
fi

pipeline_pid=""
publication_started=0
backup_complete=0
cleanup() {
  rm -f -- "$tmp_dump" "$tmp_checksum" "$tmp_manifest"
  [[ -z "$tmp_encrypted" ]] || rm -f -- "$tmp_encrypted"
  [[ -z "$tmp_encrypted_checksum" ]] || rm -f -- "$tmp_encrypted_checksum"
  if [[ "$publication_started" -eq 1 && "$backup_complete" -eq 0 ]]; then
    rm -f -- "$file" "$checksum_file" "$manifest_file" "$file.age" "$file.age.sha256"
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
dump_sha256="$(sha256sum -- "$tmp_dump" | cut -d' ' -f1)"
printf '%s  %s\n' "$dump_sha256" "$(basename -- "$file")" > "$tmp_checksum"

encrypted_sha256=""
if [[ "$offsite_enabled" -eq 1 ]]; then
  timeout "$BACKUP_TIMEOUT_SECONDS" age --encrypt --recipient "$BACKUP_AGE_RECIPIENT" \
    --output "$tmp_encrypted" "$tmp_dump"
  encrypted_sha256="$(sha256sum -- "$tmp_encrypted" | cut -d' ' -f1)"
  printf '%s  %s\n' "$encrypted_sha256" "$(basename -- "$encrypted_file")" > "$tmp_encrypted_checksum"
fi

{
  printf 'format=postgresql-plain-gzip\n'
  printf 'database=%s\n' "$DB_NAME"
  printf 'created_at_utc=%s\n' "$(date -u -Iseconds)"
  printf 'release_dir=%s\n' "$release_dir"
  printf 'dump_file=%s\n' "$(basename -- "$file")"
  printf 'sha256_file=%s\n' "$(basename -- "$checksum_file")"
  printf 'dump_sha256=%s\n' "$dump_sha256"
  if [[ "$offsite_enabled" -eq 1 ]]; then
    printf 'encryption=age\n'
    printf 'encrypted_dump_file=%s\n' "$(basename -- "$encrypted_file")"
    printf 'encrypted_sha256_file=%s\n' "$(basename -- "$encrypted_checksum_file")"
    printf 'encrypted_sha256=%s\n' "$encrypted_sha256"
  fi
} > "$tmp_manifest"

[[ ! -e "$file" && ! -e "$checksum_file" && ! -e "$manifest_file" && ! -e "$encrypted_file" && ! -e "$encrypted_checksum_file" ]] || {
  printf 'backup artifact already exists for timestamp %s\n' "$TIMESTAMP" >&2
  exit 1
}
publication_started=1
mv -- "$tmp_dump" "$file"
mv -- "$tmp_checksum" "$checksum_file"
mv -- "$tmp_manifest" "$manifest_file"
if [[ "$offsite_enabled" -eq 1 ]]; then
  mv -- "$tmp_encrypted" "$encrypted_file"
  mv -- "$tmp_encrypted_checksum" "$encrypted_checksum_file"
fi
backup_complete=1

if [[ "$offsite_enabled" -eq 1 ]]; then
  remote_base="${B2_REMOTE%/}/$(basename -- "$file")"
  timeout "$BACKUP_TIMEOUT_SECONDS" rclone --config "$RCLONE_CONFIG" copyto --immutable "$encrypted_file" "$remote_base.age"
  timeout "$BACKUP_TIMEOUT_SECONDS" rclone --config "$RCLONE_CONFIG" copyto --immutable "$encrypted_checksum_file" "$remote_base.age.sha256"
  timeout "$BACKUP_TIMEOUT_SECONDS" rclone --config "$RCLONE_CONFIG" copyto --immutable "$manifest_file" "$remote_base.manifest"
fi

mapfile -t backups < <(find "$BACKUP_DIR" -maxdepth 1 -type f -name "${DB_NAME}_*.sql.gz" -printf '%T@ %p\n' | sort -nr | cut -d' ' -f2-)
for ((index = KEEP_DAYS; index < ${#backups[@]}; index++)); do
  old="${backups[$index]}"
  rm -f -- "$old" "$old.sha256" "$old.manifest" "$old.age" "$old.age.sha256"
done

printf '%s\n' "$file"
