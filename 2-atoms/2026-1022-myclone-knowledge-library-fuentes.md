---
id: 2026-1022-myclone-knowledge-library-fuentes
type: atom
certainty: solid
sources: [raw/articles/myownclone-technical-deep-dive-2026-06-23.md, raw/articles/myclone-deep-api-osint-2026-06-24.md]
links: ["[[2026-1022-myclone-competidor-arquitectura]]", "[[2026-1022-myclone-limites-plan-free]]", "[[ai-clones]]", "[[2026-1022-myclone-scraping-ingestion-pipeline]]"]
---
## Claim
La Knowledge Library de MyClone.is soporta 7 tipos de fuente: LinkedIn (perfil, posts, experiencia), Twitter/X (tuits, hilos, engagement), Website (blog, artículos, portfolio), Documents (PDF, DOCX, XLSX, PPTX), Text (pegado directo), Audio (MP3/WAV/M4A, máx 10MB por archivo) y Video (MP4/MOV/AVI/MKV, máx 200MB por archivo con tope total de 500MB). La ingesta de YouTube transcripts no está disponible en el plan Free (solo Pro+).

## Why It Matters
Es la misma superficie de ingesta que [[ai-clones]] describe como núcleo técnico (ingesta → retrieval → generación → guardrails), pero resuelta con conectores sociales OAuth además de ficheros. Los conectores de Twitter/X y LinkedIn son la diferencia: permiten a un clon "seguir" al creador en tiempo real en lugar de depender solo de material subido, algo que el modelo de datos de [[myownclone]] (biblioteca del creador) no cubre hoy.

## Extensión (API OSINT 2026-06-24)
La API confirma la superficie y añade dos matices: (a) la ingesta es **asíncrona y en jobs** con `POST /scraping/linkedin|twitter|website`, `auto-onboard`, `bulk-onboard`, más `GET /scraping/status/{user_id}` y `GET /scraping/audit/{job_id}`; (b) la ingesta de YouTube tiene su propio pipeline en `/voice-processing/*` (`POST /voice-processing/ingest-youtube`, `/youtube/refresh`, `/youtube/check-embeddings/{user_id}/{video_id}`), lo que confirma que YouTube no es solo "un tipo de fuente más" sino un subsistema con processing de audio y reindexado de embeddings. Ver [[2026-1022-myclone-scraping-ingestion-pipeline]] y [[2026-1022-myclone-viaje-embeddings-voyage]].
