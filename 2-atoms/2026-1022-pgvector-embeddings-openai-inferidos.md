---
id: 2026-1022-pgvector-embeddings-openai-inferidos
type: atom
certainty: tentative
sources: [raw/articles/myownclone-new-findings-may-2026.md]
links: ["[[2026-1022-neon-postgres-serverless]]", "[[2026-1022-ia-y-auth-totalmente-servidor]]", "[[2026-1022-myclone-viaje-embeddings-voyage]]", "[[2026-1022-arquitectura-rac-tres-modos-por-clon]]"]
---
## Claim
El análisis de los 15 bundles JS de [[myownclone]] (~1,2 MB) sostiene que el stack usa **Neon (PostgreSQL serverless) con PGvector** como base vectorial y **OpenAI `text-embedding-3`** para embeddings, ambos marcados explícitamente como *inferidos* por extensión de Neon; los LLM serían **Anthropic Claude + OpenAI** (confirmado por strings de tracking de coste), sobre Next.js 16.2.4 (App Router) en Vercel `cdg1::iad1`, Stripe, Sentry (org 4511315838173184), PostHog (`eu.i.posthog.com`), next-intl (ES+EN) y las tipografías Poppins + JetBrains Mono.

## Why It Matters
Si es correcto, la elección de embeddings es la diferencia técnica más relevante frente a [[2026-1022-myclone-viaje-embeddings-voyage]]: MyClone.is usa Voyage AI con 96.891 embeddings ya indexados y endpoints de migración, mientras [[myownclone]] usaría el embedding de OpenAI sobre PGvector en el mismo Neon — sin deuda de migración y sin proveedor de vector store separado. Eso Simplifica la operación pero ata el corpus a OpenAI, y encaja con el RAC de [[2026-1022-arquitectura-rac-tres-modos-por-clon]] y con la base Neon de [[2026-1022-neon-postgres-serverless]]. La marca de *inferido* es obligatoria: es una hipótesis técnica, no un hecho observado.

## [FRICTION]
> [[2026-1022-ia-y-auth-totalmente-servidor]] (escrita hace ~21 semanas) afirma que **en ningún bundle JS** de [[myownclone]] aparecen claves o endpoints de OpenAI, Anthropic, Cohere u otro proveedor de LLM, y que las únicas salidas a terceros son PostHog y Sentry.
> Este átomo presiona esa creencia porque este análisis afirma encontrar strings de tracking de coste de Anthropic y OpenAI, y una base vectorial PGvector con embeddings `text-embedding-3` de OpenAI.
> Ambas no pueden ser exactamente correctas: o los strings de coste son etiquetas internas sin tráfico real (con lo que la inferencia de proveedor sería errónea), o el recon previo no revisó las bundles de administración de plataforma, donde se contabilizan los costes por proveedor. Marcado para juicio humano, no auto-resuelto.
