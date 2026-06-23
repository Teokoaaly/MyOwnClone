from __future__ import annotations

from types import SimpleNamespace

import pytest

from api.core.model_manager import ModelManager
from api.core.model_registry import ResolvedModelConfig
from api.core.providers import ModelInvocationError
from api.models.ai_models import AITask


def _resolved(**overrides) -> ResolvedModelConfig:
    data = {
        "task": AITask.CHAT,
        "provider": "openai",
        "model_id": "gpt-test",
        "tenant_id": "tenant-1",
        "source": "database",
        "priority": 10,
        "max_input_tokens": 1000,
        "max_tokens_default": 200,
    }
    data.update(overrides)
    return ResolvedModelConfig(**data)


def test_streaming_invocation_persists_zero_usage_with_diagnostic(monkeypatch):
    recorded = []
    manager = ModelManager(registry=SimpleNamespace(get_model_for_task=lambda **_: _resolved()))
    monkeypatch.setattr(manager, "_provider_adapter_for", lambda resolved: SimpleNamespace(
        generate_stream=lambda **_: iter(["a", "b"])
    ))
    monkeypatch.setattr(manager, "_record_invocation", lambda **kwargs: recorded.append(kwargs))

    chunks = list(manager.invoke_for_task_stream(
        tenant_id="tenant-1",
        clone_id="clone-1",
        task=AITask.CHAT,
        message="hello",
    ))

    assert chunks == ["a", "b"]
    assert recorded[0]["success"] is True
    assert recorded[0]["usage"] is None
    assert recorded[0]["error_message"] == "stream_usage_missing"


def test_streaming_invocation_persists_failure(monkeypatch):
    recorded = []
    manager = ModelManager(registry=SimpleNamespace(get_model_for_task=lambda **_: _resolved()))

    def broken_stream(**kwargs):
        yield "a"
        raise RuntimeError("stream boom")

    monkeypatch.setattr(manager, "_provider_adapter_for", lambda resolved: SimpleNamespace(
        generate_stream=broken_stream
    ))
    monkeypatch.setattr(manager, "_record_invocation", lambda **kwargs: recorded.append(kwargs))

    with pytest.raises(ModelInvocationError, match="stream boom"):
        list(manager.invoke_for_task_stream(
            tenant_id="tenant-1",
            clone_id="clone-1",
            task=AITask.CHAT,
            message="hello",
        ))

    assert recorded[-1]["success"] is False
