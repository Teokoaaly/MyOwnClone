---
id: 2026-1024-lowendbox-2-usd-cupon-2leba-75-de-descuento
type: atom
certainty: solid
sources: [sources/2026-10-23-lowendbox-2-usd-vps.md]
links: ["[[2026-1024-lowendbox-cupon-1aleb-80-de-descuento]]", "[[2026-1024-lowendbox-2-usd-serverhost-2gb-21-88-cupon-2leba]]", "[[2026-1024-lowendbox-2-usd-escalon-16-88-a-23-88-al-ano]]", "[[2026-1024-lowendbox-2-usd-cuatro-proveedores-con-dos-planes-leb]]"]
---

## Claim
Cada lista de LowEndBox tiene **su propio código de cupón LEB y su propio porcentaje de descuento**: en la lista de $1 el cupón es **`1ALEB`** con "**80% off**" (ServerHost $11.00/year); en la lista de $2 el cupón es **`2LEBA`** con "**75% off**" (ServerHost $21.88/year). La URL de orden de la lista de $2 lleva el código embebido (`...linux-vps-ssd-2-gb?promocode=2LEBA&billingcycle=annually`). Las otras cuatro ofertas de $2 (RackNerd ×2, DediRock, CloudServer) aparecen a **precio plano, sin código ni descuento declarado**.

## Why It Matters
Establece el patrón de que **el cupón no es una promoción del proveedor sino un contrato editorial por escalón**: LowEndBox reparte descuentos distintos por página ($1 → 80% off, $2 → 75% off), y el descuento **baja a medida que sube el precio base**. Consecuencia operativa para el vault: el precio efectivo de cualquier oferta LEB **no es el número de la tabla hasta aplicar el cupón de su lista**, y un cupón de una lista no es reutilizable en la otra. Refuerza el criterio del átomo de cupón de $1 (ver [[2026-1024-lowendbox-cupon-1aleb-80-de-descuento]]): el precio de lista de LEB debe tratarse como **precio de lista actual condicionado a una promo no fechada**, no como coste recurrente estable, porque ni el porcentaje ni la vigencia están publicados.

## Nota de verificación
Códigos, porcentajes, precios y URL con `promocode=2LEBA&billingcycle=annually` transcritos literalmente. La fuente **no** publica: fecha de caducidad de los cupones, precio de lista sin descuento del que parte el "75% off", ni si `2LEBA` funciona también sobre el plan de 1 GB de la lista de $1.
