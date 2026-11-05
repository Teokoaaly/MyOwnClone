---
id: 2026-1026-suno2openai-el-contrato-publico-es-el-formato-de-chat-con-streaming
type: atom
certainty: solid
sources: [sources/2026-10-25-suno2openai.md]
links: ["[[2026-1024-gptgrok2api-gateway-unificado-gpt-y-grok-en-api-compatible]]", "[[2026-1023-new-api-gateway-unificado-de-modelos]]"]
---

## Claim
El *Project Highlights* del README define la superficie pública en cuatro líneas, y la primera es la que manda: **"OpenAI Format Calls: Supports streaming output"**, seguida de **"Front-end Compatibility: Compatible with front-end projects like `chat-next-web`"**. El contrato documentado es, por tanto, **el endpoint de chat de OpenAI con streaming**, y el consumidor declarado es **un front-end de chat**, no un cliente de API de música. El README **no publica un endpoint de tareas, ni de progreso, ni de descarga de audio**: solo `POST /v1/chat/completions` con `model`, `messages` y `stream`.

## Why It Matters
El vault ha medido dos veces el mismo movimiento —**envolver capacidad de proveedor en el esquema OpenAI para que un cliente existente no tenga que cambiar**— en `gptGrok2api` (raíz `/v1` que despacha por modelo y conserva `/grok/v1` completo) ([[2026-1024-gptgrok2api-gateway-unificado-gpt-y-grok-en-api-compatible]]) y en `new-api` (gateway unificado que los relays exponen con `OPENAI_API_BASE` + `OPENAI_API_KEY`) ([[2026-1023-new-api-gateway-unificado-de-modelos]]). Aquí la tercera variante tiene un matiz que solo se ve al leer el README entero: **el streaming está declarado como característica principal y el formato es de chat**, no de completions de texto genérico. Es decir, **la música se entrega por el canal de una respuesta de chat**, y el usuario la consume a través de `chat-next-web`.
La consecuencia de arquitectura para el producto propio es de **canal de entrega**, no de API: un gateway de música compatible con OpenAI **no necesita que sus clientes aprendan un SDK**, pero sí necesita **decidir por su cuenta cómo se transporta el audio** (enlace en la respuesta, descarga aparte, o tarea encolada), porque el README no publica ninguno de esos mecanismos. El único indicio es que el modelo declara `MAX_TIME = 5` minutos y el plan futuro menciona **"request queueing optimizations"**, lo que sugiere que **el trabajo asíncrono todavía no está resuelto** y que el streaming es la estrategia provisional.
Para el agregador de precios esto también importa: **una capacidad que se entrega por un endpoint de chat con streaming no encaja en el modelo de "coste por token ni por request"** que el vault midió en New API; la tarifa tiene que inventarse para este canal.
