#!/usr/bin/env bash
set -Eeuo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
env_file="${BACKUP_B2_ENV_FILE:-/etc/myownclone/backup-b2.env}"

[[ "$(id -u)" -eq 0 ]] || { printf 'installer must run as root\n' >&2; exit 1; }
command -v rclone >/dev/null 2>&1 || { printf 'rclone is required before activation\n' >&2; exit 1; }
command -v age >/dev/null 2>&1 || { printf 'age is required before activation\n' >&2; exit 1; }
[[ -r "$env_file" ]] || { printf 'backup B2 environment is not readable\n' >&2; exit 1; }
[[ "$(stat -c '%u' "$env_file")" -eq 0 ]] || { printf 'backup B2 environment must be owned by root\n' >&2; exit 1; }
env_mode="$(stat -c '%a' "$env_file")"
(( (8#$env_mode & 077) == 0 )) || { printf 'backup B2 environment must not be accessible by group or others\n' >&2; exit 1; }

. "$env_file"
RCLONE_CONFIG="${RCLONE_CONFIG:-/etc/myownclone/rclone.conf}"
[[ -n "${B2_REMOTE:-}" ]] || { printf 'B2_REMOTE is required\n' >&2; exit 1; }
[[ -n "${BACKUP_AGE_RECIPIENT:-}" ]] || { printf 'BACKUP_AGE_RECIPIENT is required\n' >&2; exit 1; }
[[ -n "${RCLONE_CONFIG:-}" && -r "$RCLONE_CONFIG" ]] || { printf 'rclone config is not readable\n' >&2; exit 1; }
[[ "$(stat -c '%u' "$RCLONE_CONFIG")" -eq 0 ]] || { printf 'rclone config must be owned by root\n' >&2; exit 1; }
rclone_mode="$(stat -c '%a' "$RCLONE_CONFIG")"
(( (8#$rclone_mode & 077) == 0 )) || { printf 'rclone config must not be accessible by group or others\n' >&2; exit 1; }
rclone --config "$RCLONE_CONFIG" lsf --max-depth 1 "$B2_REMOTE" >/dev/null

for unit in myownclone-postgres-backup.service myownclone-postgres-backup.timer; do
  install -o root -g root -m 0644 "$script_dir/$unit" "/etc/systemd/system/$unit"
done
systemctl daemon-reload
systemctl enable --now myownclone-postgres-backup.timer
systemctl is-active --quiet myownclone-postgres-backup.timer

if crontab -l -u root 2>/dev/null | grep -F 'backup_postgres.sh' >/dev/null; then
  crontab -l -u root | grep -Fv 'backup_postgres.sh' | crontab -u root -
fi
printf 'PASS: systemd backup timer is active; legacy backup cron removed if present\n'
