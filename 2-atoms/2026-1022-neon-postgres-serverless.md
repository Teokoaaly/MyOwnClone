---
id: 2026-1022-neon-postgres-serverless
type: atom
certainty: solid
sources: [raw/articles/myownclone-technical-research.md, raw/articles/myownclone-frontend-recon.md, raw/articles/myownclone-new-findings-may-2026.md]
links: ["[[myownclone]]", "[[multi-tenant-saas]]", "[[2026-1022-mutaciones-rsc-sin-api-rest]]"]
---
## Claim
La base de datos de [[myownclone]] es Neon Inc. (PostgreSQL serverless), según consta en su aviso legal; el backend/API vive en Vercel serverless functions bajo api.myownclone.com, con el lenguaje base no confirmado directamente pero con un patrón de rutas que sugiere Next.js API Routes. El recon de bundles corrige la forma del backend: `api.myownclone.com` **sirve el mismo HTML de la app** (es el mismo despliegue Next.js, no un host de API Routes separado) y las mutaciones viajan por Server Actions / protocolo RSC, sin API REST.

## Why It Matters
El aviso legal es la fuente más fiable que usa el informe para el backend (todo lo demás es inferido del bundle JS). Una plataforma sobre Neon + Vercel escala por multi-tenancy sin ops propia, que es exactamente el supuesto de [[multi-tenant-saas]]. La aclaración de que `api.` es un alias del mismo deployment y no un plano de API elimina la hipótesis de dos backends separados y deja a Neon como el único plano de persistencia — ver [[2026-1022-mutaciones-rsc-sin-api-rest]].

## [FRICTION]
> La versión anterior de esta nota afirmaba que "el backend/API vive en Vercel serverless functions bajo api.myownclone.com" con un patrón de rutas que "sugiere Next.js API Routes".
> El recon de bundles presiona esa lectura porque encuentra que `api.myownclone.com` devuelve el mismo HTML de la app y que no existen endpoints REST en los bundles: el patrón de rutas era la app, no API Routes.
> Ambas no pueden ser completamente correctas: o existían API Routes no referenciadas en el cliente, o la inferencia confundió las rutas de la app con rutas de API. Marcado para juicio humano, no auto-resuelto.

## Extensión (nuevos hallazgos, mayo 2026)
El análisis de bundles añade la capa vectorial sobre el mismo Neon: **PGvector** como base de datos vectorial y **OpenAI `text-embedding-3`** para embeddings, ambos explícitamente marcados como *inferidos* por extensión de Neon, con los LLM **Anthropic Claude + OpenAI** confirmados por strings de tracking de coste. Si la inferencia es correcta, [[myownclone]] indexa en el mismo PostgreSQL serverless que guarda el resto, sin vector store separado — a diferencia de MyClone.is, que usa Voyage AI con 96.891 embeddings ya migrados (ver [[2026-1022-myclone-viaje-embeddings-voyage]]). Ver [[2026-1022-pgvector-embeddings-openai-inferidos]] para el [FRICTION] con [[2026-1022-ia-y-auth-totalmente-servidor]].
## Nota de extensión 2026-10-26 — Heroku Postgres como alternativa gestionada
Fuente: `sources/2026-10-25-heroku-pricing.md`. El vault tenía **Neon como la única base de datos gestionada documentada** del stack, y ahora tiene una **segunda con precio de lista completo** que permite contrastar. Heroku Postgres publica tres tiers: **Essential** desde **$5/mes** (1 GB de disco, **20 conexiones**, RAM compartida, "Max downtime 4 hour per month", "Table Limit: 4,000 tables"), **Standard** desde **$50/mes** (servidor **dedicado**, 4 GB RAM, 64 GB disco, 120 conexiones, "Max downtime 1 hour per month", "Rollback up to 4 days") y **Premium** desde **$200/mes** (mismas specs que Standard-0, pero con **High Availability**, "Max downtime 15 minutes per month" y "Rollback up to 7 days"); el tier **Advanced** va de **$150/mes** (4G) a **$40.000/mes** (1536G) con "Pay only for what you use", "Decoupled storage and compute" y los primeros **100 GB-mes de almacenamiento incluidos** por clúster. La comparación relevante para el producto: Neon aparece en el Aviso Legal ([[2026-1022-superficie-legal-publica-dpa-clon-terms]]) y es la elección de MyClone, pero **Heroku Essential no es utilizable como base de un producto multi-tenant**: 20 conexiones y 4 horas de downtime al mes son incompatibles con el patrón del vault. Ver [[2026-1026-heroku-postgres-essential-5-a-20-dolares-con-4-horas-de-parada]], [[2026-1026-heroku-postgres-standard-50-a-12000-con-dedicado-y-1-hora-de-parada]] y [[2026-1026-heroku-postgres-premium-200-con-ha-y-15-minutos-de-parada]].
