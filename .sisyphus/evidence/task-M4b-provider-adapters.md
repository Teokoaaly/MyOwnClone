# M4b - Concrete provider adapters

## Context
- Date: 2026-06-23
- Branch: `audit/sisyphus-vps-integration`
- Base SHA: `6aefc30`
- Goal: port the six supported providers behind `ProviderAdapter` while keeping
  the existing `ModelManager` runtime intact until the later refactor milestone.

## Changes

- Extended shared provider contracts:
  - moved `ModelInvocationError` into `api/core/providers/base.py`
  - added `latency_ms` to `ModelReply`
- Kept backward compatibility by re-exporting provider-layer symbols from
  `api/core/model_manager.py`.
- Added concrete adapters:
  - `api/core/providers/openai.py`
  - `api/core/providers/anthropic.py`
  - `api/core/providers/openai_compatible.py`
  - `api/core/providers/minimax.py`
  - `api/core/providers/together.py`
  - `api/core/providers/local.py`
- Adapter behavior normalized:
  - shared `ModelReply` output
  - shared `ModelUsage` mapping
  - `latency_ms` measurement
  - provider exceptions wrapped as `ModelInvocationError`
  - `test_connection()` returns `TestResult`
- New code consumes provider credentials from resolved config (`ResolvedModelConfig`)
  instead of reading provider env vars directly.
- Added `api/tests/test_provider_adapters.py` with mocked coverage for:
  - success path
  - missing key handling
  - provider error wrapping
  - usage normalization
  - base URL defaults for MiniMax, Together, and Local

## Verification

- `git diff --check`: passed
- `pytest -v api/tests/test_provider_adapters.py`: 9 passed
- `pytest -v api/tests/test_provider_registry.py api/tests/test_model_registry.py api/tests/test_model_manager_config.py`: 16 passed
- provider mock validation:
  - OpenAI usage normalized to `ModelUsage`
  - Anthropic usage normalized to `ModelUsage`
  - provider exceptions surfaced as `ModelInvocationError`
  - compatibility adapters fill default base URLs without reading env

## Open risks

- `ModelManager` still dispatches through legacy in-file functions; `M7` will
  switch runtime invocation onto these adapters.
- `test_connection()` is intentionally lightweight and mock-driven here; `M9`
  can decide the exact admin-facing semantics.
- The `local` adapter assumes an OpenAI-compatible endpoint at
  `http://127.0.0.1:11434/v1`; if the project standardizes on another local
  runtime later, only this adapter should need adjustment.

## Remote SHA

- Commit: `9030755`
