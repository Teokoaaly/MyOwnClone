---
id: 2026-1027-decodo-comparador-propio-de-productos-con-fecha-y-unidad
type: atom
certainty: solid
sources: [sources/2026-10-26-decodo-web-data-api-pricing.md]
links: ["[[2026-1023-priceai-modulo-api-transit-tres-ejes-de-comparacion]]", "[[2026-1024-veridrop-directorio-de-relays-distinto-del-ranking]]", "[[2026-1027-decodo-tablero-de-precios-de-la-home-con-ocho-lineas-y-cinco-unidades]]", "[[2026-1023-priceai-home-como-radar-y-no-como-vendedor]]"]
---

## Claim
La página de precios de la Web Data API de Decodo enlaza, en su propio cuerpo, a **un comparador de productos del propio proveedor**: el bloque "Find the best product match" con el texto *"**Easily compare features and prices in just a few clicks**"* y un CTA "Try now" que apunta a **`decodo.com/compare`**. La home, por su parte, publica el mismo tipo de superficie con las **ocho líneas y cinco unidades** del tablero ([[2026-1027-decodo-tablero-de-precios-de-la-home-con-ocho-lineas-y-cinco-unidades]]).

## Why It Matters
Es un dato estructural sobre el sector que el vault todavía no tenía: **el proveedor de infraestructura de acceso web es también proveedor de la comparación**. Y el mecanismo es el mismo que el que la thread está documentando en el otro extremo del mercado: PriceAI publica un inventario **de precios de terceros** como producto ([[2026-1023-priceai-modulo-api-transit-tres-ejes-de-comparacion]]) y VeriDrop publica un directorio **de relays** ([[2026-1024-veridrop-directorio-de-relays-distinto-del-ranking]]). Decodo publica un inventario **de sus propias ocho líneas de producto**, con sus unidades mezcladas —que es exactamente el problema que hace que un inventario sea útil o no: sin unidad declarada, comparar es imposible ([[2026-1023-priceai-home-como-radar-y-no-como-vendedor]]).

La diferencia con PriceAI y VeriDrop es que **aquí el inventario es de una sola casa** y las unidades **no se normalizan entre sí**: $/1K, $/GB, $/IP y "price on request" conviven en la misma pantalla, con dos líneas sin precio cotizable. Es decir, **el comparador existe pero no resuelve la fricción de comparación**, que es justamente lo que la thread identificó como el hueco defendible del agregador ([[2026-1023-priceai-modulo-api-transit-tres-ejes-de-comparacion]]).

Para el producto del vault esto tiene una consecuencia incómoda y útil: **la competencia en "comparar precios de acceso web" no la exercen los agregadores-neutrales, la ejercen los propios proveedores**, y lo hacen con una ventaja estructural —ellos conocen el margen y la unidad real. Un agregador que cotice proveedores de proxy tiene que **reconstruir la tabla que el proveedor ya publica en su propio comparador**, y esa tabla es la que el vault acaba de leer: ocho líneas, cinco unidades, dos huecos.

## Nota de verificación
Bloque y URL transcritos literalmente. La captura **no** publica qué campos compara `decodo.com/compare`, si el comparador incluye productos de terceros, ni si las líneas sin precio se muestran como "contact sales" o se omiten. No se ha capturado `decodo.com/compare` en este run: **todo lo que se afirma aquí es la existencia del enlace y su texto**, no su contenido.

## Nota relacionada
El mismo patrón de "el sitio es el producto" ya quedó registrado para los proveedores de SMS y captcha en [[2026-1023-priceai-home-como-radar-y-no-como-vendedor]]: la visibilidad y la comparación son la partida más barata y la que no necesita verificarse para funcionar.
