# CLAUDE.md — Clonify

**Proyecto:** Clon de Clonify sobre Dify (SaaS multi-tenant con chat IA, email triage, booking y billing)

## Arquitectura

- **Backend:** `dify/` — fork de Dify (Flask + PostgreSQL + Redis + Weaviate)
- **Frontend:** `replica/` — Next.js 16 App Router (TypeScript, React 19, Tailwind v4, NextAuth 5)
- **Docker:** `dify/docker/` — docker-compose.yaml con 16 servicios

## Modelo de datos (15 tablas Clonify en `dify/api/models/clonify/`)

- `clone_configs` — configuración del clon (nombre, slug, avatar, modos, custom_domain)
- `clone_mode_prompts` — prompts por modo (teach/support/sales)
- `creator_memory` — memorias del creador para contexto IA
- `email_inbound` / `email_templates` — email triage con IA
- `meeting_types` / `availability` / `bookings` — sistema de reservas
- `products` — catálogo
- `cost_tracking` / `analytics_questions` / `analytics_gaps` — analíticas
- `impersonation_log` / `impersonation_tokens` — admin impersonation
- `clonify_plans` — 4 planes con límites/features

## Endpoints Clave

- Console API: `/console/api/clonify/clones`, `/console/api/clonify/inbox`, `/console/api/clonify/analytics`, `/console/api/clonify/stripe`, `/console/api/clonify/admin`
- Public API: `/api/clonify/public/clones/<slug>/chat` (SSE streaming)

## Deps críticas

- `OPENAI_API_BASE` — proveedor LLM (DeepSeek por defecto)
- `DB_HOST=db_postgres`, `DB_PASSWORD=difyai123456`
- `REDIS_PASSWORD=difyai123456`
- `STRIPE_SECRET_KEY` — billing
- `RESEND_API_KEY` — envío email

## Bugs conocidos

1. `clonify_public_bp` no registrado → endpoints públicos no funcionan
2. `_add_memories_to_prompt()` no retorna → memorias no se injectan
3. `admin_platform.py` línea 169: `tenant_name` = `tenant_id` (sin lookup)

## Comandos comunes

```bash
# Backend
cd dify/docker && docker compose up -d
docker compose exec api flask db upgrade

# Frontend
cd replica && npm run dev

# Test auth
python test_login.py
```

## Credenciales

- DB: `postgres / difyai123456` (host `db_postgres`)
- Admin default: `admin@clonify.com / admin123`
- Weaviate API key: `WVF5YThaHlkYwhGUSmCRgsX3tD5ngdN8pkih`
- Plugin daemon key: `lYkiYYT6owG+71oLerGzA7GXCgOT++6ovaezWAjpCjf+...`
- Plugin inner API key: `QaHbTe77CtuXmsfyhR7+vRjI/+XbV1AaFy691iy+kGDv2Jvy0/eAh8Y1`