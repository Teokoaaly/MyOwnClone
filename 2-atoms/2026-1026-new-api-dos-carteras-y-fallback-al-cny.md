---
id: 2026-1026-new-api-dos-carteras-y-fallback-al-cny
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-priceai-catalogo-ocho-canales-y-fecha-de-tipo-de-cambio]]", "[[2026-1023-priceai-transit-formula-del-multiplicador-compuesto]]", "[[2026-1023-new-api-grupos-como-eje-de-precio-del-relay]]"]
---

## Claim
**v1.0.0-rc.46** corrige un fallo de **saldo visible en una moneda concreta**: con la **cartera de USD a 0** y la **de CNY con dinero**, DeepSeek mostraba el saldo como **0**. El arreglo es **caer a la cartera CNY** cuando la de USD está vacía (PR #7917).

La versión añade además el **plugin 1.1.1 de Kling**, que **acepta una clave de API sin barra vertical** (una sola clave), y el soporte de **embeddings multimodales de Alibaba Bailian** empezando por **`qwen3-vl-embedding`**, con los demás modelos de vector de visión de Bailian en el mismo endpoint.

## Why It Matters
El detalle del fallback a CNY no es un bug menor: es la prueba de que **el saldo de un relay es multimoneda** y de que **el operador puede ver "0" en su panel mientras tiene dinero**. Para un negocio de reventa, un saldo que se muestra como 0 es un cliente que se va; y para el vault, es un recordatorio de que **cualquier dato de precio del sector viene con una moneda y una fecha**, cosa que el agregador externo de referencia hace peor: su tipo de cambio está congelado en el 2026-06-07 ([[2026-1023-priceai-catalogo-ocho-canales-y-fecha-de-tipo-de-cambio]]).
Y conecta con la mecánica del multiplicador: si el multiplicador compuesto es *recarga × modelo* ([[2026-1023-priceai-transit-formula-del-multiplicador-compuesto]]), entonces **la moneda de la cartera es una tercera variable del mismo cálculo** que ninguna tabla del ranking publica. Un canal con saldo en CNY y otro con saldo en USD no son comparables con el mismo número.
El añadido de Kling (clave única sin barra vertical) es el mismo patrón de ** interoperabilidad de bajo nivel** que hace viable un canal: el formato de credencial del upstream condiciona qué proveedores se pueden añadir, y por tanto **cuánta concentración de upstream puede sostener un relay**.
