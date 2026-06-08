"""Base classes for MyOwnClone SQLAlchemy models.

These are minimal stubs to satisfy imports. The actual base platform
provides the real implementations. For standalone operation, these stubs
provide enough for the models to be loaded.
"""

import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


def naive_utc_now() -> datetime:
    """Return naive datetime in UTC."""
    return datetime.now(timezone.utc).replace(tzinfo=None)


class TypeBase(DeclarativeBase):
    """Base class for all MyOwnClone models.

    Provides the DeclarativeBase registry that SQLAlchemy needs
    to recognize subclasses as mapped ORM entities.
    Columns (id, created_at, updated_at) are declared on subclasses
    or via DefaultFieldsDCMixin to avoid conflicts.
    """

    __abstract__ = True


class DefaultFieldsDCMixin:
    """Mixin providing id, created_at and updated_at fields.

    Use this mixin for models that need standard audit columns.
    Models that define their own id/created_at/updated_at should
    NOT inherit from this mixin.
    """

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: uuidv7()
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=naive_utc_now, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=naive_utc_now, onupdate=naive_utc_now, nullable=False
    )


def uuidv7() -> str:
    """Generate a UUIDv7 string."""
    return str(uuid.uuid4())
