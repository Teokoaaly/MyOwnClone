"""Account and Tenant SQLAlchemy models for MyOwnClone admin.

These map to the base `accounts` and `tenants` tables inherited from the Dify
platform. MyOwnClone migrations (`b2c3d4e5f6a7`) add extra columns to both:

    tenants  + slug, plan, custom_domain, subscription_status,
              stripe_customer_id, stripe_subscription_id
    accounts + role

We declare only the columns our admin endpoints read; the remaining base
columns are still present in the live database and ORM queries that omit them
keep working (SQLAlchemy will populate from defaults or ignore unmapped
columns at INSERT/UPDATE time).

Dataclass note: SQLAlchemy 2.x's `MappedAsDataclass` (set up in
`api.api.base.TypeBase`) requires every `init=True` field to have an explicit
Python `default`. Optional columns with no Python default are written with
`default=None` or `default="literal"` so the generated `__init__` stays
well-formed.
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import DateTime, String, func, text
from sqlalchemy.orm import Mapped, mapped_column

from ..base import TypeBase
from ..db_types import LongText


# Canonical plan names. The DB stores them in Spanish because the seed
# migration (`c3d4e5f6a7b8`) uses Spanish labels, so we map both ways.
PLAN_NAME_ALIASES_DB_TO_API: dict[str, str] = {
    "básico": "basic",
    "basico": "basic",
    "pro": "pro",
    "escala": "scale",
    "enterprise": "enterprise",
    "trial": "trial",
}

PLAN_NAME_ALIASES_API_TO_DB: dict[str, str] = {v: k for k, v in PLAN_NAME_ALIASES_DB_TO_API.items()}

# Active statuses for the "active_tenants" metric.
# Drizzle uses `active`, the Dify base historically uses `normal`. We accept
# both to remain stable across deployments.
ACTIVE_TENANT_STATUSES: tuple[str, ...] = ("active", "normal", "trial")


def _new_uuid() -> str:
    return str(uuid.uuid4())


def _utcnow() -> datetime:
    return datetime.now(timezone.utc).replace(tzinfo=None)


class Tenant(TypeBase):
    """A workspace / customer account on the MyOwnClone platform.

    Multi-tenant boundary: every other MyOwnClone table scopes by `tenant_id`.
    """

    __tablename__ = "tenants"

    # Base columns (Dify platform)
    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=_new_uuid,
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[Optional[str]] = mapped_column(
        String(20), nullable=True, default="normal"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=_utcnow,
        server_default=func.current_timestamp(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=True,
        default=_utcnow,
        server_default=func.current_timestamp(),
        onupdate=_utcnow,
    )

    # MyOwnClone additions (migration b2c3d4e5f6a7)
    slug: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True, unique=True, default=None
    )
    plan: Mapped[Optional[str]] = mapped_column(
        String(20), nullable=True, default="básico", server_default=text("'básico'")
    )
    custom_domain: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True, default=None
    )
    subscription_status: Mapped[Optional[str]] = mapped_column(
        String(20), nullable=True, default="trial", server_default=text("'trial'")
    )
    stripe_customer_id: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True, default=None
    )
    stripe_subscription_id: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True, default=None
    )

    def __repr__(self) -> str:  # pragma: no cover - debug helper
        return f"<Tenant id={self.id!r} name={self.name!r} plan={self.plan!r} status={self.status!r}>"


class Account(TypeBase):
    """A user account belonging to a tenant.

    `role` is the only MyOwnClone-owned column. The remaining base columns
    (id, email, password, name, tenant_id, avatar, ...) are inherited from
    Dify and not declared here, but queries can still filter by `id` and
    `role` without issue.
    """

    __tablename__ = "accounts"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=_new_uuid,
    )
    tenant_id: Mapped[Optional[str]] = mapped_column(
        String(36), nullable=True, default=None
    )
    email: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True, default=None
    )
    name: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True, default=None
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=True,
        default=_utcnow,
        server_default=func.current_timestamp(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=True,
        default=_utcnow,
        server_default=func.current_timestamp(),
        onupdate=_utcnow,
    )

    # MyOwnClone addition (migration b2c3d4e5f6a7)
    role: Mapped[Optional[str]] = mapped_column(
        String(20), nullable=True, default="member", server_default=text("'member'")
    )

    def __repr__(self) -> str:  # pragma: no cover - debug helper
        return f"<Account id={self.id!r} email={self.email!r} role={self.role!r}>"


# Re-export the LongText alias so consumers can keep their `from
# api.models.account import LongText` import working.
__all__ = [
    "Account",
    "Tenant",
    "LongText",
    "PLAN_NAME_ALIASES_API_TO_DB",
    "PLAN_NAME_ALIASES_DB_TO_API",
    "ACTIVE_TENANT_STATUSES",
]