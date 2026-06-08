# Multi-stage Dockerfile for MyOwnClone API
# Stage 1: build dependencies into a wheel cache
FROM python:3.11-slim AS builder

WORKDIR /build

# Install build deps
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps into a prefix we can copy
COPY requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt

# Stage 2: lean runtime
FROM python:3.11-slim AS runtime

# Don't write .pyc files, don't buffer stdout
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Runtime system deps (libpq for psycopg2)
RUN apt-get update && apt-get install -y --no-install-recommends \
        libpq5 \
        curl \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN groupadd --system --gid 1001 app \
    && useradd --system --uid 1001 --gid app --no-create-home --shell /usr/sbin/nologin appuser

# Layout: /app/api/ is the package. WORKDIR is /app so that
# 'import api.*' resolves via /app being on sys.path (added by gunicorn).
WORKDIR /app

# Pull requirements first (cached layer)
COPY --from=builder /wheels /wheels
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --no-index --find-links=/wheels -r /app/requirements.txt gunicorn \
    && rm -rf /wheels

# Copy application code into /app/api/ so 'import api.*' works
COPY --chown=appuser:app . /app/api/

USER appuser

# Add /app to PYTHONPATH so 'import api' works regardless of cwd
ENV PYTHONPATH=/app

EXPOSE 5001

# Healthcheck
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -fsS http://localhost:5001/console/api/ || exit 1

# gunicorn with app at /app/api/app_factory.py → module is api.app_factory
# Use the path-style import so we don't depend on sys.path manipulation
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "--workers", "2", "--timeout", "60", \
     "--access-logfile", "-", "--error-logfile", "-", \
     "api.app_factory:app"]
