---
id: 2026-1026-anticaptcha-100-por-ciento-de-trabajadores-humanos
type: atom
certainty: solid
sources: [sources/2026-10-25-anti-captcha-pricing.md]
links: ["[[2026-1024-2captcha-ai-primero-con-fallback-a-trabajadores-humanos]]", "[[2026-1024-2captcha-servicio-dual-cliente-paga-y-trabajador-cobra]]", "[[2026-1026-anticaptcha-velocidad-uniforme-de-5-segundos]]"]
---

## Claim
AntiCaptcha declara que "**100% of captchas are solved by human workers from around the world**" y que "An average worker earns about **$100 per month**, which is considered a good salary in developing countries such as **Bangladesh, Pakistan, and Venezuela** among others". Es una **cifra de salario del trabajador**, no de precio al cliente, y es la primera del corpus que cuantifica la retribución del lado de la oferta.

## Why It Matters
Cierra el círculo económico que el vault tenía abierto en el átomo de 2Captcha: allí se afirmaba que "el precio del captcha es el precio de **mano de obra**, no de cómputo" y que "no se publica la tarifa por captcha resuelto al trabajador" ([[2026-1024-2captcha-servicio-dual-cliente-paga-y-trabajador-cobra]]). AntiCaptcha da la cifra del otro lado de la misma operación: **$100 al mes por trabajador**.
Eso permite una comprobación de orden de magnitud, no una medición: si 1000 trabajadores Koeplan pagan $100/mes, el coste laboral mensual es ~$100.000 y el del catálogo (a $0.5–$5 por mil) implica del orden de millones de captchas al mes para cubrirlo. Es coherente con un pool humano grande, pero **la captura no publica el número de trabajadores ni el volumen resuelto**, así que la cifra no es auditable: sirve para entender la naturaleza del coste, no para cotizarlo. La diferencia con 2Captcha es de arquitectura declarada: allí la resolución es "AI-first" con fallback humano ([[2026-1024-2captcha-ai-primero-con-fallback-a-trabajadores-humanos]]).
También explica por qué el catálogo es de precio tan plano: si **todo** el trabajo es humano, no hay una rama "modelo primero, humano de reserva" que explique dispersiones de precio o de latencia por tipo ([[2026-1026-anticaptcha-velocidad-uniforme-de-5-segundos]]).
Nota: la captura **no** publica el número de trabajadores, su tasa de(error), el volumen mensual resuelto ni si "average worker" es una media observada o una cifra de marketing.
