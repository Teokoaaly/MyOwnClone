---
id: 2026-1024-lowendbox-vps-anuales-de-10-a-11-dolares-no-mensuales
type: atom
certainty: solid
sources: [sources/2026-10-23-lowendbox-1-usd-vps.md, sources/2026-10-23-lowendbox-2-usd-vps.md]
links: ["[[2026-1024-lowendbox-cloudserver-leb-1gb-kvm-10-dolares-al-ano]]", "[[2026-1024-lowendbox-racknerd-leb-768mb-10-28-sin-stock]]", "[[2026-1024-lowendbox-cuarto-escalon-de-precio-10-dolares-al-ano]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]"]
---

## Claim
Las cuatro ofertas del artículo "VPS For About $1/Month or $12/Year" se facturan **todas con periodicidad anual**, no mensual: **ServerHost $11.00/year (80% off)**, **CloudServer $10.00/year**, **DediRock $10.18/year** y **RackNerd $10.28/year**. El propio titular lo reconoce: la sección se titula *"About $1/Month or $12/Year"*, es decir, los ~$10–11,28 anuales equivalen a **$0,83–$0,88 al mes** pagando por adelantado, no a un precio mensual de $1.

## Why It Matters
Corrige la lectura de la etiqueta "1 USD VPS" que el propio artículo usa en su entradilla (*"those who are searching for $1 USD VPS without having to prepay!"*): la realidad publicada es **prepago anual obligatorio**. Para el modelo de coste del vault esto significa que el suelo real de hosting medido es de ~$120/año, no $12/año, y que el compromiso es anual y no mensual — un VPS de $10/año no se puede apagar en un mes malo. Es un dato de flujo de caja, no solo de precio, y encaja con el corte por categoría del back-office ([[2026-1022-costes-por-categoria-tenant]]) donde el hosting aún no aparece como línea propia. Las cuatro cifras están transcritas literalmente de la fuente.

## [FRICTION]
> [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]] afirma que "ningún plan del catálogo de Hetzner Cloud cabe en un presupuesto de €4/mes" y concluye que "el VPS de €4 tiene que venir de otro proveedor o de un modelo distinto".
> Este átomo presiona esa creencia en su lectura general: el precio real por debajo de €4/mes existe y es publicable — $10–11,28 **anuales** equivalen a menos de $1/mes — pero llega con una condición que Hetzner no impone: **pago por adelantado de un año entero**, con la consecuencia de que no hay opción mensual ni de salida anticipada.
> Ambas no pueden ser completamente correctas si se leen como afirmaciones sobre "el coste de un VPS": o el suelo de ~€6/mes es una verdad que aplica solo a Hetzner, o existe una categoría más barata que compra commitment anual a cambio de precio. Marcado para juicio humano, no auto-resuelto: el artículo no publica si el prepago es reembolsable ni si el precio se renueva al mismo importe.

## [NOTA 2026-10-24 — LowEndBox $2]
Fuente: `sources/2026-10-23-lowendbox-2-usd-vps.md`. El patrón de **prepago anual** se repite sin cambios en la lista hermana: el encabezado de sección es "**VPS For About $2/Month or $24/Year**" y los cinco precios son **anuales** ($16.88, $20.88, $20.98, $21.88, $23.88/year), no mensuales. Es decir, el titular "$2/month" es el **equivalente mensual del pago del año por adelantado**, tal como ocurría con "$1/Month or $12/Year". La capacidad sí sube (1,5–2 GB / 20–50 GB / 2–5 TB), pero **la condición comercial no**: commitment de un año, sin opción mensual ni salida anticipada. Ver [[2026-1024-lowendbox-2-usd-escalon-16-88-a-23-88-al-ano]] y [[2026-1024-lowendbox-2-usd-cloudserver-2gb-23-88-new-york]].

## Nota de extensión 2026-10-26 — ServerHunter
Fuente: `sources/2026-10-25-serverhunter-cheap-vps.md`. El **prepago anual** que este átomo midió en LowEndBox aparece en ServerHunter como **periodicidad explícita y cuantificada**, y a un nivel de precio muy inferior. En la tabla de ServerHunter (ordenada por "Lowest price") el suelo es **$0.29 USD** en cinco filas, con cuatro `NAT-128` de Gullo's Hosting marcadas **"Annual billing"** y el `NanoVPS-II 384` de Centerfield Ltd también con "Annual billing" (ver [[2026-1026-serverhunter-suelo-de-029-con-128-mb-y-ipv4-nat]]). Y la misma oferta aparece **a dos precios según el periodo**: $0.29 con "Annual billing" frente a $0.33 sin etiqueta, y $0.31 ("(Annual)") frente a $0.42 ("(Semiannual)") — **hasta un 26,2 % de descuento por el compromiso anual** (ver [[2026-1026-serverhunter-periodicidad-como-eje-de-precio-en-la-misma-oferta]]). La consecuencia para el átomo es de alcance: **el suelo de hosting medido por el vault baja de ~$10–11/año a ~$3,48/año** si el precio es mensual, por debajo del SLICE 512 de BuyVM a $24/año. Lo que no cambia es la conclusión estructural: **el precio más bajo del mercado llega con 128 MB de RAM, IPv4 compartida y stock desconocido**, es decir, sigue siendo un nodo auxiliar y no el host principal, y el mismo patrón de compromiso anual que aquí se documenta es ahora un eje de precio medible y no una etiqueta.
