---
id: 2026-1101-clerk-escalera-de-sobrecoste-mru-por-tramos
type: atom
certainty: solid
sources: [sources/2026-11-01-clerk-pricing.md]
links: ["[[2026-1101-clerk-mru-no-mau-con-primer-dia-gratis]]", "[[2026-1101-clerk-precios-base-hobby-pro-business]]", "[[2026-1101-auth0-definicion-de-mau-y-cobro-al-escalon-superior]]"]
---

## Claim
El sobrecoste de Clerk por MRU es **volumétrico y decreciente**, en cuatro tramos sobre los 50.000 MRU incluidos por app: **50.001–100.000 a $0,02/mes cada uno**; **100.001–1.000.000 a $0,018**; **1.000.001–10.000.000 a $0,015**; **10.000.001+ a $0,012**. Los mismos tramos se aplican en Pro y en Business.

## Why It Matters
Es la fórmula concreta del coste variable de identidad para MyOwnClone, y hace el cálculo de sensibilidad trivial: **1.000 tenants activos de 20 usuarios = 20.000 MRU = $0** (dentro del Hobby); **5.000 tenants = 100.000 MRU = ~$20/mes de sobrecoste** (50.000 MRU × $0,02), más los $20 del plan Pro → **~$40/mes de identidad**, orden de magnitud comparable al hosting completo del producto. Es decir, **el coste de identidad solo se vuelve irrelevante en el tramo gratuito**, igual que el hosting barato del vault: a partir de cierto tamaño, ambos النمو son lineales en el número de tenants/usuarios y la pregunta "asiento o infra" se resuelve comparando dos pendientes, no un techo fijo. La comparación directa con el "billed at the next tier up" de Auth0 ([[2026-1101-auth0-definicion-de-mau-y-cobro-al-escalon-superior]]) muestra dos modelos distintos: Auth0 cobra por escalón de bloque, Clerk cobra por unidad con descuento gradual.

## Nota de verificación
Tramos verbatim de la fila "Included MRUs" de la tabla "Full price breakdown" (captura del 2026-11-01). La aritmética de ejemplo (1.000/5.000 tenants) es lectura operativa de este átomo, no una cifra de la fuente.
