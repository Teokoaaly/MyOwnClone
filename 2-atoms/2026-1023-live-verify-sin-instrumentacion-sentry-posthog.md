---
id: 2026-1023-live-verify-sin-instrumentacion-sentry-posthog
type: atom
certainty: solid
sources: [0-raw/archive/2026-10-23-2026-10-22-myownclone-live-reverification.md]
links: ["[[2026-1022-posthog-integracion-pesada-sentry]]", "[[2026-1022-sentry-dsn-publico-contamina-dashboards]]", "[[2026-1022-frontend-nextjs-vercel-sentry-posthog]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]"]
---

## Claim
El bundle vivo de [[myownclone]] sirve el 2026-10-22 **sin ningún identificador de instrumentación de terceros**: en el HTML servido y en los chunks JS referenciados no aparecen ni `sentry.io`, ni `posthog`, ni `sentry-public_key`, ni `sentry-org_id`, ni claves `phc_*`, ni `eu.i.posthog.com`. La doble cobertura Sentry + PostHog observada en mayo (DSN pública en todas las páginas, org `4511315838173184`, project key `phc_tn48YvixjuzzdhbNFLzt9hD7TfwbH2AssUxG2gAiPWei`) no es observable en la generación actual del producto.

## Why It Matters
Deja de haber, en el cliente público, el canal de escritura no autenticado a terceros que el vault había registrado como superficie de salida: si no hay DSN pública ni endpoint de PostHog embebido, tampoco hay contaminación de dashboards de error posible desde el bundle actual. Es un indicio fuerte de que la app se reconstruyó sobre una base nueva (mismo indicio que la migración a nginx de [[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]), porque una simple reubicación de hosting no elimina un SDK de observabilidad. En la práctica también significa que el coste y la complejidad de la instrumentación dual descrito en [[2026-1022-posthog-integracion-pesada-sentry]] ya no se aplican al despliegue vivo.

## [FRICTION]
> [[2026-1022-posthog-integracion-pesada-sentry]] afirma que "[[myownclone]] instrumenta con doble cobertura: Sentry (...) y PostHog con integración tan pesada que el chunk principal de JS (187KB) está dominado por su SDK", y [[2026-1022-sentry-dsn-publico-contamina-dashboards]] afirma que "la DSN de Sentry es pública en todas las páginas de [[myownclone]]" con `sentry-public_key: 6b2d7ed6999454df87ccf844aa85ba70` y `sentry-environment: vercel-production`.
> Este átomo presiona ambas creencias porque la medición del 2026-10-22 no encuentra ni una sola de esas cadenas en el bundle actual, y el entorno `vercel-production` es incompatible con el nginx autoalojado medido.
> Ambas no pueden ser completamente correctas: o la instrumentación se retiró al reconstruir el frontend, o el bundle de octubre es una build distinta sin el SDK. Lo que no puede ser es que ambos bundles coexistan: no hay versionado observable que lo explique.
> Marcado para juicio humano, no auto-resuelto.
