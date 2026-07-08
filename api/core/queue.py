"""Async task queue for heavy operations (PDF ingestion, email processing).

T3.5: Worker asincrono para que requests HTTP no se bloqueen con
operaciones pesadas (PDFs de 100+ paginas, transcripciones YouTube).

Stack: Redis Queue (RQ) — mas simple que Celery para nuestro caso.

Uso:
    from api.core.queue import enqueue_ingestion
    enqueue_ingestion(source_id)
"""
from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


def _get_queue():
    """Returns the RQ Queue named 'ingestion' backed by Redis."""
    try:
        from rq import Queue

        conn = _get_redis_client()
        return Queue("ingestion", connection=conn), conn
    except ImportError:
        logger.warning("rq no instalado, queue no disponible")
        return None, None


def _get_redis_url() -> str:
    """Construye la URL Redis desde env vars con password URL-encoded."""
    import os
    from urllib.parse import quote

    host = os.environ.get("REDIS_HOST", "redis")
    port = int(os.environ.get("REDIS_PORT", "6379"))
    password = os.environ.get("REDIS_PASSWORD", "")
    tls = os.environ.get("REDIS_TLS", "false").lower() == "true"
    scheme = "rediss" if tls else "redis"
    if password:
        auth = f":{quote(password, safe='')}@"
    else:
        auth = ""
    return f"{scheme}://{auth}{host}:{port}"


def _get_redis_client():
    """Cliente Redis con SSL (incluye certs cliente si Redis los requiere).

    Redis en este VPS está configurado con mTLS — necesita certs cliente
    ademas del CA. Los certs están montados en /etc/redis/tls/.
    """
    import os
    import redis

    url = _get_redis_url()
    is_tls = url.startswith("rediss://")
    if not is_tls:
        return redis.from_url(url)

    return redis.from_url(
        url,
        ssl_cert_reqs="required",
        ssl_ca_certs="/etc/redis/tls/ca.crt",
        ssl_certfile="/etc/redis/tls/redis.crt",
        ssl_keyfile="/etc/redis/tls/redis.key",
        ssl_check_hostname=False,  # cert generado con otro hostname
    )


def enqueue_ingestion(source_id: str, timeout: int = 600) -> str | None:
    """Encola la ingestion de una fuente. Devuelve el job_id o None.

    Args:
        source_id: UUID de la source
        timeout: Timeout en segundos (default 10 min para PDFs grandes)
    """
    q, _ = _get_queue()
    if q is None:
        logger.warning(
            "enqueue_ingestion: queue no disponible, "
            "ejecutar ingestion sincrona"
        )
        return None

    from api.core.ingestion import ingest_source

    job = q.enqueue(ingest_source, source_id, job_timeout=timeout)
    logger.info("Ingestion encolada: source=%s job=%s", source_id, job.id)
    return job.id


def get_job_status(job_id: str) -> dict:
    """Consulta el estado de un job de RQ."""
    from rq.job import Job

    q, conn = _get_queue()
    if q is None or conn is None:
        return {"status": "queue_unavailable"}

    try:
        job = Job.fetch(job_id, connection=conn)
        return {
            "id": job.id,
            "status": job.get_status(),
            "result": str(job.result) if job.is_finished else None,
            "error": str(job.exc_info) if job.is_failed else None,
            "created_at": job.created_at.isoformat() if job.created_at else None,
        }
    except Exception as exc:
        return {"id": job_id, "status": "not_found", "error": str(exc)}
