"""Content ingestion pipeline for MyOwnClone RAG.

Extracts text from a Source (pdf, youtube, web, text, interview), chunks it,
embeds it, and persists the chunks. Replaces the legacy "ingestion only
works for plain text" limitation where PDF/YouTube/web sources stayed in
status='processing' forever.

Pipeline per source:
    1. Load the source row from `sources`.
    2. Extract raw text based on `source.type`.
    3. Chunk the text (api.core.chunking.chunk_text).
    4. Embed the chunks (api.core.embeddings.EmbeddingService).
    5. DELETE existing chunks for the source (idempotent re-ingest).
    6. INSERT new chunks with their vectors.
    7. Update source.status to 'ready' (or 'error' on failure).

All extractors are defensive: missing deps return a clear error, network
failures mark the source as 'error' instead of crashing the pipeline.

Usage:
    from api.core.ingestion_pipeline import IngestionPipeline
    pipeline = IngestionPipeline()
    pipeline.ingest(source_id="<uuid>")

Or via the CLI command added in FASE 1.4 (`flask reindex --rechunk`).
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from typing import Any

from sqlalchemy import select

from api.core.chunking import chunk_text, count_words
from api.core.embeddings import EmbeddingService, EMBEDDING_DIMENSIONS
from api.extensions.ext_database import db
from api.models.clone import CloneConfig
from api.models.knowledge import Chunk, Source

logger = logging.getLogger(__name__)


# Cap raw extracted text to bound embedding cost. ~250k chars ≈ ~60k tokens,
# which at $0.02/M tokens costs ~$0.001 per source for text-embedding-3-small.
MAX_SOURCE_CHARS = 250_000


@dataclass
class IngestionResult:
    source_id: str
    status: str  # "ready" | "error"
    chunks_created: int = 0
    tokens_used: int = 0
    embedding_provider: str = "lexical"
    error: str | None = None


class IngestionPipeline:
    """Extract → chunk → embed → persist for a single source."""

    # ── Public API ───────────────────────────────────────────────────────────

    def ingest(self, source_id: str) -> IngestionResult:
        """Run the full pipeline for one source. Idempotent: safe to re-run."""
        source = db.session.execute(
            select(Source).where(Source.id == source_id)
        ).scalar_one_or_none()
        if source is None:
            return IngestionResult(
                source_id=source_id, status="error", error="source not found"
            )

        try:
            raw_text, meta = self._extract(source)
            if not raw_text.strip():
                self._mark_error(source, "no text could be extracted")
                return IngestionResult(
                    source_id=source_id, status="error",
                    error="no text extracted",
                )

            chunks = chunk_text(raw_text[:MAX_SOURCE_CHARS])
            if not chunks:
                self._mark_error(source, "text too short to chunk")
                return IngestionResult(
                    source_id=source_id, status="error",
                    error="content too short",
                )

            tenant_id = self._resolve_tenant_id(source)
            embed_service = EmbeddingService(tenant_id=tenant_id)
            embed_result = embed_service.embed_texts(chunks)

            # Idempotent: replace any existing chunks for this source.
            db.session.execute(
                Chunk.__table__.delete().where(Chunk.source_id == source.id)
            )
            chunk_rows = [
                Chunk(
                    source_id=source.id,
                    content=txt,
                    embedding=vector,
                    token_count=count_words(txt),
                    chunk_metadata={
                        "position": idx,
                        "silo": (source.source_metadata or {}).get("silo", "teach"),
                        "embedding_provider": embed_result.provider,
                        "embedding_model": embed_result.model,
                        **meta,
                    },
                )
                for idx, (txt, vector) in enumerate(zip(chunks, embed_result.vectors))
            ]
            db.session.add_all(chunk_rows)

            source.status = "ready"
            merged_meta = dict(source.source_metadata or {})
            merged_meta.update(meta)
            merged_meta["wordCount"] = count_words(raw_text)
            merged_meta["chunkCount"] = len(chunks)
            merged_meta["ingestion"] = f"{embed_result.provider}_v2"
            source.source_metadata = merged_meta

            db.session.commit()

            return IngestionResult(
                source_id=source_id,
                status="ready",
                chunks_created=len(chunks),
                tokens_used=embed_result.tokens_used,
                embedding_provider=embed_result.provider,
            )
        except Exception as exc:
            db.session.rollback()
            logger.exception("Ingestion failed for source %s", source_id)
            self._mark_error(source, str(exc)[:500])
            return IngestionResult(
                source_id=source_id, status="error", error=str(exc),
            )

    # ── Extractor dispatch ───────────────────────────────────────────────────

    def _extract(self, source: Source) -> tuple[str, dict[str, Any]]:
        """Return (raw_text, extraction_metadata) based on source.type."""
        source_type = (source.type or "").lower()
        dispatch = {
            "text": self._extract_text,
            "pdf": self._extract_pdf,
            "youtube": self._extract_youtube,
            "web": self._extract_web,
            "video": self._extract_unsupported,
            "interview": self._extract_unsupported,
        }
        handler = dispatch.get(source_type, self._extract_unsupported)
        text, meta = handler(source)
        meta.setdefault("source_type", source_type)
        return text, meta

    # ── Extractors ───────────────────────────────────────────────────────────

    def _extract_text(self, source: Source) -> tuple[str, dict[str, Any]]:
        """Plain text source: content lives in metadata.content."""
        content = (source.source_metadata or {}).get("content", "")
        if not content:
            # Legacy sources stored raw text in `title` or had no content.
            content = source.title or ""
        return content, {"extractor": "text_direct"}

    def _extract_pdf(self, source: Source) -> tuple[str, dict[str, Any]]:
        """PDF source: load from a local file:// path or download from http(s)."""
        try:
            import pypdf
            import io
            import os
            import urllib.request
        except ImportError as exc:
            raise RuntimeError(
                "pypdf is not installed. Add it to requirements.txt."
            ) from exc

        if not source.url:
            raise RuntimeError("pdf source has no url to load")

        url = source.url
        if url.startswith("file://"):
            path = url[len("file://"):]
            with open(path, "rb") as f:
                pdf_bytes = f.read()
        else:
            with urllib.request.urlopen(url, timeout=30) as resp:  # noqa: S310
                pdf_bytes = resp.read()

        reader = pypdf.PdfReader(io.BytesIO(pdf_bytes))
        pages = []
        for page in reader.pages:
            try:
                pages.append(page.extract_text() or "")
            except Exception:
                continue
        text = "\n\n".join(p for p in pages if p.strip())
        return text, {
            "extractor": "pypdf",
            "page_count": len(reader.pages),
        }

    def _extract_youtube(self, source: Source) -> tuple[str, dict[str, Any]]:
        """YouTube source: fetch transcript via youtube-transcript-api."""
        try:
            from youtube_transcript_api import YouTubeTranscriptApi
        except ImportError as exc:
            raise RuntimeError(
                "youtube-transcript-api is not installed. Add it to requirements.txt."
            ) from exc

        video_id = self._extract_youtube_id(source.url or "")
        if not video_id:
            raise RuntimeError(f"could not parse YouTube video id from {source.url}")

        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["es", "en"])
        text = " ".join(snippet["text"] for snippet in transcript)
        return text, {
            "extractor": "youtube_transcript_api",
            "video_id": video_id,
            "language": transcript[0].get("language") if transcript else None,
        }

    def _extract_web(self, source: Source) -> tuple[str, dict[str, Any]]:
        """Web source: extract main content with trafilatura (fallback urllib)."""
        try:
            import trafilatura
        except ImportError as exc:
            raise RuntimeError(
                "trafilatura is not installed. Add it to requirements.txt."
            ) from exc

        if not source.url:
            raise RuntimeError("web source has no url")

        downloaded = trafilatura.fetch_url(source.url)
        if not downloaded:
            raise RuntimeError(f"could not download {source.url}")
        text = trafilatura.extract(downloaded, include_comments=False, include_tables=True) or ""
        return text, {
            "extractor": "trafilatura",
            "url": source.url,
        }

    def _extract_unsupported(self, source: Source) -> tuple[str, dict[str, Any]]:
        """Sources that need future work (video rendering, AI interview)."""
        raise RuntimeError(
            f"source type '{source.type}' is not supported by the ingestion pipeline yet"
        )

    # ── Helpers ──────────────────────────────────────────────────────────────

    @staticmethod
    def _extract_youtube_id(url: str) -> str | None:
        """Parse a YouTube video id from common URL shapes."""
        patterns = [
            r"youtube\.com/watch\?v=([\w-]{11})",
            r"youtu\.be/([\w-]{11})",
            r"youtube\.com/embed/([\w-]{11})",
            r"youtube\.com/shorts/([\w-]{11})",
        ]
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        # Last resort: bare 11-char id.
        if re.fullmatch(r"[\w-]{11}", url.strip()):
            return url.strip()
        return None

    @staticmethod
    def _resolve_tenant_id(source: Source) -> str | None:
        clone = db.session.execute(
            select(CloneConfig.tenant_id).where(CloneConfig.id == source.clone_id)
        ).scalar_one_or_none()
        return clone

    @staticmethod
    def _mark_error(source: Source, message: str) -> None:
        try:
            source.status = "error"
            meta = dict(source.source_metadata or {})
            meta["ingestion_error"] = message
            source.source_metadata = meta
            db.session.commit()
        except Exception:
            db.session.rollback()
            logger.exception("Failed to mark source %s as error", source.id)
