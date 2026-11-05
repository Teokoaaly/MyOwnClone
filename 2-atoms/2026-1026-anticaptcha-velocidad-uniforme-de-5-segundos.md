---
id: 2026-1026-anticaptcha-velocidad-uniforme-de-5-segundos
type: atom
certainty: solid
sources: [sources/2026-10-25-anti-captcha-pricing.md]
links: ["[[2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar]]", "[[2026-1024-2captcha-arkose-funcaptcha-50-dolares-por-1000]]", "[[2026-1026-anticaptcha-altcha-a-2-dolares-y-5-segundos]]"]
---

## Claim
La columna "Solving Speed" del catálogo de AntiCaptcha da **5 s para los trece tipos**, sin excepción: Images, reCAPTCHA v2, reCAPTCHA v3, reCAPTCHA Enterprise v2/v3, GeeTest, Arkose Labs, Turnstile, Custom Tasks, Object Coordinates, Prosopo, Friendly Captcha, Amazon WAF y Altcha.

## Why It Matters
Convierte la latencia en una **constante del proveedor** en vez de una variable del tipo de captcha. En el catálogo de 2Captcha la columna va de 1 s a 17 s y el átomo del vault la usa para distinguir tipos "estándar" de tipos "lentos" y sacar de ahí la conclusión de que "solo los dos tipos caros son además los lentos" ([[2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar]]). AntiCaptcha no tiene esa estructura: **no existe un tipo lento**, y los dos que en 2Captcha lo eran —Arkose 16 sec y ALTCHA 17 sec— aquí resuelven en 5 s ([[2026-1026-anticaptcha-altcha-a-2-dolares-y-5-segundos]], [[2026-1026-anticaptcha-arkose-labs-a-3-dolares-por-1000]]).
Para el vault esto tiene una consecuencia de diseño: al elegir proveedor, la latencia se cotiza como **una constante por proveedor** (1-2 s en 2Captcha, 5 s en AntiCaptcha) y el tipo de captcha solo cambia el precio. Es un argumento a favor de tratar el solver como **commodity con SLA** —como ya hace el thread con la tabla de coste por insumo ([[2026-1024-2captcha-solo-se-paga-por-captcha-resuelto]])— y en contra de pagar el sobrecoste del tipo difícil "porque el tipo difícil es más lento", que es la inferencia que el corpus podría hacer de un solo proveedor.
Nota: la captura **no** publica percentiles, ni tiempo de espera en cola, ni si los 5 s son media o mediana.
