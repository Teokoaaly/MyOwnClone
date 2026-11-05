---
id: 2026-1103-auth0-precios-35-y-240-bajo-el-encabezado-b2b-billing
type: atom
certainty: tentative
sources: [sources/2026-11-03-auth0-pricing.md]
links: ["[[2026-1101-auth0-b2b-essentials-escala-por-mau]]", "[[2026-1101-auth0-b2c-essentials-escala-por-mau]]", "[[2026-1103-auth0-captura-reducida-sin-tablas-ni-feature-matrix]]", "[[2026-1102-auth0-precios-sin-cambios-en-48-horas]]"]
---

## Claim
La captura del 2026-11-03 muestra el selector "**B2B BILLING**" activo (después de la pregunta "WHAT IS YOUR USE CASE?") y el escalón de MAU "500", pero los importes que imprime son **Essentials $35/mes** ("Up to 500 monthly active users") y **Professional $240/mes** ("Up to 500 monthly active users") — los mismos importes que el 2026-11-01 atribuía a B2C, mientras que B2B costaba $150 y $800.

## Why It Matters
Con tres capturas de la misma URL ya no se puede afirmar que "la página de precios de Auth0" tenga un único conjunto de cifras: **lo que se renderiza depende de un selector interactivo** que la captura textual no captura de forma fiable. Para el vault esto importa porque la escalera de coste que se está construyendo ([[2026-1101-auth0-precios-por-mau-no-por-evento]]) se apoya en cifras tomadas de renders concretos, y este render es el primero que contradice su propio encabezado. Dos lecturas posibles —y ambas pueden ser ciertas a la vez—: (a) el texto plano del extractor no distingue columnas B2C/B2B y el encabezado "B2B BILLING" es solo una etiqueta del toggle que quedó pegada al contenido B2C; (b) Auth0 cambió la cifra de entrada de B2B. Ninguna se puede resolver desde el texto, de ahí `tentative`. La consecuencia práctica: **ningún precio de Auth0 debe fijarse en un presupuesto sin re-verificar contra una captura de la tabla completa** (ver [[2026-1103-auth0-captura-reducida-sin-tablas-ni-feature-matrix]]).

## [FRICTION]
> [[2026-1101-auth0-b2b-essentials-escala-por-mau]] (escrita el 2026-11-01) afirma, leído de las tablas "B2B Base Price by MAUs": "Auth0 Essentials **B2B** cuesta **$150/mes en 500 MAU** (vs $35 en B2C) […] Professional B2B parte de **$800/mes** en 500 MAU".
> Este átomo presiona eso porque la captura del 2026-11-03, bajo un encabezado que dice literalmente "B2B BILLING", imprime $35 y $240 — no $150 y $800.
> Ambas no pueden ser completamente correctas: o el render del 2026-11-03 no está en modo B2B (y el encabezado es un artefacto de la extracción), o la tabla B2B del 2026-11-01 se leyó sobre la columna equivocada. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
Encabezado "B2B BILLING", escalón "500" y los importes $35 / $240 son lectura literal de `sources/2026-11-03-auth0-pricing.md`. La explicación del artefacto de render es hipótesis de este átomo, no texto de la fuente.
