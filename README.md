# myownclone — SaaS Multi-tenant sobre Dify

Plataforma SaaS multi-tenant que permite crear "clones" de IA con personalidad, modos (teach/support/sales), email triage con IA, booking y billing stripe.

## Arquitectura

```
replica/
├── myownclone/               # Fork de Dify (backend Python/Flask)
│   ├── api/                  # Controllers standalone (clonify_public, console/myownclone/*)
│   ├── dify/api/             # Dify source completo (3,076 archivos Python)
│   │   ├── controllers/      # Dify controllers base
│   │   ├── core/myownclone/  # Lógica de negocio: silos, retrieval, ingestion, email_ai, email_processor
│   │   ├── models/myownclone/  # Modelos SQLAlchemy (15 tablas)
│   │   └── migrations/versions/  # Migrations de las tablas myownclone
│   └── dify/docker/         # docker-compose.yaml + .env (16 servicios)
└── replica_src/             # Frontend Next.js 16 (App Router)
    └── src/app/             # 28 páginas, 15 API routes
```

El código principal de los controllers está en `myownclone/api/` (los módulos clonify_public y console/myownclone). El directorio `myownclone/dify/` contiene el source completo de Dify sobre el que se ejecutan los controllers.

## Stack

- **Backend:** Dify (Flask + SQLAlchemy + PostgreSQL + Redis + Weaviate)
- **Frontend:** Next.js 16.2.6 (React 19.2.4, App Router, TypeScript)
- **Auth:** NextAuth 5 (beta) + JWT multi-tenant
- **LLM:** DeepSeek (configurable via `OPENAI_API_BASE`)
- **BD:** PostgreSQL (`difyai123456`) + Redis (`difyai123456`)
- **Vector DB:** Weaviate
- **Billing:** Stripe (checkout + webhooks + billing portal)
- **Email:** SendGrid Inbound Parse (webhook) + Resend (envío)
- **Deployment:** Docker Compose (16 servicios)

## 15 Tablas myownclone

| Tabla | Función |
|---|---|
| `clone_configs` | Config del clon (nombre, slug, avatar, modos activos, custom_domain) |
| `clone_mode_prompts` | System prompts por modo (teach/support/sales) |
| `creator_memory` | Memorias del creador para contexto IA |
| `email_inbound` | Emails recibidos con clasificación IA |
| `email_templates` | Templates de respuesta |
| `meeting_types` | Tipos de reunión (nombre, duración, precio, color) |
| `availability` | Horario semanal (día, hora inicio/fin, buffer) |
| `bookings` | Reservas (visitante, fecha, hora, url reunión) |
| `products` | Catálogo de productos |
| `cost_tracking` | Costes por categoría (respuestas, ingestión, ops) |
| `analytics_questions` | Preguntas más frecuentes |
| `analytics_gaps` | Lagunas de conocimiento (preguntas sin respuesta) |
| `impersonation_log` | Log de impersonación admin |
| `impersonation_tokens` | Tokens de impersonación |
| `myownclone_plans` | 4 planes: Básico $49, Pro $99, Escala $199, Enterprise $499 |

## APIs (36 endpoints)

### Console (autenticado)
- **Clone:** CRUD clones + prompts por modo
- **Inbox:** Lista, detalle, generar draft IA, marcar enviado/descartado
- **Analytics:** Overview, top preguntas, gaps, breakdown costes
- **Booking:** Meeting types, availability, products, bookings CRUD
- **Stripe:** Planes, checkout, billing portal
- **Admin:** MRR overview, tenant list, impersonation on/off

### Público (sin auth)
- `GET /api/myownclone/public/clones/<slug>` — Info pública del clon
- `POST /api/myownclone/public/clones/<slug>/chat` — Chat streaming SSE
- `POST /api/myownclone/public/clones/<slug>/chat-simple` — Chat JSON (mock)
- `GET /api/myownclone/public/clones/<slug>/meeting-types` — Tipos de reunión públicos
- `POST /api/myownclone/public/clones/<slug>/bookings` — Crear reserva
- `POST /api/myownclone/public/inbound-email` — Webhook SendGrid

## Problemas identificados (auditoría)

### Críticos — RESUELTOS
1. ✅ **`myownclone_public_bp` no registrado** — Corregido en `myownclone/api/app_factory.py` (líneas 42-47). El Blueprint público ahora se registra en el app factory.

### Bugs — RESUELTOS
2. ✅ **`_add_memories_to_prompt` no retorna** (clonify_public.py:166) — Corregido: `system_prompt = _add_memories_to_prompt(clone.id, system_prompt)`. Las memorias del creador ahora se injectan en el prompt.

3. ✅ **`admin_platform.py` devuelve `tenant_id` como nombre** (línea 166) — Corregido: `tenant.name if tenant and hasattr(tenant, 'name') else str(data.tenant_id)`. Ahora hace lookup real del nombre.

### Media
4. **`MeetingType_` con underscore** — Nombre poco idiomático (evita conflicto con built-in). Pending rename.

5. **`impersonation_tokens` usa `String(36)`** en vez de tipo UUID — Inconsistente con el resto del schema. Pending.

6. **`custom_domain` en ambas tablas** (`tenants` y `clone_configs`) — Potencial ambigüedad. Pending.

## Setup Local

```bash
# Dify (backend)
cd dify/docker
cp .env.example .env
# Editar .env con API keys reales
docker compose up -d

# Réplica (frontend)
cd replica
cp .env.example .env.local
npm install
npm run dev
```

## Migración DB

```bash
cd dify/docker
docker compose exec api flask db upgrade
```

## Planos implementados (9 fases completadas ~85 min)

| Fase | Descripción | Archivos |
|---|---|---|
| 0 | Análisis + Setup | Mapa código Dify |
| 1 | Schema + Auth multi-tenant | 9 archivos |
| 2 | Silos + RAG | 4 archivos |
| 3 | Chat UI + Widget | 8 archivos |
| 4 | Dashboard Creador | 10 archivos |
| 5 | Email Triage IA | 8 archivos |
| 6 | Stripe + Planes | 7 archivos |
| 7 | Booking + Video | 2 archivos |
| 8 | Admin Plataforma | 4 archivos |

**Total: 52 archivos | 4 modificados | 48 nuevos**