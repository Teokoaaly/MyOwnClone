---
id: 2026-1103-twilio-tercera-renderizacion-texto-plano-sin-algunas-secciones
type: atom
certainty: solid
sources: [sources/2026-11-03-twilio-sms-pricing.md]
links: ["[[2026-1031-twilio-la-captura-del-31-de-octubre-es-una-renderizacion-reducida]]", "[[2026-1102-twilio-precio-estable-entre-capturas-del-1-y-2-de-noviembre]]", "[[2026-1101-twilio-addons-de-features-y-descuentos-no-publicados]]"]
---

## Claim
La captura del **2026-11-03** de `twilio.com/en-us/sms/pricing` es una **tercera variante de renderizado** de la misma página: texto plano sin markdown (ni negritas, ni enlaces, ni imágenes — 9.029 bytes, `word_count: 610` frente a los 15.9 KB / 2.212 palabras del 1 y 2 de noviembre), pero **con todas las tablas de precios completas e idénticas en cifras**. Lo que la variante pierde frente al renderizado del 1–2 de noviembre es contenido, no precios: la fila del **Traffic Optimization Engine ($300/mes)** en la tabla de Features, el FAQ *"What is the base cost to send and receive SMS in the US with Twilio?"*, la sección **Committed-use discounts** (precios enterprise con compromiso anual), los **nombres de los miembros de los grupos A y B** de operadores, la frase *"Twilio helps by handling the carrier nuances in every country you send to"*, los enlaces de descarga de los CSV (`SMSPricing.csv`, `NumbersPricing.csv`), la frase introductoria de precios de números (*"Phone number charges are added to your message volume…"*) y la cláusula *"Review our Privacy Notice for additional details on how we use data."* El titular sí coincide con el del 2 de noviembre (*"SMS and RCS pricing built to break even fast"*) y el sello de vigencia sigue siendo **"current as of October 2026"**.

## Why It Matters
Confirma el patrón ya registrado para la captura del 31 de octubre ([[2026-1031-twilio-la-captura-del-31-de-octubre-es-una-renderizacion-reducida]]): **la misma URL produce renderizados de distinta fidelidad y el `word_count` es un mal indicador de contenido** — un `word_count` menor (610 vs 2.212) aquí no significa "menos producto" sino "menos cromo y menos enlaces". Consecuencia operativa para el vault: **una ausencia en una captura no es una retirada de precio**. Por ejemplo, el Traffic Optimization Engine a $300/mes documentado en [[2026-1101-twilio-addons-de-features-y-descuentos-no-publicados]] no aparece en esta captura, pero sigue respaldado por la fuente del 1 de noviembre: no debearse de reescribir ese átomo, ni marcarlo como superado, a partir de una captura reducida. Al mismo tiempo, la estabilidad de las cifras queda reforzada por un tercer punto de datos ([[2026-1102-twilio-precio-estable-entre-capturas-del-1-y-2-de-noviembre]]).

## [FRICTION]
> [[2026-1101-twilio-addons-de-features-y-descuentos-no-publicados]] (escrita hace 3 días) afirma que *"El Traffic Optimization Engine empieza en **$300/mes**"* y que los descuentos de uso comprometido exigen un compromiso anual, citando una sección **Committed-use discounts** de la página.
> La captura del 2026-11-03 **no muestra ninguna de las dos cosas**: la tabla de Features solo lista Engagement Suite y Compliance Toolkit, y no hay sección de descuentos comprometidos.
> Ambas no pueden ser completamente correctas **si se interpreta la captura como el estado actual de la página**: o el producto y la sección desaparecieron de la página entre el 1 y el 3 de noviembre, o — más probable — la página se renderizó con menos contenido (texto plano, `word_count: 610` vs 2.212) y el material sigue ahí pero no se capturó. La segunda explicación es la que sostiene este átomo, y por eso la cifra de $300/mes **no se da por retirada**.
> Marcado para juicio humano, no auto-resuelto.
