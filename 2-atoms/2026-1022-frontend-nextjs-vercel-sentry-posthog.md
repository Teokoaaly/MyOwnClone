---
id: 2026-1022-frontend-nextjs-vercel-sentry-posthog
type: atom
certainty: solid
sources: [raw/articles/myownclone-technical-research.md, raw/articles/myownclone-frontend-recon.md, raw/articles/myownclone-scrape_web-scrape.md, raw/articles/myownclone-vulnerabilities-confirmed.md, raw/articles/myownclone-new-findings-may-2026.md]
links: ["[[myownclone]]", "[[multi-tenant-saas]]", "[[2026-1022-mutaciones-rsc-sin-api-rest]]", "[[2026-1022-myclone-stack-tecnologico]]", "[[2026-1022-posthog-integracion-pesada-sentry]]", "[[2026-1022-tema-oscuro-css-variables]]"]
---
## Claim
El frontend de [[myownclone]] corre Next.js con turbopack sobre Vercel (Edge Network, x-vercel-id cdg1::iad1), con renderizado SSR + React Server Components, y expone instrumentación identificable: Sentry (org_id 4511315838173184, sentry-environment vercel-production, public key 6b2d7ed6999454df87ccf844aa85ba70, sample rate 0.1) y PostHog con apiHost eu.i.posthog.com (SDK 1.373.4, project key phc_tn48YvixjuzzdhbNFLzt9hD7TfwbH2AssUxG2gAiPWei); además incluye i18n por locale routing con español por defecto e inglés en /en. El recon de bundles fija la versión exacta en **Next.js 16.2.4 (Turbopack) con React 19**, deployment id `dpl_8jxBD8eEioaPmHarRs3eofX1Ks3S` y release `3cd116d948dc38b980833dd9d465bcffbc8fd443`.
El scrape público del 2026-05-25 añade el detalle de hosting e i18n: región de despliegue Vercel **cdg1 (Paris)**, headers `x-powered-by: Next.js` / `server: Vercel`, polyfill core-js 3.38.1, framework `@next/intl` con español por defecto en `/` e inglés en `/en`, y tipografías Poppins (variable) y JetBrains Mono (variable) servidas como woff2 por la optimización de fuentes de Next.js.

## Why It Matters
Los identificadores de Sentry y PostHog permiten correlacionar cualquier marcado público con la cuenta del proveedor, y el locale routing confirma un producto con mercado dual ES/EN. La ausencia de servidor propio es coherente con el patrón serverless de [[multi-tenant-saas]]. La project key de PostHog es **distinta** de la de MyClone.is (phc_zXjWGA3SNsR5sFCowUgXOXro4tWY7or485lpQzNQtzh), lo que confirma que son cuentas de analítica independientes y no una implementación copiada — matiza la "coincidencia de stack" de [[2026-1022-myclone-stack-tecnologico]]. La versión exacta y el release hash son los anclajes verificables del binario desplegado, útiles para cualquier análisis posterior de bundles.
La verificación de vulnerabilidades del 2026-05-25 confirma en producción los mismos identificadores de stack (`server: Vercel`, `x-powered-by: Next.js`), añade que **Turbopack se usa en producción siendo aún experimental** y que los hashes de chunk son débiles (5-8 caracteres), lo que dificulta el versionado de bundles — y confirma que la DSN de Sentry es pública en todas las páginas (ver [[2026-1022-sentry-dsn-publico-contamina-dashboards]]).

## [FRICTION]
> [[myownclone]] (nota de entidad, escrita hace ~21 semanas) afirma en su tabla de stack "Frontend: Next.js 14+ (turbopack)".
> Esta nota presiona eso porque el recon de bundles del mismo producto identifica la versión servida como **Next.js 16.2.4** con React 19.
> Ambas no pueden ser exactamente correctas: o la entidad resume mal la versión, o el producto ha avanzado dos majors desde que se escribió la nota. Marcado para juicio humano, no auto-resuelto.

## Extensión (nuevos hallazgos, mayo 2026)
El análisis de los 15 bundles JS de la misma ronda **confirma de nuevo la versión exacta**: Next.js 16.2.4 con App Router (confirmado por el payload RSC y `__next_f`), Vercel `cdg1::iad1`, Sentry (org 4511315838173184), PostHog (`eu.i.posthog.com`), i18n con next-intl en ES + EN por routing de locale, y tipografías Poppins + JetBrains Mono servidas como woff2 vía next/font. Es la segunda fuente independiente que fija la versión 16.2.4, lo que refuerza la lectura del [FRICTION] anterior: la entidad que dice "Next.js 14+" es la que está desactualizada. Ver también [[2026-1022-pgvector-embeddings-openai-inferidos]].
