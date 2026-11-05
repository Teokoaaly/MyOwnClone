---
id: 2026-1026-5sim-home-en-sin-widget-ni-contadores-de-stock
type: atom
certainty: tentative
sources: [sources/2026-10-25-5sim-home.md, sources/2026-10-22-5sim-home.md]
links: ["[[2026-1023-5sim-catalogo-servicios-precios-y-stock]]", "[[2026-1023-5sim-catalogo-153-paises-contra-180-de-la-home]]", "[[2026-1023-5sim-catalogo-1221-servicios-nombres-unicos]]"]
---

## Claim
La captura del 2026-10-25 de `https://5sim.net/en` (653 palabras) **no contiene ningún selector de compra**: ni los ocho servicios con su "from $" y su contador de stock, ni los botones `Show all 1329` / `Show all 153`, ni el pie con "Prices / Statistics / Contacts / Services / Guides / Countries", ni "FAQ / How to buy?", ni el aviso "© 2016-2026 5sim.net". Lo que sí trae es la **copy de marketing completa** (los cinco bloques de boasts, los cinco casos de uso, el flujo de tres pasos, las cinco razones de "Why 5SIM beats other SMS verification services") más las **cinco imágenes hero** con sus `alt` y cinco enlaces sociales al pie. En total, **la única cifra cuantitativa de toda la página es `$0.008`**. La captura del 2026-10-22 de `https://5sim.net/` (563 palabras) sí traía el bloque completo del selector con los ocho servicios, los ocho contadores (64 M–162 M de unidades) y los dos botones de exhaustividad.

## Why It Matters
Separa de forma limpia **qué es la página de marketing y qué es el dato**: los 500.000 números, los 180 países y el $0.008 son texto; los precios por par país-operador, los contadores de stock y los recuentos de cobertura viven en un **widget aparte**, que es exactamente el componente que el vault ya identificó como renderizado en servidor y replicado byte a byte en tres URLs ([[2026-1023-5sim-catalogo-servicios-precios-y-stock]]). Es decir: **la única página que un humano lee como "la web de 5sim" no tiene ni un solo dato de inventario**, y la única que los tiene no los tiene con contexto.
Además explica por qué los conteos del vault no cuadran entre sí: `1329` servicios, `153` países, `111` países en el CSV, `76` países en la ficha de OpenAI y "180" en la prosa ([[2026-1023-5sim-catalogo-153-paises-contra-180-de-la-home]], [[2026-1023-5sim-catalogo-1221-servicios-nombres-unicos]]) son **cifras de cinco superficies distintas del mismo sitio**, no cinco estimaciones de un mismo inventario.

## [FRICTION]
> [[2026-1023-5sim-catalogo-servicios-precios-y-stock]] (escrita el 2026-10-23, a partir de `sources/2026-10-22-5sim-home.md`) afirma que "**la home de 5sim** ofrece un selector de compra en tres pasos —servicio → país → operador— y expone en el propio selector los precios 'from' y un contador de stock por servicio", y de ahí extrae los ocho precios de escaparate y los ocho contadores.
> Este átomo presiona esa creencia porque **la home de la ruta `/en` no tiene ese selector**: en la captura del 2026-10-25 de `https://5sim.net/en` no hay ni un precio, ni un contador, ni un botón de exhaustividad, y la única cifra es el claim de $0.008.
> Ambas no pueden ser completamente correctas: o las dos rutas (`/` y `/en`) sirven páginas distintas —una con widget y otra sin él—, o la diferencia es del método de captura y no del sitio, y entonces el "widget compartido renderizado en servidor" que el vault da por probado en tres URLs se explica en parte por el scraping, no por la arquitectura. Marcado para juicio humano, no auto-resuelto: esta captura no permite distinguir entre las dos hipótesis —no hay indicación en el documento de la ruta servida más allá de la URL de la captura.
