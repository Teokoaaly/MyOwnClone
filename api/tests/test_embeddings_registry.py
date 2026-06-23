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
        service.embed_texts(["hello"], model=_embedding_model(embedding_dimensions=768))


def test_embedding_service_rejects_unsupported_provider():
    service = EmbeddingService()

    with pytest.raises(ModelInvocationError):
        service.embed_texts(["hello"], model=_embedding_model(provider="anthropic"))
