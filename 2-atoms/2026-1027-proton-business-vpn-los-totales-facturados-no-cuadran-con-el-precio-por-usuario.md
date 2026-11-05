---
id: 2026-1027-proton-business-vpn-los-totales-facturados-no-cuadran-con-el-precio-por-usuario
type: atom
certainty: solid
sources: [sources/2026-10-26-proton-business-vpn-pricing.md]
links: ["[[2026-1027-proton-business-vpn-precios-publicados-por-usuario-en-cuatro-planes]]", "[[2026-1024-protonvpn-el-descuento-caduza-y-la-renovacion-sube-a-6-99]]", "[[2026-1024-proton-captura-con-placeholders-xx-y-tabla-en-neerlandes]]"]
---

## Claim
Las cuatro tarjetas de plan cierran con un total facturado literal que **no siempre cuadra con su propio precio unitario**: VPN Essentials declara **"Billed at $167.76 for 2 users."** (sí cuadra: $6,99 × 2 × 12 = $167,76), VPN Professional declara **"Billed at $719.64 for 2 users."** (no cuadra: $9,99 × 2 × 12 = $239,76), VPN and Pass Professional declara **"Billed at $875.52 for 3 users."** (no cuadra: $10,99 × 3 × 12 = $395,64) y Workspace Standard declara **"Billed at $155.88 every 12 months."** (sí cuadra con $12,99 × 12 = $155,88, para una sola licencia, ya que no se indica número de usuarios). Los cuatro totales llevan además la línea **"Taxes may apply."**.

## Why It Matters
El vault ya había registrado que la página de consumo de Proton es **parcialmente renderizada**, con marcadores sin sustituir ("$XX.XX", "Save XX%") y la tabla comparativa traducida al neerlandés ([[2026-1024-proton-captura-con-placeholders-xx-y-tabla-en-neerlandes]]): esta captura muestra que **el defecto no es solo de plantilla, es de los totales concretos que se publican**. Dos de los cuatro totales son irreproducibles con el precio y el número de usuarios que la propia tarjeta muestra, y las magnitudes no cuadran en ningún sentido razonable: $719,64 son exactamente **$19,99 × 3 × 12** y $875,52 son **$24,32 × 3 × 12** —importes que **no aparecen en ninguna parte de la página**—. La lectura más probable es que el extractor haya **mezclado el estado `Monthly` con el `Yearly`** del conmutador, pero la captura no permite demostrarlo. La consecuencia operativa para el vault es dura: **la única cifra de gasto real que la página da por plan (el total facturado) no es fiable, y la fiable (precio por usuario) no permite reconstruir el total sin conocer el conmutador activo**. Cualquier cálculo de coste de la línea B2B tiene que apoyarse en el precio unitario y declarar el supuesto, nunca en el total impreso ([[2026-1024-protonvpn-el-descuento-caduza-y-la-renovacion-sube-a-6-99]]).

## [FRICTION]
> [[2026-1024-protonvpn-el-descuento-caduza-y-la-renovacion-sube-a-6-99]] (escrita el 2026-10-24) establece la regla de lectura del vault para Proton: «el precio **sube al 100 % en la primera renovación** ($3,49 → $6,99) sin que ningún elemento de la página lo alerte, porque el titular es el del primer periodo», y por tanto «la cifra correcta de Proton no es $3,49, es $6,99».
> Este átomo presiona esa regla en la línea B2B: allí **no hay ninguna regla de lectura segura**. El precio unitario es explícito ($6,99 / $9,99 / $10,99 / $12,99) pero los totales publicados no son reproducibles, de modo que **el principio "el precio unitario publicado es la cifra correcta" tampoco basta**: hay que declarar que se está usando el precio unitario del conmutador `Yearly` y que los totales de la página **no se usan como fuente de gasto**.
> Ambas no pueden ser completamente correctas al mismo tiempo: o la página B2B tiene un error de renderizado —y entonces sus totales no son datos—, o los precios unitarios están recalculados sobre otra base y no son comparables con los totales. Marcado para juicio humano, no auto-resuelto.
