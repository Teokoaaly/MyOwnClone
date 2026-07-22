from __future__ import annotations

import inspect
from types import SimpleNamespace
from unittest.mock import patch

import pytest
from flask import Flask, g

from api.controllers.console.myownclone import admin_platform, clone, prompts_ctrl
from api.core.ingestion import UnsafeURLError, _extract_from_url, _is_safe_url
from api.libs.login import login_required


def _protected_app() -> Flask:
    app = Flask(__name__)
    app.config["TESTING"] = True

    @app.get("/protected")
    @login_required
    def protected():
        return {
            "account_id": g.account_id,
            "tenant_id": g.tenant_id,
            "role": g.account_role,
            "email": g.account_email,
        }

    return app


def _db_account() -> SimpleNamespace:
    return SimpleNamespace(
        id="11111111-1111-1111-1111-111111111111",
        tenant_id="22222222-2222-2222-2222-222222222222",
        role="member",
        status="active",
        is_platform_admin=False,
        email="member@example.com",
    )


def test_jwt_claims_are_replaced_by_database_identity(monkeypatch) -> None:
    account = _db_account()
    forged_claims = {
        "sub": account.id,
        "tenant_id": "33333333-3333-3333-3333-333333333333",
        "role": "platform_admin",
        "email": "attacker@example.com",
    }

    with (
        patch("api.libs.login._verify_token", return_value=forged_claims),
        patch("api.extensions.ext_database.db") as fake_db,
    ):
        fake_db.session.get.return_value = account
        response = (
            _protected_app()
            .test_client()
            .get("/protected", headers={"Authorization": "Bearer signed-token"})
        )

    assert response.status_code == 200
    assert response.get_json() == {
        "account_id": account.id,
        "tenant_id": account.tenant_id,
        "role": account.role,
        "email": account.email,
    }


def test_service_headers_cannot_override_database_identity(monkeypatch) -> None:
    account = _db_account()
    monkeypatch.setenv("SERVICE_API_KEY", "service-secret")
    monkeypatch.delenv("ALLOW_DEV_SERVICE_KEY", raising=False)

    with patch("api.extensions.ext_database.db") as fake_db:
        fake_db.session.get.return_value = account
        response = (
            _protected_app()
            .test_client()
            .get(
                "/protected",
                headers={
                    "X-API-Key": "service-secret",
                    "X-User-Id": account.id,
                    "X-Tenant-Id": "33333333-3333-3333-3333-333333333333",
                    "X-User-Role": "platform_admin",
                    "X-User-Email": "attacker@example.com",
                },
            )
        )

    assert response.status_code == 200
    assert response.get_json()["tenant_id"] == account.tenant_id
    assert response.get_json()["role"] == account.role
    assert response.get_json()["email"] == account.email


def test_unknown_forwarded_account_is_rejected(monkeypatch) -> None:
    monkeypatch.setenv("SERVICE_API_KEY", "service-secret")
    with patch("api.extensions.ext_database.db") as fake_db:
        fake_db.session.get.return_value = None
        response = (
            _protected_app()
            .test_client()
            .get(
                "/protected",
                headers={
                    "X-API-Key": "service-secret",
                    "X-User-Id": "11111111-1111-1111-1111-111111111111",
                    "X-User-Role": "member",
                },
            )
        )

    assert response.status_code == 401


def test_clone_prompt_update_checks_tenant_before_loading_prompt() -> None:
    source = clone.CloneModePromptApi.put.__wrapped__.__wrapped__.__wrapped__
    assert "_clone_owned_by_tenant" in source.__code__.co_names


@pytest.mark.parametrize(
    "handler", [clone.CloneAvatarApi.post, clone.CloneAvatarApi.delete]
)
def test_clone_avatar_handlers_scope_clone_query_by_tenant(handler) -> None:
    source = inspect.getsource(handler.__wrapped__.__wrapped__.__wrapped__)
    assert "CloneConfig.tenant_id == tenant_id" in source
    assert "db.session.get(CloneConfig" not in source


def test_source_and_prompt_handlers_use_authoritative_tenant_id() -> None:
    source_handler = inspect.getsource(inspect.unwrap(clone.SourceListApi.get))
    prompt_handler = inspect.getsource(inspect.unwrap(prompts_ctrl.PromptListApi.get))
    assert "tenant.id" not in source_handler
    assert "tenant.id" not in prompt_handler
    assert "tenant_id" in source_handler
    assert "tenant_id" in prompt_handler


def test_prompt_creation_requires_an_owned_clone() -> None:
    assert prompts_ctrl.PromptCreatePayload.model_fields["clone_id"].is_required()


def test_ssrf_rejects_userinfo_urls() -> None:
    with pytest.raises(UnsafeURLError, match="userinfo"):
        _is_safe_url("https://user:password@8.8.8.8/document")


def test_url_ingestion_disables_automatic_redirects(monkeypatch) -> None:
    calls: list[str] = []

    def fake_get(url: str, **kwargs):
        assert kwargs["allow_redirects"] is False
        calls.append(url)
        return SimpleNamespace(
            status_code=302,
            headers={"Location": "http://127.0.0.1/admin"},
            text="",
            raise_for_status=lambda: None,
        )

    monkeypatch.setattr("requests.get", fake_get)
    assert _extract_from_url("https://8.8.8.8/start") == ""
    assert calls == ["https://8.8.8.8/start"]


def test_admin_audit_endpoint_reads_persistent_audit_log() -> None:
    names = admin_platform.AdminAuditLogApi.get.__wrapped__.__wrapped__.__wrapped__.__code__.co_names
    assert "AuditLog" in names
    assert "ImpersonationLog" not in names


def test_courtesy_account_creation_is_audited() -> None:
    assert hasattr(admin_platform.AdminCourtesyAccountApi.post, "__wrapped__")
    source = admin_platform.AdminCourtesyAccountApi.post
    wrapped_names: set[str] = set()
    while hasattr(source, "__wrapped__"):
        wrapped_names.update(source.__code__.co_names)
        source = source.__wrapped__
    assert "log_audit_action" in wrapped_names


@pytest.mark.parametrize("is_platform_admin,expected", [(False, False), (True, True)])
def test_admin_permission_comes_from_database(
    is_platform_admin, expected, monkeypatch
) -> None:
    account = SimpleNamespace(is_platform_admin=is_platform_admin)
    result = SimpleNamespace(scalar_one_or_none=lambda: account)
    monkeypatch.setattr(
        admin_platform.db.session,
        "execute",
        lambda statement: result,
    )

    assert admin_platform._is_platform_admin("account-id") is expected
