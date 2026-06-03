# MyOwnClone — SaaS Multi-tenant AI Platform

**Repository:** https://github.com/Teokoaaly/MyOwnClone

Plataforma SaaS multi-tenant que permite crear "clones" de IA con personalidad, modos (teach/support/sales), email triage con IA, booking y billing Stripe.

## Arquitectura

```
myownclone/
├── api/                      # Backend Python/Flask
│   ├── controllers/          # API endpoints (console + public)
│   │   └── console/myownclone/  # 8 controllers: clone, inbox, analytics, booking, stripe, admin, memory, feedback
│   ├── core/myownclone/      # Lógica de negocio: silos, retrieval, ingestion, email_ai, email_processor
│   ├── models/myownclone/    # Modelos SQLAlchemy
│   └── migrations/versions/  # 5 migrations (15 tablas)
├── replica/                  # Frontend Next.js 16 (App Router)
│   └── src/
│       └── app/             # 19 páginas, 18 API routes
└── docs/                     # Documentación del plan maestro
```

## Stack

- **Backend:** Python/Flask + SQLAlchemy + PostgreSQL + Redis
- **Frontend:** Next.js 16.2.6 (React 19.2.4, App Router, TypeScript)
- **Auth:** NextAuth 5 (beta) + JWT multi-tenant
- **LLM:** DeepSeek (configurable via `OPENAI_API_BASE`)
- **BD:** PostgreSQL + Redis
- **Vector DB:** Weaviate
- **Billing:** Stripe (checkout + webhooks + billing portal)
- **Email:** SendGrid Inbound Parse (webhook) + Resend (envío)
- **Deployment:** Docker Compose

## 15 Tablas MyOwnClone

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
- `POST /api/myownclone/public/clones/<slug>/chat-simple` — Chat JSON
- `GET /api/myownclone/public/clones/<slug>/meeting-types` — Tipos de reunión públicos
- `POST /api/myownclone/public/clones/<slug>/bookings` — Crear reserva
- `POST /api/myownclone/public/inbound-email` — Webhook SendGrid

## Setup Local

```bash
# API (backend)
cd api
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
cd api
docker compose exec api flask db upgrade
```