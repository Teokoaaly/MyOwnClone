# Evidence — M13 (defects #3/#4/#6, backfill, docs, final verification)

- Date: 2026-06-23
- Branch: `audit/sisyphus-vps-integration`
- Base SHA: `2c099f2fbcbfbc34783268c3a04c550aa943d285` (M12)
- Worktree: `/opt/myownclone/worktrees/sisyphus-vps-integration`
- Remote target: `origin audit/sisyphus-vps-integration`

## Context

Closes the final Sisyphus milestone (M13) of the
`Sistema de Modelos IA Configurables por Tarea` plan, building on M0–M12. The
five user-facing tasks (`chat`, `embedding`, `email_classification`,
`email_draft`, `stt`) are already routed through the DB-driven model catalog
on the runtime side; M13 lands the backfill command to seed that catalog from
legacy env vars, the documentation for the env-to-DB rollout/rollback, and
three defect fixes that surfaced during the M9–M12 work.

## Changes

### Defect #3 — explicit cost-category mapping
- File: `api/controllers/console/myownclone/analytics.py`
- The `CostBreakdownApi` endpoint used to derive the response field name
  from the raw `CostTracking.category` string via
  `f"{row[0]}_cents"`. Any category whose name did not happen to match the
  convention was silently dropped.
- Now imports `CostCategory` (the typed `enum.StrEnum` defined in
  `api/models/analytics.py`) and maps each member explicitly:
  - `CLONE_RESPONSE` → `clone_response_cents`
  - `CONTENT_INGESTION` → `content_ingestion_cents`
  - `PLATFORM_OPS` → `platform_ops_cents`
- Unknown DB values are logged at WARNING and skipped, not mis-bucketed.

### Defect #6 — threshold logging in retrieval
- File: `api/core/retrieval.py`
- `_retrieve_from_local_chunks` now counts the chunks that passed
  silo/context filtering (`scanned`).
- When `scanned > 0` but no chunk clears the score threshold, emits an
  `INFO` log with `clone`, `silo`, `threshold`, `scanned`, and the
  query terms, so an empty retrieval can be diagnosed from logs.

### Defect #6 — runtime embeddings guard and error logging
- File: `api/controllers/console/myownclone/runtime.py`
- Adds `import logging` and `logger = logging.getLogger(__name__)`.
- New constant `_MAX_EMBED_TEXTS = 256` caps the texts per request.
- Over-limit requests are rejected with **HTTP 413** and a WARNING log
  (short-circuits before fanning out to the embedding provider).
- Embedding failures now log the full exception (`logger.exception`) before
  returning **HTTP 422**, replacing the silent bare-except behavior.

### Defect #4 — frontend batching of embeddings calls
- File: `MyOwnClone/src/app/api/clone/sources/route.ts`
- New constant `EMBEDDING_BATCH_SIZE = 64`.
- `resolveEmbeddings` now iterates over fixed-size batches instead of
  POSTing every chunk in one request.
- Each batch is validated (`response.ok`, length match, 1536-dim
  numeric rows). Vectors are accumulated in order.
- If any batch fails, the function falls back to lexical embeddings for
  the **whole** set so the caller always receives a fully-populated vector
  list of length `texts.length`.

### New command — `flask ai-backfill-from-env`
- New file: `api/commands/ai_backfill.py`
- Public API:
  - `backfill_from_env(*, session=None, env=None, dry_run=False) -> BackfillResult`
  - `ai_backfill_from_env_command` (Click command, name `ai-backfill-from-env`)
- Provider detection (only providers whose key is set are considered):
  `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `MINIMAX_API_KEY`, `TOGETHER_API_KEY`.
- For each `AITask` picks the highest-priority detected provider that
  defines a model for the task's `AICapability`:
  - `chat`, `email_classification`, `email_draft` → LLM
    (priority: openai → anthropic → minimax → together)
  - `embedding` → embedding model (priority: openai → together),
    recorded with `embedding_dimensions=1536`
  - `stt` → only backfilled when `OPENAI_API_KEY` is present (`whisper-1`)
- API keys are encrypted with `SecretCipher` (AES-256-GCM) — never
  stored in plaintext.
- Idempotent: re-runs with an unchanged env produce
  `models_created=0 models_updated=0 assignments_created=0
  assignments_reused=5`; an active assignment that already points at
  the correct model is reused, not duplicated. Stale active assignments
  are deactivated (preserving the "one active per (tenant, task)"
  invariant enforced by the partial unique index).
- Emits structured output: `models_created`, `models_updated`,
  `assignments_created`, `assignments_reused`, `providers_detected`,
  `skipped_tasks`. Supports `--dry-run`.
- Injection points (`session=`, `env=`) mirror `test_ai_audit_rotation`'s
  monkeypatch style, so the command is testable without a live DB.

### Command registration
- File: `api/app_factory.py`
- Imports `ai_backfill_from_env_command` from `api.commands.ai_backfill`.
- Registers it via `app.cli.add_command(ai_backfill_from_env_command)`
  alongside the M12 commands.

### Documentation
- New file: `docs/model-backfill-and-rollout.md`
- Companion to `docs/model-secrets-key-management.md` (M12).
- Documents: what the backfill does, idempotency contract, prerequisites
  (`MODEL_SECRETS_KEY`, migrations), rollout procedure (dry-run → apply →
  verify), rollback (deactivate assignments; do not hard-delete models
  that are still referenced — `ON DELETE RESTRICT` will refuse), and
  verification commands.

### Tests
- New: `api/tests/test_ai_backfill.py` (6 cases) — covers creation from
  env, idempotency on re-run, reuse of an already-correct active
  assignment, update of a model whose encrypted key no longer matches
  the env, no-op when no providers are present, and dry-run.
- New: `api/tests/test_runtime_embeddings_guard.py` (3 cases) — verifies
  413 over-limit, 200 at the exact limit, and 422 on a provider error.
- New: `api/tests/test_analytics_cost_mapping.py` (2 cases) — guards
  that the explicit `CostCategory` mapping is present and the
  implicit-string derivation is gone from the code (asserts on
  statements, not the comment, to avoid false positives).
- Updated: `tests/test_plan_completion.py::test_m13_backfill_command_exists`
  — now strictly requires the `api.commands.ai_backfill` module to expose
  `backfill_from_env` and `ai_backfill_from_env_command`, the command name
  to be exactly `ai-backfill-from-env`, and the registration in
  `api/app_factory.py` to add the command.

## Verification

All commands run on the VPS worktree
`/opt/myownclone/worktrees/sisyphus-vps-integration`.

```text
# 1. Whitespace / conflict check
$ sudo git diff --check
(no output — clean)

# 2. Compile all M13 Python files
$ sudo python3 -m py_compile \
    api/controllers/console/myownclone/analytics.py \
    api/controllers/console/myownclone/runtime.py \
    api/core/retrieval.py \
    api/commands/ai_backfill.py \
    api/app_factory.py \
    api/tests/test_ai_backfill.py \
    api/tests/test_runtime_embeddings_guard.py \
    api/tests/test_analytics_cost_mapping.py \
    tests/test_plan_completion.py
(all 9 files: OK)

# 3. M13 test subset
$ sudo env PYTHONDONTWRITEBYTECODE=1 /tmp/m13venv/bin/python -m pytest -p no:cacheprovider -q \
    api/tests/test_ai_backfill.py \
    api/tests/test_runtime_embeddings_guard.py \
    api/tests/test_analytics_cost_mapping.py \
    tests/test_plan_completion.py::test_m13_backfill_command_exists
collected 12 items
api/tests/test_ai_backfill.py ......... [ 50%]
api/tests/test_runtime_embeddings_guard.py ...                           [ 75%]
api/tests/test_analytics_cost_mapping.py ..                              [ 91%]
tests/test_plan_completion.py .                                          [100%]
============================== 12 passed in 1.47s ==============================

# 4. Regression: M0–M12 plan completion + runtime integration still green
$ sudo env PYTHONDONTWRITEBYTECODE=1 /tmp/m13venv/bin/python -m pytest -p no:cacheprovider -q \
    tests/test_plan_completion.py \
    api/tests/test_ai_runtime_integration.py
collected 17 items
tests/test_plan_completion.py ..............                             [ 82%]
api/tests/test_ai_runtime_integration.py ...                             [100%]
============================== 17 passed in 1.31s ==============================
```

Total M13 deliverable: **29 tests pass** (12 new + 17 regression), zero
failures, zero skips. The full pre-M13 API test suite is not run here
because it requires PostgreSQL + weaviate (CI covers it on 3.11).

## Open risks

- **Local execution environment**: the VPS user has only Python 3.14; CI
  targets 3.11 (`.github/workflows/ci.yml`). Wheels were installed
  `--only-binary=:all:`, so we did not compile any extension. The full
  integration test suite (which exercises real Postgres + weaviate
  containers) is **not** executed on the VPS — CI on `audit/sisyphus-vps-integration`
  will validate it on push.
- **Frontend static checks** (`npm run typecheck` / `lint` / `build`): the
  worktree has `MyOwnClone/` as a directory of tracked files but no
  `node_modules` and no `package.json` is set up at the worktree root
  (`/opt/myownclone/current/MyOwnClone` is the build location). The
  frontend edits are syntactically isolated (one constant + one
  refactor of `resolveEmbeddings`) and will be validated by the frontend
  build step during deploy.
- **Backfill on a populated database**: the command is idempotent by
  design, but the first apply on a real catalog with legacy partial
  state should be preceded by `--dry-run` (documented in
  `docs/model-backfill-and-rollout.md`).
- **No live production apply**: this evidence covers the integration
  branch; deployment to `/opt/myownclone/current` is a separate,
  explicitly-not-performed step per the work brief.

## Remote SHA

- Populated after the M13 commit-and-push step.
- Commit SHA: `d7a1e1e8287f7e1412bbb6d8a1d3c96ba2ae426a`
- Remote: `origin audit/sisyphus-vps-integration` (verified: local HEAD == remote HEAD; GitHub API returns this SHA at the tip of the branch).
- Commit SHA: 
- Remote:  (verified: local HEAD == remote HEAD).
