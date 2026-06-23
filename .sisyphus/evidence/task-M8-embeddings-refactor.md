# M8 - Embeddings registry refactor

## Context
- Date: 2026-06-23
- Branch: `audit/sisyphus-vps-integration`
- Base SHA: `5baa1bc`
- Goal: add an embedding service that resolves models through `ModelRegistry`,
  preserves batching, and enforces the `1536` dimension contract.

## Changes

- Added `api/core/embeddings.py` with `EmbeddingService`.
- Added `_OPENAI_BATCH_SIZE = 64` and preserved batching across large input
  lists.
- `EmbeddingService.embed_texts(...)` now accepts an optional `model` argument
  and falls back to `ModelRegistry.get_model_for_task(..., task=AITask.EMBEDDING)`
  when no model is passed.
- Enforced `embedding_dimensions == 1536` via
  `TokenBudgeter.validate_embedding_model(...)`.
- Restricted M8 embedding execution to OpenAI-compatible providers for now,
  with explicit errors for unsupported providers.
- Added `api/tests/test_embeddings_registry.py` for provided-model flow,
  registry flow, batching, dimension mismatch, and unsupported provider
  handling.

## Verification

- `git diff --check`: passed
- embeddings registry test:
  - `pytest -v api/tests/test_embeddings_registry.py` -> 5 passed
- batching regression check:
  - `pytest -v tests/test_plan_completion.py::test_m8_embed_texts_accepts_model api/tests/test_token_budget.py api/tests/test_model_registry.py` -> 13 passed
- embedding dimension guard validation:
  - `1536` accepted
  - non-`1536` rejected
  - batching preserved at `64 + remainder`

## Open risks

- Current retrieval still uses lexical/local embeddings; this milestone adds
  the service layer first and does not yet rewire every ingestion/retrieval
  path.
- Only OpenAI-compatible embedding providers are supported in M8.
- API-facing `422` translation remains for the next integration layer to wire.

## Remote SHA

- Commit: `0dc1abc`
