---
id: 2026-1022-myclone-chat-streaming-sse
type: atom
certainty: solid
sources: [raw/articles/myclone-deep-api-osint-2026-06-24.md, raw/articles/myownclone-osint-implementation-plan-2026-06-24.md]
links: ["[[2026-1022-myclone-widget-comunicacion-websocket]]", "[[2026-1022-myclone-api-superficie-227-endpoints]]", "[[2026-1022-instancia-como-captador-de-leads]]", "[[2026-1022-gap-lead-capture-visitors]]"]
---
## Claim
El chat de MyClone.is usa **SSE (Server-Sent Events)** con el patrón Vercel AI SDK: `POST /api/v1/personas/username/{username}/init-session` devuelve `{session_token, persona_id, persona_name, is_anonymous}` y `POST .../stream-chat` (Accept: `text/event-stream`) emite `data: {"type":"content","chunk":"..."}` y cierra con `data: {"type":"complete","session_token":"..."}`. Existe además un `special-stream-chat` paralelo. La captura de lead ocurre tras la conversación vía `POST /api/v1/sessions/{session_token}/capture-lead` con `{email, full_name}`.

## Why It Matters
El chat no requiere cuenta (`is_anonymous: true` en la sesión): el visitante interactúa sin registrarse y el email se pide **después**, en el momento de mayor valor — el mismo patrón de captador de leads que [[2026-1022-instancia-como-captador-de-leads]] describe para [[myownclone]], pero implementado con captura posterior al chat en lugar de email-gate previo.
El transporte de texto (SSE) es distinto del de audio (WebSocket/Socket.IO): ver [[2026-1022-myclone-widget-comunicacion-websocket]].

## [FRICTION]
> [[2026-1022-myclone-widget-comunicacion-websocket]] (escrita hace unas horas) afirma que "la comunicación widget↔backend de MyClone.is usa Socket.IO sobre WebSocket" con fallback a polling, y que el streaming de audio viaja por el evento `voice` binario.
> Este átomo presiona esa creencia porque el streaming de **texto** está documentado como SSE sobre HTTP (`text/event-stream`), no sobre el socket; solo el audio usaría WebSocket.
> Ambas no pueden ser completamente correctas: o el widget no usa Socket.IO para el texto y el análisis de bundles interpretó mal el transporte, o conviven dos canales (texto por SSE, audio por socket) y la nota anterior lo generalizó de más. Marcado para juicio humano, no auto-resuelto.

## Extensión (Plan de implementación 2026-06-24)
El plan de replicación de [[myownclone]] confirma este patrón como el a replicar: el popup de captura de email se dispara **después de 3 mensajes del usuario**, y la correlación se hace por `session_token` guardado en `chat_public` hacia una tabla `LeadCapture` (session_token, visitor_id, captured_at, source). Es decir, el mismo diseño de "email-gate posterior al valor" que usa MyClone.is con `POST /sessions/{token}/capture-lead`. Ver [[2026-1022-gap-lead-capture-visitors]].
