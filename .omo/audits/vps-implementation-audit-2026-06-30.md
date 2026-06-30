# Auditoría de implementación en VPS — 2026-06-30

## Resumen ejecutivo

**Estado general**: ✅ Producción estable y operativa. 5 containers
corriendo, 28 tests backend, 10 tests frontend, backups diarios
automatizados, SSL válido hasta Sep 2026, CSP y HSTS activos, fail2ban
protegiendo SSH.

**Riesgos principales identificados** (ordenados por severidad):
1. 🔴 9 imágenes Docker de API obsoletas (~5.4GB) sin política de
   limpieza
2. 🟠 Sin rate limiting en nginx para `/api/*` ni para `/login`
3. 🟠 `ops-api:latest` pesa 1.41GB vs 597MB anteriores (faster-whisper
   + ctranslate2); no se ha cuantificado el impacto en arranque ni
   memoria
4. 🟠 Sin monitoreo centralizado (métricas, alertas, dashboards)
5. 🟡 Paquetes de sistema desactualizados (pip, setuptools, wheel,
   grpcio, protobuf)
6. 🟡 Imagen `ops-api` no está pinned (tag `:latest`) — deployments
   no son reproducibles
7. 🟡 Sin tag de release explícito en el contenedor actual (las
   imágenes intermedias `v1.0.0` ... `v1.5.1` sí lo tienen)
8. 🟢 Frontend no tiene tests e2e corriendo contra el live (Playwright
   existe pero no hay CI)

---

## 1. Containers y servicios

| Container | Imagen | Estado | Uptime | Notas |
|---|---|---|---|---|
| myownclone_api | ops-api (1.41GB) | Up (healthy) | 6h | Sin tag, ahora 2.4× más pesado por STT |
| myownclone_postgres | pgvector/pgvector:pg15 | Up (healthy) | 24h | Pinned, OK |
| myownclone_redis | redis:7-alpine | Up (healthy) | 24h | Pinned, OK |
| myownclone_ollama | ollama/ollama:latest | Up | 30h | Sin pin (latest) |
| myownclone_weaviate | cr.weaviate.io/.../weaviate:1.24.0 | Up (healthy) | 6d | Pinned, OK |

**Recursos host**:
- 3.8Gi RAM total, 1.2Gi usado, 2.5Gi disponible
- 116GB disco, 33GB usado (28%), 84GB libre
- Load average 0.11 (excelente)
- Frontend: 12ms response time

**Imagen `ops-api`** no está pinneada a un tag. Tag `latest` impide
rollbacks reproducibles. **Recomendación**: taggear cada release
ej. `ops-api:v2026.06.30` y referenciar siempre por tag.

## 2. Backend

**Readiness**: `{"checks":{"database":"ok","redis":"ok"},"status":"ready"}`

**Tests** (28 archivos):
- `test_i18n.py` (23 tests) — todos pasan
- `test_local_whisper_stt.py` (18 tests) — todos pasan
- Otros: maintenance, embeddings, registry, retry, token budget, etc.

**Logs**: sin errores en la última hora. Sin tracebacks. Worker
gunicorn 2× healthy.

**Issue menor**: el endpoint `/console/api/myownclone/admin/ia-modelos/registry-status`
devuelve 404 — el path real no es ése. La UI admin debe estar usando otro
endpoint o un fallback. Verificar antes de exponer el panel admin.

## 3. Frontend

**Build**: 200 OK, ~12ms response time
**Tests**: 10 archivos (`__tests__`)
**Rutas auditadas** (todas 200):
- `/`, `/login`, `/registro` (legacy Spanish, conservado intencionalmente)
- `/signup` eliminado (404)

**Stack**:
- Next 16.2.9, React 19.2.4
- next-intl 4.13, next-auth 5.0.0-beta.25
- tailwindcss 4
- framer-motion 12.40

**Issue**: `next-auth@5.0.0-beta.25` sigue en beta. Riesgo de
breaking changes en releases. Monitorear.

## 4. Nginx

**Config**: `nginx -t` OK
**SSL**: TLSv1.3, cipher TLS_AES_256_GCM_SHA384, cert válido hasta
2026-09-13 (auto-renew via certbot timer, próximo run en 7h)
**Headers de seguridad**: ✅
- HSTS: `max-age=31536000; includeSubDomains; preload`
- X-Frame-Options: DENY (con SameOrigin duplicado — limpiar)
- X-Content-Type-Options: nosniff
- Referrer-Policy: strict-origin-when-cross-origin
- Permissions-Policy: deshabilita cámara, micrófono, geolocation
- CSP definida pero `default-src 'self'` es muy restrictivo — puede
  romper features como login social con Google

**Issue crítico**: NO hay rate limiting (`limit_req` ausente). El login
form puede ser objetivo de fuerza bruta. fail2ban protege SSH pero no
HTTPS.

**Issue duplicado**: 2× Strict-Transport-Security y 2× X-Frame-Options
en cada response (uno del server block, otro de defaults). Limpiar.

## 5. Secrets y env

**Producción** (`/opt/myownclone/shared/backend.env.production`):

| Clave | Estado |
|---|---|
| DB_PASSWORD, REDIS_PASSWORD | ✅ set, 64+ chars |
| JWT_SECRET_KEY, IMPERSONATION_TOKEN_PEPPER | ✅ set, 64+ chars |
| SECRET_KEY, SERVICE_API_KEY, MODEL_SECRETS_KEY | ✅ set |
| WEAVIATE_API_KEY | ✅ set |
| MINIMAX_API_KEY | ✅ set (en uso activo) |
| SENDGRID_INBOUND_WEBHOOK_SECRET | ✅ set (rotado) |
| OPENAI_API_KEY, OPENAI_BASE_URL | ❌ vacíos (intencional — STT usa local_whisper) |
| ANTHROPIC_API_KEY, TOGETHER_API_KEY | ❌ vacíos (legacy, sin uso) |
| STRIPE_*, WHEREBY_API_KEY | ❌ vacíos (features deshabilitadas) |
| RESEND_API_KEY, RESEND_FROM_EMAIL | ✅ set |

**Riesgos**:
- `backend.env.production` tiene permisos `600 root:root` ✅
- Las env vars se cargan vía `env_file: ./backend.env.production`
  (relativo al compose). Cuando se hace `set -a && .` antes de `docker
  compose up` se evita el problema. Documentar.
- OPENAI_API_KEY y OPENAI_BASE_URL vacíos son correctos para el
  fallback `local_whisper` actual.

**Recomendación**: mover secretos a un gestor real
(sops/age, Vault, AWS Secrets Manager) cuando se escale.

## 6. Modelos IA — runtime actual

| Task | Provider | Model | Fuente | Notas |
|---|---|---|---|---|
| chat | minimax | minimax-m2.7 | legacy_env | En uso |
| email_classification | minimax | minimax-m2.7 | legacy_env | (alias de chat) |
| email_draft | minimax | minimax-m2.7 | legacy_env | (alias de chat) |
| embedding | minimax | embo-01 | legacy_env | Pero el registry muestra `local/mxbai-embed-large` activo via DB |
| stt | local_whisper | tiny | legacy_env | Recién integrado, 1.18s/trans |

**Ollama (local embeddings)**: 2 modelos cargados
- `mxbai-embed-large:latest` (669MB) — activo vía DB
- `embeddinggemma:latest` (621MB) — instalado, sin uso actual

**Recomendación**: decidir si `embeddinggemma` se queda o se borra
para liberar 621MB en disco. Si no se va a usar → `docker exec
myownclone_ollama ollama rm embeddinggemma`.

## 7. Base de datos

| Tabla | Conteo |
|---|---|
| accounts | 3 |
| conversations | 3 |
| messages | 6 |
| chunks | 3 (todos embedded) |
| ai_models | 3 |
| ai_model_assignments | 5 |
| bookings | 0 |
| cost_tracking | 0 |

**Alembic**: 1 versión aplicada (tabla `alembic_version` presente).
**Pending**: bookings y cost_tracking vacíos — features no usadas aún.

**Issue**: la tabla `clones` no existe (referenciada en el log del
costs-fix). El nombre real es `clone_configs` o `clone_silo` —
verificar mapeo.

## 8. Weaviate y Ollama

- Weaviate 1.24.0 healthy, 5 días uptime
- Ollama con 2 modelos, 0 requests en cola

## 9. Backups y DR

**Cron backup**: `0 3 * * * /opt/myownclone/current/ops/backup_postgres.sh 7`
- Diario 03:00 UTC
- Retención 7 días
- Último: `myownclone_20260629_030001.sql.gz` (hace 1 día)

**Snapshots manuales**: ninguno

**Issue**: 
- No hay backup off-server (todo en /opt/myownclone/backups local).
  Si el disco falla, los backups se pierden con el DB.
- No hay backup de `weaviate_data` (chunks vectoriales).
- No hay backup de `ollama_data` (modelos descargados).

**Recomendación**:
- Push backups diarios a S3/B2 vía rclone cron
- Incluir `weaviate_data` (rsync) en el backup script
- Documentar restore procedure

## 10. Logs y monitoring

**Sin monitoring**: no hay Prometheus, Grafana, ni ningún agente de
métricas. Sólo logs de journalctl y Docker.

**Recomendación** (mínima viable):
- Instalar `node_exporter` + `promtail` (Loki) o `prometheus + grafana`
- Alertas básicas: backend down, disco >80%, RAM >90%, cert expiring
  <30d, error rate >1% en nginx access log

## 11. Seguridad

| Aspecto | Estado |
|---|---|
| HTTPS | ✅ forzado (redirect 80→443) |
| TLS 1.2/1.3 | ✅ solo protocolos modernos |
| HSTS | ✅ con preload |
| CSP | ⚠️ muy restrictiva (`'unsafe-inline'` en script-src) |
| CORS | ✅ ALLOWED_ORIGINS configurado |
| Rate limiting | ❌ no existe |
| Fail2ban SSH | ✅ activo, 884 baneos totales |
| Backups cifrados | ❌ no cifrados |
| Headers duplicados | ⚠️ 2× HSTS, 2× X-Frame-Options |
| Server tokens | ✅ `server_tokens build` |
| Container images pinned | ⚠️ api y ollama sin pin |

## 12. Dependencias desactualizadas

**Python** (en ops-api):
- pip 24.0 → 26.1.2
- setuptools 79.0.1 → 82.0.1
- wheel 0.45.1 → 0.47.1
- grpcio 1.78.0 → 1.81.1
- protobuf 6.33.6 → 7.35.1 (mayor; chequear breaking)
- pydantic_core 2.46.4 → 2.47.0 (menor)
- typer 0.25.1 → 0.26.8

**Sistema**:
- Node 22.22.3 → 22.23.1 disponible
- noderpms con upgrades pendientes

**Recomendación**: actualizar en release dedicado con tests
regresivos antes de promover a producción.

---

## Plan de mejoras y updates propuesto

### Prioridad CRÍTICA (esta semana)

1. **Limpiar imágenes Docker obsoletas** — `docker rmi` las 9 imágenes
   con tag `v1.0.0`–`v1.5.1` (libera 5.4GB)
2. **Pinneal tag de imagen api** — tag `ops-api:v2026.06.30`,
   documentar proceso de build
3. **Rate limiting básico en nginx** — al menos para `/login` y
   `/api/auth/*`. `limit_req_zone $binary_remote_addr zone=login:10m
   rate=5r/m;`
4. **Quitar headers duplicados** — eliminar el bloque duplicado en
   nginx site

### Prioridad ALTA (próximas 2 semanas)

5. **Backups off-server** — `rclone sync` diario a S3/B2 (o rsync
   contra otro host). Cifrar con age/sops
6. **Quitar `embeddinggemma` de Ollama** si no se va a usar (libera
   621MB)
7. **Tag explícito en release** — `ops-api:vYYYY.MM.DD-<sha>` y
   ajustar `docker-compose.backend.prod.yml` para usar el tag
8. **Monitoring mínimo** — instalar `node_exporter` + `promtail` →
   Grafana Cloud (free tier) o similar

### Prioridad MEDIA (próximas 4 semanas)

9. **Actualizar Python deps** — bump pip/setuptools/wheel/protobuf
   en release dedicado, correr suite completa
10. **CSP más estricto** — quitar `'unsafe-inline'` de `script-src`
    (requiere nonces o refactor de Next.js)
11. **STT model upgrade** — `tiny` → `base` (mejor calidad, ~150MB
    más RAM, aún dentro del budget de 3.8Gi)
12. **Logging estructurado** — JSON logs en backend (actualmente
    texto plano) + Loki/Grafana

### Prioridad BAJA (backlog)

13. **Migrar secrets a sops/age** — quitar `backend.env.production`
14. **Habilitar HSTS preload** — ya está en header, registrar en
    hstspreload.org
15. **Test e2e Playwright en CI** — actualmente los `.spec.ts`
    existen pero no corren en pipeline
16. **Documentar restore procedure** — sin doc, el equipo no sabe
    cómo recuperar desde un backup
17. **TLS 1.3 only** — quitar `TLSv1.2` del `ssl_protocols` (es
    opcional, mejora seguridad pero rompe clientes viejos)

---

## Recomendaciones operacionales inmediatas

- **No tocar `ops-api:latest`**: taggear y actualizar manualmente
- **No hacer `docker system prune` automático**: las imágenes viejas
  son rollback points
- **Documentar en `HANDOFF_LLM.md`** cualquier cambio de release
- **Tests deben pasar antes de cada deploy** — pytest 28 + vitest 10
- **Backups de 7 días** son insuficientes para un SaaS — llevar a 30
  días + off-server

## Shas de referencia

- Backend: `codex/backend-admin-vps-exec @ c610e14`
- Frontend: `deploy/maint-mode-plus-wip @ 6984c6c`
- Audit branch (autorizada): `origin/audit/sisyphus-vps-integration @ 1fe0ae3`
- VPS release: `20260629144355-frontend-i18n-selector`