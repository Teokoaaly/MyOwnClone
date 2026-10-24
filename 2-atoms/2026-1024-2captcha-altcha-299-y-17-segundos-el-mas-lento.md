---
id: 2026-1024-2captcha-altcha-299-y-17-segundos-el-mas-lento
type: atom
certainty: solid
sources: [sources/2026-10-23-2captcha-solver.md]
links: ["[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar]]", "[[2026-1024-2captcha-capacidad-libre-por-minuto-como-proxy-de-cola]]"]
---
## Claim
**ALTCHA** es el único tipo con **precio único cerrado de $2.99 por 1000** y el de **velocidad más lenta de la tabla: 17 sec**. La captura añade el dato cualitativo que lo explica: "A key feature of this captcha is that it is designed as a slider, making it difficult for bots to bypass" — es un captcha de deslizador. Su "free capacity, per minute" es de **203**, la más baja del catálogo.

## Why It Matters
ALTCHA define el techo de coste **sin rango**: frente a reCAPTCHA v2 ($1 — $2.99, 2 sec) es más lento en 8,5 veces y no tiene banda de precio. Para un pipeline de scraping, 17 segundos por captcha es un límite de concurrencia, no un detalle: define cuántos workers hacen falta y, por tanto, cuál es la factura de capacidad.
La combinación **precio cerrado + slowest + menor capacidad libre** lo señala como el punto donde el mercado anti-bot se está endureciendo: los captchas de deslizador (slider) son la generación posterior a reCAPTCHA y aquí son los que cuestan más por unidad de tiempo. Es la señal temprana de que laIndustria del WAF se está moviendo hacia resistencias que el scraping directo no salva.
Nota: la captura **no** publica cuánto cuesta resolver un ALTCHA en horas punta ni si el precio $2.99 cubre Sites con slider más complejos.
