# Live re-verification — myownclone.com

**Captured:** 2026-10-22, 06:07–06:15 UTC
**Method:** `curl` against the live public site (unauthenticated GET/POST, desktop Chrome UA)
**Why:** The OSINT backlog in `raw/articles/` describes the deployment as of May–June 2026. The Editor run re-checked the live site because the `admin-p2-fuga-codigo-panel-sin-auth` atom was explicitly flagged as requiring curl re-verification. The re-verification shows the deployment is **no longer the one the atoms describe**.

---

## 1. Hosting and DNS — the deployment moved off Vercel

```
$ dig +short myownclone.com A
212.227.169.99

$ curl -sSI https://myownclone.com/
HTTP/1.1 200 OK
Server: nginx/1.28.3 (Ubuntu)
X-Powered-By: Next.js
Content-Type: text/html; charset=utf-8
```

No `x-vercel-id`, no `x-vercel-cache`, no `x-matched-path`, no `via`. The site is now served by **nginx 1.28.3 on Ubuntu**, self-hosted, fronting a Next.js app.

TLS:

```
issuer=C = US, O = Let's Encrypt, CN = YE1
subject=CN = myownclone.com
notBefore=Oct 14 03:54:44 2026 GMT
notAfter=Jan 12 03:54:43 2027 GMT
```

The certificate was issued **2026-10-14** — eight days before this capture.

Subdomain DNS (all resolve to the same IP, all serve byte-identical HTML):

| Host | DNS | HTTP |
|---|---|---|
| `myownclone.com` | 212.227.169.99 | 200 |
| `www.myownclone.com` | 212.227.169.99 | 200 (md5-identical to apex) |
| `app.myownclone.com` | **NO_DNS** | — |
| `api.myownclone.com` | **NO_DNS** | — |
| `admin.myownclone.com` | **NO_DNS** | — |
| `docs.myownclone.com` | **NO_DNS** | — |
| `status.myownclone.com` | **NO_DNS** | — |
| `dashboard.myownclone.com` | **NO_DNS** | — |
| `support.myownclone.com` | **NO_DNS** | — |

`http://myownclone.com/` → `301` to `https://myownclone.com/`.

## 2. Security headers — now present

```
Content-Security-Policy: default-src 'self' https: data: blob:;
  script-src 'self' 'unsafe-inline' 'unsafe-eval' https:;
  style-src 'self' 'unsafe-inline' https:;
  img-src 'self' data: blob: https:;
  font-src 'self' data: https:;
  media-src 'self' blob: data: https:;
  connect-src 'self' https: ws: wss:;
  object-src 'none'; base-uri 'self'; form-action 'self'; frame-ancestors 'none'
Referrer-Policy: strict-origin-when-cross-origin
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Permissions-Policy: camera=(), microphone=(), geolocation=()
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```

On `/admin` and `/registro` a **second, stricter** CSP is also present alongside the above
(`script-src 'self' 'unsafe-inline' https:` — no `unsafe-eval`; `frame-ancestors 'none'`).

CORS, with `Origin: https://evil.example`:

```
/login     NO access-control-allow-origin header
/registro  NO access-control-allow-origin header
```

Rate limiting — no 429 observed:

```
GET /login   x12  → 200 200 200 200 200 200 200 200 200 200 200 200
GET /api/clones x15 → 401 401 401 401 401 401 401 401 401 401 401 401 401 401 401
```

No `Set-Cookie` header observed on `/login`.

## 3. `/admin` — the reported leak is gone, a different leak remains

```
GET /admin (no session)
HTTP/1.1 200 OK
Content-Length: 32973
<title>YouOwnClone</title>
```

The body is **not** the admin panel. It is the public clone chat page, with the slug echoed as the
page heading (`<h1>…">admin</h1>`) and the generic title `YouOwnClone`.

```
grep -o 'AdminPlatform[A-Za-z]+'  →  (no matches)
grep -c 'notFound'                →  1
grep -o '<h1[^>]*>[^<]*</h1>'      →  <h1 …>admin</h1>
```

A catch-all slug route serves the clone page for **any** single-segment path:

| Path | HTTP | Bytes | Rendered as |
|---|---|---|---|
| `/admin` | 200 | 32973 | clone chat, `<h1>admin</h1>` |
| `/pricing` | 200 | 32983 | clone chat, `<h1>pricing</h1>` |
| `/robots.txt` | 200 | 32998 | clone chat, `<h1>robots.txt</h1>` |
| `/zzz-random-99` | 200 | 33013 | clone chat, `<h1>zzz-random-99</h1>` |
| `/notfoundxyz` | 200 | — | clone chat |

Real admin sub-routes now enforce auth server-side:

```
/admin/tenants        → 307  location: /login
/admin/platform/tenants → 404
/admin/clon           → 404
/admin/cerebro        → 404
/dashboard            → 307  location: /resumen
/dashboard/resumen    → 404
```

Creator dashboard routes all redirect to `/login` (307):

```
/resumen /cerebro /biblioteca /inbox /productos /reuniones
/analiticas /facturacion /configuracion
```

**However**, the client-side i18n bundle still ships the full admin namespace on clone pages and on
`/registro`. Extracted from the RSC payload of an arbitrary slug (`/zzz-random-99`):

```
"admin": { "shell": {...}, "overview": {...}, "tenants": {...},
           "tenantDetail": {...}, "courtesy": {...}, "feedback": {...},
           "impersonation": {...}, "audit_log": {...} }
```

238 admin i18n strings, including:

- `impersonation` — title "User Impersonation", modal "Create a temporary session that lets you act
  as this tenant. Provide a reason for audit logging.", `tokenHelp: "Copy this token and use it in
  the Authorization header to impersonate the tenant."`
- `audit_log` — "Security and activity audit trail"
- `courtesy` — "Grant courtesy credits", "Grant a trial period to a user by email"
- `tenantDetail` — `stripeCustomer`, `stripeSubscription`, `subscriptionStatus`
- `tenantDetail` / `common` — the full plan vocabulary `basic, pro, scale, enterprise, free`

The landing page (`/`) does **not** carry this namespace (`admin_ns=0`); the clone pages and
`/registro` do (`admin_ns=1`).

## 4. A REST API surface exists now

```
GET /api/clones                → 401  {"error":"Unauthorized"}
GET /api/inbox                 → 401  {"error":"Unauthorized"}
GET /api/clones/x/prompts      → 401  {"error":"Unauthorized"}
GET /api/auth/session          → 200
GET /api/analytics             → 404
GET /api/stripe                → 404
GET /api/admin                 → 404
GET /api/tenant                → 404
GET /api/me                    → 404
GET /api/health                → 404
GET /api/version               → 404
GET /api/myownclone            → 404
POST /api/webhooks/stripe      → 404
POST /api/myownclone/public/clones/x/chat → 404
```

`/api/webhooks/stripe` returns **404** (was `405 Method Not Allowed` in the May capture).
The public chat endpoint is still **404** — consistent with the known bug
`myownclone_public_bp` not being registered.

## 5. Product surface — signup, pricing and legal all moved

`/registro` no longer meta-refreshes to `/contacto`. It serves a real signup form:

```
<title>MyOwnClone - Multiply Yourself</title>
Crea tu cuenta y empieza a escalarte
Full name | Email address | Create account | Continue with Google | Already have an account? Sign in
```

`/contacto` still exists (200, 28177 bytes). The i18n bundle for the signup flow includes
`sendLink: "Send magic link"`, `verifyEmailDesc: "Enter the code we sent to your email"`,
`googleButton`, `forgotPassword` (link valid 30 minutes), and `passwordRequirements`
(min 12 chars, upper/lower/number/symbol).

The landing page now has a **pricing section**:

```
h2: "Everything your clone can handle."
h2: "Real-time dashboard"
h2: "Structured knowledge"
h2: "AI-powered inbox"
h2: "Four steps to your clone."
h2: "Pick your plan."
h3: "Free"   h3: "Enterprise"
```

Plan names in the bundle: `basic, pro, scale, enterprise`. `trialDaysLeft: "{days} days left in your
free trial"`, `trialEnded`, `currentPlan`, `upgrade`, `manageBilling`. No `€` amount is present in
the server HTML — prices are client-rendered or absent.

Legal is now a **single page** at `/legal` (200, 49723 bytes), not six separate documents:

```
<title>Aviso legal | MyOwnClone</title>
h2: Aviso Legal — Última actualización: 11 de mayo de 2026
  I. Datos identificativos
  II. Objeto del Sitio Web
  III. Hosting y prestadores de servicio
  IV. Aceptación de las condiciones
  V. Propiedad intelectual e industrial
  VI. Responsabilidad del usuario
  VII. Naturaleza generativa del servicio
  VIII. Limitación de responsabilidad
  IX. Modificaciones
  X. Legislación aplicable y jurisdicción
```

Key strings from that page:

- Denominación social **Myownclone llc**, LLC (Wyoming, EE.UU.)
- Domicilio: **30 N Gould St, Ste R, Sheridan, WY 82801**, Estados Unidos
- **Representantes legales: Jacinto Guzman II**
- `contacto@myownclone.com`, `privacy@myownclone.com`
- Hosting: "El Sitio Web está alojado en **Vercel Inc.** (440 N Barranca Ave #4133, Covina, CA 91723)"
- Base de datos: "operada por **Neon Inc.**"
- "Cada clon está organizado en tres modos de comportamiento (pedagogía, ventas y soporte)"
- "El acceso al panel de administración del creador requiere una suscripción activa"
- "Los visitantes que interactúan con un clon publicado pueden hacerlo de forma anónima o
  identificándose mediante un código de un solo uso (OTP) enviado a su email"
- Ley aplicable y jurisdicción: Spain (referencia a la LSSI-CE)

`/en/legal` returns **byte-identical Spanish content** to `/legal` (49723 bytes, same title).

The English `legal` namespace in the i18n bundle is still a placeholder:

```
"pageDescription": "This page is a production placeholder for the legal documents that should be
                     reviewed with counsel before a public launch."
```

`/robots.txt`, `/sitemap.xml` and `/sitemap-0.xml` no longer serve text/XML — all three return the
clone chat HTML page.

## 6. Design system and locale

```html
<html lang="en" class="dm_sans_…variable jetbrains_mono_…variable">
```

- Font: **DM Sans** (not Poppins) + JetBrains Mono
- Theme key `localStorage["theme"]` with values `light` / `dark` / `system`, class `dark` on `<html>`,
  `prefers-color-scheme` detection
- CSS variables are a new set: `--bg-page`, `--text-primary`, `--text-muted`, `--text-secondary`,
  `--border-soft`, `--border-medium`, `--surface-2`, `--color-accent-violet`
- Locale: `/`, `/es` and `/en` all return `lang="en"` and byte-identical bodies (49386 bytes each).
  The `/es` route does not switch language.

## 7. Product capabilities confirmed in the live bundle

- Clone page modes: `Learn` / `Support` / `Sales` buttons in a "Conversation mode" group
- Guardrail string: `"notEnoughInfo": "I don't have enough information to answer this question
  accurately. Would you like me to notify the team?"`
- Clone modes in bundle: `pedagogy, sales, support`
- Dashboard sections: `biblioteca, cerebro, inbox, productos, reuniones, analiticas, facturacion,
  configuracion, resumen`
- Onboarding slug placeholder: `"slugSuffix": ".myownclone.yourdomain.com"` and
  `"urlSuffix": ".myownclone.com"`
- Onboarding steps: `name` (clone name) → `personality` (tone: formal/informal/friendly/technical)
  → `language` (Spanish/English) → `confirm`
- Admin overview: `mrrCostsMarginLegend: "MRR / Costs / Margin"`
- `costs30d: "Costs (30d)"`, `tenant`, `trial`, `suspended`
- Inbox: `automationDesc: "AI triage for incoming emails, classify intent, suggest replies and
  recommend products."`
- `feedbackWidget` present; `Feedback` copy: `ratingLabel: "Rating"`, `noFeedback`
- `errors.rateLimit: "Too many requests. Please wait a moment."` — the string exists but no 429 was
  observed

## 8. Instrumentation

No Sentry or PostHog identifiers appear in the served HTML or in the referenced JS chunks. The
strings `sentry.io`, `posthog`, `sentry-public_key`, `sentry-org_id`, `phc_*` and `eu.i.posthog.com`
are all absent from the current bundle set.

## 9. Next.js version — not determinable

`/_next/version.json` and `/_next/build-manifest.json` both return 404 (the catch-all HTML).
Chunk filenames are Turbopack-style hashes (`3n4651xroeu_4.css`, `turbopack-38b-0kt0grqjp.js`), so
the app is still built with Turbopack, but the exact Next.js version could not be read.

---

## Summary of the delta vs. the May–June 2026 OSINT

| Claim in the atoms | Live state 2026-10-22 |
|---|---|
| Vercel Edge `cdg1::iad1` | nginx 1.28.3 self-hosted, Let's Encrypt cert from 2026-10-14 |
| 9 subdomains on DNS | only apex + `www`; the other 7 have no DNS record |
| Zero CSP | two CSPs, one strict, `frame-ancestors 'none'` |
| No security headers | HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy all present |
| CORS `*` on `/login` and `/registro` | no CORS headers at all |
| `/admin` leaks 266 KB of admin panel code | `/admin` serves the public clone page; `AdminPlatform*` code gone |
| No REST API | `/api/clones`, `/api/inbox`, `/api/clones/x/prompts` exist and return 401 JSON |
| `/api/webhooks/stripe` → 405 | → 404 |
| `/registro` → meta-refresh to `/contacto` | real signup form with magic link + Google OAuth |
| No pricing, no docs | pricing section on the landing; `/legal` is a full ten-section Aviso Legal |
| Six separate legal documents | one `/legal` page; `/en/legal` duplicates the Spanish text |
| `robots.txt` blocks `/embed/`, `/__t/`, `/c/` | `robots.txt` is not served at all — the catch-all page is returned |
| Sentry + PostHog instrumented | no Sentry/PostHog identifiers in the served HTML |
| Poppins + JetBrains Mono | DM Sans + JetBrains Mono, new CSS variable set, `localStorage["theme"]` |
| Spanish-first (`/` es, `/en` en) | all of `/`, `/es`, `/en` return `lang="en"` |
| Legal entity Marea Kiss LLC (Wyoming) | Myownclone llc, 30 N Gould St Ste R Sheridan WY, rep. Jacinto Guzman II |
| No rate limiting | still no 429 observed (12× login 200, 15× API 401) |

**Still true:** no rate limiting observed; the public chat endpoint still 404s
(`myownclone_public_bp`); the admin i18n namespace still ships in the public clone-page payload;
the legal notice still claims Vercel hosting while the site is self-hosted on nginx.
