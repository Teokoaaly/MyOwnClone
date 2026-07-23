# Runbook: Restaurar MyOwnClone desde backup

Documento de recuperación de desastre. Úsalo en caso de pérdida de
datos, restauración a un punto en el tiempo, o migración a otro host.

## 0. Estado esperado antes de empezar

- SSH al VPS con permisos sudo
- Docker funcionando
- `~/.ssh/config` con `myownclone-vps`
- Credenciales de admin en mano

## 1. Restaurar PostgreSQL desde `.sql.gz`

```bash
# 1. Localiza el backup más reciente
ls -t /opt/myownclone/backups/*.sql.gz | head -3

# 2. Verifica checksum, manifest, gzip y restore aislado (debe terminar PASS)
/opt/myownclone/backend-current/ops/verify_postgres_backup.sh \
  /opt/myownclone/backups/myownclone_YYYYMMDD_HHMMSS.sql.gz

# 3. Restaurar (reemplaza DB actual; detener antes los writers de la aplicación)
zcat /opt/myownclone/backups/myownclone_YYYYMMDD_HHMMSS.sql.gz | \
  docker exec -i myownclone_postgres psql -U postgres -d myownclone

# 4. Verifica
docker exec myownclone_postgres psql -U postgres -d myownclone -c "SELECT COUNT(*) FROM accounts;"
```

**Tiempo estimado**: 2-5 min (DB pequeña, ~10MB).

## 1.1 Programación, retención y copia B2

El backup se ejecuta desde la release resuelta por
`/opt/myownclone/backend-current`; no usar un path de release antiguo ni un
cron paralelo. La unidad `myownclone-postgres-backup.timer` corre diariamente,
incluye retraso aleatorio y no pierde una ejecución tras una caída (`Persistent=true`).

La retención es únicamente local y conserva siempre el dump más reciente.
Si existe `/etc/myownclone/backup-b2.env`, el servicio root carga
`B2_REMOTE=remote:bucket/prefix` en runtime y sube el dump, checksum y manifest
con nombres inmutables. Ese archivo y cualquier configuración/credencial rclone
son root-only, nunca se versionan. El proceso no borra objetos remotos.

Instalación o migración, únicamente durante una ventana de mantenimiento:

```bash
install -m 0600 /dev/null /etc/myownclone/backup-b2.env
# editar como root: B2_REMOTE=remote:bucket/myownclone/postgres
/opt/myownclone/backend-current/ops/install-postgres-backup-systemd.sh
systemctl list-timers myownclone-postgres-backup.timer
systemctl start myownclone-postgres-backup.service
journalctl -u myownclone-postgres-backup.service -n 50 --no-pager
```

El instalador activa y comprueba el timer antes de eliminar sólo una línea cron
legacy que invoque `backup_postgres.sh`. Para rollback de la migración, deshabilitar
el timer antes de restaurar explícitamente el cron aprobado; no ejecutar ambos.

## 2. Reconstruir Weaviate

Los embeddings vectoriales están en dos lugares:
- **PostgreSQL** (tabla `chunks`, con `vector` pgvector): la verdad
- **Weaviate**: cache para búsqueda semántica rápida

Si Weaviate está vacío, rehidratarlo:

```bash
# 1. Comprueba si Weaviate tiene datos
curl -s http://127.0.0.1:8080/v1/objects?limit=1 | jq '.objects | length'

# 2. Si devuelve 0, rehidratar desde PostgreSQL
docker exec myownclone_api python -m api.scripts.reindex_weaviate
```

**Tiempo estimado**: 10-30 min (depende del número de chunks).

## 3. Re-pull modelos Ollama

```bash
# 3.1. Comprueba qué modelos están activos
docker exec myownclone_api python -c "
from api.core.model_registry import ModelRegistry
from api.models.ai_models import AITask
for task in [AITask.EMBEDDING, AITask.STT]:
    r = ModelRegistry().get_model_for_task(tenant_id=None, task=task)
    print(task.value, r.provider, r.model_id)
"

# 3.2. Reconstruye la imagen Docker (incluye faster-whisper)
cd /opt/myownclone/current
docker compose -f ops/docker-compose.backend.prod.yml build api

# 3.3. Pull de los modelos (ejemplo para mxbai-embed-large)
docker exec myownclone_ollama ollama pull mxbai-embed-large:latest
```

**Tiempo estimado**: 5-10 min (descarga 669MB por modelo + build de imagen).

## 4. Reconstruir imagen API

Si la imagen `ops-api` se perdió o está corrupta:

```bash
cd /opt/myownclone/current
docker compose -f ops/docker-compose.backend.prod.yml build api

# Verificar SHA de la imagen
docker images | grep ops-api
```

**Tiempo estimado**: 5-10 min.

## 5. Reiniciar todos los servicios

```bash
cd /opt/myownclone/current
set -a && . ops/backend.env.production && set +a
docker compose -f ops/docker-compose.backend.prod.yml up -d
systemctl restart myownclone-frontend
systemctl reload nginx
```

## 6. Verificación post-restore

```bash
# Backend
curl -s http://127.0.0.1:5001/readyz

# Frontend
curl -s -o /dev/null -w "http=%{http_code}\n" -k https://localhost/

# Containers
docker ps --format "{{.Names}}: {{.Status}}"

# Node exporter
curl -s http://127.0.0.1:9100/metrics | grep -c "^node_"
```

**Criterios de éxito**:
- `/readyz` → `"status":"ready"`
- Frontend → `http=200`
- Todos los containers → `Up`
- node_exporter → métricas disponibles

## 7. Tiempos totales estimados

| Paso | Tiempo |
|---|---|
| 1. PostgreSQL restore | 2-5 min |
| 2. Weaviate reindex | 10-30 min |
| 3. Ollama pull + API build | 10-20 min |
| 4. Image rebuild | 5-10 min |
| 5. Restart services | 1 min |
| 6. Verificación | 1 min |
| **TOTAL** | **29-67 min** |

## 8. Si todo falla: recovery desde cero

1. **Crear nuevo VPS** (mismo tamaño, mismo OS Ubuntu 24.04)
2. **Instalar docker, docker compose, nginx, certbot**
3. **Restaurar backup de `/opt/myownclone/releases/20260629144355-frontend-i18n-selector`** desde git:
   ```bash
   git clone git@github.com:Teokoaaly/MyOwnClone.git /opt/myownclone/source
   cd /opt/myownclone/source
   git checkout deploy/maint-mode-plus-wip
   ```
4. **Copiar backups** desde offsite (S3/B2) — requiere configuración rclone previa
5. **Reconstruir `.env` files** con las claves secretas (gestionadas fuera del repo)
6. **Seguir pasos 1-6** de este runbook

## 9. Referencias

- Auditoría: `.omo/audits/vps-implementation-audit-2026-06-30.md`
- Plan hardening: `.omo/plans/vps-hardening-implementation-plan-2026-07-01.md`
- Task list: `.omo/plans/vps-hardening-tasklist-2026-07-01.md`
- Logs de ejecución: `.omo/evidence/vps-hardening-execution-log-2026-07-01.md`
