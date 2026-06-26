---
source_url: file:///home/haxth3/myownclone_scrape_findings.md
ingested: 2026-05-25
sha256: 9ad31de2cc666afeedaf7d8722765dae3fe1551b3a3473c9199e1857f1d8efbe
---

# myownclone Public Website Scrape Report
**Date:** 2026-05-25
**Sites scraped:** myownclone.com, app.myownclone.com, api.myownclone.com

---

## 1. INFRASTRUCTURE & HOSTING

- **Hosting:** Vercel (all three subdomains)
- **Framework:** Next.js (App Router) with Turbopack
- **i18n:** `@next/intl` — Spanish (default, `/`) and English (`/en`)
- **Server:** `x-powered-by: Next.js`, `server: Vercel`
- **Deployment ID:** `dpl_8jxBD8eEioaPmHarRs3eofX1Ks3S`
- **Release:** `3cd116d948dc38b980833dd9d465bcffbc8fd443`
- **Vercel Regions:** cdg1 (Paris)
- **Fonts:** Poppins (variable), JetBrains Mono (variable) — loaded as woff2 via Next.js font optimization
- **Polyfill:** core-js 3.38.1
- **DNS:** All three subdomains resolve via Vercel (no CNAME/A records visible via dig ANY)

### Subdomain Behavior
All three subdomains (`myownclone.com`, `app.myownclone.com`, `api.myownclone.com`) serve IDENTICAL HTML — a monorepo Next.js app. The app handles routing internally; there is no separate API or app server.

---

## 2. OBSERVABILITY / ANALYTICS

### Sentry
- **DSN/Public Key:** `6b2d7ed6999454df87ccf844aa85ba70`
- **Organization ID:** `4511315838173184`
- **Environment:** `vercel-production`
- **Integration:** `@sentry/nextjs` — App Router instrumentation
- **Tracing:** Enabled (`__SENTRY_TRACING__`)
- **Tunnel:** Sentry tunnel path rewrites configured
- **Meta tags:** `sentry-trace` and `baggage` on every page

### PostHog
- **Heavy integration** — the main JS chunk (187KB) is dominated by PostHog SDK code
- **Features used:**
  - Feature flags
  - Session recording (with rageclick detection)
  - Surveys
  - Product tours
  - Conversations (chat/widget)
  - Web analytics (pageview, pageleave, autocapture)
  - Performance/web vitals (LCP, CLS, FCP, INP)
  - Dead click autocapture
  - Error tracking integration
  - Toolbar/editor
  - Site apps
- **PostHog API host pattern:** `https://{region}.posthog.com` (configured in SDK)
- **PostHog UI:** `https://app.posthog.com/home`
- **Cookieless mode support** configured
- **External integrations configured:** Intercom, Crisp Chat (integration keys found)

### Error Tracking
- Double coverage: both Sentry AND PostHog error tracking
- PostHog wraps `onerror`, `unhandledrejection`, `console.error`
- Bot detection: extensive user-agent bot list for filtering analytics

---

## 3. ALL PUBLIC PAGES (from sitemap + robots.txt)

### Sitemap (https://www.myownclone.com/sitemap.xml)
| Path | Spanish | English | Priority | Change Freq |
|------|---------|---------|----------|-------------|
| `/` | `/` | `/en` | 1.0 | weekly |
| `/login` | `/login` | `/en/login` | 0.3 | yearly |
| `/registro` | `/registro` | `/en/signup` | 0.9 | monthly |
| `/legal/aviso-legal` | `/legal/aviso-legal` | (same) | 0.2 | yearly |
| `/legal/privacidad` | `/legal/privacidad` | `/en/legal/privacy` | 0.2 | yearly |
| `/legal/cookies` | `/legal/cookies` | `/en/legal/cookies` | 0.2 | yearly |
| `/legal/terminos` | `/legal/terminos` | `/en/legal/terms` | 0.2 | yearly |
| `/legal/dpa` | `/legal/dpa` | `/en/legal/dpa` | 0.2 | yearly |
| `/legal/clon-terms` | `/legal/clon-terms` | `/en/legal/clon-terms` | 0.2 | yearly |
| `/contacto` | `/contacto` | `/en/contact` | (not in sitemap) | — |

### Live paths discovered (not in sitemap):
- `/admin` → 200 (redirects to homepage, auth-gated)
- `/contacto` → 200
- `/en/contact` → 200
- `/api/webhooks/stripe` → **405 Method Not Allowed** (confirms Stripe webhook endpoint exists!)

### Robots.txt disallowed paths:
- `/admin` — admin panel (requires auth)
- `/api/` — API routes (all return 404 or 405, not publicly accessible)
- `/embed/` — embeds (404)
- `/__t/` — likely toolbar/tracking (404)
- `/c/` — likely clone shortlinks (404)
- `/registro/onboarding` — onboarding flow
- `/registro/exito` — success page
- `/en/admin` — English admin
- `/en/signup/onboarding` — English onboarding
- `/en/signup/success` — English success

### Pages that 404 (do NOT exist):
- /pricing, /plans, /features, /blog, /changelog, /roadmap, /docs, /documentation, /about, /register, /terms, /privacy (all 404)

---

## 4. HOMEPAGE CONTENT

### Spanish (myownclone.com)
- **Title:** "Tu clon de IA, entrenado con tu contenido"
- **H1:** "Crea tu clon y haz que trabaje por ti."
- **Tagline:** "Tu aliado perfecto para tu negocio online."
- **Beta notice:** "myownclone está en fase beta. Queremos acompañar a cada cliente en la integración con su negocio, así que de momento entramos caso por caso. Escríbenos contándonos el tuyo y vemos si encaja."
- **CTA:** "Cuéntanos tu caso" → links to /contacto
- **Header nav:** "Iniciar sesión" (Sign in) only
- **Footer:** Escríbenos, Aviso legal, Privacidad, Cookies, Términos, DPA

### English (myownclone.com/en)
- **Title:** "Your AI clone, trained on your content"
- **H1:** "Build your clone and let it work for you."
- **Tagline:** "Your perfect partner for your online business."
- **Beta notice:** "myownclone is in beta. We want to walk every customer through their integration, so for now we onboard case by case. Tell us about yours and we'll see if it's a fit."
- **CTA:** "Tell us your case" → links to /en/contact
- **Header nav:** "Sign in" only
- **Footer:** Contact us, Privacy, Cookies, Terms, DPA

### Key product description (from meta/JSON-LD):
> "myownclone gives creators an AI clone trained on their own content — pedagogy, support, and product recommendations on a single chat surface."

### Spanish meta description:
> "Crea un clon que enseña, da soporte y recomienda tus productos. Entrenado solo con lo que tú decides — vídeos, cursos, PDFs, web."

### English meta description:
> "Build a clone that teaches, supports, and recommends your products. Trained only on what you choose — videos, courses, PDFs, websites."

### Product feature keywords extracted from copy:
- **Pedagogy / Teaching:** "enseña" / "teaches"
- **Support:** "da soporte" / "supports"
- **Product Recommendations:** "recomienda tus productos" / "recommends your products"
- **Content Sources:** videos, courses, PDFs, websites
- **Interface:** "una sola superficie de chat" / "a single chat surface"
- **Opt-in silos:** "tres silos opt-in" / "three opt-in silos" (pedagogy, support, recommendations)
- **Training:** "entrenado solo con lo que tú decides" / "trained only on what you choose"

---

## 5. CONTACT PAGE

### Spanish (myownclone.com/contacto)
- **Title:** "Contacto · myownclone"
- **H1:** "Cuéntanos tu caso."
- **Subtitle:** "Y te respondemos lo antes posible."
- **Form fields:**
  - Nombre (Name) — required, 2-80 chars
  - Email — required, max 254 chars
  - Mensaje (Message) — required, 20-3000 chars, placeholder: "Cuéntanos tus dudas o tu caso concreto y te explicamos cómo podemos ayudarte y si myownclone es para ti."
  - Honeypot field: "website" (hidden, anti-spam)
  - Hidden field: locale="es"
- **Form type:** multipart/form-data, POST
- **Server Action:** Next.js Server Action
  - Action ID: `6099af3b3ab1c96b73100889f9e2f9b19fd2bcdbb9`
  - Action Key: `kf4d3b1191473e442e1ccd7782f2f9e97`
- **Submit button:** "Enviar"
- **Header:** Crear cuenta (Create account) + Acceder (Sign in)

### `/registro` redirects to `/contacto`
The signup page (`/registro`) meta-refreshes to `/contacto` — there is NO self-service signup. All onboarding is manual/white-glove.

### `/login` page
- **Title:** "Iniciar sesión · myownclone"
- **Description:** "Accede a tu panel de myownclone."
- **Content:** BAILOUT_TO_CLIENT_SIDE_RENDERING — the login form is a client-side React component (skeleton loading state visible in HTML)

---

## 6. META TAGS & OPENGRAPH

### Spanish Homepage
```
title: Tu clon de IA, entrenado con tu contenido
description: Crea un clon que enseña, da soporte y recomienda tus productos. Entrenado solo con lo que tú decides — vídeos, cursos, PDFs, web.
og:title: Tu clon de IA, entrenado con tu contenido
og:description: (same as description)
og:url: https://www.myownclone.com
og:locale: es_ES
og:image: https://www.myownclone.com/es/opengraph-image?1b2d46d437b07cd3
og:image:type: image/png
og:image:width: 1200
og:image:height: 630
og:image:alt: myownclone
twitter:card: summary
twitter:title: Tu clon de IA, entrenado con tu contenido
twitter:description: (same as description)
twitter:image: https://www.myownclone.com/es/opengraph-image?1b2d46d437b07cd3
application-name: myownclone
theme-color: #ffffff (light) / #0a0a0c (dark)
```

### English Homepage
```
title: Your AI clone, trained on your content
description: Build a clone that teaches, supports, and recommends your products. Trained only on what you choose — videos, courses, PDFs, websites.
og:title: Your AI clone, trained on your content
og:url: https://www.myownclone.com/en
og:locale: en_US
og:image: https://www.myownclone.com/en/opengraph-image?1b2d46d437b07cd3
twitter:card: summary
```

### Registro (meta-refresh to /contacto)
```
title: myownclone — Tu clon de IA entrenado con tu contenido
description: myownclone convierte tu contenido en un clon de IA que enseña, da soporte y recomienda tus productos. Una sola superficie de chat, tres silos opt-in.
og:title: myownclone — Tu clon de IA entrenado con tu contenido
og:site_name: myownclone
og:type: website
twitter:card: summary_large_image
```

---

## 7. PRICING

**NO PUBLIC PRICING PAGE EXISTS.** All pricing-related paths (/pricing, /plans) return 404. The beta onboarding is case-by-case ("entramos caso por caso"). No pricing information is visible anywhere on the public site.

---

## 8. BLOG / CHANGELOG / ROADMAP / DOCS

**NONE EXIST PUBLICLY.** All of the following return 404:
- /blog
- /changelog
- /roadmap
- /docs
- /documentation

There are no links to external blogs, changelogs, or documentation from any page.

---

## 9. JS BUNDLE ANALYSIS — API ENDPOINTS & INTERNAL STRUCTURE

### Stripe Integration (CONFIRMED)
- `/api/webhooks/stripe` → **HTTP 405 Method Not Allowed**
- This confirms Stripe is integrated for payment processing
- The webhook endpoint is server-side only (POST required)

### PostHog Analytics Endpoints (client-side)
- `/e/` — event ingestion
- `/i/v1/logs` — log ingestion
- `/array/` — feature flags
- `/decide/` — feature flag decisions
- `/api/surveys/` — surveys
- `/api/product_tours/` — product tours
- `/person/` — person profiles
- `/project/` — project settings
- `/replay/` — session replays
- `/static/` — static assets
- `/config` — remote config

These are all PostHog's own endpoints, consumed by the PostHog JS SDK.

### Sentry Endpoints
- Sentry tunnel path rewrites configured (internal Next.js routing)
- Envelope endpoint for error/transaction submission

### External Integrations
- **Intercom:** integration key `intercom-integration` found
- **Crisp Chat:** integration key `crisp-chat-integration` found

### Authentication
- No Supabase client code found in any JS bundle
- No Auth0, Clerk, NextAuth, or other auth provider client code found
- Authentication likely handled server-side (Next.js Server Actions + server-side sessions)
- Login page is a client-side rendered React component (bailout from RSC)

### AI/LLM Services
- No OpenAI, Anthropic, Cohere, or other LLM API keys/endpoints found in client JS
- AI training/inference is likely server-side only

### Internal API Patterns
- Next.js Server Actions used for form submissions (contact form)
- RSC (React Server Components) protocol used for page rendering
- No REST API endpoints visible on client side
- No GraphQL endpoints found
- No WebSocket endpoints found

### CSS Custom Properties (Design System)
```
--bg: background color
--fg: foreground/text color
--fg-muted: muted text color
--fg-faint: faint/subtle text
--bg-muted: muted background
--bg-subtle: subtle background
--surface: surface/card background
--surface-hover: surface hover state
--border: border color
--radius: border radius
--accent: accent color (CTA buttons)
--accent-fg: accent text color
--accent-hover: accent hover state
--brand-lime: brand lime green (logo color)
```

### Theme System
- Dark/Light mode via localStorage key `myownclone-theme`
- CSS class `dark` toggled on `<html>`
- System preference detection via `prefers-color-scheme`

### Logo
- SVG: Arc path + circle, lime green (#brand-lime) on dark background (#0a0a0c)
- Favicon: `/myownclone-favicon.svg`

---

## 10. LEGAL PAGES

### Available legal documents:
| Path | Title | 
|------|-------|
| `/legal/aviso-legal` | Aviso Legal |
| `/legal/privacidad` | Política de Privacidad |
| `/legal/cookies` | Política de Cookies |
| `/legal/terminos` | Términos del Servicio |
| `/legal/dpa` | Data Processing Agreement |
| `/legal/clon-terms` | Clone-specific Terms |

---

## 11. SUMMARY OF KEY FINDINGS

1. **myownclone is an AI clone platform** for creators — it trains a chatbot clone on the creator's own content (videos, courses, PDFs, websites) that can teach, support customers, and recommend products.

2. **Three opt-in "silos":** Pedagogy (teaching), Support, Product Recommendations — all on a single chat interface.

3. **Early-stage / beta:** No self-service signup, no public pricing, white-glove onboarding. Users must fill out a contact form to get access.

4. **Tech stack:** Next.js (App Router + Turbopack) on Vercel, with PostHog for analytics, Sentry for error tracking, Stripe for payments, and Intercom/Crisp for customer communication.

5. **No public API documentation, blog, changelog, roadmap, or pricing** — the product is in a pre-launch/stealth phase.

6. **AI model details are entirely server-side** — no client-side references to which LLM or training pipeline is used.

7. **Multi-tenant app:** The same Next.js app serves the marketing site, the web app, and the API — routing is handled internally. `app.myownclone.com` and `api.myownclone.com` are aliases pointing to the same deployment.

8. **Internationalization:** Spanish-first (based in Spain/ES?), with English translations available. Legal docs suggest Spanish jurisdiction.

9. **Stripe webhook endpoint confirmed** at `/api/webhooks/stripe` (HTTP 405 = exists but requires POST).

10. **Contact form uses Next.js Server Actions** — form submission is handled server-side with anti-spam honeypot.
