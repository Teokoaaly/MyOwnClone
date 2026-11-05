---
id: 2026-1026-anticaptcha-descuento-automatico-por-volumen-diario
type: atom
certainty: solid
sources: [sources/2026-10-25-anti-captcha-pricing.md]
links: ["[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1026-anticaptcha-trece-tipos-con-precio-por-1000]]", "[[2026-1024-iproyal-cinco-lineas-y-cinco-unidades-de-precio]]"]
---

## Claim
Los precios de AntiCaptcha se presentan como **rangos** con dos notas al pie: "\*We provide **automatic discounts based on your daily captcha volumes**" (afecta a Images $0.5 - $0.7\*, reCAPTCHA v2 $0.95 - $2\*) y "\*\*Cost depends on the **V3 quality score**" (reCAPTCHA v3 $1 - $2\*\*). La home lo confirma: "Starting from 0.5USD per 1000 images, **depending on your daily spending volume**".

## Why It Matters
Es la **primera evidencia del corpus de un mecanismo de precio por volumen en el solver de captchas**, y tiene una consecuencia aritmética que el thread necesita: el precio **publicado no es el precio unitario real**, es una **banda** [nivel alto, nivel bajo] en la que se mueve según el volumen diario. La cifra correcta para un pipeline es **el extremo bajo de la banda**, que solo se alcanza con volumen — es decir, el descuento es una barrera de entrada, no un ahorro.
Es un mecanismo ausente en el otro proveedor del corpus, cuyo catálogo enumera ocho tipos con bandas de precio ya publicadas ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]). Y es comparable al de IPRoyal, donde cada línea de producto cambia de unidad y de palanca de precio ([[2026-1024-iproyal-cinco-lineas-y-cinco-unidades-de-precio]]).
Y hay un segundo mecanismo, más raro: **el precio de reCAPTCHA v3 depende de la "quality score"**, es decir, el proveedor **cobra por calidad de resolución, no solo por resolución**. Eso es una forma de pricing por SLA de calidad embebida en el unit price, y es un patrón que el vault no tenía catalogado en commodities (el resto del corpus cobra por unidades, por GB, por proxies o por requests).
El contraste con el otro proveedor se cierra así: en 2Captcha el "server load does not affect the price" era una promesa explícita de precio estable; en AntiCaptcha el precio **sí se mueve** con el volumen. Es decir, "el captcha es commodity con precio estable" es una propiedad de un proveedor, no del sector.
Nota: la captura **no** publica los tramos de volumen que activan cada descuento, ni el umbral diario, ni cómo se calcula el "quality score" de V3 ni qué penalización tiene un score bajo.


## Nota de extensión 2026-10-27
Este átomo identifica el **descuento automático por volumen diario** como "la **primera evidencia del corpus de un mecanismo de precio por volumen en el solver de captchas**" y afirma que es "un mecanismo **ausente** en el otro proveedor del corpus" (2Captcha). El Scraper API de 2Captcha confirma esa ausencia **en la línea de scraping también**: sus cinco planes (1.000 / 10.000 / 100.000 / 1.000.000 / 10.000.000 de requests) tienen **exactamente el mismo precio unitario de $0.3 por 1.000 requests**, sin ninguna columna de descuento ni banda de volumen ([[2026-1027-2captcha-scraper-api-030-por-mil-de-requests-en-los-cinco-planes]]).

**El valor de esta extensión está en la generalización y en el contrapunto.** Por un lado, el "no hay descuento por volumen en 2Captcha" deja de ser un rasgo del solver de captchas y pasa a ser un rasgo del **proveedor**, que lo mantiene en las dos líneas de producto que el vault ha capturado. Por otro lado, el caso de 2Captcha aporta un **tercer patrón de escalamiento de volumen** al corpus, y este es el más simple de los tres: **no es un descuento, es un pre-pago**. Los cinco planes son cinco denominaciones de venta del mismo producto al mismo precio, de modo que el "escalamiento" no cambia el precio unitario sino **el compromiso de capital y el número de compras de reposición**. Esto contrasta con las escaleras de los proveedores de proxy —DataImpulse por GB, IPRoyal con cinco unidades distintas ([[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]], [[2026-1024-iproyal-cinco-lineas-y-cinco-unidades-de-precio]])— donde el escalamiento **sí** cambia el precio unitario.

**Consecuencia para el modelo de coste del thread**: cuando el thread affine "el volumen baja el precio unitario", debe añadir el caso de que **el volumen puede no bajar nada** y lo único que hace es obligar a comprometer capital antes. Es un recordatorio de que un proveedor con precio unitario plano y sin suscripción es, para el vault, **la opción de coste variable más pura del corpus**, no la más barata.
