---
id: 2026-1022-myclone-prompt-versioning
type: atom
certainty: solid
sources: [raw/articles/myclone-deep-api-osint-2026-06-24.md, raw/articles/myownclone-osint-implementation-handoff-2026-06-24.md, raw/articles/myownclone-osint-implementation-plan-2026-06-24.md]
links: ["[[2026-1022-myclone-prompt-template-sistema]]", "[[2026-1022-myclone-langfuse-observabilidad]]", "[[2026-1022-myclone-competidor-arquitectura]]", "[[2026-1022-plan-prompt-versioning-nuestro]]", "[[2026-1022-gap-prompt-versioning-clonemodeprompt]]"]
---
## Claim
Cada prompt de persona en MyClone.is es **versionado y reversible**: `GET/PUT /prompt/persona-prompts/{persona_id}`, `GET .../compare` (comparación lado a lado de versiones), `GET .../history` y `GET .../history/{version}`, `POST .../restore/{version}`, `GET .../timeline` (evolución temporal) y `GET .../versions`. Además existe `GET /prompt/list-active-prompts` y un gestor de plantillas reutilizables (`/prompt-templates/`) con deactivate.

## Why It Matters
Es la diferencia entre "editar el prompt" y "gobernar el prompt": con timeline, compare y restore, un cambio de prompt es un artefacto auditable y reversible. Para [[myownclone]], cuyo clon se define vía interview + base de conocimiento, esto cubre un riesgo real: cuando un creator ajusta su prompt y el clon empeora, no hay forma de volver atrás sin redeploy.
El `restore` por versión es además la pieza que hace posible el A/B testing controlado que el propio informe de MyClone.is lista como ventaja (ver [[2026-1022-myclone-langfuse-observabilidad]]).

## Extensión (Plan de implementación 2026-06-24)
El plan de replicación de [[myownclone]] confirma esta superficie como referencia a replicar y **concreta el gap de nuestro lado**: `CloneModePrompt` es un único campo `system_prompt` sin historial, y cada `PUT` sobrescribe el anterior. La propuesta es crear `PersonaPromptVersion` y `PersonaPromptHistory` y exponer `/prompts/history`, `/prompts/restore/{version}` y `/prompts/diff?v1&v2`. Un matiz propio: el versionado debe ir **por modo** (teach/support/sales), cosa que MyClone.is no necesita al no tener modos. Ver [[2026-1022-gap-prompt-versioning-clonemodeprompt]].

## Extensión (Handoff OSINT+Implementación 2026-06-24)
El handoff confirma la superficie con los nombres exactos de los endpoints y añade el detalle de la **forma de la versión**: el historial devuelve objetos `{version_number, created_at, change_summary, created_by}` — es decir, MyClone.is **etiqueta cada versión con un resumen del cambio y su autor**, no solo con un timestamp. `compare?v1=X&v2=Y` y `timeline` completan el juego.
Ese detalle es la parte que [[2026-1022-plan-prompt-versioning-nuestro]] propone replicar en [[myownclone]] (campo `change_summary` + `created_by` + `difflib` para generar el resumen automáticamente), junto con una tabla `prompt_variables` que MyClone.is **no** expone y que el handoff añade por decisión propia.
