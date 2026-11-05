---
id: 2026-1024-brightdata-escalera-de-volumen-141-a-798-gb
type: atom
certainty: solid
sources: [sources/2026-10-24-brightdata-proxy-pricing.md]
links: ["[[2026-1024-brightdata-payg-a-4-por-gb-sin-compromiso]]", "[[2026-1024-brightdata-cupon-50-off-y-match-del-primer-deposito]]", "[[2026-1024-dataimpulse-escalera-de-volumen-por-tipo]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]"]
---

## Claim
Los tres planes con compromiso mensual de Bright Data son **141 GB incluidos por $499/mes** ($7 → **$3.50/GB**), **332 GB incluidos por $999/mes** ($6 → **$3.00/GB**) y **798 GB incluidos por $1.999/mes** ($5 → **$2.50/GB**). Por encima de 1 TB la página remite a "Contact us" con "Custom price per GB", unlimited seats, premium SLA y 99.99 % de uptime de red.

## Why It Matters
El coste de entrada a un plan con compromiso de Bright Data es de **$499/mes por 141 GB**, es decir **$3,54/GB efectivos** — por debajo del PAYG de $4/GB, no por encima, pero a cambio de un **mínimo de gasto mensual de $499**, más de dos órdenes de magnitud por encima del techo de infraestructura de ≤ €4/mes con el que el vault ha construido su ancla ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]). El salto de escalón es de 2× en el desembolso ($499 → $999 → $1.999) para un descuento unitario del 14 % y del 17 %: **el descuento por volumen de Bright Data es marginal y está eclipsado por un compromiso de capital enorme**, exactamente el patrón inverso al de DataImpulse, donde el salto de $50 a $800 compra un 20 % de descuento unitario ([[2026-1024-dataimpulse-escalera-de-volumen-por-tipo]]).
La consecuencia operativa es que el único modo de comprar Bright Data con presupuesto pequeño es el PAYG, y que el PAYG es **precisamente el modo sin SLA, sin brillo en las cifras corporativas y sin el programa enterprise** ([[2026-1024-brightdata-payg-a-4-por-gb-sin-compromiso]]).

## [FRICTION]
> [[2026-1024-dataimpulse-escalera-de-volumen-por-tipo]] (escrita el 2026-10-24) afirma que "el punto de economies of scale real está en el contrato Custom+ de 5TB+, no en el autoservicio", con el descuento unitario limitado al 10–20 % en el escalón Advanced.
> Este átomo confirma ese patrón en un segundo proveedor y añade la variable que faltaba: **el descuento unitario del 14 % en el primer escalón de Bright Data cuesta $499/mes de golpe**. Si la comparación de proveedores se hace solo sobre $/GB, ambos parecen similares; si se hace sobre $/mes comprometido, Bright Data es 10× más caro en el primer escalón que DataImpulse ($50) y 8× más caro en el tercero.
> Ambas no pueden ser completamente correctas: o el criterio de selección de proveedor de proxy del vault es $/GB (y entonces el mínimo de $499 es un coste invisible que dominates el presupuesto), o es $/mes comprometido (y entonces DataImpulse es el único proveedor viable para el vault). Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
Volúmenes e importes transcritos literalmente. La captura **no** publica: si los GB incluidos son acumulativos o caducan cada mes, si el excedente se factura al mismo $/GB, ni qué incluye exactamente "Custom price per GB" por encima de 1 TB.


## Nota de extensión 2026-10-27
La escalera de 2Captcha confirma la forma general de la escalera de Bright Data —**precio de entrada alto y descuento fuerte al subir de volumen**— y añade dos magnitudes que el vault no tenía. **Descuento**: −68,7 % en el tramo de 10 TB, contra los **−14 % y −17 %** de Bright Data y el **−26,7 %** de Decodo. **Precio unitario final**: **$1.25/GB**, por debajo del $2.50/GB del tramo de 798 GB de Bright Data.

La diferencia de fondo es el compromiso: **Bright Data exige $499/mes en su primer tramo**, y su "−14 %" es un descuento pequeño **sobre una base de compromiso alto**; 2Captcha alcanza un descuento **4,8 veces mayor** partiendo de un tramo de **1 GB**. Es decir, **la profundidad de la escalera no está correlacionada con la exigencia de capital**: hay una escalera profunda sobre un compromiso bajo y una escalera superficial sobre un compromiso alto. La afirmación de este átomo —que "**el descuento unitario del 14 % en el primer escalón de Bright Data cuesta $499/mes de golpe**"— **se aplica al subconjunto de planes mensuales** y el vault debe corregirla como una generalización, no como una ley del sector.

Nota: Bright Data declara el cupón `RESIGB50` y el *match* del primer depósito; **2Captcha no publica ninguna promoción**, solo precios y descuentos de volumen.
