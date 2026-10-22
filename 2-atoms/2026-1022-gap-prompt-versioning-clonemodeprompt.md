---
id: 2026-1022-gap-prompt-versioning-clonemodeprompt
type: atom
certainty: solid
sources: [raw/articles/myownclone-osint-implementation-plan-2026-06-24.md]
links: ["[[2026-1022-myclone-prompt-versioning]]", "[[2026-1022-arquitectura-rac-tres-modos-por-clon]]", "[[2026-1022-myclone-prompt-template-sistema]]", "[[2026-1022-plan-prompt-versioning-nuestro]]"]
---
## Claim
El prompt de modo de [[myownclone]] es un **campo único sobrescribible**: `CloneModePrompt` tiene solo `clone_id`, `mode`, `system_prompt` e `is_active`, y cada `PUT /myownclone/clones/<clone_id>/prompts` sobrescribe sin guardar la versión anterior — no hay historial, ni restore, ni diff. El plan de implementación lo marca como el gap **crítico**: el historial de versiones de prompt no existe en nuestro código.

## Why It Matters
Un creator que ajusta el prompt y empeora el clon no tiene forma de volver atrás sin redeploy: el prompt es el producto, y sin versionado no es gobernable. MyClone.is resuelve esto con `persona_prompt_versions` + history/restore/compare/timeline ([[2026-1022-myclone-prompt-versioning]]).
El plan propone dos tablas nuevas (`PersonaPromptVersion` y `PersonaPromptHistory`, con `version_number`, `change_summary`, `created_by`) y cuatro endpoints (`/prompts/history`, `/prompts/restore/{version}`, `/prompts/diff?v1&v2`, más el `PUT` que ya crea versión), con el guardado del prompt anterior ocurre **antes** de sobrescribir.
El versionado tendría además que funcionar **por modo** (teach/support/sales), que es una ventaja que MyClone.is no tiene al no tener modos ([[2026-1022-arquitectura-rac-tres-modos-por-clon]]): el versionado por modo no es un clon de la API de MyClone, es un feature propio.
El diseño detallado de la propuesta (tablas `prompt_versions` + `prompt_variables`, `generate_change_summary()` con `difflib`, tab "Historial" en `cerebro/page.tsx`) está en [[2026-1022-plan-prompt-versioning-nuestro]], derivado del handoff complementario.
