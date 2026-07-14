"""Regression tests for P1.2: audit-trail wired into admin endpoints
(auditoria 2026-07-13, C-16/C-03).

Covers:
- audit_log table created via Alembic migration (no runtime DDL).
- @audit_action decorator logs successful 2xx state changes.
- audit_action fails open: a DB error must not break the endpoint.
- AdminTenantsApi.post/put/delete, AdminImpersonateApi.post, and
  AdminStopImpersonateApi.post are wired with @audit_action.
"""
from __future__ import annotations

import inspect

import pytest

from api.middleware import audit_trail
from api.middleware.audit_trail import AuditLog, audit_action, log_audit_action


# ── Source-level checks (where the security lives) ─────────────────────

def test_audit_log_migration_exists():
    """C-16: audit_log must be created via Alembic, not runtime DDL."""
    from pathlib import Path
    repo = Path(__file__).resolve().parent.parent.parent
    mig = repo / "api" / "migrations" / "versions" / "2026_07_14_0002_add_audit_log_table.py"
    assert mig.exists(), f"Migration missing: {mig}"
    src = mig.read_text(encoding="utf-8")
    assert "audit_log" in src and "create_table" in src
    assert "downgrade" in src


def test_audit_trail_no_runtime_ddl():
    """The old _ensure_table runtime DDL must be gone (cold-start race)."""
    assert not hasattr(audit_trail, "_ensure_table"), (
        "_ensure_table (runtime DDL) must be removed; audit_log is now a migration"
    )
    assert not hasattr(audit_trail, "_table_created"), (
        "_table_created flag is no longer needed"
    )


def test_audit_action_decorator_imported_in_admin_platform():
    """P1.2: admin endpoints must import and use @audit_action."""
    from api.controllers.console.myownclone import admin_platform
    assert "audit_action" in dir(admin_platform), (
        "admin_platform.py must import audit_action"
    )


def test_admin_endpoints_have_audit_decorator():
    """Every state-changing admin endpoint must be wired."""
    from api.controllers.console.myownclone import admin_platform
    src = inspect.getsource(admin_platform)
    expected_actions = [
        "admin.tenant.create",
        "admin.tenant.update",
        "admin.tenant.delete",
        "admin.impersonate.start",
        "admin.impersonate.stop",
    ]
    for action in expected_actions:
        assert f'@audit_action("{action}"' in src, (
            f"Missing @audit_action(\"{action}\") in admin_platform.py"
        )


# ── Behavioral checks ──────────────────────────────────────────────────

class TestAuditActionDecorator:
    """The decorator must log only on 2xx POST/PUT/PATCH/DELETE."""

    def test_logs_on_successful_post(self, app, monkeypatch):
        from flask import g
        captured = []
        monkeypatch.setattr(
            "api.middleware.audit_trail.log_audit_action",
            lambda **kw: captured.append(kw),
        )

        @audit_action("test.action", resource_type="test")
        def handler():
            return {"ok": True}, 201

        with app.test_request_context("/x", method="POST"):
            handler()
        assert len(captured) == 1
        assert captured[0]["action"] == "test.action"
        assert captured[0]["resource_type"] == "test"

    def test_does_not_log_on_4xx(self, app, monkeypatch):
        captured = []
        monkeypatch.setattr(
            "api.middleware.audit_trail.log_audit_action",
            lambda **kw: captured.append(kw),
        )

        @audit_action("test.action")
        def handler():
            return {"error": "no"}, 400

        with app.test_request_context("/x", method="POST"):
            handler()
        assert captured == []

    def test_does_not_log_on_get(self, app, monkeypatch):
        captured = []
        monkeypatch.setattr(
            "api.middleware.audit_trail.log_audit_action",
            lambda **kw: captured.append(kw),
        )

        @audit_action("test.action")
        def handler():
            return {"ok": True}, 200

        with app.test_request_context("/x", method="GET"):
            handler()
        assert captured == []

    def test_log_audit_action_fails_open_on_db_error(self, monkeypatch):
        """log_audit_action wraps its work in try/except and logs the
        failure instead of propagating. This guarantees a DB outage never
        breaks user-facing requests.
        """
        from api.extensions.ext_database import db

        class BoomSession:
            def add(self, *_a, **_kw):
                raise RuntimeError("db down")
            def commit(self, *_a, **_kw):
                raise RuntimeError("db down")
            def rollback(self, *_a, **_kw):
                pass
        monkeypatch.setattr(db, "session", BoomSession())

        # Must NOT raise — exception is swallowed by the try/except inside.
        log_audit_action(action="test.action", resource_type="test")
