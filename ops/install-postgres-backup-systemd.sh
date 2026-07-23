#!/usr/bin/env bash
set -Eeuo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
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
