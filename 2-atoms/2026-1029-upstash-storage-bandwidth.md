---
id: 2026-1029-upstash-storage-bandwidth
type: atom
certainty: solid
sources: [sources/2026-10-29-upstash-redis-pricing.md]
links: ["[[2026-1029-upstash-command-billing]]", "[[2026-1029-upstash-enterprise]]"]
---

## Claim

Storage costs $0.25 per GB beyond the first 1 GB free; bandwidth is free up to 200 GB/month on pay as you go, then $0.03/GB; Fixed plans include bandwidth limits from 50 GB to 20 TB depending on tier; max data size ranges from 250 MB (Free/Fixed 250MB) to 500 GB (Fixed 500GB/Enterprise 10TB).

## Why It Matters

Storage and bandwidth are often the hidden cost drivers — keeping data under 1 GB avoids the $0.25/GB charge, and staying under 200 GB/month bandwidth avoids the $0.03/GB overage, but traffic-heavy workloads can accumulate costs quickly.

## [FRICTION]

> [[2026-1029-upstash-command-billing]] (escrita hoy) fixed plans no tienen billing de commands, solo data size + bandwidth — esto crea un tercer régimen donde storage/bandwidth son el costo principal vs. paygo donde commands son el costo principal, y las dos nociones friccionan si un usuario cambia de plan mid-month.

> [[2026-1029-upstash-enterprise]] (por crear) Enterprise tiene datos ilimitados y bandwidth ilimitado custom — si el storage cost de $0,25/GB se aplica también a Enterprise o si hay acuerdos a medida, el passage de fixed 500GB ($1500) a Enterprise podría ser un ahorro o un costocamuflando.

Ambas no pueden ser completamente correctas: o los costos de storage/bandwidth son transversales a todos los planes, o Enterprise negocia exenciones y la estructura de costos deja de ser comparable. Marcado para juicio humano, no auto-resuelto.