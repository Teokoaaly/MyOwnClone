---
id: 2026-1101-twilio-numeros-telefonicos-1-15-y-2-15-al-mes
type: atom
certainty: solid
sources: [sources/2026-11-01-twilio-sms-pricing.md, sources/2026-11-03-twilio-sms-pricing.md]
links: ["[[2026-1101-twilio-cargos-de-operador-por-sms-y-costo-real-por-mensaje]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1031-twilio-sms-pricing]]"]
---

## Claim
Twilio cobra el número aparte del tráfico: long code **$1.15/mes** (alquilado por Twilio) o $0.50/mes si traes el tuyo; toll-free **$2.15/mes** o $0.50/mes propio; short code aleatorio **$1000** y vanity **$1500**, facturados trimestralmente y con una cuota de alta única de $500 para los short codes MMS. La página lo dice: *"Phone number charges are added to your message volume and carrier costs for your total price."*

## 2026-11-03 — re-verificación
La tabla de precios de números de la captura del **2026-11-03** es **idéntica en todas sus cifras**: long code $1.15 (alquilado) / $0.5 (propio), toll-free $2.15 / $0.5, short code aleatorio $1000 y vanity $1500 (ambos *billed quarterly, requires one time setup fee*), vanity propio $500, y la nota *"All MMS-enabled Short Codes have a $500 one-time fee charged at time of purchase"*. Nota de fidelidad: esta captura **omite la frase introductoria** *"Phone number charges are added to your message volume and carrier costs for your total price"* (y el enlace al CSV de números), de modo que la afirmación de "número + tráfico + recargo = precio total" queda anclada a la fuente del 1 de noviembre. El alquiler de $2.15/mes del toll-free sigue siendo el coste dominante del canal (ver [[2026-1103-twilio-tercera-renderizacion-texto-plano-sin-algunas-secciones]]).

## Why It Matters
Este es el coste que decide la pregunta "¿Twilio cabe en el presupuesto?" y casi siempre se pasa por alto: el **número toll-free se lleva $2.15 al mes**, es decir aproximadamente la mitad del presupuesto total de infraestructura de ≤ 4 EUR/mes del vault ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]) antes de enviar un solo mensaje. Sumando tráfico (≈$0.013 por SMS) el coste fijo mensual de un canal de verificación con toll-free es de ~$2.30/mes y el variable va aparte. Comparación de arquitectura: un long code alquilado ($1.15) más un número virtual de pago por uso de un proveedor como 5sim puede salir más barato en la unidad, pero introduce la fricción de números duplicados y bloqueos de operador ya documentada en [[2026-1031-twilio-sms-pricing]]. Para una herramienta de verificación de cuentas ([[2026-1101-twilio-cargos-de-operador-por-sms-y-costo-real-por-mensaje]]), el coste dominante es el número, no el mensaje.
