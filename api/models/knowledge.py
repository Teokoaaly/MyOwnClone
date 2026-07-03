from typing import Optional

import sqlalchemy as sa
from pgvector.sqlalchemy import Vector
from sqlalchemy import DateTime, Float, Integer, String, Text, func, text
from sqlalchemy.orm import Mapped, mapped_column

from api.base import TypeBase


class Source(TypeBase):
    __tablename__ = "sources"

    id: Mapped[str] = mapped_column(Text, primary_key=True)
    clone_id: Mapped[str] = mapped_column(Text, nullable=False)
    type: Mapped[str] = mapped_column(String(30), nullable=False)
    title: Mapped[str] = mapped_column(Text, nullable=False)
    url: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(30), nullable=False, server_default=text("'uploading'"))
    source_metadata: Mapped[Optional[dict]] = mapped_column("metadata", sa.JSON, nullable=True)
    created_at = mapped_column(DateTime, nullable=False, server_default=func.current_timestamp())
    updated_at = mapped_column(DateTime, nullable=False, server_default=func.current_timestamp())


class Chunk(TypeBase):
    __tablename__ = "chunks"

    id: Mapped[str] = mapped_column(Text, primary_key=True)
    source_id: Mapped[str] = mapped_column(Text, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    # Migrado a pgvector (T1.4) — vector(1024) en vez de double precision[]
    embedding: Mapped[Optional[list[float]]] = mapped_column(Vector(1024), nullable=True)
    token_count: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    chunk_metadata: Mapped[Optional[dict]] = mapped_column("metadata", sa.JSON, nullable=True)


__all__ = ["Source", "Chunk"]
