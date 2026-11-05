---
id: 2026-1023-hetzner-escalera-de-precios-y-salto-a-dedicados
type: atom
certainty: solid
sources: [sources/2026-10-22-hetzner-cloud.md, sources/2026-11-03-hetzner-cloud.md]
links: ["[[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]", "[[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]"]
---

## Claim
La página de Hetzner Cloud presenta tres familias de plan con precio "starting from", siempre **excl. VAT**: **Cost-Optimized** (Shared) desde **€ 5.99/mes**, **Regular Performance** (Shared) desde **€ 6.49/mes** y **General Purpose** (Dedicated vCPUs) desde **€ 43.49/mes**. Los saltos son de **+€ 0.50 (×1.08)** entre los dos planos compartidos y de **+€ 37.00 (×6.70)** al pasar a recursos dedicados; en total, el plan dedicado cuesta **×7.26** el plan más barato.

## Why It Matters
La escalera define qué significa "subir de tier" en coste: moverse de Cost-Optimized a Regular Performance es marginal (+8 %), mientras que saltar a vCPU dedicadas multiplica la factura por más de seis. Para el modelo de coste del vault, esto separa dos decisiones distintas — *rendimiento compartido* (barato, variable, adequate para desarrollo/pruebas) frente a *rendimiento dedicado* (caro, constante, para carga de producción sostenida), tal como describe [[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]. También fija el techo del rango: si el presupuesto de infraestructura es pequeño, el único tramo del catálogo realmente utilizable son los dos primeros escalones, los que juntos están en [[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]] y [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]].

## Nota de lectura
Los rótulos que acompaña a cada familia describen el uso declarado: "Perfect for test environments / Extremely cost-effective / Low CPU usage" (Cost-Optimized), "Best price-performance ratio / Inexpensive due to shared resources / Low to medium CPU usage" (Regular Performance) y "Optimized for business applications / Dedicated vCPUs / Constantly high CPU usage" (General Purpose). "Shared Resources — Currently not available" aparece en la captura inmediatamente antes del bloque Cost-Optimized, lo que deja abierto si ese escalón está disponible en todas las zonas.

## Nota de extensión 2026-11-03
Fuente: `sources/2026-10-31-hetzner-cloud.md`, `sources/2026-11-01-hetzner-cloud.md`, `sources/2026-11-02-hetzner-cloud.md`. Los tres precios "starting from" de esta escalera (**€ 5.99 / € 6.49 / € 43.49**, excl. VAT) se repiten **idénticos en las tres capturas**, con los mismos rótulos de uso y el mismo "Shared Resources — Currently not available" antes del bloque Cost-Optimized. La escalera del vault, por tanto, **está vigente y no se ha movido** en el periodo 2026-10-22 → 2026-11-02.

Lo que las capturas nuevas añaden es que **cada familia tiene además un techo "max/mo." que la escalera no recogía, y ese techo varía entre capturas** sin que cambien los precios de entrada: Cost-Optimized € -25.81 → € -31.19 → € -27.33, Regular Performance € -27.85 → € -33.80 → € -29.65, General Purpose € -187.46 → € -226.48 → € -199.05. La lectura operativa se corrige: el "salto a dedicados" de ×7,26 sobre el plan más barato es el suelo de una **banda** que llega a un orden de € 190–226/mes para un solo servidor dedicado, no a un escalón cerrado de € 43,49 — ver [[2026-1102-hetzner-techo-max-mo-de-cada-familia-varia-entre-capturas]]. La confirmación del precio de entrada con tres capturas fechadas está en [[2026-1102-hetzner-precio-de-entrada-5-99-no-4-67]], que además plantea la fricción con la cifra de € 4,67 afirmada en [[2026-1031-hetzner-cloud]].

## 2026-11-03 — re-verificación
Fuente: `sources/2026-11-03-hetzner-cloud.md`. Los tres precios "starting from" de la escalera (**€ 5.99 / € 6.49 / € 43.49**, excl. VAT) se repiten **idénticos**, con los mismos rótulos de uso y el mismo "Shared Resources — Currently not available" antes del bloque Cost-Optimized (que aparece dos veces, una por cada repetición del carrusel de planes). La escalera del vault **no se ha movido** en el periodo 2026-10-22 → 2026-11-03: sigue siendo un salto de **+€ 0,50 (×1,08)** entre los dos tramos compartidos y **×7,26** del plan más barato al dedicado. Lo que esta captura añade al widget es el techo "max/mo." nuevo de General Purpose (**€ -240.99**, el más alto en cinco capturas), que ensancha la banda dedicada pero **no puede leerse como precio** — ver la fricción planteada en [[2026-1103-hetzner-max-mo-cost-optimized-cero-ruptura-de-serie]].
