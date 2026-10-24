---
id: 2026-1023-new-api-una-sola-api-multiproto
type: atom
certainty: solid
sources: [sources/2026-10-22-new-api-github.md, sources/2026-10-23-veridrop-relays.md]
links: ["[[2026-1023-new-api-gateway-unificado-de-modelos]]", "[[2026-1023-new-api-relaykit-conversion-perdida-de-campos]]", "[[2026-1022-myclone-api-superficie-227-endpoints]]"]
---

## Claim
El README tabula la **superficie de protocols y endpoints** que New API expone con una única API:

| Interfaz | Endpoints |
| --- | --- |
| OpenAI Chat / Responses | `POST /v1/chat/completions`, `POST /v1/responses` |
| Anthropic Messages | `POST /v1/messages` |
| Gemini | `POST /v1beta/models/{model}:generateContent`, `POST /v1beta/models/{model}:streamGenerateContent` |
| Realtime / Responses WebSocket | `GET /v1/realtime`, `GET /v1/responses` (upgrade a WebSocket) |
| Imágenes / audio | `/v1/images/generations`, `/v1/images/edits`, `/v1/audio/speech`, `/v1/audio/transcriptions`, `/v1/audio/translations` |
| Embeddings / rerank | `POST /v1/embeddings`, `POST /v1/rerank` |
| Plugins de tareas | `POST /v1/tasks/{pluginKey}`, `GET /v1/tasks/{taskId}` + rutas declaradas por cada plugin |

La columna de capacidades añade que se soportan **streaming, tools, reasoning y entradas multimodales** "where supported", y que la consola web incluye un **playground** para probar modelos.

## Why It Matters
Da la medida exacta de la **superficie de API unificada** que el vault no tenía: un solo prefijo `/v1` que habla cuatro protocolos de texto más imágenes, audio, embeddings, rerank y tareas.
El vault ya tiene una referencia de contraste: MyClone.is expone **227 endpoints** organizados por dominio de producto ([[2026-1022-myclone-api-superficie-227-endpoints]]). New API es la **concentración** — pocas rutas, pero cada una con una **matriz de proveedores detrás** — frente a la dispersión por dominio del competidor.
Los endpoints `POST /v1/embeddings` y `POST /v1/rerank` son especialmente relevantes para la decisión de proveedor de embeddings del vault, hoy partida entre Voyage (MyClone.is) y `text-embedding-3` inferido en [[myownclone]]: un gateway que los unifica bajo la misma clave y la misma factura es un sustituto plausible de esa decisión.

## [NOTA 2026-10-24 — VeriDrop]
Fuente: `sources/2026-10-23-veridrop-relays.md`. La superficie multi-protocolo del README **no es lo que el mercado compra**: en el directorio de VeriDrop, sobre 50 relays, solo **15 ofrecen Claude+Gemini+OpenAI a la vez**, **19 ofrecen dos protocolos** y **16 ofrecen uno solo** (10 solo-OpenAI, 5 solo-Claude, 1 solo-Gemini). OpenAI-compatible aparece en 42 de 50 filas, Claude en 39 y Gemini en solo 18 — el **36 %** ([[2026-1024-veridrop-cobertura-de-protocolos-por-relay]]). La lectura para el vault: la ruta `/v1` unificada de New API es una capacidad del software, no un estándar de despliegue; la mayoría de relays del mercado exponen un único dialecto, y la compatibilidad entre protocolos no se puede asumir al elegir `OPENAI_API_BASE` como proveedor de un clon que también quiere Claude o Gemini. Esto refuerza la tesis del átomo original en su versión operativa: la conversión multi-protocolo es lo que hace posible el negocio de reventa ([[2026-1023-new-api-gateway-unificado-de-modelos]]), y precisamente porque es difícil, el mercado se reparte en especialistas de un solo protocolo.
