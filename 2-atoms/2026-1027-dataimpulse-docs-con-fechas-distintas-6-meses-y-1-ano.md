---
id: 2026-1027-dataimpulse-docs-con-fechas-distintas-6-meses-y-1-ano
type: atom
certainty: solid
sources: [sources/2026-10-26-dataimpulse-docs-home.md, sources/2026-10-26-dataimpulse-docs-proxies-index.md, sources/2026-10-26-dataimpulse-docs-types-of-connections.md]
links: ["[[2026-1027-dataimpulse-intervalo-rotacion-sticky-configurable-1-a-120-minutos]]", "[[2026-1024-dataimpulse-sesiones-rotating-y-sticky]]", "[[2026-1024-dataimpulse-gateway-unico-y-protocolos]]", "[[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]"]
---

## Claim
Las tres páginas de documentación capturadas **publican su propia fecha de última actualización, y no es la misma**: la home de la docs dice **"Last updated 6 months ago"**; el índice de proxies y la página *Types of connections* dicen **"Last updated 1 year ago"**. Es decir, la página que contiene las especificaciones técnicas (puertos 823/824, sticky 10000–20000, intervalo 1–120 min) es **la más antigua de las tres**, un año más antigua que la home de la misma documentación. Capturadas el **2026-10-26**, esas especificaciones describen, por declaración del propio proveedor, un producto **anterior en ~12 meses** a la última vez que se tocó la home de la documentación, y anterior también a las landings de producto del 2026-10-23 y del 2026-10-26.

## Why It Matters
Es la **salvedad metodológica** que hay que arrastrar a cada cifra nueva de esta tanda, y el corpus del vault no la tenía: el thread fecha las capturas, pero no fecha las **páginas** que las capturas transcriben. Aquí el propio proveedor fecha las suyas, y la jerarquía es unfavorable al dato más útil: lo que se acaba de aprender —puertos, rango sticky, intervalo configurable ([[2026-1027-dataimpulse-intervalo-rotacion-sticky-configurable-1-a-120-minutos]])— viene de la página marcada como **más antigua**.
La consecuencia práctica es de **vigencia**, no de exactitud**: si la página de *Types of connections* no se toca desde hace un año, entonces sus cifras describen el producto de hace un año, y el corpus del vault tiene **dos capas de precio y contrato con fechas distintas** —la home y las landings, con cifras de 2026-10, y las docs, con cifras de 2025-10— que el vault estaba tratando como un solo proveedor homogéneo ([[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]], [[2026-1024-dataimpulse-gateway-unico-y-protocolos]]). Es también la explicación más económica de por qué el intervalo sticky de la home ("30-120 minutes on average") y el de las docs ("1 to 120 minutes, average 30") **no coinciden sin contradecirse**: pueden ser dos versiones del mismo parámetro separadas por un año de evolución del producto ([[2026-1024-dataimpulse-sesiones-rotating-y-sticky]]).
Para el criterio del vault esto fija un umbral de confianza explícito: **una cifra que solo aparece en la documentación de DataImpulse debe citarse con "según docs, página sin actualizar desde hace un año"**, igual que las claims de home se citan como claim y no como medición. Y ofrece un método reutilizable: **cualquier captura de docs que traiga el pie "Last updated" debe conservarlo como metadato**, porque es la única señal gratuita de vigencia que publica el proveedor.

## Nota de verificación
Los tres pies "Last updated" están transcritos literalmente de las tres fuentes. La captura **no** publica: la fecha absoluta de la última actualización de cada página, ni si el `llms.txt` y los espejos `.md` se regeneran aunque la página no cambie.
