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


def test_ai_model_playground_uses_selected_model(ai_client, monkeypatch):
    model = SimpleNamespace(
        id="m1",
        tenant_id=None,
        name="Global", provider="openai", model_id="gpt",
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
        lambda self, **kwargs: SimpleNamespace(
            provider="openai",
            model_id="gpt",
            source="database",
            override_params={},
            temperature_default=None,
            max_tokens_default=None,
        ),
    )
    monkeypatch.setattr(
        "api.controllers.console.myownclone.ai_models.ModelManager._provider_adapter_for",
        lambda self, resolved: SimpleNamespace(
            generate=lambda prompt, params: SimpleNamespace(
                text=f"reply:{prompt}",
                usage=SimpleNamespace(as_dict=lambda: {"prompt_tokens": 1, "completion_tokens": 2, "total_tokens": 3}),
                latency_ms=12,
            )
        ),
    )

    resp = ai_client.post(
        "/console/api/myownclone/ai-models/playground",
        headers={"Authorization": "Bearer ok"},
        json={"model_id": "m1", "task": "chat", "prompt": "hello"},
    )

    assert resp.status_code == 200
    assert resp.get_json()["text"] == "reply:hello"


def test_ai_model_costs_aggregates_rows(ai_client, monkeypatch):
    rows = [
        SimpleNamespace(created_at=__import__("datetime").datetime(2026, 6, 23, 8, 0, 0), prompt_tokens=10, completion_tokens=5, model_id="gpt-4o-mini"),
        SimpleNamespace(created_at=__import__("datetime").datetime(2026, 6, 23, 9, 0, 0), prompt_tokens=20, completion_tokens=15, model_id="gpt-4o-mini"),
    ]

    class ExecuteResult:
        def __init__(self, rows):
            self._rows = rows

        def scalars(self):
            return SimpleNamespace(all=lambda: self._rows)

    calls = {"count": 0}

    def fake_execute(stmt):
        calls["count"] += 1
        return ExecuteResult([] if calls["count"] == 1 else rows)

    monkeypatch.setattr(
        "api.controllers.console.myownclone.ai_models.db.session.execute",
        fake_execute,
    )

    resp = ai_client.get(
        "/console/api/myownclone/ai-models/costs",
        headers={"Authorization": "Bearer ok"},
    )

    assert resp.status_code == 200
    body = resp.get_json()
    assert body["totals"]["invocations"] == 2
    assert body["totals"]["prompt_tokens"] == 30
    assert body["totals"]["completion_tokens"] == 20
    assert body["by_model"][0]["invocations"] == 2


def test_ai_model_costs_prefers_rollup_rows(ai_client, monkeypatch):
    rollups = [
        SimpleNamespace(day=__import__("datetime").date(2026, 6, 23), invocations=4, prompt_tokens=40, completion_tokens=20)
    ]

    class ExecuteResult:
        def __init__(self, rows):
            self._rows = rows

        def scalars(self):
            return SimpleNamespace(all=lambda: self._rows)

    calls = {"count": 0}

    def fake_execute(stmt):
        calls["count"] += 1
        return ExecuteResult(rollups if calls["count"] == 1 else [])

    monkeypatch.setattr(
        "api.controllers.console.myownclone.ai_models.db.session.execute",
        fake_execute,
    )

    resp = ai_client.get(
        "/console/api/myownclone/ai-models/costs",
        headers={"Authorization": "Bearer ok"},
    )

    assert resp.status_code == 200
    body = resp.get_json()
    assert body["totals"]["invocations"] == 4
    assert body["series"][0]["day"] == "2026-06-23"


def test_ai_model_costs_handles_missing_rollup_table(ai_client, monkeypatch):
    """When the cost_daily_rollup table does not exist (migration not applied),
    the endpoint must return 200 by falling back to AIInvocation, not 500."""
    from sqlalchemy.exc import ProgrammingError

    inv_rows = [
        SimpleNamespace(
            created_at=__import__("datetime").datetime(2026, 6, 23, 10, 0, 0),
            prompt_tokens=7, completion_tokens=3, model_id="gpt-4o-mini",
        ),
    ]

    class ExecuteResult:
        def __init__(self, rows):
            self._rows = rows

        def scalars(self):
            return SimpleNamespace(all=lambda: self._rows)

    calls = {"count": 0}

    def fake_execute(stmt):
        calls["count"] += 1
        # First query targets cost_daily_rollup → table missing → ProgrammingError
        if calls["count"] == 1:
            raise ProgrammingError("SELECT cost_daily_rollup", {}, Exception("relation does not exist"))
        # Fallback to AIInvocation
        return ExecuteResult(inv_rows)

    monkeypatch.setattr(
        "api.controllers.console.myownclone.ai_models.db.session.execute",
        fake_execute,
    )

    resp = ai_client.get(
        "/console/api/myownclone/ai-models/costs",
        headers={"Authorization": "Bearer ok"},
    )

    assert resp.status_code == 200, resp.get_data(as_text=True)
    body = resp.get_json()
    assert body["totals"]["invocations"] == 1
    assert body["totals"]["prompt_tokens"] == 7
    assert body["totals"]["completion_tokens"] == 3
    assert body["by_model"][0]["model_id"] == "gpt-4o-mini"


def test_ai_model_costs_handles_both_tables_missing(ai_client, monkeypatch):
    """When BOTH cost_daily_rollup and AIInvocation queries fail, the endpoint
    must still return 200 with empty series (defensive degradation)."""
    from sqlalchemy.exc import ProgrammingError

    def fake_execute(stmt):
        raise ProgrammingError("SELECT cost_daily_rollup", {}, Exception("relation does not exist"))

    monkeypatch.setattr(
        "api.controllers.console.myownclone.ai_models.db.session.execute",
        fake_execute,
    )

    resp = ai_client.get(
        "/console/api/myownclone/ai-models/costs",
        headers={"Authorization": "Bearer ok"},
    )

    assert resp.status_code == 200, resp.get_data(as_text=True)
    body = resp.get_json()
    assert body["series"] == []
    assert body["by_model"] == []
    assert body["totals"] == {"invocations": 0, "prompt_tokens": 0, "completion_tokens": 0}


def test_ai_model_costs_uses_real_invocation_columns(ai_client, monkeypatch):
    """Reproduce the live 500: cost_daily_rollup is empty (table exists, 0 rows),
    so the handler falls back to AIInvocation aggregation. The real
    ai_invocations schema exposes `model` (NOT `model_id`), so the handler
    must read the actual column name and still return 200 with data."""
    # Mock AIInvocation rows using the REAL schema: 'model' (not 'model_id')
    inv_rows = [
        SimpleNamespace(
            created_at=__import__("datetime").datetime(2026, 6, 23, 10, 0, 0),
            prompt_tokens=12, completion_tokens=8, model="minimax-m2.7",
        ),
        SimpleNamespace(
            created_at=__import__("datetime").datetime(2026, 6, 24, 11, 0, 0),
            prompt_tokens=4, completion_tokens=6, model="minimax-m2.7",
        ),
    ]

    class ExecuteResult:
        def __init__(self, rows):
            self._rows = rows

        def scalars(self):
            return SimpleNamespace(all=lambda: self._rows)

    calls = {"count": 0}

    def fake_execute(stmt):
        calls["count"] += 1
        # First call is rollup (returns empty because table has 0 rows)
        # Second call is the AIInvocation fallback (returns real rows)
        return ExecuteResult([] if calls["count"] == 1 else inv_rows)

    monkeypatch.setattr(
        "api.controllers.console.myownclone.ai_models.db.session.execute",
        fake_execute,
    )

    resp = ai_client.get(
        "/console/api/myownclone/ai-models/costs",
        headers={"Authorization": "Bearer ok"},
    )

    assert resp.status_code == 200, resp.get_data(as_text=True)
    body = resp.get_json()
    assert body["totals"]["invocations"] == 2
    assert body["totals"]["prompt_tokens"] == 16
    assert body["totals"]["completion_tokens"] == 14
    assert len(body["by_model"]) == 1
    assert body["by_model"][0]["model_id"] == "minimax-m2.7"
    assert body["by_model"][0]["invocations"] == 2
    assert len(body["series"]) == 2  # two different days
