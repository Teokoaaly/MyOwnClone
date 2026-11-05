---
id: 2026-1029-upstash-command-billing
type: atom
certainty: solid
sources: [sources/2026-10-29-upstash-redis-pricing.md]
links: ["[[2026-1029-upstash-paygo-model]]", "[[2026-1029-upstash-storage-bandwidth]]"]
---

## Claim

Upstash billing counts Redis commands at $0.20 per 100K for the Pay as You Go plan; operational commands (AUTH, HELLO, SELECT, COMMAND, CONFIG, INFO, PING, RESET, QUIT) are not charged; Fixed plans have no command-count billing whatsoever.

## Why It Matters

Knowing which commands are billable helps optimize costs — skipping PING/HELLO/INFO in tight loops saves money on pay as you go, but Fixed plan users ignore command costs entirely since they pay for data size and bandwidth instead.

## [FRICTION]

> [[2026-1029-upstash-paygo-model]] (escrita hoy) $0,20 por 100K commands — el free tier incluye 500K commands/month gratis, lo que sugiere que los primeros 50K commands en paygo cuestan $0,10 y el umbral de 500K free es un punto de cambio de régimen, no un continuum suave.

> [[2026-1029-upstash-storage-bandwidth]] (por crear) fixed plans tienen billing por data size y bandwidth, no por commands, lo que fricciona con la idea de que "todos los planes cobran por commands" — de hecho, fixed plans explicitly no lo hacen, creando dos regímenes de billing diferentes dependiendo del plan.

Ambas no pueden ser completamente correctas: o hay dos regímenes de billing y el usuario debe conocer cuál aplica, o el billing es uniformemente por commands y la distinción fixed vs paygo es marketing. Marcado para juicio humano, no auto-resuelto.