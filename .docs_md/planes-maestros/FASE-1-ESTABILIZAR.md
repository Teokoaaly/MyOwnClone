# FASE 1 — Estabilizar Backend (Crítico)

> **Objetivo**: Garantizar que no se pierden datos, el RAG es rápido, y los deploys no rompen el schema.
> **Tiempo estimado**: 4-6 horas
> **Urgencia**: 🔴 Crítico (producción con usuarios)
> **Prerequisito**: Acceso SSH al VPS, rama `codex/backend-admin-vps-exec`

---

## Tasks

### T1.1 — Backup off-site a almacenamiento externo

**Problema**: Los backups solo existen en `/opt/myownclone/backups/` en el mismo VPS. Si el VPS muere, se pierde todo.

**Solución**: Subir cada backup diario a almacenamiento externo (S3, Backblaze B2, o similar).

#### Pasos

1. **Crear cuenta y bucket en Backblaze B2** (más barato que S3) o AWS S3.
2. **Instalar CLI en el VPS**:
```bash
ssh -i ~/.ssh/myownclone_vps_ed25519 root@212.227.169.99

# Instalar rclone (más versátil que aws-cli)
curl https://rclone.org/install.sh | sudo bash

# Configurar remote
rclone config
# Seguir asistente: name=myownclone, type=b2 o s3, keys, bucket
```

3. **Modificar el cron de backup** para subir después del dump:
```bash
# Editar crontab
crontab -e

# Reemplazar la línea actual con:
0 3 * * * /opt/myownclone/current/ops/backup_postgres.sh 7 && rclone copy /opt/myownclone/backups/ myownclone:myownclone-backups/db/ --progress >> /var/log/myownclone-backup-offsite.log 2>&1
```

4. **Verificar manualmente**:
```bash
rclone copy /opt/myownclone/backups/ myownclone:myownclone-backups/db/ --dry-run
```

#### Verificación
- `rclone ls myownclone:myownclone-backups/db/` muestra los backups
- El log `/var/log/myownclone-backup-offsite.log` no tiene errores

#### Rollback
- Revertir crontab a la versión anterior (sin rclone)

---

### T1.2 — Índice vectorial ivfflat en pgvector

**Problema**: La tabla `chunks` tiene columna `embedding` (array) pero **sin índice vectorial**. Con >10.000 documentos, la búsqueda semántica será O(n) — lenta.

**Solución**: Crear índice ivfflat optimizado.

#### Pasos

1. **Verificar el tipo de la columna embedding**:
```bash
ssh -i ~/.ssh/myownclone_vps_ed25519 root@212.227.169.99
docker exec myownclone_postgres psql -U postgres -d myownclone -c "
SELECT column_name, data_type, udt_name
FROM information_schema.columns
WHERE table_name = 'chunks' AND column_name = 'embedding';
"
```

2. **Si `embedding` es `ARRAY` (no `vector`), necesita conversión**:
```sql
-- Solo si embedding es ARRAY, no vector:
-- Esto requiere migración de schema. Consultar antes.
-- Si ya es vector(1024) o vector(1536), saltar al paso 3.
```

3. **Crear índice ivfflat** (si la columna ya es tipo `vector`):
```sql
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_chunks_embedding_ivfflat
ON chunks USING ivfflat (embedding vector_cosine_ops)
WITH (lists = 100);

-- Analizar para que el planner use el índice
ANALYZE chunks;
```

4. **Si `lists = 100` no es óptimo** (regla general: `sqrt(row_count)`):
   - < 10.000 rows: `lists = 100`
   - 10.000-100.000 rows: `lists = sqrt(rows)`
   - > 100.000 rows: `lists = 1000`

#### Verificación
```sql
EXPLAIN SELECT * FROM chunks ORDER BY embedding <-> '[0.1, 0.2, ...]' LIMIT 5;
-- Debe mostrar "Index Scan using idx_chunks_embedding_ivfflat"
```

#### Rollback
```sql
DROP INDEX CONCURRENTLY IF EXISTS idx_chunks_embedding_ivfflat;
```

#### ⚠️ Nota sobre tipo de dato
La auditoría mostró que `chunks.embedding` es `ARRAY`, no `vector`. Esto significa que pgvector no está siendo usado para búsqueda semántica en pg — los embeddings van a Weaviate. **Antes de crear el índice, hay que decidir si migrar embeddings a pgvector (FASE 1 T1.4) o quedarse con Weaviate.**

---

### T1.3 — Eliminar Weaviate del stack (redundante con pgvector)

**Problema**: Hay DOS stores vectoriales corriendo: pgvector (PostgreSQL) y Weaviate. Esto duplica recursos y complejidad.

**Decisión**: Quedarse solo con pgvector. Es más simple, transaccional con los datos, y un servicio menos que mantener.

#### Pasos

1. **Verificar que Weaviate no tiene datos críticos**:
```bash
ssh root@212.227.169.99
# Intentar listar esquemas (requiere auth)
WEAVIATE_KEY=$(grep WEAVIATE_API_KEY /opt/myownclone/shared/backend.env.production | cut -d= -f2)
curl -H "Authorization: Bearer $WEAVIATE_KEY" http://127.0.0.1:8080/v1/schema
```

2. **Verificar que el código usa Weaviate (no pgvector) para retrieval**:
```bash
# En el repo local:
grep -rn "weaviate" api/core/retrieval.py api/core/embeddings.py
```

3. **Si el código depende de Weaviate para retrieval**:
   - NO eliminar Weaviate todavía
   - En su lugar, migrar el código de retrieval a pgvector primero (ver FASE 2 T2.1)
   - Volver a este task después de FASE 2

4. **Si el código ya NO usa Weaviate**:
```bash
# En el VPS:
cd /opt/myownclone/current/ops

# Quitar weaviate del docker-compose
# Editar docker-compose.backend.prod.yml y eliminar el servicio weaviate
# Eliminar el volume ops_weaviate_data

# Restart sin weaviate
docker compose -f docker-compose.backend.prod.yml up -d --remove-orphans
```

5. **Limpiar volumen**:
```bash
docker volume rm ops_weaviate_data
```

#### Verificación
- `docker ps` no muestra `myownclone_weaviate`
- RAM libre aumenta ~30 MB
- `/readyz` sigue dando `{status: ready}`
- Chat funciona normalmente

#### Rollback
```bash
# Restaurar weaviate del compose (git checkout del archivo)
docker compose -f docker-compose.backend.prod.yml up -d
```

---

### T1.4 — Migrar `chunks.embedding` de ARRAY a `vector(1024)`

**Problema**: La columna `embedding` en `chunks` es tipo `ARRAY` (float[]), no `vector` (tipo pgvector). Sin tipo vector, no se puede crear índice ivfflat ni usar operadores de distancia.

**Solución**: Migrar la columna a tipo `vector`.

#### Pasos

1. **Crear migración Alembic**:
```bash
# En el repo local, rama codex/backend-admin-vps-exec:
cd api/migrations/versions/
```

Crear archivo `2026_07_02_0001_chunks_embedding_to_vector.py`:
```python
"""chunks.embedding: ARRAY -> vector(1024)

Revision ID: 2026_07_02_0001
Revises: 2026_06_27_0001
Create Date: 2026-07-02
"""
from alembic import op
import sqlalchemy as sa

revision = '2026_07_02_0001'
down_revision = '2026_06_27_0001'
branch_labels = None
depends_on = None

def upgrade():
    # Solo si hay datos: convertir ARRAY a vector
    op.execute("""
        ALTER TABLE chunks
        ALTER COLUMN embedding TYPE vector(1024)
        USING array_to_vector(embedding::double precision[])::vector(1024);
    """)
    # Crear índice ivfflat
    op.execute("""
        CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_chunks_embedding_ivfflat
        ON chunks USING ivfflat (embedding vector_cosine_ops)
        WITH (lists = 100);
    """)

def downgrade():
    op.execute("DROP INDEX CONCURRENTLY IF EXISTS idx_chunks_embedding_ivfflat;")
    op.execute("""
        ALTER TABLE chunks
        ALTER COLUMN embedding TYPE double precision[]
        USING ARRAY(SELECT * FROM unnest(embedding::real[]));
    """)
```

⚠️ **Nota**: `array_to_vector` no es función estándar. Verificar la función de conversión correcta en la docs de pgvector. Alternativa:
```sql
-- Si embedding es text[] con valores float:
ALTER TABLE chunks ALTER COLUMN embedding TYPE vector(1024)
USING (SELECT vector(embedding::float4[])::vector(1024));
```

2. **Actualizar el modelo SQLAlchemy** en `api/models/dataset.py` o donde esté `Chunk`:
```python
from pgvector.sqlalchemy import Vector

class Chunk(TypeBase):
    __tablename__ = 'chunks'
    # ...
    embedding: Mapped[list[float]] = mapped_column(Vector(1024), nullable=True)
```

3. **Probar la migración en local antes de producción**.

4. **Aplicar en producción**:
```bash
ssh root@212.227.169.99
docker exec myownclone_api flask --app api.app_factory db upgrade
```

#### Verificación
```sql
SELECT column_name, data_type FROM information_schema.columns
WHERE table_name='chunks' AND column_name='embedding';
-- data_type debe ser USER-DEFINED (vector)

\d chunks
-- Debe mostrar: embedding | vector(1024)
```

#### Rollback
```bash
docker exec myownclone_api flask --app api.app_factory db downgrade -1
```

---

### T1.5 — Migraciones automáticas en deploy

**Problema**: `flask db upgrade` NO se ejecuta durante el deploy. El schema puede desincronizarse del código.

**Solución**: Crear entrypoint script que ejecute migraciones antes de gunicorn.

#### Pasos

1. **Crear `api/entrypoint.sh`**:
```bash
#!/bin/sh
set -e

echo "[entrypoint] Ejecutando migraciones..."
cd /app
flask --app api.app_factory db upgrade

echo "[entrypoint] Arrancando gunicorn..."
exec gunicorn --bind 0.0.0.0:5001 --workers 2 --timeout 60 \
  --access-logfile - --error-logfile - api.app_factory:app
```

2. **Modificar `api/Dockerfile`** para usar entrypoint:
```dockerfile
# Al final del Dockerfile, reemplazar CMD directo:
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
# Eliminar el CMD anterior de gunicorn directo
```

3. **Verificar en local** con `docker build` + `docker run`.

4. **Deploy al VPS** (como hicimos en la sesión anterior: tar + scp + symlink swap + compose up).

#### Verificación
```bash
# Después del deploy, logs del contenedor api deben mostrar:
# [entrypoint] Ejecutando migraciones...
# [entrypoint] Arrancando gunicorn...
docker logs myownclone_api | head -5
```

#### Rollback
- Restaurar Dockerfile anterior (sin entrypoint, CMD directo gunicorn)
- Redeploy

---

### T1.6 — Healthcheck más estricto del backend

**Problema**: El healthcheck actual solo verifica `/readyz`. No detecta si endpoints críticos fallan.

**Solución**: Ampliar healthcheck con checks de DB + Redis + endpoints clave.

#### Pasos

1. **Crear endpoint `/healthz` detallado** en `api/app_factory.py` o un blueprint nuevo:
```python
@app.route('/healthz')
def healthz():
    checks = {}
    # DB
    try:
        db.session.execute(db.text('SELECT 1'))
        checks['database'] = 'ok'
    except Exception:
        checks['database'] = 'error'
    # Redis
    try:
        from api.extensions.ext_redis import redis_client
        redis_client.ping()
        checks['redis'] = 'ok'
    except Exception:
        checks['redis'] = 'error'
    # Ollama (si embedding es local)
    try:
        import requests
        r = requests.get('http://127.0.0.1:11434/api/tags', timeout=2)
        checks['ollama'] = 'ok' if r.status_code == 200 else 'error'
    except Exception:
        checks['ollama'] = 'unreachable'

    all_ok = all(v == 'ok' for v in checks.values())
    return jsonify({
        'status': 'ready' if all_ok else 'degraded',
        'checks': checks
    }), 200 if all_ok else 503
```

2. **Actualizar healthcheck de Docker** en `docker-compose.backend.prod.yml`:
```yaml
api:
  healthcheck:
    test: ["CMD-SHELL", "curl -fsS http://127.0.0.1:5001/healthz || exit 1"]
    interval: 30s
    timeout: 10s
    retries: 5
    start_period: 30s
```

#### Verificación
```bash
curl http://127.0.0.1:5001/healthz
# {"status":"ready","checks":{"database":"ok","redis":"ok","ollama":"ok"}}
```

---

### T1.7 — Limpiar imágenes Docker viejas

**Problema**: Hay imágenes Docker antiguas acumuladas (build cache 2.17 GB + imágenes `<none>`).

**Solución**: Limpiar para recuperar espacio.

#### Pasos

```bash
ssh root@212.227.169.99

# Limpiar imágenes sin tag (dangling)
docker image prune -f

# Limpiar build cache viejo
docker builder prune -f --keep-storage 500m

# Limpiar imágenes antiguas no usadas
docker image prune -a --filter "until=168h" --force

# Verificar espacio recuperado
docker system df
```

#### Verificación
- `docker system df` muestra menos espacio usado
- `df -h /` muestra más espacio libre

#### ⚠️ No borrar imágenes en uso
El comando `--filter "until=168h"` solo afecta imágenes de hace más de 7 días. Las actuales están a salvo.

---

### T1.8 — Documentar runbook operacional

**Problema**: No hay documentación operacional centralizada para el VPS actual.

**Solución**: Crear `RUNBOOK_VPS.md` en `.docs_md/`.

#### Contenido obligatorio

```markdown
# Runbook VPS — MyOwnClone Producción

## Acceso
- Host: 212.227.169.99
- Usuario: root
- Clave: ~/.ssh/myownclone_vps_ed25519
- Comando: ssh -i ~/.ssh/myownclone_vps_ed25519 root@212.227.169.99

## Servicios
| Servicio | Comando status | Comando restart |
|---|---|---|
| Frontend | systemctl status myownclone-frontend | systemctl restart myownclone-frontend |
| Backend | docker ps | cd /opt/myownclone/current/ops && docker compose -f docker-compose.backend.prod.yml up -d --build |
| Nginx | systemctl status nginx | systemctl restart nginx |

## Rollback
1. Identificar release anterior: cat /opt/myownclone/shared/.backend-prev-release
2. Repoint symlink: ln -sfn <release-anterior> /opt/myownclone/current
3. Restart frontend + backend

## Backups
- Diario 03:00 UTC: /opt/myownclone/backups/
- Off-site: rclone a B2/S3
- Restaurar: gunzip -c backup.sql.gz | docker exec -i myownclone_postgres psql -U postgres -d myownclone

## Emergencias
- Si la web cae: systemctl restart myownclone-frontend nginx
- Si el backend cae: docker compose up -d --build
- Si la DB cae: docker restart myownclone_postgres, esperar healthy
```

#### Verificación
- Archivo existe en `.docs_md/RUNBOOK_VPS.md`
- Contiene todos los comandos operacionales

---

## Resumen FASE 1

| Task | Descripción | Tiempo | Dependencias |
|---|---|---|---|
| T1.1 | Backup off-site | 1h | Cuenta B2/S3 |
| T1.2 | Índice ivfflat | 30min | T1.4 (si embedding es ARRAY) |
| T1.3 | Eliminar Weaviate | 1h | Verificar uso en código |
| T1.4 | Migrar embedding a vector | 2h | Tests locales primero |
| T1.5 | Migraciones automáticas | 1h | T1.4 |
| T1.6 | Healthcheck estricto | 30min | Ninguna |
| T1.7 | Limpiar Docker | 15min | Ninguna |
| T1.8 | Runbook | 30min | Ninguna |

**Orden recomendado**: T1.7 → T1.6 → T1.8 → T1.1 → T1.4 → T1.2 → T1.3 → T1.5
