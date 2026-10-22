---
id: 2026-1022-myownclone-ventajas-sobre-myclone
type: atom
certainty: solid
sources: [raw/articles/myownclone-osint-implementation-plan-2026-06-24.md]
links: ["[[2026-1022-myclone-vs-myownclone-gaps-api]]", "[[2026-1022-arquitectura-rac-tres-modos-por-clon]]", "[[2026-1022-gap-dify-como-capa-inferencia-prompts]]", "[[2026-1022-myclone-carece-modos-memories-ni-visitors]]"]
---
## Claim
El gap analysis del plan de implementación deja explícito que [[myownclone]] tiene **dos ventajas que MyClone.is no tiene**: el sistema de modos por clon (teach/support/sales vía `CloneSilo`) y las memorias/plantillas del creator (`CreatorMemory` con tipos MEMORY, SIGNATURE, TEMPLATE). MyClone.is no tiene modos ni sistema de memorias, y usa OpenAI directo mientras [[myownclone]] usa Dify. En lo demás —chat streaming SSE, creación de clones, biblioteca de conocimiento, email inbound, multi-tenant— el nivel de paridad es alta.

## Why It Matters
Es la otra mitad del análisis de gaps: los 7 gaps del plan no cubren el núcleo técnico, sino la capa de monetización, orquestación y observabilidad. MyClone.is es más ancho en superficie; [[myownclone]] es más profundo en el modelo de persona.
Las memorias con tipo y condición de disparo (`trigger_condition`, `priority`) son un modelo de prompt persistente por el creator, que es justo lo que MyClone.is resuelve con plantillas de prompt reutilizables ([[2026-1022-gap-dify-como-capa-inferencia-prompts]]): mismo problema —composición de identidad reutilizable— con dos designs distintos, uno dirigido a la granularidad por modo y el otro a la plantilla parametrizada.
El sistema de modos es la ventaja que el propio plan de replicación quiere **mantener**: el versionado de prompt debe funcionar por modo, no sobre un prompt único.
El handoff complementario llega a la misma conclusión desde otra fuente y añade el matiz de que MyClone.is sustituye los modos por workflows con estado y objetivo; ver [[2026-1022-myclone-carece-modos-memories-ni-visitors]].
