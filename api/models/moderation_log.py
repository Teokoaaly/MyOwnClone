"""Moderation event log — records every moderation check.

Used for audit, analytics, and improving moderation patterns.
"""
from __future__ import annotations

import hashlib
import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from api.base import TypeBase


def _sha256(s: str) -> str:
    """Return lowercase hex SHA-256 of a string."""
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


class ModerationEvent(TypeBase):
    """Every moderation check is logged here."""

    __tablename__ = "moderation_events"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        insert_default=lambda: str(uuid.uuid4()),
        default=lambda: str(uuid.uuid4()),
    )
    # Tenant that owns this check (null for platform-level checks)
    tenant_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    # SHA-256 of the moderated text
    text_hash: Mapped[str] = mapped_column(String(64), nullable=False)
    # Whether the content was flagged
    flagged: Mapped[bool] = mapped_column(nullable=False, default=False)
    # Moderation level: "level_1" (regex) or "level_2" (OpenAI)
    level: Mapped[str] = mapped_column(String(10), nullable=False)
    # Categories detected (JSON array of strings)
    categories: Mapped[Optional[str]] = mapped_column(nullable=True)
    # Model used for level 2 (null for level 1)
    model: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.current_timestamp(),
    )


__all__ = ["ModerationEvent", "_sha256"]
