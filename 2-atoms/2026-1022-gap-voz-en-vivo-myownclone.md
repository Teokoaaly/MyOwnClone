---
id: 2026-1022-gap-voz-en-vivo-myownclone
type: atom
certainty: solid
sources: [raw/articles/myownclone-osint-implementation-plan-2026-06-24.md]
links: ["[[2026-1022-myclone-voice-providers-cartesia-elevenlabs]]", "[[2026-1022-myclone-chat-streaming-sse]]", "[[2026-1022-myclone-api-superficie-227-endpoints]]"]
---
## Claim
[[myownclone]] no tiene voz de ningún tipo: ni clonación de voz, ni LiveKit para conversación en tiempo real. El gap está marcado como **baja prioridad** en el plan, a diferencia de MyClone.is, que expone `POST /livekit/connection-details` (credenciales de sala), `POST /livekit/session/{id}/heartbeat` (keepalive) y voz en vivo durante el chat, además de clonación con Cartesia y ElevenLabs.

## Why It Matters
El gap de voz está completo, no parcial: [[2026-1022-myclone-voice-providers-cartesia-elevenlabs]] describe tres proveedores en paralelo en MyClone.is (Cartesia, ElevenLabs, LiveKit), mientras el plan confirma que de nuestro lado no hay ni el transporte en vivo.
Priorizarlo bajo es coherente con el tipo de cliente objetivo del vault —negocios online con infoproductos, no fama— y con el hecho de que el modo soporte/ventas de [[2026-1022-myclone-chat-streaming-sse]] resuelva más valor en texto que en voz.
Pero es también el gap que más se aleja de "habla como el creador": MyClone.is combina voz con streaming SSE de texto, y un clon de voz es lo que más se parece a la persona real frente a un clon de texto bien diseñado.
