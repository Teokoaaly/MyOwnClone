# House Rules — Léete esto antes de cualquier acción

## El Pipeline
- **0-raw/** : Capturas crudas. SOLO LECTURA. Nunca editar una captura cruda.
- **0-raw/archive/** : Capturas ya procesadas, movidas aquí por el Refinery.
- **1-desk/** : Espacio de trabajo temporal. Limpiar al final de cada turno.
- **2-atoms/** : Notas atómicas permanentes. Una idea por archivo. Núcleo del vault.
- **2-atoms/archive/** : Notas marcadas [RETIRED]. No se borra nada.
- **3-threads/** : Documentos de síntesis. Actualizar el thread relevante; no duplicar.
- **sources/** : Fuentes originales (artículos completos). SOLO LECTURA. Nunca modificar.
- **briefings/** : Briefings diarios y auditorías. Aquí se escribe de vuelta al humano.

## Directiva Principal
Toda nota atómica DEBE trazar a una fuente real en `sources/` o `0-raw/`.
Sin fuente no hay nota. No puedes escribir una afirmación que no esté en el material.
No rellenas huecos con información que suene plausible. Jamás.

## Reglas de Trabajo
1. Una idea por átomo. Si una fuente tiene 8 ideas, crea 8 átomos.
2. Antes de crear un átomo, busca en `2-atoms/` si ya existe uno para extender.
3. Cada átomo enlaza al menos a otros 2 átomos relacionados con `[[wikilink]]`.
4. Cuando un átomo nuevo contradice uno existente, añade un bloque `## [FRICTION]` al nuevo apuntando al viejo. Nunca sobrescribas silenciosamente una creencia previa.
5. Nunca borres. Marca las notas superadas como `[RETIRED]` y muévelas a `2-atoms/archive/`.
6. Termina cada turno actualizando el thread relevante en `3-threads/` y escribiendo un briefing.

## Autoridad
- Solo puedes escribir en: `1-desk/`, `2-atoms/`, `3-threads/`, `briefings/`.
- Cualquier acción destructiva o ambigua: **para y pregunta al humano**. No adivines.

## Formato de Átomo
```markdown
---
id: YYYY-MMDD-slug
type: atom
certainty: tentative | solid | retired
sources: [sources/YYYY-MM-DD-filename.md]
links: ["[[nota-1]]", "[[nota-2]]"]
---

## Claim
(Una afirmación clara, una sola idea)

## Why It Matters
(Por qué esta idea es relevante en el contexto del vault)

## [FRICTION] (opcional, solo si hay conflicto)
> [[nota-conflictiva]] (escrita hace X semanas) afirma Y. Esta nota presiona eso porque Z.
> Ambas no pueden ser completamente correctas. Marcado para juicio humano, no auto-resuelto.
```
