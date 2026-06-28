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
        SimpleNamespace(
            day=__import__("datetime").date(2026, 6, 23),
            created_at=__import__("datetime").datetime(2026, 6, 23, 8, 0, 0),
            prompt_tokens=10, completion_tokens=5,
            invocations=1, model="minimax",
        ),
        SimpleNamespace(
            day=__import__("datetime").date(2026, 6, 23),
            created_at=__import__("datetime").datetime(2026, 6, 23, 9, 0, 0),
            prompt_tokens=20, completion_tokens=15,
            invocations=1, model="minimax",
        ),
    ]

    class ExecuteResult:
        def __init__(self, rows):
            self._rows = rows

        def scalars(self):
            return SimpleNamespace(all=lambda: self._rows)

        def scalar_one_or_none(self):
            return None  # maintenance flag reads return None (off)

    # Count ONLY rollup queries (skip maintenance middleware queries)
    rollup_calls = {"count": 0}

    def fake_execute(stmt):
        try:
            stmt_str = str(stmt)
        except Exception:
            stmt_str = ""
        # Maintenance middleware queries system_settings table
        if "system_settings" in stmt_str:
            return ExecuteResult([])
        # Otherwise it's a rollup query - return real data on first call
        rollup_calls["count"] += 1
        if rollup_calls["count"] == 1:
            return ExecuteResult(rows)
        return ExecuteResult([])

    monkeypatch.setattr(
        "api.controllers.console.myownclone.ai_models.db.session.execute",
        fake_execute,
    )
    # Mock _tenant_id to return a known value (test expects tenant-scoped query)
    monkeypatch.setattr(
        "api.controllers.console.myownclone.ai_models._tenant_id", lambda: "test-tenant"
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


def test_ai_model_costs_prefers_rollup_rows(ai_client, monkeypatch):
    rollups = [
        SimpleNamespace(day=__import__("datetime").date(2026, 6, 23), invocations=4, prompt_tokens=40, completion_tokens=20)
    ]

    class ExecuteResult:
        def __init__(self, rows):
            self._rows = rows

        def scalars(self):
            return SimpleNamespace(all=lambda: self._rows)

        def scalar_one_or_none(self):
            return None  # maintenance flag reads return None (off)

    # Count ONLY rollup queries (skip maintenance middleware queries)
    rollup_calls = {"count": 0}

    def fake_execute(stmt):
        try:
            stmt_str = str(stmt)
        except Exception:
            stmt_str = ""
        if "system_settings" in stmt_str:
            return ExecuteResult([])
        rollup_calls["count"] += 1
        if rollup_calls["count"] == 1:
            return ExecuteResult(rollups)
        return ExecuteResult([])

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

    # Count only rollup queries (skip maintenance middleware queries)
    rollup_calls = {"count": 0}

    def fake_execute(stmt):
        try:
            stmt_str = str(stmt)
        except Exception:
            stmt_str = ""
        if "system_settings" in stmt_str:
            return ExecuteResult([])
        rollup_calls["count"] += 1
        if rollup_calls["count"] == 1:
            raise ProgrammingError("SELECT cost_daily_rollup", {}, Exception("relation does not exist"))
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
        try:
            stmt_str = str(stmt)
        except Exception:
            stmt_str = ""
        if "system_settings" in stmt_str:
            # Maintenance middleware query - return empty
            return SimpleNamespace(scalar_one_or_none=lambda: None)
        # Both tables missing - always raise
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
