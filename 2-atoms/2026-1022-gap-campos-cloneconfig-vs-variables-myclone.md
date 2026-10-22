---
id: 2026-1022-gap-campos-cloneconfig-vs-variables-myclone
type: atom
certainty: solid
sources: [raw/articles/myownclone-osint-implementation-handoff-2026-06-24.md]
links: ["[[2026-1022-myclone-prompt-template-sistema]]", "[[2026-1022-myownclone-dos-repos-flask-nextjs]]", "[[2026-1022-arquitectura-rac-tres-modos-por-clon]]"]
---
## Claim
El handoff cuantifica el gap de modelo de datos entre ambos: MyClone.is parametriza sus personas con 10 variables (`name`, `role`, `company`, `description`, `introduction`, `area_of_expertise`, `chat_objective`, `thinking_style`, `objective_response`, `example_responses`), mientras que `CloneConfig` de [[myownclone]] solo tiene `name`, `description`, `personality_tone` y `language`. **Faltan `role`, `company`, `introduction`, `area_of_expertise` y `chat_objective`** como campos separados; `personality_tone` es el equivalente más cercano de `thinking_style` y `language` es una ventaja propia que MyClone no tiene.

## Why It Matters
El bloqueo no es el prompt: es que la identidad del clon vive en un prompt monolítico mientras que MyClone la tiene **estructurada en campos** ([[2026-1022-myclone-prompt-template-sistema]]). Sin `role`/`company`/`area_of_expertise` no se puede generar una plantilla con parámetros ni versionarla por variables — que es el diseño que hace posible el versionado con `prompt_variables` y el diff granular.
El handoff recomienda explícitamente **no** copiar el prompt de MyClone tal cual sino adaptar sus variables a los campos existentes de `CloneConfig`; esto es una decisión de scope: replicar el esquema completo (5 campos nuevos) es más caro que el versionado que se quiere construir, y el handoff pone el versionado por encima de las variables.
`language` como campo propio es la única ventaja de modelo de datos que MyOwnClone tiene sobre MyClone: [[2026-1022-arquitectura-rac-tres-modos-por-clon]] ya define [[myownclone]] como producto ES-first (ver [[2026-1022-i18n-es-first-jurisdiccion-es]]).
