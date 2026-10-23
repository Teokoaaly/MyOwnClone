---
id: 2026-1023-herosms-verificacion-por-llamada-y-bot-de-voz
type: atom
certainty: solid
sources: [sources/2026-10-22-hero-sms-home.md]
links: ["[[2026-1023-hero-sms-modelo-pay-per-use-y-tabla-real-vs-virtual]]", "[[2026-1023-5sim-una-entrada-de-verificacion-por-llamada]]", "[[2026-1022-auth-magic-link-codigo-seis-digitos]]"]
---

## Claim
HeroSMS declara soportar **más que SMS**. En el FAQ, bajo "What is a temporary number?": "Usually such virtual numbers only accept SMS for registration, but **the HeroSMS service also supports verification by call and voice bot**". La página no expone ninguna entrada de catálogo, precio ni stock para un canal de voz: el catálogo visible sigue siendo exclusivamente de SMS (45 servicios enlazados, de los que solo las 5 tarjetas del selector muestran precio y stock). El "voice bot" es, por definición del término, un bot que llama —es decir, un canal distinto del flash call en el que el titular de la línea confirma.

## Why It Matters
Marca una diferencia de producto frente a 5sim, donde la verificación por llamada existe como **una entrada de catálogo concreta** (`Virtual Number for Dropped-Call & Flash Call Verification`, ver [[2026-1023-5sim-una-entrada-de-verificacion-por-llamada]]), y donde la página además declara que el servicio "does not support sending outgoing SMS and calls". En HeroSMS la voz es una **capacidad transversal del servicio**, sin entrada de catálogo que la localice: es un claim de FAQ sin ninguna evidencia de precio, stock o configuración visible.
Para el vault esto importa porque el canal de voz no es un detalle: si una plataforma de verificación exige callback en lugar de SMS, la cobertura pasa a depender de un número que además no se puede auditar desde la página. Y es el mismo punto ciego que ya tiene el producto propio, que autentica por magic link con código de 6 dígitos por email y no tiene ningún canal telefónico ([[2026-1022-auth-magic-link-codigo-seis-digitos]]). El canal de voz, de ser real, se negaría al modelo prepago y pago por uso que el proveedor documenta ([[2026-1023-hero-sms-modelo-pay-per-use-y-tabla-real-vs-virtual]]).

## Nota de verificación
La cita es literal de la captura del 2026-10-22. Lo **no** observable: si la función está activa, en qué servicios, con qué coste adicional y con qué tasa de entrega. La captura no contiene ninguna mención a voz en el catálogo ni en la tabla de stock.
