---
id: 2026-1029-weaviate-cloud-free-tier-100000-objetos-1gb-memoria
type: atom
certainty: solid
sources: [sources/2026-10-29-weaviate-cloud-pricing.md]
links: ["[[2026-1102-aiven-valkey-y-opensearch-tambien-tienen-plan-gratuito]]", "[[2026-1029-qdrant-free-tier]]", "[[2026-1022-myclone-viaje-embeddings-voyage]]", "[[2026-1101-aiven-postgresql-plan-gratuito-1gb-sin-region]]"]
---
## Claim
El plan **Free de Weaviate Cloud** es "Forever $0/mo", sin tarjeta de crédito y limitado a **1 cluster por usuario**, con límites explícitos: **100.000 objetos · 1 GB de memoria · 10 GB de disco**, **1 colección hasta 3 tenants**, **Embeddings (2.000 req/día) + Query Agent (1.000 req/mes)**, soporte por email. La tabla de comparación añade las ausencias: **sin HA/replicación**, **sin tipos de índice flexibles**, **sin retención de backup (×)**, disponibilidad **"Best effort"** (sin SLA y sin tiempo de respuesta para Sev 1), **AWS** con **regiones limitadas (2)**.

## Why It Matters
Es el único plan de Weaviate que no cuesta nada, y por tanto el único que puede convivir con un presupuesto de ≤ €4/mes ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]). Pero sus límites reales son más duros que el titular "100.000 objetos": **1 colección y 3 tenants** es el número que rompe la arquitectura multi-tenant de MyOwnClone, donde cada creator tiene su propio silo/corpus y el isolation por tenant es requirement de producto (ver [[multi-tenant-saas]] y [[2026-1022-multi-tenant-slug-unpublished]]). Tres tenants no son "un tenant por clon": son un plan de evaluación, no un plan de producción. Y el **"1 GB de memoria"** como techo de 100.000 objetos es un número que hay que contrastar con el competidor, que ya tiene **96.891 embeddings reales indexados** ([[2026-1022-myclone-viaje-embeddings-voyage]]) — el free tier de Weaviate está al mismo orden de magnitud del corpus entero del competidor, lo que sugiere que un solo clon con historial de email y memoria de entrenamiento puede agotarlo. Comparado con el free tier de Qdrant (0,5 vCPU / 1 GB RAM / 4 GB disco, un nodo único, también solo para testing) ([[2026-1029-qdrant-free-tier]]), ambos quedan en la categoría "gratis para evaluar, insuficiente para producir".

## [FRICTION]
> [[2026-1102-aiven-valkey-y-opensearch-tambien-tienen-plan-gratuito]] afirma, en su "Why It Matters", que "**no hay free tier para el motor vectorial si se elige Qdrant o Weaviate**" y que ese componente es "el que quedaría fuera del presupuesto cero".
> Este átomo presiona esa creencia porque la página oficial de precios de Weaviate publica un plan **Free permanente** con límites explícitos (100.000 objetos, 1 GB de memoria, 10 GB de disco, 2.000 embeddings/día) y sin tarjeta de crédito.
> Ambas no pueden ser completamente correctas: o el átomo de Aiven se equivocó al extender a Weaviate una ausencia que solo applies a Aiven, o "free tier" no equivale aquí a "capa vectorial gratis" — porque el límite de **1 colección y 3 tenants** lo deja inservible para un producto multi-tenant, de modo que la frase correcta sería "Weaviate tiene free tier, pero no utilizable como capa vectorial multi-tenant sin pagar". Marcado para juicio humano, no auto-resuelto.
