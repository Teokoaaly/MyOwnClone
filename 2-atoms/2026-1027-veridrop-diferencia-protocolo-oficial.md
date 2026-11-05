---
id: 2026-1027-veridrop-diferencia-protocolo-oficial
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1027-veridrop-que-es-relay]]", "[[2026-1027-veridrop-por-que-relay]]"]
---

## Claim

La diferencia fundamental entre el **API oficial** y un **中转站** radica en la consistencia de campos, firmas y formato de respuesta: el API oficial tiene campos de firma, estructura de error y formato de `usage` definidos y predecibles; en cambio, los relay entre sí tienen diferencias gigantescas — algunos hacen un 1:1 pas-through, otros reescriben campos `usage`, otros suprimen bloques `thinking`, reemplazan modelos o inyectan system prompt adicionales. Veridrop detecta precisamente estas diferencias «en el medio» para identificar qué relay ha alterado la respuesta original.

## Why It Matters

Para el vault, esta diferencia es crítica porque determina la fiabilidad de los downstream business processes: si un modelo de Claude es reemplazado silenciosamente por Haiku en el relay, los estilos de escritura, los patrones de razonamiento y los hábitos de resolución de problemas cambian sin aviso, lo que puede hacer que outputs orientados a trabajo serio fallen estrepitosamente. El mismo argumento que el gateway del vault (que ya eligió AGPLv3 con atribución en la interfaz) usa para diferenciar entre dos herramientas que ambas prometen no subir la key.

## Nota de verificación

La distinción entre protocolo oficial y relay es literal de la sección «中转站和官方 API 有什么区别?» de la FAQ. La captura no cataloga ejemplos específicos de field rewriting por relay, que Veridrop explora mediante sus 7-10 items de detección.