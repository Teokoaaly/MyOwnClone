# M6 - TokenBudgeter

## Context
- Date: 2026-06-23
- Branch: `audit/sisyphus-vps-integration`
- Base SHA: `01c2d93`
- Goal: enforce prompt budget boundaries and embedding dimension contracts
  before runtime integration starts routing through the configurable model layer.

## Changes

- Added `api/core/token_budget.py` with:
  - `TokenBudgeter`
  - `BudgetResult`
  - `TokenBudgetError`
  - `EmbeddingDimensionError`
  - `EXPECTED_EMBEDDING_DIMENSIONS = 1536`
- Implemented:
  - rough token estimation based on configurable chars/token
  - available prompt token computation from `max_input_tokens` minus reserved
    completion budget
  - truncation path with explicit warning log
  - rejection path for oversized non-truncatable input
  - embedding dimension validation for models that must expose `1536`
- Added `api/tests/test_token_budget.py` covering:
  - within-budget flow
  - truncation flow
  - oversized rejection
  - override max token budget
  - embedding dimension accept/reject cases

## Verification

- `git diff --check`: passed
- `pytest -v api/tests/test_token_budget.py`: 6 passed
- `pytest -v tests/test_plan_completion.py::test_m6_token_budgeter_exists`: 1 passed
- `pytest -v api/tests/test_retry_client.py api/tests/test_provider_registry.py api/tests/test_model_registry.py api/tests/test_provider_adapters.py api/tests/test_model_manager_config.py`: 31 passed
- embedding dimension guard validation:
  - `1536` accepted
  - `768` rejected with `EmbeddingDimensionError`

## Open risks

- Token estimation is intentionally coarse in `M6`; a provider-specific
  tokenizer can replace or augment it later without changing the calling shape.
- API-facing HTTP 422 mapping is not wired yet; that belongs where `M7`/`M9`
  start consuming `TokenBudgeter`.
- Truncation policy is synchronous and text-only for now; multimodal inputs are
  out of scope for this milestone.

## Remote SHA

- Commit: `4388535`
