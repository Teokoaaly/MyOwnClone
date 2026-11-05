---
id: 2026-1102-clerk-precios-sin-cambios-en-48-horas
type: atom
certainty: solid
sources: [sources/2026-11-02-clerk-pricing.md]
links: ["[[2026-1101-clerk-precios-base-hobby-pro-business]]", "[[2026-1102-auth0-precios-sin-cambios-en-48-horas]]", "[[2026-1031-clerk-pricing]]"]
---

## Claim
Las capturas de la página de precios de Clerk del **2026-11-01 y del 2026-11-02 son idénticas salvo la fecha de captura**: mismas cifras ($20/$25 Pro, $250/$300 Business, mismos tramos de MRU, MRO, SSO, protección y verificaciones), misma feature matrix y misma FAQ. En 48 horas **no cambió ni un precio ni una feature** en clerk.com/pricing.

## Why It Matters
Es un dato de **estabilidad de precios** y completes la fotografía que ya tenía el vault para Auth0: los dos proveedores de identidad candidatos capturados el 1 y el 2 de noviembre **están estables en la ventana medida** ([[2026-1102-auth0-precios-sin-cambios-en-48-horas]]), mientras que los proveedores de hosting baratos del corpus sí han movido precios entre capturas. La consecuencia operativa para MyOwnClone es que **el número de identidad se puede fixear ahora en el presupuesto**: si se elige Clerk, el coste conocido es $0 (Hobby) o $20/mes (Pro), sin riesgo de recargo de tarifa a mitad de ciclo; y para la pregunta abierta del vault —si domina el coste por asiento o el de infraestructura— la estabilidad de los proveedores de identidad refuerza que **el coste variable del stack vendrá del hosting y del crecimiento de tenants, no de cambios de lista en auth**.

## Nota de verificación
Identidad verificada por diff directo tras normalizar la línea `captured:` del frontmatter: la única diferencia entre `sources/2026-11-01-clerk-pricing.md` y `sources/2026-11-02-clerk-pricing.md` es un salto de línea final. Las cifras citadas son las de la captura del 2026-11-02, idénticas a las del 2026-11-01.
