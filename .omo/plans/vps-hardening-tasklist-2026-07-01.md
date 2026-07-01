# Lista de Tareas — Endurecimiento del VPS MyOwnClone

**Agente ejecutor**: cualquiera con acceso SSH a `myownclone-vps`.
**Reglas**:
1. Ejecuta las tareas **EN ORDEN** (de la 1 a la N).
2. Tras cada tarea, ejecuta el bloque "VERIFICAR".
3. Si "VERIFICAR" falla, ejecuta el bloque "ROLLBACK" de esa tarea y
   **PÁRA**. No sigas a la siguiente tarea.
4. No inventes comandos. Si una tarea dice "ejecutar exactamente esto",
   ejecútalo literal.
5. Al final de cada tarea, anota el resultado en
   `.omo/evidence/vps-task-NN-YYYY-MM-DD.md` (un archivo por tarea).

**Conexión SSH**: `ssh myownclone-vps '<comando>'`
(El host `myownclone-vps` ya está configurado en `~/.ssh/config`.)

---

## TAREA 1 — Eliminar imágenes Docker API obsoletas

**Objetivo**: liberar ~5.4GB borrando 7 imágenes antiguas.

### EJECUTAR
```bash
ssh myownclone-vps 'docker rmi \
  myownclone_api:v1.0.0-costs-fix \
  myownclone_api:fix-persisted \
  myownclone_api:v1.1.0-maint-mode-wip \
  myownclone_api:v1.2.0-i18n-wip \
  myownclone_api:v1.3.0-i18n-fixed \
  myownclone_api:v1.4.0-i18n-corrected \
  myownclone_api:v1.5.0-i18n-xlocale 2>&1'
```

### SI FALLA con "image is being reused" o "is in use"
Significa que una imagen comparte capas con la activa. Ejecutar:
```bash
ssh myownclone-vps 'docker images -q | sort -u | wc -l'
```
Si el número baja, está bien. Si no baja nada, **PÁRA** y reporta.

### VERIFICAR
```bash
ssh myownclone-vps 'docker images --format "{{.Repository}}:{{.Tag}}" | grep -i "api" | sort'
```
**ÉXITO**: la salida contiene EXACTAMENTE estas 2 líneas:
```
myownclone_api:v1.5.1-i18n-final
<otra línea con ops-api o myownclone_api:latest>
```
Si aparecen más de 2 imágenes API, **PÁRA**.

### ROLLBACK (no aplica — las imágenes borradas ya estaban merged en master)

---

## TAREA 2 — Limpiar build cache de Docker

**Objetivo**: liberar ~3GB.

### EJECUTAR
```bash
ssh myownclone-vps 'docker builder prune --all --force 2>&1 | tail -3'
```

### VERIFICAR
```bash
ssh myownclone-vps 'docker system df 2>&1 | head -5'
```
**ÉXITO**: la fila "Build Cache" tiene `TOTAL: 0` o `SIZE` < 100MB.

### ROLLBACK (no aplica)

---

## TAREA 3 — Pin de la imagen API activa

**Objetivo**: crear un tag reproducible para rollback.

### PASO 3.1 — Obtener el SHA del código desplegado
```bash
ssh myownclone-vps 'cd /opt/myownclone/worktrees/sisyphus-vps-integration && git rev-parse --short HEAD'
```
**Anota el valor** (ej: `6984c6c`). Lo llamaremos `<SHA>`.

### PASO 3.2 — Crear el tag
Sustituye `<SHA>` por el valor del paso anterior:
```bash
ssh myownclone-vps 'docker tag ops-api:latest "ops-api:v2026.07.01-<SHA>"'
```

### VERIFICAR
```bash
ssh myownclone-vps 'docker images | grep ops-api'
```
**ÉXITO**: aparecen 2 filas:
- `ops-api:latest` con un Image ID
- `ops-api:v2026.07.01-<SHA>` con el MISMO Image ID

### ROLLBACK
```bash
ssh myownclone-vps 'docker rmi "ops-api:v2026.07.01-<SHA>"'
```

---

## TAREA 4 — Eliminar modelo `embeddinggemma` de Ollama

**Objetivo**: liberar 621MB de un modelo que no se usa.

### PASO 4.1 — Confirmar que NO es el modelo de embedding activo
```bash
ssh myownclone-vps 'docker exec myownclone_api python -c "
from api.core.model_registry import ModelRegistry
from api.models.ai_models import AITask
r = ModelRegistry().get_model_for_task(tenant_id=None, task=AITask.EMBEDDING)
print(r.provider, r.model_id)
"'
```
**ÉXITO**: imprime `local mxbai-embed-large` (NO `embeddinggemma`).
Si imprime `embeddinggemma`, **PÁSA** y reporta — no se puede borrar.

### PASO 4.2 — Borrar el modelo
```bash
ssh myownclone-vps 'docker exec myownclone_ollama ollama rm embeddinggemma:latest'
```

### VERIFICAR
```bash
ssh myownclone-vps 'docker exec myownclone_ollama ollama list'
ssh myownclone-vps 'docker exec myownclone_api python -c "
from api.core.model_registry import ModelRegistry
from api.models.ai_models import AITask
r = ModelRegistry().get_model_for_task(tenant_id=None, task=AITask.EMBEDDING)
print(\"embedding OK:\", r.provider, r.model_id)
"'
```
**ÉXITO**:
- `ollama list` muestra SOLO `mxbai-embed-large:latest`
- El segundo comando imprime `embedding OK: local mxbai-embed-large`

### ROLLBACK
```bash
ssh myownclone-vps 'docker exec myownclone_ollama ollama pull embeddinggemma:latest'
```

---

## TAREA 5 — Backup de config nginx

**Objetivo**: tener un punto de restauración antes de tocar nginx.

### EJECUTAR
```bash
ssh myownclone-vps 'cp /etc/nginx/sites-available/myownclone /etc/nginx/sites-available/myownclone.bak-20260701'
ssh myownclone-vps 'cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak-20260701'
```

### VERIFICAR
```bash
ssh myownclone-vps 'ls -la /etc/nginx/sites-available/myownclone.bak-20260701 /etc/nginx/nginx.conf.bak-20260701'
```
**ÉXITO**: ambos archivos existen y no están vacíos.

### ROLLBACK (no aplica — es un backup)

---

## TAREA 6 — Añadir rate limiting a nginx

**Objetivo**: proteger `/login` y `/api/` de fuerza bruta.

### PASO 6.1 — Añadir las zonas en `nginx.conf`
Editar `/etc/nginx/nginx.conf`. Buscar el bloque `http {` (empieza con
`http {` en una línea sola). Justo DESPUÉS de esa línea, añadir:
```nginx
    limit_req_zone $binary_remote_addr zone=login_zone:10m rate=5r/m;
    limit_req_zone $binary_remote_addr zone=api_zone:10m rate=30r/s;
```

Comando para hacerlo de forma segura (sed):
```bash
ssh myownclone-vps 'sed -i "/^http {/a\\    limit_req_zone \$binary_remote_addr zone=login_zone:10m rate=5r/m;\n    limit_req_zone \$binary_remote_addr zone=api_zone:10m rate=30r/s;" /etc/nginx/nginx.conf'
```

### PASO 6.2 — Aplicar la zona de login
En `/etc/nginx/sites-available/myownclone`, busca el bloque
`location / {` (el que hace `proxy_pass http://127.0.0.1:3000`).
Justo DESPUÉS de la línea `proxy_pass http://127.0.0.1:3000;`, añadir:
```nginx
            limit_req zone=login_zone burst=10 nodelay;
```

Comando sed (busca el proxy_pass a 3000 y añade la línea después):
```bash
ssh myownclone-vps 'sed -i "/proxy_pass http:\/\/127.0.0.1:3000;/a\\            limit_req zone=login_zone burst=10 nodelay;" /etc/nginx/sites-available/myownclone'
```

### PASO 6.3 — Test de sintaxis
```bash
ssh myownclone-vps 'nginx -t'
```
**ÉXITO**: imprime `syntax is ok` y `test is successful`.
Si falla, **ROLLBACK** (Tarea 5) y **PÁRA**.

### PASO 6.4 — Recargar nginx
```bash
ssh myownclone-vps 'systemctl reload nginx'
```

### VERIFICAR
```bash
# Hacer 15 requests rápididas a /login. Debe dar 200 y luego 429.
ssh myownclone-vps 'for i in $(seq 1 15); do
  curl -s -o /dev/null -w "%{http_code} " -k https://localhost/login
done; echo'
```
**ÉXITO**: la salida contiene al menos un `429` entre los códigos.
**ADVERTENCIA**: si TODOS son 429, el rate limit es demasiado agresivo.
Ejecutar ROLLBACK y reportar.

### ROLLBACK
```bash
ssh myownclone-vps 'cp /etc/nginx/sites-available/myownclone.bak-20260701 /etc/nginx/sites-available/myownclone'
ssh myownclone-vps 'cp /etc/nginx/nginx.conf.bak-20260701 /etc/nginx/nginx.conf'
ssh myownclone-vps 'systemctl reload nginx'
```

---

## TAREA 7 — Eliminar headers duplicados en nginx

**Objetivo**: que HSTS y X-Frame-Options aparezcan 1 sola vez.

### PASO 7.1 — Verificar duplicación actual
```bash
ssh myownclone-vps 'curl -sI -k https://localhost/ | grep -ciE "strict-transport|x-frame"'
```
**Anota el número**. Si es 4 (2 de cada uno), hay duplicación.

### PASO 7.2 — Quitar headers del `http {}` block de nginx.conf
Los headers están definidos en `/etc/nginx/sites-available/myownclone`
(líneas 37-41). Si también aparecen en `/etc/nginx/nginx.conf`, hay que
quitarlos del `nginx.conf`.

Comprobar:
```bash
ssh myownclone-vps 'grep -nE "Strict-Transport|X-Frame-Options|X-Content-Type|Referrer-Policy|Permissions-Policy" /etc/nginx/nginx.conf'
```
- Si NO aparecen → el problema es otro. **PÁSA** a la siguiente tarea.
- Si aparecen → borrar esas líneas con sed. **CONSULTA con el operador
  antes de borrar de nginx.conf**, porque puede afectar a otros sites.

### PASO 7.3 (alternativa segura) — Mover headers a un snippet
Si hay duda, crear `/etc/nginx/snippets/security-headers.conf`:
```nginx
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
add_header X-Frame-Options "DENY" always;
add_header X-Content-Type-Options "nosniff" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header Permissions-Policy "geolocation=(), microphone=(), camera=()" always;
```
E incluirlo en el server block con `include snippets/security-headers.conf;`
y quitar los `add_header` individuales. **CONSULTA al operador antes.**

### VERIFICAR
```bash
ssh myownclone-vps 'curl -sI -k https://localhost/ | grep -ciE "strict-transport|x-frame"'
```
**ÉXITO**: el número es 2 (1 de cada header).

### ROLLBACK
```bash
ssh myownclone-vps 'cp /etc/nginx/sites-available/myownclone.bak-20260701 /etc/nginx/sites-available/myownclone'
ssh myownclone-vps 'systemctl reload nginx'
```

---

## TAREA 8 — Instalar node_exporter para monitoring

**Objetivo**: exponer métricas de host en 127.0.0.1:9100.

### EJECUTAR
```bash
ssh myownclone-vps 'apt-get update -qq && apt-get install -y prometheus-node-exporter 2>&1 | tail -5'
```

### PASO 8.1 — Configurar bind a localhost
```bash
ssh myownclone-vps 'echo "ARGS=\"--web.listen-address=127.0.0.1:9100\"" > /etc/default/prometheus-node-exporter'
ssh myownclone-vps 'systemctl restart prometheus-node-exporter'
```

### PASO 8.2 — Habilitar al arranque
```bash
ssh myownclone-vps 'systemctl enable prometheus-node-exporter'
```

### VERIFICAR
```bash
ssh myownclone-vps 'systemctl is-active prometheus-node-exporter'
ssh myownclone-vps 'curl -s http://127.0.0.1:9100/metrics | grep -cE "^node_"'
```
**ÉXITO**:
- `systemctl` imprime `active`
- `curl` imprime un número > 100 (hay cientos de métricas node_*)

### ROLLBACK
```bash
ssh myownclone-vps 'systemctl stop prometheus-node-exporter && systemctl disable prometheus-node-exporter'
```

---

## TAREA 9 — STT upgrade (whisper tiny → base)

**Objetivo**: mejorar la precisión de transcripción.
**Precondición**: al menos 500MB de RAM libre.

### PASO 9.1 — Verificar RAM libre
```bash
ssh myownclone-vps 'free -h | awk "/Mem:/{print \$7}"'
```
**ÉXITO**: el valor es ≥ 500M (ej: `2.5Gi`). Si es menor, **PÁSA** de
esta tarea — no hay memoria suficiente para `base`.

### PASO 9.2 — Añadir variable de entorno
```bash
ssh myownclone-vps 'grep -q "LOCAL_WHISPER_MODEL" /opt/myownclone/shared/backend.env.production || echo "LOCAL_WHISPER_MODEL=base" >> /opt/myownclone/shared/backend.env.production'
```

### PASO 9.3 — Reiniciar el backend con env cargado
```bash
ssh myownclone-vps 'cd /opt/myownclone/releases/20260629144355-frontend-i18n-selector && docker compose -f ops/docker-compose.backend.prod.yml stop api && set -a && . ops/backend.env.production && set +a && docker compose -f ops/docker-compose.backend.prod.yml up -d --no-deps api 2>&1 | tail -3'
```

### PASO 9.4 — Esperar a que arranque
```bash
ssh myownclone-vps 'sleep 20 && curl -s http://127.0.0.1:5001/readyz'
```
**ÉXITO**: imprime JSON con `"status":"ready"`.
Si falla o no responde en 60s, **ROLLBACK**.

### VERIFICAR
```bash
ssh myownclone-vps 'docker exec myownclone_api python -c "
from api.core.model_registry import ModelRegistry
from api.models.ai_models import AITask
r = ModelRegistry().get_model_for_task(tenant_id=None, task=AITask.STT)
print(r.provider, r.model_id)
"'
```
**ÉXITO**: imprime `local_whisper base`.

### ROLLBACK
```bash
ssh myownclone-vps 'sed -i "s/^LOCAL_WHISPER_MODEL=base/LOCAL_WHISPER_MODEL=tiny/" /opt/myownclone/shared/backend.env.production'
ssh myownclone-vps 'cd /opt/myownclone/releases/20260629144355-frontend-i18n-selector && docker compose -f ops/docker-compose.backend.prod.yml stop api && set -a && . ops/backend.env.production && set +a && docker compose -f ops/docker-compose.backend.prod.yml up -d --no-deps api'
```

---

## TAREA 10 — Documentar restore procedure

**Objetivo**: crear un runbook de recuperación.

### EJECUTAR
Crear el archivo `.omo/runbooks/restore-from-backup.md` con el
siguiente contenido (copiar literal):
```markdown
# Runbook: Restaurar MyOwnClone desde backup

## 1. Restaurar PostgreSQL
\`\`\`bash
# 1. Localiza el backup más reciente
ls -t /opt/myownclone/backups/*.sql.gz | head -3

# 2. Restaura
zcat /opt/myownclone/backups/myownclone_YYYYMMDD_HHMMSS.sql.gz | \
  docker exec -i myownclone_postgres psql -U postgres -d myownclone

# 3. Verifica
docker exec myownclone_postgres psql -U postgres -d myownclone -c "SELECT COUNT(*) FROM accounts;"
\`\`\`

## 2. Reconstruir Weaviate
Los embeddings están en la tabla `chunks` (PostgreSQL). Weaviate se
reconstruye desde ahí:
\`\`\`bash
docker exec myownclone_api python -m api.scripts.reindex_weaviate
\`\`\`

## 3. Re-pull modelos Ollama
\`\`\`bash
docker exec myownclone_ollama ollama pull mxbai-embed-large:latest
\`\`\`

## 4. Reconstruir imagen API
\`\`\`bash
cd /opt/myownclone/current
docker compose -f ops/docker-compose.backend.prod.yml build api
\`\`\`

## 5. Tiempos estimados
- PostgreSQL: 2-5 min (DB pequeña)
- Weaviate: 10-30 min (depende del número de chunks)
- Ollama: 5-10 min (descarga 669MB)
- Imagen API: 5-10 min (build)
- TOTAL: 22-55 min
```

### VERIFICAR
```bash
ls -la /c/Users/haxth3/Documents/MyOwnClone-admin-vps-exec/.omo/runbooks/restore-from-backup.md
```
**ÉXITO**: el archivo existe y no está vacío.

### ROLLBACK (no aplica)

---

## CHECKPOINT FINAL — Verificación global

**Ejecutar DESPUÉS de completar todas las tareas (o cuando se pare).**

```bash
ssh myownclone-vps '
  echo "=== HEALTH ===" &&
  curl -s http://127.0.0.1:5001/readyz && echo "" &&
  echo "=== DISK ===" && df -h / | tail -1 &&
  echo "=== MEMORY ===" && free -h | head -2 &&
  echo "=== CONTAINERS ===" && docker ps --format "{{.Names}}: {{.Status}}" &&
  echo "=== FRONTEND ===" && curl -s -o /dev/null -w "http=%{http_code}\n" -k https://localhost/ &&
  echo "=== OLLAMA MODELS ===" && docker exec myownclone_ollama ollama list &&
  echo "=== NODE_EXPORTER ===" && curl -s http://127.0.0.1:9100/metrics | head -1
'
```

**CRITERIOS DE ÉXITO GLOBAL**:
- `/readyz` → contiene `"status":"ready"`
- Disco `Use%` ≤ 30%
- Todos los contenedores: `Up`
- Frontend → `http=200`
- Ollama lista solo `mxbai-embed-large`
- node_exporter responde

---

## RESUMEN DE TAREAS (checklist)

Copia esta lista y márcala conforme avances:

- [ ] TAREA 1 — Eliminar imágenes Docker API obsoletas
- [ ] TAREA 2 — Limpiar build cache
- [ ] TAREA 3 — Pin de imagen API activa
- [ ] TAREA 4 — Eliminar embeddinggemma de Ollama
- [ ] TAREA 5 — Backup de config nginx
- [ ] TAREA 6 — Rate limiting en nginx
- [ ] TAREA 7 — Eliminar headers duplicados
- [ ] TAREA 8 — Instalar node_exporter
- [ ] TAREA 9 — STT upgrade tiny → base
- [ ] TAREA 10 — Documentar restore procedure
- [ ] CHECKPOINT FINAL — Verificación global

---

## TAREAS PENDIENTES DE INPUT DEL USUARIO (no ejecutar sin autorización)

Estas tareas requieren credenciales o decisiones del operador humano:

- **BACKUPS OFF-SITE**: necesita credencial de S3/B2/Backblaze.
  Ver detalle en `vps-hardening-implementation-plan-2026-07-01.md` Parte 5.
- **GRAFANA CLOUD**: necesita URL + API key del workspace.
- **ACTUALIZAR DEPENDENCIAS PYTHON**: requiere tests regresivos
  completos antes de promover a producción.
- **CSP ESTRICTA (sin unsafe-inline)**: requiere refactor del frontend.