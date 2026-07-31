#!/usr/bin/env bash
set -Eeuo pipefail
umask 077

backup_name="${1:?usage: verify_b2_backup.sh BACKUP_BASENAME.sql.gz}"
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
env_file="${BACKUP_B2_ENV_FILE:-/etc/myownclone/backup-b2.env}"
timeout_seconds="${BACKUP_TIMEOUT_SECONDS:-300}"

[[ "$backup_name" == "$(basename -- "$backup_name")" && "$backup_name" =~ ^[A-Za-z0-9._-]+\.sql\.gz$ ]] || {
  printf 'backup name must be a safe .sql.gz basename\n' >&2
  exit 64
}
[[ -r "$env_file" ]] || { printf 'backup B2 environment is not readable\n' >&2; exit 1; }
[[ "$(stat -c '%u' "$env_file")" -eq 0 ]] || { printf 'backup B2 environment must be owned by root\n' >&2; exit 1; }
env_mode="$(stat -c '%a' "$env_file")"
(( (8#$env_mode & 077) == 0 )) || { printf 'backup B2 environment must not be accessible by group or others\n' >&2; exit 1; }
. "$env_file"
identity_file="${BACKUP_AGE_IDENTITY_FILE:-/etc/myownclone/backup-age.key}"
RCLONE_CONFIG="${RCLONE_CONFIG:-/etc/myownclone/rclone.conf}"

[[ -n "${B2_REMOTE:-}" ]] || { printf 'B2_REMOTE is required\n' >&2; exit 1; }
[[ -n "${RCLONE_CONFIG:-}" && -r "$RCLONE_CONFIG" ]] || { printf 'rclone config is not readable\n' >&2; exit 1; }
[[ "$(stat -c '%u' "$RCLONE_CONFIG")" -eq 0 ]] || { printf 'rclone config must be owned by root\n' >&2; exit 1; }
rclone_mode="$(stat -c '%a' "$RCLONE_CONFIG")"
(( (8#$rclone_mode & 077) == 0 )) || { printf 'rclone config must not be accessible by group or others\n' >&2; exit 1; }
[[ -r "$identity_file" ]] || { printf 'age identity is not readable\n' >&2; exit 1; }
[[ "$(stat -c '%u' "$identity_file")" -eq 0 ]] || { printf 'age identity must be owned by root\n' >&2; exit 1; }
identity_mode="$(stat -c '%a' "$identity_file")"
(( (8#$identity_mode & 077) == 0 )) || { printf 'age identity must not be accessible by group or others\n' >&2; exit 1; }
for command_name in rclone age sha256sum; do
  command -v "$command_name" >/dev/null 2>&1 || { printf '%s is required\n' "$command_name" >&2; exit 1; }
done

tmp_dir="$(mktemp -d /tmp/moc-task04-b2.XXXXXX)"
cleanup() { rm -rf -- "$tmp_dir"; }
trap cleanup EXIT INT TERM HUP

remote_base="${B2_REMOTE%/}/$backup_name"
encrypted_file="$tmp_dir/$backup_name.age"
encrypted_checksum_file="$encrypted_file.sha256"
manifest_file="$tmp_dir/$backup_name.manifest"
plain_file="$tmp_dir/$backup_name"
plain_checksum_file="$plain_file.sha256"

timeout "$timeout_seconds" rclone --config "$RCLONE_CONFIG" copyto "$remote_base.age" "$encrypted_file"
timeout "$timeout_seconds" rclone --config "$RCLONE_CONFIG" copyto "$remote_base.age.sha256" "$encrypted_checksum_file"
timeout "$timeout_seconds" rclone --config "$RCLONE_CONFIG" copyto "$remote_base.manifest" "$manifest_file"

(cd "$tmp_dir" && sha256sum -c -- "$(basename -- "$encrypted_checksum_file")")
grep -Fxq "encrypted_dump_file=$(basename -- "$encrypted_file")" "$manifest_file" || {
  printf 'manifest encrypted filename mismatch\n' >&2
  exit 1
}
plain_sha256="$(sed -n 's/^dump_sha256=//p' "$manifest_file")"
[[ "$plain_sha256" =~ ^[0-9a-f]{64}$ ]] || { printf 'manifest plaintext checksum is invalid\n' >&2; exit 1; }

timeout "$timeout_seconds" age --decrypt --identity "$identity_file" --output "$plain_file" "$encrypted_file"
printf '%s  %s\n' "$plain_sha256" "$backup_name" > "$plain_checksum_file"
(cd "$tmp_dir" && sha256sum -c -- "$(basename -- "$plain_checksum_file")")

BACKUP_TIMEOUT_SECONDS="$timeout_seconds" "$script_dir/verify_postgres_backup.sh" "$plain_file"
printf 'PASS: encrypted B2 backup downloaded, checksummed, decrypted, and restored in isolation\n'
