"""Pipeline de ingestion RAG: fuente → texto → chunks → embeddings → DB.

Soporta:
- Texto plano
- URL (HTTP fetch + extraccion HTML con BeautifulSoup)
- PDF (PyPDF2)
- YouTube (youtube-transcript-api)

Pipeline:
1. Extraer texto segun source.type
2. Dividir en chunks (350 palabras, overlap 40)
3. Generar embeddings via EmbeddingService (Ollama local)
4. INSERT INTO chunks
5. UPDATE sources SET status='ready'
"""
from __future__ import annotations

import logging
import re

from api.extensions.ext_database import db
from api.models.knowledge import Chunk, Source

logger = logging.getLogger(__name__)

_CHUNK_SIZE = 350
_CHUNK_OVERLAP = 40


def ingest_source(source_id: str) -> None:
    """Procesa una fuente: extrae texto, hace chunks, embeddea y guarda."""
    source = db.session.get(Source, source_id)
    if not source:
        logger.error("Source %s no encontrada", source_id)
        return

    try:
        source.status = "processing"
        db.session.commit()

        raw_text = _extract_text(source)
        if not raw_text or not raw_text.strip():
            _fail(source, "Sin contenido extraible")
            return

        chunks = _split_text(raw_text, chunk_size=_CHUNK_SIZE, overlap=_CHUNK_OVERLAP)
        if not chunks:
            _fail(source, "Texto demasiado corto para chunking")
            return

        from api.core.embeddings import EmbeddingService
        embedder = EmbeddingService()
        try:
            embeddings = embedder.embed_texts(chunks, tenant_id=source.clone_id)
        except Exception as exc:
            logger.exception("Error generando embeddings para source %s", source_id)
            _fail(source, f"Embedding fallo: {exc}")
            return

        db.session.query(Chunk).filter(Chunk.source_id == source_id).delete()
        db.session.commit()

        for idx, (text, embedding) in enumerate(zip(chunks, embeddings)):
            chunk = Chunk(
                source_id=source_id,
                content=text,
                embedding=embedding,
                token_count=len(text.split()),
                chunk_metadata={"chunk_index": idx, "total_chunks": len(chunks)},
            )
            db.session.add(chunk)

        source.status = "ready"
        db.session.commit()
        logger.info("Source %s ingerida: %d chunks, %d chars", source_id, len(chunks), len(raw_text))

    except Exception as exc:
        logger.exception("Error ingiriendo source %s", source_id)
        db.session.rollback()
        _fail(source, str(exc))


def _extract_text(source: Source) -> str:
    """Extrae texto segun el tipo de fuente."""
    if source.type == "text":
        meta = source.source_metadata or {}
        return meta.get("content") or source.url or ""
    if source.type == "url":
        return _extract_from_url(source.url or "")
    if source.type == "pdf":
        return _extract_from_pdf(source.url or "")
    if source.type == "youtube":
        return _extract_from_youtube(source.url or "")
    return ""


def _extract_from_pdf(url: str) -> str:
    from io import BytesIO
    import requests
    from PyPDF2 import PdfReader

    if not url:
        return ""
    try:
        resp = requests.get(url, timeout=60, headers={"User-Agent": "MyOwnClone/1.0"})
        resp.raise_for_status()
    except Exception as exc:
        logger.warning("Error descargando PDF %s: %s", url, exc)
        return ""
    try:
        reader = PdfReader(BytesIO(resp.content))
    except Exception as exc:
        logger.warning("Error parseando PDF %s: %s", url, exc)
        return ""
    pages = []
    for i, page in enumerate(reader.pages):
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        if text.strip():
            pages.append(text)
    return re.sub(r"\n{3,}", "\n\n", "\n\n".join(pages))


def _extract_youtube_id(url: str) -> str | None:
    patterns = [
        r"(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([a-zA-Z0-9_-]{11})",
    ]
    for pat in patterns:
        m = re.search(pat, url)
        if m:
            return m.group(1)
    return None


def _extract_from_youtube(url: str) -> str:
    video_id = _extract_youtube_id(url)
    if not video_id:
        return ""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join(entry["text"] for entry in transcript)
    except Exception as exc:
        logger.warning("Error YouTube %s: %s", video_id, exc)
        return ""


def _extract_from_url(url: str) -> str:
    import requests
    from bs4 import BeautifulSoup
    try:
        resp = requests.get(url, timeout=30, headers={"User-Agent": "MyOwnClone/1.0"})
        resp.raise_for_status()
    except Exception as exc:
        logger.warning("Error descargando %s: %s", url, exc)
        return ""
    soup = BeautifulSoup(resp.text, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()
    text = soup.get_text(separator="\n", strip=True)
    return re.sub(r"\n{3,}", "\n\n", text)


def _split_text(text: str, chunk_size: int = _CHUNK_SIZE, overlap: int = _CHUNK_OVERLAP) -> list[str]:
    words = text.split()
    if not words:
        return []
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunks.append(" ".join(words[start:end]))
        if end >= len(words):
            break
        start = end - overlap
    return chunks


def _fail(source: Source, reason: str) -> None:
    try:
        source.status = "failed"
        meta = source.source_metadata or {}
        meta["error"] = reason
        source.source_metadata = meta
        db.session.commit()
    except Exception:
        db.session.rollback()
