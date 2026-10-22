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
