"""ResponseFeedback — user feedback on AI responses.

Used for quality scoring and improving model selection.
"""
from __future__ import annotations

import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from api.base import TypeBase


class ResponseFeedback(TypeBase):
    """User feedback on AI responses."""

    __tablename__ = "response_feedback"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        insert_default=lambda: str(uuid.uuid4()),
        default=lambda: str(uuid.uuid4()),
    )
    # Tenant that owns this feedback
    tenant_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    # FK to ai_invocations.id
    invocation_id: Mapped[Optional[str]] = mapped_column(
        String(36),
        ForeignKey("ai_invocations.id", ondelete="SET NULL"),
        nullable=True,
    )
    # Rating: +1 (thumbs up) or -1 (thumbs down)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    # Optional implicit signal (e.g., time spent, clicks)
    implicit_signal: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    # Optional comment
    comment: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.current_timestamp(),
    )


__all__ = ["ResponseFeedback"]
