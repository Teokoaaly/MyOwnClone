"""Tests for provider adapters (mocked HTTP)."""
from __future__ import annotations
from unittest.mock import patch, MagicMock

import pytest

from api.core.providers import (
    OpenAIAdapter, AnthropicAdapter, CohereAdapter, OllamaAdapter,
    get_adapter_for_provider, ProviderError,
)


# ---------- OpenAI ----------

def test_openai_chat_non_stream():
    adapter = OpenAIAdapter(api_key="test-key")
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "choices": [{"message": {"content": "Hello"}}],
        "usage": {"prompt_tokens": 10, "completion_tokens": 5},
        "model": "gpt-4o-mini",
    }
    with patch("httpx.Client") as MockClient:
        client_instance = MockClient.return_value.__enter__.return_value
        client_instance.post.return_value = mock_resp
        result = adapter.chat("gpt-4o-mini", [{"role": "user", "content": "Hi"}])
    assert result["content"] == "Hello"
    assert result["tokens_in"] == 10
    assert result["tokens_out"] == 5


def test_openai_chat_retriable_on_429():
    adapter = OpenAIAdapter(api_key="test-key")
    mock_resp = MagicMock()
    mock_resp.status_code = 429
    mock_resp.text = "rate limited"
    mock_resp.json.side_effect = Exception("no json")
    with patch("httpx.Client") as MockClient:
        client_instance = MockClient.return_value.__enter__.return_value
        client_instance.post.return_value = mock_resp
        with pytest.raises(ProviderError) as exc_info:
            adapter.chat("gpt-4o-mini", [{"role": "user", "content": "Hi"}])
    assert exc_info.value.retriable is True
    assert exc_info.value.status_code == 429


def test_openai_chat_non_retriable_on_400():
    adapter = OpenAIAdapter(api_key="test-key")
    mock_resp = MagicMock()
    mock_resp.status_code = 400
    mock_resp.text = "bad request"
    mock_resp.json.side_effect = Exception("no json")
    with patch("httpx.Client") as MockClient:
        client_instance = MockClient.return_value.__enter__.return_value
        client_instance.post.return_value = mock_resp
        with pytest.raises(ProviderError) as exc_info:
            adapter.chat("gpt-4o-mini", [{"role": "user", "content": "Hi"}])
    assert exc_info.value.retriable is False


def test_openai_embed():
    adapter = OpenAIAdapter(api_key="test-key")
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "data": [
            {"embedding": [0.1, 0.2, 0.3]},
            {"embedding": [0.4, 0.5, 0.6]},
        ]
    }
    with patch("httpx.Client") as MockClient:
        client_instance = MockClient.return_value.__enter__.return_value
        client_instance.post.return_value = mock_resp
        result = adapter.embed("text-embedding-3-small", ["a", "b"])
    assert result == [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]


def test_openai_moderate():
    adapter = OpenAIAdapter(api_key="test-key")
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "results": [{
            "flagged": False,
            "categories": {"hate": False},
            "category_scores": {"hate": 0.01},
        }]
    }
    with patch("httpx.Client") as MockClient:
        client_instance = MockClient.return_value.__enter__.return_value
        client_instance.post.return_value = mock_resp
        result = adapter.moderate("hello world")
    assert result["flagged"] is False


# ---------- Anthropic ----------

def test_anthropic_chat_non_stream():
    adapter = AnthropicAdapter(api_key="test-key")
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "content": [{"text": "Hello from Claude"}],
        "usage": {"input_tokens": 8, "output_tokens": 4},
        "model": "claude-3-5-sonnet",
    }
    with patch("httpx.Client") as MockClient:
        client_instance = MockClient.return_value.__enter__.return_value
        client_instance.post.return_value = mock_resp
        result = adapter.chat("claude-3-5-sonnet", [
            {"role": "system", "content": "Be brief"},
            {"role": "user", "content": "Hi"},
        ])
    assert result["content"] == "Hello from Claude"
    assert result["tokens_in"] == 8
    assert result["tokens_out"] == 4


def test_anthropic_strips_system_message():
    """System message should be passed as 'system' field, not in 'messages'."""
    adapter = AnthropicAdapter(api_key="test-key")
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "content": [{"text": "ok"}],
        "usage": {"input_tokens": 1, "output_tokens": 1},
        "model": "claude",
    }
    with patch("httpx.Client") as MockClient:
        client_instance = MockClient.return_value.__enter__.return_value
        client_instance.post.return_value = mock_resp
        adapter.chat("claude", [
            {"role": "system", "content": "You are X"},
            {"role": "user", "content": "Hi"},
        ])
        # Verify the request payload had 'system' and NO system-role in messages
        call_args = client_instance.post.call_args
        payload = call_args.kwargs["json"]
        assert "system" in payload
        assert payload["system"] == "You are X"
        assert all(m["role"] != "system" for m in payload["messages"])


# ---------- Cohere ----------

def test_cohere_rerank():
    adapter = CohereAdapter(api_key="test-key")
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "results": [
            {"index": 2, "relevance_score": 0.9},
            {"index": 0, "relevance_score": 0.7},
        ]
    }
    with patch("httpx.Client") as MockClient:
        client_instance = MockClient.return_value.__enter__.return_value
        client_instance.post.return_value = mock_resp
        result = adapter.rerank("rerank-english-v3.0", "query", ["a", "b", "c"], top_n=2)
    assert result == [{"index": 2, "score": 0.9}, {"index": 0, "score": 0.7}]


def test_cohere_chat_converts_messages():
    adapter = CohereAdapter(api_key="test-key")
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "text": "Hi there",
        "meta": {"tokens": {"input_tokens": 3, "output_tokens": 2}},
    }
    with patch("httpx.Client") as MockClient:
        client_instance = MockClient.return_value.__enter__.return_value
        client_instance.post.return_value = mock_resp
        result = adapter.chat("command-r-plus", [
            {"role": "user", "content": "Hello"},
        ])
    assert result["content"] == "Hi there"
    call_args = client_instance.post.call_args
    payload = call_args.kwargs["json"]
    assert payload["message"] == "Hello"
    assert payload["model"] == "command-r-plus"


# ---------- Ollama ----------

def test_ollama_inherits_openai():
    """OllamaAdapter should be an OpenAIAdapter subclass."""
    assert issubclass(OllamaAdapter, OpenAIAdapter)
    adapter = OllamaAdapter()
    assert adapter.base_url == "http://localhost:11434/v1"
    assert adapter.api_key == "ollama"
    assert adapter.is_available() is True


def test_ollama_custom_base_url():
    adapter = OllamaAdapter(base_url="http://gpu-server.local:11434/v1")
    assert adapter.base_url == "http://gpu-server.local:11434/v1"


# ---------- Factory ----------

def test_factory_returns_correct_adapter():
    assert isinstance(get_adapter_for_provider("openai", api_key="k"), OpenAIAdapter)
    assert isinstance(get_adapter_for_provider("anthropic", api_key="k"), AnthropicAdapter)
    assert isinstance(get_adapter_for_provider("cohere", api_key="k"), CohereAdapter)
    assert isinstance(get_adapter_for_provider("ollama"), OllamaAdapter)


def test_factory_unknown_provider_raises():
    with pytest.raises(ValueError, match="Unknown provider"):
        get_adapter_for_provider("nonexistent")


# ---------- Availability ----------

def test_adapters_require_api_key():
    with pytest.raises(ValueError, match="api_key is required"):
        OpenAIAdapter(api_key="")
    with pytest.raises(ValueError, match="api_key is required"):
        AnthropicAdapter(api_key="")
    with pytest.raises(ValueError, match="api_key is required"):
        CohereAdapter(api_key="")


def test_openai_is_available_false_without_key():
    with patch.dict("os.environ", {}, clear=True):
        adapter = OpenAIAdapter(api_key="real-key")
        # Manually clear api_key
        adapter.api_key = ""
        assert adapter.is_available() is False
