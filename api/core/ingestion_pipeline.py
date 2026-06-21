"""IngestionPipeline: chunk text, embed, write to outbox.

The pipeline:
1. Chunks the text (simple character-based chunking for now)
2. Embeds each chunk via EmbeddingService
3. Writes to embedding_outbox (status='pending') in a single Postgres transaction
4. Returns list of chunk_ids

The outbox worker (run separately) syncs to Weaviate asynchronously.
"""
from __future__ import annotations

import logging
import uuid
from typing import Optional

from api.core.embeddings import EmbeddingService, FallbackEmbeddingService
from api.models.embedding_outbox import EmbeddingOutbox, OutboxStatus
from api.extensions import db


logger = logging.getLogger(__name__)


class IngestionPipeline:
    """Pipeline for text → chunks → embeddings → outbox (Postgres + Weaviate)."""

    DEFAULT_CHUNK_SIZE = 1000  # characters
    DEFAULT_CHUNK_OVERLAP = 200

    def __init__(
        self,
        chunk_size: int = DEFAULT_CHUNK_SIZE,
        chunk_overlap: int = DEFAULT_CHUNK_OVERLAP,
        embedding_service: Optional[EmbeddingService] = None,
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.embedding_service = embedding_service or EmbeddingService()

    def ingest_text(
        self,
        tenant_id: str,
        text: str,
        *,
        metadata: Optional[dict] = None,
        weaviate_class: str = "Chunk",
    ) -> list[str]:
        """Ingest a single text. Returns list of chunk_ids (outbox row ids)."""
        chunks = self._chunk_text(text)
        return self.ingest_chunks(
            tenant_id, chunks, metadata=metadata, weaviate_class=weaviate_class
        )

    def ingest_chunks(
        self,
        tenant_id: str,
        chunks: list[str],
        *,
        metadata: Optional[dict] = None,
        weaviate_class: str = "Chunk",
    ) -> list[str]:
        """Ingest pre-chunked text. Returns list of chunk_ids (outbox row ids)."""
        if not chunks:
            return []

        # Generate embeddings (one batch call)
        embeddings = self.embedding_service.embed_texts(tenant_id, chunks)

        # Write to outbox in a single transaction
        outbox_ids: list[str] = []
        for text_chunk, embedding in zip(chunks, embeddings):
            row = EmbeddingOutbox(
                id=str(uuid.uuid4()),
                tenant_id=tenant_id,
                text=text_chunk,
                embedding=embedding,
                metadata_json=metadata or {},
                weaviate_class=weaviate_class,
                status=OutboxStatus.PENDING,
                attempts=0,
            )
            db.session.add(row)
            db.session.flush()  # populate row.id
            outbox_ids.append(row.id)
        db.session.commit()
        return outbox_ids

    def ingest_batch(
        self,
        tenant_id: str,
        texts: list[str],
        *,
        metadata: Optional[dict] = None,
        weaviate_class: str = "Chunk",
    ) -> list[str]:
        """Ingest a batch of texts. Returns list of chunk_ids."""
        # Chunk each text first, then ingest all chunks
        all_chunks: list[str] = []
        for text in texts:
            all_chunks.extend(self._chunk_text(text))
        return self.ingest_chunks(
            tenant_id, all_chunks, metadata=metadata, weaviate_class=weaviate_class
        )

    def _chunk_text(self, text: str) -> list[str]:
        """Simple character-based chunking with overlap.

        For real RAG, replace with token-aware chunking. This is a starting point.
        """
        if not text:
            return []
        if len(text) <= self.chunk_size:
            return [text]

        chunks = []
        start = 0
        step = self.chunk_size - self.chunk_overlap
        while start < len(text):
            chunk = text[start : start + self.chunk_size]
            if chunk.strip():  # skip empty chunks
                chunks.append(chunk)
            start += step
        return chunks