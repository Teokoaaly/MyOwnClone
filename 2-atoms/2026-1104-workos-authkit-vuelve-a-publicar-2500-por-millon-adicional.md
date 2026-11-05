---
id: 2026-1104-workos-authkit-vuelve-a-publicar-2500-por-millon-adicional
type: atom
certainty: solid
sources: [sources/2026-11-04-workos-pricing.md]
links: ["[[2026-1103-workos-calculadora-interactiva-y-cta-schedule-a-call]]", "[[2026-1031-workos-authkit-primer-millon-de-mau-gratis]]", "[[2026-1104-workos-precios-estables-en-cinco-capturas]]"]
---

## Claim
El volcado crudo del **2026-11-04** de workos.com/pricing (1.067 palabras) vuelve a renderizar el bloque de precio de **AuthKit** que el volcado del 11-03 no traía: bajo el calculador aparecen las filas literales **"Up to 1 million users — Free"** y **"Per additional 1M users — $2,500 / mo"**. Es decir, la cifra de **$2.500/mes por cada millón adicional de MAU** está **publicada en la página real** (no solo en las capturas condensadas del 10-31, 11-01 y 11-02). La tabla de AuthKit solo publica ese bloque: **no hay filas intermedias ni escalones por debajo de 5M+** de MAU, aunque el deslizador del calculador sí llega hasta "5M+".

## Why It Matters
Cierra (a favor de la existencia de la cifra) la fricción abierta en [[2026-1103-workos-calculadora-interactiva-y-cta-schedule-a-call]], que sostenía que el volcado crudo del 11-03 no publicaba ninguna cifra por encima de 1M de MAU y que por tanto la cifra de $2.500 podía proceder de una transcripción condensada. El 11-04 es también un volcado crudo (no una tabla) y **sí** trae las dos filas, lo que refuerza que la cifra es de la página y que el 11-03 fue un render parcial (la sección de soporte tampoco salió en el 11-03 y sí en el 11-04).

Para el vault la conclusión de [[2026-1031-workos-authkit-primer-millon-de-mau-gratis]] queda corroborada en su parte cuantitativa: la partida de usuarios de WorkOS es **$0 hasta 1M de MAU** y el primer escalón cuesta **$2.500/mes**, inalcanzable para un SaaS multi-tenant en beta con presupuesto de ≤ €4/mes. La confirmación literal de los importes y la ausencia de cualquier cambio en ellos queda en [[2026-1104-workos-precios-estables-en-cinco-capturas]].

## [FRICTION]
> [[2026-1103-workos-calculadora-interactiva-y-cta-schedule-a-call]] afirma, sobre la captura del 2026-11-03, que "**no publica ninguna cifra por encima de 1M de MAU**" y que el único precio impreso era "$0 /month $0.00 — Free", y deja abierto que "esa cifra procedía de una transcripción condensada de una captura anterior y **no está publicada en la página**".
> Este átomo presiona esa creencia porque la captura del **2026-11-04**, del mismo tipo de volcado crudo y con la calculadora presente (deslizador "0 1M 2M 3M 4M 5M+"), **sí imprime** "$2,500 / mo" en la fila "Per additional 1M users".
> Ambas no pueden ser completamente correctas: o el 11-03 fue un render truncado que se saltó la tabla de precios de AuthKit (lo más probable, dado que tampoco renderizó la sección de soporte), o el 11-03 y el 11-04 son renders de la misma página en estados distintos. Marcado para juicio humano, no auto-resuelto: lo que sí queda asentado es que la cifra **existe en la página** y que el 11-03 no sirve para refutarla.

## Nota de verificación
sources/2026-11-04-workos-pricing.md, líneas 85-101: encabezado "### Pricing" con las filas "- Up to 1 million users / Free" y "- Per additional 1M users / $2,500 / mo". La ausencia de filas intermedias y el tope "5M+" del deslizador (líneas 65-73) son lectura literal del mismo bloque.
