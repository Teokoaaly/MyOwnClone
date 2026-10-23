---
id: 2026-1023-5sim-openai-76-paises-y-130-operadores
type: atom
certainty: solid
sources: [sources/2026-10-22-5sim-openai-chatgpt-pricing.md]
links: ["[[2026-1023-5sim-chatgpt-verificacion-stock-13-7-millones]]", "[[2026-1023-5sim-catalogo-153-paises-contra-180-de-la-home]]", "[[2026-1023-5sim-openai-tabla-visible-8-filas]]", "[[2026-1023-5sim-openai-tasa-entrega-techo-56]]"]
---

## Claim
La página de producto de OpenAI/ChatGPT en 5sim lleva su propio bloque de estadísticas, distinto del selector genérico: **Price from $0.05**, **Countries available 76**, **Operators 130**, **Best SMS delivery rate 56%**. Es decir, la cobertura del servicio OpenAI es de **76 países y 130 operadores** —muy por debajo de los 153 países del catálogo y los 1329 servicios— y su precio de entrada declarado ($0.05) **no coincide** con el `from $0.01` que el selector muestra para `OpenAI/ChatGPT`. De esos 76 países la página solo hace visibles 8 filas de la tabla de precios; el resto no es verificable desde el texto capturado.

## Why It Matters
El número que de verdad limita un flujo de verificación de cuentas OpenAI es el par (país, operador) realmente disponible para ese servicio, no el catálogo global del proveedor: 76 países y 130 operadores son el inventario efectiva. Por debajo del precio declarado hay además una discrepancia de precios entre dos representations del mismo proveedor el mismo día, que hay que resolver antes de calcular margen ([[2026-1023-5sim-chatgpt-verificacion-stock-13-7-millones]]). Y la cifra de 76 se suma al conflicto ya abierto de cifras de cobertura ([[2026-1023-5sim-catalogo-153-paises-contra-180-de-la-home]]): ahora hay cuatro números (180 de la home, 153 del catálogo, 111 del CSV de `telegram`, 76 para OpenAI). La tabla visible es solo una muestra ordenada, no el inventario ([[2026-1023-5sim-openai-tabla-visible-8-filas]]), y su techo de entrega es del 56% ([[2026-1023-5sim-openai-tasa-entrega-techo-56]]).

## [FRICTION]
> [[2026-1023-5sim-chatgpt-verificacion-stock-13-7-millones]] (escrita hoy, desde la home) afirma que `OpenAI/ChatGPT` aparece con precio `from $0.01` y 13 724 093 números en stock.
> Esta nota, desde la página del propio producto OpenAI, declara `Price from $0.05`.
> Ambas no pueden ser el mismo precio de suelo: el $0.01 es el precio *de escaparate* del selector genérico y el $0.05 el mínimo declarado por la página del servicio, o bien son precios de combinaciones distintas con countries/rate distintos. Marcado para juicio humano, no auto-resuelto.
