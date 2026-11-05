---
type: desk-note
date: 2026-11-05
role: refinery-shared-context
---

# Contexto compartido del Refinery — 2026-11-05 (run 03:00)

Vault: `/home/haxth3/wiki`. Esta nota la leen TODOS los subagentes de este turno. No la modifiques.

## Contexto general (léelo antes de nada)

Este es el **quinto turno consecutivo** en que el Scout recaptura las mismas 15 URLs (lista de lectura sin rotar desde 2026-10-29). Las capturas del `2026-11-04` son la **quinta** captura de cada slug. La mayor parte del contenido ya está atomizada en `2-atoms/` con prefijos `2026-1024`, `2026-1026`, `2026-1031`, `2026-1101`, `2026-1102`, `2026-1103`.

**Consecuencia obligatoria:** NO generes átomos que repitan lo ya dicho. Un átomo nuevo debe aportar **una de estas cosas**:

1. **Novedad real**: una afirmación, cifra o contradicción que aparece en la captura del 2026-11-04 y no en las anteriores.
2. **Delta de captura**: la captura del 11-04 renderiza una sección que las anteriores no renderizaban (o al revés). El vault ya tiene átomos con este patrón (ej. `2026-1103-assemblyai-captura-reducida-solo-pre-recorded-expandido`, `2026-1103-tailscale-cuarta-captura-del-kb-sin-frase-zero-trust-ni-urls`).
3. **Confirmación de estabilidad**: la misma cifra aparece por quinta vez → átomo de estabilidad (patrón existente: `2026-1103-backblaze-b2-precios-estables-en-cuatro-capturas-consecutivas`, `2026-1103-deepgram-precios-estables-en-cuatro-capturas-consecutivas`).
4. **Contradicción / fricción**: la captura nueva contradice un átomo viejo, o dos secciones de la misma página se contradicen.

Si una idea de la fuente ya está cubierta por un átomo existente, **no crees un átomo nuevo**: enlázala desde el átomo nuevo más cercano o menciónala en "Why It Matters". Truco: busca en `2-atoms/` con `search_files` por slug **y** por palabras clave del dato antes de escribir nada.

**Objetivo de volumen:** entre 3 y 7 átomos nuevos por captura. Si crees más, estás duplicando. Si no puedes encontrar nada nuevo, crea 1 átomo de estabilidad o de "captura sin novedad" — eso también es un resultado válido y honesto.

## House Rules (texto íntegro — aplica TODO)

```
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

## Convenciones de esta tanda

- **Prefijo de átomo: `2026-1104-`** (la fecha de la captura, no la del run). Ejemplo: `2-atoms/2026-1104-hetzner-captura-sin-cambio-de-precio.md`.
- **frontmatter `id:`** = mismo slug que el nombre de fichero, sin `.md`.
- **`sources:`** = `[sources/2026-11-04-<slug>.md]` (el slug exacto que te paso en tu tarea).
- **`links:`** = lista de strings con el **nombre completo del fichero** de otro átomo, incluyendo su prefijo de fecha: `"[[2026-1103-backblaze-b2-precios-estables-en-cuatro-capturas-consecutivas]]"`. Mínimo 2 links reales (verifica que el fichero existe).
- **`certainty`**: `solid` si el dato se repite en 2+ capturas o es una cifra literal inequívoca; `tentative` si es una afirmación única, un claim de marketing, o un dato de una sola captura no corroborada.
- **Cifras**: transcribe literalmente. No conviertas unidades, no apliques IVA, no normalices $/TB vs $/GB sin decirlo explícitamente. Si comparas dos proveedores, deja claro que son magnitudes distintas.
- **Distinción medición/claim**: si el texto dice "Save up to 20%", es un claim del proveedor, no un hecho verificado. Cítalo entre comillas.
- **Absencia de dato ≠ retirada**: si un render pierde una sección, no escribas "el precio X ha desaparecido". Escribe "esta captura no lo renderiza".
- **Escritura**: usa `write_file` con la ruta ABSOLUTA `/home/haxth3/wiki/2-atoms/<nombre>.md`. No uses `cat >` ni heredocs.

## Prohibiciones (duro)

- No modifiques `sources/`. No modifiques `0-raw/` (solo mover el fichero de captura al archivar).
- No modifiques átomos existentes, salvo **extensión** permitida: puedes añadir una sección `## Actualización 2026-11-04` al FINAL de un átomo viejo SOLO si (a) es un átomo del mismo slug que tú procesas, (b) la extensión es puramente aditiva (nueva captura corrobora o matiza), y (c) NO lo mueves a `2-atoms/archive/` ni cambias su `certainty`. En ese caso repórtalo en `ATOMS_EXTENDED`. Nunca reescribas el `## Claim` de un átomo viejo: la contradicción va en el átomo nuevo.
- No crees ficheros en `3-threads/` ni en `briefings/` (eso lo hace el orquestador).
- No crees ficheros en `1-desk/` salvo que necesites un borrador temporal (bórralo antes de terminar).
- No borres nada. No muevas átomos a `2-atoms/archive/` salvo que el átomo esté **literalmente** superado — y en ese caso, consérvalo, no lo borres. Ante la duda, no lo muevas: Márcalo y repórtalo.
- No inventes cifras, fechas, condiciones ni nombres de producto. Si no está en el texto, no está.

## Movimiento de la captura (último paso)

Cuando hayas terminado todos los átomos de tu captura:

```
mv /home/haxth3/wiki/0-raw/2026-11-04-<slug>.md /home/haxth3/wiki/0-raw/archive/2026-11-05-2026-11-04-<slug>.md
```

(si ya existe un destino con ese nombre, añade sufijo `-2`, `-3`… y repórtalo).

## Formato del informe de retorno (obligatorio, exacto)

```
CAPTURE: 2026-11-04-<slug>.md
SOURCE: sources/2026-11-04-<slug>.md
PREV_CAPTURE: sources/<fecha>-<slug>.md
ATOMS_CREATED: <n> (lista de rutas 2-atoms/...)
ATOMS_EXTENDED: <n> (lista de rutas, o "0")
FRICTIONS_RAISED: <n> (lista de pares "nuevo -> viejo")
NOTES: <una línea sobre lo que aporta esta captura frente a la anterior>
ERRORS: <ninguno | descripción>
```
