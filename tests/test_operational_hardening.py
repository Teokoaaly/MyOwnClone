"""Operational hardening tests for production readiness."""
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


def test_healthz_returns_ok(client):
    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_readyz_returns_ready_when_dependencies_pass(app, monkeypatch):
    from api.app_factory import db

    monkeypatch.setattr(db.session, "execute", lambda *_args, **_kwargs: object())
    monkeypatch.setattr("api.app_factory._redis_ready", lambda: (True, None))

    response = app.test_client().get("/readyz")

    assert response.status_code == 200
    assert response.get_json()["status"] == "ready"


def test_readyz_returns_503_when_database_fails(app, monkeypatch):
    from api.app_factory import db

    def fail_execute(*_args, **_kwargs):
        raise RuntimeError("db unavailable")

    monkeypatch.setattr(db.session, "execute", fail_execute)
    monkeypatch.setattr(db.session, "rollback", lambda: None)
    monkeypatch.setattr("api.app_factory._redis_ready", lambda: (True, None))

    response = app.test_client().get("/readyz")

    assert response.status_code == 503
    assert response.get_json()["status"] == "not_ready"


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
