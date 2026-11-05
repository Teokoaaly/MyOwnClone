---
id: 2026-1026-suno2openai-el-campo-model-es-gpt-3-5-turbo-sobre-un-backend-de-musica
type: atom
certainty: solid
sources: [sources/2026-10-25-suno2openai.md]
links: ["[[2026-1023-new-api-precios-por-ratio-y-expresion]]", "[[2026-1023-new-api-routing-por-grupo-prioridad-y-afinidad]]"]
---

## Claim
El único ejemplo de generación que da el README es un `POST /v1/chat/completions` con `"model": "gpt-3.5-turbo"` y `messages` de sistema y usuario (*"Tell me a joke."*), con `"stream": true` como opción comentada. El `model` enviado **no identifica la capacidad real** —el backend es `https://studio-api.suno.ai`—: es una etiqueta de compatibilidad para que un cliente OpenAI no falle al validar el cuerpo. El README **no publica ningún catálogo de modelos**, ni cómo se mapea `model` a un modelo o modo de Suno, ni qué ocurre si el `model` no es `gpt-3.5-turbo`.

## Why It Matters
El vault ha medido que el precio de un canal se define **por modelo** (ratio) y por nivel de uso (expresión), y que el routing se decide por **mapeos de modelo, prioridad, peso y afinidad** ([[2026-1023-new-api-precios-por-ratio-y-expresion]], [[2026-1023-new-api-routing-por-grupo-prioridad-y-afinidad]]). Este gateway **rompe el supuesto de que el campo `model` describe la capacidad**: un canal de relay que lo exponga publicará `gpt-3.5-turbo` en su catálogo y cobrará por ratio de OpenAI mientras entrega **música generada por Suno**.
Eso tiene tres consecuencias operativas que el vault debe tener presentes al construir un agregador: (1) **el nombre del modelo es la clave de la facturación y aquí es opaco**; (2) **una misma etiqueta puede cubrir modos de coste muy distintos** (canción completa, continuación, estilo, tags), porque el README dice que los parámetros propios —*tags, prompt, style, song continuation*— aún **no están soportados** y están listados como planes futuros; (3) el único indicador de consumo observable es el **formato de respuesta OpenAI**, no una unidad de uso de música.
En otras palabras: **el precio por modelo presupone un modelo; aquí hay una etiqueta**. Es exactamente el hueco de measurement que el vault ya vio en el lado de los canales de relay, donde "disponible" y "sirve el modelo que dice" son cosas distintas.

## [FRICTION]
> [[2026-1023-new-api-precios-por-ratio-y-expresion]] (escrita el 2026-10-23) establece que el precio interno de un canal se define **"por modelo (ratio) y por nivel de uso (expresión)"**, con precios built-in por tipo de caché y precios por número de peticiones, y lo usa como **el mecanismo interno que produce el multiplicador que PriceAI tabula**.
> Este átomo presiona ese mecanismo desde el lado del upstream: **este gateway no tiene modelo que tarificar**. Publica `gpt-3.5-turbo` como etiqueta de compatibilidad y no documenta ni el mapeo a modos de Suno ni unidades de uso; su única granularidad real será, cuando se implemente, la lista de planes futuros (tags, prompt, style, continuation), que **no son precios sino parámetros**. Un canal de relay que lo integre tiene que **inventar su propio eje de precio** (por canción, por request, por minuto de audio) porque el upstream no le da ninguno.
> Ambas no pueden ser la misma regla: o todo upstream expone un modelo tarifable y este es una excepción documentada, o el precio-por-modelo de New API es una convención de gateways **de modelos reales** y no aplicable a gateways de capacidad musical. Marcado para juicio humano, no auto-resuelto: el vault no ha ejecutado el gateway ni observado qué `model` acepta realmente ni qué devuelve la respuesta.
