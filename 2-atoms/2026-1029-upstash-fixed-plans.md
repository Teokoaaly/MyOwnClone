---
id: 2026-1029-upstash-fixed-plans
type: atom
certainty: solid
sources: [sources/2026-10-29-upstash-redis-pricing.md]
links: ["[[2026-1029-upstash-free-tier]]", "[[2026-1029-upstash-read-regions]]"]
---

## Claim

Upstash Fixed plans range from $10/month (250 MB, 50 GB bandwidth) to $1500/month (500 GB, 20 TB bandwidth), with predictable pricing based on data size and optional read regions at +$5/+$10/+$50/+$100/+$200/+$400/+$750 per region, and include uptime SLA, multi-zone HA, encryption, SOC-2, Prometheus, Grafana, and Insights.

## Why It Matters

Fixed plans provide cost predictability for consistent workloads — you pay once per month for data size and bandwidth, not per command — but the per-region add-on cost can make multi-region deployments expensive.

## [FRICTION]

> [[2026-1029-upstash-free-tier]] (escrita hoy) también incluye 250 MB — el fixed 250MB cuesta $10/month mientras que el free tier es gratis, lo que sugiere que fixed no es más que paid con garantías (SLA, HA) y dominio personalizado, no un upgrade de features genuinas.

> [[2026-1029-upstash-read-regions]] (por crear) los fixed plans añaden +$5 a +$750 por región de lectura, lo que significa que una base con 3 regiones puede triplicar o cuadruplicar el coste base — este modelo de costes geográficos fricciona con la idea de que Redis es "fácilmente multi-region" sin penalty significativo.

Ambas no pueden ser completamente correctas: o el costode regions es un penalty menor por fiabilidad, o hace que los fixed plans sean prohibitivos para multi-region y la propuesta de valor colapse. Marcado para juicio humano, no auto-resuelto.