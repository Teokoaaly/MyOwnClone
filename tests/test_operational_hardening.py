"""Operational hardening tests for production readiness."""
from types import SimpleNamespace

import pytest


def test_database_url_takes_precedence(monkeypatch):
    from api.app_factory import _database_uri

    monkeypatch.setenv("DATABASE_URL", "postgresql://u:p@db.example.com:5432/app")
    monkeypatch.setenv("DB_HOST", "ignored")

    assert _database_uri() == "postgresql://u:p@db.example.com:5432/app"


def test_psycopg_url_is_normalized_for_psycopg2(monkeypatch):
    from api.app_factory import _database_uri

    monkeypatch.setenv("DATABASE_URL", "postgresql+psycopg://u:p@db.example.com:5432/app")

    assert _database_uri() == "postgresql://u:p@db.example.com:5432/app"


def test_database_uri_falls_back_to_db_parts(monkeypatch):
    from api.app_factory import _database_uri

    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.setenv("DB_USER", "postgres")
    monkeypatch.setenv("DB_PASSWORD", "secret")
    monkeypatch.setenv("DB_HOST", "db_postgres")
    monkeypatch.setenv("DB_PORT", "5432")
    monkeypatch.setenv("DB_NAME", "myownclone")

    assert _database_uri() == "postgresql://postgres:secret@db_postgres:5432/myownclone"


def test_healthz_returns_ready_when_dependencies_ok(client, monkeypatch):
    """P0.6 (C-21): /healthz contrato real = readiness check.

    ``status`` es ``ready`` (no ``ok``) y se incluye ``checks`` por componente.
    DB, Redis y Ollama se mockean porque la suite CI no garantiza que esten
    levantados (no hay Postgres/Redis/Ollama reales en el entorno de test).
    """
    from api.app_factory import db

    monkeypatch.setattr(db.session, "execute", lambda *_a, **_kw: object())
    monkeypatch.setattr("api.core.readiness._redis_ready", lambda: (True, None))
    monkeypatch.setattr(
        "api.core.readiness.ModelRegistry.resolve",
        lambda *_a, **_kw: SimpleNamespace(provider="openai"),
    )
    # Stub Ollama probe to avoid real network in CI.
    monkeypatch.setattr(
        "requests.get",
        lambda *a, **k: type("R", (), {"status_code": 200})(),
    )

    response = client.get("/healthz")

    assert response.status_code == 200
    body = response.get_json()
    assert body["status"] == "ready"
    assert body["checks"]["database"] == "ok"
    assert body["checks"]["redis"] == "ok"
    assert body["checks"]["ollama"] == "ok"


def test_readyz_is_liveness_and_always_ready(app):
    """P0.6 (C-21): /readyz es liveness, no readiness.

    Siempre devuelve 200 ``{"status": "ready"}`` si el proceso atiende.
    No mockea dependencias porque readyz no las chequea.
    """
    response = app.test_client().get("/readyz")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ready"}


def test_healthz_returns_503_when_database_fails(app, monkeypatch):
    """P0.6 (C-21): el 503 por DB caida lo devuelve /healthz, no /readyz.

    Antes este test apuntaba a /readyz (liveness) y afirmaba 503, lo cual
    era estructuralmente imposible: /readyz siempre devuelve 200. Ahora
    apunta al endpoint correcto (/healthz, readiness) y verifica ademas
    que el body no expone texto interno del driver (info leak).
    """
    from api.app_factory import db

    def fail_execute(*_args, **_kwargs):
        raise RuntimeError("db unavailable")

    monkeypatch.setattr(db.session, "execute", fail_execute)
    monkeypatch.setattr(db.session, "rollback", lambda: None)
    monkeypatch.setattr("api.core.readiness._redis_ready", lambda: (True, None))
    monkeypatch.setattr(
        "api.core.readiness.ModelRegistry.resolve",
        lambda *_a, **_kw: SimpleNamespace(provider="openai"),
    )
    monkeypatch.setattr(
        "requests.get",
        lambda *a, **k: type("R", (), {"status_code": 200})(),
    )

    response = app.test_client().get("/healthz")

    assert response.status_code == 503
    body = response.get_json()
    assert body["status"] == "degraded"
    assert body["checks"]["database"] == "error"
    # Info leak guard: el texto interno del driver NO debe estar en el body.
    assert "db unavailable" not in response.get_data(as_text=True)


def test_dev_service_key_is_rejected_in_production(monkeypatch):
    from api.libs.login import _allow_dev_service_key

    monkeypatch.setenv("FLASK_ENV", "production")
    monkeypatch.setenv("ALLOW_DEV_SERVICE_KEY", "true")

    assert _allow_dev_service_key() is False


def test_dev_service_key_can_be_allowed_only_outside_production(monkeypatch):
    from api.libs.login import _allow_dev_service_key

    monkeypatch.setenv("FLASK_ENV", "development")
    monkeypatch.setenv("ALLOW_DEV_SERVICE_KEY", "true")

    assert _allow_dev_service_key() is True
