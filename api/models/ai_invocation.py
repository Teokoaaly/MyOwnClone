"""AI Invocation log — every LLM call is recorded here for analytics and billing.

Records prompt/response hashes (SHA-256) for deduplication, token counts,
cost, and latency. Powers the cost_daily_rollup materialized view.
"""
from __future__ import annotations

import hashlib
from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, DateTime, Integer, String, Text, func, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from api.base import TypeBase


def _sha256(s: str) -> str:
    """Return lowercase hex SHA-256 of a string."""
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


class AIInvocation(TypeBase):
    """Every LLM invocation is logged here.

    Uses prompt_hash + response_hash for deduplication.
    """

    __tablename__ = "ai_invocations"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        insert_default=lambda: str(hashlib.uuid4()),
        default=lambda: str(hashlib.uuid4()),
    )
    # Tenant that owns this invocation
    tenant_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    # FK to ai_models.id (nullable for env-key based calls before model registry existed)
    model_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    # Task name: chat_primary, embedding, rerank, etc.
    task: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    # SHA-256 of the prompt (messages concatenated)
    prompt_hash: Mapped[str] = mapped_column(String(64), nullable=False)
    # SHA-256 of the raw response text
    response_hash: Mapped[str] = mapped_column(String(64), nullable=False)
    # Token counts from provider
    tokens_in: Mapped[int] = mapped_column(Integer, server_default=text("0"), default=0)
    tokens_out: Mapped[int] = mapped_column(Integer, server_default=text("0"), default=0)
    # Cost in cents
    cost_cents: Mapped[int] = mapped_column(Integer, server_default=text("0"), default=0)
    # Latency in milliseconds (provider-reported or measured)
    latency_ms: Mapped[int] = mapped_column(Integer, server_default=text("0"), default=0)
    # Whether the call succeeded
    success: Mapped[bool] = mapped_column(Boolean, server_default=text("true"), default=True)
    # Error message if success=false
    error_message: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.current_timestamp(),
    )


__all__ = ["AIInvocation", "_sha256"]
