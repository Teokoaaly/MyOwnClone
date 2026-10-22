---
id: 2026-1022-mutaciones-rsc-sin-api-rest
type: atom
certainty: solid
sources: [raw/articles/myownclone-frontend-recon.md]
links: ["[[myownclone]]", "[[2026-1022-api-privada-sin-documentacion]]", "[[2026-1022-myclone-api-rest]]"]
---
## Claim
Las mutaciones de [[myownclone]] no viajan por una API REST: el cliente invoca Next.js Server Actions (protocolo RSC) contra el mismo servidor Next.js que sirve la app —`api.myownclone.com` sirve el mismo HTML, no un backend separado— y en los bundles analizados no aparecen endpoints REST, GraphQL, tRPC, WebSocket ni SSE; las únicas salidas a terceros son PostHog (`eu.i.posthog.com/i/v1/logs`) y Sentry (`sentry.io`).

## Why It Matters
La ausencia de superficie REST/WebSocket es una decisión de arquitectura defensiva heredera del modelo serverless: no hay contrato de API que un atacante pueda enumerar y cada acción va por el mismo canal autenticado del servidor. Esto refuerza la lectura de [[2026-1022-api-privada-sin-documentacion]] y contrasta con el competitor [[2026-1022-myclone-api-rest]], que sí expone rutas REST versionadas y un endpoint público de experimentos A/B: [[myownclone]] no puede integrarse programáticamente como lo hace MyClone.is, lo que es una disadvantage de plataforma pero una ventaja de superficie.
