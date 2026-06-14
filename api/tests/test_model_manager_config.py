"""Configuration tests for the standalone LLM runtime."""

from api.core import model_manager


def test_openai_base_url_prefers_standard_env(monkeypatch):
    monkeypatch.setenv("OPENAI_BASE_URL", "https://standard.example/v1")
    monkeypatch.setenv("OPENAI_API_BASE", "https://legacy.example/v1")

    assert model_manager._openai_base_url() == "https://standard.example/v1"


def test_openai_base_url_accepts_legacy_alias(monkeypatch):
    monkeypatch.delenv("OPENAI_BASE_URL", raising=False)
    monkeypatch.setenv("OPENAI_API_BASE", "https://api.deepseek.com")

    assert model_manager._openai_base_url() == "https://api.deepseek.com"


def test_openai_client_kwargs_include_base_url_when_configured(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("OPENAI_BASE_URL", "https://api.deepseek.com")

    assert model_manager._openai_client_kwargs() == {
        "api_key": "test-key",
        "base_url": "https://api.deepseek.com",
    }


def test_openai_client_kwargs_omit_blank_base_url(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("OPENAI_BASE_URL", "")
    monkeypatch.setenv("OPENAI_API_BASE", "")

    assert model_manager._openai_client_kwargs() == {"api_key": "test-key"}
