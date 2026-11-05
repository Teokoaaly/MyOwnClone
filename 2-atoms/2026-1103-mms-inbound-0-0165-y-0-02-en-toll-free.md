---
id: 2026-1103-mms-inbound-0-0165-y-0-02-en-toll-free
type: atom
certainty: solid
sources: [sources/2026-11-03-twilio-sms-pricing.md]
links: ["[[2026-1101-twilio-sms-base-0-0083-por-segmento-de-160-caracteres]]", "[[2026-1101-twilio-segmento-de-160-caracteres-y-regla-de-concatenacion]]", "[[2026-1101-twilio-cargos-de-operador-por-sms-y-costo-real-por-mensaje]]"]
---

## Claim
El MMS **entrante** se cobra a tarifa plana por mensaje y con un **diferencial según el tipo de número**: **$0.0165** en long codes y short codes, y **$0.02** en números toll-free. El FAQ lo enuncia literal: *"Inbound MMS costs $0.0165 per message for long codes and short codes, and $0.02 per message for toll-free numbers."* El outbound es **$0.022** en los tres tipos de número. Además, el MMS se factura como tarifa plana que admite **adjuntos de hasta 5 MB** y **hasta 1.600 caracteres de texto sin activar el cobro multi-segmento**, frente al segmentado de 160 caracteres del SMS.

## Why It Matters
Completa la tabla de precios de Twilio en el lado que el vault tenía sin atomizar: hasta ahora solo estaba registrado el outbound de MMS a $0.022 ([[2026-1101-twilio-sms-base-0-0083-por-segmento-de-160-caracteres]]). El único número toll-free es precisamente el de mayor coste en MMS entrante (+21 % frente a $0.0165), así que **el tipo de número elegido importa en ambos sentidos de tráfico** y no solo en el mensual del alquiler: un flujo que recibe respuestas MMS (por ejemplo, rich replies con imagen) encarece ~$0.0035 por mensaje entrante si el número es toll-free. Combinado con el cobro por segmento del SMS ([[2026-1101-twilio-segmento-de-160-caracteres-y-regla-de-concatenacion]]), el umbral de 1.600 caracteres hace del MMS la opción de menor coste *por byte de texto* a partir de cierto tamaño — aunque el cargo de operador se suma igual y hasta puede duplicar el coste real ([[2026-1101-twilio-cargos-de-operador-por-sms-y-costo-real-por-mensaje]]).
