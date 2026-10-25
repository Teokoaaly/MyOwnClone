---
id: 2026-1024-gptgrok2api-compatibilidad-multiprotocolo-y-despacho-por-modelo
type: atom
certainty: solid
sources: [sources/2026-10-24-gptgrok2api.md]
links: ["[[2026-1024-gptgrok2api-gateway-unificado-gpt-y-grok-en-api-compatible]]", "[[2026-1023-new-api-una-sola-api-multiproto]]", "[[2026-1023-new-api-routing-por-grupo-prioridad-y-afinidad]]"]
---

## Claim
La tabla de "entradas de API" del README publica **siete endpoints** con su ruta literal: `GET /v1/models`, `POST /v1/chat/completions`, `POST /v1/responses`, `POST /v1/messages` (compatibilidad con Anthropic Messages), `POST /v1/images/generations`, `POST /v1/images/edits` y `POST /grok/v1/videos`; la consola de administración cuelga de `/`. La compatibilidad declarada no es solo de rutas sino de **semántica**: streaming y no-streaming, llamadas a herramientas, búsqueda y nivel de razonamiento. El despacho es **por modelo**: la raíz `/v1` enruta automáticamente GPT, Grok SSO y Grok Build OAuth en un único catálogo, mientras `/grok/v1` conserva la interfaz Grok completa. La autenticación es un **token Bearer único** (`CHATGPT2API_AUTH_KEY`) para consola y API a la vez.

## Why It Matters
Es exactamente la **superficie que el vault necesita para hablar con un proveedor (y con un gateway) sin cambiar código por proveedor**: si un cliente habla Anthropic Messages, `/v1/messages` lo acepta; si habla Responses API, `/v1/responses`. El vault ya tiene una pieza equivalente documentada en new-api, que normaliza los cuatro protocolos de texto ([[2026-1023-new-api-una-sola-api-multiproto]]); la diferencia es que aquí el **enrutamiento es por modelo dentro de un mismo catálogo**, no por grupo de prioridad o afinidad como en new-api ([[2026-1023-new-api-routing-por-grupo-prioridad-y-afinidad]]).
Para MyOwnClone la consecuencia es de **coste de integración**: añadir este gateway como proveedor de respaldo no exige un adaptador nuevo, solo otra entrada de `OPENAI_API_BASE`. Y la existencia de `/v1/messages` significa que **una misma credencial** puede servir tanto al cliente OpenAI-compatible como al cliente Anthropic-compatible, lo que reduce el número de claves que hay que custodiar.
Un apunte de diseño que conviene retener: la documentación de API del vault ya no tiene que ser específica del proveedor, porque el formato se vuelve **una decisión del wrapper y no del modelo**.

## Nota de verificación
Rutas transcritas literalmente de la tabla del README. La captura **no** publica: los cuerpos de request/response, los códigos de error, los límites de tasa, ni los nombres reales del catálogo de modelos más allá del ejemplo `gpt-5` y del parámetro `gpt-image-2` del ejemplo de edición de imagen.
