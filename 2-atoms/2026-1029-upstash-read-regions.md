---
id: 2026-1029-upstash-read-regions
type: atom
certainty: solid
sources: [sources/2026-10-29-upstash-redis-pricing.md]
links: ["[[2026-1029-upstash-fixed-plans]]", "[[2026-1029-upstash-enterprise]]"]
---

## Claim

Fixed plans charge +$5/month for read regions (read replica) starting from the 250 MB tier, with costs scaling to +$750/month for the 500 GB tier; read regions provide high availability with primary replicas and read replicas across zones, and command replication adds to bandwidth usage.

## Why It Matters

Read regions improve latency and availability for geographically distributed users, but the per-region cost can significantly increase monthly bills — a 3-region setup on a modest plan can effectively triple the base price.

## [FRICTION]

> [[2026-1029-upstash-fixed-plans]] (escrita hoy) fixed plans start at $10/month +$5/region — 3 regions añaden $15 al mes, haciendo que el plan base pase de $10 a $25, un aumento del 150% sobre el costo base para fiabilidad geográfica.

> [[2026-1029-upstash-enterprise]] (por crear) Enterprise incluye multi-zone HA por defecto — la pregunta es si el costode +$5/region en fixed plans es necesario si Enterprise ya incluye HA multi-zone sin penalty adicional, o si el modelo de costes por region es un penalty por fiabilidad que Enterprise absorbe en su pricing custom.

Ambas no pueden ser completamente correctas: o el costode regions es un penalty razonable por HA, o es un costocamuflando que hace que multi-region sea economicamente inviable para la mayoría de workloads. Marcado para juicio humano, no auto-resuelto.