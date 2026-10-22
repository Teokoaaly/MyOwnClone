---
id: 2026-1022-sin-headers-de-seguridad
type: atom
certainty: solid
sources: [raw/articles/myownclone-vulnerabilities-confirmed.md]
links: ["[[myownclone]]", "[[2026-1022-ausencia-csp-xss-sin-mitigacion]]", "[[2026-1022-cors-wildcard-en-login-y-registro]]", "[[2026-1022-frontend-nextjs-vercel-sentry-posthog]]"]
---
## Claim
[[myownclone]] no emite headers de seguridad: faltan `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy` y `Permissions-Policy` en las respuestas verificadas el 2026-05-25.

## Why It Matters
La ausencia de headers defensivos, junto con la ausencia total de CSP de [[2026-1022-ausencia-csp-xss-sin-mitigacion]] y el CORS abierto de [[2026-1022-cors-wildcard-en-login-y-registro]], dibuja un patrón: el sitio no aplica una capa de hardening HTTP en el borde de Vercel. Sin `X-Frame-Options` el panel de admin puede embeberse en un iframe de terceros (clickjacking sobre acciones de plataforma como la impersonación), sin `X-Content-Type-Options` los tipos MIME no se fijan y sin `Permissions-Policy` no se restringen APIs sensibles del navegador. Todo ello sobre el stack Next.js/Vercel descrito en [[2026-1022-frontend-nextjs-vercel-sentry-posthog]], donde la única defensa observada es la de las Server Actions descritas en [[2026-1022-mutaciones-rsc-sin-api-rest]].
