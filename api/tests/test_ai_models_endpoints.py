from __future__ import annotations

from types import SimpleNamespace

import pytest

@pytest.fixture
def ai_client(app, monkeypatch):
    monkeypatch.setattr("api.controllers.console.myownclone.ai_models.SecretCipher.encrypt", lambda value: f"enc:{value}")
    monkeypatch.setattr("api.controllers.console.myownclone.ai_models.ModelRegistry.invalidate", lambda self, **kwargs: None)
    monkeypatch.setattr("api.libs.login._verify_token", lambda token: {
        "sub": "user-1",
        "tenant_id": "tenant-1",
        "role": "admin",
        "email": "u@example.com",
    })
    app.config["TESTING"] = True
    return app.test_client()


def test_ai_models_requires_auth(client):
    assert client.get("/console/api/myownclone/ai-models").status_code == 401


def test_ai_models_list_is_tenant_scoped(ai_client, monkeypatch):
    models = [
        SimpleNamespace(
            id="m1", tenant_id="tenant-1", name="Tenant", provider="openai", model_id="gpt",
            base_url=None, capabilities=["llm"], input_price_cents_per_mtok=0,
            output_price_cents_per_mtok=0, priority=1, temperature_default=None,
            max_tokens_default=None, max_input_tokens=None, embedding_dimensions=None,
            is_active=True, api_key_encrypted="x",
        )
    ]
    monkeypatch.setattr(
        "api.controllers.console.myownclone.ai_models.db.session.execute",
        lambda stmt: SimpleNamespace(scalars=lambda: SimpleNamespace(all=lambda: models)),
    )

    resp = ai_client.get("/console/api/myownclone/ai-models", headers={"Authorization": "Bearer ok"})

    assert resp.status_code == 200
    body = resp.get_json()
    assert body[0]["id"] == "m1"
    assert "api_key" not in body[0]
    assert body[0]["has_api_key"] is True


def test_ai_models_create_encrypts_plaintext(ai_client, monkeypatch):
    added = []
    monkeypatch.setattr("api.controllers.console.myownclone.ai_models.db.session.add", lambda row: added.append(row))
    monkeypatch.setattr("api.controllers.console.myownclone.ai_models.db.session.commit", lambda: None)

    resp = ai_client.post(
        "/console/api/myownclone/ai-models",
        headers={"Authorization": "Bearer ok"},
        json={
            "name": "My Model",
            "provider": "openai",
            "model_id": "gpt-4o-mini",
            "api_key": "sk-secret",
            "capabilities": ["llm"],
        },
    )

    assert resp.status_code == 201
    assert added[0].api_key_encrypted == "enc:sk-secret"


def test_ai_model_assignment_rejects_capability_mismatch(ai_client, monkeypatch):
    model = SimpleNamespace(
        id="m1",
        tenant_id="tenant-1",
        capabilities=["embedding"],
        provider="openai",
    )
    monkeypatch.setattr(
        "api.controllers.console.myownclone.ai_models.db.session.execute",
        lambda stmt: SimpleNamespace(scalar_one_or_none=lambda: model),
    )

    resp = ai_client.put(
        "/console/api/myownclone/ai-models/assignments",
        headers={"Authorization": "Bearer ok"},
        json={"task": "chat", "model_id": "m1", "override_params": {}},
    )

    assert resp.status_code == 400
    assert resp.get_json()["error"] == "model capability mismatch"


def test_ai_model_test_connection_uses_adapter(ai_client, monkeypatch):
    model = SimpleNamespace(
        id="m1",
        tenant_id="tenant-1",
        name="Tenant", provider="openai", model_id="gpt",
        base_url=None, capabilities=["llm"], input_price_cents_per_mtok=0,
        output_price_cents_per_mtok=0, priority=1, temperature_default=None,
        max_tokens_default=None, max_input_tokens=None, embedding_dimensions=None,
        is_active=True, api_key_encrypted="encrypted",
    )
    monkeypatch.setattr(
        "api.controllers.console.myownclone.ai_models.db.session.execute",
        lambda stmt: SimpleNamespace(scalar_one_or_none=lambda: model),
    )
    monkeypatch.setattr(
        "api.controllers.console.myownclone.ai_models.ModelRegistry._build_resolved_from_db",
        lambda self, **kwargs: SimpleNamespace(provider="openai", model_id="gpt"),
    )
    monkeypatch.setattr(
        "api.controllers.console.myownclone.ai_models.ModelManager._provider_adapter_for",
        lambda self, resolved: SimpleNamespace(test_connection=lambda: SimpleNamespace(ok=True, message="ok", details={})),
    )

    resp = ai_client.post(
        "/console/api/myownclone/ai-models/test-connection",
        headers={"Authorization": "Bearer ok"},
        json={"model_id": "m1"},
    )

    assert resp.status_code == 200
    assert resp.get_json()["ok"] is True
