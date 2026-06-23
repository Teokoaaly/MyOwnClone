# M4a - ProviderAdapter base and ProviderRegistry

## Context
- Date: 2026-06-23
- Branch: `audit/sisyphus-vps-integration`
- Base SHA: `1733c41`
- Goal: extract the provider-facing contracts out of `api/core/model_manager.py`
  so `M3` can resolve adapters without circular imports or concrete provider
  coupling.

## Changes

- Added `api/core/providers/base.py` with:
  - `ModelType`
  - `GenerationParams`
  - `ModelUsage`
  - `ModelReply`
  - `TestResult`
  - abstract `ProviderAdapter`
- Added `api/core/providers/registry.py` with:
  - singleton-backed `ProviderRegistry`
  - `DuplicateProviderError`
  - `UnknownProviderError`
- Added `api/core/providers/__init__.py` re-exports for the new provider layer.
- Updated `api/core/model_manager.py` to import and re-export the moved public
  types for backward compatibility.
- Added `api/tests/test_provider_registry.py` covering:
  - adapter `supports()` behavior
  - singleton registry lookup
  - register/get/has/names flow
  - duplicate registration error
  - unknown provider error
  - import smoke for `api.core.model_manager.GenerationParams`

## Verification

- `git diff --check`: passed
- `pytest -v api/tests/test_provider_registry.py`: 6 passed
- `pytest -v api/tests/test_model_manager_config.py`: 4 passed
- import smoke:
  - `from api.core.model_manager import GenerationParams`
  - instantiated successfully

## Open risks

- `ProviderRegistry` is intentionally minimal in `M4a`; it does not yet resolve
  by tenant, task, cache, or encrypted credentials. That arrives in `M3`/`M4b`.
- Concrete adapters are still the legacy in-file functions in
  `api/core/model_manager.py` until `M4b` ports them behind `ProviderAdapter`.

## Remote SHA

- Commit: `18fc1b5`
