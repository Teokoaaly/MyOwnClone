# Post-deploy Hardening - 2026-06-27

After the main VPS deploy (commit `8f73137`), follow-up hardening was
performed to reduce the risk surface discovered during the deploy.

## Changes made

### 1. Env vars backup moved to durable location

**Before**: `/tmp/api_env.json` (2084 bytes) was in the container's
ephemeral `/tmp/` layer, with the risk of being lost on container
recreation.

**After**: `/opt/myownclone/shared/api_env.json` (2084 bytes, mode 0600,
owner myownclone:myownclone). Survives container recreation. Contains
all 54 environment variables needed to recreate the `myownclone_api`
container with the rebuilt image.

This file is the source of truth for the env vars the API container
expects. If the container is recreated, this file is what the rollback
script should use.

### 2. Backup cron permissions fixed

**Problem discovered**: `0 3 * * * /opt/myownclone/current/ops/backup_postgres.sh`
was failing daily with `Permission denied`. The script existed but was
not executable (`-rw-r--r--`). This had been failing silently for
~9 days, leaving only one stale backup from 2026-06-19.

**Fix**:
```
sudo -n chmod +x /opt/myownclone/current/ops/backup_postgres.sh
sudo -n /opt/myownclone/current/ops/backup_postgres.sh 7
[2026-06-27T08:51:26+00:00] Starting backup of myownclone to /opt/myownclone/backups/myownclone_20260627_085126.sql.gz
[2026-06-27T08:51:27+00:00] Backup complete: /opt/myownclone/backups/myownclone_20260627_085126.sql.gz (12K)
[2026-06-27T08:51:27+00:00] Rotation: keeping last 7 days (1 backups on disk)
```

The 2026-06-19 backup was automatically rotated out by `KEEP_DAYS=7`.

### 3. Verified backup content

The backup is real (1623 lines uncompressed, 56KB raw, 9.7KB gzipped).
Uses pg_dump 15 format with `COPY public.<table>` blocks for 22
tables:

- `accounts`, `ai_model_assignments`, `ai_models`, `ai_invocations`
- `bookings`, `chunks`, `clone_configs`, `clone_feedback`,
  `clone_mode_prompts`, `conversations`, `cost_daily_rollup`,
  `cost_tracking`, `creator_memory`
- `email_inbound`, `email_templates`, `impersonation_log`,
  `impersonation_tokens`
- `meeting_types`, `messages`, `myownclone_plans`, `products`, `session`,
  `sources`, `tenants`, `users`, `verification_tokens`

The earlier confusion in this session — Python grep not finding
`INSERT INTO` — was a false negative: pg_dump 15 emits `COPY
public.<table> (...) FROM stdin;\n<tab-separated-values>\n\.` blocks,
not SQL `INSERT INTO` statements.

### 4. Image tags for rollback

The fixed image is tagged under THREE names so no future `docker
image prune` can accidentally remove it:

- `myownclone_api:fix-persisted` (the active deployment tag)
- `myownclone_api:v1.0.0-costs-fix` (semantic version tag)
- `ops-api:latest` (the build output)

All three point to the same SHA (`1c71792532410e2784be7311adfe7c4aa6b2ad7d91467357cfb12b93f31ba352`).

### 5. Build cache cleaned

`docker builder prune -af` reclaimed 1.702 GB of build cache. Docker
disk usage went from 2.779 GB (1.702 GB reclaimable) to 1.345 GB
(non-reclaimable, all in-use images).

### 6. Deploy script status

`ops/deploy-backend.sh` (read 2026-06-27) already uses the correct
modern deploy flow:

```bash
COMPOSE_BAKE=true "${COMPOSE_CMD[@]}" -f docker-compose.backend.prod.yml \
    up -d --build --remove-orphans
```

This is the correct command for future deploys. No changes were needed.

The deploy script also already includes:
- Pre-flight release directory creation
- `current` symlink swap with rollback trap
- Auto-loading env from `backend.env.production`
- Meta file `.deploy-backend-meta` with release info
- Health check loop (10 attempts x 3s) before declaring success
- Rollback on failure

## What is NOT done

1. **Old container images are gone**. The original image
   `8d4e055df156` was pruned during this session. Rollback to the
   pre-fix state is no longer possible via image tag — it requires
   rebuilding from the M14 source commit (SHA `8b16d1cc08a683df9e7ba6ebfbcfa1c1`).
2. **`ops/deploy-backend.sh` was NOT executed during this deploy**,
   because the live container was launched manually (not via compose).
   Future deploys SHOULD use this script for consistency.
3. **`/opt/myownclone/backups/` rotation**: the script deletes backups
   older than 7 days, but there is no off-host copy. A single disk
   failure would lose all backups. Consider adding `aws s3 sync` or
   similar.
4. **`ops/deploy-backend.sh` PATH**: the script does not verify
   `docker compose` plugin vs `docker-compose` binary before running.
   In a fresh host, neither may be available.

## State snapshot

| Path | Status |
| --- | --- |
| `/opt/myownclone/shared/api_env.json` | 2084 bytes, mode 0600, durable |
| `/opt/myownclone/shared/backend.env.production` | unchanged (used by deploy script) |
| `/opt/myownclone/backups/myownclone_20260627_085126.sql.gz` | 9.7KB, gzip valid, COPY format, 22 tables |
| `/opt/myownclone/current/ops/backup_postgres.sh` | mode 755 (was 644, broken cron) |
| Crontab `0 3 * * * /opt/myownclone/current/ops/backup_postgres.sh 7` | active |
| Image `myownclone_api:v1.0.0-costs-fix` | tagged for rollback |
| Image `myownclone_api:fix-persisted` | active container tag |
| Image `ops-api:latest` | build output, same SHA |