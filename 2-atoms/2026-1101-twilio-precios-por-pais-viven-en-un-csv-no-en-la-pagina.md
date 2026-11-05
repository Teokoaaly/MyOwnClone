---
id: 2026-1101-twilio-precios-por-pais-viven-en-un-csv-no-en-la-pagina
type: atom
certainty: solid
sources: [sources/2026-11-01-twilio-sms-pricing.md, sources/2026-11-03-twilio-sms-pricing.md]
links: ["[[2026-1101-twilio-sms-base-0-0083-por-segmento-de-160-caracteres]]", "[[2026-1031-twilio-sms-pricing]]", "[[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]"]
---

## Claim
La página de precios de Twilio no contiene una tabla de países: es una página **por país** (el selector fijo dice "United States", el enlace de salto apunta a `/en-us/sms/pricing/us`) y el tarifario internacional solo se descarga como **CSV** (`assets.cdn.prod.twilio.com/pricing-csv/SMSPricing.csv`, más `NumbersPricing.csv` para números). Todo lo capturado — SMS/MMS, RCS, cargos de operador, features y precios de números — es exclusivamente de **Estados Unidos**. La propia frase de la página lo confirma: *"Twilio helps by handling the carrier nuances in every country you send to"*, pero la página no las enumera.

## 2026-11-03 — re-verificación
La captura del **2026-11-03** mantiene el **selector de país "United States"** y el bloque "Jump to:" (SMS/MMS pricing, RCS pricing, Carrier fees, Features, Phone number pricing), es decir, la página sigue siendo **estructuralmente por país**. Novedad de esta captura: el texto del botón **"Download SMS prices (.CSV)" sí aparece**, pero **sin la URL del CSV**, que en las capturas del 1 y 2 sí era visible (`assets.cdn.prod.twilio.com/pricing-csv/SMSPricing.csv`, más `NumbersPricing.csv`); además desaparece la frase *"Twilio helps by handling the carrier nuances in every country you send to"*. Conclusión operativa: **la conclusión del átomo se mantiene, pero su evidencia se debilita** — la única prueba de la existencia del CSV en esta captura es el texto del botón, sin URL, y la frase que confirmaba la cobertura internacional ya no está. Para una afirmación sobre precios internacionales, la captura del 3 de noviembre **no basta**: hay que recurrir a la del 1 o 2 de noviembre o al CSV directamente.

## Why It Matters
Cualquier afirmación sobre "la tasa europea o latinoamericana" de Twilio **no es verificable con esta captura**: no hay cifras de España, México, Brasil, India ni Europa en la fuente, solo un selector de país y un CSV. Para la unidad económica del vault —verificación por SMS en flujos de creación de cuentas, donde el coste por asiento es marginal ([[2026-1031-twilio-sms-pricing]]) frente a un producto que verifica en LATAM ([[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]])— la consecuencia práctica es: **no se puede derivar de la web el coste de una verificación Twilio fuera de US sin descargar el CSV**, y la propia diferencia de precio por país es la variable que 5sim explota (el mismo producto cuesta 86 veces más en Italia que en Colombia). Cualquier tabla internacional en el vault tiene que venir del CSV o de una captura por país, no de esta URL genérica.
