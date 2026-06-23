from __future__ import annotations

from types import SimpleNamespace

from api.core.model_manager import ModelManager
from api.core.model_registry import ResolvedModelConfig
from api.core.providers import ModelReply, ModelUsage
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
        "embedding_dimensions": 1536,
    }
    data.update(overrides)
    return ResolvedModelConfig(**data)


def test_model_manager_invoke_for_task_uses_registry_and_persists(monkeypatch):
    recorded = []
    manager = ModelManager(
        registry=SimpleNamespace(get_model_for_task=lambda **_: _resolved()),
        retry_client=SimpleNamespace(invoke=lambda candidates: candidates[0].invoke()),
    )
    monkeypatch.setattr(manager, "_provider_adapter_for", lambda resolved: SimpleNamespace(
        generate=lambda **_: ModelReply(
            text="ok",
            usage=ModelUsage(prompt_tokens=3, completion_tokens=5, total_tokens=8),
            latency_ms=12,
        )
    ))
    monkeypatch.setattr(manager, "_record_invocation", lambda **kwargs: recorded.append(kwargs))

    reply = manager.invoke_for_task(
        tenant_id="tenant-1",
        clone_id="clone-1",
        task=AITask.CHAT,
        message="hello",
    )

    assert reply.text == "ok"
    assert recorded[0]["success"] is True
    assert recorded[0]["model_name"] == "gpt-test"


def test_model_manager_legacy_invoke_non_streaming_delegates(monkeypatch):
    monkeypatch.setattr(
        ModelManager,
        "invoke_for_task",
        lambda self, **kwargs: ModelReply(text="legacy-ok"),
    )

    reply = ModelManager.invoke_non_streaming(
        tenant_id="tenant-1",
        clone_id="clone-1",
        message="hello",
    )

    assert reply.text == "legacy-ok"
