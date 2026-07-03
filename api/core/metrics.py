"""T3.6: Prometheus metrics para la API Flask.

Expone /metrics con:
- Request counter por endpoint y status
- Latencia histogram por endpoint
- DB connection pool stats
- Custom counters (LLM cost, embeddings)
"""
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
from flask import Response
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
        return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)