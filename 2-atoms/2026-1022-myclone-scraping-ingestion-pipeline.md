---
id: 2026-1022-myclone-scraping-ingestion-pipeline
type: atom
certainty: solid
sources: [raw/articles/myclone-deep-api-osint-2026-06-24.md]
links: ["[[2026-1022-myclone-knowledge-library-fuentes]]", "[[2026-1022-myclone-api-superficie-227-endpoints]]", "[[2026-1022-myclone-viaje-embeddings-voyage]]"]
---
## Claim
La ingesta de MyClone.is es un **pipeline asíncrono con jobs**: `POST /scraping/linkedin`, `/scraping/twitter`, `/scraping/website`, `/scraping/auto-onboard` y `/scraping/bulk-onboard` lanzan trabajos, con `GET /scraping/status/{user_id}` y `GET /scraping/audit/{job_id}` para seguimiento y auditoría. La expertización tiene su propio estado en streaming: `GET /ingestion/expert-status/{username}` y `GET /ingestion/expert-status-stream/{username}` (SSE), más `GET /ingestion/persona/{persona_id}/data-sources`. En paralelo, el pipeline de voz procesa ficheros (`/voice-processing/upload`, `/jobs`, `/jobs/{job_id}/progress`, `/jobs/{job_id}/retry`) e **ingiere YouTube** (`POST /voice-processing/ingest-youtube`, `/youtube/refresh`, `/youtube/check-embeddings/{user_id}/{youtube_video_id}`).

## Why It Matters
`auto-onboard` + `bulk-onboard` es el atajo de mayor apalancamiento: una sola llamada construye el clon completo (perfil + contenido + voz) desde un username. Para [[myownclone]], ese es el gap de activación más caro — hoy el onboarding es caso por caso y manual.
El par `status` + `audit/{job_id}` es un patrón de **jobs observables**: progreso, reintentos y auditoría por job. Y el endpoint `expert-status-stream` sugiere que la interfaz muestra la expertización construyéndose en vivo, un feedback loop de activación que una replicación de [[myownclone]] no tiene.
Ver también [[2026-1022-myclone-knowledge-library-fuentes]] para los tipos de fuente y [[2026-1022-myclone-viaje-embeddings-voyage]] para la capa de embeddings.
