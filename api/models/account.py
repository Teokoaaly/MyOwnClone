"""Account and Tenant models — full SQLAlchemy ORM for MyOwnClone standalone.

Replaces the previous stub classes that lacked SQLAlchemy mapping,
which caused InvalidRequestError on all admin queries.
"""
from __future__ import annotations

import enum
from datetime import datetime
from typing import Optional

import sqlalchemy as sa
from sqlalchemy import Boolean, DateTime, String, func, text
from sqlalchemy.orm import Mapped, mapped_column

from api.libs.datetime_utils import naive_utc_now
from api.libs.uuid_utils import uuidv7
from api.base import TypeBase


# ─── Enums ──────────────────────────────────────────────────────────────────

class TenantStatus(enum.StrEnum):
    NORMAL = "normal"
    SUSPENDED = "suspended"
    BANNED = "banned"


class SubscriptionStatus(enum.StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    TRIALING = "trialing"
    PAST_DUE = "past_due"
    CANCELLED = "cancelled"


class AccountRole(enum.StrEnum):
    OWNER = "owner"
    ADMIN = "admin"
    MEMBER = "member"
    PLATFORM_ADMIN = "platform_admin"


class AccountStatus(enum.StrEnum):
    ACTIVE = "active"
    BANNED = "banned"
    CLOSED = "closed"


# ─── Tenant ─────────────────────────────────────────────────────────────────

class Tenant(TypeBase):
    """Multi-tenant root. Every clone and user belongs to a tenant."""

    __tablename__ = "tenants"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        insert_default=lambda: str(uuidv7()),
        default=lambda: str(uuidv7()),
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[Optional[str]] = mapped_column(String(100), unique=True, nullable=True)

    # Subscription / billing
    plan: Mapped[str] = mapped_column(
        String(50), server_default=text("'básico'"), default="básico"
    )
    status: Mapped[str] = mapped_column(
        String(50), server_default=text("'normal'"), default="normal"
    )
    subscription_status: Mapped[str] = mapped_column(
        String(50), server_default=text("'inactive'"), default="inactive"
    )
    stripe_customer_id: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    stripe_subscription_id: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    trial_ends_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        insert_default=naive_utc_now,
        default=naive_utc_now,
        server_default=func.current_timestamp(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        insert_default=naive_utc_now,
        default=naive_utc_now,
        onupdate=naive_utc_now,
        server_default=func.current_timestamp(),
    )


# ─── Account ────────────────────────────────────────────────────────────────

class Account(TypeBase):
    """User account. Each account belongs to one tenant."""

    __tablename__ = "accounts"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        insert_default=lambda: str(uuidv7()),
        default=lambda: str(uuidv7()),
    )
    tenant_id: Mapped[str] = mapped_column(
        String(36),
        sa.ForeignKey("tenants.id", ondelete="CASCADE"),
        nullable=False,
    )
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True, comment="bcrypt hash"
    )
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    avatar: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    role: Mapped[str] = mapped_column(
        String(50), server_default=text("'owner'"), default="owner"
    )
    status: Mapped[str] = mapped_column(
        String(50), server_default=text("'active'"), default="active"
    )

    # Platform-wide admin flag (not tenant-scoped)
    is_platform_admin: Mapped[bool] = mapped_column(
        Boolean, server_default=text("false"), default=False
    )

    last_login_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        insert_default=naive_utc_now,
        default=naive_utc_now,
        server_default=func.current_timestamp(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        insert_default=naive_utc_now,
        default=naive_utc_now,
        onupdate=naive_utc_now,
        server_default=func.current_timestamp(),
    )


__all__ = [
    "Tenant",
    "TenantStatus",
    "SubscriptionStatus",
    "Account",
    "AccountRole",
    "AccountStatus",
]
