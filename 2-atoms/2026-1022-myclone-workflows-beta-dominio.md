---
id: 2026-1022-myclone-workflows-beta-dominio
type: atom
certainty: solid
sources: [raw/articles/myclone-deep-api-osint-2026-06-24.md, raw/articles/myownclone-osint-implementation-plan-2026-06-24.md]
links: ["[[2026-1022-myclone-verticalizacion-y-transparencia]]", "[[2026-1022-myclone-api-superficie-227-endpoints]]", "[[2026-1022-myclone-competidor-arquitectura]]", "[[2026-1022-gap-workflows-myownclone]]"]
---
## Claim
El módulo **Workflows (BETA)** de MyClone.is es un motor de flujos de conversación con estado, no una simple plantilla: `GET /workflow-templates` (público) y `GET /workflow-templates/{id}`, `POST /workflow-templates/enable`, `PUT /workflow-templates/workflows/{workflow_id}/customize`, `POST .../sync` + `GET .../sync-status`, CRUD de `/workflows` con `GET /workflows/{id}/analytics` y `POST /workflows/{id}/publish` y `POST /workflows/{id}/regenerate-objective`, más sesiones (`/workflows/sessions`) con `POST .../answer` y `POST .../abandon`.

## Why It Matters
Esto confirma y **precisa** la verticalización que [[2026-1022-myclone-verticalizacion-y-transparencia]] solo daba por observada en la navegación: la API revela un workflow con objetivo (`regenerate-objective`), progreso de sync, publicación, métricas de analítica y un ciclo de vida de sesión con respuestas y abandono. Es decir, workflows no son "prompts con ramas" — tienen ciclo de vida, métricas y versión publicada.
Para [[myownclone]], es el gap estructural más caro de replicar: un workflow es un flujo con estado y objetivo, no una respuesta aislada.

## Extensión (Plan de implementación 2026-06-24)
El plan de replicación confirma los endpoints y añade que las plantillas de MyClone.is vienen **por industria (CPA, Tax, Insurance, Legal)**, y que cada workflow expone `objectives` como pasos con preguntas más un `regenerate-objective` que genera nuevos objetivos con el LLM. Del lado de [[myownclone]] no hay nada de esto: solo chat libre. Ver [[2026-1022-gap-workflows-myownclone]].
