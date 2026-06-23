from __future__ import annotations

import sys
from types import SimpleNamespace

import pytest

from api.core.model_registry import ResolvedModelConfig
from api.core.providers import GenerationParams, ModelInvocationError
from api.core.providers.anthropic import AnthropicAdapter
from api.core.providers.local import LocalAdapter
from api.core.providers.minimax import MiniMaxAdapter
from api.core.providers.openai import OpenAIAdapter
from api.core.providers.openai_compatible import OpenAICompatibleAdapter
from api.core.providers.together import TogetherAdapter
from api.models.ai_models import AITask


def _base_config(**overrides) -> ResolvedModelConfig:
    data = {
        "task": AITask.CHAT,
        "provider": "openai",
        "model_id": "demo-model",
        "tenant_id": "tenant-1",
        "source": "database",
        "api_key": "secret",
        "base_url": None,
    }
    data.update(overrides)
    return ResolvedModelConfig(
        **data,
    )


def test_openai_adapter_normalizes_usage_and_text(monkeypatch):
    class FakeOpenAIClient:
        def __init__(self, **kwargs):
            self.kwargs = kwargs
            self.chat = SimpleNamespace(
                completions=SimpleNamespace(
                    create=lambda **_: SimpleNamespace(
                        choices=[SimpleNamespace(message=SimpleNamespace(content="hello"))],
                        usage=SimpleNamespace(prompt_tokens=3, completion_tokens=5, total_tokens=8),
                    )
                )
            )
            self.models = SimpleNamespace(list=lambda: [])

    monkeypatch.setitem(sys.modules, "openai", SimpleNamespace(OpenAI=FakeOpenAIClient))

    reply = OpenAIAdapter(_base_config()).generate(prompt="hi")

    assert reply.text == "hello"
    assert reply.usage.as_dict() == {
        "prompt_tokens": 3,
        "completion_tokens": 5,
        "total_tokens": 8,
    }
    assert isinstance(reply.latency_ms, int)


def test_openai_adapter_reports_missing_api_key_in_test_connection():
    adapter = OpenAIAdapter(_base_config(api_key=None))

    result = adapter.test_connection()

    assert result.ok is False
    assert "api_key" in result.message


def test_openai_compatible_requires_base_url():
    with pytest.raises(ModelInvocationError):
        OpenAICompatibleAdapter(_base_config(base_url=None))


@pytest.mark.parametrize(
    ("adapter_cls", "expected_base_url"),
    [
        (MiniMaxAdapter, "https://api.minimax.io/v1"),
        (TogetherAdapter, "https://api.together.xyz/v1"),
        (LocalAdapter, "http://127.0.0.1:11434/v1"),
    ],
)
def test_compatible_adapters_fill_expected_base_url(adapter_cls, expected_base_url):
    adapter = adapter_cls(_base_config(base_url=None, api_key=None))

    assert adapter.config.base_url == expected_base_url


def test_anthropic_adapter_normalizes_usage(monkeypatch):
    class FakeAnthropicClient:
        def __init__(self, **kwargs):
            self.kwargs = kwargs
            self.messages = SimpleNamespace(
                create=lambda **_: SimpleNamespace(
                    content=[SimpleNamespace(text="anthropic hi")],
                    usage=SimpleNamespace(input_tokens=7, output_tokens=11),
                ),
                stream=lambda **_: None,
            )

    monkeypatch.setitem(sys.modules, "anthropic", SimpleNamespace(Anthropic=FakeAnthropicClient))

    reply = AnthropicAdapter(_base_config(provider="anthropic")).generate(prompt="hi")

    assert reply.text == "anthropic hi"
    assert reply.usage.as_dict() == {
        "prompt_tokens": 7,
        "completion_tokens": 11,
        "total_tokens": 18,
    }


def test_provider_error_is_wrapped(monkeypatch):
    class FakeOpenAIClient:
        def __init__(self, **kwargs):
            self.chat = SimpleNamespace(
                completions=SimpleNamespace(
                    create=lambda **_: (_ for _ in ()).throw(RuntimeError("provider boom"))
                )
            )
            self.models = SimpleNamespace(list=lambda: [])

    monkeypatch.setitem(sys.modules, "openai", SimpleNamespace(OpenAI=FakeOpenAIClient))

    with pytest.raises(ModelInvocationError, match="provider boom"):
        OpenAIAdapter(_base_config()).generate(prompt="hi")


def test_test_connection_success_is_reported(monkeypatch):
    class FakeOpenAIClient:
        def __init__(self, **kwargs):
            self.chat = SimpleNamespace(completions=SimpleNamespace(create=lambda **_: None))
            self.models = SimpleNamespace(list=lambda: ["ok"])

    monkeypatch.setitem(sys.modules, "openai", SimpleNamespace(OpenAI=FakeOpenAIClient))

    result = OpenAIAdapter(_base_config()).test_connection()

    assert result.ok is True
