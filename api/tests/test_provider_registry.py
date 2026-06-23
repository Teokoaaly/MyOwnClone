from __future__ import annotations

import pytest

from api.core.model_manager import GenerationParams
from api.core.providers import (
    DuplicateProviderError,
    ModelReply,
    ModelType,
    ProviderAdapter,
    ProviderRegistry,
    TestResult,
    UnknownProviderError,
)


class DummyAdapter(ProviderAdapter):
    provider_name = "dummy"

    def generate(self, *, prompt: str, params: GenerationParams | None = None) -> ModelReply:
        return ModelReply(text=f"echo:{prompt}")

    def generate_stream(self, *, prompt: str, params: GenerationParams | None = None):
        yield prompt

    def test_connection(self) -> TestResult:
        return TestResult(ok=True, message="ok")


def test_provider_adapter_supports_declared_model_type():
    adapter = DummyAdapter()

    assert adapter.supports(ModelType.LLM) is True
    assert adapter.supports(ModelType.EMBEDDING) is False


def test_provider_registry_default_is_singleton():
    registry_a = ProviderRegistry.reset_default()
    registry_b = ProviderRegistry.get_default()

    assert registry_a is registry_b


def test_provider_registry_register_and_lookup():
    registry = ProviderRegistry.reset_default()
    adapter = DummyAdapter()

    registry.register(adapter)

    assert registry.get("dummy") is adapter
    assert registry.has("dummy") is True
    assert registry.names() == ("dummy",)


def test_provider_registry_rejects_duplicate_provider_name():
    registry = ProviderRegistry.reset_default()
    registry.register(DummyAdapter())

    with pytest.raises(DuplicateProviderError):
        registry.register(DummyAdapter())


def test_provider_registry_raises_for_unknown_provider():
    registry = ProviderRegistry.reset_default()

    with pytest.raises(UnknownProviderError):
        registry.get("missing")


def test_generation_params_is_reexported_via_model_manager():
    params = GenerationParams(model="demo-model", temperature=0.2)

    assert params.model == "demo-model"
    assert params.temperature == 0.2
