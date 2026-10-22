---
id: 2026-1022-plan-replicacion-myclone-fases-prioridad
type: atom
certainty: tentative
sources: [raw/articles/myownclone-osint-implementation-plan-2026-06-24.md]
links: ["[[2026-1022-myclone-vs-myownclone-gaps-api]]", "[[2026-1022-gap-prompt-versioning-clonemodeprompt]]", "[[2026-1022-gap-lead-capture-visitors]]", "[[2026-1022-mvp-salir-al-mercado-pronto]]", "[[2026-1022-plan-orden-implementacion-myownclone]]"]
---
## Claim
El plan de implementación de [[myownclone]] para replicar a MyClone.is ordena 11 pasos en 4 fases con una matriz impacto/esfuerzo: **Fase 1 (semanas 1-2)** prompt versioning backend+frontend y lead capture backend+frontend (prioridad 🔴 ALTA); **Fase 2 (semanas 3-4)** workflows, modelo + API + frontend (🟡 MEDIA); **Fase 3 (semanas 5-6)** Stripe Connect (🟡 MEDIA); **Fase 4 (semana 7+)** Langfuse, voice cloning y custom domains (🟢 BAJA).

## Why It Matters
La prioridad operativa es explícita: cerrar primero los dos gaps que tocan la **confianza del creator en su clon** (poder deshacer un prompt) y el **contacto con el visitante** (saber quién llega), antes que la sofisticación de plataforma.
Es coherente con [[2026-1022-mvp-salir-al-mercado-pronto]]: el founder prioriza lo que ya está validado, y tanto versionado como captura de leads son cambios cerrados sobre código existente, no nuevas superficies.
El plan marca workflow con effort alto en las tres capas (modelo, API, frontend), lo que explica que quede por detrás de monetización aunque ambas tengan impacto medio-alto: la monetización es un endpoint y el workflow es un sistema.
Nota: es una **planificación**, no una evidencia de ejecución — se marca `tentative`.
Este plan de implementación y el handoff ([[2026-1022-plan-orden-implementacion-myownclone]]) son dos documentos de la misma fecha con **órdenes de ejecución distintos**: este pone los workflows en Fase 2 (semanas 3-4) y añade monetización, voz y dominios; el handoff pone los workflows al final ("solo si hay demanda") y abre con bug fixes de schema. La divergencia es la observación más útil de la comparación.

## [FRICTION]
> [[2026-1022-myclone-vs-myownclone-gaps-api]] enumera 8 gaps de [[myownclone]] frente a MyClone.is e incluye en ellos la "ingesta de YouTube" y el "versionado de prompts" como ausencias; este plan de implementación solo aborda 7 gaps (no aborda la ingesta de YouTube ni los endpoints de voz con ingesta).
> La fricción es de alcance: o el plan es intencionadamente parcial, o la lista de 8 gaps del OSINT es más amplia que la prioridad real de ejecución. Marcado para juicio humano, no auto-resuelto.
