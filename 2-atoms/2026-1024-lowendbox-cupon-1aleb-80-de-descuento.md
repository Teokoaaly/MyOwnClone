---
id: 2026-1024-lowendbox-cupon-1aleb-80-de-descuento
type: atom
certainty: solid
sources: [sources/2026-10-23-lowendbox-1-usd-vps.md, sources/2026-10-23-lowendbox-2-usd-vps.md]
links: ["[[2026-1024-lowendbox-serverhost-leb-1gb-kvm-11-dolares-al-ano]]", "[[2026-1024-lowendbox-vps-anuales-de-10-a-11-dolares-no-mensuales]]", "[[2026-1024-lowendbox-captura-sin-comentarios-ni-barra-lateral]]", "[[2026-1024-lowendbox-lowend-score-cinco-estrellas-como-filtro]]"]
---

## Claim
Solo la oferta de **ServerHost** se publica como **promoción con cupón**: "$11.00/year (**80% off**)" con **Coupon Code `1ALEB`**, y el enlace de compra es un enlace de orden con el código ya embebido (`...order/.../ssd-4-gb?promocode=1ALEB&billingcycle=annually`). Las otras tres (CloudServer, DediRock, RackNerd) aparecen a precio plano **sin código ni descuento declarado**, y ServerHost es el único cuyo precio se presenta como precio ya descontado respecto de una lista.

## Why It Matters
Distingue dos statuses distintos dentro del mismo catálogo: **precio de lista permanente** (CloudServer $10, DediRock $10.18, RackNerd $10.28) frente a **precio promocional con cupón** (ServerHost $11 con 80% off ya aplicado). Para el modelo de coste del vault la diferencia es de ~$10 al año, pero conceptualmente es la diferencia entre un coste recurrente conocido y un coste que sube al expirar el cupón o al no renovar el trato LEB — por eso el átomo [[2026-1024-lowendbox-vps-anuales-de-10-a-11-dolares-no-mensuales]] trata estos importes como **precio de lista actual, no precio estructural**. El que los enlaces incluyan `billingcycle=annually` confirma también que el ciclo de facturación es anual y no mensual, algo que el titular "$1/Month" no deja claro.

## Nota de verificación
El cupón, el porcentaje y la URL con el parámetro `promocode=1aleb&billingcycle=annually` están transcritos literalmente. La fuente **no** publica fecha de caducidad del cupón ni el precio de lista sin descuento del que parte el "80% off".

## [NOTA 2026-10-24 — LowEndBox $2]
Fuente: `sources/2026-10-23-lowendbox-2-usd-vps.md`. El patrón de cupón por escalón queda **confirmado y ampliado**: la lista hermana de $2 usa un código distinto, **`2LEBA` con "75% off"** (ServerHost $21.88/year), frente al **`1ALEB` con "80% off"** de esta lista. Las otras cuatro ofertas de $2 (RackNerd 1.5 GB y 2 GB, DediRock 2 GB, CloudServer 2 GB) aparecen **a precio plano, sin código ni descuento declarado**, igual que las de $1. La conclusión operativa se refuerza: el precio de lista LEB debe tratarse como **precio condicionado a una promoción no fechada**, con un descuento que **baja a medida que sube el precio base** (80% en $1, 75% en $2). Ver [[2026-1024-lowendbox-2-usd-cupon-2leba-75-de-descuento]].
