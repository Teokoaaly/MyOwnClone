# Runbook VPS — MyOwnClone Producción

> **Última actualización**: 2026-07-07
> **Servidor**: VPS de producción
> **Dominio**: myownclone.com

---

## 1. Acceso

```bash
# Conexión SSH (Tailscale)
ssh myownclone@100.125.128.116

# Conexión SSH (directa - si disponible)
ssh -i ~/.ssh/myownclone_vps_ed25519 root@212.227.169.99
```

## 2. Servicios

| Servicio | Comando status | Comando restart |
|---|---|---|
| **Frontend** (Next.js) | `systemctl status myownclone-frontend` | `sudo systemctl restart myownclone-frontend` |
| **Backend API** (Docker) | `sudo docker ps` | `cd /opt/myownclone/current/ops && sudo docker compose -f docker-compose.backend.prod.yml up -d --build api` |
| **Worker RQ** (Docker) | `sudo docker ps` | `cd /opt/myownclone/current/ops && sudo docker compose -f docker-compose.backend.prod.yml up -d --build api_worker` |
| **PostgreSQL** | `sudo docker ps` | `sudo docker restart myownclone_postgres` |
| **Redis** (TLS) | `sudo docker ps` | `sudo docker restart myownclone_redis` |
| **Ollama** | `sudo docker ps` | `sudo docker restart myownclone_ollama` |
| **Nginx** | `systemctl status nginx` | `sudo systemctl restart nginx` |

## 3. Layout del VPS

```
/opt/myownclone/
├── current → /opt/myownclone/releases/<release-id>   # symlink activo
├── releases/
│   └── <release-id>                                   # código desplegado
├── shared/
│   ├── backend.env.production                         # secrets del backend
│   ├── frontend.env.production                        # secrets del frontend
│   └── redis-tls/                                     # certs TLS para Redis
│       ├── ca.crt
│       ├── redis.crt
│       └── redis.key
├── backups/                                            # pg_dump diarios (cron 03:00 UTC)
└── bootstrap/                                          # repo git clonado
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

# Métricas Prometheus
curl -s http://127.0.0.1:5001/metrics

# Logs del backend en vivo
sudo docker logs -f myownclone_api

# Logs del worker en vivo
sudo docker logs -f myownclone_worker

# Logs del frontend en vivo
sudo journalctl -u myownclone-frontend -f
```

### Ver qué release está activo
```bash
readlink /opt/myownclone/current
ls -la /opt/myownclone/current/
```

### Deploy manual (sin script)
```bash
# 1. Crear release dir
NEW_RELEASE=/opt/myownclone/releases/$(date +%Y%m%d%H%M%S)-mi-deploy
sudo mkdir -p $NEW_RELEASE

# 2. Empaquetar código (en PC local)
cd C:/Users/haxth3/Documents/MyOwnClone-admin-vps-exec
tar -czf /tmp/deploy.tar.gz --exclude='api/.venv' --exclude='**/__pycache__' \
  --exclude='ops/backend.env.production' api/ ops/ .dockerignore

# 3. Subir
scp /tmp/deploy.tar.gz myownclone@100.125.128.116:$NEW_RELEASE/

# 4. Extraer, swap symlink, restart
ssh myownclone@100.125.128.116 "
  cd $NEW_RELEASE
  tar -xzf deploy.tar.gz
  rm deploy.tar.gz
  sudo ln -sfn $NEW_RELEASE /opt/myownclone/current
  cd /opt/myownclone/current/ops
  sudo cp /opt/myownclone/shared/backend.env.production ./backend.env.production
  sudo chown myownclone:myownclone ./backend.env.production
  set -a; . ./backend.env.production; set +a
  sudo docker compose -f docker-compose.backend.prod.yml up -d --build
"
```

## 5. Rollback

```bash
# 1. Ver releases anteriores
ls /opt/myownclone/releases/

# 2. Identificar el release bueno anterior
PREV=/opt/myownclone/releases/20260703190910-landing-cleanup-restore

# 3. Rollback
sudo ln -sfn $PREV /opt/myownclone/current
sudo systemctl restart myownclone-frontend
cd /opt/myownclone/current/ops
sudo cp /opt/myownclone/shared/backend.env.production ./backend.env.production
sudo chown myownclone:myownclone ./backend.env.production
set -a; . ./backend.env.production; set +a
sudo docker compose -f docker-compose.backend.prod.yml up -d --build

# 4. Verificar
curl -s https://myownclone.com | head -3
```

## 6. Backups

```bash
# Backup manual
sudo /opt/myownclone/current/ops/backup_postgres.sh 7

# Backup dual (local + secundario)
sudo /opt/myownclone/current/ops/backup_dual.sh

# Ver backups existentes
ls -la /opt/myownclone/backups/

# Restaurar un backup
LATEST=$(ls -t /opt/myownclone/backups/myownclone_*.sql.gz | head -1)
gunzip -c $LATEST | sudo docker exec -i myownclone_postgres psql -U postgres -d myownclone

# ⚠️ Esto sobreescribe la DB actual. Hazlo solo si sabes lo que haces.
```

## 7. Base de datos

```bash
# Conectar a Postgres
sudo docker exec -it myownclone_postgres psql -U postgres -d myownclone

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
sudo systemctl restart myownclone-frontend
```

### Backend caído
```bash
sudo docker logs myownclone_api --tail 50
sudo docker ps  # ¿está corriendo?
cd /opt/myownclone/current/ops
sudo docker compose -f docker-compose.backend.prod.yml up -d --build api
```

### Worker caído
```bash
sudo docker logs myownclone_worker --tail 50
sudo docker ps  # ¿está corriendo?
cd /opt/myownclone/current/ops
sudo docker compose -f docker-compose.backend.prod.yml up -d --build api_worker
```

### DB caída
```bash
sudo docker logs myownclone_postgres --tail 50
sudo docker restart myownclone_postgres
# Esperar 30s a que arranque
sudo docker ps  # verificar healthy
```

### Redis caído
```bash
sudo docker restart myownclone_redis
```

### Ollama caído (embeddings fallan)
```bash
sudo docker logs myownclone_ollama --tail 50
sudo docker restart myownclone_ollama
# Esperar 30s a que cargue el modelo
sudo docker exec myownclone_ollama ollama list
```

### Nginx caído
```bash
systemctl status nginx
sudo nginx -t  # validar config
sudo systemctl restart nginx
```

### Disco lleno
```bash
# ¿Qué ocupa?
df -h /var/lib/docker
du -sh /opt/myownclone/* | sort -h

# Limpiar Docker
sudo docker image prune -f
sudo docker builder prune -f --keep-storage 500m

# Limpiar logs
sudo journalctl --vacuum-time=7d
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
| `REDIS_TLS` | true | Habilitar TLS en Redis |
| `OLLAMA_BASE_URL` | http://ollama:11434 | Conexión Ollama (embeddings locales) |
| `OPENAI_API_KEY` | (cifrado en ai_models.api_key_encrypted) | Fallback LLM |
| `MINIMAX_MODEL` | minimax-m2.7 | LLM primario |
| `LOCAL_WHISPER_MODEL` | base | STT local |
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

## 11. Respaldo de seguridad

| Componente | Frecuencia | Ubicación | Retention |
|---|---|---|---|
| `pg_dump` | Diario 03:00 UTC | `/opt/myownclone/backups/` | 7 días |
| Backup dual | Diario | `/var/backups/myownclone/` | 7 días |
| Docker volumes | Automático | `/var/lib/docker/volumes/` | Persistente |

## 12. Contactos y propietarios

- **Operaciones**: usuario myownclone del VPS (Tailscale)
- **Ramas git activas**:
  - `codex/backend-admin-vps-exec`: rama deploy principal
  - `master`: docs/planes

---

*Documento vivo. Actualizar cuando cambien releases, env vars, o procedimientos.*
