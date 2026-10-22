---
id: 2026-1022-myclone-api-rest
type: atom
certainty: tentative
sources: [raw/articles/myownclone-technical-deep-dive-2026-06-23.md, raw/articles/myclone-deep-api-osint-2026-06-24.md]
links: ["[[2026-1022-myclone-widget-comunicacion-websocket]]", "[[2026-1022-myclone-limites-plan-free]]", "[[myownclone]]", "[[2026-1022-myclone-api-superficie-227-endpoints]]"]
---
## Claim
MyClone.is expone cuatro endpoints públicos sin autenticación (`/api/cookies/set-onboarded`, `/api/early_access_features/?token=`, `/api/surveys/?token=`, `/api/web_experiments/?token=` — este último revela un sistema de experimentos A/B en producción) y una API REST inferida desde los bundles JS con prefijo `/api/v1/`: personas, knowledge/sources, voice/sessions, widgets/tokens, conversations, usage/stats, profile, billing, más `/api/v2/integrations/zapier/webhook`. El patrón de llamada declarado es `Authorization: Bearer` + `Content-Type: application/json`, respuesta con envoltorio `{data, error}` y rate limiting con HTTP 429.

## Why It Matters
El versioning `v1`/`v2` y la envoltura uniforme `{data: ..., error: null}` son el tipo de contrato estable que [[myownclone]] (que expone su API por OpenAPI en `myownclone/dify/api/openapi/`) ya tiene estandarizado, así que la API de MyClone no aporta una ventaja técnica. Lo relevante es el endpoint público de experimentos A/B: confirma que MyClone.is optimiza por producto con experimentación continua, una capacidad de la que no hay evidencia en [[myownclone]]. Nota importante: el propio documento marca estas rutas como "inferidas de JS", no interceptadas, así que el verbo HTTP exacto y la existencia misma de cada endpoint no están verificados.

## Extensión (API OSINT 2026-06-24)
El **OpenAPI 1.0.0 de `api.myclone.is` documenta 227 endpoints con método y ruta explícitos** (`/api/v1/...`, auth por JWT Bearer), lo que confirma la existencia y el prefijo `v1` de la mayor parte de lo inferido. Ver [[2026-1022-myclone-api-superficie-227-endpoints]], donde se registra la fricción con el carácter "tentative" de esta nota. Dato nuevo no presente antes: el envolturamiento `{data, error}` **no** se observa en la respuesta de login, que devuelve campos planos (`message`, `user_id`, `token`, `account_type`).

## [FRICTION]
> [[myownclone-competitors]] (escrita hace ~4 meses) concluye que "el mercado está verde" y que solo Personify compite directamente en el mismo espacio, listando a Cpycat, Coachvox, CustomGPT, ElevenLabs y Tavus — sin mencionar a MyClone.is.
> Este átomo presiona esa creencia porque MyClone.is ocupa el mismo nicho (clone con voz + embed + knowledge connectors + páginas públicas) y su stack es más moderno (Next.js + Astro + Vercel) que el de Personify y Coachvox, que el propio informe de competencia describe como WordPress o HTML propio.
> Ambas no pueden ser completamente correctas: o MyClone.is no es un competidor directo, o la conclusion de "mercado verde con un solo rival directo" está desactualizada. Marcado para juicio humano, no auto-resuelto.
