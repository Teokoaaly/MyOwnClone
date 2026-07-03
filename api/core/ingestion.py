"""Pipeline de ingestion RAG: fuente → texto → chunks → embeddings → DB.

T2.1 de FASE 2.

Soporta:
- Texto plano
- URL (HTTP fetch + extraccion HTML con BeautifulSoup)
- PDF (T2.3)
- YouTube (T2.4)

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

# Chunk size en palabras (aprox ~500 tokens para ratio 1 palabra = 1.3 tokens)
_CHUNK_SIZE = 350
_CHUNK_OVERLAP = 40


def ingest_source(source_id: str) -> None:
    """Procesa una fuente: extrae texto, hace chunks, embeddea y guarda.

    Marca status='processing' al inicio y 'ready'/'failed' al final.
    """
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

        # Embeddings (batch via EmbeddingService, ahora Ollama local)
        from api.core.embeddings import EmbeddingService

        embedder = EmbeddingService()
        try:
            embeddings = embedder.embed_texts(chunks, tenant_id=source.clone_id)
        except Exception as exc:
            logger.exception("Error generando embeddings para source %s", source_id)
            _fail(source, f"Embedding fallo: {exc}")
            return

        # Limpieza previa (re-ingesta idempotente)
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
        logger.info(
            "Source %s ingerida: %d chunks, %d chars",
            source_id, len(chunks), len(raw_text),
        )

    except Exception as exc:
        logger.exception("Error ingiriendo source %s", source_id)
        db.session.rollback()
        _fail(source, str(exc))


def _extract_text(source: Source) -> str:
    """Extrae texto segun el tipo de fuente."""
    if source.type == "text":
        # Texto plano: viene en el campo url o en metadata.content
        meta = source.chunk_metadata or {}
        return meta.get("content") or source.url or ""
    if source.type == "url":
        return _extract_from_url(source.url or "")
    if source.type == "pdf":
        # T2.3 implementara extraccion de PDF
        return source.url or ""
    if source.type == "youtube":
        # T2.4 implementara transcripciones
        return source.url or ""
    return ""


def _extract_from_url(url: str) -> str:
    """Descarga una URL y extrae texto plano."""
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
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def _split_text(text: str, chunk_size: int = _CHUNK_SIZE, overlap: int = _CHUNK_OVERLAP) -> list[str]:
    """Divide texto en chunks solapados por numero de palabras."""
    words = text.split()
    if not words:
        return []

    chunks: list[str] = []
    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        if end >= len(words):
            break
        start = end - overlap
    return chunks


def _fail(source: Source, reason: str) -> None:
    """Marca la fuente como fallida con la razon del error."""
    try:
        source.status = "failed"
        meta = source.chunk_metadata or {}
        meta["error"] = reason
        source.chunk_metadata = meta
        db.session.commit()
    except Exception:
        db.session.rollback()