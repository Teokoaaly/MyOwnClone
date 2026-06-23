# M3 - ModelRegistry

## Context
- Date: 2026-06-23
- Branch: `audit/sisyphus-vps-integration`
- Base SHA: `a7a19df`
- Goal: resolve the active model for each `(tenant, task)` with DB-first routing,
  60s cache, invalidation, and a safe fallback to legacy env configuration.

## Changes

- Added `api/core/model_registry.py` with:
  - `ResolvedModelConfig`
  - `ModelRegistry`
  - `_CacheEntry`
  - `ModelRegistryError`
- Implemented DB-first resolution order:
  - tenant-specific active assignment first
  - global active assignment second
- Implemented 60-second cache with explicit `invalidate()` support.
- Implemented stale-cache fallback on DB exceptions.
- Implemented legacy env fallback for current standalone providers:
  - OpenAI / OpenAI-compatible base URL
  - Anthropic
  - MiniMax
  - Together
- Decrypts DB-stored provider keys via `SecretCipher.decrypt(...)` so the
  resolved config is ready for the adapter layer in `M4b`.
- Added `api/tests/test_model_registry.py` covering:
  - tenant-specific precedence
  - global fallback
  - cache reuse
  - invalidation and hot-swap for new requests
  - stale-cache fallback on DB error
  - legacy env fallback
  - hard error when nothing is configured

## Verification

- `git diff --check`: passed
- `pytest -v api/tests/test_model_registry.py`: 6 passed
- `pytest -v api/tests/test_provider_registry.py api/tests/test_model_manager_config.py`: 10 passed
- cache/fallback validation:
  - cached result reused within TTL
  - `invalidate(tenant_id=..., task=...)` forces a fresh DB load
  - expired cache is reused only when DB resolution raises

## Open risks

- `ModelRegistry` is not wired into `ModelManager` yet; that integration lands
  in `M7` after concrete adapters and retry/budget layers exist.
- DB capability mismatch currently skips the offending row and falls through;
  `M9` admin APIs should prevent invalid assignments from being created.
- The default registry singleton is not introduced yet; callers instantiate
  `ModelRegistry` directly for now.

## Remote SHA

- Commit: `5a9f076`
