"""Regression tests for P0.1: auth header lockdown + production-env unification
(auditoria 2026-07-13).

Covers:
- C-02: privileged roles forwarded via ``X-User-Role`` in the service-to-service
  path are confirmed against the DB before being honored. Prevents privilege
  escalation if ``SERVICE_API_KEY`` leaks.
- H-01: ``_allow_dev_service_key()`` and ``jwt_utils._get_secret_key()`` use the
  strict ``_is_production()`` criterion (staging counts as production), so the
  dev key / random per-process JWT secret can no longer leak into staging-like
  environments.
"""
from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import patch

import pytest

from api.libs.login import (
    _allow_dev_service_key,
    _load_authoritative_identity,
)


# ── H-01: production-env unification ───────────────────────────────────

class TestProductionEnvUnification:
    """H-01: ``_allow_dev_service_key`` must treat staging as production."""

    def test_dev_key_allowed_in_development(self, monkeypatch):
        monkeypatch.setenv("FLASK_ENV", "development")
        monkeypatch.setenv("ALLOW_DEV_SERVICE_KEY", "true")
        assert _allow_dev_service_key() is True

    def test_dev_key_blocked_in_production(self, monkeypatch):
        monkeypatch.setenv("FLASK_ENV", "production")
        monkeypatch.setenv("ALLOW_DEV_SERVICE_KEY", "true")
        assert _allow_dev_service_key() is False

    def test_dev_key_blocked_in_staging(self, monkeypatch):
        """H-01 regression: before, FLASK_ENV=staging fell through the
        ``not in ("production", "prod")`` check and ENABLED the dev key,
        while security_checks treated staging as production. Now unified."""
        monkeypatch.setenv("FLASK_ENV", "staging")
        monkeypatch.setenv("ALLOW_DEV_SERVICE_KEY", "true")
        assert _allow_dev_service_key() is False

    def test_dev_key_blocked_when_flag_unset(self, monkeypatch):
        monkeypatch.setenv("FLASK_ENV", "development")
        monkeypatch.delenv("ALLOW_DEV_SERVICE_KEY", raising=False)
        assert _allow_dev_service_key() is False

    def test_jwt_secret_strict_in_staging(self, monkeypatch):
        """H-01: jwt_utils._get_secret_key must refuse weak secrets in staging."""
        monkeypatch.setenv("FLASK_ENV", "staging")
        monkeypatch.setenv("JWT_SECRET_KEY", "")
        from api.libs.jwt_utils import _get_secret_key
        with pytest.raises(RuntimeError, match="must be set"):
            _get_secret_key()


class TestAuthoritativeIdentity:
    ACCOUNT_ID = "11111111-1111-1111-1111-111111111111"

    def test_platform_role_comes_from_database(self):
        account = SimpleNamespace(
            id=self.ACCOUNT_ID,
            tenant_id="22222222-2222-2222-2222-222222222222",
            role="member",
            status="active",
            is_platform_admin=True,
            email="admin@example.com",
        )
        with patch("api.extensions.ext_database.db") as fake_db:
            fake_db.session.get.return_value = account
            identity = _load_authoritative_identity(self.ACCOUNT_ID)

        assert identity is not None
        assert identity.role == "platform_admin"

    def test_normal_role_and_tenant_come_from_database(self):
        account = SimpleNamespace(
            id=self.ACCOUNT_ID,
            tenant_id="22222222-2222-2222-2222-222222222222",
            role="owner",
            status="active",
            is_platform_admin=False,
            email="owner@example.com",
        )
        with patch("api.extensions.ext_database.db") as fake_db:
            fake_db.session.get.return_value = account
            identity = _load_authoritative_identity(self.ACCOUNT_ID)

        assert identity is not None
        assert identity.tenant_id == account.tenant_id
        assert identity.role == "owner"

    def test_unknown_or_inactive_account_is_rejected(self):
        with patch("api.extensions.ext_database.db") as fake_db:
            fake_db.session.get.return_value = None
            assert _load_authoritative_identity(self.ACCOUNT_ID) is None

            fake_db.session.get.return_value = SimpleNamespace(status="banned")
            assert _load_authoritative_identity(self.ACCOUNT_ID) is None


# ── C-01: nginx config no longer contains the leaked key ───────────────

class TestNginxConfigSanitized:
    """C-01 regression: the leaked SERVICE_API_KEY must not appear in the
    committed nginx config, and no X-User-Role/X-User-Id/X-User-Email may be
    injected by nginx."""

    LEAKED_KEY = "XimE6gtCeMepQ3WC8RwIBI7hgSJfAiozCdY95oEz1qBDm18h"

    def test_leaked_key_absent_from_nginx_conf(self):
        import pathlib
        conf = pathlib.Path("ops/nginx-myownclone.conf").read_text(encoding="utf-8")
        assert self.LEAKED_KEY not in conf, (
            "C-01 regression: leaked SERVICE_API_KEY still in nginx-myownclone.conf"
        )

    def test_nginx_does_not_inject_identity_headers(self):
        """C-01/C-02: nginx must not inject X-User-Role/X-User-Id/X-User-Email."""
        import pathlib
        conf = pathlib.Path("ops/nginx-myownclone.conf").read_text(encoding="utf-8")
        for header in ("X-User-Role", "X-User-Id", "X-User-Email"):
            # Allow the header to appear in comments but not in proxy_set_header directives.
            for line in conf.splitlines():
                stripped = line.strip()
                if stripped.startswith("proxy_set_header") and header in stripped:
                    pytest.fail(
                        f"C-01/C-02 regression: nginx injects {header}: {stripped!r}"
                    )

    def test_nginx_does_not_inject_hardcoded_api_key(self):
        """C-01: nginx must not set X-API-Key to a literal value (only forward)."""
        import pathlib
        import re
        conf = pathlib.Path("ops/nginx-myownclone.conf").read_text(encoding="utf-8")
        # Find any proxy_set_header X-API-Key "..." with a literal string.
        pattern = re.compile(r'proxy_set_header\s+X-API-Key\s+"[^"]+"\s*;', re.IGNORECASE)
        match = pattern.search(conf)
        assert match is None, (
            f"C-01 regression: nginx sets a literal X-API-Key: {match.group(0)!r}"
        )
