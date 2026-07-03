# FASE 3 — Escalar Infraestructura

> **Objetivo**: Preparar el VPS para >100 usuarios, opcionalmente IA 100% local, CDN y HA.
> **Tiempo estimado**: 1-2 semanas
> **Urgencia**: 🟢 Futuro (cuando el tráfico lo justifique)
> **Prerequisitos**: FASE 1 + FASE 2 completadas

---

## Tasks

### T3.1 — Upgrade del VPS (más CPU/RAM)

**Cuándo**: Cuando llegues a ~30 usuarios simultáneos o el load average > 2.0.

**Problema actual**: 2 cores / 3.8 GB RAM. Ollama solo puede cargar modelos pequeños. Gunicorn con 2 workers.

#### Pasos

1. **Hacer upgrade en el proveedor del VPS** (Hetzner, DigitalOcean, etc.).
2. **Tier recomendado por escala**:

| Nivel | CPU | RAM | Disco | Usuarios aprox. | Coste/mes aprox. |
|---|---|---|---|---|---|
| Actual | 2 | 3.8 GB | 116 GB | ~50 | ~€10 |
| **Fase crecimiento** | 4 | 8 GB | 160 GB | ~200 | ~€20 |
| **Fase escala** | 8 | 16 GB | 320 GB | ~500 | ~€40 |
| **IA local chat** | 8 | 32 GB | 320 GB | ~200 + LLM local | ~€80 |

3. **Después del upgrade** (suele requerir reboot del VPS):
```bash
# Verificar nuevos recursos
nproc
free -h
df -h
```

4. **Aumentar gunicorn workers** en `api/Dockerfile`:
```dockerfile
# workers = (CPU cores * 2) + 1
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "--workers", "5", ...]
```

5. **Aumentar Postgres config**:
```sql
ALTER SYSTEM SET shared_buffers = '2GB';
ALTER SYSTEM SET max_connections = 200;
ALTER SYSTEM SET effective_cache_size = '6GB';
SELECT pg_reload_conf();
```

#### Verificación
- `nproc` muestra nuevo número de cores
- `free -h` muestra nueva RAM
- Stress test: `ab -n 1000 -c 50 https://myownclone.com/`

---

### T3.2 — IA local para chat (Ollama LLM, no solo embeddings)

**Cuándo**: Cuando quieras eliminar dependencia de MiniMax/OpenAI para chat.

**Requisito**: Mínimo 8 GB RAM (preferible 16 GB).

**Problema actual**: Ollama solo tiene `mxbai-embed-large` (embeddings). Para chat local necesitas un LLM generativo.

#### Pasos

1. **Instalar modelo de chat en Ollama**:
```bash
ssh root@212.227.169.99
docker exec myownclone_ollama ollama pull llama3.2:3b
# O si tienes 16GB RAM:
# docker exec myownclone_ollama ollama pull llama3.1:8b
```

2. **Registrar modelo local en el catálogo IA**:
```sql
INSERT INTO ai_models (id, name, provider, model_id, api_key_encrypted, base_url, is_active)
VALUES (
  gen_random_uuid()::varchar,
  'Local Llama 3.2 3B',
  'local',
  'llama3.2:3b',
  '',  -- sin API key
  'http://ollama:11434',
  true
);
```

3. **Crear asignación para chat local**:
```sql
INSERT INTO ai_model_assignments (task, model_id, priority)
VALUES ('chat', '<llama_model_id>', 300);  -- prioridad alta
```

4. **Verificar que el provider adapter de Ollama soporta chat** (no solo embeddings):
```python
# api/core/providers/ollama_adapter.py
# Debe manejar /api/chat además de /api/embeddings
```

#### Modelos recomendados por RAM

| Modelo | RAM mínima | Calidad | Velocidad |
|---|---|---|---|
| `llama3.2:1b` | 2 GB | Baja | Muy rápida |
| `llama3.2:3b` | 3 GB | Media | Rápida |
| `llama3.1:8b` | 6 GB | Buena | Media |
| `qwen2.5:7b` | 5 GB | Buena | Media |
| `mistral:7b` | 5 GB | Buena | Media |

#### Verificación
- Chat funciona usando modelo local
- `docker stats` muestra Ollama usando más RAM cuando chatea

---

### T3.3 — CDN para assets estáticos

**Cuándo**: Cuando tengas >100 usuarios o sirvas muchos assets.

**Problema actual**: Nginx sirve todo (CSS, JS, imágenes, fuentes). Sin CDN, la latencia es alta para usuarios lejanos.

**Solución**: Cloudflare Free (gratis) o Bunny.net.

#### Pasos (Cloudflare)

1. **Crear cuenta en Cloudflare**.
2. **Añadir dominio** `myownclone.com`.
3. **Cambiar nameservers** del dominio a los de Cloudflare.
4. **Configurar reglas**:
   - Cache everything para `/static/*`, `/_next/static/*`
   - Bypass cache para `/api/*`, `/console/api/*`
5. **Verificar** que el tráfico pasa por Cloudflare (headers `cf-ray`).

#### Alternativa: Bunny.net o AWS CloudFront

Si prefieres no usar Cloudflare (que hace proxy completo), usar Bunny.net para assets específicos:
```nginx
# Para assets estáticos, redirigir a CDN
location /static/ {
    rewrite ^/static/(.*)$ https://myownclone.b-cdn.net/static/$1 redirect;
}
```

#### Verificación
- `curl -sI https://myownclone.com/_next/static/chunks/main.js | grep cf-ray` muestra header
- PageSpeed Insights mejora puntuación

---

### T3.4 — Leer réplicas de PostgreSQL

**Cuándo**: Cuando la DB sea un cuello de botella (>1000 queries/segundo).

**Problema actual**: 1 sola instancia de Postgres para todo (writes + reads).

**Solución**: Añadir réplica de solo lectura.

#### Arquitectura

```
                    ┌─ Postgres Primary (writes) ─┐
Aplicación ─────────┤                              ├─ WAL shipping
                    └─ Postgres Replica (reads) ───┘
```

#### Pasos

1. **Añadir servicio réplica** en docker-compose:
```yaml
db_postgres_replica:
  image: pgvector/pgvector:pg15
  container_name: myownclone_postgres_replica
  environment:
    POSTGRES_USER: postgres
    POSTGRES_PASSWORD: ${DB_PASSWORD}
    PGUSER: replicator
  volumes:
    - postgres_replica_data:/var/lib/postgresql/data
  command: >
    postgres
      -c hot_standby=on
      -c primary_conninfo='host=db_postgres port=5432 user=replicator password=${DB_PASSWORD}'
```

2. **Configurar aplicación para separar reads/writes**:
```python
# Flask-SQLAlchemy: usar binds o session routing
READ_DB = "postgresql://..."
WRITE_DB = "postgresql://..."

# En queries de lectura (analytics, retrieval):
db.session.bind = READ_DB
```

#### Verificación
- Writes van al primary
- Reads van al replica
- Lag < 1 segundo

---

### T3.5 — Worker asíncrono (Celery o RQ)

**Cuándo**: Cuando la ingestion de fuentes tarde >10 segundos (PDFs grandes).

**Problema actual**: La ingestion es sincrónica. Si un usuario sube un PDF de 100 páginas, el request HTTP se bloquea hasta terminar.

**Solución**: Queue asíncrona con Redis + worker.

#### Arquitectura

```
POST /sources → enqueue job → 202 Accepted
                     ↓
              Redis Queue (RQ o Celery)
                     ↓
              Worker procesa ingestion en background
                     ↓
              UPDATE sources SET status='ready'
```

#### Pasos

1. **Añadir dependencias**:
```
rq>=1.15.0
```

2. **Crear worker config**:
```python
# api/core/queue.py
from redis import Redis
from rq import Queue

redis = Redis.from_url(os.environ['REDIS_URL'])
q = Queue('ingestion', connection=redis)

def enqueue_ingestion(source_id: str):
    q.enqueue(api.core.ingestion.ingest_source, source_id, timeout=600)
```

3. **Añadir servicio worker** en docker-compose:
```yaml
api_worker:
  build:
    context: ../api
    dockerfile: Dockerfile
  command: rq worker ingestion --url redis://redis:6379
  container_name: myownclone_worker
  env_file: ./backend.env.production
  depends_on:
    redis:
      condition: service_healthy
```

4. **Modificar endpoint** para encolar en vez de procesar sincrónico:
```python
# clone.py
from api.core.queue import enqueue_ingestion
source = Source(...)
db.session.add(source)
db.session.commit()
enqueue_ingestion(str(source.id))
return jsonify({"status": "processing"}), 202
```

#### Verificación
- POST /sources devuelve 202 inmediatamente
- Worker procesa en background
- Polling del status funciona

---

### T3.6 — Monitoreo con Prometheus + Grafana

**Cuándo**: Cuando necesitas visibilidad de métricas (latencia, errores, recursos).

**Solución**: Stack de monitoreo completo.

#### Arquitectura

```
Exporter → Prometheus → Grafana Dashboard
  ├─ node_exporter (VPS metrics)
  ├─ postgres_exporter (DB metrics)
  ├─ redis_exporter (cache metrics)
  └─ flask metrics (app metrics)
```

#### Pasos

1. **Añadir servicios** en un docker-compose de monitoreo separado:
```yaml
# ops/docker-compose.monitoring.yml
services:
  prometheus:
    image: prom/prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - "127.0.0.1:9090:9090"

  grafana:
    image: grafana/grafana
    ports:
      - "127.0.0.1:3001:3000"
    volumes:
      - grafana_data:/var/lib/grafana
```

2. **Configurar Prometheus scrape**:
```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'node'
    static_configs:
      - targets: ['node_exporter:9100']
  - job_name: 'postgres'
    static_configs:
      - targets: ['postgres_exporter:9187']
  - job_name: 'flask'
    static_configs:
      - targets: ['api:5000']
```

3. **Añadir Prometheus middleware a Flask**:
```python
# app_factory.py
from prometheus_client import generate_latest, Counter, Histogram

REQUEST_COUNT = Counter('flask_requests_total', 'Total requests', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('flask_request_duration_seconds', 'Request latency')
```

#### Verificación
- Grafana dashboard muestra métricas en tiempo real
- Alertas configuradas para CPU > 80%, errores > 1%

---

### T3.7 — Multi-región / alta disponibilidad

**Cuándo**: Cuando no puedes tolerar downtime (>99.9% uptime).

**Solución**: Despliegue multi-región con load balancer.

#### Arquitectura simplificada

```
                    ┌─ Load Balancer (HAProxy/Nginx) ─┐
                    │                                   │
        ┌───────────┼───────────┐                       │
        ↓           ↓           ↓                       │
   VPS EU      VPS US     VPS LATAM                    │
   (primary)   (replica)  (replica)                    │
        │           │           │                       │
        └───────────┴───────────┘                       │
                    ↓                                   │
              Postgres Primary                          │
              + Réplicas síncronas                      │
```

#### Nota
**Esto es complejo y caro.** Solo considerarlo cuando el producto genere ingresos que lo justifiquen. Para la mayoría de SaaS初期, un solo VPS con backups off-site es suficiente.

#### Pasos de alto nivel

1. Desplegar el mismo stack en 2-3 regiones.
2. Configurar DNS failover (Cloudflare o Route53).
3. Postgres replicación síncrona entre regiones.
4. Sesiones sticky o compartidas (Redis cluster).
5. Health checks automáticos.

---

## Resumen FASE 3

| Task | Descripción | Tiempo | Cuándo |
|---|---|---|---|
| T3.1 | Upgrade VPS (más recursos) | 2h | >30 usuarios simultáneos |
| T3.2 | IA local para chat | 3h | >8GB RAM |
| T3.3 | CDN para assets | 2h | >100 usuarios |
| T3.4 | Leer réplicas Postgres | 1 día | >1000 qps DB |
| T3.5 | Worker asíncrono | 1 día | PDFs grandes |
| T3.6 | Prometheus + Grafana | 1 día | Necesidad de observabilidad |
| T3.7 | Multi-región HA | 1 semana | >99.9% uptime requerido |

**Orden recomendado**: T3.1 → T3.5 → T3.3 → T3.2 → T3.6 → T3.4 → T3.7

---

## Indicadores de cuándo escalar

| Señal | Acción |
|---|---|
| Load average > 2.0 sostenido | T3.1 (upgrade VPS) |
| Tiempo de ingestion > 10s | T3.5 (worker async) |
| DB CPU > 70% | T3.4 (réplicas) |
| Latencia chat > 5s | T3.2 (IA local) o fallback LLM |
| Peticiones globales | T3.3 (CDN) |
| Downtime inaceptable | T3.7 (HA) |

---

*Este plan debe revisarse trimestralmente según evolucione el tráfico y los requisitos del producto.*
