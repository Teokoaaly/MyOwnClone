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

import os
from types import SimpleNamespace
from unittest.mock import patch

import pytest

from api.libs.login import (
    _allow_dev_service_key,
    _confirm_privileged_role,
    _PRIVILEGED_ROLES,
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


# ── C-02: privileged role confirmation ─────────────────────────────────

class TestPrivilegedRoleConfirmation:
    """C-02: forwarded privileged roles must be confirmed against the DB."""

    def test_non_privileged_role_passes_through_unchanged(self):
        """A normal user role is trusted from the proxy (it validated the JWT)."""
        assert _confirm_privileged_role("acc-1", "owner") == "owner"
        assert _confirm_privileged_role("acc-1", "user") == "user"
        assert _confirm_privileged_role("acc-1", "") == ""

    def test_privileged_role_confirmed_when_db_agrees(self, monkeypatch):
        """If the DB says the account IS platform_admin, the role is honored."""
        fake_row = ("platform_admin", True)
        fake_session = SimpleNamespace(
            execute=lambda _stmt: SimpleNamespace(first=lambda: fake_row)
        )
        with patch("api.extensions.ext_database.db") as fake_db:
            fake_db.session = fake_session
            for role in _PRIVILEGED_ROLES:
                assert _confirm_privileged_role("acc-1", role) == role

    def test_privileged_role_downgraded_when_db_disagrees(self, monkeypatch):
        """C-02 core: if X-User-Role claims platform_admin but the DB says the
        account is a normal user, downgrade to prevent escalation."""
        fake_row = ("user", False)
        fake_session = SimpleNamespace(
            execute=lambda _stmt: SimpleNamespace(first=lambda: fake_row)
        )
        with patch("api.extensions.ext_database.db") as fake_db:
            fake_db.session = fake_session
            assert _confirm_privileged_role("acc-1", "platform_admin") == "user"

    def test_privileged_role_downgraded_when_account_unknown(self, monkeypatch):
        """Unknown account claiming platform_admin -> downgrade (no privilege grant)."""
        fake_session = SimpleNamespace(
            execute=lambda _stmt: SimpleNamespace(first=lambda: None)
        )
        with patch("api.extensions.ext_database.db") as fake_db:
            fake_db.session = fake_session
            assert _confirm_privileged_role("ghost-account", "platform_admin") == "user"

    def test_privileged_role_downgraded_on_db_failure(self, monkeypatch):
        """C-02: DB error during role check must NOT grant privilege (fail closed)."""
        fake_session = SimpleNamespace(
            execute=lambda _stmt: (_ for _ in ()).throw(RuntimeError("db down"))
        )
        with patch("api.extensions.ext_database.db") as fake_db:
            fake_db.session = fake_session
            # Must NOT return platform_admin; falls back to "user".
            result = _confirm_privileged_role("acc-1", "platform_admin")
            assert result != "platform_admin"
            assert result == "user"


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
