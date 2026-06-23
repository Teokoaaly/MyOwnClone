# M7 - ModelManager task invocation refactor

## Context
- Date: 2026-06-23
- Branch: `audit/sisyphus-vps-integration`
- Base SHA: `df781e4`
- Goal: route `ModelManager` through the configurable runtime building blocks
  while preserving the legacy public surface used by existing controllers.

## Changes

- Refactored `api/core/model_manager.py` to add:
  - `ModelManager.__init__(registry, retry_client, token_budgeter)`
  - `ModelManager.invoke_for_task(...)`
  - `ModelManager.invoke_for_task_stream(...)`
  - `_provider_adapter_for(...)`
  - `_build_generation_params(...)`
  - `_record_invocation(...)`
- Legacy path preserved:
  - `invoke_non_streaming(...)` now delegates to `invoke_for_task(...)`
  - `get_default_model_instance(...)` still returns a graphon-compatible object
    exposing `invoke_llm` and `invoke_llm_stream`
- Runtime now composes:
  - `ModelRegistry`
  - `RetryClient`
  - `TokenBudgeter`
  - provider adapters from `M4b`
- Added `AIInvocation` persistence for:
  - successful non-streaming calls
  - failed non-streaming calls
  - successful streaming calls with missing usage recorded as zero plus
    `error_message="stream_usage_missing"`
  - failed streaming calls
- Added tests:
  - `api/tests/test_model_manager_registry.py`
  - `api/tests/test_streaming_cost_tracking.py`

## Verification

- `git diff --check`: passed
- runtime test:
  - `pytest -v api/tests/test_model_manager_registry.py`: 2 passed
  - `pytest -v api/tests/test_model_manager_config.py tests/test_plan_completion.py::test_m7_invoke_for_task_exists`: 5 passed
- streaming cost tracking test:
  - `pytest -v api/tests/test_streaming_cost_tracking.py`: 2 passed
- broader regression:
  - `pytest -v api/tests/test_retry_client.py api/tests/test_token_budget.py api/tests/test_provider_registry.py api/tests/test_model_registry.py api/tests/test_provider_adapters.py api/tests/test_model_manager_registry.py api/tests/test_streaming_cost_tracking.py api/tests/test_model_manager_config.py`: 41 passed

## Open risks

- Existing controllers are still calling the legacy methods, so `M7` improves
  the engine first but does not yet rework every caller to pass explicit tasks.
- Streaming usage remains provider-limited; when adapters cannot produce usage,
  invocation rows intentionally persist zeros plus a diagnostic marker.
- `_record_invocation(...)` currently commits per call. That is correct for
  audit durability, but may deserve batching or an outbox later if throughput
  becomes significant.

## Remote SHA

- Commit: `3d1fd19`
