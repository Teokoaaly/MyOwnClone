---
id: 2026-1026-serverhunter-stock-desconocido-en-la-fila-mas-barata
type: atom
certainty: solid
sources: [sources/2026-10-25-serverhunter-cheap-vps.md]
links: ["[[2026-1023-priceai-channels-53-productos-y-minimo-con-stock]]", "[[2026-1024-extravm-stock-casi-todo-agotado-y-solo-cinco-planes-comprables]]", "[[2026-1026-serverhunter-suelo-de-029-con-128-mb-y-ipv4-nat]]"]
---

## Claim
La tabla de ServerHunter tiene una columna **Stock** con **dos estados reales más una categoría aparte**, sobre **21 filas renderizadas** (20 ofertas + 1 fila de anuncio): **"In stock"** en **13 de las 20 ofertas**, **"Stock unknown"** en **7 ofertas** —las tres `NAT-128` de Gullo's Hosting en **FR, CA y DE**, a $0.29, y las cuatro `NAT-256` de Gullo's Hosting en **FR, FIN, CA y DE**, a $0.33— y la **fila etiquetada "Ad"** de Ignero Corp, que además muestra "In stock". El dato clave para el vault: **tres de las cinco ofertas más baratas de la tabla ($0.29) están en "Stock unknown"**; solo el `NanoVPS-II 384 Low-Cost Special US` de Centerfield Ltd y el `NAT-128 FIN` de Gullo's Hosting están "In stock".

## Why It Matters
Es el problema que PriceAI resolvió por decreto y ServerHunter resuelve por datos: el "mínimo" del mercado **no es comprable por definición**. En PriceAI la regla es explícita —*主价格优先取有货最低价，缺货会明显标注*— y por eso sus mínimos excluyen lo agotado ([[2026-1023-priceai-channels-53-productos-y-minimo-con-stock]]); en ServerHunter **no hay tal regla**, el control "Stock" es un filtro que la captura no permite ver aplicado, y el resultado es que **7 de las 20 ofertas visibles —incluidas tres de las cinco más baratas— no tienen stock conocido**. La consecuencia para el vault es la misma que ya registró con ExtraVM —el precio nominal no es el precio comprable ([[2026-1024-extravm-stock-casi-todo-agotado-y-solo-cinco-planes-comprables]])— pero aquí con un detalle que la hace más fuerte: **"Stock unknown" no es "agotado" sino "no se sabe"**, es decir el agregador expone una **incertidumbre de inventario como si fuera un estado de inventario**, y un scraper que solo mira la columna Precio construye su ranking de precios más baratos sobre 20 filas cuyo estado de compra se desconoce en un 35 %.

## [FRICTION]
> [[2026-1023-priceai-channels-53-productos-y-minimo-con-stock]] establece la regla del agregador que publica precio: "el precio principal es el más bajo **con stock**, y el agotamiento se marca de forma visible", y en la tabla una fila sin stock muestra "暂无价格" / "暂无最低渠道".
> ServerHunter ordena por "Lowest price" **sin filtrar por stock**: el precio más bajo de la tabla ($0.29) se repite en cuatro filas con "Stock unknown" y en una con "In stock", de modo que **"lowest price" y "lowest available price" son dos rankings distintos y el sitio solo expone el primero**. Las dos afirmaciones no pueden ser a la vez el criterio de este agregador: o ServerHunter aplica un criterio de stock que la captura no muestra (por ejemplo, un filtro activo que la captura no preserva), o no lo aplica y su mínimo es un precio fantasma.
> Marcado para juicio humano, no auto-resuelto: la captura solo revela el estado "Sort by: Lowest price" y la existencia de un control "Stock" / "Clear all filters" en el panel de filtros; no permite saber si ese filtro estaba aplicado al capturar la tabla.

## Nota de verificación
Los tres estados ("In stock", "Stock unknown", "Ad") y el reparto por fila están transcritos literalmente de las 21 filas renderizadas. La captura no muestra el número total de filas del catálogo de 88.559 ofertas, ni la fuente del campo de stock (feed del proveedor vs. scraping), ni ninguna fecha de actualización de ese campo.
