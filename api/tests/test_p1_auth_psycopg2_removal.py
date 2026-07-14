"""Regression tests for P1.10 (H-10): auth.py uses Flask-SQLAlchemy instead
of raw psycopg2 per-login connections (DoS amplifier + bypasses pool).

Covers:
- _get_db_conn / psycopg2.connect removed from api.controllers.console.auth
- _lookup_account_via_sqlalchemy uses db.session (Account model)
- Login endpoint returns 401 (not 500) for missing accounts, when DB
  lookup fails. Bad-credentials and missing-table paths are handled.
- Invalid stored hash (legacy md5/plain) returns 401 not 500.
"""
from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import patch

import pytest


# ── Source-level checks (where the security lives) ─────────────────────

class TestAuthNoLongerUsesRawPsycopg2:
    """H-10 core: the per-login psycopg2.connect call must be gone."""

    def test_psycopg2_import_removed(self):
        from api.controllers.console import auth as auth_mod
        import inspect
        source = inspect.getsource(auth_mod)
        assert "import psycopg2" not in source, (
            "auth.py must not import psycopg2 directly (use Flask-SQLAlchemy)"
        )

    def test_get_db_conn_removed(self):
        from api.controllers.console import auth as auth_mod
        import inspect
        source = inspect.getsource(auth_mod)
        assert "def _get_db_conn" not in source, (
            "_get_db_conn (raw psycopg2.connect) must be removed (H-10)"
        )
        assert "psycopg2.connect" not in source, (
            "psycopg2.connect must not be called from auth.py (H-10)"
        )

    def test_login_uses_sqlalchemy_session(self):
        from api.controllers.console import auth as auth_mod
        import inspect
        source = inspect.getsource(auth_mod.login)
        # The login function must delegate to the helper.
        assert "_lookup_account_via_sqlalchemy" in source, (
            "login() must use the SQLAlchemy-backed lookup helper"
        )
        # And must NOT contain psycopg2/conn patterns.
        assert "cur = conn.cursor" not in source, (
            "login() must not use raw cursor pattern (H-10)"
        )


class TestLookupAccountViaSqlalchemy:
    """The new helper returns dict-shaped rows with the canonical keys."""

    def test_returns_none_when_account_missing(self, monkeypatch):
        from api.controllers.console import auth as auth_mod
        fake_session = SimpleNamespace(
            execute=lambda *_a, **_kw: SimpleNamespace(scalar_one_or_none=lambda: None)
        )
        with patch.object(auth_mod, "db") as fake_db:
            fake_db.session = fake_session
            assert auth_mod._lookup_account_via_sqlalchemy("noone@x") is None

    def test_returns_dict_when_account_found(self, monkeypatch):
        from api.controllers.console import auth as auth_mod
        fake_account = SimpleNamespace(
            id="acc-1",
            email="alice@example.com",
            password="$2b$10$abcdef",
            name="Alice",
            role="admin",
            tenant_id="tenant-1",
        )
        fake_session = SimpleNamespace(
            execute=lambda *_a, **_kw: SimpleNamespace(
                scalar_one_or_none=lambda: fake_account
            )
        )
        with patch.object(auth_mod, "db") as fake_db:
            fake_db.session = fake_session
            row = auth_mod._lookup_account_via_sqlalchemy("alice@example.com")
        assert row is not None
        assert row["email"] == "alice@example.com"
        assert row["password_hash"] == "$2b$10$abcdef"  # alias of Account.password
        assert row["tenant_id"] == "tenant-1"

    def test_returns_none_on_programming_error(self, monkeypatch):
        """If 'accounts' table is missing (ProgrammingError), helper returns None
        without raising (legacy users table fallback happens separately or also fails)."""
        from api.controllers.console import auth as auth_mod
        from sqlalchemy.exc import ProgrammingError

        def boom(*_a, **_kw):
            raise ProgrammingError("SELECT", {}, Exception("UndefinedTable"))
        fake_session = SimpleNamespace(execute=boom)
        # Legacy fallback also raises -> helper returns None overall.
        with patch.object(auth_mod, "db") as fake_db:
            fake_db.session = fake_session
            assert auth_mod._lookup_account_via_sqlalchemy("x@y") is None


class TestLoginEndpointRejectsBadCredentials:
    """H-10: login must NOT 500 on bad credentials / missing accounts."""

    def test_missing_account_returns_401(self, app):
        from api.controllers.console import auth as auth_mod
        with patch.object(auth_mod, "_lookup_account_via_sqlalchemy", return_value=None):
            r = app.test_client().post(
                "/console/api/auth/login",
                json={"email": "noone@example.com", "password": "wrong"},
            )
            assert r.status_code == 401, (
                f"login must return 401 for missing account, got {r.status_code}"
            )

    def test_invalid_stored_hash_returns_401_not_500(self, app, monkeypatch):
        """Legacy password hashes (md5/plain) would raise ValueError on bcrypt;
        the endpoint must catch it and return 401, not 500."""
        import bcrypt as _bcrypt
        from api.controllers.console import auth as auth_mod

        # Stored "hash" that bcrypt will reject (not a valid bcrypt string).
        fake_row = {
            "id": "acc-1", "email": "a@b", "password_hash": "not-a-bcrypt-hash",
            "name": "A", "role": "user", "tenant_id": "t1",
        }
        monkeypatch.setattr(auth_mod, "_lookup_account_via_sqlalchemy", lambda _e: fake_row)
        # Force bcrypt to throw (defensive: in practice it raises ValueError).
        def boom(*_a, **_kw):
            raise ValueError("Invalid salt")
        monkeypatch.setattr(_bcrypt, "checkpw", boom)

        r = app.test_client().post(
            "/console/api/auth/login",
            json={"email": "a@b", "password": "anything"},
        )
        assert r.status_code == 401, (
            f"login must return 401 on invalid stored hash, got {r.status_code}: {r.get_data(as_text=True)}"
        )
