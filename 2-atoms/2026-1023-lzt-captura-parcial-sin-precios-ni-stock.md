---
id: 2026-1023-lzt-captura-parcial-sin-precios-ni-stock
type: atom
certainty: solid
sources: [sources/2026-10-22-lzt-market-home.md]
links: ["[[2026-1022-guardarrail-no-alucinar]]", "[[2026-1023-5sim-catalogo-servicios-precios-y-stock]]", "[[2026-1023-lzt-categorias-gaming-y-social-network]]"]
---

## Claim
La captura de la home de lzt.market (2026-10-22) es un **render parcial de una SPA**: conserva el aviso de cookies, el banner del nuevo método de pago, un bloque de error literal del sitio ("Something went wrong... The requested page could not be found.") y **dos marcadores "Загрузка..." (Loading)** —uno al principio del documento y otro entre el bloque de categorías y las listas de venta— y al mismo tiempo **no contiene ningún precio, ningún contador de stock, ninguna ficha de cuenta ni ningún número de artículos**. Lo que sí queda es la estructura de navegación: 22 categorías de compra, 23 de venta individual y 19 de carga masiva. Por tanto, ninguna afirmación sobre lo que lzt.market vende en términos de precio, stock o calidad de cuenta está soportada por esta fuente; lo único soportado es la forma del catálogo.

## Why It Matters
Es la diferencia entre una fuente de precios y una fuente de estructura: el mismo corpus que sí trae CSV de precios y stock para 5sim ([[2026-1023-5sim-catalogo-servicios-precios-y-stock]]) aquí no trae ni un número. Cualquier lectura del vault sobre lzt.market como proveedor de identidades verificadas tiene que apoyarse en un re-fetch con renderizado JS, no en esta captura; tomarla como fuente de precio sería exactamente el hueco que el guardarrail del producto evita ([[2026-1022-guardarrail-no-alucinar]]). Lo que sí se puede usar es el esqueleto del catálogo ([[2026-1023-lzt-categorias-gaming-y-social-network]]).

## Nota de verificación
El bloque de error y los dos "Загрузка..." están transcritos literalmente de la captura. La captura **no** publica: precios unitarios, stock, número de listings, tipos de cuenta, garantía ni plazos de entrega.
