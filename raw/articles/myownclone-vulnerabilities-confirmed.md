---
title: "Informe de Vulnerabilidades de myownclone (OSINT)"
created: 2026-05-25
updated: 2026-05-25
type: research
tags: [myownclone, security, vulnerabilities, osint]
sources: [/root/myownclone-errors-report.md, /root/myownclone-p2-fix.md, verificacion directa]
confidence: confirmed
---

# Vulnerabilidades de myownclone — Verificación Directa

Todas las vulnerabilidades fueron verificadas con curl a `myownclone.com` el 2026-05-25.

---

## CRÍTICAS (confirmadas abiertas)

### P2 — `/admin` expone el código del panel sin autenticación

- **HTTP 200** con **266,282 bytes** de HTML
- Redirect vía `<meta http-equiv="refresh">` (client-side, no server-side)
- El RSC payload contiene el código del panel admin ANTES del redirect
- **Componentes expuestos**: AdminPlatformTenants, AdminPlatformInbox, AdminPlatformResumen, AdminPlatformSpam, AdminPlatformFeedback, AdminImpersonationBanner
- **81+ referencias** a features internas: tenant, stripe, brain, triage, templates, booking, labels, mrr, impersonate, spamDomain
- **Estados de suscripción**: active, trialing, past_due, unpaid, canceled, incomplete, complimentary, suspended, deleted

### S1 — Sentry DSN público en todas las páginas

```
sentry-public_key: 6b2d7ed6999454df87ccf844aa85ba70
sentry-org_id: 4511315838173184
sentry-environment: vercel-production
sentry-release: 1c3b63592f99cfe9bd4aa112cd693195202cb612
```
Cada página genera un trace_id único. Un atacante puede enviar eventos falsos y contaminar dashboards.

### S2 — Sin Content-Security-Policy

Cero header CSP. XSS sin mitigación. Dependencias de terceros sin restricción.

### S4 — CORS wildcard en `/login` y `/registro`

```
access-control-allow-origin: *
access-control-allow-methods: OPTIONS, GET, HEAD
```
Cualquier dominio puede leer estas páginas vía JavaScript cross-origin.

---

## ALTAS (confirmadas abiertas)

- **S3**: Sin headers de seguridad (X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy)
- **P1**: `/registro` redirige con meta refresh (260KB descargados para nada)

## MEDIAS

- **S5**: Sin rate limiting (10 peticiones rápidas, todas HTTP 200)
- **S6**: Headers revelan stack: `server: Vercel`, `x-powered-by: Next.js`
- **B1**: Turbopack en producción (experimental)

## BAJAS

- **B2**: Hashes de chunk débiles (5-8 chars)
- **S7**: Cookie NEXT_LOCALE sin HttpOnly/Secure
- **P3**: Página 404 sin marca

---

## Archivos

- `/home/haxth3/myownclone-errors-report.md` — Informe completo (21KB, 17 hallazgos)
- `/home/haxth3/myownclone-p2-fix.md` — Fix detallado para P2 (11KB, código TypeScript)
- `/tmp/myownclone_admin_leak.html` — HTML del leak de admin (266KB)
