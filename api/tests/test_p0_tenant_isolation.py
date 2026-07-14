"""Regression tests for P0.4: tenant isolation / IDOR fixes (auditoria 2026-07-13).

Covers:
- H-03: ``SourceListApi`` (clone.py) no usa prefix-like; requiere que el
  clone_id pertenezca al tenant (GET y POST).
- H-04: ``PromptListApi``/``DetailApi``/``VersionApi``/``ActiveApi``
  (prompts_ctrl.py) aplican el predicado de tenant en cada operacion.

Estos tests validan la logica del helper ``_clone_owned_by_tenant`` (donde
reside la seguridad) sin requerir PostgreSQL real: mockean ``db.session``.
Tambien amplian la cobertura de ``test_tenant_scoping`` verificando que los
nuevos endpoints sources/prompts requieren auth.
"""
from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import patch

import pytest

from api.controllers.console.myownclone.clone import (
    _clone_owned_by_tenant as clone_owns,
)
from api.controllers.console.myownclone.prompts_ctrl import (
    _clone_owned_by_tenant as prompts_owns,
)


# ── Helper unit tests (where the security lives) ───────────────────────

class TestCloneOwnedByTenant:
    """The helper returns True only when a CloneConfig row exists scoped to
    the caller's tenant. Both clone.py and prompts_ctrl.py expose an
    identical helper; both must behave the same."""

    @pytest.mark.parametrize("helper", [clone_owns, prompts_owns])
    def test_returns_false_for_empty_clone_id(self, helper):
        assert helper(None, "tenant-1") is False
        assert helper("", "tenant-1") is False

    @pytest.mark.parametrize("helper", [clone_owns, prompts_owns])
    def test_returns_false_for_empty_tenant_id(self, helper):
        assert helper("clone-1", None) is False
        assert helper("clone-1", "") is False

    @pytest.mark.parametrize("helper", [clone_owns, prompts_owns])
    def test_returns_true_when_clone_matches_tenant(self, helper, monkeypatch):
        """Mock the session to return a row for the matching (clone, tenant)."""
        fake_session = SimpleNamespace(
            execute=lambda _stmt: SimpleNamespace(
                scalar_one_or_none=lambda: "clone-1"  # truthy = found
            )
        )
        # Patch db on BOTH modules (each imports its own db symbol).
        import api.controllers.console.myownclone.clone as clone_mod
        import api.controllers.console.myownclone.prompts_ctrl as prompts_mod
        monkeypatch.setattr(clone_mod, "db", SimpleNamespace(session=fake_session))
        monkeypatch.setattr(prompts_mod, "db", SimpleNamespace(session=fake_session))
        assert helper("clone-1", "tenant-1") is True

    @pytest.mark.parametrize("helper", [clone_owns, prompts_owns])
    def test_returns_false_when_clone_belongs_to_other_tenant(self, helper, monkeypatch):
        """Mock the session to return None (no row) — the IDOR case."""
        fake_session = SimpleNamespace(
            execute=lambda _stmt: SimpleNamespace(
                scalar_one_or_none=lambda: None  # not found
            )
        )
        import api.controllers.console.myownclone.clone as clone_mod
        import api.controllers.console.myownclone.prompts_ctrl as prompts_mod
        monkeypatch.setattr(clone_mod, "db", SimpleNamespace(session=fake_session))
        monkeypatch.setattr(prompts_mod, "db", SimpleNamespace(session=fake_session))
        # clone-1 exists but belongs to tenant-OTHER, not tenant-1
        assert helper("clone-1", "tenant-1") is False


# ── Endpoint auth gate (no token -> 401) ───────────────────────────────

SOURCES_AND_PROMPTS_ENDPOINTS = [
    ("GET", "/console/api/myownclone/sources"),
    ("POST", "/console/api/myownclone/sources"),
    ("GET", "/console/api/myownclone/prompts"),
    ("POST", "/console/api/myownclone/prompts"),
    ("GET", "/console/api/myownclone/prompts/some-id"),
    ("POST", "/console/api/myownclone/prompts/some-id/versions"),
    ("GET", "/console/api/myownclone/prompts/active"),
]


@pytest.mark.parametrize("method,path", SOURCES_AND_PROMPTS_ENDPOINTS)
def test_sources_and_prompts_endpoints_require_auth(client, method, path):
    """P0.4: every sources/prompts endpoint must require auth (no 200 without token).

    This guards against regressions where a refactor drops the @login_required
    decorator. It does NOT verify the tenant predicate itself (that's the job
    of ``TestCloneOwnedByTenant`` above), but it ensures the gate is in place.
    """
    r = client.open(path, method=method)
    assert r.status_code != 200, (
        f"{method} {path} returned 200 without auth - endpoint unprotected!"
    )
    assert r.status_code not in (404, 405), (
        f"{method} {path} returned {r.status_code} - missing route or wrong method"
    )


# ── Source prefix-like regression (H-03) ────────────────────────────────

def test_source_list_no_longer_uses_prefix_like():
    """H-03 regression: the old code did ``Source.clone_id.like(f"{tenant}%")``
    which let tenant A read tenant B's sources by passing the exact clone_id.

    The new code uses a subquery against CloneConfig.id scoped by tenant_id.
    This test asserts the source file no longer contains the broken pattern
    in the SourceListApi.get handler.
    """
    import inspect
    from api.controllers.console.myownclone import clone as clone_mod

    source = inspect.getsource(clone_mod.SourceListApi.get)
    assert ".like(" not in source, (
        "SourceListApi.get still uses .like() for tenant scoping (H-03 regression)"
    )
    # The new code must reference CloneConfig for proper tenancy.
    assert "CloneConfig" in source, (
        "SourceListApi.get must scope via CloneConfig, not via clone_id prefix"
    )


def test_source_create_verifies_clone_ownership():
    """H-03 regression: SourceListApi.post must call _clone_owned_by_tenant
    before creating a Source (prevents cross-tenant source injection)."""
    import inspect
    from api.controllers.console.myownclone import clone as clone_mod

    source = inspect.getsource(clone_mod.SourceListApi.post)
    assert "_clone_owned_by_tenant" in source, (
        "SourceListApi.post must verify clone ownership before insert (H-03)"
    )


def test_prompts_list_without_clone_id_is_tenant_scoped():
    """H-04 residual (found by verifier): PromptListApi.get WITHOUT a clone_id
    query param must scope by the tenant's clone set, not return all prompts
    across tenants. Before, list_prompts(clone_id=None) ran select(Prompt)
    with no tenant filter — cross-tenant read of system instructions."""
    import inspect
    from api.controllers.console.myownclone import prompts_ctrl

    source = inspect.getsource(prompts_ctrl.PromptListApi.get)
    # The handler must build a tenant clone set and pass it to list_prompts
    # when no clone_id is supplied (the unfiltered path).
    assert "tenant_clone_ids" in source or "clone_ids=" in source, (
        "PromptListApi.get must scope the unfiltered list by tenant clone set "
        "(H-04 residual: cross-tenant prompt read)"
    )


def test_prompts_service_list_prompts_accepts_clone_ids():
    """H-04 residual: list_prompts must accept a clone_ids set for tenant
    scoping (not just a single clone_id)."""
    import inspect
    from api.core.prompts import PromptService

    sig = inspect.signature(PromptService.list_prompts)
    assert "clone_ids" in sig.parameters, (
        "PromptService.list_prompts must accept clone_ids for tenant scoping (H-04)"
    )
