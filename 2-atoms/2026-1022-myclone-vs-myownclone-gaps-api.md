---
id: 2026-1022-myclone-vs-myownclone-gaps-api
type: atom
certainty: tentative
sources: [raw/articles/myclone-deep-api-osint-2026-06-24.md, raw/articles/myownclone-osint-implementation-handoff-2026-06-24.md, raw/articles/myownclone-osint-implementation-plan-2026-06-24.md]
links: ["[[2026-1022-myclone-api-superficie-227-endpoints]]", "[[2026-1022-myclone-workflows-beta-dominio]]", "[[myownclone]]", "[[2026-1022-myclone-carece-modos-memories-ni-visitors]]", "[[2026-1022-plan-orden-implementacion-myownclone]]", "[[2026-1022-myownclone-ventajas-sobre-myclone]]"]
---
## Claim
El propio informe de OSINT traza una comparativa MyClone.is vs MyOwnClone a partir de la API. Lo que MyOwnClone **sí puede replicar** (auth completo con credenciales + OAuth, knowledge library con scraping multi-fuente, clonación de voz con Cartesia + ElevenLabs, pipeline RAG con embeddings de Voyage, widget embebible, chat por sesión con streaming SSE, captura de leads, sistema de plantillas de prompt) coincide casi exactamente con el núcleo técnico de [[myownclone]]. Lo que MyOwnClone **no tiene** son 8 gaps: `/workflows/*`, `/langfuse/*`, `/livekit/*`, `/stripe/personas/*/monetization`, `/custom-domains/*`, `/visitors/*`, `/voice-processing/*` con ingesta de YouTube, y el historial/comparación de versiones de prompt.

## Why It Matters
El informe delinea el **núcleo replicable vs los 8 gaps**, y los 8 gaps son todos de *producto y comercial* (flujos, eval, voz en vivo, pagos por clon, whitelabel, gestión de leads, ingesta de vídeo, versionado de prompts) — ninguno es de infraestructura base. Es decir: el diferencial real de MyClone.is sobre [[myownclone]] no está en el RAG ni en el widget, sino en la capa de monetización y de orquestación de producto.
Los 7 gaps que la investigación anterior ([[2026-1022-myclone-verticalizacion-y-transparencia]]) listaba como "no llega" son los mismos que esta API confirma. La lista de replicables es, en cambio, un checklist de implementación: es la parte que [[myownclone]] puede igualar, y por tanto también la que deja de ser ventaja para MyClone.is.
Nota: la comparativa la hace el propio autor del OSINT, no una medición independiente; se marca `tentative`.

## Extensión (Handoff OSINT+Implementación 2026-06-24)
El handoff de implementación **confirma uno de los 8 gaps desde dentro de nuestro propio código**: `CloneModePrompt.system_prompt` está comentado explícitamente como "PROMPT ACTUAL — SIN HISTORIAL", es decir, el historial de versiones de prompt no existe en [[myownclone]] y hay que construirlo (ver [[2026-1022-plan-prompt-versioning-nuestro]]).
También reordena el coste real de los gaps con una tabla de prioridades y esfuerzo: workflows = esfuerzo **alto** y "solo si hay demanda"; prompt versioning = esfuerzo medio con "código existente ya tiene el put()"; lead/visitor = esfuerzo **bajo** con "alto impacto" (ver [[2026-1022-plan-orden-implementacion-myownclone]]).
Y añade una asimetría que el comparativo anterior no recogía: MyOwnClone ya tiene modos por clon, memorias y visitor tracking, capacidades que MyClone.is no expone (ver [[2026-1022-myclone-carece-modos-memories-ni-visitors]]). Es decir, la relación no es "MyOwnClone va detrás en 8 features": va detrás en 8 features de plataforma/comercial, y delante en 3 de modelo de producto.

## [FRICTION]
> [[2026-1022-myclone-verticalizacion-y-transparencia]] (escrita hace unas horas) afirma que MyClone.is "no llega" a 7 oportunidades de [[myownclone]] (onboarding por objetivo, kits por industria, colaboración en equipo, marketplace de prompts, analytics de funnel, modo sandbox, export/import de config).
> Este átomo presiona esa creencia porque la API muestra que MyClone.is tiene workflows con analytics por workflow (`GET /workflows/{id}/analytics`), plantillas de prompt reutilizables (`/prompt-templates/`) y versionado de prompts con compare/timeline — es decir, buena parte de esas 7 "no llega" sí están cubiertas en alguna forma, aunque sea más cruda.
> Ambas no pueden ser completamente correctas: o esas 7 oportunidades siguen sin estar (y las coincidencias son superficiales), o la lista de "no llega" era demasiado generosa con MyClone.is. Marcado para juicio humano, no auto-resuelto.

## Extensión (Plan de implementación 2026-06-24)
El plan de replicación de [[myownclone]] confirma esta lectura desde el lado de nuestro código y la **reduce a 7 gaps**, todos de la misma familia (prompt versioning, visitors/leads, workflows, Langfuse, Stripe Connect, custom domains, LiveKit). Los dos gaps que este plan no aborda son la ingesta de YouTube y los endpoints de voz con ingesta — es decir, lo que el plan considera "ya cubrible" o "no prioritario".
El plan añade además la **mitad positiva** de la comparativa: MyOwnClone tiene modos por clon y memorias/plantillas, que MyClone.is no tiene, y mantiene Dify como capa de inferencia frente al OpenAI directo del competidor. Ver [[2026-1022-myownclone-ventajas-sobre-myclone]].
