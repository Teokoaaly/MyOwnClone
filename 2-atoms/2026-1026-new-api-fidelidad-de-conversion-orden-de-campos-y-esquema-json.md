---
id: 2026-1026-new-api-fidelidad-de-conversion-orden-de-campos-y-esquema-json
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-relaykit-conversion-perdida-de-campos]]", "[[2026-1023-new-api-una-sola-api-multiproto]]", "[[2026-1026-new-api-plugins-de-tareas-sobre-moejs-y-conteo-de-tokens-mas-rapido]]"]
---

## Claim
Una serie de versiones cierran **pérdidas de campo en la conversión** que el vault ya había registrado como límite honesto del producto:

- **rc.47**: la **salida estructurada y los parámetros de tools ya no reordenan sus campos**; se envían **en el orden del cliente**. Chat a Gemini **ya no pierde `imageConfig`**, así que el tamaño y la ratio de la imagen se mantienen.
- **rc.44**: las tools y la salida estructurada enviadas a Gemini **conservan el JSON Schema completo** — `const`, `oneOf`, `$ref`, `$defs`, arrays de tipo y **enums no-string**; lo que el Schema tipado de Gemini no puede sostener va en `parametersJsonSchema` o `responseJsonSchema`. Los modelos en **Gemini API v1** reciben un schema limpio y una **advertencia de conversión**. Además, los **modelos Claude conocidos reciben el esfuerzo de pensamiento más cercano que aceptan** (y ninguno si no aceptan ninguno), lo que corrige los **400 en Opus 4.5 con `max` o `xhigh`**; **Claude Haiku 5.5** usa pensamiento adaptativo con esfuerzo medio, y **Gemini 2.5 Pro** recibe un presupuesto de pensamiento de **32768** para `xhigh` y `max`.
- **rc.45**: se arregla que los **mensajes de asistente fusionados perdieran las tool calls**, lo que hacía que Claude rechazara la petición.

## Why It Matters
El átomo de RelayKit ya decía lo esencial: *"protocol-specific tools and fields may not map exactly"*, y que la conversión es **commodity** ([[2026-1023-new-api-relaykit-conversion-perdida-de-campos]]). Este conjunto de fixes **convierte ese límite en una lista concreta y datada**, que es lo que hace falta para medir el coste real de la conversión.
Los dos casos con número son los que el vault puede cuantificar: **32768 tokens** de presupuesto de pensamiento para Gemini 2.5 Pro con `xhigh` es un **coste de inferencia directo** (32 k tokens de razonamiento por llamada a ese nivel), y el **400 en Opus 4.5 con `max`/`xhigh`** es el modo de fallo que hace que un cliente de código se caiga — no un detalle de formato.
Y hay un patrón de governance que el vault no tenía: **el schema no se degrada, se traslada**. Gemini no puede sostener un schema tipado completo, así que el gateway lo mete en `parametersJsonSchema` en lugar de recortarlo — la alternativa sería perder restricciones silenciosamente. Eso es **fail-safe**, y es el mismo criterio que ya se habían observado en el precio ([[2026-1026-new-api-reintento-de-tarea-reserva-el-sobrante-y-no-sale-si-no-alcanza]]).
Para el producto del vault, que expone una sola API multi-protocolo ([[2026-1023-new-api-una-sola-api-multiproto]]), esta lista es el **argumento honesto** de qué significa "compatible": no "idéntico", sino "conoce las diferencias y las nombra".
