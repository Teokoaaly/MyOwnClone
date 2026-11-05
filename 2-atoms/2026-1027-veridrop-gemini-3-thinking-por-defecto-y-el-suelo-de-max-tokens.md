---
id: 2026-1027-veridrop-gemini-3-thinking-por-defecto-y-el-suelo-de-max-tokens
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1027-veridrop-gemini-solo-se-detecta-por-la-ruta-openai-compatible]]", "[[2026-1027-veridrop-json-schema-estricto-y-el-flag-markdown-json-seen]]", "[[2026-1026-new-api-cache-12h-openai-2-5x-y-precios-gpt-6-astra]]"]
---

## Claim
Gemini 3 **abre thinking por defecto**, lo que obliga a un suelo en el límite de tokens de salida: **"至少 64,推荐 128+"**, porque **"Gemini 3 默认开 thinking,会消耗 30-60 reasoning_tokens 才输出 texto"** y **"如果 max 太小(< 32),thinking 占满后没空间出 texto,响应就是空字符串 + finish_reason=length"**. VeriDrop ajusta su detector a **64-384**. La FAQ explica además que las **claves nativas de Gemini no funcionan** con la ruta OpenAI-compatible: hay que usar **el endpoint oficial `/v1beta/openai`** con una **API key de Google AI Studio (`AIza...`)**, y además se topa el `model` con prefijo **`models/`** (`gemini-2.5-flash` vs `models/gemini-2.5-flash`).

## Why It Matters
Es un **fallo silencioso de configuración** con una firma muy reconocible — **respuesta vacía con `finish_reason=length`** — que un integrador suele atribuir a un relay roto o a un modelo agotado, cuando en realidad es **el presupuesto de salida agotado por el razonamiento**. La regla operativa (mínimo 64, recomendado 128+) es directamente copiable al producto: **es un parámetro que el cliente de un gateway debe tener en cuenta antes de quejarse del proveedor**.
Y el dato estructural es más importante que el número: **"thinking por defecto" significa que el mínimo de tokens de salida lo fija el proveedor, no el cliente**. Para cualquier capa que traduzca peticiones hacia Gemini —como la del vault ([[2026-1027-veridrop-gemini-solo-se-detecta-por-la-ruta-openai-compatible]])— esto tiene una consecuencia económica: **la reserva de tokens para razonamiento es un coste invisible en la facturación por token de salida**, porque el cliente pidió una respuesta de 50 tokens y el modelo consumió 60 de razonamiento antes. Es un **coste oculto del mismo tipo que la caché de 12 h del gateway** ([[2026-1026-new-api-cache-12h-openai-2-5x-y-precios-gpt-6-astra]]), y por eso pertenece al modelo de coste del producto.
Los tres fallos de configuración que la FAQ enumera (modelo sin prefijo `models/`, modelo no proxyado, `max` insuficiente) son un recordatorio útil: **en la ruta OpenAI-compatible, un error de nombre de modelo produce un `model_not_found` que el integrador tiende a leer como "el relay no tiene ese modelo"**, cuando puede ser solo el prefijo.

## Nota de verificación
Cifras y umbrales literales de la FAQ. La captura **no** publica si el ahorro de 30-60 reasoning_tokens varía por modelo o por dificultad de la tarea, ni qué hace el detector cuando la respuesta vuelve vacía.
