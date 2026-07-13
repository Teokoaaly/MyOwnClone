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

import ipaddress
import logging
import re
import socket
from urllib.parse import urlparse

from api.extensions.ext_database import db
from api.models.knowledge import Chunk, Source

logger = logging.getLogger(__name__)


# Hostnames que sirven metadata cloud a cualquier caller interno.
# Cubren AWS, GCP, Azure, DigitalOcean, Alibaba, Oracle.
_CLOUD_METADATA_HOSTS = frozenset({
    "169.254.169.254",       # AWS / Azure / DigitalOcean / OCI link-local
    "metadata.google.internal",  # GCP
    "metadata",              # alias GCP
    "169.254.170.2",         # AWS ECS task metadata (v2)
    "fd00:ec2::254",         # AWS IPv6 metadata
})


class UnsafeURLError(ValueError):
    """Raised when a URL is rejected by the SSRF allowlist."""


def _is_safe_url(url: str) -> None:
    """SSRF allowlist (auditoria 2026-07-13 / P0.5, defecto C-10).

    Rechaza URLs que apunten a infraestructura interna antes de hacer el
    fetch. Bloquea:

    - Esquemas distintos de ``http``/``https`` (evita ``file://``, ``gopher``,
      ``ftp``...).
    - Hosts que resuelvan (o sean literalmente) IPs privadas, loopback,
      link-local, reservadas o multicast.
    - Hosts conocidos de metadata cloud (AWS/GCP/Azure/DO/OCI).
    - URLs sin host o con userinfo sospechoso.

    Resuelve el hostname a sus IPs (getaddrinfo) y valida TODAS las
    resoluciones, para que un DNS rebinding no escape del check.
    """
    if not url or not isinstance(url, str):
        raise UnsafeURLError("empty url")

    parsed = urlparse(url)
    if parsed.scheme.lower() not in ("http", "https"):
        raise UnsafeURLError(f"scheme not allowed: {parsed.scheme!r}")

    host = parsed.hostname
    if not host:
        raise UnsafeURLError("missing host")

    if host.lower() in _CLOUD_METADATA_HOSTS:
        raise UnsafeURLError(f"cloud metadata host blocked: {host}")

    # Primero, si el host es ya una IP literal, validarla directamente.
    try:
        ip = ipaddress.ip_address(host)
    except ValueError:
        ip = None
    if ip is not None:
        if _is_blocked_ip(ip):
            raise UnsafeURLError(f"ip address blocked: {ip}")
        return

    # Si es un hostname, resolverlo y validar todas las IPs resultantes
    # (DNS rebinding defense).
    try:
        infos = socket.getaddrinfo(host, None)
    except socket.gaierror as exc:
        raise UnsafeURLError(f"unable to resolve host {host!r}: {exc}") from exc

    resolved = set()
    for family, _stype, _proto, _canon, sockaddr in infos:
        ip_str = sockaddr[0]
        # Normalizar IPv6 con scope id (fe80::1%eth0 -> fe80::1).
        ip_str = ip_str.split("%", 1)[0]
        try:
            resolved.add(ipaddress.ip_address(ip_str))
        except ValueError:
            continue

    if not resolved:
        raise UnsafeURLError(f"host {host!r} did not resolve to any IP")

    for resolved_ip in resolved:
        if _is_blocked_ip(resolved_ip):
            raise UnsafeURLError(
                f"host {host!r} resolves to blocked ip {resolved_ip}"
            )


def _is_blocked_ip(ip: ipaddress._BaseAddress) -> bool:
    """True si la IP apunta a infraestructura interna/prohibida."""
    return (
        ip.is_private
        or ip.is_loopback
        or ip.is_link_local
        or ip.is_reserved
        or ip.is_multicast
        or ip.is_unspecified
    )

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
    # P0.5 (C-10): bloquear SSRF antes del fetch.
    try:
        _is_safe_url(url)
    except UnsafeURLError as exc:
        logger.warning("SSRF blocked (pdf): %s", exc)
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
    # P0.5 (C-10): bloquear SSRF antes del fetch.
    try:
        _is_safe_url(url)
    except UnsafeURLError as exc:
        logger.warning("SSRF blocked (url): %s", exc)
        return ""
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
