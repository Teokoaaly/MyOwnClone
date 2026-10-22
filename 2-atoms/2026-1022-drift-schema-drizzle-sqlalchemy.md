---
id: 2026-1022-drift-schema-drizzle-sqlalchemy
type: atom
certainty: solid
sources: [raw/articles/myownclone-osint-implementation-handoff-2026-06-24.md]
links: ["[[2026-1022-myownclone-dos-repos-flask-nextjs]]", "[[2026-1022-bug-enum-modos-teach-vs-pedagogy]]", "[[myownclone]]"]
---
## Claim
El handoff de implementación de [[myownclone]] documenta **cuatro bugs de drift** entre los modelos SQLAlchemy de Flask y los schemas Drizzle del frontend: (1) el enum de modos usa `"teach"` en Flask y `"pedagogy"` en Drizzle; (2) `cloneModePrompts` no tiene `updatedAt` en Drizzle aunque SQLAlchemy sí lo hereda de `TypeBase`; (3) el frontend envía `title` en el POST de memorias pero `MemoryPayload` en Flask no tiene ese campo y `CreatorMemory` tampoco, aunque `memories.title` sí existe en Drizzle — el campo **se pierde en el pipeline**; (4) `memories.updatedAt` existe en Drizzle pero no en el modelo SQLAlchemy `CreatorMemory`.

## Why It Matters
Son fallos de datos, no de estilo: el bug 3 significa que títulos de memoria escritos por el usuario desaparecen sin error visible. El bug 2+4 es la firma de que **nadie es dueño del schema**: cada lado lo define por su cuenta (ver [[2026-1022-myownclone-dos-repos-flask-nextjs]]).
El handoff ordena resolverlos **antes** de añadir features ("Step 4 — Bug Fixes, hacer primero"), lo que conecta directamente con la lección ya registrada en el vault sobre no sobreconstruir ([[2026-1022-error-fase-3-sobreconstruir]]): el coste real de añadir versionado de prompts o workflows sobre schemas inconsistentes es multiplicar el número de campos que hay que mantener sincronizados a mano.
El bug 1 (enum) tiene además un coste de datos ya materializado: requiere `UPDATE clone_mode_prompts SET mode = 'teach' WHERE mode = 'pedagogy'`, es decir, la corrección no es solo de código sino de migración (ver [[2026-1022-bug-enum-modos-teach-vs-pedagogy]]).
