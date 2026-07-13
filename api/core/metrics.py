"""T3.6: Prometheus metrics para la API Flask.

Expone /metrics con:
- Request counter por endpoint y status
- Latencia histogram por endpoint
- DB connection pool stats
- Custom counters (LLM cost, embeddings)

Seguridad (auditoria 2026-07-13 / P0.5):
``/metrics`` está protegido. Sin credenciales válidas devuelve 401.
Se soportan dos modos (configurables por env, mutuamente compatibles):

- **Basic auth**: ``METRICS_USER`` + ``METRICS_PASSWORD`` (recomendado para
  Prometheus scrape con ``basic_auth``).
- **Bearer token**: ``METRICS_TOKEN`` (alternativa simple para setups donde
  solo se quiere un token compartido).

Si ninguno está configurado, el endpoint requiere ``FLASK_ENV != production``
(escaneo libre solo en dev). En producción sin credenciales configuradas,
  el endpoint devuelve 404 para evitar exponer métricas por defecto.
"""
import base64
import hmac
import os

from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
from flask import Response, request
import time

# Métricas HTTP
REQUESTS_TOTAL = Counter(
    "flask_http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"],
)
REQUEST_LATENCY = Histogram(
    "flask_http_request_duration_seconds",
    "Request latency in seconds",
    ["method", "endpoint"],
    buckets=(0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0),
)
IN_PROGRESS = Gauge(
    "flask_http_requests_in_progress",
    "In-progress HTTP requests",
    ["method", "endpoint"],
)

# Métricas de IA (custom)
LLM_TOKENS = Counter(
    "llm_tokens_total",
    "Total LLM tokens",
    ["model", "provider", "direction"],  # direction: in | out
)
LLM_COST_CENTS = Counter(
    "llm_cost_cents_total",
    "Total LLM cost in cents",
    ["model", "provider"],
)
EMBEDDINGS = Counter(
    "embeddings_total",
    "Total embedding operations",
    ["model", "provider"],
)


def register_metrics_endpoint(app):
    """Registra el endpoint /metrics y middleware de tracking."""

    @app.before_request
    def _start_timer():
        from flask import request, g
        g._start_time = time.perf_counter()
        # Normalizar endpoint para evitar cardinalidad infinita
        endpoint = request.endpoint or "unknown"
        IN_PROGRESS.labels(method=request.method, endpoint=endpoint).inc()

    @app.after_request
    def _record_metrics(response):
        from flask import request, g
        try:
            duration = time.perf_counter() - getattr(g, "_start_time", time.perf_counter())
            endpoint = request.endpoint or "unknown"
            REQUESTS_TOTAL.labels(
                method=request.method,
                endpoint=endpoint,
                status=response.status_code,
            ).inc()
            REQUEST_LATENCY.labels(method=request.method, endpoint=endpoint).observe(duration)
            IN_PROGRESS.labels(method=request.method, endpoint=endpoint).dec()
        except Exception:
            pass  # nunca romper el request por métricas
        return response

    @app.route("/metrics", methods=["GET"])
    def metrics():
        if not _metrics_authorized(request):
            # 404 en prod sin creds configuradas (no revelar que existe);
            # 401 cuando hay creds configuradas para que Prometheus pueda
            # reintentar con Authorization.
            if _metrics_has_creds_configured():
                headers = {"WWW-Authenticate": "Basic realm=\"metrics\""}
                return Response("Unauthorized", status=401, headers=headers)
            return Response("Not Found", status=404)
        return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


def _metrics_has_creds_configured() -> bool:
    """True si hay basic-auth o token configurado para /metrics."""
    return bool(
        os.environ.get("METRICS_USER")
        or os.environ.get("METRICS_TOKEN")
    )


def _is_production_env() -> bool:
    """Mismo criterio que libs.security_checks._is_production (unificado en P0.1)."""
    return os.environ.get("FLASK_ENV", "development").lower() not in (
        "development", "dev", "test", "testing",
    )


def _metrics_authorized(req) -> bool:
    """Verifica credenciales para /metrics.

    - Si hay ``METRICS_USER``+``METRICS_PASSWORD``: valida HTTP Basic.
    - Si hay ``METRICS_TOKEN``: valida ``Authorization: Bearer <token>``.
    - Si no hay creds configuradas:
      * dev/test: permite (escaneo libre local).
      * production: deniega (defensa por defecto).
    """
    user = os.environ.get("METRICS_USER")
    password = os.environ.get("METRICS_PASSWORD")
    token = os.environ.get("METRICS_TOKEN")

    if user and password:
        auth_header = req.headers.get("Authorization", "")
        if not auth_header.startswith("Basic "):
            return False
        try:
            decoded = base64.b64decode(auth_header[6:]).decode("utf-8")
        except Exception:
            return False
        if ":" not in decoded:
            return False
        req_user, _, req_pass = decoded.partition(":")
        # Timing-safe comparison para evitar username/password oracle.
        return (
            hmac.compare_digest(req_user, user)
            and hmac.compare_digest(req_pass, password)
        )

    if token:
        auth_header = req.headers.get("Authorization", "")
        bearer = auth_header[7:] if auth_header.startswith("Bearer ") else req.headers.get("X-Metrics-Token", "")
        return bool(bearer) and hmac.compare_digest(bearer, token)

    # Sin creds configuradas: permitido solo fuera de producción.
    return not _is_production_env()
