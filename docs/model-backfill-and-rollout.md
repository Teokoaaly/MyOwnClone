# AI Models — env-to-DB backfill and rollout (M13)

This document describes how to migrate an existing MyOwnClone deployment from
legacy environment-variable provider selection to the DB-driven
`AIModel` / `AIModelAssignment` catalog (M1–M12), and how to roll the change
out and back safely.

It is the final operational companion to
`docs/model-secrets-key-management.md` (M12, master key + rotation).

## What the backfill does

`flask ai-backfill-from-env` reads the legacy provider env vars and materializes
them into the catalog as **global** rows (`tenant_id IS NULL`):

- Detects providers from these env vars (only those that are set):
  - `OPENAI_API_KEY`   → `openai`
  - `ANTHROPIC_API_KEY` → `anthropic`
  - `MINIMAX_API_KEY`  → `minimax`
  - `TOGETHER_API_KEY` → `together`
- Creates/updates one `AIModel` per `(provider, model_id)` with the API key
  **encrypted** via `SecretCipher` (AES-256-GCM — never stored in plaintext).
- Creates one active `AIModelAssignment` per task, choosing the
  highest-priority detected provider that can serve the task's capability:
  - `chat`, `email_classification`, `email_draft` → an LLM model
    (priority: openai → anthropic → minimax → together)
  - `embedding` → an embedding model (priority: openai → together),
    recorded with `embedding_dimensions=1536`
  - `stt` → only backfilled when `OPENAI_API_KEY` is present (`whisper-1`)

Tasks with no available provider key are **skipped** (reported on stderr), not
errored.

## Idempotency

The command is safe to run repeatedly:

- A model that already exists for a `(provider, model_id)` is **updated only**
  when something actually changed (a new capability, the embedding dimension,
  or a changed API key — detected by decrypting the stored blob and comparing
  to the environment value).
- An active assignment that already points at the correct model is **reused**,
  not duplicated. If it points at a different model, the stale assignment is
  deactivated and a new active one is created (preserving the "one active
  assignment per (tenant, task)" invariant).
- A re-run with an unchanged environment produces
  `models_created=0 models_updated=0 assignments_created=0`.

## Prerequisites

1. `MODEL_SECRETS_KEY` is set and valid (see M12 doc). Without it the backfill
   cannot encrypt provider keys and will fail fast.
2. The `ai_models`, `ai_model_assignments` tables exist (Alembic migrations
   from M1 applied).
3. The legacy provider env vars are present in the API environment.

## Rollout

```bash
# 1. Dry-run first — see exactly what would change, write nothing.
flask ai-backfill-from-env --dry-run

# 2. Apply.
flask ai-backfill-from-env
# Example output:
# [OK] ai-backfill-from-env applied: providers=openai models_created=3 \
#      models_updated=0 assignments_created=5 assignments_reused=0

# 3. Verify the assignments resolve as expected (admin API / UI).
#    /console/api/myownclone/ai-models  and  /admin/ia-modelos
```

After the catalog is populated, runtime task routing (M7/M8/M10) resolves the
model from the DB; the legacy env vars become a fallback only.

## Rollback

The backfill writes data, not schema, so rollback is a data operation:

- To revert to env-driven behavior, deactivate the backfilled assignments
  (`is_active=False`) — the runtime falls back to env-based selection when no
  active assignment exists for a task. Do **not** hard-delete `AIModel` rows
  that assignments still reference (`ON DELETE RESTRICT`).
- Master-key rollback and key rotation are covered in
  `docs/model-secrets-key-management.md`.

## Verification commands

```bash
# CLI command is registered:
flask --help | grep ai-backfill-from-env

# Dry-run shows detected providers and intended changes:
flask ai-backfill-from-env --dry-run

# Idempotency: a second apply reports 0 created / 0 updated:
flask ai-backfill-from-env && flask ai-backfill-from-env
```
