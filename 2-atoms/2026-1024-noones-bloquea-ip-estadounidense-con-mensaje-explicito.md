---
id: 2026-1024-noones-bloquea-ip-estadounidense-con-mensaje-explicito
type: atom
certainty: solid
sources: [sources/2026-10-23-noones-p2p.md]
links: ["[[2026-1024-noones-jurisdicciones-globalmente-restringidas]]", "[[2026-1022-i18n-es-first-jurisdiccion-es]]", "[[2026-1024-noones-catalogo-de-paises-soportados-y-150-mas]]"]
---
## Claim
La captura de `https://noones.com/` del 2026-10-23 **no devuelve la home**: el texto literal es *"You are accessing NoOnes from a restricted jurisdiction"* y *"The IP address you are connecting from is located in the United States (USA). We do not offer services in this region."*. El bloqueo decide por **IP**, antes de cualquier cuenta o navegador. La página solo ofrece dos salidas —un enlace a la KB de países bloqueados y el centro de ayuda— y **no enumera catálogo, precios, servicios ni stock**: nada de esa página permite afirmar qué ofrece NoOnes más allá del mensaje de bloqueo.

## Why It Matters
La puerta de entrada de un proveedor P2P de cripto se cierra por geolocalización de IP, no por autenticación: un nodo de salida en USA no ve ni un precio. Para el phone farm eso significa que la cobertura de un proveedor depende de **dónde está la IP**, no de quién la usa, y que el mismo proveedor es usable desde una IP Nigerian o Vietnamese pero invisible desde una estadounidense ([[2026-1024-noones-catalogo-de-paises-soportados-y-150-mas]]). Es la misma variable que ya condiciona el precio en 5sim ([[2026-1023-5sim-europa-occidental-paga-la-factura]]) pero aquí decide además si hay producto o solo un muro: el vault no puede tratar a NoOnes como un proveedor accesible "desde el mercado occidental" desde la vantage de una operación con origen en España ([[2026-1022-i18n-es-first-jurisdiccion-es]]).
