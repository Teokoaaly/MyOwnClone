#!/usr/bin/env bash
set -Eeuo pipefail

backup_file="${1:?usage: verify_postgres_backup.sh BACKUP.sql.gz}"
container="${POSTGRES_CONTAINER:-myownclone_postgres}"
restore_db="terra_restore_$(date +%s)_$$"

[[ -f "$backup_file" ]] || {
  printf 'Backup not found: %s\n' "$backup_file" >&2
  exit 1
}
gzip -t -- "$backup_file"

cleanup() {
  docker exec "$container" dropdb --if-exists --force -U postgres "$restore_db" \
    >/dev/null 2>&1 || true
}
trap cleanup EXIT

docker exec "$container" createdb -U postgres "$restore_db"
gzip -dc -- "$backup_file" | docker exec -i "$container" \
  psql -v ON_ERROR_STOP=1 -U postgres -d "$restore_db" >/dev/null
table_count="$(docker exec "$container" psql -At -U postgres -d "$restore_db" \
  -c "SELECT count(*) FROM pg_catalog.pg_tables WHERE schemaname = 'public'")"
[[ "$table_count" =~ ^[1-9][0-9]*$ ]] || {
  printf 'Restored backup has no public tables\n' >&2
  exit 1
}
printf 'PASS: gzip and isolated PostgreSQL restore (%s tables)\n' "$table_count"
