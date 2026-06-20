# MANUAL TÉCNICO INTERACTIVO — MyOwnClone (RSL)

> Documento vivo. Última revisión: 2026-06-20.
> Rama base: `audit/vps-sync-and-docs`
> Alcance: cómo funciona TODO el sistema por dentro, basado en el código real del repositorio.
> Convención de rutas: las rutas son **relativas a la raíz del repo** (`C:\Users\haxth3\Documents\MyOwnClone-vps-fixes` en local, `/opt/myownclone/current` en el VPS).

---

## ⚠️ 5 VERDADES QUE DEBES SABER ANTES DE EMPEZAR

Estos 5 hechos cambian todo lo que crees saber si vienes de leer documentación genérica de "aplicaciones con IA":

1. **El "embedding" NO es un embedding semántico de IA.** Es un **hash léxico FNV-1a de 1536 dimensiones** inventado a mano en este proyecto. No usa OpenAI, no usa un modelo de lenguaje para crear vectores. Es matemática de hashing. Está en `api/core/retrieval.py:90` y `MyOwnClone/src/app/api/clone/sources/route.ts:61`. Esto significa que las búsquedas son **por palabras clave + similitud del hash**, no por significado real.

2. **Weaviate, `RetrievalService`, `Dataset` y `DocumentSegment` están DORMIDOS.** Son *stubs* (código vacío). Arrancan en Docker pero el sistema **nunca los llama en runtime**. La recuperación real usa las tablas Postgres `sources` + `chunks`.

3. **La ingesta de documentos (trocear texto y crear vectores) ocurre en el FRONTEND Next.js**, no en Flask. El endpoint `POST /api/clone/sources` (Next.js) es quien trocea y guarda. Flask solo lee.

4. **El chat usa el primer proveedor de IA con API key configurada**, en orden fijo: OpenAI → Anthropic → MiniMax → Together. No hay selector por tenant. En el VPS de producción **solo MiniMax tiene key configurada**.

5. **La identidad de admin NO se hereda de cabeceras HTTP.** `X-User-Role: platform_admin` es solo una pista; el backend siempre consulta la columna `is_platform_admin` en la tabla `accounts`. Ver `_is_platform_admin` en `api/controllers/console/myownclone/admin_platform.py:697`.

Si memorizas estos 5 puntos, el resto del manual tiene sentido.

---

# SECCIÓN 1: RADIOGRAFÍA COMPLETA DEL SISTEMA

## ¿Qué es este sistema por dentro?

**MyOwnClone** es una plataforma SaaS multi-tenant para crear **clones digitales de IA**. Cada "clon" es un asistente conversacional entrenado con el contenido de un creador, que puede tener 3 modos (enseñar, soporte, ventas), clasificar emails entrantes, agendar reuniones y vender productos.

### El edificio, piso por piso

```
[USUARIO / NAVEGADOR]
       │  hace petición HTTPS
       ▼
[NGINX]  ← reverse proxy, TLS, security headers  (puerto 443)
       │
       ├──────────────────────────────────────────┐
       ▼                                          ▼
[FRONTEND NEXT.JS]                    [BACKEND FLASK directo]
app/* (páginas)                       /api/myownclone/public/inbound-email  (SendGrid)
src/proxy.ts  ← valida JWT NextAuth   /api/deploy                            (CI/CD webhook)
   │  inyecta X-API-Key + identidad
   ▼
[BACKEND FLASK / Gunicorn]  (puerto 5001)
   ├─ /console/api/*        ← panel de gestión (auth requerida)
   ├─ /api/myownclone/public/*  ← chat público (rate-limited)
   ├─ /healthz, /readyz     ← healthchecks
   │
   ├──────────────┬──────────────┬──────────────┐
   ▼              ▼              ▼              ▼
[POSTGRESQL]   [REDIS]      [WEAVIATE]     [LLM externo]
pg15+pgvector  cache/rate   (stub dormido) MiniMax/OpenAI/
memoria real   limiting                    DeepSeek/Anthropic/
                                           Together
```

### Capas detalladas

| Capa | Tecnología | Dónde vive | Qué la configura | Cómo inicia/detiene | Cómo sé que funciona |
|---|---|---|---|---|---|
| **Reverse proxy** | nginx | VPS host (`/etc/nginx/sites-enabled/myownclone`) | `ops/nginx.myownclone.conf.example` | `sudo systemctl reload nginx` | `curl -I https://myownclone.com` → 200 + HSTS |
| **Frontend** | Next.js 16 + React 19 + TypeScript | VPS, systemd service `myownclone-frontend`, WorkingDir `/opt/myownclone/current/MyOwnClone` | `MyOwnClone/.env.production` | `sudo systemctl restart myownclone-frontend` | `curl http://127.0.0.1:3000/` → HTML 200 |
| **Backend** | Flask 3 + Gunicorn (Docker) | Contenedor `myownclone_api`, puerto 5001 | `ops/backend.env.production` | `docker compose -f ops/docker-compose.backend.prod.yml restart api` | `curl http://127.0.0.1:5001/readyz` → `{"status":"ready"}` |
| **Base de datos** | PostgreSQL 15 + pgvector 0.8.2 | Contenedor `myownclone_postgres`, puerto 5432 | `DATABASE_URL` / `DB_*` en backend env | `docker compose ... restart db_postgres` | `/readyz` muestra `"database":"ok"` |
| **Cache/Rate limit** | Redis 7-alpine | Contenedor `myownclone_redis`, puerto 6379 | `REDIS_HOST`, `REDIS_PASSWORD` | `docker compose ... restart redis` | `/readyz` muestra `"redis":"ok"` |
| **Vector DB (dormida)** | Weaviate 1.24.0 | Contenedor `myownclone_weaviate`, puerto 8080 | `WEAVIATE_API_KEY`, `WEAVIATE_URL` | `docker compose ... restart weaviate` | NO se usa en runtime; healthcheck wget |
| **IA externa** | MiniMax (configurado) / OpenAI / DeepSeek / Anthropic / Together | Servicios externos en internet | `MINIMAX_API_KEY`, `OPENAI_API_KEY`, etc. | N/A (serverless) | El chat responde |

### Puertos del VPS de producción (212.227.169.99)

| Puerto | Servicio | Exposición | Estado tras hardening |
|---|---|---|---|
| 22 | SSH | Público (solo llave tras P0-2) | ✅ Endurecido |
| 80 | nginx | Público (redirect a 443) | ✅ |
| 443 | nginx | Público (HTTPS) | ✅ |
| 3000 | Next.js | **Bloqueado al exterior por UFW** | ✅ |
| 5001 | Flask | Loopback `127.0.0.1` | ✅ |
| 5432 | PostgreSQL | Loopback | ✅ |
| 6379 | Redis | Loopback | ✅ |
| 8080 | Weaviate | Loopback | ✅ |
| 9999 | (era `python -m http.server` root) | **Cerrado** tras P0-1 | ✅ Eliminado |

### El flujo de un chat público (el más importante)

```
Visitante abre https://myownclone.com/miclone
   │
   ▼  (nginx → Next.js SSR)
Página [slug]/page.tsx  →  fetch GET /api/myownclone/public/clones/miclone
   │
   ▼  (ChatPanel.tsx, React)
Usuario escribe y pulsa enviar
   │
   ▼  POST /api/public/clones/miclone/chat  (Next.js)
   │
   ▼  proxy.ts enruta → POST http://127.0.0.1:5001/api/myownclone/public/clones/miclone/chat
   │
   ▼  Flask: chat_public() en myownclone_public.py:283
   │    1. Rate limit (20 msgs/60s por IP+slug)
   │    2. Valida silo (teach/support/sales)
   │    3. Carga CloneModePrompt (system prompt del modo)
   │    4. Añade CreatorMemory a ese prompt
   │    5. retrieve_from_silo() → busca chunks relevantes en sources/chunks
   │    6. Construye prompt final: system + contexto RAG + pregunta
   │    7. ModelManager.invoke_llm_stream() → MiniMax (streaming SSE)
   │    8. Persiste Conversation + Message + AnalyticsQuestion
   ▼  Respuesta SSE: data: {"content":"..."}...\ndata: [DONE]
   │
   ▼  proxy.ts detecta text/event-stream → pasa el stream tal cual
   ▼  ChatPanel renderiza token a token
```

---

# SECCIÓN 2: EL BACKEND — EL CEREBRO DEL SISTEMA

## Estructura de archivos del backend

El backend vive en `api/`. Punto de entrada: `api/app_factory.py` (factory `create_app()`, línea 134).

```
api/
├── app_factory.py          ← Crea la app Flask. Punto de entrada real.
├── run_dev.py              ← Servidor de desarrollo (solo local).
├── base.py                 ← Mixins base para modelos ORM.
├── model_types.py          ← Tipo LongText (TEXT de Postgres).
├── Dockerfile              ← Imagen del contenedor (gunicorn en :5001).
├── docker-compose.yml      ← Compose de desarrollo local.
├── requirements.txt        ← Dependencias Python (Flask, SQLAlchemy, etc.).
├── requirements-dev.txt    ← Dependencias de desarrollo.
│
├── commands/
│   └── seed.py             ← Comando CLI: flask seed-demo-data
│
├── configs/
│   └── __init__.py         ← myownclone_config (STRIPE_SECRET_KEY, etc.)
│
├── controllers/            ← TODOS los endpoints HTTP
│   ├── myownclone_public.py    ← Endpoints PÚBLICOS (chat, booking, email)
│   ├── deploy.py               ← /api/deploy (webhook CI/CD)
│   ├── common/schema.py        ← Helpers de esquema flask-restx
│   └── console/                ← Panel de gestión (auth requerida)
│       ├── auth.py             ← /console/api/auth/login (JWT)
│       ├── wraps.py            ← Decoradores @login_required, @setup_required
│       └── myownclone/
│           ├── clone.py            ← CRUD de clones y prompts
│           ├── admin_platform.py   ← Multi-tenant, impersonación, MRR
│           ├── booking.py          ← Meeting types, disponibilidad, bookings
│           ├── inbox.py            ← Email inbound CRUD
│           ├── stripe_ctrl.py      ← Checkout, billing portal
│           ├── analytics.py        ← Métricas, gaps, costos
│           ├── creator_memory.py   ← Memorias/firmas/plantillas
│           └── feedback.py         ← Thumbs up/down
│
├── core/                  ← LÓGICA DE NEGOCIO Y IA
│   ├── model_manager.py   ← ⭐ Façade LLM (OpenAI/Anthropic/MiniMax/Together)
│   ├── retrieval.py       ← ⭐ RAG: retrieve_from_silo() (hash léxico local)
│   ├── ingestion.py       ← Metadata de ingesta (wrapper, actualmente dormido)
│   ├── contracts.py       ← Normalización de planes, silos, estados
│   ├── myownclone/
│   │   ├── email_ai.py    ← Prompts de clasificación y borrador de email
│   │   ├── email_processor.py  ← Parser MIME + resolve clone por dominio
│   │   └── silos.py       ← Gestión de datasets por silo (legacy/stub)
│   └── rag/
│       ├── datasource/retrieval_service.py  ← ⚠️ STUB (vacío)
│       └── retrieval/retrieval_methods.py   ← Enum de métodos (no usado)
│
├── extensions/
│   └── ext_database.py    ← Instancia `db` de SQLAlchemy
│
├── fields/
│   └── base.py            ← ResponseModel (pydantic para respuestas)
│
├── libs/                  ← Utilidades compartidas
│   ├── login.py           ← ⭐ @login_required (JWT o X-API-Key+forwarded)
│   ├── jwt_utils.py       ← Firma/verificación JWT (HS256)
│   ├── security_checks.py ← assert_production_secrets() (fail-fast)
│   ├── uuid_utils.py      ← uuidv7() (IDs ordenados por tiempo)
│   └── datetime_utils.py  ← naive_utc_now()
│
├── migrations/            ← Alembic
│   ├── env.py
│   └── versions/          ← 11 migraciones (c3d4e5f6a7c1 = head actual)
│
├── models/                ← SQLAlchemy ORM (esquema DB)
│   ├── account.py         ← Tenant, Account (usuarios)
│   ├── clone.py           ← CloneConfig, CloneModePrompt, CreatorMemory
│   ├── knowledge.py       ← Source, Chunk  ⭐ (la base de conocimiento real)
│   ├── conversation.py    ← Conversation, Message
│   ├── email.py           ← EmailInbound, EmailTemplate
│   ├── meeting.py         ← MeetingType_, Availability, Booking, Product
│   ├── analytics.py       ← CostTracking, Plan, AnalyticsQuestion, etc.
│   ├── dataset.py         ← ⚠️ STUB Dataset/DocumentSegment
│   └── myownclone/        ← Re-export de compatibilidad
│
└── tests/
```

### Archivos clave en detalle

#### 📁 `api/app_factory.py`
- **¿Qué hace?**: Crea y configura la app Flask. Es el corazón del arranque.
- **¿Cuándo se ejecuta?**: Al arrancar el contenedor (gunicorn llama `api.app_factory:app`).
- **¿Puedo modificarlo?**: Sí, con cuidado.
- **¿Si lo borro qué pasa?**: El backend no arranca. Fatal.
- **Funciones clave**:
  - `create_app()` (l.134) → construye la app, registra blueprints, healthchecks.
  - `_setup_dev_keys()` (l.56) → genera secretos aleatorios en dev si faltan.
  - `_parse_origins()` (l.82) → lee `ALLOWED_ORIGINS` (CORS).
  - `_database_uri()` (l.91) → construye la URL de Postgres (prioriza `DATABASE_URL`).
  - `_redis_ready()` (l.113) → ping a Redis para `/readyz`.
  - `register_health_routes(app)` (l.184) → registra `/healthz` y `/readyz`.
  - `register_myownclone_blueprints(app)` (l.217) → monta public, console, auth, deploy.

#### 📁 `api/libs/security_checks.py`
- **¿Qué hace?**: `assert_production_secrets()` aborta el arranque si hay secretos inseguros.
- **Variables que valida en producción** (l.13-18):
  - `JWT_SECRET_KEY`, `IMPERSONATION_TOKEN_PEPPER`, `ALLOWED_ORIGINS`, `REDIS_PASSWORD` → obligatorios.
  - `DB_*` o `DATABASE_URL` → obligatorios.
  - `DB_PASSWORD`, `REDIS_PASSWORD` → rechazan `postgres`, `changeit`, `change-me`, vacío.
- **⚠️ Si lo borras**: el backend arrancaría con secretos débiles en producción = brecha de seguridad.

#### 📁 `api/libs/login.py`
- **¿Qué hace?**: Decorador `@login_required` (l.49). Es el **guardián de autenticación**.
- **Flujo** (l.51-89):
  1. Intenta `Authorization: Bearer <JWT>` → `_verify_token()` (HS256).
  2. Si no, intenta `X-API-Key` → compara con `SERVICE_API_KEY` (timing-safe).
  3. Si la key service es válida, lee identidad de `X-User-Id`, `X-User-Role`, etc. (inyectados por el proxy Next.js).
- **⚠️ Advertencia**: `X-User-Role` es solo una pista. El check real de platform_admin consulta la DB (`_is_platform_admin`).
- **Variable clave**:
  - `SERVICE_API_KEY` → clave de servicio frontend↔backend. **Debe coincidir** en ambos `.env`.
  - `ALLOW_DEV_SERVICE_KEY=true` → permite `dev-api-key-for-proxy` solo fuera de producción.

#### 📁 `api/libs/jwt_utils.py`
- **¿Qué hace?**: Firma y verifica JWT.
- **`_get_secret_key()`** (l.12): rechaza producción si `JWT_SECRET_KEY` es débil o < 32 chars.
- **`_verify_token()`** (l.33): decodifica HS256, devuelve payload o None.

### Flujo de una petición autenticada (ej: crear clone)

```
1. Usuario en dashboard hace clic en "Crear clone"
   → POST /api/clones  (Next.js)
2. proxy.ts valida:
   - Sí es ruta protegida (no es /api/auth/login ni /api/public/*)
   - Sí hay token NextAuth (sino 401)
   - Mapea: /api/clones → /console/api/myownclone/clones
   - Inyecta: X-API-Key, X-User-Id, X-User-Email, X-User-Role, X-Tenant-Id
3. Backend recibe en:
   → api/controllers/console/myownclone/clone.py:104 (CloneConfigListApi.post)
4. Decoradores:
   @login_required → valida X-API-Key + forwarded identity
   @account_initialization_required → comprueba g.account_id
5. Valida con CloneConfigPayload (pydantic)
6. Consulta DB:
   → SELECT * FROM clone_configs WHERE slug = ?
   → si existe: 409 "already exists"
7. Crea CloneConfig + 3 CloneModePrompt (teach/support/sales)
8. INSERT, commit
9. Devuelve JSON 201 con el clone serializado
```

### Flujo de un chat público (con IA) — ver Sección 1, ya detallado arriba.

### Flujo de un email entrante (SendGrid Inbound Parse)

```
1. Alguien escribe a hola@dominio-del-clon.com
2. SendGrid recibe el email y POST a:
   https://myownclone.com/api/myownclone/public/inbound-email
   (nginx → directo a Flask, NO pasa por proxy.ts porque es multipart)
3. Flask: myownclone_public.py:186 inbound_email()
   - Valida X-Webhook-Secret (SENDGRID_INBOUND_WEBHOOK_SECRET)
   - En producción sin secret: 503
4. parse_inbound_email() → extrae From, Subject, Body, To-domain
5. resolve_clone_by_domain() → busca CloneConfig.custom_domain
6. _classify_and_draft():
   - classify_email() → LLM clasifica (consulta/queja/venta/soporte)
   - generate_draft_reply() → LLM redacta borrador con memoria+plantillas
7. INSERT en email_inbound (status=pending, draft_reply=...)
8. 200 {"status":"received","id":"..."}
9. El creador revisa el borrador en /inbox
```

---

# SECCIÓN 3: APIs — TODAS LAS CONEXIONES

## Mapa completo de endpoints

### 3.1 Endpoints PÚBLICOS (sin auth de usuario, rate-limited)

Blueprint: `myownclone_public_bp`, prefijo `/api/myownclone/public`. Archivo: `api/controllers/myownclone_public.py`.

---

🔗 **`POST /api/myownclone/public/inbound-email`**
- **¿Para qué?**: Webhook de SendGrid Inbound Parse (recibe emails).
- **¿Quién lo llama?**: SendGrid (server-to-server).
- **Auth**: cabecera `X-Webhook-Secret` vs `SENDGRID_INBOUND_WEBHOOK_SECRET`. En producción sin secret → 503.
- **Request**: multipart/form-data con campo `email` (raw MIME) o JSON `{"email": "..."}`.
- **Response 200**: `{"status":"received","id":"<uuid>"}`
- **Response 200 (no content)**: `{"status":"no_content"}`
- **Response 401**: secret inválido.
- **Response 503**: producción sin secret configurado.
- **Código**: `myownclone_public.py:186`

---

🔗 **`GET /api/myownclone/public/clones/<slug>`**
- **¿Para qué?**: Info pública de un clone para la página de chat.
- **Auth**: ninguna.
- **Response 200**: `{id, name, slug, description, avatar_url, personality_tone, language, active_modes, is_active}`
- **Response 404**: clone no encontrado o inactivo.
- **Código**: `myownclone_public.py:254`

---

🔗 **`POST /api/myownclone/public/clones/<slug>/chat`** ⭐ (el principal)
- **¿Para qué?**: Chat público con streaming SSE.
- **Rate limit**: 20 mensajes / 60 segundos por IP+slug (`_CHAT_LIMIT=20`, `_WINDOW_SECONDS=60`).
- **Request body**:
  ```json
  {
    "message": "¿cómo funciona X?",     // obligatorio, máx 2000 chars
    "silo": "teach",                     // teach|support|sales, default teach
    "context_id": "abc-123",             // opcional, filtra por contexto
    "conversation_id": "<uuid>"          // opcional, continúa conversación
  }
  ```
- **Response**: `text/event-stream` (SSE).
  - Durante: `data: {"content":"token"}\n\n`
  - Final: `data: {"content":"","done":true,"conversation_id":"...","context_found":true,"silo":"teach","confidence":0.85,"sources":[...]}\n\n`
  - Cierre: `data: [DONE]\n\n`
- **Response 404**: clone no encontrado.
- **Response 400**: message vacío o silo inválido.
- **Response 413**: message > 2000 chars.
- **Response 429**: rate limit excedido.
- **Probarlo**:
  ```bash
  curl -N -X POST "http://127.0.0.1:5001/api/myownclone/public/clones/miclone/chat" \
    -H "Content-Type: application/json" \
    -d '{"message":"hola","silo":"teach"}'
  ```
- **Código**: `myownclone_public.py:283`

---

🔗 **`POST /api/myownclone/public/clones/<slug>/chat-simple`**
- **¿Para qué?**: Chat sin streaming, JSON directo. No usa RAG, solo LLM puro.
- **Rate limit**: 10 / 60s (`_CHAT_SIMPLE_LIMIT=10`).
- **Request**: `{"message":"...","session_id":"..."}` (session_id opcional).
- **Response 200**: `{"slug":"...","reply":"...","usage":{"prompt_tokens":N,"completion_tokens":N,"total_tokens":N}}`
- **Response 502**: `{"error":"model_unavailable"}` → no hay API key de LLM.
- **Código**: `myownclone_public.py:479`

---

🔗 **`GET /api/myownclone/public/clones/<slug>/meeting-types`**
- **¿Para qué?**: Tipos de reunión públicos de un clone.
- **Response 200**: array de `{id, name, duration_minutes, price_cents, description, color}`.
- **Código**: `myownclone_public.py:525`

---

🔗 **`POST /api/myownclone/public/clones/<slug>/bookings`**
- **¿Para qué?**: Crear reserva pública.
- **Rate limit**: 10 / 60s.
- **Request**:
  ```json
  {
    "meeting_type_id": "<uuid>",     // obligatorio
    "visitor_name": "Ana",           // obligatorio, máx 200 chars
    "visitor_email": "ana@x.com",    // obligatorio, máx 320, con @
    "date": "2026-07-01",            // obligatorio, ISO
    "start_time": "10:00"            // opcional, ISO
  }
  ```
- **Response 201**: `{id, status, meeting_type, visitor_name}`
- **Response 409**: slot ya reservado.
- **Código**: `myownclone_public.py:560`

---

### 3.2 Auth (console)

Blueprint: `auth_bp`, prefijo `/console/api/auth`. Archivo: `api/controllers/console/auth.py`.

🔗 **`POST /console/api/auth/login`**
- **¿Para qué?**: Login del panel (emite JWT).
- **Request**: `{"email":"...","password":"..."}`
- **Rate limit**: 5 intentos fallidos / IP → 15 min ban (`_RATE_LIMIT_MAX_ATTEMPTS=5`).
- **Response 200**: `{"token":"<jwt>","expires_in":86400,"user":{...}}` (expira en 24h).
- **Response 401**: credenciales inválidas.
- **Response 429**: demasiados intentos.
- **Comportamiento**: busca en `accounts` (canónico) y si no existe la tabla, cae a `users` (legacy Drizzle/NextAuth).

🔗 **`GET /console/api/auth/verify`**
- **¿Para qué?**: Verificar validez de un token.
- **Header**: `Authorization: Bearer <token>`
- **Response 200**: `{"valid":true,"user":"...","role":"..."}`
- **Response 401**: token inválido/expirado.

---

### 3.3 Deploy (webhook CI/CD)

Blueprint: `deploy_bp`, prefijo `/api`. Archivo: `api/controllers/deploy.py`.

🔗 **`POST /api/deploy`**
- **¿Para qué?**: Desplegar el frontend (git pull + build + restart) desde CI.
- **Auth**: `X-Deploy-Secret` vs `DEPLOY_SECRET`.
- **Ejecuta** en el VPS:
  1. `git pull origin master` en `/opt/myownclone-frontend/MyOwnClone`
  2. `npm run build`
  3. `systemctl restart myownclone-frontend`
- **Response 200**: `{"status":"success|failed","steps":[...]}`
- **Response 401**: secret inválido o ausente.
- **Código**: `deploy.py:49`

---

### 3.4 Healthchecks

🔗 **`GET /healthz`** → `{"status":"ok"}` 200. Liveness. (`app_factory.py:187`)
🔗 **`GET /readyz`** → `{"status":"ready","checks":{"database":"ok","redis":"ok"}}` 200 o 503. (`app_factory.py:191`)

---

### 3.5 Console API (protegidas, prefijo `/console/api`)

Namespace flask-restx `console_ns`. Auth: `@login_required` en todos.

> **Importante**: el proxy Next.js expone estas rutas con paths distintos. La tabla "Path frontend" es lo que ve el navegador; "Path backend" es lo real en Flask.

#### Clones (`api/controllers/console/myownclone/clone.py`)

| Método | Path frontend | Path backend | Descripción | Código |
|---|---|---|---|---|
| GET | `/api/clones` | `/console/api/myownclone/clones` | Lista clones del tenant | `clone.py:88` |
| POST | `/api/clones` | `/console/api/myownclone/clones` | Crea clone + 3 prompts | `clone.py:98` |
| GET | `/api/clone/clones/<id>` | `/console/api/myownclone/clones/<id>` | Detalle de clone | `clone.py:152` |
| PUT | `/api/clone/clones/<id>` | `/console/api/myownclone/clones/<id>` | Actualiza clone | `clone.py:171` |
| PUT | `/api/clone/clones/<id>/prompts` | `/console/api/myownclone/clones/<id>/prompts` | Modifica system prompt de un modo | `clone.py:204` |

#### Admin platform (`admin_platform.py`) — requiere `is_platform_admin=true`

| Método | Path backend | Descripción | Código |
|---|---|---|---|
| GET | `/console/api/myownclone/admin/overview` | MRR, tenants, clones, costos | `admin_platform.py:152` |
| GET | `/console/api/myownclone/admin/tenants` | Lista paginada de tenants | `admin_platform.py:199` |
| POST | `/console/api/myownclone/admin/tenants` | Crea tenant | `admin_platform.py:260` |
| GET | `/console/api/myownclone/admin/impersonation` | Log de impersonaciones | `admin_platform.py:313` |
| POST | `/console/api/myownclone/admin/impersonate` | Inicia impersonación (token 30 min) | `admin_platform.py:374` |
| POST | `/console/api/myownclone/admin/impersonate/stop` | Detiene impersonación | `admin_platform.py:437` |
| GET/POST | `/console/api/myownclone/admin/courtesy-account` | Cuentas de cortesía | `admin_platform.py:475` |
| GET | `/console/api/myownclone/admin/audit-log` | Log de auditoría | `admin_platform.py:573` |
| GET | `/console/api/myownclone/admin/feedback` | Feedback global | `admin_platform.py:630` |

#### Booking (`booking.py`)

| Método | Path backend | Descripción |
|---|---|---|
| GET/POST | `/console/api/myownclone/clones/<id>/meeting-types` | Tipos de reunión |
| GET/PUT/DELETE | `/console/api/myownclone/clones/<id>/meeting-types/<mt_id>` | Un tipo |
| GET/POST | `/console/api/myownclone/clones/<id>/availability` | Disponibilidad |
| GET/PUT/DELETE | `/console/api/myownclone/clones/<id>/availability/<aid>` | Un slot |
| GET/POST | `/console/api/myownclone/clones/<id>/products` | Productos |
| GET/PUT/DELETE | `/console/api/myownclone/clones/<id>/products/<pid>` | Un producto |
| GET/POST | `/console/api/myownclone/clones/<id>/bookings` | Reservas |
| GET/PUT/DELETE | `/console/api/myownclone/clones/<id>/bookings/<bid>` | Una reserva |

#### Inbox (`inbox.py`)

| Método | Path backend | Descripción |
|---|---|---|
| GET | `/console/api/myownclone/clones/<id>/inbox` | Lista emails (paginado) |
| GET/PUT/DELETE | `/console/api/myownclone/inbox/<email_id>` | Detalle / actualizar / descartar |
| POST | `/console/api/myownclone/inbox/<email_id>/generate-draft` | Regenerar borrador con LLM |

#### Stripe (`stripe_ctrl.py`)

| Método | Path backend | Descripción |
|---|---|---|
| GET | `/console/api/myownclone/plans` | Lista planes y precios |
| POST | `/console/api/myownclone/stripe/checkout` | Crea sesión de checkout |
| GET | `/console/api/myownclone/stripe/billing` | Portal de facturación |

#### Analytics (`analytics.py`)

| Método | Path backend | Descripción |
|---|---|---|
| GET | `/console/api/myownclone/clones/<id>/analytics/overview` | Conversaciones, mensajes, gaps |
| GET | `/console/api/myownclone/clones/<id>/analytics/top-questions` | Top 10 preguntas |
| GET/POST | `/console/api/myownclone/clones/<id>/analytics/gaps` | Huecos de conocimiento |
| GET | `/console/api/myownclone/clones/<id>/analytics/costs` | Desglose de costos |

#### Memorias (`creator_memory.py`)

| Método | Path backend | Descripción |
|---|---|---|
| GET/POST | `/console/api/myownclone/clones/<id>/memories` | Lista / crea memoria |
| PUT/DELETE | `/console/api/myownclone/memories/<mid>` | Actualiza / borra memoria |

#### Feedback (`feedback.py`)

| Método | Path backend | Descripción |
|---|---|---|
| POST | `/console/api/myownclone/feedback` | Recibe thumbs up/down |
| GET | `/console/api/myownclone/feedback/stats` | Estadísticas de feedback |

---

### 3.6 API routes nativas de Next.js (NO van al backend)

Estas se ejecutan **dentro de Next.js** (acceden a la DB vía Drizzle):

| Método | Path | Descripción | Archivo |
|---|---|---|---|
| GET/POST | `/api/clone/sources` | ⭐ Lista / **crea fuentes de conocimiento** (chunking + embedding aquí) | `MyOwnClone/src/app/api/clone/sources/route.ts` |
| GET/POST | `/api/bookings` | Reservas del usuario (vía Drizzle + Whereby + Resend) | `MyOwnClone/src/app/api/bookings/route.ts` |
| POST | `/api/stripe/webhook` | Webhook de Stripe (update tenant vía Drizzle) | `MyOwnClone/src/app/api/stripe/webhook/route.ts` |
| POST | `/api/stt` | Speech-to-text (Whisper de OpenAI) | `MyOwnClone/src/app/api/stt/route.ts` |
| GET/POST | `/api/auth/*` | NextAuth (login, OAuth, magic link) | `MyOwnClone/src/app/api/auth/[...nextauth]/route.ts` |
| GET/POST | `/api/csrf` | Token CSRF | `MyOwnClone/src/app/api/csrf/route.ts` |
| GET/POST | `/api/auth/forgot-password` | Recuperar contraseña | `.../forgot-password/route.ts` |
| POST | `/api/auth/reset-password` | Resetear contraseña | `.../reset-password/route.ts` |
| POST | `/api/auth/verify-email` | Verificar email | `.../verify-email/route.ts` |

> ⚠️ **Por qué esto importa**: la subida de documentos NO toca el backend Flask. Si el frontend Next.js está caído, no se puede entrenar clones.

---

### 3.7 Cómo cambiar/actualizar una API

**TAREA: Agregar un nuevo endpoint `GET /api/clones/<id>/stats`**

1. **Define la ruta** en el controlador correspondiente (`api/controllers/console/myownclone/clone.py`):
   ```python
   @console_ns.route("/myownclone/clones/<string:clone_id>/stats")
   class CloneStatsApi(Resource):
       @login_required
       @account_initialization_required
       @setup_required
       def get(self, clone_id: str):
           account, tenant_id = current_account_with_tenant()
           _verify_clone_access(clone_id, tenant_id)  # SIEMPRE scope por tenant
           # ... tu lógica
           return {...}, 200
   ```
2. **Verifica el scope por tenant**: toda query debe filtrar por `tenant_id`. Si no, es un fallo de seguridad cross-tenant.
3. **Si es ruta pública** (sin auth), añade rate limit con `_consume_rate_limit()` y valida inputs estrictamente.
4. **Reinicia el backend**: `docker compose -f ops/docker-compose.backend.prod.yml restart api`
5. **Si la llama el frontend**, añade el mapeo en `MyOwnClone/src/proxy.ts` (`ROUTE_MAP` o `findBackendPath`).
6. **Prueba**:
   ```bash
   curl http://127.0.0.1:5001/console/api/myownclone/clones/<id>/stats \
     -H "X-API-Key: $SERVICE_API_KEY" -H "X-User-Id: <uid>" -H "X-User-Role: owner"
   ```

⚠️ **Reglas de oro de seguridad** (aprendidas de auditorías H1-H5 del repo):
- **H1**: scope por tenant SIEMPRE en escritura de prompts (`clone.py:213`).
- **H2**: feedback solo en clones del tenant (`feedback.py:19`).
- **H3**: bookings/sources/feedback en Next.js verifican `cloneConfigs.tenantId == session.tenantId`.
- **H4**: `_is_platform_admin` consulta DB, NO confía en `X-User-Role` (`admin_platform.py:697`).
- **H5**: inbox/analytics filtran por tenant sin carve-outs mágicos (`inbox.py:214`, `analytics.py:20`).

---

### 3.8 APIs Externas que usa el sistema

🌐 **OpenAI / DeepSeek / compatible**
- **¿Para qué?**: LLM principal del chat y STT (Whisper).
- **¿Cuándo se llama?**: Cada mensaje de chat, cada clasificación de email, cada borrador, cada transcripción de audio.
- **¿Qué pasa si falla?**: chat → SSE con error; chat-simple → 502 `model_unavailable`; STT → 500.
- **API key**:
  - Backend: `OPENAI_API_KEY` en `ops/backend.env.production`
  - Frontend (STT): `OPENAI_API_KEY` en `MyOwnClone/.env.production`
- **Modelo**: `OPENAI_MODEL` (default `gpt-4o-mini`). DeepSeek: `OPENAI_BASE_URL=https://api.deepseek.com` + `OPENAI_MODEL=deepseek-chat`.
- **Dashboard**: https://platform.openai.com/usage
- **Cambiar key**:
  1. Edita `ops/backend.env.production` (y frontend si usa STT).
  2. `docker compose ... restart api`
  3. Prueba: `curl .../chat-simple` y mira los logs.

🌐 **Anthropic (Claude)**
- **¿Para qué?**: LLM alternativo (prioridad 2).
- **Variables**: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL` (default `claude-3-haiku-20240307`).
- **Dashboard**: https://console.anthropic.com/usage

🌐 **MiniMax** ⭐ (ÚNICO configurado en producción)
- **¿Para qué?**: LLM mediante endpoint OpenAI-compatible.
- **Variable**: `MINIMAX_API_KEY`, `MINIMAX_MODEL` (default `minimax-m2.7`).
- **Endpoint**: `https://api.minimax.io/v1`
- **Dashboard**: https://platform.minimaxi.com/

🌐 **Together.ai (Llama 3)**
- **¿Para qué?**: LLM económico (prioridad 4).
- **Variables**: `TOGETHER_API_KEY`, `TOGETHER_MODEL` (default `meta-llama/Llama-3-8b-chat-hf`).
- **Dashboard**: https://api.together.ai/

🌐 **Stripe**
- **¿Para qué?**: Suscripciones, checkout, billing portal.
- **Variables**: `STRIPE_SECRET_KEY` (backend), `STRIPE_WEBHOOK_SECRET` (frontend), `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY`, `STRIPE_BASIC_PRICE_ID`, `STRIPE_PRO_PRICE_ID`, `STRIPE_SCALE_PRICE_ID`.
- **Estado VPS**: **vacío** (billing no operativo).
- **Dashboard**: https://dashboard.stripe.com/

🌐 **SendGrid Inbound Parse**
- **¿Para qué?**: Recibir emails y procesarlos con IA.
- **Variable**: `SENDGRID_INBOUND_WEBHOOK_SECRET` (valida `X-Webhook-Secret`).
- **Configuración en SendGrid**: POST a `https://myownclone.com/api/myownclone/public/inbound-email`.
- **Dashboard**: https://app.sendgrid.com/

🌐 **Whereby**
- **¿Para qué?**: Crear salas de video para reuniones (`createMeeting()`).
- **Variable**: `WHEREBY_API_KEY`.
- **Estado VPS**: **vacío**.

🌐 **Resend**
- **¿Para qué?**: Emails transaccionales (magic link NextAuth, confirmación de reserva).
- **Variables**: `RESEND_API_KEY`, `RESEND_FROM_EMAIL`.
- **Dashboard**: https://resend.com/emails

🌐 **Google OAuth**
- **¿Para qué?**: Login social en NextAuth.
- **Variables**: `AUTH_GOOGLE_ID`, `AUTH_GOOGLE_SECRET`.

---

# SECCIÓN 4: INTELIGENCIA ARTIFICIAL — CÓMO PIENSA EL SISTEMA

## ¿Qué IA usa el sistema y para qué?

El sistema tiene **UN único gestor de IA** (`ModelManager`) que sabe hablar con 4 proveedores. No hay un modelo "propio"; todo es API externa.

### 🧠 COMPONENTE: ModelManager

- **Archivo**: `api/core/model_manager.py`
- **¿Qué modelo usa?**: El **primer proveedor con API key configurada**, en este orden fijo:
  1. `OPENAI_API_KEY` → OpenAI (`gpt-4o-mini` o `OPENAI_MODEL`)
  2. `ANTHROPIC_API_KEY` → Claude (`claude-3-haiku-20240307`)
  3. `MINIMAX_API_KEY` → MiniMax (`minimax-m2.7`) ⭐ **este es el activo en producción**
  4. `TOGETHER_API_KEY` → Llama 3 (`meta-llama/Llama-3-8b-chat-hf`)
- **Prioridad**: función `_detect_provider()` en `model_manager.py:88`.
- **¿Para qué sirve?**: Chat público (streaming y simple), clasificación de email, borradores de email.
- **¿Cuándo se activa?**: Cada vez que un usuario chatea o llega un email.
- **¿Cuánto cuesta?**: Depende del proveedor. MiniMax es el más barato (~$0.01-0.05 por conversación corta).

### Flujo de la IA en el chat

```
1. Usuario envía mensaje
   ↓
2. retrieve_from_silo() busca contexto en chunks
   ↓ (texto de referencia)
3. Se construye el prompt final:
   [system_prompt del modo]
   [CreatorMemory añadida]
   "CONTENIDO DE REFERENCIA: <chunks>"   (o "No se encontró contenido relevante")
   "Pregunta del usuario: <mensaje>"
   ↓
4. ModelManager.get_default_model_instance(tenant_id, ModelType.LLM)
   → detecta proveedor (MiniMax en prod)
   → _ModelInstance.invoke_llm_stream(prompt)
   ↓
5. Proveedor devuelve tokens uno a uno
   ↓
6. Flask los emite como SSE al navegador
   ↓
7. Al acabar: persiste conversation + message + analytics_question
   ↓
8. Usuario ve la respuesta token a token
```

### Funciones clave de IA

- `ModelManager.invoke_non_streaming()` (`model_manager.py:374`) → chat-simple y uso interno.
- `ModelManager.get_default_model_instance()` (`model_manager.py:395`) → chat streaming.
- `_dispatch()` / `_dispatch_stream()` (l.310, l.326) → enrutan al proveedor correcto.
- `_invoke_minimax()` / `_invoke_minimax_stream()` (l.260, l.286) → llamadas concretas.

### Parámetros configurables

**⚠️ IMPORTANTE**: este código **no setea `temperature` ni `max_tokens` explícitamente para OpenAI/MiniMax/Together**. Usa los defaults del proveedor. Solo Anthropic fija `max_tokens=2048` (l.181, l.206).

Si quieres controlar creatividad:

| Parámetro | Valor actual | Dónde cambiar | Cómo |
|---|---|---|---|
| `temperature` | default proveedor (≈1.0) | `model_manager.py:135` (dentro de `client.chat.completions.create`) | Añade `temperature=0.3,` para respuestas más deterministas |
| `max_tokens` | sin límite (OpenAI/MiniMax); 2048 (Anthropic) | Igual que arriba | Añade `max_tokens=512,` |
| `model` | `OPENAI_MODEL` / `ANTHROPIC_MODEL` / `MINIMAX_MODEL` / `TOGETHER_MODEL` | `.env` | Cambia la variable de entorno |

**Recomendación**: para clones educativos/de soporte, `temperature=0.2-0.4`. Para ventas conversacionales, `0.6-0.8`.

### Cómo cambiar el modelo de IA

**TAREA: Pasar de MiniMax a OpenAI GPT-4o-mini**

1. Consigue una API key en https://platform.openai.com/api-keys
2. Edita `ops/backend.env.production`:
   ```
   OPENAI_API_KEY=sk-...
   OPENAI_MODEL=gpt-4o-mini
   # OPENAI_BASE_URL=  (vacío para OpenAI real)
   ```
3. Como `_detect_provider()` revisa en ORDEN, basta con que `OPENAI_API_KEY` esté presente para que gane sobre MiniMax.
4. Reinicia: `docker compose -f ops/docker-compose.backend.prod.yml restart api`
5. Verifica:
   ```bash
   curl -X POST http://127.0.0.1:5001/api/myownclone/public/clones/miclone/chat-simple \
     -H "Content-Type: application/json" -d '{"message":"hola"}'
   # Debe devolver {"reply":"...","usage":{...}}
   ```
6. **Diferencias que notarás**: GPT-4o-mini es más rápido y preciso en español que MiniMax-m2.7, pero cuesta más por token.

**TAREA: Usar DeepSeek (barato y buen español)**

```
OPENAI_API_KEY=tu-key-de-deepseek
OPENAI_BASE_URL=https://api.deepseek.com
OPENAI_MODEL=deepseek-chat
```
(`OPENAI_API_BASE` también funciona como alias legacy.)

---

### El System Prompt — Las instrucciones secretas de la IA

**¿Qué es?**: Las instrucciones que se envían ANTES de la pregunta, para definir personalidad y límites.

**¿Dónde está?**: El sistema tiene **TRES fuentes de prompt**:

#### 1. Prompts por defecto por modo (`DEFAULT_PROMPTS`)
Archivo: `api/controllers/console/myownclone/clone.py:276`

Estos se asignan automáticamente al crear un clone, uno por cada silo:

```python
CloneSilo.TEACH: "Eres un asistente pedagógico amable y paciente. Tu objetivo es
   ayudar a los estudiantes a comprender el contenido del curso. Explica los conceptos
   de forma clara, usa ejemplos y anima a hacer preguntas. Basa tus respuestas
   ÚNICAMENTE en el contenido proporcionado. Si no tienes suficiente información,
   di claramente 'No tengo suficiente información para responder a eso'."

CloneSilo.SUPPORT: "Eres un agente de soporte eficiente y resolutivo. Tu objetivo es
   resolver dudas y problemas de los clientes de forma rápida y profesional. Si la
   consulta requiere atención humana, indícalo claramente y ofrece derivar al equipo
   de soporte. Basas tus respuestas en la documentación proporcionada."

CloneSilo.SALES: "Eres un asesor de ventas entusiasta pero no agresivo. Tu objetivo es
   ayudar a los clientes a encontrar el producto o servicio que mejor se adapte a sus
   necesidades. Destaca los beneficios, responde objeciones con honestidad y recomienda
   productos basándote en la información de catálogo proporcionada."
```

#### 2. Prompts personalizados (tabla `clone_mode_prompts`)
- Editables vía `PUT /api/clone/clones/<id>/prompts`.
- Se guardan en la columna `system_prompt`.
- Si un modo no tiene prompt activo, el chat cae a: `"Eres un asistente útil. Responde basándote en el contenido proporcionado."` (`myownclone_public.py:334`).

#### 3. Memorias del creador (tabla `creator_memory`)
- Antes de cada chat, `_add_memories_to_prompt()` (l.464) adjunta las memorias tipo `MEMORY` al system prompt.
- Formato: `"Información importante que debes recordar:\n- memoria1\n- memoria2"`.

**✅ Puedes cambiar**:
- Tono, longitud de respuesta, idioma, formalidad.
- Qué hacer cuando no hay contexto (decir "no sé" vs inventar).
- Reglas específicas del dominio.

**❌ No debes quitar**:
- La línea sobre "basarte en el contenido proporcionado" (sin ella, el LLM alucina fuera del conocimiento del clone).
- Las memorias del creador (rompe la personalización).

---

### Prompts de email (`api/core/myownclone/email_ai.py`)

#### `CLASSIFICATION_PROMPT` (l.29)
Clasifica email en `{category, urgency, summary, sentiment}`:
- category: `consulta|queja|venta|soporte|otro`
- urgency: `baja|normal|alta`
- Devuelve SOLO JSON.

#### `DRAFT_PROMPT` (l.46)
Redacta respuesta en el tono del creador:
- Usa `memory_context` (memorias + firma).
- Usa `template_context` (plantillas disponibles).
- Máximo 500 palabras, sin markdown/HTML.
- Devuelve JSON `{"subject":"...","body":"..."}`.

**Cómo modificarlos**: edita las constantes en `email_ai.py:29` y `email_ai.py:46`. Reinicia el backend. ⚠️ Mantén el formato JSON de salida o `_parse_json_response()` fallará.

---

# SECCIÓN 5: EMBEDDINGS — LA MEMORIA INTELIGENTE

## ⚠️ LEER ESTO PRIMERO: lo que el sistema llama "embeddings" NO lo es

### Analogía simple (la oficial)

Imagina que cada texto es una persona en una ciudad. Los embeddings ubican a cada persona en coordenadas (latitud/longitud). Textos similares quedan cerca. Cuando buscas algo, el sistema encuentra a las personas más cercanas.

### La realidad de este sistema

**No hay coordenadas geográficas reales.** Lo que hay es un **sistema de votación por palabras**:

1. Cada texto se trocea en palabras (quitando "el, la, de, que...").
2. Cada palabra genera un número pseudoaleatorio (hash FNV-1a).
3. Ese número decide en cuál de 1536 "cajas" (dimensiones) deposita un `+1` o `-1`.
4. Al final, el vector de 1536 cajas se normaliza (longitud = 1).

**Resultado**: dos textos que comparten palabras tendrán cajas en común → su producto punto (coseno) será alto. Pero **textos con significado similar y palabras distintas NO se encuentran**. Por ejemplo:

- "¿cuánto cuesta?" → encuentra textos con "precio", "tarifa" solo si esas palabras están literal.
- "¿cuánto vale?" → NO encuentra "precio" (palabras distintas, hash distinto).

### Esto significa

- ✅ **Bueno para**: búsquedas donde el usuario usa el mismo vocabulario que el contenido.
- ❌ **Malo para**: sinonimia, paráfrasis, preguntas abstractas.
- 💡 **Si quieres embeddings semánticos reales**, debes activar OpenAI `text-embedding-3-small` o similar (ver final de esta sección).

---

## Cómo funciona el sistema de "embeddings" en MyOwnClone

### 🔮 FASE 1 — INDEXACIÓN (cuando subes contenido)

**Ocurre en el FRONTEND Next.js**, no en Flask.
Archivo: `MyOwnClone/src/app/api/clone/sources/route.ts`

```
1. Usuario sube contenido (texto, PDF, URL YouTube, URL web)
   vía POST /api/clone/sources (con auth NextAuth)
   ↓
2. route.ts:145 POST handler:
   - Valida silo (teach/support/sales)
   - Valida type (pdf/youtube/text/web/interview)
   - Para texto: trocea (chunkText)
   ↓
3. chunkText() (route.ts:76):
   - Tamaño chunk: MAX_CHUNK_CHARS = 1200 caracteres
   - Overlap: CHUNK_OVERLAP_CHARS = 160 caracteres
   - Corta en fin de frase o doble salto de línea si está cerca del límite
   ↓
4. lexicalEmbedding() (route.ts:61):
   - EMBEDDING_DIMENSIONS = 1536
   - tokenize(): palabras de 3+ chars, quita STOPWORDS
   - hashTerm(): FNV-1a, signo +1/-1
   - Normaliza a vector unitario
   ↓
5. INSERT en tabla sources (status: "ready" si texto, "processing" si otro)
   INSERT en tabla chunks (content + embedding + metadata {position, silo})
```

⚠️ **Solo el tipo `text` se indexa automáticamente.** Para PDF, YouTube, web → el campo `metadata.ingestion` queda `pending_external_ingestion` y el contenido **no se indexa** (no hay ingester real implementado). Para que esos tipos funcionen, habría que implementar el extractor.

### 🔮 FASE 2 — BÚSQUEDA (cuando el usuario pregunta)

**Ocurre en el BACKEND Flask.**
Archivo: `api/core/retrieval.py`

```
1. chat_public() llama retrieve_from_silo() (retrieval.py:197)
   con: clone_id, query, silo, top_k=5, score_threshold=0.7
   ↓
2. retrieve_from_silo() intenta primero _retrieve_from_local_chunks() (retrieval.py:129)
   ↓
3. _retrieve_from_local_chunks():
   - Calcula query_terms = palabras de la pregunta (3+ chars, no stopwords)
   - Calcula query_embedding = _lexical_embedding(query) (mismo algoritmo FNV-1a)
   - SELECT chunks JOIN sources WHERE clone_id=? AND status='ready'
   - Por cada chunk:
       * Filtra por silo (metadata.silo)
       * Filtra por context_id si vino
       * term_score = _lexical_score() → cobertura de términos
       * vector_score = _cosine_similarity(query_embedding, chunk.embedding)
       * score = max(term_score, vector_score)
       * Si score < 0.7: descarta
   - Ordena por score desc, toma top_k=5
   ↓
4. Si local encontró: devuelve SiloRetrievalResult
   Si no: intenta legacy Dataset/DocumentSegment (que son stubs) → devuelve vacío
   ↓
5. Los chunks recuperados se formatean como contexto:
   "[Fuente 1] (relevancia: 0.85)
    <contenido del chunk>"
   ↓
6. Se inyectan en el prompt del LLM
```

### TECNOLOGÍA USADA (real)

| Componente | Valor | Archivo |
|---|---|---|
| "Modelo de embedding" | Hash léxico FNV-1a (hecho a mano) | `retrieval.py:82`, `route.ts:52` |
| Dimensiones del vector | 1536 | `retrieval.py:71`, `route.ts:8` |
| Base de datos vectorial | PostgreSQL (tabla `chunks`, columna `embedding vector(1536)`) | `models/knowledge.py:30` |
| Índice vectorial | ivfflat (pgvector) | `schema/chunks.ts:29` |
| Algoritmo de búsqueda | `max(term_score, cosine_similarity)` | `retrieval.py:168` |
| Stopwords | 36 palabras ES+EN | `retrieval.py:64`, `route.ts:9` |
| Weaviate | **CONFIGURADO PERO NO USADO** (stub) | `silos.py:31` |

---

## Gestión de la base de datos vectorial

### 🗄️ No hay BD vectorial separada

Los "vectores" viven en la misma PostgreSQL, en la tabla `chunks`. pgvector proporciona el tipo `vector(1536)` y el índice `ivfflat` para búsquedas rápidas.

### 📥 AGREGAR NUEVO CONTENIDO

**Solo texto por ahora:**
1. Entra al dashboard → /biblioteca → subir contenido.
2. O vía API:
   ```bash
   curl -X POST https://myownclone.com/api/clone/sources \
     -H "Cookie: <tu-cookie-nextauth>" \
     -F "silo=teach" -F "type=text" -F "content=Aquí va el texto a indexar..."
   ```
3. El sistema trocea, hashea y guarda. status="ready" inmediatamente.
4. Verifica:
   ```bash
   docker exec myownclone_postgres psql -U postgres -d myownclone \
     -c "SELECT id, title, status, metadata->>'wordCount' FROM sources ORDER BY created_at DESC LIMIT 5;"
   ```

### 🗑️ ELIMINAR CONTENIDO

```bash
# Borrar una fuente y sus chunks (ON DELETE CASCADE)
docker exec myownclone_postgres psql -U postgres -d myownclone \
  -c "DELETE FROM sources WHERE id = '<source_id>';"
```
⚠️ Esto borra en cascada todos los chunks (definido en `schema/sources.ts:33`). No hay undo sin backup.

### 🔄 RE-INDEXAR TODO

No hay comando automático. Para reindexar tras cambiar parámetros:

```bash
# 1. Backup primero
bash /opt/myownclone/current/ops/backup_postgres.sh

# 2. Borrar chunks (NO las sources)
docker exec myownclone_postgres psql -U postgres -d myownclone \
  -c "TRUNCATE chunks;"

# 3. Re-subir cada source desde el dashboard (no hay script batch)
#    O escribir un script que lea sources.content y regenere chunks.
```
⚠️ **Costo**: si mantienes el hash léxico, $0. Si cambias a OpenAI embeddings, ~$0.02 por millón de tokens.

### 🔍 VERIFICAR QUÉ HAY INDEXADO

```bash
docker exec myownclone_postgres psql -U postgres -d myownclone -c "
  SELECT s.title, s.status, count(c.id) as chunks,
         s.metadata->>'silo' as silo
  FROM sources s LEFT JOIN chunks c ON c.source_id = s.id
  GROUP BY s.id ORDER BY s.created_at DESC;
"
```

### Cómo cambiar a embeddings REALES (OpenAI)

**⚠️ Requiere reindexar TODO.**

1. Modifica `MyOwnClone/src/app/api/clone/sources/route.ts`:
   - Reemplaza `lexicalEmbedding(chunk)` por una llamada a OpenAI:
   ```typescript
   async function openaiEmbedding(text: string): Promise<number[]> {
     const res = await fetch("https://api.openai.com/v1/embeddings", {
       method: "POST",
       headers: { Authorization: `Bearer ${process.env.OPENAI_API_KEY}`, "Content-Type": "application/json" },
       body: JSON.stringify({ model: "text-embedding-3-small", input: text }),
     });
     return (await res.json()).data[0].embedding;
   }
   ```
2. Haz lo mismo en `api/core/retrieval.py` (`_lexical_embedding` → llamada OpenAI).
3. Reindexa todo (borra chunks, re-sube).
4. Las dimensiones de `text-embedding-3-small` son 1536 → coincide con el esquema actual.
5. ⏰ Tiempo: ~1 min por 100KB de texto. 💰 Costo: ~$0.02 por millón de tokens.

---

## Parámetros de búsqueda semántica que puedes ajustar

| Parámetro | Valor actual | Archivo | Efecto |
|---|---|---|---|
| `CHUNK_SIZE` (chars) | **1200** | `route.ts:6` (`MAX_CHUNK_CHARS`) | Más grande = más contexto por chunk pero búsquedas menos precisas |
| `CHUNK_OVERLAP` (chars) | **160** | `route.ts:7` (`CHUNK_OVERLAP_CHARS`) | Cuánto texto se repite entre chunks; evita cortar ideas |
| `_EMBEDDING_DIMENSIONS` | **1536** | `retrieval.py:71` | Tamaño del vector. ⚠️ Cambiarlo requiere regenerar TODO y migrar el esquema. |
| `TOP_K` | **5** | `myownclone_public.py:347` | Cuántos chunks recuperar. Más alto = más contexto = más tokens = más costo |
| `SCORE_THRESHOLD` | **0.7** | `myownclone_public.py:348` | Mínima similitud para mostrar. 0.0=permisivo, 1.0=estricto |
| `_STOPWORDS` | 36 palabras | `retrieval.py:64` | Palabras ignoradas al tokenizar |
| `_CHAT_LIMIT` | 20/60s | `myownclone_public.py:46` | Rate limit chat público |

**Recomendaciones**:
- Si las respuestas son pobres → baja `SCORE_THRESHOLD` a 0.5 o sube `TOP_K` a 8.
- Si las respuestas son costosas → baja `TOP_K` a 3 y sube `SCORE_THRESHOLD` a 0.8.
- Si trozos cortan ideas → sube `CHUNK_OVERLAP` a 200.

---

# SECCIÓN 6: BASE DE DATOS — LA MEMORIA DEL SISTEMA

## Visión general

- **Motor**: PostgreSQL 15.18 + pgvector 0.8.2 + uuid-ossp 1.1
- **Contenedor**: `myownclone_postgres` (imagen `pgvector/pgvector:pg15`)
- **Tamaño actual**: ~9 MiB (datos seed)
- **Conexiones**: 8 máx, sin saturación
- **Migración head**: `c3d4e5f6a7c1` (habilita `CREATE EXTENSION vector`)
- **Editor recomendado**: Drizzle Studio (`npm run db:studio`) o `psql`

## Multi-tenancy

Cada tabla de negocio tiene `clone_id` y/o `tenant_id`. El aislamiento se hace por filtro en cada query (no por RLS de Postgres). **Cualquier query nueva debe incluir `WHERE tenant_id = ?`** o será un fallo cross-tenant.

## Mapa completo de tablas

### 📊 `tenants`
- **¿Para qué?**: Raíz multi-tenant. Cada cuenta de cliente = un tenant.
- **Columnas**: `id` (uuidv7), `name`, `slug` (único), `plan` (trial/basic/pro/scale/enterprise), `status`, `subscription_status`, `stripe_customer_id`, `stripe_subscription_id`, `trial_ends_at`, `created_at`, `updated_at`.
- **No borrar**: el tenant con tu cuenta activa (rompe todo el dashboard).

### 📊 `accounts` (canónica) y `users` (legacy)
- **¿Para qué?**: Usuarios. `accounts` la crean las migraciones Alembic; `users` es de Drizzle/NextAuth.
- **`accounts`**: `id`, `tenant_id` (FK→tenants), `email` (único), `password` (bcrypt hash), `name`, `avatar`, `role` (owner/admin/member/platform_admin), `status`, `is_platform_admin` (bool), `last_login_at`, timestamps.
- **El login** busca primero en `accounts` y cae a `users` si la tabla no existe.
- **Registros críticos**: cualquier fila con `is_platform_admin=true`.

### 📊 `clone_configs`
- **¿Para qué?**: Cada clone digital.
- **Columnas**: `id`, `tenant_id`, `name`, `slug` (único), `description`, `avatar_url`, `personality_tone`, `language` (default "es"), `custom_domain`, `active_modes` (array de silos), `is_active`.
- **Relación**: N clones por tenant.

### 📊 `clone_mode_prompts`
- **¿Para qué?**: El system prompt de cada modo (teach/support/sales) por clone.
- **Columnas**: `id`, `clone_id`, `mode`, `system_prompt` (TEXT), `is_active`.
- **Se crean 3 filas automáticamente** al crear un clone (`clone.py:130`).

### 📊 `sources` ⭐ (base de conocimiento)
- **¿Para qué?**: Documentos subidos para entrenar el clone.
- **Columnas**: `id` (text UUID), `clone_id`, `type` (youtube/pdf/video/text/web/interview), `title`, `url`, `status` (uploading/processing/ready/error), `metadata` (JSON: silo, wordCount, chunkCount, ingestion), timestamps.
- **Índices**: `sources_clone_id_idx`, `sources_status_idx`.

### 📊 `chunks` ⭐ (los "embeddings")
- **¿Para qué?**: Fragmentos de texto con su vector léxico.
- **Columnas**: `id`, `source_id` (FK→sources, CASCADE), `content` (TEXT), `embedding` (`vector(1536)`), `token_count`, `metadata` (JSON: position, silo).
- **Índices**: `chunks_source_id_idx`, `chunks_embedding_idx` (ivfflat).
- **⚠️ El tipo `vector`** es de pgvector. Si la extensión no está cargada, todo falla.

### 📊 `conversations` y `messages`
- **`conversations`**: `id`, `clone_id`, `visitor_id` (hash IP+UA), `mode`, `created_at`.
- **`messages`**: `id`, `conversation_id`, `role` (user/assistant), `content`, `confidence`, `sources` (JSON), `feedback`, `created_at`.

### 📊 `meeting_types`, `availability`, `bookings`
- **`meeting_types`**: `id`, `clone_id`, `name`, `duration_minutes`, `price_cents`, `description`, `color`, `active`.
- **`availability`**: `id`, `clone_id`, `day_of_week` (0-6), `start_time`, `end_time`, `buffer_minutes`.
- **`bookings`**: `id`, `meeting_type_id`, `visitor_name`, `visitor_email`, `date`, `start_time`, `end_time`, `status`, `meeting_url`, `recording_url`, `transcript`, `notes`.

### 📊 `products`
- Catálogo del clone: `id`, `clone_id`, `name`, `description`, `price_cents`, `url`, `image_url`, `priority`, `active`.

### 📊 `creator_memory`
- **¿Para qué?**: Memorias/firmas/plantillas que enriquecen el system prompt y los borradores de email.
- **Columnas**: `id`, `clone_id`, `type` (memory/signature/template), `content`, `trigger_condition`, `priority`.

### 📊 `email_inbound` y `email_templates`
- **`email_inbound`**: emails recibidos vía SendGrid. `id`, `clone_id`, `from_email`, `from_name`, `subject`, `body_text`, `body_html`, `draft_reply`, `status`, `labels`, `classification`, `thread_id`, `received_at`, `responded_at`.
- **`email_templates`**: plantillas para borradores. `id`, `clone_id`, `name`, `subject`, `body`, `trigger_keywords`.

### 📊 `analytics_questions` y `analytics_gaps`
- **`analytics_questions`**: conteo de preguntas frecuentes. `id`, `clone_id`, `question`, `count`, `last_asked_at`.
- **`analytics_gaps`**: huecos de conocimiento detectados. `id`, `clone_id`, `question`, `count`, `suggested_source`, `status` (open/resolved).

### 📊 `cost_tracking`
- **¿Para qué?**: Registro de costos por tenant.
- **Columnas**: `id`, `tenant_id`, `category` (clone_response/content_ingestion/platform_ops), `operation`, `model`, `tokens_in`, `tokens_out`, `cost_cents`, `created_at`.
- **⚠️ Actualmente poco poblado** porque el ModelManager no inserta filas en cada llamada. Para tener datos reales, habría que añadir el INSERT en `_dispatch()`.

### 📊 `myownclone_plans`
- **¿Para qué?**: Definición de planes y precios. Seed por migración `c3d4e5f6a7b8`.
- **Columnas**: `id`, `name`, `price_cents`, `stripe_price_id`, `words_training_limit`, `responses_month_limit`, `modes_active`, flags de features (`email_triage`, `booking`, `api_access`, `multi_clone`, `whitelabel`).

### 📊 `impersonation_log` y `impersonation_tokens`
- **`impersonation_log`**: auditoría de impersonaciones admin→tenant. `id`, `admin_id`, `tenant_id`, `reason`, `started_at`, `ended_at`.
- **`impersonation_tokens`**: tokens hasheados (SHA-256 + pepper). `id`, `token` (hash), `admin_id`, `tenant_id`, `expires_at`, `created_at`.
- **⚠️ El pepper** (`IMPERSONATION_TOKEN_PEPPER`) si se rota invalida TODOS los tokens activos.

### 📊 `clone_feedback`
- Thumbs up/down en respuestas. `id`, `clone_id`, `conversation_id`, `message_id`, `rating` (up/down), `comment`, timestamps.

### Diagrama de relaciones (simplificado)

```
tenants (1) ──< accounts (N)
         └──< clone_configs (N) ──< clone_mode_prompts
                                  ├──< sources ──< chunks
                                  ├──< conversations ──< messages
                                  ├──< meeting_types ──< bookings
                                  ├──< availability
                                  ├──< products
                                  ├──< creator_memory
                                  ├──< email_inbound
                                  ├──< email_templates
                                  ├──< analytics_questions
                                  ├──< analytics_gaps
                                  └──< clone_feedback
cost_tracking (tenant_id)
myownclone_plans (sin FK, catálogo)
impersonation_log, impersonation_tokens (admin_id→accounts)
```

---

## Cómo hacer operaciones en la base de datos

### ⚠️ REGLAS DE ORO

1. **SIEMPRE haz backup antes** de tocar producción.
2. **NUNCA ejecutes DELETE/UPDATE sin WHERE**.
3. **Si borras algo sin backup, es permanente.**

### BACKUP MANUAL

```bash
# Script del repo (rotación 7 días)
bash /opt/myownclone/current/ops/backup_postgres.sh 7
# → /opt/myownclone/backups/myownclone_YYYYMMDD_HHMMSS.sql.gz
```

### RESTAURAR

```bash
gunzip < /opt/myownclone/backups/myownclone_YYYYMMDD_HHMMSS.sql.gz | \
  docker exec -i myownclone_postgres psql -U postgres -d myownclone
```

### VER LOS DATOS (solo lectura)

```bash
# Entrar al cliente
docker exec -it myownclone_postgres psql -U postgres -d myownclone

# Ver tablas
\dt

# Ver schema de una tabla
\d clone_configs

# Ver 10 clones
SELECT id, name, slug, is_active FROM clone_configs LIMIT 10;

# Contar chunks por clone
SELECT c.name, count(ch.id) FROM clone_configs c
  LEFT JOIN sources s ON s.clone_id = c.id
  LEFT JOIN chunks ch ON ch.source_id = s.id
  GROUP BY c.name;

# Salir
\q
```

### MIGRACIONES (Alembic)

```bash
# Estado actual
docker exec myownclone_api flask --app app_factory db current

# Aplicar pendientes
docker exec myownclone_api flask --app app_factory db upgrade

# Rollback una migración
docker exec myownclone_api flask --app app_factory db downgrade -1
```

⚠️ Para bases preexistentes sin `alembic_version`, haz backup y luego `flask db stamp head` (marca como aplicadas sin ejecutarlas).

---

# SECCIÓN 7: VARIABLES DE ENTORNO — EL PANEL DE CONTROL

## Resumen de archivos

- **Backend**: `ops/backend.env.production` (en VPS: `/opt/myownclone/shared/backend.env.production`).
- **Frontend**: `MyOwnClone/.env.production` (generado desde `/opt/myownclone/shared/frontend.env.production`).
- **Plantillas**: `ops/backend.env.production.example`, `ops/frontend.env.production.example`.

> ⚠️ **NUNCA subas los `.env` reales a Git.** Solo los `.example` (sin secretos) están versionados.

---

## El `.env` del BACKEND explicado línea por línea

### ── Obligatorios (fail-fast si son "change-me") ──

```
DB_PASSWORD=change-me
```
- **¿Para qué?**: Password del usuario postgres de la BD.
- **¿Vacía?**: `assert_production_secrets()` aborta el arranque.
- **¿Incorrecta?**: Error de conexión a la BD.
- **Sensible**: Sí.
- **Dónde conseguirla**: la generas tú con `openssl rand -base64 24`. Debe coincidir con `POSTGRES_PASSWORD` del compose.

```
REDIS_PASSWORD=change-me
```
- **¿Para qué?**: Password de Redis.
- **Rechazada si**: es `changeit`, `dev_password_123`, o vacía (en producción).
- **Sensible**: Sí.

```
JWT_SECRET_KEY=change-me-min-32-chars-randomly-generated
```
- **¿Para qué?**: Firma los JWT de `/console/api/auth/login`.
- **Mínimo**: 32 caracteres. Si no, RuntimeError.
- **⚠️ Si la cambias**: todos los JWT emitidos quedan inválidos (los usuarios deben re-login).
- **Generar**: `python -c "import secrets; print(secrets.token_urlsafe(64))"`

```
IMPERSONATION_TOKEN_PEPPER=change-me-min-32-chars-randomly-generated
```
- **¿Para qué?**: Pepper para hashear tokens de impersonación (SHA-256 + pepper).
- **⚠️ Si la cambias**: todos los tokens de impersonación activos quedan inválidos.

### ── Conexión ──

```
DB_USER=postgres
DB_HOST=127.0.0.1          # en Docker: db_postgres
DB_PORT=5432
DB_NAME=myownclone
DATABASE_URL=postgresql+psycopg://postgres:PWD@127.0.0.1:5432/myownclone
```
- **Prioridad**: si `DATABASE_URL` está seteada, gana. `_database_uri()` (l.91) convierte `postgresql+psycopg://` a `postgresql://` para psycopg2.

### ── Flask runtime ──

```
FLASK_ENV=production       # o "development"
LOG_LEVEL=INFO             # DEBUG/INFO/WARNING/ERROR
SECRET_KEY=change-me       # Flask session signing
```

### ── CORS ──

```
ALLOWED_ORIGINS=https://myownclone.example.com
```
- **¿Para qué?**: Orígenes permitidos para CORS. Separados por coma, sin espacios.
- **Dev default**: `http://localhost:3000, http://127.0.0.1:3000`.
- **⚠️ En producción**: debe ser SOLO tu dominio público.

### ── Service-to-service ──

```
SERVICE_API_KEY=change-me
ALLOW_DEV_SERVICE_KEY=false
```
- **`SERVICE_API_KEY`**: clave mutua frontend↔backend. **DEBE SER IDÉNTICA** en backend y frontend.
- **`ALLOW_DEV_SERVICE_KEY=false`**: en producción debe ser false. Si true, acepta `dev-api-key-for-proxy` (peligroso).

### ── LLM (al menos uno) ──

```
OPENAI_API_KEY=            # prioridad 1
OPENAI_BASE_URL=           # para DeepSeek: https://api.deepseek.com
OPENAI_API_BASE=           # alias legacy
OPENAI_MODEL=gpt-4o-mini

ANTHROPIC_API_KEY=         # prioridad 2
ANTHROPIC_MODEL=claude-3-haiku-20240307

MINIMAX_API_KEY=           # prioridad 3 (activo en prod)
MINIMAX_MODEL=minimax-m2.7

TOGETHER_API_KEY=          # prioridad 4
TOGETHER_MODEL=meta-llama/Llama-3-8b-chat-hf
```
- **Si ninguno está seteado**: chat devuelve 502 `model_unavailable`.

### ── Integraciones opcionales ──

```
WEAVIATE_API_KEY=
WEAVIATE_URL=http://weaviate:8080     # dormido en runtime

STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=                # esta va en el FRONTEND
SENDGRID_INBOUND_WEBHOOK_SECRET=
WHEREBY_API_KEY=
RESEND_API_KEY=
RESEND_FROM_EMAIL=noreply@myownclone.example.com
```

### ── URL pública ──

```
APP_URL=https://myownclone.example.com
```

---

## El `.env` del FRONTEND explicado

### ── Runtime ──

```
NODE_ENV=production
PORT=3000
HOSTNAME=127.0.0.1
```

### ── Base de datos (Drizzle/NextAuth) ──

```
DATABASE_URL=postgresql://postgres:PWD@127.0.0.1:5432/myownclone
```
⚠️ La misma BD que el backend, pero con formato `postgresql://` (sin `+psycopg`).

### ── Conexión al backend ──

```
MYOWNCLONE_API_URL=http://127.0.0.1:5001
DEFAULT_CLONE_ID=                       # fallback si no hay cookie
DEFAULT_PLAN=trial
```

### ── Auth.js / NextAuth ──

```
AUTH_URL=https://myownclone.com          # URL pública canónica
NEXTAUTH_URL=https://myownclone.com      # alias
AUTH_TRUST_HOST=true                     # detrás de nginx
AUTH_SECRET=<openssl-rand-hex-32>        # firma JWT NextAuth
NEXTAUTH_SECRET=<igual que AUTH_SECRET>  # alias legacy
```
⚠️ `AUTH_SECRET` y `NEXTAUTH_SECRET` deben ser el mismo valor.

### ── Admin bootstrap (emergencia) ──

```
PLATFORM_ADMIN_EMAIL=admin@example.com
PLATFORM_ADMIN_PASSWORD_HASH=$2b$12$...   # bcrypt
```
- **¿Para qué?**: Login de admin cuando no hay tabla `users` funcional.
- **Generar hash**:
  ```bash
  node -e 'require("bcryptjs").hash(process.argv[1], 12).then(console.log)' "tu-password"
  ```
- **⚠️ Solo se inyecta vía systemd EnvironmentFile**, no llega al `.env.production` de Next.js (lo filtra `deploy-frontend.sh:113`).

### ── OAuth y APIs ──

```
AUTH_GOOGLE_ID=
AUTH_GOOGLE_SECRET=
RESEND_API_KEY=
RESEND_FROM_EMAIL=noreply@myownclone.local

NEXT_PUBLIC_APP_URL=https://myownclone.com
NEXT_PUBLIC_API_URL=https://myownclone.com:5001
NEXT_PUBLIC_ADMIN_URL=https://myownclone.com/admin
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=

STRIPE_BASIC_PRICE_ID=
STRIPE_PRO_PRICE_ID=
STRIPE_SCALE_PRICE_ID=

ANTHROPIC_API_KEY=
OPENAI_API_KEY=                          # para STT (Whisper)

SUPABASE_URL=                            # opcional
SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=

NEXT_PUBLIC_POSTHOG_KEY=                 # telemetría (vacío = no envía)
NEXT_PUBLIC_POSTHOG_HOST=
NEXT_PUBLIC_SENTRY_DSN=                  # errores (vacío = no envía)
SENTRY_ORG=
SENTRY_PROJECT=
```

---

## Cómo agregar una nueva variable de entorno

1. **Backend**: añade a `ops/backend.env.production` (y `.example` con descripción).
2. **Frontend**: añade a `/opt/myownclone/shared/frontend.env.production` y a `ops/frontend.env.production.example`.
3. **En el código**:
   - Python: `valor = os.getenv("NUEVA_VAR", "default")`
   - TypeScript: `process.env.NUEVA_VAR`
4. **Si es del backend**: añádeala a `environment:` del servicio `api` en `ops/docker-compose.backend.prod.yml` (o depende del `env_file`).
5. **Reinicia**: backend → `docker compose ... restart api`; frontend → `sudo systemctl restart myownclone-frontend`.
6. **⚠️ Variables `NEXT_PUBLIC_*`** se incrustan en el bundle del navegador al hacer `npm run build`. Cambiarlas requiere redeploy del frontend, no solo reiniciar.

---

# SECCIÓN 8: EL SERVIDOR VPS — CÓMO MANTENERLO VIVO

## Datos del VPS de producción

| Item | Valor |
|---|---|
| Hostname | `ubuntu` / Ubuntu 26.04 LTS |
| IP pública | `212.227.169.99` |
| IP Tailscale | `100.125.128.116` |
| Acceso SSH | `ssh root@212.227.169.99` o `ssh myownclone-vps` (config Tailscale) |
| CPU / RAM | 2 vCPU AMD EPYC / 3.8 GiB |
| Disco | 116 GiB en `/` (36% usado) |
| Dominio | `myownclone.com` |

## 🖥️ COMANDOS ESENCIALES DEL DÍA A DÍA

### ENTRAR AL SERVIDOR

```bash
# Desde tu máquina, por IP pública (solo llave tras hardening)
ssh root@212.227.169.99

# O por Tailscale (más seguro)
ssh myownclone-vps
```

### VER SI TODO ESTÁ FUNCIONANDO

```bash
# Estado de contenedores del backend
docker compose -f /opt/myownclone/current/ops/docker-compose.backend.prod.yml ps
# Debes ver: myownclone_api, myownclone_postgres, myownclone_redis, myownclone_weaviate  → "healthy"

# Estado del frontend (systemd)
sudo systemctl status myownclone-frontend
# Debes ver: "active (running)"

# Healthchecks
curl -s http://127.0.0.1:5001/healthz   # → {"status":"ok"}
curl -s http://127.0.0.1:5001/readyz    # → {"status":"ready","checks":{...}}
curl -sI https://myownclone.com         # → HTTP/2 200

# Smoke test completo
bash /opt/myownclone/current/ops/smoke-prod.sh
```

### REINICIAR EL SISTEMA

```bash
# Backend (Flask)
docker compose -f /opt/myownclone/current/ops/docker-compose.backend.prod.yml restart api

# Base de datos
docker compose -f /opt/myownclone/current/ops/docker-compose.backend.prod.yml restart db_postgres

# Redis
docker compose -f /opt/myownclone/current/ops/docker-compose.backend.prod.yml restart redis

# Frontend (Next.js)
sudo systemctl restart myownclone-frontend

# nginx
sudo systemctl reload nginx

# TODO el backend (emergencia)
docker compose -f /opt/myownclone/current/ops/docker-compose.backend.prod.yml down
docker compose -f /opt/myownclone/current/ops/docker-compose.backend.prod.yml up -d
```

### VER LOS LOGS

```bash
# Logs del backend (Flask/gunicorn)
docker logs -f --tail 100 myownclone_api

# Logs de errores del backend (solo stderr)
docker logs myownclone_api 2>&1 | grep -i error

# Logs del frontend (Next.js, journalctl)
sudo journalctl -u myownclone-frontend -f --no-pager

# Logs de nginx (acceso)
sudo tail -f /var/log/nginx/access.log

# Logs de nginx (errores)
sudo tail -f /var/log/nginx/error.log

# Logs de PostgreSQL
docker logs myownclone_postgres

# Backups
tail -f /var/log/myownclone-backup.log
```

**Cómo interpretar un error típico**:
```
[ERROR] ModelInvocationError: No LLM API key configured
→ falta MINIMAX_API_KEY u otra. Revisa backend.env.production.

[CRITICAL] RuntimeError: JWT_SECRET_KEY must be set
→ JWT_SECRET_KEY vacío o < 32 chars.

sqlalchemy.exc.OperationalError: could not connect to server
→ PostgreSQL caído o credenciales mal.
```

### ACTUALIZAR EL CÓDIGO (DEPLOY)

#### Opción A: Deploy desde tu máquina (recomendado para cambios controlados)

```bash
# Backend (desde local)
bash ops/deploy-backend.sh
# Sube código por rsync, reconstruye la imagen, reinicia el contenedor.
# Variables: HOST, SSH_USER, SSH_PORT, BACKEND_ENV_FILE, RELEASE_ID.

# Frontend (desde local)
bash ops/deploy-frontend.sh
# Sube código, npm install, npm run build, reinicia systemd.
```

#### Opción B: Restaurar/deploy desde GitHub en el propio VPS

```bash
# En el VPS
BRANCH=master bash /opt/myownclone/current/ops/restore-from-github-on-vps.sh
# Hace fetch de GitHub, build, activa release, levanta backend y frontend.
```

#### Opción C: Deploy vía webhook CI/CD

```bash
curl -X POST https://myownclone.com/api/deploy \
  -H "X-Deploy-Secret: $DEPLOY_SECRET"
```
Solo actualiza el frontend (`git pull` + `npm build` + `systemctl restart`).

### VER USO DE RECURSOS

```bash
# CPU y RAM en tiempo real
htop
# o:
docker stats --no-stream

# Espacio en disco
df -h
# Preocúpate si / > 90%

# Tamaño de releases acumulados
du -sh /opt/myownclone/releases/*

# Tamaño de volúmenes Docker
docker system df

# Conexiones a PostgreSQL
docker exec myownclone_postgres psql -U postgres -d myownclone \
  -c "SELECT count(*) FROM pg_stat_activity;"
```

---

## Proceso completo de actualización (DEPLOY SEGURO)

### Antes de empezar

```
□ ¿Hice backup de la BD?         → bash /opt/myownclone/current/ops/backup_postgres.sh
□ ¿Guardé el .env actual?        → cp /opt/myownclone/shared/backend.env.production /root/env-backup-$(date +%F).env
□ ¿Es horario de bajo tráfico?   → Recomendado: madrugada
□ ¿Probé localmente?             → pytest -q && cd MyOwnClone && npm run test
```

### Proceso (backend)

```bash
# 1. Sube el código
bash ops/deploy-backend.sh
#   (rsync → symlink current → docker compose up -d --build)

# 2. Verifica que responde
curl -s http://127.0.0.1:5001/readyz

# 3. Si hay migraciones nuevas
docker exec myownclone_api flask --app app_factory db upgrade

# 4. Revisa logs 5 min
docker logs -f --tail 50 myownclone_api
```

### Proceso (frontend)

```bash
bash ops/deploy-frontend.sh
#   (rsync → npm install → npm run build → systemctl restart)

curl -sI http://127.0.0.1:3000/   # → 200
```

### Si algo sale mal (ROLLBACK)

```bash
# Listar releases
ls -lt /opt/myownclone/releases/

# Apuntar current a la versión anterior
ln -sfn /opt/myownclone/releases/<RELEASE_ANTERIOR> /opt/myownclone/current

# Reiniciar servicios
sudo systemctl restart myownclone-frontend
docker compose -f /opt/myownclone/current/ops/docker-compose.backend.prod.yml up -d

# Restaurar BD si la migración la rompió
gunzip < /opt/myownclone/backups/myownclone_YYYYMMDD_HHMMSS.sql.gz | \
  docker exec -i myownclone_postgres psql -U postgres -d myownclone
```

---

## Estado actual del VPS (post-hardening 2026-06-19)

| Control | Estado |
|---|---|
| HTTPS `https://myownclone.com/` | ✅ 200, cert Let's Encrypt (vence 2026-09-13) |
| Backend `/healthz`, `/readyz` | ✅ ok / ready |
| Contenedores | ✅ 4/4 healthy |
| Security headers | ✅ HSTS, X-Frame, X-Content-Type, Referrer, Permissions |
| Puerto 9999 | ✅ cerrado |
| Puerto 3000 al exterior | ✅ bloqueado por UFW |
| SSH | ✅ prohibit-password, PasswordAuth no |
| fail2ban | ✅ activo |
| Backups | ✅ cron diario 03:00 + rotación 7 días |
| LLM configurado | MiniMax (los demás vacíos) |
| Stripe/SendGrid/OpenAI/Whereby | ❌ vacíos (no operativos) |

---

# SECCIÓN 9: COSTOS Y CONSUMO — LO QUE TE CUESTA CADA MES

## 💰 MAPA DE COSTOS DEL SISTEMA

### SERVICIO: MiniMax (LLM activo)
- **Costo base**: $0/mes (pay-per-use)
- **Costo por uso**: ~$0.001-0.01 por mensaje de chat (depende de longitud)
- **Dónde ver consumo**: https://platform.minimaxi.com/
- **Cómo reducir**: baja `TOP_K` (menos contexto), acorta system prompts, cachea respuestas frecuentes.

### SERVICIO: VPS (Ionos / proveedor)
- **Costo base**: ~€10-20/mes (2 vCPU, 4GB RAM)
- **Incluido**: todo el stack (nginx, Next.js, Flask, Postgres, Redis, Weaviate)
- **Dónde ver**: panel de tu proveedor cloud

### SERVICIO: PostgreSQL (autohospedado)
- **Costo**: $0 (incluido en VPS)

### SERVICIO: SendGrid (email inbound)
- **Costo base**: $0 (free tier: 100 emails/día)
- **Dónde ver**: https://app.sendgrid.com/

### SERVICIO: Stripe
- **Costo base**: $0
- **Por transacción**: 1.5% + €0.25 (Europa)
- **Dónde ver**: https://dashboard.stripe.com/

### SERVICIO: Resend (email transaccional)
- **Costo base**: $0 (free: 3000/mes)
- **Dónde ver**: https://resend.com/

### ESTIMADO TOTAL MENSUAL

- **Tráfico bajo** (< 1000 chats): **~€15-25/mes** (VPS + algo de MiniMax)
- **Tráfico medio** (10k chats): **~€30-50/mes**
- **Tráfico alto** (100k chats): **~€100-200/mes**

## CÓMO CONTROLAR COSTOS DE IA

El sistema registra costos en la tabla `cost_tracking` (aunque actualmente el ModelManager no inserta filas automáticamente). Para ver lo que hay:

```sql
SELECT category, sum(cost_cents) as total_cents, count(*) as calls
FROM cost_tracking WHERE created_at > now() - interval '30 days'
GROUP BY category;
```

### Palancas de ahorro (de más a menos impacto)

1. **Cambiar a modelo más barato**: MiniMax ya es barato; Together.ai (Llama 3) suele ser más barato aún.
2. **Reducir `TOP_K`** de 5 → 3: ahorra ~40% de tokens de contexto por mensaje.
   - Archivo: `myownclone_public.py:347`
3. **Acortar system prompts**: los `DEFAULT_PROMPTS` son ~400 tokens cada uno.
4. **Añadir `max_tokens=512`** en `model_manager.py:135` (OpenAI/MiniMax no lo setea ahora).
5. **Cachear respuestas** a preguntas frecuentes (requiere implementación; la tabla `analytics_questions` ya las agrupa).
6. **Implementar guard de costos**: antes de llamar al LLM, comprobar `tenant.responses_month_limit` (campo en `myownclone_plans`, hoy no enforceado).

### Configurar alertas de billing

- **MiniMax**: la plataforma envía alertas por email cuando se acerca a un umbral.
- **OpenAI**: https://platform.openai.com/account/billing/limits → set hard limit.
- **Stripe**: https://dashboard.stripe.com/settings/notifications

---

# SECCIÓN 10: SOLUCIÓN DE PROBLEMAS TÉCNICOS

---

### ❌ PROBLEMA: "El chat no responde / responde con error"

**¿Qué ves?**: En el navegador, el chat muestra "Lo siento, ha ocurrido un error..." o no carga.
**¿Dónde aparece?**: navegador, logs del backend.

🔍 **DIAGNÓSTICO**:
1. Revisa logs: `docker logs --tail 50 myownclone_api 2>&1 | grep -i "ModelInvocation\|Error"`
2. Verifica que hay un proveedor configurado:
   ```bash
   grep -E "MINIMAX_API_KEY|OPENAI_API_KEY|ANTHROPIC_API_KEY|TOGETHER_API_KEY" \
     /opt/myownclone/shared/backend.env.production
   ```
3. Prueba el chat-simple:
   ```bash
   curl -X POST http://127.0.0.1:5001/api/myownclone/public/clones/<slug>/chat-simple \
     -H "Content-Type: application/json" -d '{"message":"hola"}'
   ```

💡 **SOLUCIÓN**:
- Si `model_unavailable` (502): no hay API key → rellena una en `.env` y `docker compose ... restart api`.
- Si `401`/`403` del proveedor: key inválida o sin saldo → rota la key.
- Si timeout: proveedor caído → prueba otro proveedor cambiando el orden de keys.

✅ **VERIFICAR**: el chat responde con `{"reply":"...","usage":{...}}`.

---

### ❌ PROBLEMA: "401 Unauthorized en /api/clone/* del dashboard"

**¿Qué ves?**: El dashboard no carga datos, errores 401 en consola del navegador.

🔍 **DIAGNÓSTICO**:
1. Compara `SERVICE_API_KEY` en backend y frontend:
   ```bash
   grep SERVICE_API_KEY /opt/myownclone/shared/backend.env.production
   grep -E "SERVICE_API_KEY|MYOWNCLONE_SERVICE_API_KEY" /opt/myownclone/shared/frontend.env.production
   ```
2. Revisa que `ALLOW_DEV_SERVICE_KEY=false` en producción.
3. Verifica tu sesión NextAuth (¿te logueaste?).

💡 **SOLUCIÓN**:
- Si difieren: pon el mismo valor en ambos y reinicia frontend (`systemctl restart myownclone-frontend`) y backend (`docker compose ... restart api`).
- Si `ALLOW_DEV_SERVICE_KEY=true` en prod: cámbialo a `false`.

---

### ❌ PROBLEMA: "La IA responde cosas que no están en mi contenido"

**¿Qué ves?**: El clone alucina o responde fuera de tema.

🔍 **DIAGNÓSTICO**:
1. Revisa el system prompt del modo: `SELECT mode, system_prompt FROM clone_mode_prompts WHERE clone_id=?`
2. Comprueba que incluye "basarte en el contenido proporcionado".
3. Verifica que hay chunks: `SELECT count(*) FROM chunks ch JOIN sources s ON s.id=ch.source_id WHERE s.clone_id=?`

💡 **SOLUCIÓN**:
- Restaura la línea anti-alucinación en el prompt.
- Si `chunks=0`: sube contenido en `/biblioteca`.
- Baja `temperature` en `model_manager.py` (añade `temperature=0.3`).

✅ **VERIFICAR**: pregunta algo fuera de tema → debe decir "no tengo información".

---

### ❌ PROBLEMA: "Weaviate aparece unhealthy"

**¿Qué ves?**: `docker compose ps` muestra `myownclone_weaviate (unhealthy)`.

🔍 **DIAGNÓSTICO**:
1. `docker logs myownclone_weaviate | tail -30`
2. La imagen 1.24.0 **no tiene curl**, solo wget. El healthcheck debe usar `wget`.

💡 **SOLUCIÓN**:
- El compose actual ya usa wget (l.72). Si tu compose es viejo, actualízalo:
  ```yaml
  healthcheck:
    test: ["CMD-SHELL", "wget -qO- http://localhost:8080/v1/.well-known/ready >/dev/null 2>&1 || exit 1"]
  ```
- **No afecta al funcionamiento**: Weaviate está dormido en runtime.

---

### ❌ PROBLEMA: "Rate limit 429 en el chat público"

**¿Qué ves?**: `{"error":"rate_limit_exceeded"}` 429.

💡 **SOLUCIÓN**:
- Límite: 20 mensajes/60s por IP+slug (`_CHAT_LIMIT=20`).
- Para subirlo: edita `myownclone_public.py:46` y reinicia.
- ⚠️ Subirlo mucho = mayor costo de IA y riesgo de abuso.

---

### ❌ PROBLEMA: "El servidor se cayó / 502 Bad Gateway"

🔍 **DIAGNÓSTICO**:
```bash
docker compose -f /opt/myownclone/current/ops/docker-compose.backend.prod.yml ps
sudo systemctl status myownclone-frontend
sudo nginx -t
```

💡 **SOLUCIÓN**:
- Si `api` está down: `docker compose ... up -d api`.
- Si frontend down: `sudo systemctl restart myownclone-frontend`.
- Si nginx falla config: `sudo nginx -t` te dice la línea del error.

---

### ❌ PROBLEMA: "La base de datos no conecta"

**¿Qué ves?**: `/readyz` devuelve `"database":"error: ..."`, errores `OperationalError`.

🔍 **DIAGNÓSTICO**:
```bash
docker exec myownclone_postgres pg_isready -U postgres -d myownclone
docker logs myownclone_postgres | tail -20
```

💡 **SOLUCIÓN**:
- Contenedor caído: `docker compose ... restart db_postgres`.
- Credenciales mal: verifica `DB_PASSWORD` y `DATABASE_URL` coinciden con `POSTGRES_PASSWORD` del compose.
- Disco lleno: `df -h` → limpia releases (`du -sh /opt/myownclone/releases/*`).

---

### ❌ PROBLEMA: "El sistema va muy lento"

🔍 **DIAGNÓSTICO**:
```bash
htop                                    # CPU/RAM
docker stats                            # por contenedor
docker exec myownclone_postgres psql -U postgres -d myownclone \
  -c "SELECT count(*) FROM pg_stat_activity;"   # conexiones
```

💡 **SOLUCIÓN**:
- CPU > 80% sostenido: reduce workers de gunicorn en `Dockerfile` (ahora 2) o sube plan VPS.
- Postgres lento: revisa queries lentas (`pg_stat_statements`).
- Chat lento: el cuello suele ser el LLM externo. Prueba un modelo más rápido (DeepSeek-chat).

---

### ❌ PROBLEMA: "El deploy falló"

🔍 **DIAGNÓSTICO**:
```bash
# Salida del script de deploy
# Logs del último intento
docker logs myownclone_api | tail -50
sudo journalctl -u myownclone-frontend --since "10 min ago"
```

💡 **SOLUCIÓN**:
- Si `npm install` falla: red o `package-lock.json` corrupto. Borra `node_modules` y reintenta.
- Si build falla: error TypeScript. Corre localmente `npm run typecheck`.
- Si docker build falla: espacio en disco → `docker system prune`.

**ROLLBACK**: ver Sección 8.

---

### ❌ PROBLEMA: "Se acabaron los créditos de la IA"

**¿Qué ves?**: 401/403 del proveedor, o respuestas vacías.

💡 **SOLUCIÓN**:
1. Recarga saldo en el dashboard del proveedor.
2. Rota la API key (puede estar comprometida).
3. Cambia a otro proveedor configurando su key (prioridad automática).

---

### ❌ PROBLEMA: "Migración Alembic falla"

🔍 **DIAGNÓSTICO**:
```bash
docker exec myownclone_api flask --app app_factory db current
docker exec myownclone_api flask --app app_factory db heads
```

💡 **SOLUCIÓN**:
- Si hay multiples heads: `flask db merge -m "merge heads"`.
- Si la BD no tiene `alembic_version` (Drizzle-only): backup + `flask db stamp head` (marca sin ejecutar).
- Si una migración existe a medias: restaura backup y reintenta.

---

### ❌ PROBLEMA: "El webhook de Stripe no actualiza el plan"

**¿Qué ves?**: pagas en Stripe pero el tenant sigue en `trial`.

🔍 **DIAGNÓSTICO**:
```bash
# ¿Llega el webhook?
sudo journalctl -u myownclone-frontend | grep -i stripe
# ¿STRIPE_WEBHOOK_SECRET coincide con el endpoint de Stripe?
```

💡 **SOLUCIÓN**:
- En Stripe → Developers → Webhooks → tu endpoint →Signing secret debe coincidir con `STRIPE_WEBHOOK_SECRET` del frontend.
- El endpoint debe ser `https://myownclone.com/api/stripe/webhook`.

---

# SECCIÓN 11: CHECKLIST DE MANTENIMIENTO

## 📅 MANTENIMIENTO DIARIO (5 minutos)

```
□ Healthchecks
  curl -s http://127.0.0.1:5001/readyz | grep ready
  curl -sI https://myownclone.com | head -1

□ Estado de contenedores
  docker compose -f /opt/myownclone/current/ops/docker-compose.backend.prod.yml ps | grep -v healthy

□ Logs de errores (últimas 24h)
  docker logs --since 24h myownclone_api 2>&1 | grep -iE "error|exception" | tail -20
  sudo journalctl -u myownclone-frontend --since "24 hours ago" | grep -i error | tail -20

□ Fallos de auth (posible ataque)
  sudo journalctl -u myownclone-frontend --since "24 hours ago" | grep -i "401\|403" | wc -l
  sudo fail2ban-client status sshd

□ Consumo de IA
  # Visita el dashboard de tu proveedor LLM
```

## 📅 MANTENIMIENTO SEMANAL (15 minutos)

```
□ Backup manual (además del cron)
  bash /opt/myownclone/current/ops/backup_postgres.sh

□ Verificar que los backups del cron existen
  ls -lh /opt/myownclone/backups/ | tail -7

□ Espacio en disco
  df -h
  du -sh /opt/myownclone/releases/*
  # Si / > 80%: limpia releases viejos (deja 5)

□ Limpieza Docker
  docker system df
  docker builder prune -f    # si hay > 2GB reclaimable

□ Rotación de logs
  sudo journalctl --vacuum-size=200M

□ Estado de fail2ban
  sudo fail2ban-client status
  sudo fail2ban-client status sshd

□ Revisar costos de servicios IA
  # MiniMax: https://platform.minimaxi.com/
  # OpenAI: https://platform.openai.com/usage

□ Ver actualizaciones del SO pendientes
  apt list --upgradable
```

## 📅 MANTENIMIENTO MENSUAL (1 hora)

```
□ Actualizar dependencias Python
  cd /opt/myownclone/current
  pip install --upgrade -r requirements.txt  # probar en staging primero

□ Actualizar dependencias Node
  cd /opt/myownclone/current/MyOwnClone
  npm audit
  npm update

□ Rotar API keys sensibles (LLM, Stripe, SendGrid)
  # MiniMax/OpenAI: generar nueva key, actualizar .env, reiniciar
  # SERVICE_API_KEY: generar nueva, actualizar AMBOS .env, reiniciar AMBOS servicios
  # JWT_SECRET_KEY: ⚠️ invalida todas las sesiones (avisa a usuarios)

□ Limpiar logs antiguos
  sudo journalctl --vacuum-time=30d
  docker logs --tail 0 -f myownclone_api  # solo verificar, no borrar

□ Verificar certificado SSL
  echo | openssl s_client -connect myownclone.com:443 2>/dev/null | openssl x509 -noout -dates
  # Si vence en < 30 días: sudo certbot renew

□ Probar restauración de backup (en entorno staging)
  gunzip < /opt/myownclone/backups/myownclone_YYYYMMDD_HHMMSS.sql.gz | \
    docker exec -i myownclone_postgres_staging psql -U postgres -d myownclone_test

□ Smoke test completo
  bash /opt/myownclone/current/ops/smoke-prod.sh

□ Revisar tenants inactivos / clones huérfanos
  docker exec myownclone_postgres psql -U postgres -d myownclone -c "
    SELECT t.name, t.plan, t.status, count(c.id) as clones
    FROM tenants t LEFT JOIN clone_configs c ON c.tenant_id = t.id
    GROUP BY t.id ORDER BY t.created_at;
  "

□ Revisar huecos de conocimiento detectados
  docker exec myownclone_postgres psql -U postgres -d myownclone -c "
    SELECT clone_id, question, count FROM analytics_gaps
    WHERE status='open' ORDER BY count DESC LIMIT 20;
  "
```

---

# APÉNDICE A: GLOSARIO RÁPIDO

| Término | Significado en este sistema |
|---|---|
| **Tenant** | Una cuenta de cliente. Aísla todos sus datos. |
| **Clone** | Un asistente de IA configurado por un tenant. |
| **Silo** | Modo del clone: `teach` (enseñar), `support` (soporte), `sales` (ventas). |
| **Source** | Un documento subido para entrenar el clone. |
| **Chunk** | Un fragmento de texto de una source, con su vector léxico. |
| **System prompt** | Instrucciones que definen la personalidad del clone en un modo. |
| **Creator memory** | Notas/firmas/plantillas del creador que enriquecen respuestas. |
| **Inbound email** | Email recibido vía SendGrid, clasificado y con borrador generado por IA. |
| **Impersonación** | Acción de un platform_admin operando como si fuera un tenant (auditado, 30 min). |
| **RAG** | Retrieval-Augmented Generation: buscar contexto antes de llamar al LLM. |
| **`local_hybrid_v1`** | El algoritmo de recuperación real: combina score léxico + coseno del hash. |

---

# APÉNDICE B: RUTAS DE ARCHIVO CRÍTICAS (chuleta)

```
Punto de entrada backend ...... api/app_factory.py
Gestor de IA .................. api/core/model_manager.py
Recuperación RAG .............. api/core/retrieval.py
Prompts IA .................... api/controllers/console/myownclone/clone.py (DEFAULT_PROMPTS)
Prompts email ................. api/core/myownclone/email_ai.py
Auth JWT ...................... api/libs/jwt_utils.py
Auth decorator ................ api/libs/login.py
Validación secretos ........... api/libs/security_checks.py
Esquema DB (ORM) .............. api/models/
Migraciones ................... api/migrations/versions/

Proxy Next.js ................. MyOwnClone/src/proxy.ts
Auth NextAuth ................. MyOwnClone/src/lib/auth.ts
Subida de fuentes (chunks) .... MyOwnClone/src/app/api/clone/sources/route.ts
Chat UI ....................... MyOwnClone/src/components/chat/ChatPanel.tsx
Esquema Drizzle ............... MyOwnClone/src/lib/db/schema/

Compose producción ............ ops/docker-compose.backend.prod.yml
Env backend ................... ops/backend.env.production.example
Env frontend .................. ops/frontend.env.production.example
Deploy backend ................ ops/deploy-backend.sh
Deploy frontend ............... ops/deploy-frontend.sh
Restore desde GitHub .......... ops/restore-from-github-on-vps.sh
Backup Postgres ............... ops/backup_postgres.sh
Smoke test .................... ops/smoke-prod.sh
Systemd frontend .............. ops/myownclone-frontend.service
nginx ......................... ops/nginx.myownclone.conf.example

Auditoría VPS ................. AUDIT_REPORT_VPS.md
Hardening aplicado ............ VPS_HARDENING.md
Arquitectura .................. ARCHITECTURE.md
Deploy guide .................. DEPLOYMENT.md
```

---

*Fin del manual. Si encuentras algo desactualizado, la fuente de verdad SIEMPRE es el código.*

---

# APÉNDICE C: PIPELINE RAG ESTÁNDAR (post-refactor 2026-06-21)

> Esta sección documenta la implementación estándar y optimizada que reemplaza
> al hash léxico original por embeddings reales + pipeline de ingesta completo.
> Ver `SCHEMA_OWNERSHIP.md` para la regla de oro del esquema.

## Qué cambió (resumen ejecutivo)

| Antes | Después |
|---|---|
| Embedding léxico FNV-1a (hash de palabras) | **OpenAI `text-embedding-3-small`** (semántico real), con fallback léxico |
| Solo contenido tipo `text` se indexaba | **PDF + YouTube + Web** funcionan vía extractores |
| `temperature` no se controlaba (default proveedor) | **Configurable por modo** (teach=0.20, sales=0.60) + env vars |
| Sin tracking de costos IA | **`cost_tracking`** registra cada llamada LLM y embedding |
| Sin anti-alucinación explícita | **Prompt fuerza "no inventes"** + registra huecos en `analytics_gaps` |
| Drizzle y Alembic editaban el schema | **Alembic único dueño** (ver `SCHEMA_OWNERSHIP.md`) |
| Retrieval: hash léxico puro | **Híbrido**: `max(cosine, 0.7·cosine + 0.3·term_score)` |

## Archivos nuevos del pipeline

```
api/core/embeddings.py           ← EmbeddingService (OpenAI + fallback léxico)
api/core/chunking.py             ← Troceador canónico (1200/160 chars)
api/core/ingestion_pipeline.py   ← Extractores PDF/YouTube/Web + chunk + embed
api/core/pricing.py              ← Tabla de precios LLM + embeddings
api/commands/reindex.py          ← flask reindex [--tenant|--clone|--rechunk]
api/migrations/versions/2026_06_21_0001_align_with_drizzle.py
SCHEMA_OWNERSHIP.md              ← Regla de oro: Alembic único dueño
```

## Nuevos endpoints internos (auth: `X-API-Key`)

```
POST /api/myownclone/internal/embed         ← embebe textos (OpenAI o léxico)
GET  /api/myownclone/internal/embed/status  ← proveedor/modelo activos
POST /api/myownclone/internal/ingest        ← dispara ingesta de una source
POST /api/myownclone/internal/upload        ← sube PDF al disco del backend
```

El frontend Next.js ya no necesita `OPENAI_API_KEY`: delega al backend.

## Variables de entorno nuevas

```
# Embeddings (FASE 1)
EMBEDDING_PROVIDER=openai          # openai | lexical (auto: openai si hay key)
EMBEDDING_MODEL=text-embedding-3-small

# LLM generation params (FASE 3)
LLM_TEMPERATURE=0.30               # default global; overrideable por modo
LLM_MAX_TOKENS=1024
LLM_TOP_P=1.0

# Uploads (FASE 2)
UPLOAD_DIR=/tmp/myownclone-uploads # donde se guardan los PDFs temporalmente
```

## Cómo activar embeddings semánticos reales

1. Configura `OPENAI_API_KEY` en `ops/backend.env.production`.
2. (Opcional) `EMBEDDING_PROVIDER=openai` (auto-detectado si hay key).
3. Reinicia backend: `docker compose -f ops/docker-compose.backend.prod.yml restart api`
4. **Reindexa el contenido existente** (los chunks viejos tienen hash léxico):
   ```bash
   docker exec myownclone_api flask --app app_factory reindex
   # o con rechunk (re-trocea también):
   docker exec myownclone_api flask --app app_factory reindex --rechunk
   ```
5. Verifica el estado:
   ```bash
   curl http://127.0.0.1:5001/api/myownclone/internal/embed/status \
     -H "X-API-Key: $SERVICE_API_KEY"
   # → {"provider":"openai","model":"text-embedding-3-small","semantic":true}
   ```

⚠️ **Antes de reindexar en producción**: `bash ops/backup_postgres.sh`.

## Cómo subir PDF/YouTube/Web (ahora funcionan)

El dashboard `/biblioteca` ya no requiere cambios: el handler `POST /api/clone/sources` detecta el tipo y delega al backend:

- **Texto**: se trocea y embebe inline (rápido).
- **PDF**: se sube al backend vía `/upload`, luego `/ingest` extrae con `pypdf`.
- **YouTube**: `/ingest` obtiene la transcripción con `youtube-transcript-api`.
- **Web**: `/ingest` extrae el contenido principal con `trafilatura`.

El `status` de la source pasa de `processing` → `ready` (o `error`) en segundo plano. Refresca la página del dashboard para verlo actualizado.

## Control de costos de IA (ahora con datos reales)

Cada llamada al LLM y cada embedding registran una fila en `cost_tracking`:

```sql
SELECT model, category,
       sum(tokens_in) as tokens_in,
       sum(tokens_out) as tokens_out,
       sum(cost_cents) as cost_cents,
       count(*) as calls
FROM cost_tracking
WHERE created_at > now() - interval '7 days'
GROUP BY model, category
ORDER BY cost_cents DESC;
```

Palancas de ahorro (efecto real):
- `LLM_MAX_TOKENS=512` → respuestas más cortas, ~50% menos tokens de output.
- `top_k=3` en `chat_public` (l.347 de `myownclone_public.py`) → 40% menos tokens de contexto.
- Cambiar a MiniMax o DeepSeek (más baratos que OpenAI gpt-4o-mini).

## Temperatura por modo (FASE 3.1)

Cada `clone_mode_prompt` tiene ahora columna `temperature`:

| Modo | Default | Carácter |
|---|---|---|
| teach | 0.20 | Factual, predecible |
| support | 0.25 | Consistente, profesional |
| sales | 0.60 | Más variado, conversacional |

Cámbialo vía `PUT /api/clone/clones/<id>/prompts` con `{"temperature": 0.4}`.

## Migración de schema a aplicar

```bash
docker exec myownclone_api flask --app app_factory db upgrade
# Crea enums PG faltantes + índices + clone_mode_prompts.temperature
```

Compatible con drift Drizzle (ver migración `2026_06_21_0001_align_with_drizzle.py`).
