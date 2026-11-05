---
id: 2026-1101-twilio-sms-base-0-0083-por-segmento-de-160-caracteres
type: atom
certainty: solid
sources: [sources/2026-11-01-twilio-sms-pricing.md, sources/2026-11-03-twilio-sms-pricing.md]
links: ["[[2026-1031-twilio-sms-pricing]]", "[[2026-1022-costes-por-categoria-tenant]]", "[[2026-1101-twilio-cargos-de-operador-por-sms-y-costo-real-por-mensaje]]"]
---

## Claim
En Estados Unidos la tarifa base de Twilio es **$0.0083 por segmento de 160 caracteres**, idéntica para SMS saliente y entrante y para los tres tipos de número (long code, toll-free y short code), tal y como enuncia el FAQ: *"The base rate to send or receive standard outbound or inbound SMS segments in the US is $0.0083 per 160-character segment across long codes, toll-free numbers, and short codes."* MMS saliente se cobra a **$0.022 por mensaje** (plano, no por segmento).

## 2026-11-03 — re-verificación
La captura del **2026-11-03** (texto plano, `word_count: 610`) **confirma sin variación** la tabla completa: SMS outbound e inbound $0.0083 para long codes, toll-free y short codes; MMS outbound $0.022 en los tres; MMS inbound $0.0165 en long code y short code, **$0.02 en toll-free**. La etiqueta de vigencia es *"SMS and RCS pricing current as of October 2026"*. Nuance de esta captura: la tabla sigue intacta pero **el FAQ que enunciaba literalmente "$0.0083 per 160-character segment across long codes, toll-free numbers, and short codes" ya no está** (la variante de texto plano lo omite), así que a partir de ahora la confirmación de la tarifa base depende de la tabla y no de la cita textual — la afirmación sigue en pie, la cita literal queda anclada a la fuente del 1 de noviembre. El MMS entrante ($0.0165 / $0.02 toll-free) queda atomizado aparte en [[2026-1103-mms-inbound-0-0165-y-0-02-en-toll-free]].

## Why It Matters
Es el suelo del coste variable de una verificación por SMS en US: $0.0083 es el precio por segmento antes de cualquier cargo de operador ([[2026-1101-twilio-cargos-de-operador-por-sms-y-costo-real-por-mensaje]]). Sobre el plan más barato de $99/mes ([[2026-1022-precio-99-mensual]]) una verificación de un solo segmento consume el **0.0084 %** del ingreso mensual; 1.000 verificaciones mensuales ≈ $12.80–$13.30, es decir un 12–13 % de un plan de $99. Traducido al eje del vault: el coste por asiento ([[2026-1022-costes-por-categoria-tenant]]) domina con dos órdenes de magnitud, y el SMS es una categoría marginal — pero solo si se cobra por segmento de 160, no por mensaje suelto.

## [FRICTION]
> [[2026-1031-twilio-sms-pricing]] afirma que el precio es *"approximately $0.0075/message"*.
> Esta nota presiona esa cifra porque la página de precios enuncia explícitamente **$0.0083 por segmento de 160 caracteres**, y además ese $0.0075 "por mensaje" mezcla dos conceptos: el precio base es **por segmento**, y el coste real **por mensaje** incluye el cargo de operador que se suma encima (hasta $0.005 en Verizon), dejando un total de $0.0108–$0.0133 por SMS saliente de un segmento.
> Ambas no pueden ser completamente correctas: o el átomo viejo usa una cifra de otra tarifa/época, o la nueva captura muestra un precio que cambió. Marcado para juicio humano, no auto-resuelto.
