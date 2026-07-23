from __future__ import annotations

from types import SimpleNamespace

import requests

from api.core.model_registry import ModelRegistry, ModelRegistryError
from api.models.ai_models import AITask


def _make_non_embedding_dependencies_healthy(monkeypatch) -> None:
    monkeypatch.setattr(
        "api.core.readiness.db.session.execute", lambda statement: SimpleNamespace()
    )
    monkeypatch.setattr("api.core.readiness._redis_ready", lambda: (True, None))
    monkeypatch.setattr(
        requests,
        "get",
        lambda url, timeout: SimpleNamespace(status_code=200),
    )


def test_healthz_is_degraded_when_embedding_model_cannot_be_resolved(
    app, monkeypatch
) -> None:
    _make_non_embedding_dependencies_healthy(monkeypatch)

    def _unresolved(self, *, tenant_id, task):
        assert tenant_id is None
        assert task is AITask.EMBEDDING
        raise ModelRegistryError("no embedding model")

    monkeypatch.setattr(ModelRegistry, "resolve", _unresolved)

    response = app.test_client().get("/healthz")

    assert response.status_code == 503
    assert response.get_json()["checks"]["embedding_model"] == "error"


def test_healthz_is_ready_when_embedding_model_resolves(app, monkeypatch) -> None:
    _make_non_embedding_dependencies_healthy(monkeypatch)

    def _resolved(self, *, tenant_id, task):
        assert tenant_id is None
        assert task is AITask.EMBEDDING
        return SimpleNamespace(
            provider="openai", model_id="text-embedding-3-small"
        )

    monkeypatch.setattr(ModelRegistry, "resolve", _resolved)

    response = app.test_client().get("/healthz")

    assert response.status_code == 200
    assert response.get_json()["checks"]["embedding_model"] == "ok"


def test_healthz_is_degraded_when_local_embedding_model_is_missing_from_ollama(
    app, monkeypatch
) -> None:
    _make_non_embedding_dependencies_healthy(monkeypatch)

    def _resolved(self, *, tenant_id, task):
        assert tenant_id is None
        assert task is AITask.EMBEDDING
        return SimpleNamespace(provider="local", model_id="mxbai-embed-large")

    monkeypatch.setattr(ModelRegistry, "resolve", _resolved)
    monkeypatch.setattr(
        requests,
        "get",
        lambda url, timeout: SimpleNamespace(
            status_code=200,
            json=lambda: {"models": [{"name": "nomic-embed-text:latest"}]},
        ),
    )

    response = app.test_client().get("/healthz")

    assert response.status_code == 503
    assert response.get_json()["checks"]["embedding_model"] == "error"
