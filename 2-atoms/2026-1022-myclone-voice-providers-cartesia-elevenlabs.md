---
id: 2026-1022-myclone-voice-providers-cartesia-elevenlabs
type: atom
certainty: solid
sources: [raw/articles/myclone-deep-api-osint-2026-06-24.md, raw/articles/myownclone-osint-implementation-plan-2026-06-24.md]
links: ["[[2026-1022-myclone-voice-clone]]", "[[2026-1022-myclone-knowledge-library-fuentes]]", "[[2026-1022-myclone-chat-streaming-sse]]", "[[2026-1022-gap-voz-en-vivo-myownclone]]"]
---
## Claim
La voz de MyClone.is se apoya en **tres proveedores simultáneos**: Cartesia AI (`/api/v1/cartesia/create_voice_clone`, `..._from_paths`, `..._from_s3`, `GET .../users/{user_id}/voice-clones`, `DELETE .../voice-clones/{voice_id}`), ElevenLabs (`/api/v1/eleven_labs/create_voice_clone`, `..._from_paths`, `..._from_s3`, `DELETE /eleven_labs/voice/{voice_id}`, `DELETE /eleven_labs/voice/by-username/{username}`) y **LiveKit** para voz en tiempo real (`POST /livekit/connection-details`, `POST /livekit/session/{session_id}/heartbeat`). El clon se asigna por persona o por expert (`PATCH /persona/{persona_id}/voice`, `PATCH /expert/{username}/voice`).

## Why It Matters
Los tres endpoints de clonación por cada proveedor (`from_paths`, `from_s3`, directo) son la misma operación con tres orígenes: fichero local, objeto S3 o stream. Es una abstracción de ingesta reutilizable — valiosa si [[myownclone]] quiere clonar voz desde material ya subido a su propio bucket, sin re-descargar.
Mantener **dos proveedores de clonación en paralelo** es una decisión de negocio: redundancia y rango de precio, pero también duplicación de código. El único que no es clonación sino transporte es LiveKit, que habilita conversación en vivo (voz ↔ voz), no solo texto con voz ([[2026-1022-myclone-chat-streaming-sse]]).
El borrado por username (`by-username/{username}`) sugiere que la voz está linked al creator, no solo a la persona: un mismo creator con varios clones de voz.

## Extensión (Plan de implementación 2026-06-24)
El plan de replicación confirma que el gap de voz de [[myownclone]] es **total** — no hay clonación de voz ni LiveKit — y lo clasifica como prioridad **baja**, con la voz en tiempo real como el único gap que no se aborda en las tres primeras fases (queda para Fase 4, semana 7+, junto a Langfuse y dominios). Ver [[2026-1022-gap-voz-en-vivo-myownclone]].
