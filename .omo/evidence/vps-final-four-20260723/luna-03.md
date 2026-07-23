# LUNA-03 — Auth schema repair evidence

## Baseline

- Base commit: `1af7ca9a94b3fc83f1e5858726ce2e75d1f`.
- `MyOwnClone/src/lib/db/schema/users.ts` already declares nullable `emailVerified` as `email_verified`.
- Drizzle snapshots `0000` through `0004` also declare that column, but production-compatible databases can lack it; a generated snapshot migration would therefore not repair the discrepancy.

## Red to green

- Focused red run: `python -m pytest api/tests/test_auth_schema_boundary.py tests/test_release_manifest.py tests/test_deploy_backend_script.py -q` failed because `0005_repair_users_email_verified.sql` did not exist.
- Focused green run: `21 passed, 2 skipped` for auth boundary, migration integration, manifest, and deploy-script tests.
- Full suite: `132 passed, 3 skipped, 2 warnings` from `python -m pytest -q`.

## Implemented behavior

- `0005_repair_users_email_verified.sql` is a custom, journalled Drizzle migration. It checks that `public.users` exists, then adds nullable `email_verified timestamp` with `IF NOT EXISTS`; reruns preserve all table rows.
- The release manifest scopes frontend payloads to Drizzle SQL/meta, package metadata, `drizzle.config.ts`, and `src/lib/db/schema/**` only; it excludes UI/application sources.
- `ops/docker-compose.schema-migrator.yml` uses an ephemeral Node 22 service, validates `DATABASE_URL` without logging it, executes `npm ci --ignore-scripts`, then `npx drizzle-kit migrate`. It does not build or start Next.
- Deployment runs the isolated schema migrator before API Alembic migrations and continues to restart only API/worker services.

## Manual QA and cleanup receipt

- Compose configuration check passed with an isolated PostgreSQL URL: `docker compose -f ops/docker-compose.schema-migrator.yml config`.
- Local container QA was not executable: Docker client 29.6.1 reported that `dockerDesktopLinuxEngine` was unavailable, and two bounded `docker info` probes timed out. The integration tests therefore skipped rather than reporting a false pass.
- No Postgres container, volume, or temporary database was created; no cleanup action was necessary.
- The committed integration tests execute both paths when a Docker daemon is available: empty database no-op, then compatible database migration twice with explicit `information_schema.columns` plus seeded user identity, password hash, and tenant preservation assertions.

## DoneClaim

Schema migration, release packaging, manifest validation, and isolated migration-runner implementation are complete and verified by static/configuration tests plus the full Python suite. Real container execution remains locally unverified solely because the Docker daemon is unavailable; CI or a host with Docker will execute the retained integration assertions.
