# AI Costs Fix - VPS Deploy Record - 2026-06-26

## Summary

The `ai_models.py` handler in the running backend container was patched
in-place to fix the 500 on `GET /console/api/myownclone/ai-models/costs`.
No image rebuild, no full release redeploy, no DB migration was needed.

## Pre-deploy state

- Live backend container: `myownclone_api` (id `6b61ad107e1a`)
- cwd: `/app`
- Active gunicorn cmdline: `gunicorn --bind 0.0.0.0:5001 --workers 2 --timeout 60 --access-logfile - --error-logfile - api.app_factory:app`
- Active code SHA on disk: `8b16d1cc08a683df9e7ba6ebfbcfa1c1`
  (identical to M14 commit `c00612f`).
- `alembic_version = f3a4b5c6d7e8` (cost_daily_rollup head — table exists, 0 rows).
- `ai_invocations` schema exposes column `model` (NOT `model_id`).
- `GET /console/api/myownclone/ai-models/costs` → HTTP 500 (`Internal Server Error`).

## Deploy steps (executed)

```bash
# 1. Backup the original file inside the container
sudo -n docker exec myownclone_api \
    cp /app/api/controllers/console/myownclone/ai_models.py \
       /app/api/controllers/console/myownclone/ai_models.py.bak

# 2. Copy the fixed file into the container
#    (fixed file produced from local commit ed47382)
scp /tmp/ai_models_fixed.py myownclone@100.125.128.116:/tmp/
sudo -n docker cp /tmp/ai_models_fixed.py \
    myownclone_api:/app/api/controllers/console/myownclone/ai_models.py

# 3. Reload gunicorn workers via SIGHUP
sudo -n docker kill --signal=SIGHUP myownclone_api
```

## Post-deploy state

- File SHA on disk inside container:
  - new `ai_models.py`: `ca4fef8b4c5d9c1c1f1b74e3719c2f24`
  - backup `ai_models.py.bak`: `8b16d1cc08a683df9e7ba6ebfbcfa1c1`
- Gunicorn master still alive (PID 1 inside container, cwd `/app`).

## Live validation (after deploy)

```
$ curl -sS -w 'HTTP %{http_code}\n' \
    -H "Authorization: Bearer $TOKEN" \
    http://127.0.0.1:5001/console/api/myownclone/ai-models/costs

{"series": [{"day": "2026-06-26", "invocations": 1, "prompt_tokens": 0, "completion_tokens": 0}],
 "totals": {"invocations": 1, "prompt_tokens": 0, "completion_tokens": 0},
 "by_model": [{"model_id": "minimax-m2.7", "invocations": 1, "prompt_tokens": 0, "completion_tokens": 0}]}
HTTP 200
```

All other AI admin endpoints:

| Endpoint | Status | Body excerpt |
| --- | --- | --- |
| `ai-models` | 200 | `[]` (empty list) |
| `ai-models/assignments` | 200 | `[]` (empty list) |
| `ai-models/registry-status` | 200 | 5 tasks from `legacy_env` |
| `ai-models/embedding-status` | 200 | `{max_embed_texts: 256, ...}` |
| `ai-models/costs` | **200** | 1 series bucket, 1 by_model entry |
| `admin/overview` | 200 | 2 tenants, 2 clones, $0 MRR |

`/readyz`: `{"checks":{"database":"ok","redis":"ok"},"status":"ready"}`.

## Backfill endpoint (NOT executed, awaiting user approval)

`POST /console/api/myownclone/ai-models/backfill` exists and triggers
`flask ai-backfill-from-env`. It is idempotent and reads only env vars, but
it commits new rows to `ai_models` and `ai_model_assignments`. It was
**not** called as part of this deploy — explicit approval required because
it mutates production data.

## Rollback procedure

If the new code causes regressions:

```bash
# Restore the original file from the backup inside the container
sudo -n docker exec myownclone_api \
    cp /app/api/controllers/console/myownclone/ai_models.py.bak \
       /app/api/controllers/console/myownclone/ai_models.py

# Reload gunicorn
sudo -n docker kill --signal=SIGHUP myownclone_api
```

The backup file `ai_models.py.bak` is preserved inside the container. No
DB changes were made during the deploy, so no DB rollback is needed.

For full release rollback to the previous version (pre-deploy):

```bash
# Container has no image rollback button; rebuild + restart is the path.
# Safer: re-pin the image tag in docker-compose.backend.prod.yml and
# run docker compose up -d --build.
```

## Commits included in this deploy

| SHA | Description |
| --- | --- |
| `b568ca2` | `fix(ai): handle missing cost_daily_rollup in admin costs endpoint` (defensive try/except, kept for depth) |
| `ed47382` | `fix(ai): tolerate AIInvocation.model vs model_id column in costs handler` (real bug fix) |

Branch: `fix/ai-costs-missing-rollup-table`, pushed to
`origin/fix/ai-costs-missing-rollup-table`.

## What this deploy did NOT do

- Did not rebuild the docker image. The patched `ai_models.py` lives
  only inside the running container and will be lost if the container is
  recreated.
- Did not run any DB migration.
- Did not trigger the backfill endpoint.
- Did not change any env var.
- Did not touch the live VPS release symlinks (`/opt/myownclone/current`
  still points to the frontend-only release `20260620070304-frontend-dashboard-fix`).

## Recommended follow-ups

1. **Persist the patch** in the image: update the source on the integration
   branch (`audit/sisyphus-vps-integration-push-sync`) by merging
   `fix/ai-costs-missing-rollup-table`, rebuild the `ops-api` image, and
   redeploy via `docker compose up -d --build` so the patched file
   survives container recreations.
2. **Apply the backfill** (only after explicit user OK) by POSTing to
   `/console/api/myownclone/ai-models/backfill` so `ai_models` and
   `ai_model_assignments` get populated from the existing env vars.
3. **Schedule a daily rollup** so `cost_daily_rollup` gets pre-aggregated
   rows and the costs endpoint uses the fast-path instead of always
   falling back to `AIInvocation`.