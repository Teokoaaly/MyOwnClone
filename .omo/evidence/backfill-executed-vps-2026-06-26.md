# Backfill Trigger Executed - VPS 2026-06-26

## What happened

Triggered `POST /console/api/myownclone/ai-models/backfill` on the live VPS
backend (container `myownclone_api`) with `Bearer` token from the
`platform_admin` admin login. The endpoint is defined in
`api/controllers/console/myownclone/ai_models.py::AIModelBackfillApi.post`
and calls `backfill_from_env(dry_run=False)` from
`api/commands/ai_backfill.py`, then invalidates the in-memory
`ModelRegistry()` cache.

## Trigger result

```json
{
  "models_created": 1,
  "models_updated": 0,
  "assignments_created": 3,
  "assignments_reused": 0,
  "providers_detected": ["minimax"],
  "skipped_tasks": ["embedding", "stt"]
}
HTTP 200
```

The idempotent backfill created:

- 1 `ai_models` row: `minimax/abab6.5s-chat` (provider `minimax`,
  capability `llm`).
- 3 `ai_model_assignments` rows mapping the same model to three LLM tasks:
  `chat`, `email_classification`, `email_draft`.
- Two tasks were skipped (`embedding`, `stt`) because no env vars for them
  exist in the running container — they keep the `legacy_env` source in
  `registry-status`.

## Post-backfill admin panel state

| Endpoint | Status | Body excerpt |
| --- | --- | --- |
| `ai-models` | 200 | 1 row (the `minimax/abab6.5s-chat` row above) |
| `ai-models/assignments` | 200 | 3 rows mapping LLM tasks to that model |
| `ai-models/registry-status` | 200 | `chat`, `email_classification`, `email_draft` now show `source: "database"` (not `legacy_env`) |
| `ai-models/embedding-status` | 200 | unchanged (no embedding env vars to backfill) |
| `ai-models/costs` | 200 | unchanged (1 invocation, 0 tokens) |

## Side effects (audited)

- **DB writes**: 1 insert into `ai_models`, 3 inserts into
  `ai_model_assignments`. All rows have `tenant_id = NULL` (platform-global,
  matching the backfill's design — LLM defaults apply to every tenant
  unless they override).
- **Cache invalidation**: `ModelRegistry().invalidate()` was called so the
  next `registry-status` GET rebuilds the registry with the new DB-backed
  entries.
- **No env vars touched**: env files in `/opt/myownclone/shared/` are
  unchanged; the backfill only reads them.

## Rollback (if needed)

The backfill is reversible because it only inserts rows. To revert, delete
the inserted rows by their ids:

```sql
DELETE FROM ai_model_assignments
WHERE id IN (
    '019f03d0-95bb-7bad-abe7-85b6ed7b7dae',
    '019f03d0-95bb-7afd-8b50-9e6228913427',
    '019f03d0-95bb-76bc-bdcb-d6bba13c5767'
);

DELETE FROM ai_models
WHERE id = '019f03d0-95b6-796a-a233-5ca74c05cb34';
```

Then call `POST /console/api/myownclone/ai-models/backfill` again — its
idempotency check (`SELECT … WHERE model_id = ?`) would skip them, so
re-running does NOT re-insert. To repopulate legacy behavior, simply delete
the rows above.

## Why the cost endpoint still shows only 1 invocation, 0 tokens

The cost endpoint aggregates from `ai_invocations`, not from `ai_models`
or `ai_model_assignments`. The only existing `AIInvocation` row in the
DB was created during the smoke test on Jun 24 and has `prompt_tokens = 0`,
`completion_tokens = 0` (no real tokens were consumed). This is expected
and not affected by the backfill.

To populate `cost_daily_rollup` and see real data in the panel's cost
chart, the daily rollup job (`api/core/ai_audit.py`) needs to run. This is
not blocked by the backfill and can be ***REMOVED*** in a separate step.

## What this did NOT do

- Did not modify any env var.
- Did not rebuild the docker image.
- Did not restart gunicorn (the backfill itself invalidated the registry
  cache, which is sufficient).
- Did not trigger any migration.
- Did not touch the `cost_daily_rollup` table (still empty).

## Follow-ups

1. Populate `cost_daily_rollup` by running the rollup job (`flask ai-rotate-audit`
   or whatever the entry point is named in the deployment script).
2. Optionally add `embedding` and `stt` providers so the remaining
   `legacy_env` tasks also move to `database`.
3. Build the `ops-api` image from the integration branch so the
   `_invocation_model_key` fix survives container recreations.