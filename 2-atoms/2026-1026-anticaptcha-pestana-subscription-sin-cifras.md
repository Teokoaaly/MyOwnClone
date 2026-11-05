---
id: 2026-1026-anticaptcha-pestana-subscription-sin-cifras
type: atom
certainty: tentative
sources: [sources/2026-10-25-anti-captcha-pricing.md]
links: ["[[2026-1024-2captcha-solo-se-paga-por-captcha-resuelto]]", "[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1026-anticaptcha-trece-tipos-con-precio-por-1000]]"]
---

## Claim
El bloque de precios de AntiCaptcha tiene **dos pestañas**: "**Pay as you go**" y "**Subscription**", y solo la primera está renderizada en la captura. Es decir, el proveedor **ofrece un modo suscripción** cuyo precio,_plan, volumen incluido y condiciones no son públicos en la página capturada; la tabla visible es la de pay-as-you-go.

## Why It Matters
Es la primera evidencia de que en esta categoría hay **dos modelos de precio coexistiendo en el mismo proveedor**, y no solo entre proveedores. 2Captcha publica únicamente "price per 1000" y su modelo declarado es "**Pay only for solved captchas**" / "The server load does not affect the price" ([[2026-1024-2captcha-solo-se-paga-por-captcha-resuelto]]), sin suscripción.
Para el vault esto tiene una consecuencia práctica sobre la lectura de la tabla de coste por insumo de la §7 del thread: la fila "Captcha estándar" es **una fila de pay-as-you-go**, no el coste total de un cliente de AntiCaptcha. Un pipeline de volumen con suscripción pagaría un fijo por un techo de captchas, lo que cambia la aritmética por unidad en el sentido contrario al "coste marginal de céntimos" que el thread deriva ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]).
Y abre una pregunta de criterio que el vault no puede cerrar: **la unidad "por 1000" es una unidad de pay-as-you-go**, y si el proveedor tiene también un modo suscripción, entonces "el captcha es la partida más barata y la más fácil de cotizar" ([[2026-1024-2captcha-solo-se-paga-por-captcha-resuelto]]) depende del régimen de compra, no del producto.
Nota: la captura **no** publica ninguna cifra de la pestaña "Subscription": ni precio, ni captchas incluidas, ni periodo, ni si el ahorro es por volumen o por anticipo.
