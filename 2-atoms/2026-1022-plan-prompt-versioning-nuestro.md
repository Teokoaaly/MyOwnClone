---
id: 2026-1022-plan-prompt-versioning-nuestro
type: atom
certainty: tentative
sources: [raw/articles/myownclone-osint-implementation-handoff-2026-06-24.md]
links: ["[[2026-1022-myclone-prompt-versioning]]", "[[2026-1022-pipeline-chat-actual-myownclone]]", "[[2026-1022-drift-schema-drizzle-sqlalchemy]]"]
---
## Claim
El handoff propone replicar en [[myownclone]] el versionado de prompts de MyClone.is (prioridad 🔴 ALTA, esfuerzo medio) con **dos tablas nuevas** (`prompt_versions` con snapshot completo + unicidad `(clone_id, mode, version_number)`, y `prompt_variables` con el valor de cada variable), **cuatro endpoints** (`prompts/history`, `prompts/restore/{version}`, `prompts/diff`, más el `put()` existente modificado para guardar la versión anterior antes de sobrescribir), una función `generate_change_summary()` con `difflib` que resume "+N líneas / -N líneas", y una **UI**: un cuarto tab "Historial" en `cerebro/page.tsx` con botón "Restaurar" y modal de diff. La migración inicial crea la versión 1 desde los prompts activos existentes (`INSERT ... SELECT ... WHERE is_active = TRUE`).

## Why It Matters
Es el gap de gobernanza de prompt identificado en [[2026-1022-myclone-prompt-versioning]], y el handoff es explícito sobre por qué encaja aquí: el `put()` de prompts ya existe, así que el coste incremental es bajo y el impacto alto — "mayor impacto, código existente ya tiene el put()".
El plan es **nuestro**, no un hecho verificado de MyClone: se marca `tentative`. El diseño replica la superficie observada del competidor (history/restore/diff), pero el nuestro añade `prompt_variables` y un resumen de cambios cuantitativo, que en MyClone no se observan.
El riesgo que el propio plan no cierra: cada tabla y endpoint nuevo vuelve a duplicarse entre SQLAlchemy y Drizzle (ver [[2026-1022-drift-schema-drizzle-sqlalchemy]]), y el snapshot completo duplica el texto del prompt en cada versión.
