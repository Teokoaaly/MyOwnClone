"""Routing decision log — SmartRouter records every routing decision here.

Used for analytics, debugging, and improving routing algorithms.
"""
from __future__ import annotations

import hashlib
import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from api.base import TypeBase


class RoutingDecision(TypeBase):
    """Every routing decision is logged for analytics."""

    __tablename__ = "routing_decisions"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        insert_default=lambda: str(uuid.uuid4()),
        default=lambda: str(uuid.uuid4()),
    )
    # Tenant that owns this routing decision
    tenant_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    # Task that triggered the routing (e.g., chat_primary, embedding)
    task: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    # Number of candidate models considered
    candidates_considered: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    # The chosen model ID
    chosen_model_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    # Composite score of the chosen model
    score: Mapped[Optional[float]] = mapped_column(Integer, nullable=True)
    # Human-readable reason for the choice
    reason: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.current_timestamp(),
    )


__all__ = ["RoutingDecision"]
