#!/usr/bin/env bash
set -Eeuo pipefail
umask 077

backup_file="${1:?usage: verify_postgres_backup.sh BACKUP.sql.gz}"
timeout_seconds="${BACKUP_TIMEOUT_SECONDS:-300}"
checksum_file="$backup_file.sha256"
manifest_file="$backup_file.manifest"
restore_image="${RESTORE_POSTGRES_IMAGE:-pgvector/pgvector:pg15@sha256:3073dc147f5b0ca05b36e10e04e73ca180b1e726e453c72a6fcc85f788afd0d1}"
resource_prefix="${RESTORE_RESOURCE_PREFIX:-moc-task04-$(date -u +%Y%m%d%H%M%S)-$$}"
restore_container="${resource_prefix}-postgres"
restore_network="${resource_prefix}-network"
restore_volume="${resource_prefix}-data"
restore_db="task04_restore"

[[ "$timeout_seconds" =~ ^[1-9][0-9]*$ ]] || { printf 'BACKUP_TIMEOUT_SECONDS must be a positive integer\n' >&2; exit 64; }
[[ "$resource_prefix" =~ ^moc-task04-[A-Za-z0-9][A-Za-z0-9_.-]*$ ]] || {
  printf 'RESTORE_RESOURCE_PREFIX must start with moc-task04- and contain only safe characters\n' >&2
  exit 64
}
[[ -f "$backup_file" && -f "$checksum_file" && -s "$manifest_file" ]] || {
  printf 'backup, checksum, and manifest are all required\n' >&2; exit 1
}
grep -Fxq "dump_file=$(basename -- "$backup_file")" "$manifest_file" || { printf 'manifest dump filename mismatch\n' >&2; exit 1; }
grep -Fxq "sha256_file=$(basename -- "$checksum_file")" "$manifest_file" || { printf 'manifest checksum filename mismatch\n' >&2; exit 1; }
(cd "$(dirname -- "$backup_file")" && sha256sum -c -- "$(basename -- "$checksum_file")")
timeout "$timeout_seconds" gzip -t -- "$backup_file"

command -v docker >/dev/null 2>&1 || { printf 'docker is required for isolated restore\n' >&2; exit 1; }
docker image inspect "$restore_image" >/dev/null 2>&1 || {
  printf 'compatible PostgreSQL/pgvector restore image is not available locally\n' >&2
  exit 1
}

if docker ps -a --format '{{.Names}}' | grep -Fxq "$restore_container" \
  || docker network ls --format '{{.Name}}' | grep -Fxq "$restore_network" \
  || docker volume ls --format '{{.Name}}' | grep -Fxq "$restore_volume"; then
  printf 'one or more isolated restore resources already exist\n' >&2
  exit 1
fi

container_created=0
network_created=0
volume_created=0
cleanup() {
  [[ "$container_created" -eq 0 ]] || docker rm --force "$restore_container" >/dev/null 2>&1 || true
  [[ "$network_created" -eq 0 ]] || docker network rm "$restore_network" >/dev/null 2>&1 || true
  [[ "$volume_created" -eq 0 ]] || docker volume rm "$restore_volume" >/dev/null 2>&1 || true
}
trap cleanup EXIT INT TERM HUP

docker network create "$restore_network" >/dev/null
network_created=1
docker volume create "$restore_volume" >/dev/null
volume_created=1
docker run --detach \
  --name "$restore_container" \
  --network "$restore_network" \
  --mount "type=volume,source=$restore_volume,target=/var/lib/postgresql/data" \
  --env POSTGRES_HOST_AUTH_METHOD=trust \
  "$restore_image" >/dev/null
container_created=1

ready=0
for _ in $(seq 1 60); do
  if docker exec "$restore_container" pg_isready -U postgres >/dev/null 2>&1; then
    ready=1
    break
  fi
  sleep 1
done
[[ "$ready" -eq 1 ]] || { printf 'isolated PostgreSQL did not become ready\n' >&2; exit 1; }

timeout "$timeout_seconds" docker exec "$restore_container" createdb -U postgres "$restore_db"
timeout "$timeout_seconds" gzip -dc -- "$backup_file" | timeout "$timeout_seconds" docker exec -i "$restore_container" \
  psql -v ON_ERROR_STOP=1 -U postgres -d "$restore_db" >/dev/null

table_count="$(timeout "$timeout_seconds" docker exec "$restore_container" psql -At -U postgres -d "$restore_db" -c "SELECT count(*) FROM pg_catalog.pg_tables WHERE schemaname = 'public'")"
[[ "$table_count" =~ ^[1-9][0-9]*$ ]] || { printf 'restored backup has no public tables\n' >&2; exit 1; }

alembic_head="$(timeout "$timeout_seconds" docker exec "$restore_container" psql -At -U postgres -d "$restore_db" -c "SELECT version_num FROM alembic_version ORDER BY version_num DESC LIMIT 1")"
[[ -n "$alembic_head" ]] || { printf 'restored backup has no Alembic version\n' >&2; exit 1; }

declare -A counts=()
for table in tenants users clone_configs sources chunks; do
  exists="$(timeout "$timeout_seconds" docker exec "$restore_container" psql -At -U postgres -d "$restore_db" -c "SELECT to_regclass('public.$table') IS NOT NULL")"
  [[ "$exists" == "t" ]] || { printf 'restored backup is missing required table %s\n' "$table" >&2; exit 1; }
  count="$(timeout "$timeout_seconds" docker exec "$restore_container" psql -At -U postgres -d "$restore_db" -c "SELECT count(*) FROM \"$table\"")"
  [[ "$count" =~ ^[0-9]+$ ]] || { printf 'invalid row count for table %s\n' "$table" >&2; exit 1; }
  counts["$table"]="$count"
done

printf 'PASS: isolated restore tables=%s alembic=%s tenants=%s users=%s clone_configs=%s sources=%s chunks=%s\n' \
  "$table_count" "$alembic_head" "${counts[tenants]}" "${counts[users]}" \
  "${counts[clone_configs]}" "${counts[sources]}" "${counts[chunks]}"
