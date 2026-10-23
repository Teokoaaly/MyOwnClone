---
id: 2026-1022-live-verify-deployment-migrada-a-vps-nginx
type: atom
certainty: solid
sources: [0-raw/archive/2026-10-23-2026-10-22-myownclone-live-reverification.md]
links: ["[[myownclone]]", "[[2026-1022-frontend-nextjs-vercel-sentry-posthog]]", "[[2026-1022-neon-postgres-serverless]]", "[[2026-1022-dns-superficie-publica-myownclone]]"]
---

## Claim
La verificación en vivo del 2026-10-22 muestra que [[myownclone]] **ya no está desplegado en Vercel**: el sitio responde con `Server: nginx/1.28.3 (Ubuntu)` desde la IP `212.227.169.99`, sin cabeceras `x-vercel-id` ni `x-vercel-cache`. El TLS lo emite Let's Encrypt con un certificado emitido el **2026-10-14** (válido hasta 2027-01-12) para `CN=myownclone.com`. La app sigue siendo Next.js con Turbopack (`X-Powered-By: Next.js`, chunks `turbopack-38b-0kt0grqjp.js`), pero servida detrás de nginx autoalojado. La versión exacta de Next.js no es determinable: `/_next/version.json` y `/_next/build-manifest.json` devuelven 404 porque el catch-all sirve HTML en su lugar.

## Why It Matters
Todo el corpus OSINT de mayo–junio 2026 describe una topología Vercel Edge que ya no es la de producción. Cualquier plan de migración, coste de hosting, presupuesto de observabilidad (Sentry/PostHog) o supuesto de "edge" construido sobre esos atoms parte de premisas caducadas.

## [FRICTION]
> [[2026-1022-frontend-nextjs-vercel-sentry-posthog]] (escrita hace ~21 semanas) afirma que el frontend corre "sobre Vercel (Edge Network, x-vercel-id cdg1::iad1)" y fija la versión en **Next.js 16.2.4** con deployment id `dpl_8jxBD8eEioaPmHarRs3eofX1Ks3S`.
> Este átomo presiona esa creencia porque la cabecera `x-vercel-id` ya no aparece en ninguna respuesta y el servidor es nginx autoalojado; la versión de Next.js solo puede acotarse por el formato de chunk (Turbopack), no confirmarse.
> Ambas no pueden ser completamente correctas: o el sitio se migró a un VPS propio después del 2026-06-24 y el átomo quedó obsoleto, o se observa un entorno distinto del que se escaneó en junio.
> Marcado para juicio humano, no auto-resuelto.
