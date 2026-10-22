---
id: 2026-1022-myclone-verticalizacion-y-transparencia
type: atom
certainty: tentative
sources: [raw/articles/myownclone-technical-deep-dive-2026-06-23.md, raw/articles/myclone-deep-api-osint-2026-06-24.md]
links: ["[[2026-1022-myclone-competidor-arquitectura]]", "[[2026-1022-myclone-limites-plan-free]]", "[[myownclone-competitors]]", "[[2026-1022-myclone-workflows-beta-dominio]]", "[[2026-1022-myclone-stripe-connect-monetizacion]]"]
---
## Claim
El informe acredita dos palancas competitivas de MyClone.is más allá de la tecnología: (a) verticalización mediante "Workflows BETA" con plantillas por industria (CPA, Tax, Insurance) y (b) transparencia de uso, con contadores en tiempo real y fecha explícita de reset en `/dashboard/usage`, lo que según el informe reduce el churn por sorpresas de facturación. Ambas son a nivel de producto: no dependen del stack.

## Why It Matters
El propio informe concluye que para [[myownclone]] "el camino no es copiar sino elevar", y enumera las 7 oportunidades donde MyClone.is todavía no llega: onboarding más personalizado por objetivo, kits de knowledge por industria, colaboración en equipo en la biblioteca, marketplace de prompts, analytics de funnel widget→acción, modo sandbox y export/import de config. Ese es el gap accionable: las palancas de MyClone.is son de UX/comercial, no de arquitectura, y [[myownclone]] ya tiene la parte difícil (multi-tenant, inbox triage, RAC) documentada en `entities/myownclone.md`. Nota: el item de Workflows BETA aparece en la navegación y en la tabla de diferenciales, pero el informe no describe sus plantillas ni su contenido, así que la afirmación sobre verticalización es solida en cuanto a existencia e industrias listadas, no en cuanto a calidad.

## Extensión (API OSINT 2026-06-24)
La API confirma la existencia de **Workflows BETA** como módulo de primera clase y precisa su naturaleza: `GET /workflow-templates` (público), `POST /workflow-templates/enable`, `PUT /workflow-templates/workflows/{id}/customize`, `.../sync` + `.../sync-status`, CRUD de `/workflows` con `GET /workflows/{id}/analytics` y `POST /workflows/{id}/publish`, y sesiones con `POST .../answer` / `POST .../abandon`. Es decir, son flujos con **objetivo, ciclo de vida, publicación y métricas** — no plantillas estáticas. La transparencia, por su parte, se confirma vía `/tier/usage` con `reset_date` explícito. Ver [[2026-1022-myclone-workflows-beta-dominio]] y [[2026-1022-myclone-stripe-connect-monetizacion]] (la monetización por persona es la segunda palanca comercial que la API confirma).

## [FRICTION]
> [[myownclone-competitors]] (escrita hace ~4 meses) sitúa a Personify como el único rival directo, con una similaridad estimada del 80% frente a [[myownclone]], y define la oportunidad de MyOwnClone como "3 silos RAG + triage inbox + videollamadas + instancias contextuales" frente a un rival "más simple".
> Este átomo presiona esa creencia porque MyClone.is ofrece además voz clonada con streaming de audio, workflow templates por industria y páginas públicas por clon — un rival directo que además tiene el stack más moderno (Next.js + Astro + Vercel) de todo el mapa de competidores.
> Ambas no pueden ser completamente correctas: o MyClone.is es el verdadero rival directo y el mapa de [[myownclone-competitors]] está incompleto/desactualizado, o su verticalización (BETA) y su "similaridad" no alcanzan el nivel de un competidor temido. Marcado para juicio humano, no auto-resuelto.
