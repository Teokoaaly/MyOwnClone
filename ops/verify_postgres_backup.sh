#!/usr/bin/env bash
set -Eeuo pipefail
umask 077

backup_file="${1:?usage: verify_postgres_backup.sh BACKUP.sql.gz}"
container="${POSTGRES_CONTAINER:-myownclone_postgres}"
timeout_seconds="${BACKUP_TIMEOUT_SECONDS:-300}"
checksum_file="$backup_file.sha256"
manifest_file="$backup_file.manifest"
restore_db="terra_restore_$(date +%s)_$$"

[[ "$timeout_seconds" =~ ^[1-9][0-9]*$ ]] || { printf 'BACKUP_TIMEOUT_SECONDS must be a positive integer\n' >&2; exit 64; }
[[ -f "$backup_file" && -f "$checksum_file" && -s "$manifest_file" ]] || {
  printf 'backup, checksum, and manifest are all required\n' >&2; exit 1
}
grep -Fxq "dump_file=$(basename -- "$backup_file")" "$manifest_file" || { printf 'manifest dump filename mismatch\n' >&2; exit 1; }
grep -Fxq "sha256_file=$(basename -- "$checksum_file")" "$manifest_file" || { printf 'manifest checksum filename mismatch\n' >&2; exit 1; }
(cd "$(dirname -- "$backup_file")" && sha256sum -c -- "$(basename -- "$checksum_file")")
timeout "$timeout_seconds" gzip -t -- "$backup_file"

cleanup() { timeout "$timeout_seconds" docker exec "$container" dropdb --if-exists --force -U postgres "$restore_db" >/dev/null 2>&1 || true; }
trap cleanup EXIT INT TERM HUP

timeout "$timeout_seconds" docker exec "$container" createdb -U postgres "$restore_db"
timeout "$timeout_seconds" gzip -dc -- "$backup_file" | timeout "$timeout_seconds" docker exec -i "$container" \
  psql -v ON_ERROR_STOP=1 -U postgres -d "$restore_db" >/dev/null
table_count="$(timeout "$timeout_seconds" docker exec "$container" psql -At -U postgres -d "$restore_db" -c "SELECT count(*) FROM pg_catalog.pg_tables WHERE schemaname = 'public'")"
[[ "$table_count" =~ ^[1-9][0-9]*$ ]] || { printf 'restored backup has no public tables\n' >&2; exit 1; }
printf 'PASS: gzip, checksum, manifest, and isolated PostgreSQL restore (%s tables)\n' "$table_count"
