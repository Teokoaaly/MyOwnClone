---
id: 2026-1029-upstash-paygo-model
type: atom
certainty: solid
sources: [sources/2026-10-29-upstash-redis-pricing.md]
links: ["[[2026-1029-upstash-free-tier]]", "[[2026-1029-upstash-command-billing]]"]
---

## Claim

The Pay as You Go plan charges $0.20 per 100K commands with unlimited commands, 100 GB data size, unlimited monthly bandwidth (free up to 200 GB, then $0.03/GB beyond), and supports AWS, GCP, FLY, and Vercel platforms.

## Why It Matters

Pay as You Go offers elastic pricing for variable traffic — you only pay for actual usage, which is ideal for unpredictable workloads, but costs can spiral if command volume grows unchecked without a budget limit.

## [FRICTION]

> [[2026-1029-upstash-free-tier]] (escrita hoy) da 500K commands gratis — el modelo paygo cobra $0,20 por 100K, lo que significa que los primeros 50K commands efectivamente cuestan $0,10, y cualquier uso beyond 500K empieza a tener un coste directo que el free tier oculta.

> [[2026-1029-upstash-budget-feature]] (por crear) existe un límite de presupuesto en paygo que envía email a 70% y 90%, pero el modelo paygo no impone un teto duro al coste total — el usuario debe monitorizar activamente o arriesgarse a cobros inesperados. Esta falta de ceiling automático fricciona con la promesa de "presupuesto controlado".

Ambas no pueden ser completamente correctas: o el budget feature resuelve el problema de costes inesperados, o sigue siendo responsabilidad del usuario monitorizar y el modelo sigue having no ceiling hard. Marcado para juicio humano, no auto-resuelto.