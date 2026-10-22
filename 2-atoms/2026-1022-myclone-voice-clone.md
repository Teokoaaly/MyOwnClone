---
id: 2026-1022-myclone-voice-clone
type: atom
certainty: solid
sources: [raw/articles/myownclone-technical-deep-dive-2026-06-23.md, raw/articles/myclone-deep-api-osint-2026-06-24.md]
links: ["[[2026-1022-myclone-knowledge-library-fuentes]]", "[[2026-1022-myclone-limites-plan-free]]", "[[2026-1022-myclone-competidor-arquitectura]]", "[[2026-1022-myclone-voice-providers-cartesia-elevenlabs]]"]
---
## Claim
El Voice Clone de MyClone.is ofrece dos vías de captura —grabar directamente (30-60 segundos recomendados) o subir fichero WAV/MP3/M4A de hasta 10MB— con visualización de forma de onda, prueba de síntesis de voz antes de completar el setup y un límite de consumo de 10 minutos de voz al mes en plan Free.

## Why It Matters
El "grabar 30-60s en el wizard + probar la síntesis antes de salir" es un patrón de activación: el usuario oye su clone funcionando y eso es lo que dispara el alta, no el formulario. Es la diferencia real frente a un clon solo-texto. El límite de 10 min/mes en Free está atado al mismo contador que el texto (500 msgs), así que el uso de voz está doblemente tarifado: es la palanca de monetización más evidente del producto.

## Extensión (API OSINT 2026-06-24)
La API revela que la clonación no es una sola vía sino **tres orígenes por cada uno de dos proveedores**: Cartesia y ElevenLabs ofrecen `create_voice_clone`, `create_voice_clone_from_paths` y `create_voice_clone_from_s3`, con `GET .../users/{user_id}/voice-clones` para listar y `DELETE` para borrar (incluido `DELETE /eleven_labs/voice/by-username/{username}`). La voz se asigna por **persona o por expert** (`PATCH /persona/{persona_id}/voice`, `PATCH /expert/{username}/voice`) y convive con un subsistema de **procesamiento asíncrono** (`/voice-processing/upload`, `/jobs`, `/jobs/{job_id}/progress`, `/jobs/{job_id}/retry`) y con **LiveKit** para voz en tiempo real. Ver [[2026-1022-myclone-voice-providers-cartesia-elevenlabs]].
