"""Outbox table for cross-store (Postgres + Weaviate) embedding ingestion.

The outbox pattern handles the case where Weaviate and Postgres don't share
transactions. Steps:
1. Postgres: INSERT in `embedding_outbox` (id, tenant_id, text, status='pending')
2. Worker (APScheduler) reads pending rows, writes to Weaviate, marks 'synced' or 'failed'
3. UI can show banner if there are pending/failed items
"""
from __future__ import annotations

import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import Index, Integer, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from api.base import TypeBase


class OutboxStatus:
    PENDING = "pending"
    SYNCED = "synced"
    FAILED = "failed"


class EmbeddingOutbox(TypeBase):
    """Outbox for cross-store embedding writes."""

    __tablename__ = "embedding_outbox"

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    # For tenant-scoped embeddings
    tenant_id: Mapped[Optional[str]] = mapped_column(UUID(as_uuid=False), nullable=True)
    # If set, links to a Chunk row
    chunk_id: Mapped[Optional[str]] = mapped_column(UUID(as_uuid=False), nullable=True)
    # The text content to embed
    text: Mapped[str] = mapped_column(Text, nullable=False)
    # 1536-d vector (JSONB for portability)
    embedding: Mapped[Optional[list]] = mapped_column(JSONB, nullable=True)
    # Arbitrary metadata stored as JSONB
    metadata_json: Mapped[Optional[dict]] = mapped_column(JSONB, default=dict)
    # Weaviate class name to write to
    weaviate_class: Mapped[str] = mapped_column(String(128), nullable=False, default="Chunk")
    # pending | synced | failed
    status: Mapped[str] = mapped_column(String(16), nullable=False, default=OutboxStatus.PENDING)
    # Number of sync attempts
    attempts: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    # Last error message if status=failed
    last_error: Mapped[Optional[str]] = mapped_column(Text)
    # When to retry next (for exponential back-off)
    next_retry_at: Mapped[Optional[datetime]] = mapped_column(DateTime)
    # When successfully synced to Weaviate
    synced_at: Mapped[Optional[datetime]] = mapped_column(DateTime)

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now(), nullable=False
    )

    __table_args__ = (
        Index("ix_outbox_status_next_retry", "status", "next_retry_at"),
        Index("ix_outbox_tenant", "tenant_id"),
    )

    def __repr__(self) -> str:
        return f"<EmbeddingOutbox {self.id} status={self.status}>"