---
id: thread-myownclone-security-surface
type: thread
updated: 2026-10-22
sources: [raw/articles/myownclone-vulnerabilities-confirmed.md, raw/articles/myownclone-frontend-recon.md, raw/articles/myownclone-scrape_web-scrape.md]
links: ["[[myownclone]]", "[[multi-tenant-saas]]", "[[2026-1022-admin-p2-fuga-codigo-panel-sin-auth]]"]
---

# Thread — Superficie de ataque de MyOwnClone

Síntesis de los átomos de seguridad derivados del informe de vulnerabilidades verificadas (2026-05-25) y del recon de frontend. Todos los hallazgos están trazados a `raw/articles/myownclone-vulnerabilities-confirmed.md` y corroborados de forma independiente por el scrape público.

## El hallazgo principal

Un GET sin sesión a `/admin` devuelve **HTTP 200 con 266 KB de HTML** donde el payload RSC ya contiene el código del panel de administración (`AdminPlatformTenants`, `AdminPlatformInbox`, `AdminPlatformResumen`, `AdminPlatformSpam`, `AdminPlatformFeedback`, `AdminImpersonationBanner`) antes de que se ejecute el redirect. El redirect es un `<meta http-equiv="refresh">` en cliente, no un 307 de servidor.

Consecuencia: la barrera de auth del back-office no se aplica en servidor. 81+ referencias a features internas quedan descargables sin sesión — incluyendo el vocabulario completo de estados de suscripción y el módulo de impersonación.

Ver [[2026-1022-admin-p2-fuga-codigo-panel-sin-auth]] y [[2026-1022-admin-rutas-bilingues-sin-subdominio]].

Fricción abierta: el scrape de junio registra un 307 `NEXT_REDIRECT` en `/admin`, y el informe de mayo registra 200 con payload. Son observaciones de fechas distintas, o un cambio de comportamiento. **No resuelto — requiere re-verificación con curl antes de actuar.** La nota [[2026-1022-dns-superficie-publica-myownclone]] también afirma que `/admin` responde 200 con autenticación, lo que no encaja con ninguna de las dos lecturas.

## Hardening HTTP ausente

Verificado por curl, no inferido:

| Ausencia | Átomo |
|---|---|
| CSP (y por tanto mitigación de XSS) | [[2026-1022-ausencia-csp-xss-sin-mitigacion]] |
| Headers de seguridad (HSTS, X-Frame-Options, Referrer-Policy…) | [[2026-1022-sin-headers-de-seguridad]] |
| Rate limiting | [[2026-1022-sin-rate-limiting]] |
| CORS restrictivo en login/registro (wildcard) | [[2026-1022-cors-wildcard-en-login-y-registro]] |
| `HttpOnly`/`Secure` en la cookie `NEXT_LOCALE` | [[2026-1022-cookie-next-locale-sin-httponly-ni-secure]] |

Fricción con la nota legacy `entities/myownclone.md`, que describe "aislamiento completo". No es compatible con la ausencia total de hardening HTTP verificado por curl.

## Superficie lesser-known

- **DSN de Sentry público** — [[2026-1022-sentry-dsn-publico-contamina-dashboards]]: la clave de ingestión es pública por diseño, pero eso permite spamming de eventos falsos en nuestro dashboard y agotar la quota. Fricción adicional: el release hash difiere entre los dos informes para la misma fecha, lo que sugiere que uno de los dos tomó una build distinta.
- **Códigos de chunk débiles** y Turbopack experimental en producción — [[2026-1022-frontend-nextjs-vercel-sentry-posthog]].
- **Superficie oculta en robots.txt** — [[2026-1022-superficie-oculta-robots-txt]]: prefijos bloqueados que devuelven 404 sin marca, más el meta-refresh de 260 KB en `/registro`.
- **Email inbound sin dominio propio** — [[2026-1022-email-inbound-contacto-sin-dominio-propio]]: una única casilla `contacto@` en lugar del comodín `*@` que sí implementa el código ([[2026-1022-admin-bandeja-global-y-spam]]).

## Nota de fecha

Los tres subdominios públicos sirven el **mismo deployment** (ver [[2026-1022-dns-superficie-publica-myownclone]]), y `api.` es un alias, no una API real: los 404/405 en `/api/` confirman que no hay API Routes. La API real es Flask en el puerto 5001, expuesta por el frontend vía Server Actions ([[2026-1022-mutaciones-rsc-sin-api-rest]]).

## Prioridad sugerida

1. Mover la barrera de auth de `/admin` al servidor. Es la fuga más grande, verificada y con impacto directo en impersonación y gestión de tenants.
2. CSP como mínimo report-only, luego estricta.
3. Rate limiting en login/registro y en los endpoints de email inbound.

Los tres son cambios de una tarde en el código, no de rediseño. Nada de esto se ha ejecutado: este thread documenta, no modifica.
