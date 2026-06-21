"""Smoke test verifying SQLAlchemy column redeclaration works at runtime.

Tests that Tenant and Account models correctly persist and recall fields
including the redeclared id (UUID4), created_at, updated_at, and custom columns.
"""

from __future__ import annotations

import uuid
from datetime import datetime

from api.extensions import db
from api.models.account import Account, Tenant


def test_tenant_and_account_models_create_and_persist(app):
    """Verify Tenant and Account models create, persist, and recall correctly.

    This smoke test confirms that SQLAlchemy column redeclaration (id, created_at,
    updated_at) works at runtime in the ORM layer.

    Uses unique slug/email to avoid collisions when conftest uses a file-based
    SQLite (test.db) where db.drop_all() may not fully purge all data between
    test runs.
    """
    unique = uuid.uuid4().hex[:8]
    with app.app_context():
        # --- Tenant ------------------------------------------------------------
        t = Tenant(name="Acme", plan="pro", slug=f"acme-{unique}")
        db.session.add(t)
        db.session.flush()  # populate t.id

        assert t.id is not None, "Tenant.id should be populated after flush"
        assert len(t.id) == 36, f"Tenant.id should be UUID4 (36 chars), got {len(t.id)}"

        assert t.created_at is not None, "Tenant.created_at should be set"
        assert isinstance(t.created_at, datetime), (
            f"Tenant.created_at should be datetime, got {type(t.created_at)}"
        )

        assert t.updated_at is not None, "Tenant.updated_at should be set"

        # --- Account -----------------------------------------------------------
        a = Account(
            email=f"admin-{unique}@acme.com",
            tenant_id=t.id,
            role="platform_admin",
        )
        db.session.add(a)
        db.session.commit()

        # --- Fetch-back verification ------------------------------------------
        t_fetched = db.session.get(Tenant, t.id)
        a_fetched = db.session.get(Account, a.id)

        assert t_fetched is not None, "Fetched Tenant should not be None"
        assert t_fetched.name == "Acme"
        assert t_fetched.plan == "pro"
        assert t_fetched.slug == f"acme-{unique}"
        assert t_fetched.id == t.id
        assert isinstance(t_fetched.created_at, datetime)
        assert isinstance(t_fetched.updated_at, datetime)

        assert a_fetched is not None, "Fetched Account should not be None"
        assert a_fetched.email == f"admin-{unique}@acme.com"
        assert a_fetched.tenant_id == t.id
        assert a_fetched.role == "platform_admin"
        assert isinstance(a_fetched.created_at, datetime)
        assert isinstance(a_fetched.updated_at, datetime)