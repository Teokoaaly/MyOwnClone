---
source_url: file:///home/haxth3/myownclone-frontend-recon.md
ingested: 2026-05-25
sha256: aa6f16e91016f19a5b24dd7d12030eb8b5e33d55b00b1bb6cdd4ce3325af134f
---

# myownclone Frontend Reconnaissance Report

## Overview
- **URLs**: app.myownclone.com, myownclone.com (same Next.js monorepo), api.myownclone.com (serves same app HTML)
- **Framework**: Next.js 16.2.4 (Turbopack), React 19
- **Hosting**: Vercel (x-powered-by: Next.js, server: Vercel)
- **Deployment ID**: dpl_8jxBD8eEioaPmHarRs3eofX1Ks3S
- **Release**: 3cd116d948dc38b980833dd9d465bcffbc8fd443
- **Company**: Marea Kiss LLC
- **i18n**: Spanish (es, default) + English (en)
- **Locale paths**: / (es), /en (en)
- **Time Zone**: Europe/Madrid
- **Fonts**: Poppins, JetBrains Mono

## Third-Party Services Exposed in JS

### PostHog
- API Key: phc_tn48YvixjuzzdhbNFLzt9hD7TfwbH2AssUxG2gAiPWei
- API Host: https://eu.i.posthog.com
- SDK Version: 1.373.4

### Sentry
- Public Key: 6b2d7ed6999454df87ccf844aa85ba70
- Org ID: 4511315838173184
- Environment: vercel-production
- Sample Rate: 0.1

## Theme
- localStorage key: "myownclone-theme"
- Values: "dark" | "light"
- CSS Variables: --bg, --fg, --fg-muted, --bg-muted, --surface, --border, --accent, --accent-fg, --accent-hover, --brand-lime, --radius, --radius-lg

## Feature List (from i18n translations)

### Core Product
- AI clone trained on creator content (videos, courses, PDFs, websites)
- 3 silos: Teaching, Support, Product Recommendations
- Chat surface with knowledge/terms/personality
- Public clone URL: subdomain.myownclone.com (custom domain supported)

### Admin Dashboard (/admin/*)
Routes (ES/EN bilingual):
- /admin (redirects to /login if unauthenticated)
- /admin/clone | /admin/clon - Clone config
- /admin/identity | /admin/identidad - Identity
  - /general, /purpose | /proposito, /style | /estilo, /voice-call | /llamada
- /admin/brain | /admin/cerebro - Brain/knowledge
  - /knowledge | /conocimiento, /products | /productos, /support | /soporte, /terms | /terminos
- /admin/library | /admin/biblioteca - Content library
- /admin/learning | /admin/aprendizajes - Learning
  - /audience | /audiencia, /feedback, /gaps, /questions | /preguntas
- /admin/products | /admin/productos - Products
  - /courses | /cursos, /consulting | /consultorias, /downloads | /descargables, /masterclasses, /external | /externos
- /admin/conversations | /admin/conversaciones
- /admin/contacts | /admin/contactos
- /admin/meetings | /admin/reuniones - Meetings
  - /agenda, /availability | /disponibilidad, /integrations | /integraciones, /recordings | /grabaciones, /types | /tipos
- /admin/inbox - Inbox
  - /triage, /new | /nuevo, /settings | /configuracion, /signature | /firma, /memories | /memorias, /templates | /plantillas
- /admin/usage | /admin/uso - Usage
  - /plan, /team | /equipo, /invoices | /facturas, /resumen

### Platform Admin (/admin/platform/*)
- /admin/platform - Dashboard ("Resumen")
- /admin/platform/tenants - Tenant management
- /admin/platform/feedback
- /admin/platform/faqs

### Platform Features
- **MRR tracking**: Pro, Scale, Enterprise tiers
- **Tenants**: search/sort/filter, impersonate ("View as"), invite/grant plans
- **Impersonation**: "Support mode" with auto-expire (30 min), audit trail, red banner
- **Comp plans**: Free (forever/N months/until date) or Stripe trial (30 days with card)
- **Feedback widget**: with screenshot paste (Ctrl+V), 5MB limit
- **Inbox**: Labels, spam domains, ticket management
- **Cost tracking**: Anthropic + OpenAI + email, split by chat/ops

### Triage Mode
- AI-powered inbox processing
- Draft email proposals with send
- Memory proposals (create/update) from AI suggestions
- Template proposals (create/update) - reusable replies
- Label proposals (create/assign) - auto-classify by intent
- Thread history view
- Voice notes with transcription
- Process without reply (dismiss)

### Meetings
- Booking page (PublicBooking) with calendar, timezone detection
- Video calls "on myownclone"
- Recording with transcript
- ICS calendar download (Google, Outlook, Office 365, Apple)
- Clone chat bubble on recording pages

## Public Routes (from sitemap/robots)
- / (landing)
- /login
- /registro (signup, Spanish)
- /en/login, /en/signup, /en/signup/onboarding, /en/signup/success
- /contacto, /en/contact
- /legal/aviso-legal, /legal/privacidad, /legal/cookies, /legal/terminos, /legal/dpa, /legal/clon-terms
- /en/legal/privacy, /en/legal/cookies, /en/legal/terms, /en/legal/dpa, /en/legal/clon-terms

## Robots.txt Disallowed Paths
- /admin, /admin/
- /api/
- /embed/
- /__t/
- /c/
- /registro/onboarding, /registro/exito
- /en/admin, /en/admin/
- /en/signup/onboarding, /en/signup/success

## API Endpoint Patterns
The app uses Next.js Server Actions (RSC) for mutations - no traditional REST API endpoints were found in the client bundles. Key observations:
- API calls go through the same Next.js server (RSC protocol)
- No separate API subdomain in use (api.myownclone.com serves the same app)
- PostHog sends to eu.i.posthog.com /i/v1/logs
- Sentry reports errors to sentry.io
- No websocket/SSE endpoints found in client bundles
- No tRPC or GraphQL endpoints detected

## Plans/Pricing
- **Pro, Scale, Enterprise** tiers
- Stripe Checkout for payments
- Stripe trial: 30 days, auto-charge at month end
- Complimentary plans available via platform admin
- Subscription statuses: active, trialing, past_due, unpaid, canceled, incomplete, none, complimentary

## Email
- Default inbound: contacto@myownclone.com
- Custom inbound domains: "Coming soon"

## Key Observations
1. app.myownclone.com and myownclone.com are the SAME Next.js app
2. admin.myownclone.com doesn't exist as separate subdomain
3. Admin panel is at /admin on the main domain
4. Unauthenticated /admin redirects to /login (NEXT_REDIRECT;replace;/login;307)
5. The app is in beta - manual onboarding case by case
6. API is handled via Next.js RSC (React Server Components/Server Actions) - no exposed REST API

## JS Bundles Analyzed
- 01bvdg0qobpd1.js (188KB) - PostHog SDK
- 04fz47a9tgdfk.js (432KB) - Next.js framework + Sentry
- 0r297qmiczcw7.js (21KB) - i18n + route definitions (where admin routes were found)
- 030hv~7rpb7~s.js (41KB) - app shell
- 134azxwlkjf6d.js, 0~bq0m56ze-vu.js - admin-specific pages
- 0hvc~tg65bk-t.js (25KB) - login page specific
- 0x4l9ewfu263y.js - contact page specific
