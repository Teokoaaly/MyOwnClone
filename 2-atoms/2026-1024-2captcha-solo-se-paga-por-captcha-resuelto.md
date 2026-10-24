---
id: 2026-1024-2captcha-solo-se-paga-por-captcha-resuelto
type: atom
certainty: solid
sources: [sources/2026-10-23-2captcha-solver.md]
links: ["[[2026-1024-2captcha-servicio-dual-cliente-paga-y-trabajador-cobra]]", "[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1023-hero-sms-modelo-pay-per-use-y-tabla-real-vs-virtual]]"]
---
## Claim
Las tres condiciones comerciales de la tabla de 2Captcha son: "**The server load does not affect the price**", "**Pay only for solved captchas**" y "**99.9% uptime**". El precio se factura por captcha resuelto, nunca por captcha enviado.

## Why It Matters
Es un **modelo de pago por uso con riesgo transferido al proveedor**, el mismo eje contractual que 5sim y HeroSMS fijan para sus servicios ([[2026-1023-hero-sms-modelo-pay-per-use-y-tabla-real-vs-virtual]]): el cliente solo paga por el resultado correcto. Para una empresa que automatiza scraping esto elimina la partida de "fallos" del coste: un fallo no cuesta, y por tanto el coste marginal de una operación fallida es cero.
Combinado con el precio por mil ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]), el coste por captcha resuelto de un reCAPTCHA v2 está en el rango **$0.001 — $0.00299**. Frente a un plan de $99/mes ([[2026-1022-precio-99-mensual]]) eso es un cuatro milésimas del ingreso de un mes: **el captcha no es un problema de economía de producto**, es un problema de ingeniería. Lo que sí es caro es el trabajo humano que lo sostiene ([[2026-1024-2captcha-servicio-dual-cliente-paga-y-trabajador-cobra]]).
Nota: la captura **no** publica qué pasa con los captchas que se resuelven mal, ni si hay reembolso o solo no cobro, ni los métodos de pago.
