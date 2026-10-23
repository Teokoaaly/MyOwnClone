---
id: 2026-1023-5sim-tabla-visible-ordenada-por-descuento-no-por-precio
type: atom
certainty: solid
sources: [sources/2026-10-22-5sim-prices.md]
links: ["[[2026-1023-5sim-piso-de-precio-telegram-01026-usd]]", "[[2026-1023-5sim-paises-no-occidentales-mas-baratos]]", "[[2026-1023-5sim-stock-abundante-no-implica-precio-bajo]]"]
---

## Claim
La tabla que la página de precios de 5sim renderiza en HTML ("In stock", con cabeceras `Service | Country | Operator | (sin título) | Pcs | Price`) muestra **solo 20 filas**, y esas 20 filas son exactamente las primeras 20 del CSV embebido, que está **ordenado por la columna `rate` (porcentaje) de forma descendente**, no por precio: Lituania `virtual34` 58.33% $0.5769, Portugal `virtual51` 57.58% $2, Inglaterra `virtual34` 34.15% $1.3, Polonia `virtual66` 29.03% $2, Inglaterra `virtual51` 26.44% $1.05, … hasta Francia `virtual66` 17.14% $2.5. El dataset completo son **175 filas / 111 países**, y las 20 filas visibles son precisamente las de `rate` positivo (las 41 filas con `rate = -1.0` quedan fuera de la vista). La columna de porcentaje aparece en el HTML renderizado **sin cabecera** (vacía entre `Operator` y `Pcs`).

## Why It Matters
Quien lea solo la tabla visible concluirá que el precio de 5sim empieza en $0.5769 (Lituania) o $2 (Portugal) cuando el dataset real contiene **Colombia a $0.1026** — 5,6 veces más barato. La página no es un catálogo ordenado por coste: es un escaparate de *descuento*, y la variable `rate` es la que ordena. Cualquier aritmética de coste hecha sobre lo que se ve en pantalla (y no sobre el CSV embebido, que es lo que hay que decodificar del `data:text/csv` del enlace) parte de un mínimo falso. Ver [[2026-1023-5sim-piso-de-precio-telegram-01026-usd]] para el mínimo real y [[2026-1023-5sim-paises-no-occidentales-mas-baratos]] para la geografía que la tabla visible no muestra.
