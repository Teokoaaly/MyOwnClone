---
id: 2026-1029-upstash-free-tier
type: atom
certainty: solid
sources: [sources/2026-10-29-upstash-redis-pricing.md]
links: ["[[2026-1029-upstash-paygo-model]]", "[[2026-1029-upstash-fixed-plans]]"]
---

## Claim

The Upstash Free tier costs $0/month and includes 250 MB data size, 10 GB monthly bandwidth, and 500K commands per month, making it suitable for prototypes and hobby projects.

## Why It Matters

The free tier lowers the barrier to entry for developers wanting to test Redis without cost, but the strict limits (250 MB, 500K commands) mean it cannot support production workloads or sustained development use.

## [FRICTION]

> [[2026-1029-upstash-paygo-model]] (escrita hoy) ofrece 100 GB de datos y comandos ilimitados por $0,20 por 100K — la diferencia de escala entre 500K gratis y 100 GB pagados es órdenes de magnitud, lo que sugiere que el free tier es genuinamente solo para prototipado, no una vía deupgrade suave.

> [[2026-1029-upstash-fixed-plans]] (escrita hoy) comienza en $10/month por 250 MB — el free tier y los fixed plans comparten el mismo límite de datos, lo que plantea si el free tier es simplemente una muestra del fixed 250MB o un caso separado completamente.

Ambas no pueden ser completamente correctas: o el free tier es un embudo hacia paygo/fixed, o es un caso de uso genuinamente distinto (prototipado puro) que rara vez necesita upgrade. Marcado para juicio humano, no auto-resuelto.