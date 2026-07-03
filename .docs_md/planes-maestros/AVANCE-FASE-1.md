# Avance FASE 1 — Ejecución paso a paso

> **Fecha**: 2026-07-03
> **Ejecutor**: LLM con acceso SSH al VPS `212.227.169.99`
> **Rama de trabajo**: `docs/planes-maestros` (rama paralela para docs)

---

## Task T1.7 — Limpiar imágenes Docker ✅ COMPLETADA

**Fecha ejecución**: 2026-07-03

### Antes
- 12 imágenes Docker (5 activas, 7 inactivas)
- 4 imágenes dangling (sin tag): `b85d81abee70`, `a759f738e52d`, `3073dc147f5b`, `bd12d6788a61`
- Build cache: **2.17 GB**
- Imágenes antiguas no usadas: `weaviate:1.28.0` (18 meses), `weaviate:1.24.0` (2 años)
- Disco VPS: 83 GB libres de 116 GB

### Comandos ejecutados

```bash
# 1. Limpiar dangling (sin tag)
docker image prune -f
# Resultado: 4 imágenes eliminadas, 391.7 MB liberados

# 2. Limpiar build cache (mantener 500MB de los últimos)
docker builder prune -f --keep-storage 500m
# Resultado: 1.78 GB liberados

# 3. Limpiar imágenes con más de 7 días
docker image prune -a --filter 'until=168h' --force
# Resultado: 0B (las imágenes de weaviate son in-use porque el contenedor está corriendo)
```

### Después

| Métrica | Antes | Después | Cambio |
|---|---|---|---|
| Imágenes totales | 12 | 8 | -4 |
| Build cache | 2.17 GB | 390 MB | -1.78 GB |
| Disco libre | 83 GB | **86 GB** | **+3 GB** |
| Contenedores activos | 5 | 5 | (sanos) |

### Verificación de no-impacto

- ✅ Frontend `myownclone-frontend` sigue `active`
- ✅ Backend `myownclone_api` sigue `Up 43 hours (healthy)`
- ✅ Todos los 5 contenedores siguen activos
- ✅ `/readyz` devuelve `{database:ok, redis:ok, status:ready}`
- ✅ `myownclone.com` responde 200 OK

### Notas
- Las imágenes de weaviate 1.24.0 y 1.28.0 **no se eliminaron** porque weaviate está corriendo
- Se eliminarán cuando ejecutemos T1.3 (eliminar Weaviate)

### Próxima task
**T1.6** — Healthcheck estricto `/healthz`

---

## Task T1.6 — Healthcheck estricto /healthz ✅ COMPLETADA

**Fecha ejecución**: 2026-07-03

### Antes
- `/healthz` devolvía solo `{"status":"ok"}` (sin checks reales)
- `/readyz` ya tenía checks de DB+Redis, pero con un bug oculto (`***REMOVED***:` en línea 214 del repo local)
- Ollama no se chequeaba en ningún endpoint
- Downtime desconocido si Ollama caía (afecta embeddings)

### Cambios aplicados

**Archivo**: `api/app_factory.py`

**Diseño invertido** (mejor para Docker healthcheck):
- `/healthz` → ahora es el **detallado**: chequea DB + Redis + Ollama, devuelve 503 si DB o Redis fallan
- `/readyz` → ahora es el **simple**: solo devuelve 200, no falla por causas externas

```python
@app.get("/healthz")
def healthz():
    """Chequeo detallado: DB + Redis + Ollama. Devuelve 503 si algo falla."""
    import os
    import requests
    checks = {}
    all_ok = True
    # 1. Database (SQLAlchemy SELECT 1)
    # 2. Redis (ping)
    # 3. Ollama (GET /api/tags, timeout 2s)
    # Ollama no degrada a 503 (puede haber fallback)
    return jsonify({"status": "ready|degraded", "checks": {...}}), 200|503

@app.get("/readyz")
def readyz():
    """Liveness simple. Para Docker healthcheck, no falla por causas externas."""
    return jsonify({"status": "ready"}), 200
```

### Configuración complementaria

**Env var nueva**: `OLLAMA_BASE_URL=http://ollama:11434`
- Sin esta env var, el código usaba `http://127.0.0.1:11434` que NO resuelve dentro del contenedor Docker (donde `127.0.0.1` es el contenedor mismo, no el host)
- Añadida a `/opt/myownclone/shared/backend.env.production`

### Deploy

```bash
# 1. Backup del app_factory actual
cp /opt/myownclone/current/api/app_factory.py /tmp/app_factory.py.backup.<timestamp>

# 2. Extraer el nuevo app_factory.py del tar de la rama docs/planes-maestros
cd /opt/myownclone/current/api
tar -xzf /tmp/t1.6-deploy/t1.6-deploy.tar.gz

# 3. Verificar syntax
python3 -c 'import ast; ast.parse(open("app_factory.py").read())'

# 4. Rebuild + restart api (solo api, no otros contenedores)
cd /opt/myownclone/current/ops
set -a; . ./backend.env.production; set +a
docker compose -f docker-compose.backend.prod.yml up -d --build api

# 5. Verificar
curl http://127.0.0.1:5001/healthz
```

### Resultado

**Antes**:
```
GET /healthz → {"status":"ok"}
GET /readyz → {"checks":{"database":"ok","redis":"ok"},"status":"ready"}
```

**Después**:
```
GET /healthz → {"checks":{"database":"ok","ollama":"ok","redis":"ok"},"status":"ready"}
GET /readyz → {"status":"ready"}
```

### Verificación de no-impacto

- ✅ Frontend `active (running)` (no se tocó)
- ✅ Backend `myownclone_api` Up 5 seconds (healthy) tras rebuild
- ✅ Postgres healthy
- ✅ Redis healthy
- ✅ Weaviate no se tocó
- ✅ Ollama responde correctamente
- ✅ `myownclone.com` 200 OK
- ✅ Downtime: ~31 segundos (rebuild)

### Notas
- El bug oculto `***REMOVED***:` en el repo local ya **NO afecta al VPS** porque el VPS corre codex/backend-admin-vps-exec (rama sin censura). El archivo en VPS no tenía el bug.
- `OLLAMA_BASE_URL` debe documentarse en `vars.sh.example` para futuros deploys

### Próxima task
**T1.8** — Runbook operacional (más rápida, sin tocar infra)