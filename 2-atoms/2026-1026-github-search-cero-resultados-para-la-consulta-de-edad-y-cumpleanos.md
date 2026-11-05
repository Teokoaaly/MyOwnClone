---
id: 2026-1026-github-search-cero-resultados-para-la-consulta-de-edad-y-cumpleanos
type: atom
certainty: solid
sources: [sources/2026-10-25-github-search-chatgpt-age-verification.md]
links: ["[[2026-1024-github-search-catorce-resultados-y-el-universo-indexado-de-la-consulta]]", "[[2026-1024-github-search-tres-de-catorce-son-falsos-positivos-de-la-consulta]]", "[[2026-1024-github-search-el-tercer-puesto-no-es-describible-desde-el-json]]"]
---

## Claim
La consulta `GET /search/repositories?q=chatgpt+signup+api+birthday+age+verification` devuelve una respuesta **vacía y completa**: `total_count: 0`, `incomplete_results: false` y `items: []`. No hay ni un repositorio —ni con estrellas, ni sin ellas— que GitHub indexe bajo esa conjunción de seis términos. La captura del 2026-10-25 es, por tanto, la **primera medición del vault de un cero** en la API de búsqueda de repositorios: 6 palabras de origen en el frontmatter, 9 líneas de fuente y **ningún objeto que describir**.

## Why It Matters
El vault ya tiene nueve átomos sobre una consulta sister de esta —`chatgpt account creator`, 14 resultados, 810 estrellas, 308 forks, tres repositorios con comunidad ([[2026-1024-github-search-catorce-resultados-y-el-universo-indexado-de-la-consulta]], [[2026-1024-github-search-noventa-y-cuatro-por-ciento-de-las-estrellas-en-tres-repos]])— y esa captura es siempre la lectura "el corpus tiene 14". Este cero cambia el **status epistémico del dato de tamaño**: 14 no era "el tamaño del corpus abierto", era el tamaño de un índice **para una frase concreta**, y una frase igualmente plausible sobre el mismo tema devuelve **nada**. La línea de fondo que queda es uncomfortable y útil a la vez: **la tooling pública de registro de cuentas de ChatGPT está concentrada en repositorios que se llaman "account creator"**, no en repositorios que se describan por sus funciones internas (signup por API, verificación de edad), porque esos últimos no existen en el índice con esos nombres.
El otro valor del cero es que **es una respuesta completa, no un fallo**: `incomplete_results: false` con `items: []` significa que GitHub terminó de indexar y no encontró coincidencias. No es un timeout ni una página vacía por límite de `per_page`. El dato es utilizable como medición, que es lo que lo distingue de una captura fallida.

## [FRICTION]
> [[2026-1024-github-search-catorce-resultados-y-el-universo-indexado-de-la-consulta]] (escrita el 2026-10-24) afirma que "el conjunto indexado por GitHub para esa frase es, por tanto, **entero y cerrado en 14 repositorios**" y en su *Why It Matters* lo lee como "la oferta abierta de herramientas de registro masivo de cuentas de ChatGPT en GitHub es **muy pequeña** —catorce repositorios".
> Este átomo presiona esa lectura en un punto: con una segunda consulta sobre el mismo tema, formulada en términos de función (`chatgpt signup api birthday age verification`) en vez de de nombre de producto (`chatgpt account creator`), el índice devuelve **cero**. Las dos afirmaciones no pueden describir ambas "el corpus público de herramientas de registro de ChatGPT": o 14 es el tamaño del corpus (y entonces esta consulta debería devolver algo), o el tamaño del corpus **depende de la formulación de la consulta** y 14 mide una coincidencia de nombres, no un censo. El propio átomo viejo ya lo advertía ("14 es el tamaño del índice **para esa consulta concreta**"), y esta captura es la que convierte esa advertencia en una medición. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
Cifras leídas literalmente del JSON capturado el 2026-10-25 (`total_count`, `incomplete_results`, `items`). El vault **no ha ejecutado ninguna consulta de búsqueda adicional**, ni en GitHub ni en ningún motor, ni ha clonado ni visitado repositorios: el cero es el de esa consulta y de ese día. El JSON **no dice qué campo se empareja** (nombre, descripción, topics o README) ni **cómo se combinan los seis términos**, de modo que el cero significa estrictamente "ningún repositorio coincidió con esta conjunción", no "no existe ningún repositorio que hable de verificación de edad".
