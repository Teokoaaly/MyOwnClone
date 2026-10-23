---
id: 2026-1023-new-api-una-sola-api-multiproto
type: atom
certainty: solid
sources: [sources/2026-10-22-new-api-github.md]
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
