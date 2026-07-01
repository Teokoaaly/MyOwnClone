# Plan de Implementación — Endurecimiento del VPS MyOwnClone

**Fecha**: 2026-07-01
**Alcance**: Ejecución de las mejoras identificadas en la auditoría
`vps-implementation-audit-2026-06-30.md`, por partes, con comandos
exactos y verificación tras cada paso.
**Entorno**: VPS en producción (`myownclone-vps` vía Tailscale SSH).
**Objetivo**: TODO debe quedar perfecto, verificado y sin errores.

---

## Estado inicial verificado (2026-07-01)

| Métrica | Valor |
|---|---|
| Disco | 33G / 116G usados (28%) |
| RAM | 1.2G / 3.8G |
| Imágenes Docker API | 9 (7 obsoletas + latest + v1.5.1) |
| Imagen activa | `ops-api:latest` (1.41GB, sin pin) |
| Build cache | ~3GB reclaimable |
| Ollama models | `mxbai-embed-large` (activo), `embeddinggemma` (sin uso, 621MB) |
| Nginx | sin rate limiting, headers duplicados via `/etc/nginx/...` |
| Backups | diarios 03:00 UTC, retención 7 días, sólo local |
| Monitoring | ninguno |
| Cron | sólo backup |

---

# PARTE 1 — Limpieza de imágenes Docker y espacio en disco
**Objetivo**: liberar ~6GB de imágenes obsoletas + 3GB build cache.
**Riesgo**: bajo (no afecta contenedores en ejecución).
**Rollback**: no aplica (las imágenes viejas no se usan).

### Paso 1.1 — Identificar imágenes usadas por contenedores activos
```bash
ssh myownclone-vps 'docker ps --format "{{.Image}}" | sort -u'
```
**Esperado**:
- `cr.weaviate.io/.../weaviate:1.24.0`
- `myownclone_api:latest` o `ops-api:latest` ← verificar tag real
- `ollama/ollama:latest`
- `pgvector/pgvector:pg15`
- `redis:7-alpine`

### Paso 1.2 — Eliminar imágenes API con tag v1.0.0–v1.5.0 (7 imágenes)
Estas son rollbacks ya no necesarios (el costs-fix y los i18n-wip ya
están merged en master). Conservamos `v1.5.1-i18n-final` y `latest`
como puntos de recuperación.

```bash
ssh myownclone-vps 'docker rmi \
  myownclone_api:v1.0.0-costs-fix \
  myownclone_api:fix-persisted \
  myownclone_api:v1.1.0-maint-mode-wip \
  myownclone_api:v1.2.0-i18n-wip \
  myownclone_api:v1.3.0-i18n-fixed \
  myownclone_api:v1.4.0-i18n-corrected \
  myownclone_api:v1.5.0-i18n-xlocale 2>&1 | tail -10'
```
**Esperado**: `Untagged` + `Deleted` por cada una (~5.4GB liberados).
**Si falla** (`image is being reused`): añadir `-f` sólo si el ID
coincide con `v1.5.1` o `latest`. Verificar antes con `docker images -q`.

### Paso 1.3 — Limpiar build cache
```bash
ssh myownclone-vps 'docker builder prune --all --force 2>&1 | tail -3'
```
**Esperado**: `Total reclaimed space: ~3GB`.

### Paso 1.4 — Limpiar dangling images y containers viejos
```bash
ssh myownclone-vps 'docker image prune -f 2>&1 | tail -3'
```

### Paso 1.5 — Verificación
```bash
ssh myownclone-vps 'df -h / | tail -1 && docker images --format "{{.Repository}}:{{.Tag}}\t{{.Size}}" | grep -iE "api"'
```
**Criterio de éxito**:
- Disco baja de 33G → ~27G
- Sólo quedan: `ops-api:latest`, `myownclone_api:v1.5.1-i18n-final`

---

# PARTE 2 — Pin de la imagen API activa
**Objetivo**: tag reproducible para rollback.
**Riesgo**: ninguno (sólo crea un nuevo tag).

### Paso 2.1 — Descubrir el image ID activo
```bash
ssh myownclone-vps 'docker inspect myownclone_api --format "{{.Image}}"'
```

### Paso 2.2 — Taggear con fecha + sha corta
```bash
sha=$(ssh myownclone-vps 'cd /opt/myownclone/worktrees/sisyphus-vps-integration && git rev-parse --short HEAD')
ssh myownclone-vps "docker tag ops-api:latest ops-api:v2026.07.01-${sha}"
```

### Paso 2.3 — Verificar
```bash
ssh myownclone-vps 'docker images | grep ops-api'
```
**Criterio de éxito**: aparece `ops-api:v2026.07.01-<sha>` con mismo ID.

### Paso 2.4 — Documentar en release
Añadir al archivo `.omo/evidence/vps-image-pin-2026-07-01.md`:
```
ops-api:v2026.07.01-<sha> = <image-id>
deploy branch: deploy/maint-mode-plus-wip @ <sha>
release dir: /opt/myownclone/releases/20260629144355-frontend-i18n-selector
```

---

# PARTE 3 — Rate limiting en nginx
**Objetivo**: proteger `/login` y `/api/auth/*` de fuerza bruta.
**Riesgo**: medio — mal configurado bloquea usuarios legítimos.
**Rollback**: restaurar backup de nginx config.

### Paso 3.1 — Backup de config nginx
```bash
ssh myownclone-vps 'cp /etc/nginx/sites-available/myownclone /etc/nginx/sites-available/myownclone.bak-20260701'
```

### Paso 3.2 — Añadir `limit_req_zone` en `http {}` block
Editar `/etc/nginx/nginx.conf`, dentro del bloque `http { ... }`,
antes de cualquier `server {`:
```nginx
limit_req_zone $binary_remote_addr zone=login_zone:10m rate=5r/m;
limit_req_zone $binary_remote_addr zone=api_zone:10m rate=30r/s;
```

### Paso 3.3 — Aplicar zones en los locations
Editar `/etc/nginx/sites-available/myownclone`:

- En `location = /login` (o el bloque que sirva `/login`):
  ```nginx
  location /login {
      limit_req zone=login_zone burst=10 nodelay;
      proxy_pass http://127.0.0.1:3000;
      # ... headers existentes ...
  }
  ```
  Si `/login` es servido por Next sin location específico, añadir
  dentro de `location /`:
  ```nginx
  if ($request_uri ~* "^/login") {
      set $do_limit 1;
  }
  limit_req zone=login_zone burst=10 nodelay;
  ```
  **Preferir location específico** antes de `if`.

- En el bloque que hace proxy al backend (`location /api/`):
  ```nginx
  location /api/ {
      limit_req zone=api_zone burst=60 nodelay;
      proxy_pass http://127.0.0.1:5001;
      # ... headers existentes ...
  }
  ```

### Paso 3.4 — Test de sintaxis
```bash
ssh myownclone-vps 'nginx -t'
```
**Esperado**: `syntax is ok` + `test is successful`.

### Paso 3.5 — Reload
```bash
ssh myownclone-vps 'systemctl reload nginx'
```

### Paso 3.6 — Verificación funcional
```bash
# Test rate limit: hacer 20 requests rápididas a /login
ssh myownclone-vps 'for i in $(seq 1 20); do
  curl -s -o /dev/null -w "%{http_code} " -k https://localhost/login
done; echo'
```
**Esperado**: primeros requests 200/301, luego 429 Too Many Requests.
**Si bloquea todo (incluyendo el primer request)**: restaurar backup
```bash
ssh myownclone-vps 'cp /etc/nginx/sites-available/myownclone.bak-20260701 /etc/nginx/sites-available/myownclone && systemctl reload nginx'
```

---

# PARTE 4 — Eliminar headers duplicados en nginx
**Objetivo**: quitar el duplicado HSTS y X-Frame-Options.
**Riesgo**: bajo.
**Rollback**: restaurar backup.

### Paso 4.1 — Verificar duplicación
```bash
ssh myownclone-vps 'curl -sI -k https://localhost/ | grep -iE "strict-transport|x-frame"'
```
**Actual**: aparecen 2 veces cada uno.

### Paso 4.2 — Consolidar headers en un solo lugar
Los headers están tanto en `/etc/nginx/sites-available/myownclone`
como en `/etc/nginx/snippets/` o en `nginx.conf` defaults. Elegir:
- **Mantener**: el bloque `add_header` en
  `/etc/nginx/sites-available/myownclone` (líneas 37-41)
- **Quitar**: cualquier `add_header` duplicado en `nginx.conf` http block

### Paso 4.3 — Verificar
```bash
ssh myownclone-vps 'nginx -t && systemctl reload nginx && curl -sI -k https://localhost/ | grep -ciE "strict-transport|x-frame"'
```
**Esperado**: cada header aparece exactamente 1 vez (count = 1 por header).

---

# PARTE 5 — Backups off-server
**Objetivo**: copia cifrada diaria a almacenamiento remoto.
**Riesgo**: ninguno (sólo añade uploads).
**Requisito**: credencial de destino (S3/B2). **Pendiente del usuario**.

### Paso 5.1 — Instalar rclone
```bash
ssh myownclone-vps 'apt-get update && apt-get install -y rclone'
```

### Paso 5.2 — Configurar remote (requiere credencial)
```bash
ssh myownclone-vps 'rclone config create myownclone-backup s3 \
  provider=<provider> \
  access_key_id=<ACCESS_KEY> \
  secret_access_key=<SECRET_KEY> \
  region=<region> \
  endpoint=<endpoint>'
```
**🛑 BLOQUEANTE**: necesito que el usuario provea credenciales de S3/B2
o autorice crearlas. Sin esto, esta parte se pospone.

### Paso 5.3 — Script de sync cifrado
Crear `/opt/myownclone/current/ops/backup_offsite.sh`:
```bash
#!/usr/bin/env bash
set -euo pipefail
BACKUP_DIR="/opt/myownclone/backups"
REMOTE="myownclone-backup:myownclone-backups/$(date +%Y/%m)"

# Subir backups del día
rclone copy "$BACKUP_DIR" "$REMOTE" \
  --include "*.sql.gz" \
  --max-age 24h \
  --transfers 2 \
  --checkers 2 \
  --log-file /var/log/myownclone-offsite.log

# Cifrar con age si está disponible (opcional)
# age -r <recipient> "$FILE" > "$FILE.age"

echo "[$(date -Iseconds)] Offsite backup done"
```

### Paso 5.4 — Cron
```bash
# Backup offsite 30 min después del backup local
ssh myownclone-vps 'crontab -l | { cat; echo "30 3 * * * /opt/myownclone/current/ops/backup_offsite.sh >> /var/log/myownclone-offsite.log 2>&1"; } | crontab -'
```

### Paso 5.5 — Verificación
```bash
ssh myownclone-vps 'rclone ls myownclone-backup:myownclone-backups/ | tail -5'
```

---

# PARTE 6 — Quitar `embeddinggemma` de Ollama
**Objetivo**: liberar 621MB.
**Riesgo**: ninguno (no se usa).

### Paso 6.1 — Confirmar que no está en uso
```bash
ssh myownclone-vps 'docker exec myownclone_api python -c "
from api.core.model_registry import ModelRegistry
from api.models.ai_models import AITask
r = ModelRegistry().get_model_for_task(tenant_id=None, task=AITask.EMBEDDING)
print(r.provider, r.model_id)
"'
```
**Esperado**: `local mxbai-embed-large` (NO embeddinggemma).

### Paso 6.2 — Eliminar modelo
```bash
ssh myownclone-vps 'docker exec myownclone_ollama ollama rm embeddinggemma:latest'
```

### Paso 6.3 — Verificación
```bash
ssh myownclone-vps 'docker exec myownclone_ollama ollama list'
ssh myownclone-vps 'docker exec myownclone_api python -c "
from api.core.model_registry import ModelRegistry
from api.models.ai_models import AITask
r = ModelRegistry().get_model_for_task(tenant_id=None, task=AITask.EMBEDDING)
print(\"embedding OK:\", r.provider, r.model_id)
"'
```
**Criterio de éxito**:
- `ollama list` sólo muestra `mxbai-embed-large`
- El endpoint de embedding sigue funcionando

---

# PARTE 7 — Monitoring mínimo (node_exporter)
**Objetivo**: exponer métricas de host para Prometheus.
**Riesgo**: bajo.
**Rollback**: `systemctl stop node_exporter`.

### Paso 7.1 — Instalar
```bash
ssh myownclone-vps 'apt-get install -y prometheus-node-exporter'
```

### Paso 7.2 — Configurar bind a localhost sólo
Editar `/etc/default/prometheus-node-exporter`:
```
ARGS="--web.listen-address=127.0.0.1:9100"
```

### Paso 7.3 — Iniciar
```bash
ssh myownclone-vps 'systemctl enable --now prometheus-node-exporter && systemctl status prometheus-node-exporter --no-pager | head -10'
```

### Paso 7.4 — Verificar
```bash
ssh myownclone-vps 'curl -s http://127.0.0.1:9100/metrics | grep -E "^node_load|^node_memory_MemAvailable" | head -5'
```
**Criterio de éxito**: métricas aparecen en `127.0.0.1:9100`.

### Paso 7.5 — (Opcional) Conectar a Grafana Cloud
Requiere URL + API key del usuario. Sin esto, las métricas quedan
locales y scrapeables desde dentro del host.

---

# PARTE 8 — Actualización de dependencias Python
**Objetivo**: bump de paquetes con CVEs o versiones mayores.
**Riesgo**: medio — requiere tests.
**Rollback**: rebuild desde imagen anterior.

### Paso 8.1 — En release staging, crear requirements.actualizado
Localmente:
```bash
pip install --upgrade pip setuptools wheel
pip install --upgrade "protobuf>=6.30,<8" "grpcio>=1.78" "pydantic>=2.46"
```

### Paso 8.2 — Actualizar `api/requirements.txt`
- `setuptools>=82.0.0`
- `protobuf>=6.30,<8` (verificar breaking de grpc)
- `grpcio>=1.78.0`
- `pydantic>=2.46.0`

### Paso 8.3 — Rebuild + tests
```bash
cd /c/Users/haxth3/Documents/MyOwnClone-admin-vps-exec
python -m pytest api/tests/ -q
```
**Criterio de éxito**: 41/41 tests pasan (o todos los que pasaban antes).

### Paso 8.4 — Deploy a VPS (release dedicado)
Rebuild imagen, restart container, validar `/readyz`.

---

# PARTE 9 — STT model upgrade (tiny → base)
**Objetivo**: mejorar precisión de transcripción.
**Riesgo**: medio — +150MB RAM, +1s CPU por request.
**Rollback**: `LOCAL_WHISPER_MODEL=tiny` en env.

### Paso 9.1 — Verificar memoria disponible
```bash
ssh myownclone-vps 'free -h | head -2'
```
**Requisito**: ≥500MB libres (actual: 2.5G ✅).

### Paso 9.2 — Cambiar env
Añadir a `/opt/myownclone/shared/backend.env.production`:
```
LOCAL_WHISPER_MODEL=base
```

### Paso 9.3 — Restart backend con env cargado
```bash
ssh myownclone-vps 'cd /opt/myownclone/releases/20260629144355-frontend-i18n-selector && \
  set -a && . ops/backend.env.production && set +a && \
  docker compose -f ops/docker-compose.backend.prod.yml up -d --no-deps api'
```

### Paso 9.4 — Validar E2E
```bash
ssh myownclone-vps 'docker exec myownclone_api python -c "
import time
from api.core.providers.local_whisper import LocalWhisperAdapter
from api.core.model_registry import ResolvedModelConfig
from api.models.ai_models import AITask
cfg = ResolvedModelConfig(task=AITask.STT, provider=\"local_whisper\", model_id=\"base\", tenant_id=None, source=\"test\", api_key=None, base_url=None)
a = LocalWhisperAdapter(cfg)
t0 = time.monotonic(); a._ensure_model()
print(f\"cold load: {time.monotonic()-t0:.1f}s\")
with open(\"/tmp/hola16.wav\",\"rb\") as f: audio = f.read()
t0 = time.monotonic()
out = a.transcribe(audio_bytes=audio, filename=\"hola16.wav\", language=\"es\")
print(f\"transcribe: {time.monotonic()-t0:.2f}s -> {out!r}\")
"'
```
**Esperado**: precisión mejorada (cerca de la frase original).

---

# PARTE 10 — Documentación de restore
**Objetivo**: runbook claro para recuperación desde backup.
**Riesgo**: ninguno (sólo docs).

Crear `.omo/runbooks/restore-from-backup.md`:
- Cómo restaurar PostgreSQL desde `.sql.gz`
- Cómo reconstruir Weaviate desde chunks
- Cómo re-pull modelos Ollama
- Cómo reconstruir imagen API desde release
- Tiempos estimados por paso

---

# Orden de ejecución recomendado

| Fase | Partes | Tiempo est. | Requiere usuario |
|---|---|---|---|
| A — Limpieza | 1, 2, 6 | 15 min | No |
| B — Seguridad nginx | 3, 4 | 30 min | No |
| C — Backups | 5 | 20 min | **Sí** (credencial S3/B2) |
| D — Monitoring | 7 | 15 min | No (Grafana Cloud opcional) |
| E — Deps + STT | 8, 9 | 45 min | No |
| F — Docs | 10 | 15 min | No |

**Recomendación**: ejecutar Fases A → B → D → F primero (sin
dependencias externas). La Fase C requiere que el usuario provea
credenciales de almacenamiento remoto. La Fase E requiere tests
regresivos completos.

---

## Checkpoints de validación global

Tras cada fase, ejecutar:
```bash
ssh myownclone-vps '
  echo "=== HEALTH ===" &&
  curl -s http://127.0.0.1:5001/readyz && echo "" &&
  echo "=== DISK ===" && df -h / | tail -1 &&
  echo "=== MEMORY ===" && free -h | head -2 &&
  echo "=== CONTAINERS ===" && docker ps --format "{{.Names}}: {{.Status}}" &&
  echo "=== FRONTEND ===" && curl -s -o /dev/null -w "http=%{http_code}\n" -k https://localhost/
'
```
**Criterio de éxito global**:
- `/readyz` → status=ready
- Frontend → 200
- Todos los containers → Up (healthy)
- Disco ≤ 28%
- RAM ≤ 50%

---

## Registro de evidencia por fase

Cada fase debe generar:
- `.omo/evidence/vps-<fase>-YYYY-MM-DD.md` con:
  - Comandos ejecutados
  - Output real
  - Antes/después (mediciones)
  - Problemas encontrados y resolución
  - SHA del estado final del repo

---

## Reglas de oro durante la ejecución

1. **Un cambio a la vez** — nunca mezclar fases
2. **Verificar antes de continuar** — si algo falla, parar
3. **Backup antes de tocar nginx** — siempre
4. **No `docker system prune -a`** — borrar imágenes listadas explícitamente
5. **Documentar todo** — cada comando, cada output
6. **Si el usuario no responde** (Fase C) — saltar y seguir con la siguiente
7. **No reiniciar el backend sin `set -a && . env`** — sin env vars se cae