"""AI Model catalog and tenant-level assignments.

AIModel: a registered AI model (e.g. openai/gpt-4o, cohere/rerank-v3).
AIModelAssignment: tenant-level (or global) model assignment per task.
"""
from __future__ import annotations

import enum
from datetime import datetime
from typing import Optional

import sqlalchemy as sa
from sqlalchemy import Boolean, DateTime, Integer, String, func, text
from sqlalchemy.orm import Mapped, mapped_column

from api.libs.datetime_utils import naive_utc_now
from api.libs.uuid_utils import uuidv7

from ..base import TypeBase


class AIModelType(enum.StrEnum):
    CHAT = "chat"
    EMBEDDING = "embedding"
    RERANK = "rerank"
    TTS = "tts"
    STT = "stt"
    IMAGE = "image"
    MODERATION = "moderation"


class AssignmentTask(enum.StrEnum):
    CHAT_PRIMARY = "chat_primary"
    CHAT_FALLBACK = "chat_fallback"
    EMBEDDING = "embedding"
    RERANK = "rerank"
    TTS = "tts"
    STT = "stt"
    MODERATION = "moderation"


class AIModel(TypeBase):
    """A registered AI model (e.g. openai/gpt-4o, cohere/rerank-v3)."""

    __tablename__ = "ai_models"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        insert_default=lambda: str(uuidv7()),
        default=lambda: str(uuidv7()),
    )
    # e.g. "openai", "anthropic", "cohere", "google"
    provider: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    # e.g. "gpt-4o", "claude-3-opus", "rerank-v3"
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    # e.g. "chat", "embedding", "rerank", "tts", "stt"
    model_type: Mapped[str] = mapped_column(
        String(30),
        server_default=text("'chat'"),
        default="chat",
        nullable=False,
    )
    # JSON list of capability strings, e.g. ["vision", "function_calling"]
    capabilities: Mapped[Optional[dict]] = mapped_column(
        "capabilities", sa.JSON, nullable=True
    )
    # JSON object with model config (temperature, top_p, etc.)
    config: Mapped[Optional[dict]] = mapped_column(sa.JSON, nullable=True)
    # Cost in cents per 1,000 tokens (input)
    input_cost_per_1k: Mapped[int] = mapped_column(
        Integer, server_default=text("0"), default=0
    )
    # Cost in cents per 1,000 tokens (output)
    output_cost_per_1k: Mapped[int] = mapped_column(
        Integer, server_default=text("0"), default=0
    )
    # Maximum tokens the model can accept in a single request
    max_tokens: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    # Whether this model is available for use
    is_active: Mapped[bool] = mapped_column(
        Boolean, server_default=text("true"), default=True
    )
    # Account ID of the admin who registered this model
    created_by: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
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


class AIModelAssignment(TypeBase):
    """Tenant-level (or global) model assignment per task.

    If tenant_id is NULL, the assignment is global (platform-wide default).
    """

    __tablename__ = "ai_model_assignments"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        insert_default=lambda: str(uuidv7()),
        default=lambda: str(uuidv7()),
    )
    # NULL means global (platform-wide default assignment)
    tenant_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    # FK to ai_models.id
    model_id: Mapped[str] = mapped_column(
        String(36),
        sa.ForeignKey("ai_models.id", ondelete="CASCADE"),
        nullable=False,
    )
    # Human-readable label for this assignment, e.g. "Production GPT-4o"
    label: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    # The task this assignment covers (chat_primary, embedding, rerank, etc.)
    task: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    # Higher priority wins when multiple assignments match the same tenant+task
    priority: Mapped[int] = mapped_column(
        Integer, server_default=text("0"), default=0
    )
    # Whether this assignment is currently active
    is_active: Mapped[bool] = mapped_column(
        Boolean, server_default=text("true"), default=True
    )
    # Account ID of the admin who created this assignment
    created_by: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
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
    "AIModel",
    "AIModelAssignment",
    "AIModelType",
    "AssignmentTask",
]
