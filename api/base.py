"""Base classes for MyOwnClone SQLAlchemy models.

These are minimal stubs to satisfy imports. The actual base platform
provides the real implementations. For standalone operation, these stubs
provide enough for the models to be loaded.
"""

import uuid
from datetime import datetime, timezone
from typing import Optional


def naive_utc_now() -> datetime:
    """Return naive datetime in UTC."""
    return datetime.now(timezone.utc).replace(tzinfo=None)


class TypeBase:
    """Base class for all MyOwnClone models."""

    id: str
    created_at: datetime
    updated_at: datetime

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class DefaultFieldsDCMixin:
    """Mixin providing created_at and updated_at fields."""

    created_at: datetime
    updated_at: datetime


def uuidv7() -> str:
    """Generate a UUIDv7 string."""
    return str(uuid.uuid4())