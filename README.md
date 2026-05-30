# Clonify — SaaS Multi-tenant sobre Dify

Plataforma SaaS multi-tenant que permite crear "clones" de IA con personalidad, modos (teach/support/sales), email triage con IA, booking y billing stripe.

## Arquitectura

```
clonify_completo/
├── dify/                    # Fork de Dify (backend Python/Flask)
│   ├── api/
│   │   ├── controllers/     # API endpoints (console + public)
│   │   │   └── console/clonify/  # 8 controllers: clone, inbox, analytics, booking, stripe, admin, memory, feedback
│   │   ├── core/clonify/    # Lógica de negocio: silos, retrieval, ingestion, email_ai, email_processor
│   │   ├── models/clonify/  # Modelos SQLAlchemy
│   │   └── migrations/versions/  # 5 migrations (15 tablas)
│   └── docker/              # docker-compose.yaml + .env
├── replica/                  # Frontend Next.js 16 (App Router)
│   └── src/
│       └── app/             # 19 páginas, 18 API routes
└── docs/                     # Documentación del plan maestro
```

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

## 15 Tablas Clonify

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
| `clonify_plans` | 4 planes: Básico $49, Pro $99, Escala $199, Enterprise $499 |

## APIs (36 endpoints)

### Console (autenticado)
- **Clone:** CRUD clones + prompts por modo
- **Inbox:** Lista, detalle, generar draft IA, marcar enviado/descartado
- **Analytics:** Overview, top preguntas, gaps, breakdown costes
- **Booking:** Meeting types, availability, products, bookings CRUD
- **Stripe:** Planes, checkout, billing portal
- **Admin:** MRR overview, tenant list, impersonation on/off

### Público (sin auth)
- `GET /api/clonify/public/clones/<slug>` — Info pública del clon
- `POST /api/clonify/public/clones/<slug>/chat` — Chat streaming SSE
- `POST /api/clonify/public/clones/<slug>/chat-simple` — Chat JSON (mock)
- `GET /api/clonify/public/clones/<slug>/meeting-types` — Tipos de reunión públicos
- `POST /api/clonify/public/clones/<slug>/bookings` — Crear reserva
- `POST /api/clonify/public/inbound-email` — Webhook SendGrid

## Problemas identificados (auditoría)

### Críticos
1. **`clonify_public_bp` no registrado** — El Blueprint existe en `clonify_public.py` pero no se registra en ningún `__init__.py`. Los endpoints públicos NO funcionan sin registrarlo en `app_factory.py` o `ext_blueprints.py`.

### Bugs
2. **`_add_memories_to_prompt` no retorna** (línea 273) — Modifica `base_prompt` localmente pero no retorna el string modificado. El caller ignora el resultado (Python strings son inmutables). Las memorias del creador nunca se injectan en el prompt.

3. **`admin_platform.py` devuelve `tenant_id` como nombre** (línea 169) — `"tenant_name": data.tenant_id` debería hacer lookup del nombre real del tenant.

4. **`_is_platform_admin` demasiado permisivo** — Cualquier `OWNER` de cualquier tenant es considerado admin de plataforma.

### Media
5. **`MeetingType_` con underscore** — Nombre poco idiomático (evita conflicto con built-in).

6. **`impersonation_tokens` usa `String(36)`** en vez de tipo UUID — Inconsistente con el resto del schema.

7. **`custom_domain` en ambas tablas** (`tenants` y `clone_configs`) — Potencial ambigüedad.

###Frontend
8. **Directorios de componentes vacíos** — `components/admin/`, `components/booking/`, `components/clone/`, `components/dashboard/`, `components/inbox/`, `components/ui/` no tienen archivos.

9. **Sin SDK Supabase** — Env vars referencian Supabase pero no hay `@supabase/supabase-js` en deps.

10. **Widget route handler** — `app/widget.js/route.ts` estructura no estándar para App Router.

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