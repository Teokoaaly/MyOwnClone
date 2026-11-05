---
id: 2026-1026-heroku-key-value-store-mini-3-dolares-hasta-12500
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-pricing.md]
links: ["[[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]]", "[[2026-1026-heroku-postgres-essential-5-a-20-dolares-con-4-horas-de-parada]]", "[[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]]"]
---

## Claim
**Heroku Key-Value Store** (el Redis gestionado) publica **25 planes en cuatro familias** (Mini, Premium, Private y Shield). **Mini $3/mes**: 25 MB, **20 conexiones**, "Multi-tenant instance for small projects and concepts". **Premium 0 $15** (50 MB, 40), **Premium 1 $30** (100 MB, 80), **Premium 2 $60** (250 MB, 200), **Premium 3 $120** (500 MB, 400), **Premium 5 $200** (1 GB, 1.000) — todos "Multi-tenant (shared server)", "High availability with low-latency failover", "Resource scalability". A partir de **Premium 7 $750** (7 GB, 10.000) el servidor pasa a **"Single tenant (dedicated server)"**, y sigue subiendo: **Premium 9 $1,450** (10 GB, 25.000), **Premium 10 $3,500** (25 GB, 40.000), **Premium 12 $6,500** (50 GB, 65.000), **Premium 14 $12,500** (100 GB, 65.000). Las familias **Private** van de **$150** (Private-3, 500 MB, 400) a **$14,000** (Private-14, 100 GB) y las **Shield** de **$210** (Shield-3, 500 MB, 400) a **$19,600** (Shield-14, 100 GB), con "HIPAA compliant" y Private Space obligatorio.

## Why It Matters
El vault despliega **New API con Postgres + Redis** ([[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]]) y sabe que **sin Redis compartido los rate limiters cuentan límites de forma independiente por nodo** ([[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]]). Aquí está el precio de resolverlo: **$3/mes** el Mini de 25 MB con 20 conexiones — pero compartido con multi-tenant, es decir, **no es un Redis dedicado**. El primer plan con **servidor dedicado** es **Premium 7 a $750/mes**.
Esa es la observación que más pesa: **el salto de multi-tenant a single-tenant en Redis gestionado cuesta ×250** ($3 → $750), y ocurre precisamente en el punto donde el producto necesita aislamiento (memoria de sesiones, colas, contadores). Es el mismo patrón de "lo compartido es barato y lo dedicado es otra categoría" que el vault vio en Hetzner y en BuyVM, pero aquí el multiplicador es **mucho mayor**: **×250 en una sola decisión**, no ×6,70.
El dato complementario es que el escalón multi-tenant sí es granular y barato ($3 → $120 cubre de 25 MB a 500 MB), lo que sugiere que **el diseño correcto es Redis multi-tenant barato para lo que no importa y un dedicado caro solo para lo que sí** — con la consecuencia de que un producto con datos de sesión de tenants no puede pagar $750/mes por Redis.

## Nota de verificación
La tabla declara un "Connection Limit" por plan y la familia single-tenant aparece a partir de Premium 7; la captura **no publica el SLA, los créditos ni el precio del Private Space** para las familias Private y Shield.
