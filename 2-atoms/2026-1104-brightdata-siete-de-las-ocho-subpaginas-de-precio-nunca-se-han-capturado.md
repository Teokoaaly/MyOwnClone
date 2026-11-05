---
id: 2026-1104-brightdata-siete-de-las-ocho-subpaginas-de-precio-nunca-se-han-capturado
type: atom
certainty: solid
sources: [sources/2026-11-04-brightdata-pricing.md]
links: ["[[2026-1101-brightdata-el-hub-de-precios-no-publica-ninguna-cifra]]", "[[2026-1024-brightdata-precios-por-ip-dos-tablas-sin-etiquetar]]", "[[2026-1024-brightdata-escalera-de-volumen-141-a-798-gb]]"]
---

## Claim
La captura del 2026-11-04 publica los **ocho enlaces "See Pricing"** del hub con su URL completa y estable: `/pricing/proxy-network`, `/pricing/web-scraper`, `/pricing/web-scraper/studio`, `/pricing/scraping-browser`, `/pricing/serp`, `/pricing/web-unlocker`, `/pricing/datasets` y `/pricing/insights`. En todo el corpus de `sources/` **solo una de esas ocho subpáginas ha sido capturada alguna vez**: `/pricing/proxy-network`, el 2026-10-24. Las otras siete —incluidas `/pricing/web-scraper`, `/pricing/scraping-browser` y `/pricing/web-scraper/studio`, las que el Scout señala como las que contienen los precios— **no tienen ninguna captura en el vault**. La lista de lectura (`0-raw/reading-list.md`) apunta al hub, no a las subpáginas.

## Why It Matters
Este es el coste real de la repetición, medido en URLs y no en palabras. Cuatro capturas de `brightdata.com/pricing` (10-31, 11-01, 11-02, 11-04) han producido un índice idéntico sin una sola cifra, mientras que **la tabla de precios que el vault necesita vive en subpáginas que nadie ha visitado** — y las cifras que sí están atomizadas ($4/GB PAYG, el compromiso de $499, la escalera 141→798 GB) vienen de esa única subpágina capturada hace [[2026-1024-brightdata-precios-por-ip-dos-tablas-sin-etiquetar]] y [[2026-1024-brightdata-escalera-de-volumen-141-a-798-gb]], no del hub que se sigue recapturando.
Para el agregador de precios como producto ([[2026-1101-brightdata-el-hub-de-precios-no-publica-ninguna-cifra]]) esto fija la unidad de decisión: **la decisión de rotación de la lista de lectura no se puede tomar por slug, sino por "donde vive el número"**. Y la corrección es barata: sustituir `https://brightdata.com/pricing` por las ocho subpáginas cuesta ocho capturas y produce ocho filas cotizables; mantenerlo produce una por noche y produce cero.
También explica por qué el corpus Bright Data tiene más de 50 átomos y aun así su precio sigue siendo "no publicado": la densidad de átomos de este proveedor mide la profundidad del análisis de sus cuatro fuentes, no la cobertura de su catálogo. **Un proveedor con muchos átomos y sin subpáginas capturadas es un proveedor cuyo precio se está suponiendo, no midiendo.**

## Nota de verificación
Verificado por `grep "^url:"` sobre `sources/*brightdata*`: solo cuatro fuentes del proveedor — `/pricing` (10-31, 11-01, 11-02, 11-04), `/pricing/proxy-network` (10-24), `brightdata.com/faq` (10-25) y la página de free tier de las docs (10-25). Los ocho enlaces "See Pricing" del 11-04 tienen href en markdown (8 de 8), a diferencia de la captura del 10-31, donde el mismo texto aparece sin URL. La captura **no** publica: el precio de ninguna de las ocho subpáginas, ni si alguna de ellas publica precio sin registro, ni la fecha de vigencia de la tabla de `/pricing/proxy-network` capturada el 10-24.
