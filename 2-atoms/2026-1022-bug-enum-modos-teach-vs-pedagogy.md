---
id: 2026-1022-bug-enum-modos-teach-vs-pedagogy
type: atom
certainty: solid
sources: [raw/articles/myownclone-osint-implementation-handoff-2026-06-24.md]
links: ["[[2026-1022-arquitectura-rac-tres-modos-por-clon]]", "[[2026-1022-drift-schema-drizzle-sqlalchemy]]", "[[2026-1022-tres-silos-opt-in-publico]]"]
---
## Claim
El enum de modos de clon está definido **con nombres distintos en cada capa** de [[myownclone]]: el backend Flask declara `CloneSilo.TEACH = "teach"`, `SUPPORT`, `SALES`, y el enum de Postgres/Drizzle declara `pgEnum("clone_mode", ["pedagogy", "support", "sales"])`. Cualquier sincronización requiere un mapa explícito de conversión `{"teach": "pedagogy", "pedagogy": "teach", ...}` y una migración de datos (`UPDATE clone_mode_prompts SET mode='teach' WHERE mode='pedagogy'`). El fix propuesto en el handoff es alinear Drizzle a `"teach"`, no al revés.

## Why It Matters
El modo pedagógico es el corazón del producto: [[2026-1022-arquitectura-rac-tres-modos-por-clon]] lo sitúa como uno de los tres modelos por clon (aprendizaje, soporte, ventas) que el founder considera la diferencia frente a [[delphi]], y [[2026-1022-tres-silos-opt-in-publico]] lo confirma como silo opt-in del copy público. Que el identificador del modo tenga dos nombres según la capa es deuda en el eje más crítico del producto: cualquier consulta, filtro o etiqueta que cruce backend y frontend puede devolver cero filas o mostrar el modo vacío sin error.
La decisión de qué lado manda importa: alinear a `"teach"` (Flask, que es el que corre el chat real) evita tener que tocar el pipeline de chat y el enum público del clon, que es lo que usa el slug y los retrievals.
