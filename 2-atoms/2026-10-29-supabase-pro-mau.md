---
id: 2026-10-29-supabase-pro-mau
type: atom
certainty: solid
sources: [sources/2026-10-29-supabase-pricing.md]
links: ["[[2026-10-29-posthog-per-event-pricing]]", "[[2026-10-29-supabase-free-plan]]"]
---

## Claim

The Supabase Pro plan at $25/month includes 100,000 monthly active users, then $0.00325 per additional MAU; the Free plan includes 50,000 MAUs included.

## Why It Matters

The MAU overage rate of $0.00325 creates a predictable cost ceiling for growing applications, but teams must monitor MAU growth carefully since costs scale linearly beyond the included quota — a single project exceeding 1M MAUs would incur $250/mo in overage alone.

## [FRICTION]

> [[2026-10-29-posthog-per-event-pricing]] charges $2.50 per million messages over the included 5M, whereas Supabase Pro charges $0.00325 per MAU over 100K — the Posthog model is volume-based per million while Supabase is per-active-user, meaning Supabase overage can accumulate faster for applications with many low-activity users, while Posthog overage favors applications with bursty high-volume messaging.

> Ambas pueden ser correctas para distintos patrones de uso: si un aplicación tiene muchos usuarios con actividad baja, los $0.00325 por MAU de Supabase se acumulan linealmente y pueden ser más costosos; si el patrón es mensajes esporádicos masivos, el modelo de Posthog por millones es más eficiente. El juicio humano debe decidir según el patrón de tráfico real. Marcado para juicio humano, no auto-resuelto.