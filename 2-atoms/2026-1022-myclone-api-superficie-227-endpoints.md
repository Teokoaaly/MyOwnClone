---
id: 2026-1022-myclone-api-superficie-227-endpoints
type: atom
certainty: solid
sources: [raw/articles/myclone-deep-api-osint-2026-06-24.md, raw/articles/myownclone-osint-implementation-handoff-2026-06-24.md]
links: ["[[2026-1022-myclone-stack-tecnologico]]", "[[2026-1022-myclone-api-rest]]", "[[myownclone]]", "[[2026-1022-plan-lead-capture-visitors]]", "[[2026-1022-myclone-knowledge-library-fuentes]]"]
---
## Claim
La API de MyClone.is está documentada en un OpenAPI 1.0.0 con **227 endpoints** bajo `https://api.myclone.is`, servida por un backend **Python + Uvicorn (ASGI)** alojado en **AWS** (rangos 54.208.x.x / 3.86.x.x, certificado Amazon RSA 2048 M01) y con autenticación por **JWT Bearer**. La superficie está organizada en grupos: auth, users, personas, conversations, knowledge/RAG, embeddings, voice, livekit, prompt, workflows, scraping, voice-processing, stripe, tier, custom-domains, webhooks e integraciones.

## Why It Matters
227 endpoints es una superficie de producto muy superior a la que [[myownclone]] documenta hoy, y su organización por dominio (personas, conocimiento, voz, prompts, workflows, pagos) revela que MyClone.is opera como **plataforma**, no como herramienta de un solo creador. El backend Python/Uvicorn (no Node) es un dato de arquitectura que [[2026-1022-myclone-stack-tecnologico]] no recogía: el frontend es JS/Next, pero la lógica de dominio vive en Python. Ver [[2026-1022-myclone-api-rest]] para el patrón de contrato observado.

## [FRICTION]
> [[2026-1022-myclone-api-rest]] (escrita hace unas horas) afirma que la API de MyClone.is está "inferida desde los bundles JS" y marca `tentative` porque "el verbo HTTP exacto y la existencia misma de cada endpoint no están verificados".
> Este átomo presiona esa creencia porque el OpenAPI 1.0.0 documenta los 227 endpoints con método y ruta explícitos, y los grupos de auth/knowledge/voice/stripe coinciden con lo que antes solo se infería.
> Ambas no pueden ser completamente correctas: o la spec es la fuente real y la inferencia anterior queda superada, o la spec está desactualizada respecto al backend desplegado. Marcado para juicio humano, no auto-resuelto.

## Extensión (Handoff OSINT+Implementación 2026-06-24)
El handoff reitera la cifra (**227 endpoints**, OpenAPI 1.0.0, Python + Uvicorn en AWS) y añade la tabla de endpoints "más importantes" con su método, ruta y si requieren Bearer o son públicos. Aporta dos precisiones de contrato que no estaban en la spec resumida:
- **Dos endpoints son públicos sin auth**: `GET /tier/plans` (planes y límites) y `GET /workflow-templates` (catálogo de plantillas). Todo lo demás de la lista requiere `Authorization: Bearer`.
- El grupo de **leads** está cerrado: `GET /personas/{id}/visitors` (lista de leads por persona) y `POST /sessions/{token}/capture-lead` (captura post-chat) — el mismo patrón que [[2026-1022-plan-lead-capture-visitors]] propone replicar en [[myownclone]].
Y el grupo de conocimiento se confirma en dos endpoints: `GET /personas/{persona_id}/knowledge-sources` (fuentes asignadas a una persona) y `GET /knowledge-library/users/{user_id}` (biblioteca completa del usuario), coherente con [[2026-1022-myclone-knowledge-library-fuentes]].
