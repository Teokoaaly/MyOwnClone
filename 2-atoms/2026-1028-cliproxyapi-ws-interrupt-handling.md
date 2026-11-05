---
id: 2026-1028-cliproxyapi-ws-interrupt-handling
type: atom
certainty: solid
sources: [sources/2026-10-28-cliproxyapi-github.md]
links: ["[[2026-1023-new-api-relaykit-conversion-perdida-de-campos]]", "[[2026-1023-new-api-una-sola-api-multiproto]]"]
---

## Claim

CLIProxyAPI v8+ contains a fix (commit 9717e32) that tracks the running response identity in the Codex websocket session and rejects interrupts that do not target it, preventing late interrupts after `response.completed` from being forwarded upstream — this gates the local interrupt path by explicit turn ownership and closes it before terminal payloads are written downstream, preventing fabricated `response.incomplete` events and silently dropped claimed frames.

## Why It Matters

In multi-turn Codex workflows, websocket interrupts are a normal part of cancellation and retry behavior. Without explicit turn-ownership tracking, a late interrupt sent after the response turn is marked completed can silently forward a stale or fabricated interrupt upstream, causing the client to render incomplete or phantom responses, or to charge the user for a call that never cleanly terminated. The fix adds deterministic regression tests across completion, failure, queued rejection, upstream loss, and HTTP fallback turns, making the behavior observable and testable rather than a hidden race condition.

## [FRICTION]

> [[2026-1023-new-api-una-sola-api-multiproto]] documenta la superficie `/v1` unificada que New API expone, incluyendo `POST /v1/responses` y WebSocket `GET /v1/realtime`, pero no aborda la semántica de los interrupts dentro de esa superficie. El atom de WebSocket interrupt handling asume que el problema es específico de Codex y su sesión websocket, mientras que el atom de Nueva API trata los interrupts como una capa de protocolo más en el modelo cliente-servidor HTTP. Ambas pueden ser ciertas: el problema de interrupts después de `response.completed` es un riesgo de sesión específico de Codex, pero el patrón subyacente de que los interrupts mal clasificados pueden marcar peticiones como fallidas y regalar costos al upstream (ver [[2026-1026-new-api-correcciones-de-continuidad-de-stream-y-registro-de-uso]]) es un problema de gateway más amplio. Ambas no pueden ser completamente correctas sin distinguir el riesgo de sesión del riesgo de producto. Marcado para juicio humano, no auto-resuelto.