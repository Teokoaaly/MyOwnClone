---
id: 2026-1022-myclone-widget-comunicacion-websocket
type: atom
certainty: tentative
sources: [raw/articles/myownclone-technical-deep-dive-2026-06-23.md, raw/articles/myclone-deep-api-osint-2026-06-24.md]
links: ["[[2026-1022-myclone-widget-embed-modos]]", "[[2026-1022-myclone-api-rest]]", "[[myownclone]]", "[[2026-1022-myclone-chat-streaming-sse]]"]
---
## Claim
La comunicación widget↔backend de MyClone.is usa Socket.IO sobre WebSocket (`wss://app.myclone.is/socket.io/?EIO=4&transport=websocket`) con heartbeat de 25 segundos, reconexión automática con backoff exponencial y eventos `message`, `voice` (audio binario), `typing`, `presence` y `notification`. Hay un doble mecanismo de fallback: si el WebSocket falla, polling cada 5 segundos a `/api/v1/chats/:id/messages`; si falla el CDN, se sirve la versión alojada en el mismo dominio. El timeout inicial antes de mostrar error es de 3 segundos.

## Why It Matters
El streaming de audio binario por WebSocket (evento `voice`) es lo que hace posible una conversación hablada a baja latencia — el diferencial de voz que el informe de MyClone.is señala como su ventaja emocional fuerte frente a un chatbot de texto. Es también la parte más cara y difícil de replicar: [[myownclone]] no tiene widget embebido, así que no tiene esta capa. El patrón "websocket + fallback a polling" y el timeout de 3s son un patrón de robustez reutilizable; el fallback de CDN a mismo-dominio evita la dependencia dura de `app.myclone.is`. Nota: los tiempos y eventos están descritos en el informe a partir de análisis de bundles, no de una traza de tráfico real — de ahí `tentative`.

## Extensión (API OSINT 2026-06-24)
La API de OSINT añade el otro canal: el **streaming de texto va por SSE** (`POST /personas/username/{username}/stream-chat` con `Accept: text/event-stream`, eventos `type: content` / `type: complete`, patrón Vercel AI SDK), mientras que el audio en tiempo real usa **LiveKit** (`POST /livekit/connection-details` + `POST /livekit/session/{session_id}/heartbeat`). No hay ningún endpoint de socket en el OpenAPI, lo que apoya la hipótesis de dos canales (texto por SSE, voz por LiveKit/socket) y deja en el aire la afirmación de que el texto va por Socket.IO. Ver [[2026-1022-myclone-chat-streaming-sse]] y [[2026-1022-myclone-voice-providers-cartesia-elevenlabs]].
