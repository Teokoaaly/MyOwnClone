#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# bootstrap-drizzle-migrator.sh
#
# Idempotent bootstrap required by `ops/docker-compose.schema-migrator.yml` so
# that the `drizzle-kit migrate` step can run from a clean database.
#
# Background
# ──────────
#   • `docker-compose.schema-migrator.yml` connects to PostgreSQL using the
#     `myownclone_app` role (the one declared in `backend.env.production`).
#   • The first action of `drizzle-kit migrate` is
#         CREATE SCHEMA IF NOT EXISTS drizzle;
#         CREATE TABLE IF NOT EXISTS drizzle.__drizzle_migrations (...);
#     which requires the `CREATE` privilege on the **database**, not just on
#     a schema. The production role only has `USAGE` on `public`, so on a
#     fresh database the migrator exits with:
#         ERROR: permission denied for database myownclone
#   • The role is also expected to be able to `INSERT` into
#     `drizzle.__drizzle_migrations`; on a re-run, the table already exists
#     and only the INSERT is required, so the GRANT below must be
#     unconditionally idempotent.
#
# Usage
# ─────
#   Run this ONCE per environment, from the same host that owns the postgres
#   container, as a role that already has `CREATEROLE` / is `postgres`:
#
#     sudo ./ops/bootstrap-drizzle-migrator.sh
#
#   It is safe to re-run; every statement is `IF NOT EXISTS` / `DO $$ ... $$`.
#
#   The script reads `DB_*` variables from `ops/backend.env.production`. It
#   does not print credentials.
# ─────────────────────────────────────────────────────────────────────────────
set -Eeuo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="${ENV_FILE:-${SCRIPT_DIR}/backend.env.production}"

if [[ ! -f "${ENV_FILE}" ]]; then
    echo "ERROR: env file not found: ${ENV_FILE}" >&2
    exit 1
fi

# shellcheck disable=SC1090
. "${ENV_FILE}"

: "${DB_HOST:?DB_HOST is required}"
: "${DB_PORT:=5432}"
: "${DB_NAME:?DB_NAME is required}"
: "${DB_USER:?DB_USER is required}"
# DB_PASSWORD is read only to forward it to psql; never echo it.

POSTGRES_HOST="${POSTGRES_HOST:-${DB_HOST}}"
POSTGRES_PORT="${POSTGRES_PORT:-${DB_PORT}}"
# The GRANT must be issued by a superuser. Default to the local `postgres`
# role via the `myownclone_postgres` container, which the standard
# `docker-compose.backend.prod.yml` provides.
POSTGRES_SUPERUSER="${POSTGRES_SUPERUSER:-postgres}"
POSTGRES_CONTAINER="${POSTGRES_CONTAINER:-myownclone_postgres}"

# Sanitized display (no secret material).
echo "[bootstrap] target=${POSTGRES_HOST}:${POSTGRES_PORT}/${DB_NAME} role=${DB_USER}"

SQL=$(cat <<SQL_END
DO \$do\$
BEGIN
    -- Allow the app role to create its own bookkeeping schema.
    IF NOT EXISTS (
        SELECT 1 FROM pg_database WHERE datname = '${DB_NAME}'
    ) THEN
        RAISE EXCEPTION 'database % does not exist', '${DB_NAME}';
    END IF;

    EXECUTE format('GRANT CREATE ON DATABASE %I TO %I', '${DB_NAME}', '${DB_USER}');

    -- The schema and table are created on first use by drizzle-kit, but we
    -- also pre-create them here so that a manual `drizzle-kit migrate` run
    -- outside the schema_migrator service does not require the same
    -- permission escalation.
    EXECUTE format('GRANT USAGE, CREATE ON SCHEMA public TO %I', '${DB_USER}');
END
\$do\$;

-- The drizzle bookkeeping schema + table are created on demand by
-- drizzle-kit. We only ensure the role has the privilege to do so; the
-- actual objects are owned by the role and will be created on the first
-- `drizzle-kit migrate` invocation.
SQL_END
)

if command -v docker >/dev/null 2>&1 && docker ps --format '{{.Names}}' | grep -qx "${POSTGRES_CONTAINER}"; then
    echo "[bootstrap] using docker container ${POSTGRES_CONTAINER}"
    docker exec -e PGPASSWORD="${DB_PASSWORD}" \
        "${POSTGRES_CONTAINER}" \
        env PGPASSWORD="${DB_PASSWORD}" \
        psql -v ON_ERROR_STOP=1 -U "${POSTGRES_SUPERUSER}" -d "${DB_NAME}" -c "${SQL}"
else
    echo "[bootstrap] using local psql against ${POSTGRES_HOST}:${POSTGRES_PORT}"
    PGPASSWORD="${DB_PASSWORD}" psql -v ON_ERROR_STOP=1 \
        -h "${POSTGRES_HOST}" -p "${POSTGRES_PORT}" \
        -U "${POSTGRES_SUPERUSER}" -d "${DB_NAME}" -c "${SQL}"
fi

echo "[bootstrap] done. Drizzle migrator privileges are now in place."
