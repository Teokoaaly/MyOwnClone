---
id: 2026-1023-hetzner-escalera-de-precios-y-salto-a-dedicados
type: atom
certainty: solid
sources: [sources/2026-10-22-hetzner-cloud.md]
links: ["[[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]", "[[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]"]
---

## Claim
La página de Hetzner Cloud presenta tres familias de plan con precio "starting from", siempre **excl. VAT**: **Cost-Optimized** (Shared) desde **€ 5.99/mes**, **Regular Performance** (Shared) desde **€ 6.49/mes** y **General Purpose** (Dedicated vCPUs) desde **€ 43.49/mes**. Los saltos son de **+€ 0.50 (×1.08)** entre los dos planos compartidos y de **+€ 37.00 (×6.70)** al pasar a recursos dedicados; en total, el plan dedicado cuesta **×7.26** el plan más barato.

## Why It Matters
La escalera define qué significa "subir de tier" en coste: moverse de Cost-Optimized a Regular Performance es marginal (+8 %), mientras que saltar a vCPU dedicadas multiplica la factura por más de seis. Para el modelo de coste del vault, esto separa dos decisiones distintas — *rendimiento compartido* (barato, variable, adequate para desarrollo/pruebas) frente a *rendimiento dedicado* (caro, constante, para carga de producción sostenida), tal como describe [[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]. También fija el techo del rango: si el presupuesto de infraestructura es pequeño, el único tramo del catálogo realmente utilizable son los dos primeros escalones, los que juntos están en [[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]] y [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]].

## Nota de lectura
Los rótulos que acompaña a cada familia describen el uso declarado: "Perfect for test environments / Extremely cost-effective / Low CPU usage" (Cost-Optimized), "Best price-performance ratio / Inexpensive due to shared resources / Low to medium CPU usage" (Regular Performance) y "Optimized for business applications / Dedicated vCPUs / Constantly high CPU usage" (General Purpose). "Shared Resources — Currently not available" aparece en la captura inmediatamente antes del bloque Cost-Optimized, lo que deja abierto si ese escalón está disponible en todas las zonas.
