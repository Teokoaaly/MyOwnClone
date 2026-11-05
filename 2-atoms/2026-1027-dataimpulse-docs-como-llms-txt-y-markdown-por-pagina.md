---
id: 2026-1027-dataimpulse-docs-como-llms-txt-y-markdown-por-pagina
type: atom
certainty: solid
sources: [sources/2026-10-26-dataimpulse-docs-home.md, sources/2026-10-26-dataimpulse-docs-proxies-index.md, sources/2026-10-26-dataimpulse-docs-types-of-connections.md]
links: ["[[2026-1026-brightdata-llms-txt-como-indice-de-documentacion-para-agentes]]", "[[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]", "[[2026-1024-dataimpulse-uso-de-ips-en-agentes-y-visibilidad-en-ia]]"]
---

## Claim
La documentación de DataImpulse se publica **en dos formatos mecánicos, no solo en HTML**: en las tres páginas capturadas, la primera línea es literalmente *"For the complete documentation index, see [llms.txt](https://docs.dataimpulse.com/llms.txt). This page is also available as [Markdown](https://docs.dataimpulse.com/readme.md)."*, y el patrón se repite con la URL específica de cada página (`/proxies.md`, `/proxies/types-of-connections.md`). Es decir: **cada página de docs tiene un espejo `.md` y el conjunto tiene un índice `llms.txt`**, que es el formato de descubrimiento que el vault ya tenía registrado para Bright Data ([[2026-1026-brightdata-llms-txt-como-indice-de-documentacion-para-agentes]]).

## Why It Matters
Es el **segundo proveedor del corpus** que publica su documentación como superficie legible por máquina, y eso convierte `llms.txt` de una curiosidad de un proveedor a un **estándar de facto del sector**. El vault ya tiene la lectura de riesgo de ese formato —un índice que un agente consume para decidir qué páginas leer es un canal de inyección con los mismos privilegios que la documentación que señale ([[2026-1026-brightdata-llms-txt-como-indice-de-documentacion-para-agentes]])—; ahora el hallazgo es que **un proveedor de proxies publica el mismo formato**, lo que significa que la superficie es alcanzable por el mismo lector que consume los datos ([[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]).
La segunda mitad del dato es la que tiene valor para el vault: **el espejo `.md` por página convierte la documentación técnica en un corpus extraíble**. Las tres capturas de esta tanda —puertos, intervalo de rotación y sticky port-based— no se podían obtener de la home ni de las landings de producto: solo existen en la documentación, y su versión `.md` es la que las hace legibles de forma estable y sin render. Es decir, el propio formato que el proveedor publica para los agentes es **la vía por la que el vault puede auditar sus cifras**: cada afirmación de las páginas de docs es ahora comprobable contra un texto plano con fecha de captura, no contra una página que puede cambiar en cualquier momento.

## Nota de verificación
Textos transcritos literalmente de las tres fuentes. La captura **no** publica: el contenido del `llms.txt`, el número de páginas del índice, ni si los espejos `.md` y las páginas HTML se regeneran a la vez.
