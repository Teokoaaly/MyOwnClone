# TASKS.md - Sisyphus M3-M13 execution checklist

This document is the operational checklist for continuing the configurable AI
models work after M0-M2. It complements `.sisyphus/progress.json` and
`.sisyphus/plans/ai-models-configurable.md`; it does not replace the tracker.

## Global integration rules

- Working branch: `audit/sisyphus-vps-integration`.
- Production compatibility base: `origin/audit/vps-sync-and-docs`.
- Do not modify the live VPS checkout or the uncommitted VPS i18n changes in
  `src/i18n/en.json` and `src/i18n/es.json`.
- One task = one commit = one push.
- Do not deploy anything until backend/frontend rollback scripts are corrected
  and verified.
- Do not merge `origin/master` into this integration flow unless explicitly
  approved for a separate production compatibility pass.
- Each task must update `.sisyphus/progress.json` and add evidence under
  `.sisyphus/evidence/`.
- Every task must run `git diff --check` before commit.

## Preflight: integration branch and rollback guard

Objective: create the safe integration lane and make deployment rollback usable
before any functional AI-model changes reach the VPS.

Dependencies:
- SSH access to the VPS is available.
- `origin/audit/vps-sync-and-docs` is fetchable.
- `origin/feature/sisyphus-m1-data-layer` contains M0-M2.

Subtasks:
- Create `audit/sisyphus-vps-integration` from
  `origin/audit/vps-sync-and-docs`.
- Integrate M0-M2 from `origin/feature/sisyphus-m1-data-layer` with a controlled
  cherry-pick or merge outside the live VPS checkout.
- Fix rollback variable expansion in `ops/deploy-backend.sh` and
  `ops/deploy-frontend.sh`.
- Document the rollback verification command and the release SHA recorded by
  each deploy.

Expected files:
- `ops/deploy-backend.sh`
- `ops/deploy-frontend.sh`
- `.sisyphus/progress.json`
- `.sisyphus/evidence/task-preflight-rollback.md`

Required tests:
- `git diff --check`
- Shell syntax check for both deploy scripts.
- Dry inspection proving rollback restores the previous `current` symlink using
  the real previous release path.

Evidence:
- `.sisyphus/evidence/task-preflight-rollback.md`

Suggested commit:
- `fix(ops): prepare safe rollback for Sisyphus VPS integration`

Next milestone gate:
- Rollback path is verified well enough to be used before backend deployment.

## M4a - ProviderAdapter base and ProviderRegistry

Objective: define the stable provider interface that M3 and M4b will use.

Dependencies:
- M1 models exist.
- M2 crypto exists.
- Preflight rollback guard is done.

Subtasks:
- Create `api/core/providers/` as a package.
- Add `ProviderAdapter`, `ProviderRegistry`, `GenerationParams`, `ModelReply`,
  `ModelUsage`, and `TestResult`.
- Re-export moved types from `api/core/model_manager.py` for backward
  compatibility.
- Add tests for abstract adapter behavior, singleton registry lookup, duplicate
  registration, and unknown provider errors.

Expected files:
- `api/core/providers/base.py`
- `api/core/providers/registry.py`
- `api/core/providers/__init__.py`
- `api/core/model_manager.py`
- `api/tests/test_provider_registry.py`

Required tests:
- `git diff --check`
- `pytest -v api/tests/test_provider_registry.py`
- Import smoke for `api.core.model_manager.GenerationParams`

Evidence:
- `.sisyphus/evidence/task-M4a-providers-base.md`

Suggested commit:
- `feat(providers): M4a provider adapter interface and registry`

Next milestone gate:
- M3 can resolve a model and request an adapter without circular imports.

## M3 - ModelRegistry

Objective: resolve the active model for a tenant/task with caching, invalidation,
and safe fallback behavior.

Dependencies:
- M4a complete.
- M1/M2 integrated into the VPS integration branch.

Subtasks:
- Add `api/core/model_registry.py`.
- Resolve by tenant and `AITask`, preferring tenant-specific active assignment,
  then global active assignment.
- Cache resolved model data for 60 seconds.
- Add explicit invalidation for tenant/task and global cache.
- Implement fallback chain: DB result, then valid cache, then legacy env vars,
  then clear error.
- Ensure hot-swap affects new requests only; in-flight requests keep the model
  resolved at request start.
- Decrypt API keys through `SecretCipher`; do not expose plaintext outside the
  invocation boundary.

Expected files:
- `api/core/model_registry.py`
- `api/tests/test_model_registry.py`
- `.sisyphus/progress.json`

Required tests:
- `git diff --check`
- `pytest -v api/tests/test_model_registry.py`
- Tests for tenant override, global fallback, TTL behavior, invalidation, DB
  failure with cached value, and legacy env fallback.

Evidence:
- `.sisyphus/evidence/task-M3-model-registry.md`

Suggested commit:
- `feat(ai): M3 model registry with cache and fallback`

Next milestone gate:
- Runtime code can ask for a task model without reading provider env vars
  directly, except through controlled legacy fallback.

## M4b - Concrete provider adapters

Objective: implement the six supported providers behind the M4a interface.

Dependencies:
- M4a complete.
- M3 complete or in parallel with stable adapter interface.

Subtasks:
- Implement adapters for `openai`, `anthropic`, `minimax`, `together`,
  `openai_compatible`, and `local`.
- Normalize response text, usage, latency, and provider errors into shared
  return types.
- Add `test_connection` for each provider.
- Ensure API keys are consumed from decrypted `AIModel` data, not from direct
  env reads in new code.
- Keep provider names based on `AIProvider` enum values.

Expected files:
- `api/core/providers/openai.py`
- `api/core/providers/anthropic.py`
- `api/core/providers/minimax.py`
- `api/core/providers/together.py`
- `api/core/providers/openai_compatible.py`
- `api/core/providers/local.py`
- `api/tests/test_provider_adapters.py`

Required tests:
- `git diff --check`
- `pytest -v api/tests/test_provider_adapters.py`
- Mocked success, provider error, missing key, and usage-normalization cases.

Evidence:
- `.sisyphus/evidence/task-M4b-provider-adapters.md`

Suggested commit:
- `feat(providers): M4b add concrete AI provider adapters`

Next milestone gate:
- M5/M7 can invoke all supported providers through one adapter interface.

## M5 - RetryClient

Objective: add resilient invocation behavior without hiding persistent provider
failures.

Dependencies:
- M4b complete.

Subtasks:
- Add `api/core/retry_client.py`.
- Implement exponential backoff with bounded retries.
- Add failover across eligible models ordered by priority.
- Add circuit breaker states: closed, open, half-open.
- Open circuit after repeated provider failures.
- Move to half-open after 30 seconds; success closes, failure reopens.
- Preserve original error context for logging and API responses.

Expected files:
- `api/core/retry_client.py`
- `api/tests/test_retry_client.py`

Required tests:
- `git diff --check`
- `pytest -v api/tests/test_retry_client.py`
- Tests for backoff, failover ordering, circuit open, half-open recovery, and
  final failure after all candidates fail.

Evidence:
- `.sisyphus/evidence/task-M5-retry-client.md`

Suggested commit:
- `feat(ai): M5 retry client with failover and circuit breaker`

Next milestone gate:
- M7 can call providers through retry/failover instead of direct dispatch.

## M6 - TokenBudgeter

Objective: enforce model/task token budgets and embedding dimension contracts.

Dependencies:
- M1 model schema complete.
- M4b provider metadata available.

Subtasks:
- Add `api/core/token_budget.py`.
- Compute available prompt budget from model defaults and task overrides.
- Truncate or reject inputs according to task policy.
- Reject embedding models whose `embedding_dimensions` is not `1536`.
- Return HTTP 422 from API-facing paths for invalid embedding dimensions.
- Add clear logs when truncation happens.

Expected files:
- `api/core/token_budget.py`
- `api/tests/test_token_budget.py`

Required tests:
- `git diff --check`
- `pytest -v api/tests/test_token_budget.py`
- Tests for normal budget, truncation, oversized input rejection, and embedding
  dimension mismatch.

Evidence:
- `.sisyphus/evidence/task-M6-token-budget.md`

Suggested commit:
- `feat(ai): M6 token budget and embedding dimension guard`

Next milestone gate:
- M7/M8 can enforce limits before provider calls.

## M7 - ModelManager task invocation refactor

Objective: route LLM calls through the registry and record real usage, including
streaming usage.

Dependencies:
- M3, M4b, M5, and M6 complete.

Subtasks:
- Add `ModelManager.invoke_for_task`.
- Route non-streaming and streaming calls through `ModelRegistry`,
  `RetryClient`, provider adapters, and `TokenBudgeter`.
- Persist `AIInvocation` rows for success and failure.
- Preserve legacy public methods where callers still depend on them.
- Fix streaming cost tracking so usage is persisted after stream completion.
- If provider usage is missing in stream, record cost as zero with a diagnostic
  flag or error message.

Expected files:
- `api/core/model_manager.py`
- `api/tests/test_model_manager_registry.py`
- `api/tests/test_streaming_cost_tracking.py`

Required tests:
- `git diff --check`
- `pytest -v api/tests/test_model_manager_registry.py`
- `pytest -v api/tests/test_streaming_cost_tracking.py`
- Regression test for existing legacy invocation path.

Evidence:
- `.sisyphus/evidence/task-M7-model-manager-refactor.md`

Suggested commit:
- `feat(ai): M7 route model manager through task registry`

Next milestone gate:
- Chat-style calls can use task assignments and record invocation usage.

## M8 - Embeddings registry refactor

Objective: route embedding generation through the configurable model system while
preserving existing batching behavior.

Dependencies:
- M3, M4b, and M6 complete.

Subtasks:
- Refactor `EmbeddingService.embed_texts` to accept an optional resolved
  `AIModel`.
- Resolve embedding task model through `ModelRegistry` when no model is passed.
- Preserve current batching behavior and `_OPENAI_BATCH_SIZE`.
- Enforce `embedding_dimensions == 1536`.
- Ensure the public embed endpoint chunks or rejects safely before invoking the
  embedding service.

Expected files:
- `api/core/embeddings.py`
- Public embed controller that currently calls `embed_texts`
- `api/tests/test_embeddings_registry.py`

Required tests:
- `git diff --check`
- `pytest -v api/tests/test_embeddings_registry.py`
- Test that existing batching still works.
- Test that dimension mismatch returns/raises 422 in API-facing path.

Evidence:
- `.sisyphus/evidence/task-M8-embeddings-refactor.md`

Suggested commit:
- `feat(ai): M8 route embeddings through model registry`

Next milestone gate:
- Ingestion and public embedding paths can use assigned embedding models.

## M9 - Admin AI models REST API

Objective: expose admin endpoints for model CRUD, assignments, playground, and
basic cost/audit data.

Dependencies:
- M3, M4b, M7, and M8 complete.

Subtasks:
- Add admin blueprint/controller for AI models.
- Implement endpoints for listing models, creating/updating models, disabling
  models, reading/updating task assignments, testing provider connection, and
  playground invocation.
- Validate admin role and tenant ownership on every route.
- Encrypt API keys on write and never return plaintext keys.
- Invalidate `ModelRegistry` cache after assignment or model changes.

Expected files:
- `api/controllers/console/myownclone/ai_models.py`
- Blueprint registration file used by console routes
- `api/tests/test_ai_models_endpoints.py`

Required tests:
- `git diff --check`
- `pytest -v api/tests/test_ai_models_endpoints.py`
- Tests for admin auth, tenant isolation, plaintext key redaction, assignment
  invalidation, playground success, and invalid payloads.

Evidence:
- `.sisyphus/evidence/task-M9-admin-api.md`

Suggested commit:
- `feat(admin): M9 add AI models management API`

Next milestone gate:
- Frontend UI can manage models without calling internal services directly.

## M10 - Runtime integration points

Objective: connect the configurable model system to the five runtime tasks.

Dependencies:
- M7, M8, and M9 complete.

Subtasks:
- Route chat/public clone responses through `invoke_for_task(chat)`.
- Route ingestion and embeddings through the embedding task assignment.
- Route email classification through `email_classification`.
- Route email draft generation through `email_draft`.
- Add Flask STT endpoint and change the Next.js STT route to proxy to Flask,
  removing direct `OPENAI_API_KEY` usage from frontend runtime.
- Keep legacy env fallback for deployments that have not run backfill yet.

Expected files:
- Existing chat/public clone controller
- Existing ingestion/email/STT paths
- `MyOwnClone/src/app/api/stt/route.ts`
- `api/tests/test_ai_runtime_integration.py`

Required tests:
- `git diff --check`
- `pytest -v api/tests/test_ai_runtime_integration.py`
- Frontend typecheck for STT proxy changes.
- Smoke tests for each task resolving the expected assignment.

Evidence:
- `.sisyphus/evidence/task-M10-integration.md`

Suggested commit:
- `feat(ai): M10 integrate task-based model routing`

Next milestone gate:
- All runtime AI calls can be served through assignments with legacy fallback.

## M11 - Admin UI for AI models

Objective: provide an admin screen for managing AI models, task assignments,
playground calls, and cost visualization.

Dependencies:
- M9 complete.
- M10 stable enough for playground calls.

Subtasks:
- Add `/admin/ia-modelos`.
- Add model create/edit form with provider, model id, base URL, capabilities,
  priority, defaults, active status, and API key write-only input.
- Add task assignment cards for the five configured tasks.
- Add playground panel using the M9 playground endpoint.
- Add cost chart using available cost/audit endpoint data.
- Follow existing admin shell, i18n, fetch, and auth patterns.

Expected files:
- `MyOwnClone/src/app/admin/ia-modelos/page.tsx`
- Admin AI model UI components
- Any required i18n keys for the new screen

Required tests:
- `git diff --check`
- `cd MyOwnClone && npm run typecheck`
- `cd MyOwnClone && npm run lint`
- `cd MyOwnClone && npm run build`
- Playwright check for desktop and mobile rendering of `/admin/ia-modelos`.

Evidence:
- `.sisyphus/evidence/task-M11-admin-ui.md`

Suggested commit:
- `feat(admin): M11 add AI models admin UI`

Next milestone gate:
- Admin users can manage assignments and run playground checks from the UI.

## M12 - Audit rollup and key rotation

Objective: add operational audit support, daily cost rollups, and safe double-key
rotation for encrypted model secrets.

Dependencies:
- M7 and M9 complete.

Subtasks:
- Add `cost_daily_rollup` storage or materialized view according to existing DB
  conventions.
- Add migration and refresh/update mechanism for rollup data.
- Add `flask rotate-secrets-key` supporting old key + new key re-encryption.
- Document that losing the master key makes stored provider keys
  unrecoverable.
- Ensure rotation does not break in-flight requests that already resolved a
  model.

Expected files:
- New Alembic migration for rollup if needed
- `api/commands/crypto.py`
- `api/tests/test_ai_audit_rotation.py`
- Technical documentation section for key management

Required tests:
- `git diff --check`
- `pytest -v api/tests/test_ai_audit_rotation.py`
- CLI dry run or test DB rotation with old/new keys.
- Query check proving rollup returns expected daily totals.

Evidence:
- `.sisyphus/evidence/task-M12-audit-rotation.md`

Suggested commit:
- `feat(ai): M12 add cost rollup and model secret rotation`

Next milestone gate:
- Production can rotate keys and inspect cost trends without manual SQL.

## M13 - Defects, backfill, docs, and final verification

Objective: close known defects, provide migration from env-based config, and
finish the end-to-end rollout documentation.

Dependencies:
- M9, M10, M11, and M12 complete.

Subtasks:
- Fix defect #3: remove hard-coded cost category/task literals where enum or
  task constants should be used.
- Fix defect #4: ensure public embedding endpoint batches/chunks safely before
  calling `embed_texts`.
- Fix defect #6: add threshold/error logging required by the plan.
- Add `flask ai-backfill-from-env` to create/update `AIModel` and
  `AIModelAssignment` rows from legacy env vars.
- Make backfill idempotent and safe to re-run.
- Add final migration/operations documentation for moving from env vars to
  DB-driven assignments.
- Run final verification and update all evidence/progress fields.

Expected files:
- `api/commands/ai_backfill.py`
- Existing files touched by defects #3/#4/#6
- Final docs section for rollout and rollback
- `.sisyphus/evidence/task-M13-defects-backfill-docs.md`

Required tests:
- `git diff --check`
- Backfill command test proving idempotency.
- Regression tests for defects #3/#4/#6.
- Backend test suite or documented stable subset.
- Frontend typecheck/lint/build if UI docs or routes changed.
- Final VPS smoke only after explicit deployment approval.

Evidence:
- `.sisyphus/evidence/task-M13-defects-backfill-docs.md`

Suggested commit:
- `feat(ai): M13 add backfill, final fixes, and rollout docs`

Next milestone gate:
- M3-M13 are complete, documented, tested, and ready for controlled VPS
  deployment.
