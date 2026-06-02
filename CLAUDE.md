# CLAUDE.md — myownclone

**Proyecto:** Clon de myownclone sobre Dify (SaaS multi-tenant con chat IA, email triage, booking y billing)

## Arquitectura

- **Backend:** `dify/` — fork de Dify (Flask + PostgreSQL + Redis + Weaviate)
- **Frontend:** `replica/` — Next.js 16 App Router (TypeScript, React 19, Tailwind v4, NextAuth 5)
- **Docker:** `dify/docker/` — docker-compose.yaml con 16 servicios

## Modelo de datos (15 tablas myownclone en `dify/api/models/myownclone/`)

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
- `DB_HOST=db_postgres`, `DB_PASSWORD=difyai123456`
- `REDIS_PASSWORD=difyai123456`
- `STRIPE_SECRET_KEY` — billing
- `RESEND_API_KEY` — envío email

## Bugs conocidos — RESUELTOS

1. ✅ `myownclone_public_bp` no registrado → corregido en `myownclone/api/app_factory.py`
2. ✅ `_add_memories_to_prompt()` no retorna → corregido en `clonify_public.py:166`
3. ✅ `admin_platform.py` línea 166: `tenant_name` = `tenant_id` → corregido con lookup real

## Pendientes (no críticos)

- `MeetingType_` con underscore en el nombre
- `impersonation_tokens` usa `String(36)` en vez de UUID
- `custom_domain` ambigüedad entre `tenants` y `clone_configs`

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
- Admin default: `admin@myownclone.com / admin123`
- Weaviate API key: `WVF5YThaHlkYwhGUSmCRgsX3tD5ngdN8pkih`
- Plugin daemon key: `lYkiYYT6owG+71oLerGzA7GXCgOT++6ovaezWAjpCjf+...`
- Plugin inner API key: `QaHbTe77CtuXmsfyhR7+vRjI/+XbV1AaFy691iy+kGDv2Jvy0/eAh8Y1`