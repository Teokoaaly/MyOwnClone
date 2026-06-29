from __future__ import annotations

import sys
from types import SimpleNamespace

import pytest

from api.core.embeddings import EmbeddingService
from api.core.model_registry import ResolvedModelConfig
from api.core.providers import ModelInvocationError
from api.core.token_budget import EmbeddingDimensionError
from api.models.ai_models import AITask


def _embedding_model(**overrides) -> ResolvedModelConfig:
    data = {
        "task": AITask.EMBEDDING,
        "provider": "openai",
        "model_id": "text-embedding-3-small",
        "tenant_id": "tenant-1",
        "source": "database",
        "api_key": "secret",
        "base_url": None,
        "embedding_dimensions": 1536,
    }
    data.update(overrides)
    return ResolvedModelConfig(**data)


def test_embedding_service_uses_provided_model_without_registry(monkeypatch):
    captured = []

    class FakeOpenAIClient:
        def __init__(self, **kwargs):
            self.embeddings = SimpleNamespace(
                create=lambda **payload: captured.append(payload) or SimpleNamespace(
                    data=[SimpleNamespace(embedding=[1.0, 2.0, 3.0])]
                )
            )

    monkeypatch.setitem(sys.modules, "openai", SimpleNamespace(OpenAI=FakeOpenAIClient))

    service = EmbeddingService(registry=SimpleNamespace(get_model_for_task=lambda **_: None))
    vectors = service.embed_texts(["hello"], model=_embedding_model())

    assert vectors == [[1.0, 2.0, 3.0]]
    assert captured[0]["model"] == "text-embedding-3-small"


def test_embedding_service_resolves_model_from_registry(monkeypatch):
    class FakeOpenAIClient:
        def __init__(self, **kwargs):
            self.embeddings = SimpleNamespace(
                create=lambda **payload: SimpleNamespace(
                    data=[SimpleNamespace(embedding=[float(i)]) for i, _ in enumerate(payload["input"], start=1)]
                )
            )

    monkeypatch.setitem(sys.modules, "openai", SimpleNamespace(OpenAI=FakeOpenAIClient))

    model = _embedding_model()
    service = EmbeddingService(registry=SimpleNamespace(get_model_for_task=lambda **_: model))
    vectors = service.embed_texts(["a", "b"], tenant_id="tenant-1")

    assert vectors == [[1.0], [2.0]]


def test_embedding_service_preserves_batching(monkeypatch):
    batches = []

    class FakeOpenAIClient:
        def __init__(self, **kwargs):
            self.embeddings = SimpleNamespace(
                create=lambda **payload: batches.append(list(payload["input"])) or SimpleNamespace(
                    data=[SimpleNamespace(embedding=[0.0]) for _ in payload["input"]]
                )
            )

    monkeypatch.setitem(sys.modules, "openai", SimpleNamespace(OpenAI=FakeOpenAIClient))

    service = EmbeddingService()
    texts = [f"t{i}" for i in range(70)]
    vectors = service.embed_texts(texts, model=_embedding_model())

    assert len(vectors) == 70
    assert len(batches) == 2
    assert len(batches[0]) == 64
    assert len(batches[1]) == 6


def test_embedding_service_rejects_dimension_mismatch():
    service = EmbeddingService()

    with pytest.raises(EmbeddingDimensionError):
        service.embed_texts(["hello"], model=_embedding_model(embedding_dimensions=None))


def test_embedding_service_rejects_unsupported_provider():
    service = EmbeddingService()

    with pytest.raises(ModelInvocationError):
        service.embed_texts(["hello"], model=_embedding_model(provider="anthropic"))


def test_embedding_service_uses_minimax_embeddings_contract(monkeypatch):
    captured = {}

    class FakeResponse:
        status_code = 200

        def json(self):
            return {
                "vectors": [[0.1, 0.2, 0.3]],
                "base_resp": {"status_code": 0, "status_msg": "ok"},
            }

    def fake_post(url, *, headers, json, timeout):
        captured["url"] = url
        captured["headers"] = headers
        captured["json"] = json
        captured["timeout"] = timeout
        return FakeResponse()

    monkeypatch.setattr("api.core.embeddings.requests.post", fake_post)

    service = EmbeddingService()
    vectors = service.embed_texts(
        ["hola"],
        model=_embedding_model(
            provider="minimax",
            model_id="embo-01",
            base_url="https://api.minimax.io/v1",
        ),
    )

    assert vectors == [[0.1, 0.2, 0.3]]
    assert captured["url"] == "https://api.minimax.io/v1/embeddings"
    assert captured["json"] == {
        "model": "embo-01",
        "texts": ["hola"],
        "type": "db",
    }


def test_embedding_service_uses_local_ollama_embeddings_contract(monkeypatch):
    captured = {}

    class FakeResponse:
        status_code = 200

        def json(self):
            return {"embeddings": [[0.4, 0.5], [0.6, 0.7]]}

    def fake_post(url, *, headers, json, timeout):
        captured["url"] = url
        captured["headers"] = headers
        captured["json"] = json
        captured["timeout"] = timeout
        return FakeResponse()

    monkeypatch.setattr("api.core.embeddings.requests.post", fake_post)

    service = EmbeddingService()
    vectors = service.embed_texts(
        ["uno", "dos"],
        model=_embedding_model(
            provider="local",
            model_id="mxbai-embed-large",
            base_url="http://ollama:11434/v1",
            embedding_dimensions=1024,
        ),
    )

    assert vectors == [[0.4, 0.5], [0.6, 0.7]]
    assert captured["url"] == "http://ollama:11434/api/embed"
    assert captured["json"] == {
        "model": "mxbai-embed-large",
        "input": ["uno", "dos"],
    }
