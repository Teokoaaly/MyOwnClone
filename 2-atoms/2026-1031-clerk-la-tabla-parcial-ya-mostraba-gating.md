---
id: 2026-1031-clerk-la-tabla-parcial-ya-mostraba-gating
type: atom
certainty: solid
sources: [sources/2026-10-31-clerk-pricing.md]
links: ["[[2026-1031-clerk-pricing]]", "[[2026-1101-clerk-gating-por-plan-contradice-atom-1031]]"]
---

## Claim
La captura del **2026-10-31** de clerk.com/pricing (truncada a mitad de la tabla, termina en la fila "Sign in tokens") **ya mostraba gating explícito en la columna Hobby**: "Remove Clerk branding | **Not included**", "Social connections | **Up to 3** | Unlimited | Unlimited" y "SMS codes | **Not included** | Per SMS fees apply | Per SMS fees apply", además de la fila "Base price | $0 | $25/mo, $20/mo billed annually | $300/mo, $250/mo billed annually" y la escalera de MRU ($0,02 / $0,018 / $0,015 / $0,012).

## Why It Matters
Este átomo sitúa el error del átomo hermano en el sitio correcto: **el dato contradictorio no llegó con las capturas del 11-01/11-02, ya estaba en la fuente del 2026-10-31**. Es decir, la creencia de "Clerk incluye todas las features en todos los tiers" ([[2026-1031-clerk-pricing]]) no se sostiene por una captura posterior más completa, sino que se formó leyendo solo las viñetas de las tarjetas de plan ("+ most authentication features") y saltándose la tabla "Full price breakdown". La consecuencia metodológica para el vault es que **las capturas completas de la página de precios son más fiables que las tarjetas resumen**, y que un átomo sobre un proveedor debe confrontar la tabla antes de afirmar un modelo de gating. El conflicto queda marcado, sin auto-resolver, en [[2026-1101-clerk-gating-por-plan-contradice-atom-1031]].

## [FRICTION]
> [[2026-1031-clerk-pricing]] afirma que "Clerk includes all authentication and user management features across every pricing tier without feature gating".
> Este átomo presiona esa creencia porque **la propia fuente de ese átomo (`sources/2026-10-31-clerk-pricing.md`) la contradice**: las celdas "Not included" y "Up to 3" de la columna Hobby están escritas literalmente en su tabla.
> Ambas no pueden ser completamente correctas. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
Filas "Base price", "Remove Clerk branding", "Social connections" y "SMS codes" de la tabla "Full price breakdown" de `sources/2026-10-31-clerk-pricing.md`, verbatim. El hecho de que la captura esté truncada (termina en la fila "Sign in tokens") se verificó leyendo el archivo completo (229 líneas).
