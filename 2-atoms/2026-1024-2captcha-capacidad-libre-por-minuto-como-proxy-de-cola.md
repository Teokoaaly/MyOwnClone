---
id: 2026-1024-2captcha-capacidad-libre-por-minuto-como-proxy-de-cola
type: atom
certainty: solid
sources: [sources/2026-10-23-2captcha-solver.md]
links: ["[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1024-2captcha-altcha-299-y-17-segundos-el-mas-lento]]", "[[2026-1024-2captcha-flujo-api-en-cinco-pasos-con-captcha-id]]"]
---
## Claim
La tabla publica una quinta columna, **"Free capacity, per minute"**, que es el dato más accionable del catálogo: Image Captcha **12,000**, reCAPTCHA v2 **11,273**, Amazon captcha **5,632**, Cloudflare Turnstile **2,883**, reCAPTCHA v3 **757**, Arkose/FunCaptcha **578**, reCAPTCHA Enterprise **483**, ALTCHA **203** captchas libres por minuto.

## Why It Matters
Este número es el **proxy de la profundidad del pool de trabajadores** por tipo, y ordena el catálogo de forma distinta al precio: los tipos más baratos (Image $0.5, reCAPTCHA v2 $1) tienen capacidades de 5 cifras, mientras que ALTCHA baja a **203 por minuto** — unos 59 veces menos que Image Captcha. O sea: **el tipo de captcha que además es el más caro por mil es el que además tiene menos capacidad ([[2026-1024-2captcha-altcha-299-y-17-segundos-el-mas-lento]])**, lo que señala un nicho con pocos trabajadores especializados, no un tipo poco demandado.
Con estos números se puede dimensionar un pipeline sin hacer aritmética de suposición: 203/min significa que resolver 10.000 ALTCHA al día es imposible con este proveedor y exige cola, escalado de proveedor o aceptar el error.
Nota: la captura **no** define "free capacity" (¿capacidad o cola mínima garantizada?, ¿por minuto o por media hora?), ni publica qué pasa al saturarse.
