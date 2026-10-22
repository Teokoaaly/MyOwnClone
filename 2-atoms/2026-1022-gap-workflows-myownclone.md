---
id: 2026-1022-gap-workflows-myownclone
type: atom
certainty: solid
sources: [raw/articles/myownclone-osint-implementation-plan-2026-06-24.md]
links: ["[[2026-1022-myclone-workflows-beta-dominio]]", "[[2026-1022-gap-prompt-versioning-clonemodeprompt]]", "[[2026-1022-myclone-vs-myownclone-gaps-api]]", "[[2026-1022-plan-workflows-nuestro]]"]
---
## Claim
[[myownclone]] no tiene **workflows**: ni plantillas por industria, ni sesiones de flujo, ni objetivos con pasos. Solo chat libre. MyClone.is tiene un módulo BETA con `GET/POST /workflow-templates` (plantillas por industria: CPA, Tax, Insurance, Legal), `POST /workflows`, `POST /workflows/sessions`, `POST /workflows/sessions/{id}/answer`, `GET /workflows/{id}/analytics`, objetivos como pasos con preguntas y un `regenerate-objective` que genera nuevos objetivos con el LLM.

## Why It Matters
El gap es de **producto**, no de infraestructura: un workflow convierte un chat en un proceso con estado (activo/completado/abandonado), progreso por paso y métricas propias. Es la diferencia entre "el clon responde" y "el clon conduce una cualificación".
El plan lo sitúa en **Fase 2 (semanas 3-4)** con tres modelos nuevos —`WorkflowTemplate`, `PersonaWorkflow`, `WorkflowSession`— y effort alto, por encima de monetización y observabilidad en impacto aunque por debajo en prioridad operativa.
Es también el gap que [[2026-1022-myclone-workflows-beta-dominio]] describe como el más caro de replicar, y el que más encaja con el modo ventas de [[2026-1022-gap-prompt-versioning-clonemodeprompt]]: el versionado de prompt da control sobre el clon, pero el workflow da control sobre la conversación.
El diseño de las tres tablas (`WorkflowTemplate`, `PersonaWorkflow`, `WorkflowSession`) está en [[2026-1022-plan-workflows-nuestro]], derivado del handoff complementario.

## [FRICTION]
> [[2026-1022-plan-workflows-nuestro]] (handoff, misma fecha) sitúa los workflows **últimos** en la roadmap ("solo si hay demanda de usuarios"), mientras este plan de implementación los coloca en **Fase 2 (semanas 3-4)** con prioridad 🟡 MEDIA, por delante de Stripe Connect y de observabilidad.
> Ambas no pueden ser completamente correctas: o son dos documentos con alcances distintos (este prioriza la paridad de superficie con MyClone.is, el handoff prioriza el coste), o uno de los dos órdenes está desactualizado. Marcado para juicio humano, no auto-resuelto.
