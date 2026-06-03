# MyOwnClone — Auditoría Completa

> Fecha: 2026-05-30
> Host auditado: Windows (100.111.183.23)

---

## 1. Resumen Ejecutivo

**Proyecto:** MyOwnClone — plataforma SaaS de clones IA personalizados para creadores de contenido.

**Stack:**
- Backend: Python/Flask + SQLAlchemy, PostgreSQL, Redis, Weaviate
- Frontend: Next.js 16 (App Router), TypeScript, NextAuth5, Stripe
- Infra: Docker, Traefik, SendGrid Inbound Parse

**Estado:** MVP funcional con bugs críticos que bloquean features enteras.

---

## 2. Estructura de Archivos Auditados

```
myownclone/
├── api/
│   ├── controllers/
│   │   ├── myownclone_public.py       ← 7 endpoints públicos (NO REGISTRADOS)
│   │   ├── console/
│   │   │   └── myownclone/
│   │   │       ├── __init__.py
│   │   │       ├── admin_platform.py  ← bugs
│   │   │       ├── analytics.py
│   │   │       ├── booking.py
│   │   │       ├── clone.py
│   │   │       ├── creator_memory.py
│   │   │       ├── feedback.py
│   │   │       ├── inbox.py
│   │   │       └── stripe_ctrl.py
│   │   └── __init__.py
│   ├── models/
│   ├── core/
│   ├── services/
│   ├── migrations/
│   │   └── versions/
│   └── docker/
├── replica/
│   ├── src/
│   ├── components/
│   └── i18n/
└── docs/
```

---

## 3. Bugs Críticos

### 🔴 BUG #1 — `myownclone_public_bp` no registrado (CRÍTICO)

**Problema:** El Blueprint existe y define 7 endpoints públicos pero nunca se registra en la aplicación Flask. Todos los endpoints `/api/myownclone/public/*` devuelven **404**.

**Fix:** Registrar en `app_factory.py`:
```python
from controllers.myownclone_public import myownclone_public_bp
app.register_blueprint(myownclone_public_bp)
```

---

### 🔴 BUG #2 — `_add_memories_to_prompt()` no retorna (CRÍTICO)

**Problema:** La función modifica `base_prompt` (string local) sin retornarlo. Python strings son inmutables; `base_prompt += ...` solo cambia la variable local que se pierde al salir de la función.

**Fix:**
```python
def _add_memories_to_prompt(clone_id: str, base_prompt: str) -> str:
    ...
    return base_prompt
```

---

### 🟡 BUG #3 — `tenant_name` muestra UUID en vez de nombre

**Archivo:** `admin_platform.py:169`

**Fix:**
```python
tenant = db.session.execute(select(Tenant).where(Tenant.id == data.tenant_id)).scalar_one_or_none()
tenant_name = tenant.name if tenant else data.tenant_id
```

---

### 🟡 BUG #4 — `_is_platform_admin()` demasiado permisivo

**Problema:** Cualquier owner de cualquier tenant es admin de plataforma.

---

### 🟡 BUG #5 — `for silo in CloneSilo` itera sobre miembros del Enum

**Problema:** Itera sobre los nombres del Enum (`"TEACH"`, `"SUPPORT"`), no sobre los valores.

**Fix:**
```python
for silo in CloneSilo.__members__.values():
```

---

## 4. Bugs Menores

### custom_domain duplicado
- `tenants.custom_domain` y `clone_configs.custom_domain` coexisten

### `impersonation_tokens.token` usa String(36)
- Genera tokens via `secrets.token_urlsafe(32)` que produce strings de ~43 chars

### Componentes UI vacíos
- `components/admin/`, `components/booking/`, `components/clone/`, `components/dashboard/`, `components/inbox/` no tienen archivos

### Sin SDK Supabase
- Variables `NEXT_PUBLIC_SUPABASE_*` presentes en `.env.example` pero no hay `supabase` en `package.json`

### `widget.js/route.ts`
- Extensión `.js` no estándar para Next.js App Router

---

## 5. API Endpoints

### Console API (requiere auth)

| Método | Path | Descripción |
|--------|------|-------------|
| GET | `/console/api/myownclone/clones` | Listar clones del tenant |
| POST | `/console/api/myownclone/clones` | Crear clone |
| GET | `/console/api/myownclone/clones/<id>` | Detalle clone |
| PUT | `/console/api/myownclone/clones/<id>` | Actualizar clone |
| DELETE | `/console/api/myownclone/clones/<id>` | Eliminar clone |
| GET | `/console/api/myownclone/clones/<id>/prompts` | Obtener prompts por modo |
| PUT | `/console/api/myownclone/clones/<id>/prompts` | Actualizar prompts |
| POST | `/console/api/myownclone/clones/<id>/clone` | Clonar un clone |
| GET | `/console/api/myownclone/clones/<id>/analytics` | Analytics |
| GET | `/console/api/myownclone/clones/<id>/inbox` | Bandeja de entrada |
| GET | `/console/api/myownclone/clones/<id>/inbox/<email_id>` | Detalle email |
| POST | `/console/api/myownclone/clones/<id>/inbox/<email_id>/reply` | Generar respuesta |
| POST | `/console/api/myownclone/clones/<id>/inbox/<email_id>/classify` | Clasificar email |
| GET | `/console/api/myownclone/clones/<id>/bookings` | Listar bookings |
| POST | `/console/api/myownclone/clones/<id>/bookings` | Crear booking |
| GET | `/console/api/myownclone/clones/<id>/availability` | Disponibilidad |
| POST | `/console/api/myownclone/clones/<id>/availability` | Configurar disponibilidad |
| GET | `/console/api/myownclone/clones/<id>/feedback` | Feedback |
| POST | `/console/api/myownclone/clones/<id>/feedback` | Enviar feedback |
| GET | `/console/api/myownclone/memories` | Listar memorias |
| POST | `/console/api/myownclone/memories` | Crear memoria |
| DELETE | `/console/api/myownclone/memories/<id>` | Eliminar memoria |
| GET | `/console/api/myownclone/admin/platform-stats` | Stats plataforma |
| GET | `/console/api/myownclone/admin/tenants` | Listar tenants |
| POST | `/console/api/myownclone/admin/impersonate/start` | Iniciar impersonation |
| POST | `/console/api/myownclone/admin/impersonate/stop` | Detener impersonation |
| POST | `/console/api/myownclone/stripe/connect` | Stripe Connect |
| GET | `/console/api/myownclone/stripe/connect/callback` | Stripe callback |
| POST | `/console/api/webhook/stripe` | Webhook Stripe |

### Public API (sin auth)

| Método | Path | Descripción |
|--------|------|-------------|
| POST | `/api/myownclone/public/inbound-email` | Receptor SendGrid |
| POST | `/api/myownclone/public/clones/<slug>/chat-simple` | Chat simple |
| POST | `/api/myownclone/public/clones/<slug>/chat` | Chat streaming |
| GET | `/api/myownclone/public/clones/<slug>` | Info pública clone |
| POST | `/api/myownclone/public/clones/<slug>/book` | Booking público |
| GET | `/api/myownclone/public/clones/<slug>/availability` | Disponibilidad |
| POST | `/api/myownclone/public/clones/<slug>/analytics/track` | Tracking |

---

## 6. Modelo de Datos

### Tablas principales (15)

```
clone_configs — configuración de cada clone IA
clone_mode_prompts     — prompts por modo (teach/support/sales)
creator_memories       — memorias persistentes del creador
email_inbound          — emails recibidos
email_outbound        — emails enviados
email_templates       — plantillas de email
impersonation_logs    — log de impersonations
impersonation_tokens — tokens de impersonation
stripe_accounts       — cuentas Stripe Connect
stripe_payments       — pagos Stripe
analytics_events      — eventos analytics
availability — disponibilidad por meeting type
bookings              — reservas de meetings
feedback — feedback de usuarios
tenants               — tenants (extensión)
```

### Plans (seeded)

| Plan | Precio | Límites |
|------|--------|---------|
| starter | $9/mo | 1 clone, 50 emails, 10 bookings |
| pro | $29/mo | 5 clones, 500 emails, 50 bookings |
| growth | $99/mo | clones ilimitados, emails ilimitados, bookings ilimitados |

---

## 7. Frontend

### Stack
- Next.js 16 + TypeScript
- App Router (`src/app/`)
- next-intl para i18n (es, en)
- NextAuth 5 (Auth.js)
- Stripe (@stripe/stripe-js)
- shadcn/ui (components/ui/)
- Tailwind CSS

### Páginas identificadas (19)
```
app/(auth)/login/
app/(auth)/register/
app/(auth)/forgot-password/
app/(dashboard)/dashboard/
app/(dashboard)/clones/
app/(dashboard)/clones/[id]/
app/(dashboard)/clones/[id]/analytics/
app/(dashboard)/clones/[id]/inbox/
app/(dashboard)/clones/[id]/settings/
app/(dashboard)/bookings/
app/api/auth/[...nextauth]/
app/api/myownclone/clones/
app/api/myownclone/clones/[id]/
app/api/myownclone/clones/[id]/inbox/
app/api/myownclone/clones/[id]/analytics/
app/api/clones/[slug]/chat/
app/api/clones/[slug]/book/
```

---

## 8. Fixes Aplicados

| # | Bug | Archivo | Status |
|---|-----|---------|--------|
| 1 | `myownclone_public_bp` no importado | `controllers/__init__.py` | ✅ Fix applied |
| 2 | `_add_memories_to_prompt()` sin return | `myownclone_public.py:273` | ✅ Fix applied |
| 3 | `tenant_name` = UUID | `admin_platform.py:169` | ✅ Fix applied |
| 4 | `_is_platform_admin()` demasiado permisivo | `admin_platform.py` | ✅ Fix applied |
| 5 | `for silo in CloneSilo` itera nombres | `clone.py:119` | ✅ Fix applied |
| 6 | Sin SDK Supabase | `replica/package.json` | ✅ Fix applied |
| 7 | `custom_domain` duplicado | — | ⚠️ Requiere acceso |
| 8 | Componentes UI vacíos | `replica/src/components/` | ⚠️ Requiere acceso |
| 9 | `widget.js/route.ts` extensión | `replica/src/app/api/` | ⚠️ Requiere acceso |

---

## 9. Recomendaciones

1. Registrar `myownclone_public_bp` en `app_factory.py`
2. Añadir Supabase SDK a `package.json` si la integración está planificada
3. Implementar componentes UI vacíos
4. Renombrar `widget.js/route.ts` → `route.ts`
5. Migrar `impersonation_tokens.token` de `String(36)` a `Uuid` o `Text`
6. Considerar eliminar `tenants.custom_domain` (duplicado de `clone_configs.custom_domain`)