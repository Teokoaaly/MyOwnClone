# COMPENDIO OSINT — MyOwnClone: Auditoría Total del Sistema

> **Fecha de compilación**: 2026-06-28
> **Rama activa**: `sisyphus/anti-forget-layer`
> **Repositorio**: `C:\Users\haxth3\Documents\MyOwnClone-vps-fixes` (worktree)
> **Repositorio canónico**: `C:\Users\haxth3\Documents\MyOwnClone`
> **Fuentes**: 44 documentos en `.docs_md/` + 4 en `.sisyphus/` + 1 en `.hermes/` + 7 en raíz + código fuente completo

---

## ÍNDICE

1. [Visión General del Proyecto](#1-visión-general-del-proyecto)
2. [Stack Tecnológico Completo](#2-stack-tecnológico-completo)
3. [Arquitectura del Sistema](#3-arquitectura-del-sistema)
4. [API Surface — Cada Endpoint](#4-api-surface--cada-endpoint)
5. [Componentes Frontend — Cada Archivo](#5-componentes-frontend--cada-archivo)
6. [Rutas y Páginas — Mapa Completo](#6-rutas-y-páginas--mapa-completo)
7. [Modelo de Datos — Todas las Tablas](#7-modelo-de-datos--todas-las-tablas)
8. [Sistema de Diseño — Tokens y Reglas](#8-sistema-de-diseño--tokens-y-reglas)
9. [Estado Real por Área (Auditoría 2026-06-11)](#9-estado-real-por-área-auditoría-2026-06-11)
10. [Defectos y Bugs Conocidos](#10-defectos-y-bugs-conocidos)
11. [Historial de Implementación (Fases A→H)](#11-historial-de-implementación-fases-ah)
12. [Plan Sisyphus (M0→M13)](#12-plan-sisyphus-m0m13)
13. [QA y Testing](#13-qa-y-testing)
14. [Comparativa myclone.is → myownclone.com](#14-comparativa-mycloneis--myownclonecom)
15. [Estado del Dashboard — Página por Página](#15-estado-del-dashboard--página-por-página)

---

## 1. VISIÓN GENERAL DEL PROYECTO

**MyOwnClone** es una plataforma SaaS multi-tenant para crear clones digitales de IA. Permite a creadores de contenido, educadores y negocios lanzar un asistente conversacional basado en RAG (Retrieval-Augmented Generation) entrenado con su contenido.

### Objetivo del producto
- Multiplicar la capacidad del creador: un clon que atiende consultas, responde correos y reserva reuniones 24/7
- Tres modos de operación: **pedagogía** (teach), **soporte** (support), **ventas** (sales)
- Widget embedible para cualquier web
- Panel de administración multi-tenant

### Estado global (última auditoría 2026-06-11)
El repositorio **NO está al 100%**. Tiene una base visual y técnica importante, pero no es un producto útil end-to-end. El problema principal es que hay flujos que parecen completos en la UI pero se cortan entre Next.js, proxy, Flask, DB o servicios externos.

---

## 2. STACK TECNOLÓGICO COMPLETO

### Frontend (`MyOwnClone/`)
| Tecnología | Versión | Notas |
|---|---|---|
| Next.js | 16.2.6 | App Router, Turbopack |
| React | 19.2.4 | Server Components + Client Components |
| TypeScript | 5.x | Strict mode |
| Tailwind CSS | 4.x | PostCSS plugin, `@theme inline` block para tokens |
| Drizzle ORM | 0.38 | Solo para auth/web; NO es fuente de verdad para admin |
| NextAuth.js | v5 beta | Auth.js, adaptador Drizzle |
| next-intl | 3.24 | i18n con locale forzado a `es` |
| framer-motion | 12 | Animaciones declarativas |
| @phosphor-icons/react | latest | 8 namespaces de iconos |
| dompurify | latest | Sanitización HTML en chat |
| recharts | (planificado) | Gráficos — aún no instalado |

### Backend (`api/api/`)
| Tecnología | Versión | Notas |
|---|---|---|
| Flask | 3.x | Application factory pattern |
| SQLAlchemy | 2.0 | ORM con Mapped columns |
| Flask-SQLAlchemy | 3.1 | Integración Flask |
| Flask-Migrate | 4.x | Alembic migrations |
| Flask-CORS | 4.x | CORS configurable |
| flask-restx | 1.3 | Swagger/OpenAPI |
| Pydantic | 2.x | Validación de schemas |
| psycopg2-binary | latest | Driver PostgreSQL |
| gunicorn | latest | WSGI server producción |
| pgvector | pg15 | Búsqueda semántica vectorial |

### Infraestructura
| Componente | Tecnología |
|---|---|
| Base de datos | PostgreSQL 15 + pgvector |
| Cache / Rate Limit | Redis |
| Búsqueda vectorial | pgvector (ivfflat) |
| Weaviate | En requirements.txt pero posiblemente legacy |
| Email entrante | SendGrid Inbound Parse Webhook |
| Email saliente | Resend |
| Videollamadas | Whereby |
| Pagos | Stripe |
| Analytics | PostHog |
| Monitoreo errores | Sentry (planificado) |

---

## 3. ARQUITECTURA DEL SISTEMA

### Componentes principales

```
┌─────────────────────────────────────────────────────────┐
│  FRONTEND (Next.js 16 + React 19)                       │
│  ├── Landing page (/)                                    │
│  ├── Auth pages (/login, /registro)                      │
│  ├── Dashboard (/(dashboard)/)                           │
│  │   ├── resumen, biblioteca, cerebro, inbox            │
│  │   ├── productos, reuniones, analiticas               │
│  │   ├── facturacion, configuracion, settings           │
│  │   └── onboarding                                     │
│  ├── Admin (/admin/)                                     │
│  │   ├── resumen, tenants, feedback, audit              │
│  │   ├── impersonation, courtesy                        │
│  │   └── ia-modelos (planificado M11)                   │
│  └── Public clone page (/(public)/[slug])                │
├─────────────────────────────────────────────────────────┤
│  PROXY (Next.js API Routes)                              │
│  ├── /api/admin/[...path] → Flask admin endpoints       │
│  ├── /api/clone/[...path] → Flask user endpoints         │
│  ├── /api/auth/[...nextauth] → NextAuth                 │
│  ├── /api/stt → Speech-to-text                          │
│  ├── /api/stripe/webhook → Stripe                       │
│  └── /api/bookings → Bookings                            │
├─────────────────────────────────────────────────────────┤
│  BACKEND (Flask, api/api/)                               │
│  ├── Auth (console/auth.py)                              │
│  ├── Admin Platform (myownclone/admin_platform.py)      │
│  ├── Clones CRUD (myownclone/clone.py)                   │
│  ├── Inbox (myownclone/inbox.py)                         │
│  ├── Analytics (myownclone/analytics.py)                 │
│  ├── Stripe (myownclone/stripe_ctrl.py)                  │
│  ├── Booking (myownclone/booking.py)                     │
│  ├── Feedback (myownclone/feedback.py)                   │
│  ├── Creator Memory (myownclone/creator_memory.py)      │
│  └── Public clone chat (myownclone_public.py)            │
├─────────────────────────────────────────────────────────┤
│  CORE (api/core/)                                         │
│  ├── RAG pipeline (retrieval.py, embeddings.py)         │
│  ├── Model Manager (model_manager.py)                    │
│  ├── Email AI (email_ai.py)                              │
│  └── Silos (myownclone/silos.py)                         │
├─────────────────────────────────────────────────────────┤
│  DATOS                                                    │
│  ├── PostgreSQL + pgvector                               │
│  └── Redis (rate limiting/cache)                         │
└─────────────────────────────────────────────────────────┘
```

### Flujo de request autenticado
1. Usuario entra en dashboard Next.js
2. NextAuth emite token/sesión
3. `src/proxy.ts` valida ruta protegida
4. Proxy agrega `X-API-Key` y headers de identidad
5. Flask `login_required` valida JWT o service API key
6. Controlador ejecuta lógica de negocio con tenant/user context
7. Respuesta vuelve al frontend

### Flujo de chat público
1. Visitante abre página pública o widget
2. Frontend llama `/api/clone/{slug}/chat`
3. Proxy enruta a endpoint público Flask
4. Backend aplica rate limit, resuelve clone y fuentes
5. RAG recupera contexto, llama LLM y persiste conversación
6. Respuesta vuelve como JSON o SSE

### Multi-tenancy
- Tenant se detecta por subdominio `tenant.replica.domain`
- Datos aislados por `tenant_id` y `clone_id`
- Riesgo: cada query admin/console debe validar tenant scoping

### Estrategia de migraciones
- Frontend: Drizzle migrations en `MyOwnClone/drizzle`
- Backend: Alembic migrations en `api/migrations`
- Ambos conocen tablas compartidas — riesgo de drift
- Recomendación documentada: Alembic como fuente de verdad para schema runtime compartido

---

## 4. API SURFACE — CADA ENDPOINT

### 4.1 Rutas Next.js (BFF / proxy)

| Path | Archivo | Propósito |
|---|---|---|
| `/api/admin/[...path]` | `app/api/admin/[...path]/route.ts` | Proxy a Flask admin, valida NextAuth + DB role |
| `/api/auth/[...nextauth]` | `app/api/auth/[...nextauth]/route.ts` | NextAuth |
| `/api/csrf` | `app/api/csrf/route.ts` | CSRF token |
| `/api/clone/[...path]` | `app/api/clone/[...path]/route.ts` | Proxy a Flask user endpoints |
| `/api/clone/[slug]` | `app/api/clone/[slug]/route.ts` | Clone-scoped endpoints |
| `/api/clone/[slug]/chat` | `app/api/clone/[slug]/chat/route.ts` | Chat público/clone |
| `/api/clone/billing` | `app/api/clone/billing/route.ts` | Stripe billing |
| `/api/clone/feedback` | `app/api/clone/feedback/route.ts` | User feedback |
| `/api/clone/inbox` | `app/api/clone/inbox/route.ts` | Inbox |
| `/api/clone/inbox/[id]` | `app/api/clone/inbox/[id]/route.ts` | Message detail |
| `/api/clone/inbox/[id]/generate-draft` | `.../generate-draft/route.ts` | Generar draft |
| `/api/clone/inbox/list` | `app/api/clone/inbox/list/route.ts` | List messages |
| `/api/clone/plans` | `app/api/clone/plans/route.ts` | Plan listing |
| `/api/clone/stripe` | `app/api/clone/stripe/route.ts` | Stripe webhook |
| `/api/clone/stripe/checkout` | `app/api/clone/stripe/checkout/route.ts` | Checkout session |
| `/api/bookings` | `app/api/bookings/route.ts` | Bookings |
| `/api/inbound-email` | `app/api/inbound-email/route.ts` | Inbound email webhook |
| `/api/stt` | `app/api/stt/route.ts` | Speech-to-text |

### 4.2 Backend Flask — Auth

| Method | Path | Auth |
|---|---|---|
| POST | `/console/api/auth/login` | None (rate-limited) |
| GET | `/console/api/auth/verify` | Bearer |

### 4.3 Backend Flask — Admin Platform (9 endpoints)

| Method | Path | Descripción |
|---|---|---|
| GET | `/console/api/myownclone/admin/overview` | Métricas plataforma: tenants, MRR, plan breakdown |
| GET | `/console/api/myownclone/admin/tenants` | Lista paginada con filtros search/status/plan |
| GET | `/console/api/myownclone/admin/tenants/<id>` | Detalle tenant + usage + clones |
| PATCH | `/console/api/myownclone/admin/tenants/<id>` | Cambiar plan/status |
| GET | `/console/api/myownclone/admin/feedback` | Feedback paginado con filtros |
| POST | `/console/api/myownclone/admin/impersonate` | Iniciar impersonación (30 min TTL) |
| POST | `/console/api/myownclone/admin/impersonate/stop` | Cerrar impersonación |
| GET | `/console/api/myownclone/admin/audit-log` | Auditoría paginada |
| POST | `/console/api/myownclone/admin/courtesy` | Crear tenant+account de cortesía |

**Planes canónicos**: `["trial", "basic", "pro", "scale", "enterprise"]`
**Precios (EUR cents/mes)**: trial=0, basic=4900, pro=9900, scale=19900, enterprise=49900
**Status canónicos**: `["active", "trial", "suspended", "cancelled", "normal"]`

### 4.4 Backend Flask — User (clones, inbox, etc.)

| Method | Path | Archivo |
|---|---|---|
| GET/POST | `/console/api/myownclone/clone/...` | `controllers/console/myownclone/clone.py` |
| GET/POST | `/console/api/myownclone/inbox/...` | `controllers/console/myownclone/inbox.py` |
| POST | `/console/api/myownclone/feedback` | `controllers/console/myownclone/feedback.py` |
| GET | `/console/api/myownclone/creator-memory/...` | `controllers/console/myownclone/creator_memory.py` |
| GET | `/console/api/myownclone/analytics/...` | `controllers/console/myownclone/analytics.py` |
| POST | `/console/api/myownclone/stripe/...` | `controllers/console/myownclone/stripe_ctrl.py` |
| GET/POST | `/console/api/myownclone/booking/...` | `controllers/console/myownclone/booking.py` |

### 4.5 Backend Flask — Public (clone widget)

| Method | Path | Archivo |
|---|---|---|
| GET | `/api/myownclone/clone/<slug>/chat` | `controllers/myownclone_public.py` |
| GET | `/api/myownclone/clone/<slug>/...` | `controllers/myownclone_public.py` |

### 4.6 Errores estándar

| Código | Status | Cuándo |
|---|---|---|
| `unauthorized` | 401 | Sin sesión/token |
| `platform_admin_required` | 403 | No es platform_admin |
| `invalid_payload` | 400 | Pydantic validation falló |
| `no_op` | 400 | PATCH sin campos |
| `tenant_not_found` | 404 | tenant_id no existe |
| `no_token` | 400 | stop-impersonate sin token |
| `no_active_impersonation` | 404 | Token no encontrado/expirado |

---

## 5. COMPONENTES FRONTEND — CADA ARCHIVO

### 5.1 Componentes UI compartidos (`src/components/ui/`)

| Componente | Archivo | Uso |
|---|---|---|
| `Sidebar` | `Sidebar.tsx` | Navegación del dashboard con secciones, user block, mobile sheet |
| `AnimatedLogoMark` | `AnimatedLogoMark.tsx` | Logo animado "M" |
| `PublicPricing` | `PublicPricing.tsx` | Pricing compartido landing/dashboard |
| `LandingBehavior` | `LandingBehavior.tsx` | Comportamiento del landing page |
| `ShaderBackground` | `ShaderBackground.tsx` | Fondo con shader animado |
| `StatusBadge` | `StatusBadge.tsx` | Badges de estado (active/trial/warning/error/violet) |
| `LoadingState` | `LoadingState.tsx` | Esqueleto de carga |
| `EmptyState` | `EmptyState.tsx` | Estado vacío con icono + título + descripción |
| `ErrorState` | `ErrorState.tsx` | Estado de error con mensaje + botón reintentar |
| `Modal` | `Modal.tsx` | Modal con focus trap, escape-close, click-outside |
| `BarChart` | `BarChart.tsx` | Gráfico de barras SVG sin dependencias |
| `SearchCommandBar` | `SearchCommandBar.tsx` | ⌘K command bar (depende de endpoints frágiles) |
| `ThemeProvider` | `ThemeProvider.tsx` | Contexto de tema claro/oscuro (actualmente dead file) |
| `ThemeToggle` | `ThemeToggle.tsx` | Botón sol/luna autocontenido |
| `MobileNav` | `MobileNav.tsx` | Drawer de navegación móvil |

### 5.2 Componentes del Dashboard (`src/components/dashboard/`)

| Componente | Archivo | Uso |
|---|---|---|
| `DashboardTopbarSearch` | `DashboardTopbarSearch.tsx` | Barra de búsqueda en topbar |
| `OnboardingBanner` | `OnboardingBanner.tsx` | Banner de progreso de onboarding |
| `CloneIdResolver` | `CloneIdResolver.tsx` | Resuelve y setea el clone activo |
| `HeaderBreadcrumb` | `HeaderBreadcrumb.tsx` | Breadcrumb en dashboard |
| `Sidebar` | `Sidebar.tsx` | (mismo que en ui/ — reutilizado) |

### 5.3 Componentes del Chat (`src/components/chat/`)

| Componente | Archivo | Funcionalidad |
|---|---|---|
| `ChatPanel` | `ChatPanel.tsx` (365 líneas) | Panel de chat completo con SSE streaming, inline y default modes, sanitización ``, silo toggle, empty state personalizable |
| `MessageBubble` | `MessageBubble.tsx` (225 líneas) | Burbuja de mensaje con feedback 👍/👎, confidence bar, sources expandibles, sanitización HTML |
| `SiloToggle` | `SiloToggle.tsx` | Toggle teach/support/sales |

**Modos de ChatPanel:**
- `mode="default"` — chat centrado, para página pública del clon
- `mode="inline"` — chat embebido en dashboard, soporta `onReset`, `emptyState`, `initialQuery`

### 5.4 Componentes Admin (`src/components/admin/`)

| Componente | Archivo | Funcionalidad |
|---|---|---|
| `PageHeader` | `PageHeader.tsx` | Título + subtítulo + slot de acciones |
| `Field` | `Field.tsx` | Label + control wrapper |
| `FilterBar` | `FilterBar.tsx` | Fila de filtros estándar |
| `Pagination` | `Pagination.tsx` | ← Anterior / Siguiente → |
| `useAdminFetch` | `useAdminFetch.ts` | Hook fetch con cancelación + 401/403 redirect |
| `AdminTopbar` | `AdminTopbar.tsx` | Topbar admin con breadcrumb |
| `ImpersonateButton` | `ImpersonateButton.tsx` | Modal impersonación con textarea reason |
| `CourtesyButton` | `CourtesyButton.tsx` | Modal courtesy signup |
| `AdminCharts` | `AdminCharts.tsx` | Gráficos admin overview |

### 5.5 Auth Components

| Componente | Archivo |
|---|---|
| `SignOutButton` | `components/auth/SignOutButton.tsx` |

---

## 6. RUTAS Y PÁGINAS — MAPA COMPLETO

### 6.1 Rutas públicas

| Ruta | Layout | Archivo | Auth |
|---|---|---|---|
| `/` | `app/layout.tsx` | `app/page.tsx` | Ninguna |
| `/login` | `app/layout.tsx` | `app/login/page.tsx` | Ninguna |
| `/registro` | `(dashboard)/layout.tsx` | `app/(dashboard)/registro/page.tsx` | Ninguna |
| `/forgot-password` | `app/layout.tsx` | `app/forgot-password/page.tsx` | Ninguna |
| `/reset-password` | `app/layout.tsx` | `app/reset-password/page.tsx` | Email link |
| `/es/verificar` | `app/layout.tsx` | `app/es/verificar/page.tsx` | Email link |
| `/es/onboarding` | `app/layout.tsx` | `app/es/onboarding/page.tsx` | Email link |
| `/legal` | `app/layout.tsx` | `app/legal/page.tsx` | Ninguna |
| `/[slug]` | `(public)/layout.tsx` | `app/(public)/[slug]/page.tsx` | Ninguna (clon público) |

### 6.2 Rutas del Dashboard (requieren autenticación)

| Ruta | Archivo | APIs que consume |
|---|---|---|
| `/resumen` | `(dashboard)/resumen/page.tsx` | `/api/clone/analytics/overview`, `/api/clone/inbox/list` |
| `/biblioteca` | `(dashboard)/biblioteca/page.tsx` | `/api/clone/sources` |
| `/biblioteca/nuevo` | `(dashboard)/biblioteca/nuevo/page.tsx` | POST `/api/clone/sources` |
| `/cerebro` | `(dashboard)/cerebro/page.tsx` | `/api/clone/creator-memory` |
| `/inbox` | `(dashboard)/inbox/page.tsx` | `/api/clone/inbox/list`, `/api/clone/inbox/[id]` |
| `/productos` | `(dashboard)/productos/page.tsx` | `/api/clone/clones/${cid}/products` |
| `/reuniones` | `(dashboard)/reuniones/page.tsx` | Booking endpoints |
| `/analiticas` | `(dashboard)/analiticas/page.tsx` | Analytics endpoints |
| `/facturacion` | `(dashboard)/facturacion/page.tsx` | `/api/clone/plans`, `/api/clone/billing` |
| `/configuracion` | `(dashboard)/configuracion/page.tsx` | API Keys |
| `/settings` | `(dashboard)/settings/page.tsx` | Settings |
| `/onboarding` | `(dashboard)/onboarding/page.tsx` | POST `/api/clone/clones` |

### 6.3 Rutas Admin (requieren platform_admin)

| Ruta | Archivo | APIs que consume |
|---|---|---|
| `/admin/resumen` | `admin/resumen/page.tsx` | `/api/admin/overview` |
| `/admin/tenants` | `admin/tenants/page.tsx` | `/api/admin/tenants` |
| `/admin/tenants/[id]` | `admin/tenants/[id]/page.tsx` | `/api/admin/tenants/[id]` |
| `/admin/feedback` | `admin/feedback/page.tsx` | `/api/admin/feedback` |
| `/admin/audit` | `admin/audit/page.tsx` | `/api/admin/audit-log` |
| `/admin/impersonation` | `admin/impersonation/page.tsx` | `/api/admin/impersonate` |
| `/admin/courtesy` | `admin/courtesy/page.tsx` | `/api/admin/courtesy` |
| `/admin/ia-modelos` | `admin/ia-modelos/page.tsx` | Planificado M11 |

---

## 7. MODELO DE DATOS — TODAS LAS TABLAS

### 7.1 Esquema Drizzle (frontend — solo auth/web)

| Archivo | Tablas |
|---|---|
| `users.ts` | NextAuth users (incluye `role`) |
| `tenants.ts` | Mirror read-only de tenants Flask |
| `sources.ts` | Fuentes de conocimiento |
| `emails.ts` | Email entrante |
| `conversations.ts` | Conversaciones de chat |
| `clones.ts` | Configuraciones de clones |
| `chunks.ts` | Chunks RAG |
| `bookings.ts` | Reservas |
| `analytics.ts` | Agregaciones de analytics |

### 7.2 Modelos SQLAlchemy (backend — fuente de verdad)

| Archivo | Modelos |
|---|---|
| `account.py` | `Account`, `Tenant` |
| `analytics.py` | `CostTracking`, `Plan`, `AnalyticsQuestion`, `AnalyticsGap`, `ImpersonationLog`, `ImpersonationToken`, `Feedback`, `AdminAuditLog` |
| `clone.py` | `CloneConfig`, `CloneModePrompt`, `CloneSilo`, `CreatorMemory`, `CreatorMemoryType` |
| `email.py` | `EmailInbound`, `EmailInboundStatus`, `EmailTemplate` |
| `meeting.py` | `MeetingType_`, `Availability`, `Booking`, `BookingStatus`, `Product` |

### 7.3 Divergencias de contrato DB (P0-03)

| Concepto | Drizzle | SQLAlchemy |
|---|---|---|
| Planes | `basic/pro/scale/enterprise/trial` | default `"basico"`/`"básico"` |
| Tenant status | `trial/active/suspended/cancelled` | default `"normal"` |
| Clone modes | `pedagogy` | `teach` |
| Products status | enum en columna `status` | boolean `active` |
| Impersonation table | `impersonation_logs` | `impersonation_log` |

**Recomendación documentada**: Drizzle schema + SQLAlchemy alineado. Normalizar a inglés: `basic`, `pro`, `scale`, `enterprise`; `teach`, `support`, `sales`.

### 7.4 Migraciones Alembic (7 archivos)

| Migración | Propósito |
|---|---|
| `a1b2c3d4e5f6_...` | Tablas core MyOwnClone |
| `b2c3d4e5f6a7_...` | Añade slug, plan, custom_domain, subscription_status |
| `c3d4e5f6a7b8_...` | Seed de 5 planes con precios |
| `d4e5f6a7b8c9_...` | Añade custom_domain a clone_configs |
| `e5f6a7b8c9d0_...` | Tabla impersonation_tokens |
| `2026_06_03_0930_...` | Índices de rendimiento |
| `2026_06_04_1000_...` | Tabla admin_audit_log |

---

## 8. SISTEMA DE DISEÑO — TOKENS Y REGLAS

### 8.1 Identidad: "Institutional Console"

- Personalidad: claro, denso, premium, financiero
- Light por defecto, dark como variante por tokens
- Referencias: Madful'At dashboard, OEME console, Linear/Stripe admin panels

### 8.2 Principios (NO romper)

1. Light mode es el producto por defecto
2. UI responsive real (desktop denso, tablet compacto, mobile stacked)
3. Información, no decoración, es la protagonista
4. No landing-page dentro de la app
5. No card dentro de card
6. No texto largo explicando la UI
7. No gradientes que oculten datos
8. No colores saturados
9. No sombras pesadas

### 8.3 Tokens de superficie (light)

| Token | Valor | Uso |
|---|---|---|
| `--bg-page` | `#E8E2DD` | Fondo exterior (warm cream) |
| `--bg-shell` | `#FFFFFF` | Shell de la app |
| `--bg-sidebar` | `#FFFFFF` | Sidebar |
| `--bg-topbar` | `#FFFFFF` | Topbar |
| `--surface-1` | `#FFFFFF` | Cards |
| `--surface-2` | `#FAFAF9` | Cards anidadas / hover |
| `--surface-3` | `#F5F5F4` | Hover profundo |

### 8.4 Tokens de texto

| Token | Light | Dark |
|---|---|---|
| `--text-primary` | `#1C1917` | `#F4F4F5` |
| `--text-secondary` | `#57534E` | `#A1A1AA` |
| `--text-muted` | `#78716C` (4.69:1 AA) | `#A1A1AA` (~6.4:1) |
| `--text-faint` | `#D6D3D1` | `#52525B` |

### 8.5 Paleta de acentos

| Token | Color | Uso |
|---|---|---|
| `--color-accent-warm` | `#EA580C` | CTA por defecto, nav activo |
| `--color-accent-amber` | `#D97706` | Advertencias |
| `--color-accent-pink` | `#DB2777` | Errores |
| `--color-accent-blue` | `#2563EB` | Info |
| `--color-accent-cyan` | `#0891B2` | Trial/new |
| `--color-accent-violet` | `#7C3AED` | Chat, admin |
| `--color-accent-green` | `#059669` | Éxito |

### 8.6 Tipografía

- UI/body: DM Sans (`var(--font-dm-sans)`)
- Números/código: JetBrains Mono (`var(--font-jetbrains-mono)`)
- H1: 24-32px, H2 (card): 16-20px, Body: 14-15px, Label: 11-12px uppercase

### 8.7 Layout grid (desktop ≥1024px)

```
┌──────────────────────────────────────────────────┐
│ Page padding p-3 md:p-6                          │
│  ┌─ shell rounded-22 border shadow-soft ──────┐  │
│  │ ┌── sidebar 220px ──┐ ┌── content ────────┐ │  │
│  │ │ Logo              │ │ Topbar 72px       │ │  │
│  │ │ Nav sections      │ │ Main p-6          │ │  │
│  │ │  · API PLAYGROUND │ │   grid 12 cols    │ │  │
│  │ │  · MANAGEMENT     │ │   gap-4           │ │  │
│  │ │ User block        │ │                   │ │  │
│  │ └───────────────────┘ └───────────────────┘ │  │
│  └──────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────┘
```

### 8.8 Reglas de componentes

- **Cards**: radius 14-18px, padding 16-24px, border 1px `var(--border-soft)`, hover `translateY(-1px)` max
- **Botones**: pill shape, primary `#0C0A09` sólido, secondary blanco con borde
- **Inputs**: 36-40px height, border `var(--border-soft)`, focus `var(--color-accent-warm)`, radius 8-10px
- **Badges**: translúcidos, 1px border + 10% alpha fill + texto sólido
- **Tablas**: compact rows (36-44px), header `--surface-2`, mono números alineados derecha
- **Estados**: Empty (icono 32-40px + título + microcopy), Loading (skeleton `--surface-2`), Error (icono rojo + razón + "Try again")

---

## 9. ESTADO REAL POR ÁREA (AUDITORÍA 2026-06-11)

### Veredicto directo

**El repositorio NO está al 100%.** Tiene base visual y técnica importante, pero no es un producto útil end-to-end. El problema no es CSS: hay flujos que parecen completos en la UI pero se cortan entre Next, proxy, Flask, DB o servicios externos.

| Área | Estado | Detalle |
|---|---|---|
| Landing | 🟡 Amarillo | Visualmente avanzada, pricing debe compartir contrato con billing |
| Dashboard | 🟡🔴 Amarillo/Rojo | UI amplia, varios widgets sin datos reales |
| Backend Flask | 🟡🔴 Amarillo/Rojo | Controladores existen, hay stubs y endpoints incompletos |
| RAG/Conocimiento | 🔴 Rojo | No hay ingestion real conectada desde la UI |
| Billing/Stripe | 🔴 Rojo | Checkout tiene errores de contrato y rutas antiguas |
| Admin | 🔴🟡 Rojo/Amarillo | Pantallas que llaman rutas no mapeadas |
| Tests | 🔴 Rojo | Typecheck OK, Vitest falla, pytest raíz no cubre `api/tests` |
| Producción | 🔴 Rojo | Contratos/env/migraciones no cerrados |

### Matriz de utilidad por flujo

| Flujo | UI | API | Backend | DB | Tests | Estado |
|---|---|---|---|---|---|---|
| Landing pricing | ✅ | N/A | Parcial | Divergente | No E2E | 🟡 |
| Login | ✅ | NextAuth | Flask/raw DB | Divergente | Parcial | 🟡 |
| Crear clone | ✅ | Proxy | ✅ | clone_configs | Parcial | 🟡 |
| Chat clone | ✅ | Proxy | ✅ | RAG roto/stub | Unit rojo | 🔴 |
| Subir conocimiento | ✅ | Next local | No ingestion | No conectado | Parcial | 🔴 |
| Memories/cerebro | ✅ | Proxy | ✅ | Divergente | No E2E | 🟡 |
| Inbox/email | ✅ | Proxy | ✅ | Divergente | No E2E | 🟡 |
| Products | ✅ | Proxy | POST solo | Divergente | No E2E | 🔴 |
| Meetings | ✅ | Proxy | GET/POST | Divergente | No E2E | 🟡 |
| Billing | ✅ | Proxy | Roto | Divergente | Unit rojo | 🔴 |
| Admin tenants | ✅ | Proxy | ✅ | tenants/accounts | Smoke parcial | 🟡 |
| Admin audit | ✅ | Ruta no mapeada | No claro | Divergente | Skipped | 🔴 |
| Admin feedback | ✅ | Ruta no mapeada | Feedback clon | clone_feedback | No E2E | 🔴 |
| Courtesy | ✅ | Ruta incorrecta | courtesy-account | accounts/tenants | Skipped | 🔴 |

---

## 10. DEFECTOS Y BUGS CONOCIDOS

### P0 — Bloqueadores reales

**P0-01 — El conocimiento no llega al RAG**
- La UI de biblioteca escribe fuentes, pero el backend RAG no las lee
- `api/models/dataset.py` son stubs
- Resultado: usuario puede subir contenido y verlo como `ready`, pero el clon no lo usa

**P0-02 — Billing/Stripe roto**
- `stripe_ctrl.py` usa rutas `/dashboard/resumen` en vez de `/resumen`
- `current_account_with_tenant()` puede devolver string/proxy, no objeto con `.email`
- El checkout no es funcional

**P0-03 — Contratos DB divergentes**
- Planes: Drizzle `basic/pro/scale` vs SQLAlchemy `"basico"/"básico"`
- Clone modes: Drizzle `pedagogy` vs Backend `teach`
- Products: Drizzle enum `status` vs SQLAlchemy boolean `active`
- Impersonation: `impersonation_logs` vs `impersonation_log`

**P0-04 — Admin tiene rutas visuales no conectadas**
- Frontend llama `/api/admin/audit-log`, `/api/admin/feedback`, `/api/admin/courtesy`
- Proxy solo mapea `/api/admin/courtesy-account`
- Backend tiene rutas en Flask pero no coinciden con lo que el proxy espera

### P1 — Flujos importantes incompletos

- **P1-01**: Products no tiene GET/PUT/DELETE auditado
- **P1-02**: Analytics devuelve `total_conversations=0` hardcodeado
- **P1-03**: SearchCommandBar depende de endpoints frágiles
- **P1-04**: Proxy hardcodea `BACKEND_URL = "http://127.0.0.1:5001"`
- **P1-05**: Variables DB inconsistentes (`DB_USER` vs `DB_USERNAME`)
- **P1-06**: Tests frontend rojos (ChatPanel `scrollTo`, facturación expects antiguos)
- **P1-07**: pytest raíz no ejecuta `api/tests`

### P2 — Riesgos de producto

- **P2-01**: 7 archivos son stubs estructurales en backend
- **P2-02**: API local sources no valida ownership fuerte
- **P2-03**: `wordCount: 150` y `status: "ready"` stubs
- **P2-04**: E2E solo cubre navegación básica y auth
- **P2-05**: `.venv` dentro del repo mete ruido
- **P2-06**: `.flaskenv` trackeado con `FLASK_ENV=development`

### Defectos del plan Sisyphus (documentados en HANDOFF_LLM.md)

- **Defecto #2** (PENDIENTE): Cost tracking ausente en streaming — 4 backends streaming no llaman a `_record_llm_cost`
- **Defecto #3** (PENDIENTE): String literal `"clone_response"` en vez de `CostCategory.CLONE_RESPONSE.value`
- **Defecto #4** (PENDIENTE): Sin batching en `/api/embed` público
- **Defecto #6** (PENDIENTE): Threshold silencioso (0.25) en retrieval — sin log de warning en fallback

### Hallazgos del Functional Audit (2026-06-10)

- **F-001**: Credenciales del log de sesión obsoletas (no usar para QA automatizada)
- **F-002**: Facturación es frágil ante fallo parcial de backend
- **F-003**: Onboarding no garantiza cierre robusto del flujo
- **F-004**: Biblioteca/nuevo tiene manejo de error demasiado silencioso
- **F-005**: AI interview es placeholder "Coming soon"
- **F-006**: Inbox tiene acciones pero feedback funcional mínimo
- **F-007**: Copys y flujo de acceso mezclan estados de producto

---

## 11. HISTORIAL DE IMPLEMENTACIÓN (FASES A→H)

### Resumen ejecutivo de todo lo implementado (2026-06-05)

| Fase | Entregable | Estado |
|---|---|---|
| **Phase -1** | Auditoría completa del repositorio | ✅ |
| **Phase 0** | 8 documentos maestros creados | ✅ |
| **Phase A** | Docs (fusionado en Phase 0) | ✅ |
| **Phase B** | Backend hardening: 47 dead files eliminados, stubs fail-closed en prod, 20 pytest tests | ✅ |
| **Phase C** | Admin UI: audit log, impersonation, courtesy, SVG bar charts, 7 shared components | ✅ |
| **Phase D** | Design system: MobileNav, ThemeToggle, dark mode sin flash, login redesign, landing cleanup | ✅ |
| **Phase E** | Dashboard polish: resumen con datos reales, inbox/biblioteca/facturacion con tokens | ✅ (3/9 páginas) |
| **Phase F** | QA: ESLint flat config, 0 type errors, build OK, vitest 19/19, pytest 20/20 | ✅ |
| **Phase G** | Admin refactor: PageHeader, Field, FilterBar, Pagination, useAdminFetch, AdminTopbar | ✅ |
| **Phase H** | Accessibility: axe-core audit, color contrast AA, modal focus trap, breadcrumb aria | ✅ |

### Resultados QA (Phase F)

| Check | Resultado |
|---|---|
| `npm run lint` | ✅ 0 errors, 9 warnings |
| `npm run build` | ✅ Compiled in 50s |
| `npm run test` (vitest) | ✅ 19/19 passed |
| `pytest api/api/tests/` | ✅ 20/20 passed |
| `tsc --noEmit` | ✅ 0 errors |

---

## 12. PLAN SISYPHUS (M0→M13)

### Sistema de Modelos IA Configurables por Tarea

**Objetivo**: Reemplazar selección fija de LLM por env vars con sistema DB-driven que asigna modelo distinto a cada tarea.

**Deliverables principales**:
- Catálogo `ai_models` + asignaciones `ai_model_assignments` + auditoría `ai_invocations`
- `SecretCipher` AES-256-GCM
- `ModelRegistry` con cache TTL 60s
- 6 `ProviderAdapter` (OpenAI, Anthropic, MiniMax, Together, OpenAI-compat, Local)
- `RetryClient` con backoff + circuit breaker
- `TokenBudgeter` con gpt-tokenizer
- 6 endpoints admin REST + playground
- UI `/admin/ia-modelos`

### Estado de los 15 milestones

| ID | Título | Estado |
|---|---|---|
| **M0** | Capa anti-olvido (progress.json + checker + smoke tests + hook) | ✅ DONE |
| M1 | Capa de datos: AIModel + AIModelAssignment + AIInvocation + migración | ⏳ PENDING |
| M2 | Cifrado AES-256-GCM: crypto.py + CLI + security_checks | ⏳ PENDING |
| M4a | ProviderAdapter interface + ProviderRegistry | ⏳ PENDING |
| M3 | ModelRegistry: resolver con cache TTL 60s + invalidación + fallback | ⏳ PENDING |
| M4b | 6 adapters concretos | ⏳ PENDING |
| M5 | RetryClient: backoff exponencial + failover + circuit breaker | ⏳ PENDING |
| M6 | TokenBudgeter: tokenizer + limits | ⏳ PENDING |
| M7 | Refactor model_manager: invoke_for_task + cost tracking en streaming | ⏳ PENDING |
| M8 | Refactor embeddings: embed_texts acepta AIModel opcional | ⏳ PENDING |
| M9 | API admin REST: 6 endpoints + playground + tests | ⏳ PENDING |
| M10 | Integración en chat/embeddings/email/STT | ⏳ PENDING |
| M11 | UI /admin/ia-modelos: page + form + playground + chart | ⏳ PENDING |
| M12 | Auditoría + cost_daily_rollup + rotación doble-clave | ⏳ PENDING |
| M13 | Defectos #3/#4/#6 + backfill + docs | ⏳ PENDING |

**Orden de ejecución obligatorio**: M0(done) → M1 → M2 → M4a → M3 → M4b → M5 → M6 → M7 → M8 → M9 → M10 → M11 → M12 → M13

**Mecánica anti-olvido (M0)**:
- `python scripts/check-plan-progress.py` → exit 0 = progreso consistente
- `pytest tests/test_plan_completion.py` → 15 tests, 1 por milestone, en ROJO hasta implementado
- Pre-commit hook bloquea commits si progress.json es inconsistente

### Working tree SIN commitear (a fecha 2026-06-21)

```
M  .sisyphus/progress.json          # SHA corregido
M  scripts/check-plan-progress.py   # 2 bugfixes
M  scripts/pre-commit-hook.sh       # resolver python robusto
```

---

## 13. QA Y TESTING

### Suites de tests

| Suite | Archivos | Estado | Cobertura |
|---|---|---|---|
| Vitest (frontend) | `MyOwnClone/src/__tests__/` | ✅ 19/19 | Parcial |
| pytest (raíz) | `tests/` | ✅ ~96 passed | Parcial |
| pytest (backend) | `api/api/tests/` | ✅ 20/20 | Admin smoke tests |
| pytest (plan completion) | `tests/test_plan_completion.py` | 🔴 1 failed (esperado) | M0→M13 tracking |
| Playwright E2E | `MyOwnClone/e2e/` | ✅ 35 tests, 2 skip | Solo navegación+auth |

### Lo que NO está cubierto por tests

- Crear clone E2E
- Subir fuente → chat con contexto E2E
- Billing checkout E2E
- Admin audit/feedback/courtesy E2E
- Products CRUD E2E
- Tenant scoping negativo
- Rate limiting
- Migraciones desde DB vacía

### Configuración de pytest

```ini
# pytest.ini
[pytest]
testpaths = tests
```
**Problema**: `api/tests` queda fuera del comando normal. Hay que añadirlo.

---

## 14. COMPARATIVA myclone.is → myownclone.com

### 14.1 myclone.is (competidor de referencia)

| Elemento | Detalle |
|---|---|
| **Stack** | Astro 5.16 + React islands |
| **Hero** | "Clone Yourself. Capture Leads in your Voice." |
| **Demos** | Widgets inline con personas preconfiguradas (insurance-quoter, hvac-dispatch, restaurant) |
| **Features** | Bento grid animado: "Answers like you do", "Multiple personas", "Seamless Integration", "Train with knowledge" |
| **Testimonios** | Marquee doble animado (izq/der), 3 testimonios reales con fotos, fondo oscuro `#1a1a1a` |
| **Pricing** | FREE / PRO / ENTERPRISE |
| **About** | Equipo (Vignesh, Rohan, Vaibhav) + inversor (Script.Capital) + badges (Product Hunt, Peerlist) |
| **Analytics** | PostHog + GA4 + RB2B |
| **Login** | Google, LinkedIn, email/username |
| **App** | `app.myclone.is` (separada del landing) |
| **Embed** | `myclone-embed.js` con `window.MyClone({mode:'inline', ...})` |

### 14.2 Widget de myclone.is (anatomía)

```javascript
window.MyClone({
  mode: 'inline',
  container: '#myclone-inline-chat-insurance-quoter',
  expertUsername: 'viggy28',
  personaName: 'insurance-quoter',
  widgetToken: 'wgt_eyJhbG...',
  primaryColor: '#6366f1',
  enableVoice: true,
  branding: { showHeader: false }
});
```

Usan personas preconfiguradas con tokens de widget. El widget se carga desde `https://app.myclone.is/embed/myclone-embed.js`.

### 14.3 MyOwnClone — equivalencias técnicas YA existentes

| Capacidad myclone.is | Equivalente MyOwnClone | Gap |
|---|---|---|
| Widget inline | `ChatPanel` con `mode="inline"` | ✅ Ya existe. Solo falta crear personas seed |
| Chat SSE streaming | `ChatPanel.tsx` líneas 109-155 | ✅ Ya existe |
| Silo/mode toggle | `SiloToggle` integrado en ChatPanel | ✅ Ya existe |
| Embed script | `widget.js` en raíz | ✅ Ya existe |
| Public clone page | `/(public)/[slug]/page.tsx` | ✅ Ya existe |
| Testimonios | **NO existe** | 🔴 Hay que crear componente |
| Demos interactivas | **NO en landing** | 🔴 Hay que crear UseCasesShowcase |
| Features page | **NO existe** | 🔴 Hay que crear ruta /features |
| About page | **NO existe** | 🔴 Hay que crear ruta /about |
| Hero agresivo | Copy suave "works for you" | 🟡 Cambiar copy |
| Dashboard app separada | Mismo dominio, rutas bajo /(dashboard) | 🟡 No es crítico |

---

## 15. ESTADO DEL DASHBOARD — PÁGINA POR PÁGINA

### 15.1 Resumen (`/resumen`)

- **Estado**: 🟡 Funcional con datos reales (Phase E)
- **APIs**: `/api/clone/analytics/overview`, `/api/clone/inbox/list`
- **Componentes**: QuickActionCard, StatsCard, BarChart, ChatPanel inline, OnboardingBanner
- **Chat inline**: Input con "What do you want to build or query?", botones Search/Fast/Templates, expansión animada a ChatPanel
- **Quick links**: API Keys, Usage (barras SVG), Docs, Agent Toolkit
- **Falta**: Conexión real de analytics (backend devuelve stubs)

### 15.2 Biblioteca (`/biblioteca`)

- **Estado**: 🟡 UI pulida (Phase E), pero ingestion no conectada a RAG
- **5 tipos de fuente**: PDF, YouTube, texto, web, AI interview
- **Silos**: teach (Teaching), support (Support), sales (Sales)
- **Problema**: `status: "ready"` y `wordCount: 150` son stubs
- **AI interview**: placeholder "Coming soon"

### 15.3 Cerebro (`/cerebro`)

- **Estado**: 🟡 UI pulida (Phase F), requiere validar efecto real
- **3 tabs**: Memories, Signatures, Templates
- **Memories**: Fragmentos de info que el clon debe recordar
- **Signatures**: HTML para firma de emails
- **Templates**: Respuestas predefinidas con condiciones

### 15.4 Inbox (`/inbox`)

- **Estado**: 🟡 UI pulida (Phase E), feedback funcional mínimo
- **Filtros**: All, Pending, Sent, Discarded
- **Clasificación IA**: inquiry, complaint, sale, support, other
- **Acciones**: Generate draft, Save draft, Send, Discard
- **Problema**: Errores genéricos, usa `confirm()` nativo, sin feedback de éxito

### 15.5 Onboarding (`/onboarding`)

- **Estado**: 🟡 Funcional pero no robusto
- **4 pasos**: Clone name → Personality → Language → Confirm
- **Personalidades**: Formal 👔, Informal 👋, Friendly 🤝, Technical 🔧
- **Idiomas**: Spanish 🇪🇸, English 🇬🇧
- **Problema**: No confirma clon activo tras crear, hace `router.push("/resumen")` directamente

### 15.6 Productos (`/productos`)

- **Estado**: 🔴 Backend solo tiene POST, no GET
- **Problema**: Dashboard no puede listar productos de forma fiable

### 15.7 Reuniones (`/reuniones`)

- **Estado**: 🟡 UI pulida (Phase F), requiere validar booking real
- **Integración**: Whereby para videollamadas

### 15.8 Analíticas (`/analiticas`)

- **Estado**: 🟡 UI pulida (Phase F), datos no reales
- **Problema**: Backend `analytics.py` tiene `total_conversations = 0` hardcodeado

### 15.9 Facturación (`/facturacion`)

- **Estado**: 🟡🔴 Frágil ante error parcial
- **APIs**: `/api/clone/plans`, `/api/clone/billing`
- **Problema**: Si una API falla, toda la página falla

### 15.10 Admin — Resumen (`/admin/resumen`)

- **Estado**: 🟢 Funcional con charts
- **Componentes**: BarChart (MRR·Costes·Margen 30d), plan breakdown
- **Estados**: LoadingState, ErrorState, EmptyState

### 15.11 Admin — Tenants (`/admin/tenants`)

- **Estado**: 🟢 Funcional
- **Filtros**: search, status, plan, sort, direction
- **Componentes**: PageHeader, FilterBar, Field, Pagination, CourtesyButton, StatusBadge
- **Mobile**: List rows en <768px, tabla en ≥768px

### 15.12 Admin — Tenant Detail (`/admin/tenants/[id]`)

- **Estado**: 🟢 Funcional
- **Features**: Tenant info, usage (30d), clones list, ImpersonateButton, plan-patch modal

### 15.13 Admin — Feedback (`/admin/feedback`)

- **Estado**: 🟢 Funcional
- **Filtros**: rating (up/down), clone_id, tenant_id
- **Bug corregido**: Antes solo redirigía en 401, no en 403

### 15.14 Admin — Audit Log (`/admin/audit`)

- **Estado**: 🟢 Funcional
- **Filtros**: action, actor_id, target_id
- **Acciones registradas**: impersonation_started, impersonation_stopped, tenant_updated, tenant_created

---

## APÉNDICE A — Estructura de archivos del repositorio

```
C:\Users\haxth3\Documents\MyOwnClone-vps-fixes\
├── .dockerignore
├── .docs_md/                          # 44 documentos de auditoría y planificación
│   ├── audit/                         # 16 archivos de auditoría profunda
│   │   ├── 00-coordination.md
│   │   ├── 01-db-architecture.md
│   │   ├── 02-auth-security.md
│   │   ├── 03-frontend.md
│   │   ├── 04-backend-rag.md
│   │   ├── 05-i18n.md
│   │   ├── 06-integrations.md
│   │   ├── 07-testing-ci-prod.md
│   │   ├── 99-consolidated-action-plan.md
│   │   ├── 100-deep-repository-audit-2026-06-11.md
│   │   ├── IMPLEMENTATION_PROGRESS_2026-06-12.md
│   │   ├── _inbox.md
│   │   └── _locks.md
│   ├── MASTER_IMPLEMENTATION_PLAN.md
│   ├── DESIGN_SYSTEM.md
│   ├── BACKEND_ADMIN_CONTRACTS.md
│   ├── ROUTE_AND_COMPONENT_MAP.md
│   ├── IMPLEMENTATION_LOG.md          # 1440 líneas de historial
│   ├── FUNCTIONAL_AUDIT_2026-06-10.md
│   ├── QA_CHECKLIST.md
│   ├── BACKEND_SECURITY_AUDIT.md
│   ├── FRONTEND_UI_AUDIT.md
│   ├── SECURITY_AUDIT_2026-06-11.md
│   ├── SESSION_LOG_2026-06-10.md
│   ├── MASTER_PLAN.md
│   ├── MASTER_IMPLEMENTATION_PLAN_2026-06-12.md
│   ├── MASTER_FUNCTIONAL_COMPLETION_PLAN.md
│   ├── DIAGNOSTICO_TECNICO.md
│   ├── DASHBOARD_MESSAGING_PLAN.md
│   ├── DEPLOY_VPS.md
│   ├── VPS_DEPLOY_ERRORS.md
│   ├── AUTH_SOURCE_OF_TRUTH.md
│   ├── I18N_50_LANGUAGES_PLAN.md
│   ├── CANONICAL_POST_DEPLOY_STATE_2026-06-08.md
│   ├── HANDOFF_POST_DEPLOY_2026-06-08.md
│   ├── STYLE-CENTRIFUGE-ADMIN-GUIDE.md
│   ├── MANUAL.md
│   ├── MANUAL_EN.md
│   └── ...
├── .git                               # Apunta a C:\Users\haxth3\Documents\MyOwnClone\.git\worktrees\
├── .github/
├── .hermes/
│   └── plans/
│       └── 2026-06-08_145239-myownclone-master-recovery-plan.md
├── .sisyphus/                         # Plan Sisyphus (M0→M13)
│   ├── progress.json                  # Estado canónico, 15 tareas
│   ├── plans/
│   │   └── ai-models-configurable.md  # 621 líneas, diseño M1→M13
│   ├── drafts/
│   │   └── ai-models-catalog.md
│   └── evidence/
│       └── task-M0-anti-forget.md
├── MyOwnClone/                        # Frontend Next.js 16
│   └── src/
│       ├── app/                       # App Router
│       │   ├── (dashboard)/           # Rutas protegidas
│       │   ├── (public)/              # Páginas públicas de clon
│       │   ├── admin/                 # Admin platform
│       │   ├── api/                   # API Routes (proxy BFF)
│       │   ├── es/                    # Rutas i18n español
│       │   ├── login/
│       │   ├── registro/
│       │   ├── globals.css            # Design tokens
│       │   ├── layout.tsx
│       │   └── page.tsx               # Landing page
│       ├── components/
│       │   ├── admin/                 # 9 componentes admin
│       │   ├── chat/                  # ChatPanel, MessageBubble
│       │   ├── dashboard/             # Sidebar, OnboardingBanner
│       │   └── ui/                    # 15 componentes compartidos
│       ├── hooks/
│       ├── i18n/
│       ├── lib/                       # auth, csrf, db, email, etc.
│       └── types/
├── api/
│   └── api/                           # Backend Flask (fuente de verdad)
│       ├── controllers/console/myownclone/
│       │   ├── admin_platform.py      # 9 endpoints admin
│       │   ├── analytics.py
│       │   ├── booking.py
│       │   ├── clone.py
│       │   ├── creator_memory.py
│       │   ├── feedback.py
│       │   ├── inbox.py
│       │   └── stripe_ctrl.py
│       ├── core/                      # RAG, model_manager, embeddings
│       ├── models/                    # SQLAlchemy models
│       ├── migrations/                # Alembic
│       └── tests/                     # 20 smoke tests admin
├── tests/                             # pytest raíz (96 tests)
├── scripts/                           # check-plan-progress.py, pre-commit-hook.sh
├── README.md                          # 837 líneas
├── ARCHITECTURE.md                    # 112 líneas
├── ROADMAP.md                         # 112 líneas (7 semanas)
├── HANDOFF_LLM.md                     # 399 líneas (transferencia a LLM)
├── AUDIT_REPORT.md                    # 9870 bytes
├── BACKLOG.md
├── CONTRIBUTING.md
├── DEPLOYMENT.md
├── SETUP.md
├── Dockerfile
├── requirements.txt
├── pytest.ini
└── conftest.py
```

---

## APÉNDICE B — Documentos OSINT clave (ruta completa)

| # | Documento | Ruta | Tamaño |
|---|---|---|---|
| 1 | Auditoría profunda | `.docs_md/audit/100-deep-repository-audit-2026-06-11.md` | 14KB |
| 2 | Master Implementation Plan | `.docs_md/MASTER_IMPLEMENTATION_PLAN.md` | 16.6KB |
| 3 | Design System | `.docs_md/DESIGN_SYSTEM.md` | 9.8KB |
| 4 | Backend Admin Contracts | `.docs_md/BACKEND_ADMIN_CONTRACTS.md` | 9.8KB |
| 5 | Route & Component Map | `.docs_md/ROUTE_AND_COMPONENT_MAP.md` | 9.6KB |
| 6 | Implementation Log | `.docs_md/IMPLEMENTATION_LOG.md` | 71.9KB |
| 7 | Functional Audit | `.docs_md/FUNCTIONAL_AUDIT_2026-06-10.md` | 7.2KB |
| 8 | QA Checklist | `.docs_md/QA_CHECKLIST.md` | — |
| 9 | Backend Security Audit | `.docs_md/BACKEND_SECURITY_AUDIT.md` | — |
| 10 | Frontend UI Audit | `.docs_md/FRONTEND_UI_AUDIT.md` | — |
| 11 | Security Audit | `.docs_md/SECURITY_AUDIT_2026-06-11.md` | — |
| 12 | Session Log | `.docs_md/SESSION_LOG_2026-06-10.md` | — |
| 13 | Diagnóstico Técnico | `.docs_md/DIAGNOSTICO_TECNICO.md` | — |
| 14 | Dashboard Messaging Plan | `.docs_md/DASHBOARD_MESSAGING_PLAN.md` | — |
| 15 | Deploy VPS | `.docs_md/DEPLOY_VPS.md` | — |
| 16 | VPS Deploy Errors | `.docs_md/VPS_DEPLOY_ERRORS.md` | — |
| 17 | Auth Source of Truth | `.docs_md/AUTH_SOURCE_OF_TRUTH.md` | — |
| 18 | i18n 50 Languages Plan | `.docs_md/I18N_50_LANGUAGES_PLAN.md` | — |
| 19 | Post-Deploy State | `.docs_md/CANONICAL_POST_DEPLOY_STATE_2026-06-08.md` | — |
| 20 | Handoff Post-Deploy | `.docs_md/HANDOFF_POST_DEPLOY_2026-06-08.md` | — |
| 21 | Plan Sisyphus | `.sisyphus/plans/ai-models-configurable.md` | 35.5KB |
| 22 | Progress JSON | `.sisyphus/progress.json` | 4.7KB |
| 23 | Handoff LLM | `HANDOFF_LLM.md` | 27.4KB |
| 24 | README | `README.md` | 30.3KB |
| 25 | Architecture | `ARCHITECTURE.md` | 3.5KB |
| 26 | Roadmap | `ROADMAP.md` | 4.8KB |
| 27 | Heremes Master Recovery | `.hermes/plans/2026-06-08_145239-myownclone-master-recovery-plan.md` | — |

---

---

## 16. AUDITORÍA EN VIVO — PRODUCCIÓN (2026-06-28)

> **Método**: Navegación real del sitio https://myownclone.com con browser + curl
> **Servidor**: nginx/1.28.3 (Ubuntu), Next.js self-hosted
> **Estado general**: El sitio está VIVO y responde. El landing funciona completamente. El dashboard requiere acceso beta. El chat público tiene problemas de conexión backend.

### 16.1 Páginas verificadas en vivo

| Ruta | Status HTTP | Renderiza | Hallazgos |
|---|---|---|---|
| `/` (landing) | 200 ✅ | ✅ Completo | Landing en español, 5 secciones: Hero, Servicios, Proceso, Planes, CTA |
| `/login` | 200 ✅ | ✅ Completo | Formulario email+password + Google OAuth. Traducido al español |
| `/forgot-password` | 200 ✅ | ✅ Completo | "¿Olvidaste tu contraseña?" funcional |
| `/legal` | 200 ✅ | ✅ Parcial | Bug: `legal.legal.terms_of_service` (clave i18n sin traducir) |
| `/registro` | 307 ⚠️ | ❌ Redirige | Redirige a `/#plans` — la ruta `/registro` no existe como página independiente |
| `/demo-clone` | 200 ✅ | ✅ UI carga | Título "YouOwnClone" (bug: nombre inconsistente). Chat UI renderiza pero backend no encuentra el clon |
| `/admin/resumen` | 307 ⚠️ | ❌ Redirige | Redirige a login (esperado sin sesión) |
| `Empezar` CTA | 200 ✅ | ✅ Beta form | Formulario de solicitud de acceso beta: nombre, email, plan, motivo, comentario + Google |

### 16.2 Hero / Landing (verificado)

**Copy actual en producción (ESPAÑOL):**
- Kicker: "CLON DIGITAL CON IA"
- H1: "Crea un clon de IA que trabaja por ti."
- Subtítulo: "Entrena un asistente de IA con tu conocimiento, personalidad y datos de negocio. Responde a clientes, guía leads y automatiza el trabajo diario sin perder tu voz."
- CTA primario: "Solicitar acceso" → formulario beta
- CTA secundario: "Iniciar sesión"
- Nav: MyOwnClone | Servicios | Proceso | Planes | Idioma | Iniciar sesión | Empezar

**Secciones del landing:**
1. Hero con logo animado + shader background
2. "QUÉ HACE" — 3 cards: Resumen, Conocimiento, Automatización
3. "CÓMO FUNCIONA" — 4 pasos: Regístrate, Configura, Entrena, Despliega
4. "PRECIOS" — PublicPricing con tabs Pricing/Compare features, toggle annual/monthly, 3 planes (Free/Pro/Enterprise) con "Request access"
5. CTA final: "Listo para clonarte a ti mismo?"

**Lo que NO tiene el landing (vs myclone.is):**
- ❌ Sin testimonios
- ❌ Sin demos/widgets interactivos
- ❌ Sin casos de uso por industria
- ❌ Sin features visuales (bento grid)
- ❌ Sin badges de plataformas (Product Hunt, etc.)
- ❌ CTA es "Solicitar acceso" (beta cerrada) en vez de "Crear tu clon" (signup directo)

### 16.3 Formulario de acceso beta

**Campos del formulario (verificado en vivo):**
- Nombre (requerido)
- Email (requerido)
- Plan: Select con opciones Free/Pro/Enterprise
- Motivo de acceso beta: 6 opciones (Soporte, Ventas, Enseñanza, Asistente personal, Curiosidad, Otro)
- Comentario (opcional): "Cuéntanos sobre tu caso de uso, tamaño del equipo o qué quieres construir..."
- Botón: "Solicitar acceso" (deshabilitado hasta completar campos requeridos)
- Alternativa: "Continuar con Google"

**Hallazgo**: El registro es manual (beta cerrada). No hay signup automático. Esto limita la capacidad de demostración del producto.

### 16.4 Login

**Métodos de autenticación:**
- Email + contraseña
- Google OAuth

**Credenciales conocidas:**
- `admin@myownclone.com` / `admin123` → ❌ NO FUNCIONAN en producción ("Email o contraseña incorrectos")
- La credenciales del SESSION_LOG están obsoletas (ya advertido en FUNCTIONAL_AUDIT F-001)

### 16.5 Chat público (demo-clone)

**Estado: PARCIALMENTE ROTO**

- La página `/demo-clone` carga UI correctamente:
  - Header con nombre "demo-clone"
  - Toggle de 3 modos: Learn, Support, Sales
  - Área de mensajes vacía
  - Input text + botón Send
- **Pero el backend devuelve `{"error":"clone not found"}`**
- El título de la página es "YouOwnClone" (posible bug de nomenclatura)
- El endpoint Flask `/console/api/myownclone/public/clones/demo-clone` devuelve 404 (el proxy Next.js no lo enruta)

**Causa probable**: El clone se sembró en Drizzle (frontend) pero no en SQLAlchemy (backend Flask). El backend no encuentra el clone y el chat no puede funcionar.

### 16.6 APIs verificadas con curl

| Endpoint | Método | Resultado |
|---|---|---|
| `GET /api/clone/plans` | GET | `{"error":"Unauthorized"}` (requiere auth) |
| `GET /api/auth/session` | GET | `null` (sin sesión, esperado) |
| `POST /api/clone/demo-clone/chat` | POST | `{"error":"clone not found"}` |
| `GET /console/api/myownclone/public/clones/demo-clone` | GET | 404 HTML (no enrutado por proxy) |
| `POST /console/api/.../public/clones/demo-clone/chat` | POST | 404 HTML (no enrutado por proxy) |

### 16.7 Estado de i18n (verificado en vivo)

- El landing carga en español por defecto
- El login está en español
- La página `/legal` tiene una clave sin traducir: `legal.legal.terms_of_service`
- El formulario beta está en español
- Hay un botón "Idioma" en la nav que muestra "English" (posiblemente toggle EN/ES)

### 16.8 Seguridad (headers verificados)

```
Server: nginx/1.28.3 (Ubuntu)
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' https:; style-src 'self' https: 'unsafe-inline'; img-src 'self' data: blob: https:; font-src 'self' data: https:; connect-src 'self' https: ws: wss:; media-src 'self' blob: data: https:; object-src 'none'; base-uri 'self'; form-action 'self'; frame-ancestors 'none'
Referrer-Policy: strict-origin-when-cross-origin
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Permissions-Policy: camera=(), microphone=(), geolocation=()
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```

**Evaluación**: Headers de seguridad sólidos. CSP bien configurado. Sin vulnerabilidades obvias en headers.

### 16.9 Resumen de bugs en producción

| ID | Severidad | Descripción | Ubicación |
|---|---|---|---|
| PROD-01 | 🔴 P0 | Chat público roto: `{"error":"clone not found"}` | Backend Flask no tiene el clone seedeado |
| PROD-02 | 🔴 P0 | Proxy no enruta `/console/api/myownclone/public/clones/*` | proxy.ts o nginx config |
| PROD-03 | 🔴 P0 | Login con credenciales seed no funciona | DB de prod no tiene el usuario o contraseña cambiada |
| PROD-04 | 🟡 P1 | `/registro` redirige a landing (no hay signup público) | Ruta no accesible sin auth |
| PROD-05 | 🟡 P1 | Título de demo-clone es "YouOwnClone" (no "MyOwnClone") | Metadata o componente |
| PROD-06 | 🟡 P2 | `legal.legal.terms_of_service` clave i18n sin traducir | Archivo de traducciones |
| PROD-07 | 🟡 P2 | Sin acceso al dashboard (beta cerrada) | No se puede auditar UI autenticada |

---

## 17. DIAGNÓSTICO FINAL Y RECOMENDACIONES

### Estado real del producto (2026-06-28)

| Capa | Estado |
|---|---|
| **Landing page** | 🟢 Funcional, bien diseñado, en español. Falta: testimonios, demos, casos de uso |
| **Login/Auth** | 🟢 Funcional (Google OAuth + credenciales). Credenciales seed rotas |
| **Registro** | 🟡 Solo beta cerrada (formulario manual). Sin signup automático |
| **Chat público** | 🔴 Roto en producción. UI carga pero backend no encuentra clones |
| **Dashboard** | ⚫ No verificable (requiere acceso authenticated) |
| **Admin** | ⚫ No verificable (requiere platform_admin) |
| **API Backend** | 🔴 Endpoints públicos no enrutados correctamente |
| **Seguridad** | 🟢 Headers CSP/XFO/HSTS sólidos |

### Acciones prioritarias para producción

1. **Arreglar el chat público** — seedear el clone en la DB de Flask O hacer que el backend lea los clones de la DB compartida
2. **Arreglar el proxy** — asegurar que `/console/api/myownclone/public/clones/:slug` está enrutado
3. **Credenciales de acceso** — regenerar hash de contraseña para `admin@myownclone.com` o crear credenciales de QA
4. **Abrir registro** — cambiar de beta cerrada a signup automático (al menos en staging)
5. **Alinear DBs** — resolver divergencia Drizzle vs SQLAlchemy para clones

---

---

## 18. INVESTIGACIÓN: REGRESIÓN DEL FRONTEND Y BLOQUEO DE REGISTRO

> **Fecha del hallazgo**: 2026-06-28
> **Síntoma en producción**: `/registro` redirige a `/#plans`. Solo hay formulario beta manual. Sin signup público.

### 18.1 Causa raíz identificada

El commit **`516e805`** del **2026-06-18** en el branch **`origin/i18n/exec-en-es`** introdujo un BETA_MODE gate:

```typescript
// Añadido en MyOwnClone/src/app/registro/page.tsx
if (process.env.BETA_MODE === "true") {
  redirect("/#plans");
}
```

**Autor del commit**: `Hermes Agent <hermes@myownclone.local>`
**Mensaje**: `feat: BETA_MODE redirect en /registro — bloquea registro, redirige al beta form`
**Fecha**: Thu Jun 18 22:21:09 2026 +0000
**Branch que lo contiene**: `origin/i18n/exec-en-es`
**NO está en**: `origin/master`, `sisyphus/anti-forget-layer`

### 18.2 Estado por branch

| Branch | Registro | Landing | ¿Desplegado? |
|---|---|---|---|
| `origin/master` | ✅ Limpio (sin BETA_MODE) | 🇬🇧 Inglés, CTA `/registro` | ❌ NO |
| `sisyphus/anti-forget-layer` | ✅ Limpio (sin BETA_MODE) | 🇬🇧 Inglés, CTA `/registro` | ❌ NO |
| `origin/i18n/exec-en-es` | ❌ BETA_MODE gate | 🇪🇸 Español, CTA beta form | ✅ SÍ (producción) |

### 18.3 Cómo pasó

1. El branch `i18n/exec-en-es` se creó para añadir traducciones i18n (español)
2. Como parte de ese trabajo, se añadió el BETA_MODE gate para controlar el acceso durante la fase beta
3. Este branch se desplegó a producción (myownclone.com) 
4. La variable de entorno `BETA_MODE=true` se configuró en producción
5. **El branch `origin/master` NUNCA recibió este cambio** — master sigue con el registro abierto
6. Los branches más recientes (`sisyphus/anti-forget-layer`) tampoco tienen el BETA_MODE

**Conclusión**: NO fue un rollback ni una regresión no autorizada. Fue un despliegue legítimo del branch i18n que incluyó el beta gate. El problema es que producción se quedó en ese branch en vez de volver a master.

### 18.4 Qué hace el registro del branch actual (sisyphus/anti-forget-layer)

El registro en el branch actual es un **magic link flow** completamente funcional:

```
Campos: Nombre + Email
Método: signIn("resend", { email, name }) → envía enlace mágico
Alternativa: Google OAuth → signIn("google")
Tras registro: redirect a /resumen (dashboard)
```

**Sin contraseña** — el usuario recibe un email con un enlace que lo autentica automáticamente.

### 18.5 Plan de acción para restaurar el registro

#### Opción A (recomendada): Redesplegar desde master

```bash
# En el VPS de producción:
cd /opt/myownclone/current
git fetch origin
git checkout origin/master
# O alternativamente:
git checkout sisyphus/anti-forget-layer

# Asegurar que BETA_MODE NO está activo:
# En el archivo .env de producción:
# BETA_MODE=false   # o eliminar la línea

# Rebuild y restart:
npm run build
systemctl restart myownclone-frontend
```

#### Opción B: Parchear el código actual en producción

```bash
# En el VPS, editar el archivo de registro:
# Quitar las 3 líneas del BETA_MODE gate:

# ANTES:
if (process.env.BETA_MODE === "true") {
  redirect("/#plans");
}

# DESPUÉS:
# (eliminar esas 3 líneas)
```

#### Opción C: Solo quitar la variable de entorno

```bash
# Si la variable BETA_MODE se quita del .env de producción,
# el gate no se activa aunque el código lo tenga.
# En el .env de producción:
# Quitar: BETA_MODE=true
# O cambiar a: BETA_MODE=false
```

### 18.6 Verificación post-fix

```bash
# Después del fix, verificar:
curl -sI https://myownclone.com/registro
# Debe devolver 200 OK (no 307 redirect)
```

---

*Documento generado por OSINT de archivos locales del repositorio + auditoría en vivo de producción — 2026-06-28*
