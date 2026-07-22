"""M13 — defect #6 runtime embeddings guard (413 over-limit, 422 error path)."""

from __future__ import annotations

from api.controllers.console.myownclone.runtime import _MAX_EMBED_TEXTS
from api.libs.login import AuthenticatedIdentity


def _auth(monkeypatch):
    monkeypatch.setattr(
        "api.libs.login._verify_token",
        lambda token: {"sub": "user-1"},
    )
    monkeypatch.setattr(
        "api.libs.login._load_authoritative_identity",
        lambda account_id: AuthenticatedIdentity(
            account_id="user-1",
            tenant_id="tenant-1",
            role="admin",
            email="user@example.com",
        ),
    )
    monkeypatch.setattr(
        "api.controllers.console.myownclone.runtime._check_rate_limit",
        lambda endpoint, limit, window: (True, None),
    )


def test_embeddings_rejects_too_many_texts(app, monkeypatch):
    _auth(monkeypatch)
    called = {"embed": False}

    def fake_embed(self, texts, tenant_id=None, model=None):
        called["embed"] = True
        return [[0.0] * 1536 for _ in texts]

    monkeypatch.setattr(
        "api.controllers.console.myownclone.runtime.EmbeddingService.embed_texts",
        fake_embed,
    )

    client = app.test_client()
    response = client.post(
        "/console/api/myownclone/embeddings",
        json={"texts": ["x"] * (_MAX_EMBED_TEXTS + 1)},
        headers={"Authorization": "Bearer test-token"},
    )

    assert response.status_code == 413
    body = response.get_json()
    assert body["max_texts"] == _MAX_EMBED_TEXTS
    # Guard must short-circuit before fanning out to the embedding provider.
    assert called["embed"] is False


def test_embeddings_at_limit_is_allowed(app, monkeypatch):
    _auth(monkeypatch)
    monkeypatch.setattr(
        "api.controllers.console.myownclone.runtime.EmbeddingService.embed_texts",
        lambda self, texts, tenant_id=None, model=None: [[0.0] * 1536 for _ in texts],
    )

    client = app.test_client()
    response = client.post(
        "/console/api/myownclone/embeddings",
        json={"texts": ["x"] * _MAX_EMBED_TEXTS},
        headers={"Authorization": "Bearer test-token"},
    )

    assert response.status_code == 200
    assert response.get_json()["count"] == _MAX_EMBED_TEXTS


def test_embeddings_error_path_returns_422(app, monkeypatch):
    _auth(monkeypatch)

    def boom(self, texts, tenant_id=None, model=None):
        raise ValueError("embedding provider unavailable")

    monkeypatch.setattr(
        "api.controllers.console.myownclone.runtime.EmbeddingService.embed_texts",
        boom,
    )

    client = app.test_client()
    response = client.post(
        "/console/api/myownclone/embeddings",
        json={"texts": ["hola"]},
        headers={"Authorization": "Bearer test-token"},
    )

    assert response.status_code == 422
    assert "embedding provider unavailable" in response.get_json()["error"]
