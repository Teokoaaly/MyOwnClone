from __future__ import annotations

import logging
import os

import requests
from flask import jsonify
from sqlalchemy import text

from api.core.model_registry import ModelRegistry
from api.extensions import db
from api.models.ai_models import AITask

logger = logging.getLogger(__name__)

def _ollama_has_model(response, model_id: str) -> bool:
    names = {entry["name"] for entry in response.json()["models"]}
    return model_id in names or f"{model_id}:latest" in names


def register_health_routes(app) -> None:
    @app.get("/healthz")
    def healthz():
        checks: dict[str, str] = {}
        all_ok = True

        try:
            db.session.execute(text("SELECT 1"))
            checks["database"] = "ok"
        except Exception:
            db.session.rollback()
            checks["database"] = "error"
            all_ok = False

        redis_ok, _redis_error = _redis_ready()
        if redis_ok:
            checks["redis"] = "ok"
        else:
            checks["redis"] = "error"
            all_ok = False

        try:
            embedding_model = ModelRegistry().resolve(
                tenant_id=None, task=AITask.EMBEDDING
            )
            if embedding_model.provider != "local":
                checks["embedding_model"] = "ok"
        except Exception as error:
            logger.warning(
                "embedding readiness check failed: %s", type(error).__name__
            )
            embedding_model = None
            checks["embedding_model"] = "error"
            all_ok = False

        ollama_url = os.environ.get("OLLAMA_BASE_URL", "http://127.0.0.1:11434")
        try:
            response = requests.get(f"{ollama_url}/api/tags", timeout=2)
            if response.status_code == 200:
                checks["ollama"] = "ok"
                if embedding_model is not None and embedding_model.provider == "local":
                    if _ollama_has_model(response, embedding_model.model_id):
                        checks["embedding_model"] = "ok"
                    else:
                        checks["embedding_model"] = "error"
                        all_ok = False
            else:
                checks["ollama"] = f"error: HTTP {response.status_code}"
                if embedding_model is not None and embedding_model.provider == "local":
                    checks["embedding_model"] = "error"
                    all_ok = False
        except (requests.RequestException, KeyError, TypeError, ValueError):
            checks["ollama"] = "unreachable"
            if embedding_model is not None and embedding_model.provider == "local":
                checks["embedding_model"] = "error"
                all_ok = False

        payload_status = "ready" if all_ok else "degraded"
        http_status = 200 if all_ok else 503
        return jsonify({"status": payload_status, "checks": checks}), http_status

    @app.get("/readyz")
    def readyz():
        return jsonify({"status": "ready"}), 200


def _redis_ready() -> tuple[bool, str | None]:
    host = os.getenv("REDIS_HOST", "").strip()
    if not host:
        return True, "not_configured"

    try:
        import redis

        redis_tls = os.getenv("REDIS_TLS", "false").strip().lower() == "true"
        redis_port = int(os.getenv("REDIS_PORT", "6379"))
        if not redis_tls and redis_port == 6380:
            redis_tls = True

        client_kwargs = {
            "host": host,
            "port": redis_port,
            "password": os.getenv("REDIS_PASSWORD") or None,
            "socket_connect_timeout": 1.0,
            "socket_timeout": 1.0,
        }
        if redis_tls:
            client_kwargs["ssl"] = True
            client_kwargs["ssl_certfile"] = "/etc/redis/tls/redis.crt"
            client_kwargs["ssl_keyfile"] = "/etc/redis/tls/redis.key"
            client_kwargs["ssl_ca_certs"] = "/etc/redis/tls/ca.crt"
            client_kwargs["ssl_check_hostname"] = False

        client = redis.Redis(**client_kwargs)
        client.ping()
        return True, None
    except Exception:
        return False, "unavailable"
