#!/bin/sh
# Entrypoint del contenedor api.
# 1. Ejecuta migraciones Alembic (flask db upgrade)
# 2. Arranca gunicorn (CMD del Dockerfile)
#
# T1.5 — Migraciones automáticas en deploy.

set -e

echo "[entrypoint] $(date -u +%Y-%m-%dT%H:%M:%SZ) Ejecutando migraciones Alembic..."

# flask CLI importa api.app_factory; con PYTHONPATH=/app, --app=app_factory funciona
# cuando el módulo está accesible directamente. Como /app está en PYTHONPATH
# y el paquete es `api`, el módulo es api.app_factory.
FLASK_APP=api.app_factory flask db upgrade --directory /app/api/migrations 2>&1

echo "[entrypoint] $(date -u +%Y-%m-%dT%H:%M:%SZ) Migraciones completadas. Arrancando gunicorn..."
exec "$@"
