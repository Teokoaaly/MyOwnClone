---
id: 2026-1022-sentry-dsn-publico-contamina-dashboards
type: atom
certainty: solid
sources: [raw/articles/myownclone-vulnerabilities-confirmed.md]
links: ["[[myownclone]]", "[[2026-1022-frontend-nextjs-vercel-sentry-posthog]]", "[[2026-1022-posthog-integracion-pesada-sentry]]", "[[2026-1022-mutaciones-rsc-sin-api-rest]]"]
---
## Claim
La DSN de Sentry es pública en todas las páginas de [[myownclone]]: `sentry-public_key: 6b2d7ed6999454df87ccf844aa85ba70`, `sentry-org_id: 4511315838173184`, `sentry-environment: vercel-production` y `sentry-release: 1c3b63592f99cfe9bd4aa112cd693195202cb612`. Cada página genera un `trace_id` único, lo que permite a un atacante enviar eventos falsos a esa instrumentación y contaminar los dashboards de error del producto.

## Why It Matters
Convierte la instrumentación de [[2026-1022-frontend-nextjs-vercel-sentry-posthog]] en un canal de escritura no autenticado: la clave pública no es un secreto, y el `trace_id` por página permite falsificar reportes con formato válido, degradando la señal de calidad que la duplicación Sentry+PostHog de [[2026-1022-posthog-integracion-pesada-sentry]] pretende aportar. Es también un reminder de que la superficie de salida a terceros —Sentry y PostHog— es la única que [[2026-1022-mutaciones-rsc-sin-api-rest]] identifica en los bundles: no hay API propia que auditar, pero sí hay dos endpoints externos escribibles con credenciales embebidas en el cliente.

## [FRICTION]
> [[2026-1022-frontend-nextjs-vercel-sentry-posthog]] fija el release desplegado como `3cd116d948dc38b980833dd9d465bcffbc8fd443` (con deployment `dpl_8jxBD8eEioaPmHarRs3eofX1Ks3S`).
> Esta nota presiona eso porque el release declarado en la instrumentación de Sentry es `1c3b63592f99cfe9bd4aa112cd693195202cb612`, un hash distinto para la misma fecha de verificación (2026-05-25).
> Ambas no pueden ser completamente correctas: o el `sentry-release` no coincide con el commit del bundle (release desactualizado en el cliente), o se está observando un deploy distinto. Marcado para juicio humano, no auto-resuelto.
