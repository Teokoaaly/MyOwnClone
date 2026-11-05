---
id: 2026-1026-5sim-los-claims-viven-en-los-alt-text-de-cinco-imagenes
type: atom
certainty: solid
sources: [sources/2026-10-25-5sim-home.md]
links: ["[[2026-1023-5sim-claim-500k-numeros-y-piso-0008]]", "[[2026-1023-5sim-catalogo-servicios-precios-y-stock]]", "[[2026-1023-5sim-casos-de-uso-qa-y-privacidad]]"]
---

## Claim
Los cinco bloques de boasts de la home de 5sim están **duplicados literalmente en el atributo `alt` de las cinco imágenes hero**, y el nombre de cada PNG nombra el claim: `media/home/lots_of_numbers.png` ("Over 500,000 numbers originating from around 180 countries online"), `media/home/daily_replenishment.png` ("New virtual numbers added daily… pricing starts at $0.008"), `media/home/one_time_and_repeated_use.png` ("Single-use numbers to receive SMS"), `media/home/minimum_fees.png` ("Low commission fees"), `media/home/round_clock_support.png` ("Support available 24/7"). Los cinco `alt` reproducen **el texto íntegro** del encabezado y su párrafo, no una descripción: el primero incluye "You can find phone numbers originating from pretty much anywhere, including the Sweden, Germany, France, India, Indonesia, Malaysia, Cambodia, Mongolia, Canada, Thailand, Netherlands, Spain, etc." y el segundo "…and you will not have to pay for monthly SIM plans too".

## Why It Matters
Es un hecho estructural del sitio, no una curiosidad: **el texto de marketing de 5sim existe dos veces en el DOM** (como `alt` y como encabezado+párrafo), lo que significa que cualquier contador de menciones, cualquier extracción por texto plano y cualquier presupuesto de palabra va a duplicar los claims del proveedor ([[2026-1023-5sim-claim-500k-numeros-y-piso-0008]]). Y explica el vacío de la captura del 2026-10-25: al ser todo el contenido principal imágenes con su texto en el `alt`, **el HTML renderizado sin el bloque de precios no tiene ningún dato**, solo copy decorada por imágenes.
La consecuencia para el vault es de método: **el `alt` de estas imágenes es la misma fuente que los párrafos**, así que la única manera de no contar un claim dos veces es tratarlos como una unidad — y la única manera de no perder del todo el dato es no quedarse solo con la capa visible, como le pasó a la captura de 2026-10-22, que sí traía el widget con los ocho precios y los ocho contadores ([[2026-1023-5sim-catalogo-servicios-precios-y-stock]]).

## [FRICTION]
> [[2026-1023-5sim-claim-500k-numeros-y-piso-0008]] (escrita el 2026-10-23) trata "Over 500,000 numbers… around 180 countries", "$0.008" y "soporte 24/7" como **declaraciones comerciales de la propia página de venta**, y registra sus contradicciones con el `Show all 153` del catálogo.
> Este átomo presiona esa creencia en un punto de método: **esas mismas frases no están solo en la página, están duplicadas en los `alt` de las imágenes** que las ilustran, de modo que un corpus que las cuente como "el proveedor afirma X" puede estar contando dos apariciones del mismo texto, y un extractor que solo lea el `alt` en lugar del párrafo obtiene exactamente la misma copla con distinta fuente aparente.
> Ambas no pueden ser simultáneamente la lectura completa: o "la home afirma" describe un conjunto de afirmaciones con duplicación de presentación que hay que descontar, o el texto de marketing de 5sim es en realidad **contenido de imagen** —con la página escrita por SEO de imágenes— y entonces su "superficie de afirmaciones" es más pequeña de lo que aparenta. Marcado para juicio humano, no auto-resuelto: la captura no permite medir cuántos `<img>` y cuántos `<p>` hay en el DOM original.
