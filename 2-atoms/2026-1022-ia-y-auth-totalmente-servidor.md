---
id: 2026-1022-ia-y-auth-totalmente-servidor
type: atom
certainty: solid
sources: [raw/articles/myownclone-scrape_web-scrape.md, raw/articles/myownclone-frontend-recon.md]
links: ["[[myownclone]]", "[[2026-1022-arquitectura-rac-tres-modos-por-clon]]", "[[2026-1022-api-privada-sin-documentacion]]", "[[2026-1022-mutaciones-rsc-sin-api-rest]]"]
---
## Claim
En ningún bundle JS de [[myownclone]] aparecen claves o endpoints de OpenAI, Anthropic, Cohere u otro proveedor de LLM, ni cliente de Supabase, Auth0, Clerk o NextAuth: la inferencia de IA, el entrenamiento y la autenticación (Server Actions + sesiones server-side) ocurren íntegramente en servidor. La página `/login` hace bailout a renderizado cliente (skeleton en el HTML). El recon de bundles precisa el mecanismo: las mutaciones viajan por **Next.js Server Actions (protocolo RSC)** contra el mismo servidor Next.js que sirve la app, `api.myownclone.com` sirve el mismo HTML (no es un host de API), y las únicas salidas a terceros son PostHog (`eu.i.posthog.com/i/v1/logs`) y Sentry (`sentry.io`); tampoco se detectan tRPC, WebSocket ni SSE.

## Why It Matters
La opacidad total del núcleo —qué LLM, qué pipeline, qué proveedor de identidad— no es un descuido del OSINT sino una decisión: el producto no expone ni su stack de IA ni su API. Es coherente con la confidencialidad del pipeline RAC de [[2026-1022-arquitectura-rac-tres-modos-por-clon]] y con [[2026-1022-api-privada-sin-documentacion]], y significa que cualquier evaluación técnica de la calidad del clon es irremediablemente indirecta. La consecuencia competitiva es simétrica: la opacidad protege el pipeline pero cierra la vía de integrarse programáticamente, como detalla [[2026-1022-mutaciones-rsc-sin-api-rest]].
