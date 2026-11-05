---
id: 2026-1027-veridrop-json-schema-estricto-y-el-flag-markdown-json-seen
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1027-veridrop-una-desviacion-grave-baja-el-veredicto-a-amarillo]]", "[[2026-1027-veridrop-tres-senos-de-deteccion-protocolo-capacidad-y-uso]]", "[[2026-1026-new-api-fidelidad-de-conversion-orden-de-campos-y-esquema-json]]"]
---

## Claim
Cuando `response_format=json_schema` en modo **strict** no surte efecto —es decir, la respuesta viene envuelta en un bloque de código ```` ```json {...} ``` ```` en lugar de JSON puro—, la FAQ da **dos causas posibles y un flag que las separa**: **①** el relay **no ha pasado el parámetro `response_format`**, o **②** sí lo pasó pero el modelo de abajo (muy probablemente no un GPT) **no entiende el modo strict**. El mecanismo de discriminante es el flag **`markdown_json_seen`** ("Veridrop 通过 markdown_json_seen 标志区分这两种情况").

## Why It Matters
Es la **degradación de capacidad más silenciosa del sector**: el cliente pide JSON estructurado y recibe algo parseable a la fuerza, así que **la aplicación no falla, se degrada**. Un pipeline que espera JSON estricto y recibe markdown envuelto acaba con un `json.loads` que falla en runtime o, peor, con un extractor de regex que acepta basura: el fallo aparece **en el consumidor, no en el proveedor**, y a kilometres de distancia.
El valor del átomo está en el **flag como instrumento de diagnóstico diferencial**, y se apoya en la misma separación protocolo/capacidad/uso de [[2026-1027-veridrop-tres-senos-de-deteccion-protocolo-capacidad-y-uso]]: dos causas que producen el mismo síntoma visible (markdown) y que tienen remedies opuestos — **fallo de configuración del relay** frente a **sustitución de modelo** — se distinguen solo por un booleano que el detector guarda. Es exactamente el patrón que el vault necesita para su gateway: **un campo que registra qué se rompió**, no solo que algo se rompió. Y enlaza con la pérdida de campos en la conversión, que es el mecanismo físico de la causa ① ([[2026-1026-new-api-fidelidad-de-conversion-orden-de-campos-y-esquema-json]]).
Para el producto, la consecuencia es una regla de uso: **`response_format` en modo strict es una de las pruebas de capacidad más baratas que existen**, porque su fallo es visible en la primera respuesta y no requiere contexto largo ni estadística.

## Nota de verificación
Literal de la FAQ. La captura **no** publica en qué detector se contabiliza `markdown_json_seen`, ni si un JSON envuelto en markdown penaliza el veredicto global o solo ese detector.
