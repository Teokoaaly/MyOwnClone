---
id: 2026-1102-r2-ecosistema-plataforma-que-se-vende-junto
type: atom
certainty: solid
sources: [sources/2026-11-02-cloudflare-r2-storage.md]
links: ["[[2026-1031-cloudflare-r2-storage]]", "[[2026-10-29-d1-database]]", "[[2026-10-29-workers-compute-requests]]"]
---

## Claim
En la plataforma de Cloudflare, R2 se ofrece junto a un conjunto de primitivas de almacenamiento y cómputo con el mismo modelo de precio por uso: KV ("Ultra-fast key-value storage"), Queues ("Message processing"), Durable Objects ("Stateful compute"), D1 ("Serverless SQL"), Hyperdrive ("Global databases"), K2 (eventos ordenados y durables), Artifacts (storage versionado estilo Git) y Basin ("Ingest, catalog & query data"), además de Workers y Vectorize.

## Why It Matters
MyOwnClone ejecuta hoy PostgreSQL + Redis + Weaviate + Flask + Next.js como componentes separados, cada uno con su factura y su mínimo (ver [[2026-10-29-d1-database]] para el caso D1 como alternativa serverless SQL). Este listado muestra que existe una vía de proveedor único donde el storage de objetos, la cola de mensajes, el estado mutable y la base de datos clave-valor se sustituyen por primitivas con el mismo esquema de facturación por uso, lo que reduce el número de proveedores que hay que facturar y auditar. El riesgo es simétrico: el atajo de "todo en Cloudflare" cambia el eje de coste (infraestructura → requests, operaciones y GB) sin mover la variable dominante, que sigue siendo el coste por asiento (ver [[2026-1022-costes-por-categoria-tenant]]). Además fija el límite de R2: no sustituye a PostgreSQL ni a Weaviate, solo ofrece el storage de objetos y primitivas alrededor ([[2026-1031-cloudflare-r2-storage]]).
