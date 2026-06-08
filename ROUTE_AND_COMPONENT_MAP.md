# ROUTE AND COMPONENT MAP — MyOwnClone

> Authoritative inventory of routes, components, and the API surface they touch. Use this to plan cross-cutting changes.

## 1. Frontend routes (Next.js App Router)

### Public

| Path | Layout | File | Auth |
|---|---|---|---|
| `/` | `app/layout.tsx` | `app/page.tsx` | None |
| `/login` | `app/layout.tsx` | `app/login/page.tsx` | None |
| `/registro` | `(dashboard)/layout.tsx` | `app/(dashboard)/registro/page.tsx` | None |
| `/es/verificar` | `app/layout.tsx` | `app/es/verificar/page.tsx` | Email link |
| `/es/onboarding` | `app/layout.tsx` | `app/es/onboarding/page.tsx` | Email link |
| `/[slug]` | `(public)/layout.tsx` | `app/(public)/[slug]/page.tsx` | None (public clone) |
| `/widget.js` | n/a | `app/widget.js` | None (embed) |

### Dashboard (auth)

| Path | File | Calls |
|---|---|---|
| `/resumen` | `app/(dashboard)/resumen/page.tsx` | `/api/clone/analytics/overview` |
| `/biblioteca` | `app/(dashboard)/biblioteca/page.tsx` | (TBD) |
| `/biblioteca/nuevo` | `app/(dashboard)/biblioteca/nuevo/page.tsx` | (TBD) |
| `/cerebro` | `app/(dashboard)/cerebro/page.tsx` | (TBD) |
| `/inbox` | `app/(dashboard)/inbox/page.tsx` | (TBD) |
| `/productos` | `app/(dashboard)/productos/page.tsx` | (TBD) |
| `/reuniones` | `app/(dashboard)/reuniones/page.tsx` | (TBD) |
| `/analiticas` | `app/(dashboard)/analiticas/page.tsx` | (TBD) |
| `/facturacion` | `app/(dashboard)/facturacion/page.tsx` | (TBD) |
| `/configuracion` | `app/(dashboard)/configuracion/page.tsx` | (TBD) |

### Admin (platform_admin only)

| Path | File | Calls |
|---|---|---|
| `/admin/resumen` | `app/admin/resumen/page.tsx` | `/api/admin/overview` |
| `/admin/tenants` | `app/admin/tenants/page.tsx` | `/api/admin/tenants` |
| `/admin/tenants/[id]` | `app/admin/tenants/[id]/page.tsx` | `/api/admin/tenants/[id]` |
| `/admin/feedback` | `app/admin/feedback/page.tsx` | `/api/admin/feedback` |
| `/admin/audit` | (TO CREATE) | `/api/admin/audit-log` |
| `/admin/impersonation` | (TO CREATE) | `/api/admin/impersonate` |
| `/admin/courtesy` | (TO CREATE) | `/api/admin/courtesy` |

## 2. Next.js API routes (BFF / proxy)

| Path | File | Purpose |
|---|---|---|
| `/api/admin/[...path]` | `app/api/admin/[...path]/route.ts` | Proxy to Flask admin, validates NextAuth + DB role, forwards `X-Admin-Token` |
| `/api/auth/[...nextauth]` | `app/api/auth/[...nextauth]/route.ts` | NextAuth |
| `/api/csrf` | `app/api/csrf/route.ts` | CSRF token (TBD) |
| `/api/clone/[...path]` | `app/api/clone/[...path]/route.ts` | Proxy to Flask user endpoints |
| `/api/clone/[slug]` | `app/api/clone/[slug]/route.ts` | Clone-scoped endpoints |
| `/api/clone/[slug]/chat` | `app/api/clone/[slug]/chat/route.ts` | Chat |
| `/api/clone/billing` | `app/api/clone/billing/route.ts` | Stripe billing |
| `/api/clone/feedback` | `app/api/clone/feedback/route.ts` | User feedback |
| `/api/clone/inbox` | `app/api/clone/inbox/route.ts` | Inbox |
| `/api/clone/inbox/[id]` | `app/api/clone/inbox/[id]/route.ts` | Message detail |
| `/api/clone/inbox/[id]/generate-draft` | `app/api/clone/inbox/[id]/generate-draft/route.ts` | Draft |
| `/api/clone/inbox/list` | `app/api/clone/inbox/list/route.ts` | List messages |
| `/api/clone/plans` | `app/api/clone/plans/route.ts` | Plan listing |
| `/api/clone/stripe` | `app/api/clone/stripe/route.ts` | Stripe webhook |
| `/api/clone/stripe/checkout` | `app/api/clone/stripe/checkout/route.ts` | Checkout session |
| `/api/bookings` | `app/api/bookings/route.ts` | Bookings |
| `/api/inbound-email` | `app/api/inbound-email/route.ts` | Inbound email webhook |
| `/api/stt` | `app/api/stt/route.ts` | Speech-to-text |

## 3. Backend endpoints (Flask)

### Auth

| Method | Path | File | Auth |
|---|---|---|---|
| POST | `/console/api/auth/login` | `api/api/controllers/console/auth.py` | None (rate-limited) |
| GET | `/console/api/auth/verify` | `api/api/controllers/console/auth.py` | Bearer |

### Admin (platform_admin only)

| Method | Path | File |
|---|---|---|
| GET | `/console/api/myownclone/admin/overview` | `api/api/controllers/console/myownclone/admin_platform.py` |
| GET | `/console/api/myownclone/admin/tenants` | same |
| GET | `/console/api/myownclone/admin/tenants/<id>` | same |
| PATCH | `/console/api/myownclone/admin/tenants/<id>` | same |
| GET | `/console/api/myownclone/admin/feedback` | same |
| POST | `/console/api/myownclone/admin/impersonate` | same |
| POST | `/console/api/myownclone/admin/impersonate/stop` | same |
| GET | `/console/api/myownclone/admin/audit-log` | same |
| POST | `/console/api/myownclone/admin/courtesy` | same |

### User (clones, inbox, etc.)

| Method | Path | File |
|---|---|---|
| GET | `/console/api/myownclone/clone/...` | `controllers/console/myownclone/clone.py` |
| GET | `/console/api/myownclone/inbox/...` | `controllers/console/myownclone/inbox.py` |
| POST | `/console/api/myownclone/feedback` | `controllers/console/myownclone/feedback.py` |
| GET | `/console/api/myownclone/creator-memory/...` | `controllers/console/myownclone/creator_memory.py` |
| GET | `/console/api/myownclone/analytics/...` | `controllers/console/myownclone/analytics.py` |
| POST | `/console/api/myownclone/stripe/...` | `controllers/console/myownclone/stripe_ctrl.py` |
| GET | `/console/api/myownclone/booking/...` | `controllers/console/myownclone/booking.py` |

### Public (clone widget)

| Method | Path | File |
|---|---|---|
| GET | `/api/myownclone/clone/<slug>/chat` | `controllers/myownclone_public.py` |
| GET | `/api/myownclone/clone/<slug>/...` | same |

## 4. Components and where they're used

| Component | Used in |
|---|---|
| `Sidebar` | `app/(dashboard)/layout.tsx` (reused); `app/admin/layout.tsx` should reuse but currently duplicates |
| `HeaderBreadcrumb` | `app/(dashboard)/resumen/page.tsx` |
| `StatsCard` | `app/(dashboard)/resumen/page.tsx` |
| `QuickActionCard` | `app/(dashboard)/resumen/page.tsx` |
| `OnboardingBanner` | `app/(dashboard)/resumen/page.tsx` |
| `EndpointCard` | `app/(dashboard)/resumen/page.tsx` |
| `ChatOrb` | `app/(dashboard)/resumen/page.tsx` |
| `ChatPanel` / `MessageBubble` / `SiloToggle` | (TBD — chat pages) |
| `NavIcons` | Sidebar, dashboard layout |
| `ShortcutIcons` | resumen page |
| `ContentTypeIcons` | (TBD — biblioteca) |
| `SiloIcons` | (TBD — clon mode UI) |
| `ToneIcons` | (TBD) |
| `StatusIcons` | (TBD — inbox filters) |
| `UiIcons` | (TBD — buttons, toasts) |

## 5. Drizzle schema (`replica/src/lib/db/schema/`)

- `users.ts` — NextAuth users (includes `role` for NextAuth-based role checks in the proxy)
- `tenants.ts` — Drizzle mirror of Flask `tenants` (only for read-only auth context; not used for admin mutations)
- `sources.ts` — knowledge sources
- `emails.ts` — inbound email
- `conversations.ts` — chat conversations
- `clones.ts` — clone configs
- `chunks.ts` — RAG chunks
- `bookings.ts` — bookings
- `analytics.ts` — analytics aggregations
- `index.ts` — barrel

**Important**: Flask is the canonical source of truth for admin tables. Drizzle is for auth + user-side data only. This is documented to prevent drift.

## 6. Backend models (SQLAlchemy)

| File | Models |
|---|---|
| `api/api/models/account.py` | `Account`, `Tenant` (real Dify base + MyOwnClone additions) |
| `api/api/models/analytics.py` | `CostTracking`, `Plan`, `AnalyticsQuestion`, `AnalyticsGap`, `ImpersonationLog`, `ImpersonationToken`, `Feedback`, `AdminAuditLog` |
| `api/api/models/clone.py` | `CloneConfig`, `CloneModePrompt`, `CloneSilo`, `CreatorMemory`, `CreatorMemoryType` |
| `api/api/models/email.py` | `EmailInbound`, `EmailInboundStatus`, `EmailTemplate` |
| `api/api/models/meeting.py` | `MeetingType_`, `Availability`, `Booking`, `BookingStatus`, `Product` |
| `api/api/models/myownclone/__init__.py` | Re-exports for `from api.models.myownclone import X` |

## 7. Migrations (Alembic)

| File | Purpose |
|---|---|
| `a1b2c3d4e5f6_add_myownclone_core_tables.py` | Initial MyOwnClone tables (tenants, accounts, clones, etc.) |
| `b2c3d4e5f6a7_add_myownclone_columns_to_existing_tables.py` | Adds slug, plan, custom_domain, subscription_status to tenants; role to accounts |
| `c3d4e5f6a7b8_seed_myownclone_plans.py` | Seeds the 5 plans with prices |
| `d4e5f6a7b8c9_add_custom_domain_to_clone_configs.py` | Adds custom_domain to clone_configs |
| `e5f6a7b8c9d0_add_impersonation_tokens.py` | Impersonation tokens table |
| `2026_06_03_0930_add_myownclone_missing_indexes.py` | Indexes for performance |
| `2026_06_04_1000-b1c2d3e4f5a6_add_admin_audit_log.py` | admin_audit_log table |

## 8. Cross-cutting dependencies

- **Auth**: Next.js (NextAuth) + Flask (JWT) + Proxy (X-Admin-Token). The proxy validates the NextAuth session and the DB role before forwarding. The Flask endpoint also re-validates the role from the JWT claim or DB. **Two layers of defense**.
- **Multi-tenancy**: only enforced by application convention. No global `tenant_id` filter at the ORM level. Admin endpoints explicitly bypass tenant scoping.
- **i18n**: `next-intl` configured with `locale = "es"` in `app/layout.tsx`. Spanish is the only locale; `en` is implicit.
- **CSS**: Tailwind 4 via `@tailwindcss/postcss` + `@import "tailwindcss"` in `globals.css`. Design tokens are CSS custom properties exposed via Tailwind's `@theme inline` block.
- **Charts**: NO chart library installed. Phase D8 will add `recharts` (~100KB, MIT, tree-shakeable).
