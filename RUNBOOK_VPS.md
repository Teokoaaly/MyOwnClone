# Runbook VPS — MyOwnClone Producción

> **Última actualización**: 2026-07-03
> **Servidor**: VPS de producción
> **Dominio**: myownclone.com

---

## 1. Acceso

```bash
# Conexión SSH
ssh -i ~/.ssh/myownclone_vps_ed25519 root@212.227.169.99

# Clave pública (ya en authorized_keys de root)
~/.ssh/myownclone_vps_ed25519 (ED25519)
```

## 2. Servicios

| Servicio | Comando status | Comando restart |
|---|---|---|
| **Frontend** (Next.js) | `systemctl status myownclone-frontend` | `systemctl restart myownclone-frontend` |
| **Backend API** (Docker) | `docker ps` | `cd /opt/myownclone/current/ops && docker compose -f docker-compose.backend.prod.yml up -d --build api` |
| **PostgreSQL** | `docker ps` | `docker restart myownclone_postgres` |
| **Redis** | `docker ps` | `docker restart myownclone_redis` |
| **Ollama** | `docker ps` | `docker restart myownclone_ollama` |
| **Weaviate** | `docker ps` | `docker restart myownclone_weaviate` |
| **Nginx** | `systemctl status nginx` | `systemctl restart nginx` |

## 3. Layout del VPS

```
/opt/myownclone/
├── current → /opt/myownclone/releases/<release-id>   # symlink activo
├── releases/
│   ├── 20260620070304-frontend-dashboard-fix         # release antiguo (20 jun)
│   ├── 20260629141926-i18n-manual-selector          # 29 jun
│   ├── 20260629144355-frontend-i18n-selector         # 29 jun
│   ├── 20260630081811-dashboard-route-fix → symlink  # 30 jun (alias)
│   └── 20260701150141-backend-codex-deploy           # ACTIVO (f0418c0)
├── shared/
│   ├── backend.env.production                        # secrets del backend
│   └── frontend.env.production                       # secrets del frontend
└── backups/                                           # pg_dump diarios (cron 03:00 UTC)
```

## 4. Comandos frecuentes

### Ver estado de la app
```bash
# Healthcheck detallado (DB + Redis + Ollama)
curl -s http://127.0.0.1:5001/healthz | python3 -m json.tool

# Healthcheck simple (liveness)
curl -s http://127.0.0.1:5001/readyz

# Healthcheck público
curl -sI https://myownclone.com

# Logs del backend en vivo
docker logs -f myownclone_api

# Logs del frontend en vivo
journalctl -u myownclone-frontend -f
```

### Ver qué release está activo
```bash
readlink /opt/myownclone/current
ls -la /opt/myownclone/current/
cat /opt/myownclone/current/.deploy-backend-meta 2>/dev/null
```

### Deploy manual (sin script)
```bash
# 1. Crear release dir
NEW_RELEASE=/opt/myownclone/releases/$(date +%Y%m%d%H%M%S)-mi-deploy
ssh root@212.227.169.99 "mkdir -p $NEW_RELEASE"

# 2. Empaquetar código (en PC local)
cd C:/Users/haxth3/Documents/MyOwnClone-vps-fixes
tar -czf /tmp/deploy.tar.gz --exclude='api/.venv' --exclude='**/__pycache__' \
  --exclude='ops/backend.env.production' api/ ops/ .dockerignore

# 3. Subir
scp /tmp/deploy.tar.gz root@212.227.169.99:$NEW_RELEASE/

# 4. Extraer, swap symlink, restart
ssh root@212.227.169.99 "
  cd $NEW_RELEASE
  tar -xzf deploy.tar.gz
  rm deploy.tar.gz
  ln -sfn $NEW_RELEASE /opt/myownclone/current
  cd /opt/myownclone/current/ops
  cp /opt/myownclone/shared/backend.env.production ./backend.env.production
  set -a; . ./backend.env.production; set +a
  docker compose -f docker-compose.backend.prod.yml up -d --build
"
```

## 5. Rollback

```bash
# 1. Ver releases anteriores
ls /opt/myownclone/releases/

# 2. Identificar el release bueno anterior
PREV=/opt/myownclone/releases/20260629144355-frontend-i18n-selector

# 3. Rollback
ssh root@212.227.169.99 "
  ln -sfn $PREV /opt/myownclone/current
  systemctl restart myownclone-frontend
  cd /opt/myownclone/current/ops
  cp /opt/myownclone/shared/backend.env.production ./backend.env.production
  set -a; . ./backend.env.production; set +a
  docker compose -f docker-compose.backend.prod.yml up -d --build
"

# 4. Verificar
curl -s https://myownclone.com | head -3
```

## 6. Backups

```bash
# Backup manual
ssh root@212.227.169.99 "/opt/myownclone/current/ops/backup_postgres.sh 7"

# Ver backups existentes
ls -la /opt/myownclone/backups/

# Restaurar un backup
LATEST=$(ls -t /opt/myownclone/backups/myownclone_*.sql.gz | head -1)
gunzip -c $LATEST | docker exec -i myownclone_postgres psql -U postgres -d myownclone

# ⚠️ Esto sobreescribe la DB actual. Hazlo solo si sabes lo que haces.
```

## 7. Base de datos

```bash
# Conectar a Postgres
docker exec -it myownclone_postgres psql -U postgres -d myownclone

# Comandos SQL útiles
\dt                              # listar tablas
\d chunks                        # describir tabla
SELECT pg_size_pretty(pg_database_size('myownclone'));  # tamaño DB
SELECT * FROM alembic_version;   # versión migración
SELECT * FROM ai_models;         # catálogo IA
SELECT * FROM ai_model_assignments;  # qué modelo para qué tarea
```

## 8. Troubleshooting

### Frontend caído
```bash
systemctl status myownclone-frontend
journalctl -u myownclone-frontend -n 50 --no-pager
systemctl restart myownclone-frontend
```

### Backend caído
```bash
docker logs myownclone_api --tail 50
docker ps  # ¿está corriendo?
cd /opt/myownclone/current/ops
docker compose -f docker-compose.backend.prod.yml up -d --build api
```

### DB caída
```bash
docker logs myownclone_postgres --tail 50
docker restart myownclone_postgres
# Esperar 30s a que arranque
docker ps  # verificar healthy
```

### Redis caído
```bash
docker restart myownclone_redis
```

### Ollama caído (embeddings fallan)
```bash
docker logs myownclone_ollama --tail 50
docker restart myownclone_ollama
# Esperar 30s a que cargue el modelo
docker exec myownclone_ollama ollama list
```

### Nginx caído
```bash
systemctl status nginx
nginx -t  # validar config
systemctl restart nginx
```

### Disco lleno
```bash
# ¿Qué ocupa?
df -h /var/lib/docker
du -sh /opt/myownclone/* | sort -h

# Limpiar Docker (T1.7)
docker image prune -f
docker builder prune -f --keep-storage 500m

# Limpiar logs
docker logs myownclone_api 2>&1 | tail -100  # ver tamaño
journalctl --vacuum-time=7d
```

### Healthcheck degradado
```bash
curl -s http://127.0.0.1:5001/healthz | python3 -m json.tool
# Ver qué componente falla (database, redis, ollama)
```

## 9. Variables de entorno importantes

| Variable | Valor | Propósito |
|---|---|---|
| `DATABASE_URL` | postgresql+psycopg://... | Conexión Postgres |
| `REDIS_URL` | rediss://redis:6380 | Conexión Redis (TLS) |
| `WEAVIATE_URL` | http://weaviate:8080 | Conexión Weaviate |
| `OLLAMA_BASE_URL` | http://ollama:11434 | Conexión Ollama (embeddings locales) |
| `OPENAI_API_KEY` | (cifrado en ai_models.api_key_encrypted) | Fallback LLM |
| `MINIMAX_MODEL` | minimax-m2.7 | LLM primario |
| `LOCAL_WHISPER_MODEL` | base | STT local |
| `ALLOWED_ORIGINS` | http://212.227.169.99,https://myownclone.com | CORS |
| `FLASK_ENV` | production | Flask modo |

## 10. Catálogo IA

```sql
-- Ver modelos disponibles
SELECT name, provider, model_id, is_active, embedding_dimensions
FROM ai_models ORDER BY provider;

-- Ver asignaciones (qué tarea usa qué modelo)
SELECT t.task, m.name, t.priority
FROM ai_model_assignments t
JOIN ai_models m ON t.model_id = m.id
ORDER BY t.priority DESC;
```

## 11. Decisión sobre Weaviate

**Estado actual**: Weaviate está corriendo (1.24.0) pero **prácticamente sin uso** (115 KB de datos). El sistema usa pgvector embebido en Postgres para embeddings.

**Decisión pendiente** (FASE 1 T1.3): eliminar Weaviate para reducir recursos.

## 12. Respaldo de seguridad

| Componente | Frecuencia | Ubicación | Retention |
|---|---|---|---|
| `pg_dump` | Diario 03:00 UTC | `/opt/myownclone/backups/` | 7 días |
| Off-site | **Pendiente** (T1.1) | S3/B2 | Por configurar |
| Docker volumes | Automático | `/var/lib/docker/volumes/` | Persistente |

## 13. Contactos y propietarios

- **Operaciones**: usuario root del VPS
- **Ramas git activas**:
  - `master`: docs/planes + compendio OSINT
  - `codex/backend-admin-vps-exec`: rama deploy (f0418c0)
  - `sisyphus/anti-forget-layer`: rama paralela (incompatible con DB actual)
  - `vps-fixes`: rama alternativa (también incompatible con DB actual)

---

*Documento vivo. Actualizar cuando cambien releases, env vars, o procedimientos.*