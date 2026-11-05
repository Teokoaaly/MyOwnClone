---
id: 2026-10-29-supabase-free-plan
type: atom
certainty: solid
sources: [sources/2026-10-29-supabase-pricing.md]
links: ["[[2026-10-29-posthog-free-tier]]", "[[2026-1029-aws-ses-aws-free-tier]]"]
---

## Claim

The Supabase Free plan at $0/month includes unlimited API requests, 50,000 monthly active users, 500 MB database size per project, 5 GB egress, 5 GB cached egress, 1 GB file storage, and community support; free projects are paused after 1 week of inactivity with a limit of 2 active projects.

## Why It Matters

The Free plan serves as the entry point for hobbyists and simple websites, but its strict limits (500 MB DB, 5 GB egress, 2-project cap, 1-week pause threshold) make it unsuitable for sustained applications without upgrading, shaping the funnel from hobby to paid tier.

## [FRICTION]

> [[2026-10-29-posthog-free-tier]] offers 1 GB included log ingestion and 100 GB total database size, whereas Supabase Free includes only 500 MB database size per project — the Posthog free tier provides double the database capacity but Supabase provides unlimited API requests, creating different trade-offs for data-heavy vs. API-heavy workloads.

> Ambas no pueden ser completamente correctas: la diferencia de tamaño de base de datos (500 MB vs 100 GB) es abismal, pero Supabase incluye ilimitadas peticiones de API mientras que Posthog las limita por plan. El usuario debe evaluar si su workload es más sensato a límites de almacenamiento o a límites de API. Marcado para juicio humano, no auto-resuelto.