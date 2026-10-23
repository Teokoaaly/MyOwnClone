---
id: 2026-1023-priceai-limite-de-verificacion-y-responsabilidad
type: atom
certainty: solid
sources: [sources/2026-10-22-priceai-home.md]
links: ["[[2026-1023-priceai-home-como-radar-y-no-como-vendedor]]", "[[2026-1023-priceai-descargo-de-responsabilidad-sin-sla]]", "[[2026-1023-lzt-superficie-de-avisos-faq-y-tickets]]"]
---

## Claim
PriceAI declara un **límite de verificación explícito** y una cadena de responsabilidad: *"PriceAI 提供信息，不替任何渠道背书"* — da información, no respalda ningún canal. Lo que se conserva es lo **revisable**: nombre original del canal, título del producto y enlace de compra, más el estado 有货/缺货 y la hora de última actualización. Regla explícita: *"长期未更新的低价不应直接当成可买价"* — un precio bajo no actualizado desde hace tiempo no debe tomarse como precio comprable. Y sobre quién responde: *"PriceAI 不参与交易。付款、交付、售后、退款和账号风险都按原平台规则判断"* — pago, entrega, postventa, reembolso y riesgo de cuenta se juzgan según las reglas de la plataforma original.

## Why It Matters
Es el marco de **epistemicidad con fecha**: PriceAI no transfiere la confianza, solo la redirige al canal original y obliga a volver allí para comprar. Es exactamente el patrón de auditoría que el vault ya-marco en la capa de costes (volver al proveedor, no al agregador), pero aquí el propio agregador lo escribe: lo único que sobrevive a la agregación es el par (enlace original, timestamp).
La regla del precio obsoleto es la más accionable: convierte el **precio más bajo visible** en un dato suspecto por defecto si no se ha refrescado, lo que pone una cota de confianza sobre cualquier cifra tomada de esta fuente sin fecha de captura — problema que el vault ya había detectado en la fecha de cambio congelada del catálogo ([[2026-1023-priceai-catalogo-ocho-canales-y-fecha-de-tipo-de-cambio]]).
Sobre la responsabilidad: mientras el payload transaccional vive en el canal original, la única superficie de disputa del vault es la de tickets, que en el caso de un marketplace es una **mediación de transacción**, no soporte de software ([[2026-1023-lzt-superficie-de-avisos-faq-y-tickets]]). Y el aviso de no-SLA de la página de API ([[2026-1023-priceai-descargo-de-responsabilidad-sin-sla]]) confirma que la ausencia de respaldo no es solo retórica de la home.

## [FRICTION]
> [[2026-1023-priceai-patrocinadores-y-canales-de-reventa-con-multiplicador]] afirma que la tabla y el pie de PriceAI **no están separados por una frontera** — los patrocinadores son revendedores de la misma materia que la tabla agrega — y concluye que "una página comparativa de precios vive del sponsors de revendedores: su incentive no es la neutralidad del comparativo sino el tráfico de compra", marking as "declaración comercial o del agregador" todo lo que aparece en esa página.
> Este átomo presiona esa creencia en un punto concreto: la home **sí** declara una frontera, textual y verificable — *"PriceAI 提供信息，不替任何渠道背书"* y "PriceAI 不参与交易" — y además separa la capa de datos (los módulos, con渠道, precio, stock y fecha) de la capa comercial (el bloque de patrocinadores, con etiqueta explícita 赞助/推广 y enlace de afiliado con `aff=`/`invite_code=`). La frontera no es de neutralidad editorial, pero sí es de **etiquetado y de aislamiento físico del bloque pagador**.
> Ambas no pueden ser completamente correctas: o el sponsored placement sesga el orden, la selección o la prominencia de los canales dentro de los módulos (y entonces "no endorsement" es retórica), o la separación por bloque y por etiqueta protege de verdad la comparativa (y entonces el problema es solo de funding, no de fiabilidad). Marcado para juicio humano, no auto-resuelto: el vault no ha observado ninguno de los dos módulos de comparación de esta fuente, solo la home.
