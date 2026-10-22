---
id: 2026-1022-plan-orden-implementacion-myownclone
type: atom
certainty: tentative
sources: [raw/articles/myownclone-osint-implementation-handoff-2026-06-24.md]
links: ["[[2026-1022-drift-schema-drizzle-sqlalchemy]]", "[[2026-1022-plan-prompt-versioning-nuestro]]", "[[2026-1022-error-fase-3-sobreconstruir]]"]
---
## Claim
El handoff fija un **orden de implementación explícito** para [[myownclone]]: (1) Step 4 — bug fixes de consistencia de schema, antes que nada ("resolver inconsistencies antes de añadir features"); (2) Step 1 — prompt versioning (mayor impacto, el `put()` ya existe); (3) Step 2 — lead/visitor (bajo esfuerzo, alto impacto); (4) Step 3 — workflows, "solo si hay demanda de usuarios"; (5) Step 5 — Langfuse, "producción / observabilidad". Las prioridades declaradas son 🔴 ALTA (versioning, leads), 🟡 MEDIA (workflows, Langfuse) y 🔴 CRÍTICO (bug fixes).

## Why It Matters
El orden es la tesis del documento: el handoff se titula "no reinventar la rueda" y pone la higiene de schema por delante de toda feature. Es la corrección directa a la lección ya registrada en el vault de no sobreconstruir ([[2026-1022-error-fase-3-sobreconstruir]]): con cuatro bugs de drift abiertos ([[2026-1022-drift-schema-drizzle-sqlalchemy]]), cada tabla nueva multiplica el trabajo de sincronización.
La decisión de **no hacer workflows** salvo demanda explícita es la más relevante: workflows es el gap de producto más grande frente a MyClone.is (ver [[2026-1022-myclone-workflows-beta-dominio]]) y aun así se pospone, porque el modo por clon ya cubre el caso de uso principal.
`tentative`: es un plan del autor del informe, no una Prioridad acordada con el equipo.

## [FRICTION]
> [[2026-1022-mvp-salir-al-mercado-pronto]] recomienda salir al mercado pronto con el mínimo, lo que sugiere que el effort debe ir a launch y no a features internas.
> Este átomo presiona esa creencia en un punto: el Step 1 del plan es el versionado de prompts, que es feature interna y no launch. Ambas no pueden ser completamente correctas: o el versionado es requisito de lanzamiento (porque un creator edita prompts y rompe el clon), o el MVP no lo incluye y la prioridad 🔴 ALTA del handoff sobrevalora la gobernanza de prompts.
> Marcado para juicio humano, no auto-resuelto.
