# CLAUDE.md — MyOwnClone

**Repository:** https://github.com/Teokoaaly/MyOwnClone

**Proyecto:** Plataforma SaaS multi-tenant con clones IA, email triage, booking y billing.

## Arquitectura

- **Backend:** `api/` — Flask + PostgreSQL + Redis + Weaviate
- **Frontend:** `replica/` — Next.js 16 App Router (TypeScript, React 19, Tailwind v4, NextAuth 5)
- **Docker:** `api/` — docker-compose con servicios

## Modelo de datos (15 tablas MyOwnClone en `api/models/myownclone/`)

- `clone_configs` — configuración del clon (nombre, slug, avatar, modos, custom_domain)
- `clone_mode_prompts` — prompts por modo (teach/support/sales)
- `creator_memory` — memorias del creador para contexto IA
- `email_inbound` / `email_templates` — email triage con IA
- `meeting_types` / `availability` / `bookings` — sistema de reservas
- `products` — catálogo
- `cost_tracking` / `analytics_questions` / `analytics_gaps` — analíticas
- `impersonation_log` / `impersonation_tokens` — admin impersonation
- `myownclone_plans` — 4 planes con límites/features

## Endpoints Clave

- Console API: `/console/api/myownclone/clones`, `/console/api/myownclone/inbox`, `/console/api/myownclone/analytics`, `/console/api/myownclone/stripe`, `/console/api/myownclone/admin`
- Public API: `/api/myownclone/public/clones/<slug>/chat` (SSE streaming)

## Deps críticas

- `OPENAI_API_BASE` — proveedor LLM (DeepSeek por defecto)
- `DB_HOST=db_postgres`, `DB_PASSWORD=dev_password_123`
- `REDIS_PASSWORD=dev_password_123`
- `STRIPE_SECRET_KEY` — billing
- `RESEND_API_KEY` — envío email

## Bugs conocidos

1. `myownclone_public_bp` no registrado → endpoints públicos no funcionan
2. `_add_memories_to_prompt()` no retorna → memorias no se injectan
3. `admin_platform.py` línea 169: `tenant_name` = `tenant_id` (sin lookup)

## Comandos comunes

```bash
# Backend
cd api/api && docker compose up -d
docker compose exec api flask db upgrade

# Frontend
cd replica && npm run dev

# Test auth
python test_login.py
```

## Credenciales

- DB: `postgres / dev_password_123` (host `db_postgres`)
- Admin default: `admin@myownclone.com / admin123`
- Weaviate API key: `WVF5YThaHlkYwhGUSmCRgsX3tD5ngdN8pkih`
- Plugin daemon key: `lYkiYYT6owG+71oLerGzA7GXCgOT++6ovaezWAjpCjf+...`
- Plugin inner API key: `QaHbTe77CtuXmsfyhR7+vRjI/+XbV1AaFy691iy+kGDv2Jvy0/eAh8Y1`