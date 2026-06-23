# M5 - RetryClient

## Context
- Date: 2026-06-23
- Branch: `audit/sisyphus-vps-integration`
- Base SHA: `42dbee1`
- Goal: add bounded retries, ordered failover, and per-candidate circuit
  breaking before `ModelManager` is refactored to use the new runtime path.

## Changes

- Added `api/core/retry_client.py` with:
  - `RetryCandidate`
  - `CircuitStatus`
  - `RetryClient`
- Implemented:
  - exponential backoff per candidate
  - ordered failover by priority
  - circuit open after repeated failures
  - half-open retry window after 30 seconds
  - circuit close on recovery
  - original exception preserved via `raise ... from last_error`
- Added compatibility/support fixes discovered while wiring M5:
  - `ModelRegistry.get_model_for_task(...)` alias for smoke compatibility
  - provider adapter catalog exposure via `ProviderRegistry._adapters`
- Added `api/tests/test_retry_client.py` covering:
  - backoff schedule
  - failover ordering
  - circuit opening
  - half-open recovery
  - final failure after all candidates fail
  - skipping still-open circuits

## Verification

- `git diff --check`: passed
- `pytest -v api/tests/test_retry_client.py`: 6 passed
- `pytest -v tests/test_plan_completion.py::test_m3_model_registry_exists tests/test_plan_completion.py::test_m4b_six_provider_adapters_registered tests/test_plan_completion.py::test_m5_retry_client_exists`: 3 passed
- `pytest -v api/tests/test_provider_registry.py api/tests/test_model_registry.py api/tests/test_provider_adapters.py api/tests/test_model_manager_config.py`: 25 passed
- retry/failover validation:
  - backoff observed as `base * 2^(attempt-1)`
  - lower-priority candidate invoked only after higher-priority failure
  - half-open transitions back to closed on success

## Open risks

- `RetryClient` is not yet wired into live model invocation; that handoff lands
  in `M7`.
- Circuits are process-local in-memory state. That is fine for the current app
  shape, but it is not shared across workers or instances.
- Backoff is synchronous; if later runtime paths need async support, this should
  become a second implementation instead of overloading this one.

## Remote SHA

- Commit: `8744ab0`
