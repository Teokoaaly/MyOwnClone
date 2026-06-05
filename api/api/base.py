"""Base classes for MyOwnClone SQLAlchemy models."""
from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Any

import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

Base = declarative_base()


def naive_utc_now() -> datetime:
    return datetime.now(timezone.utc).replace(tzinfo=None)


class TypeBase(Base):
    """Base class for all MyOwnClone models — inherits from Base for SQLAlchemy 2.x."""
    __abstract__ = True
    __allow_unmapped__ = True  # Allow mixed annotation styles

    id: Mapped[str] = mapped_column(
        sa.String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )
    created_at: Mapped[datetime] = mapped_column(
        sa.DateTime,
        default=naive_utc_now,
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        sa.DateTime,
        default=naive_utc_now,
        onupdate=naive_utc_now,
        nullable=False
    )


class DefaultFieldsDCMixin:
    """Mixin providing created_at, updated_at, created_by fields."""
    __allow_unmapped__ = True

    created_at: Any
    updated_at: Any
    created_by: Any


def uuidv7() -> str:
    """Generate a UUIDv7 string."""
    return str(uuid.uuid7())
