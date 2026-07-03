# T3.4 — Réplicas de lectura PostgreSQL (PREPARACIÓN, no desplegado)

**Fecha**: 2026-07-03
**Estado**: Documentado, NO desplegado (innecesario con DB actual de 9.6 MB)

## Cuándo aplicar

| Señal | Acción |
|---|---|
| DB > 10 GB | Evaluar réplicas |
| Conexiones > 80 (de 100) | Réplicas urgentes |
| Queries lentas (>500ms) en producción | Investigar + réplicas |
| >1000 queries/segundo | Réplicas obligatorias |

## Arquitectura propuesta (cuando se necesite)

```
                    ┌─ Postgres Primary (writes) ─┐
App → pgpool2 →────┤                              ├─ WAL streaming
                    └─ Postgres Read Replica ────┘
```

- **Primary**: 1 instancia, recibe writes + reads
- **Replica**: 1+ instancias, solo reads (sincronizadas vía WAL)
- **pgpool2** o **HAProxy**: distribuye queries (writes → primary, reads → replicas)

## Setup manual (cuando se necesite)

### 1. Crear volumen para la replica
```bash
ssh root@212.227.169.99
docker volume create ops_postgres_replica_data
```

### 2. Levantar replica
```yaml
# En docker-compose.backend.prod.yml:
db_postgres_replica:
  image: pgvector/pgvector:pg15
  container_name: myownclone_postgres_replica
  restart: unless-stopped
  networks:
    - backend_internal
  environment:
    POSTGRES_USER: postgres
    POSTGRES_PASSWORD: ${DB_PASSWORD}
    POSTGRES_DB: myownclone
  volumes:
    - postgres_replica_data:/var/lib/postgresql/data
  command: >
    postgres
      -c hot_standby=on
      -c primary_conninfo='host=db_postgres port=5432 user=replicator password=${DB_PASSWORD}'
      -c primary_slot_name=replica_slot
  deploy:
    resources:
      limits:
        memory: 1G
        cpus: "0.5"
```

### 3. Crear replication slot en primary
```sql
-- Desde el primary:
SELECT pg_create_physical_replication_slot('replica_slot');
```

### 4. Configurar SQLAlchemy para usar replica en reads

Modificar `api/extensions/ext_database.py`:
```python
# engine principal: writes + reads críticos
write_engine = create_engine(WRITE_DB_URL)

# engine replica: solo reads (analytics, listados, etc.)
read_engine = create_engine(READ_REPLICA_URL, pool_pre_ping=True)

# Router: writes al primary, reads a la replica
class ReadWriteRouter:
    def db_for_read(self, *args, **kwargs):
        return read_engine
    def db_for_write(self, *args, **kwargs):
        return write_engine
```

### 5. Validar
```sql
-- En la replica:
SELECT pg_is_in_recovery();  -- debe ser true
SELECT pg_last_wal_replay_lsn();  -- debe avanzar
```

## Limitaciones con el VPS actual

- **2 cores / 3.8 GB RAM** — no hay espacio para correr 2 Postgres + pgpool2
- **DB de 9.6 MB** — réplicas serían overhead puro
- **Cero carga de queries** — la app actual no se acerca a necesitar réplicas

## Cuando llegues a >50 usuarios activos, evalúa:

1. **Upgrade VPS** a 8 GB RAM (~€20/mes) — habilita réplicas
2. **Read replicas** como опис
3. **Connection pooling** (pgBouncer) para >200 conexiones

## Status actual

- Documento: ✅
- Implementación: NO (innecesario)
- Triggger para implementar: >10 GB DB OR >80 conexiones OR >500ms latencia p99