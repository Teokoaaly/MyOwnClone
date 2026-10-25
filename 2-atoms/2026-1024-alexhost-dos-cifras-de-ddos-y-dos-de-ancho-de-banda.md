---
id: 2026-1024-alexhost-dos-cifras-de-ddos-y-dos-de-ancho-de-banda
type: atom
certainty: solid
sources: [sources/2026-10-24-alexhost-home.md]
links: ["[[2026-1024-alexhost-datacenter-propio-en-chisinau-soterrado]]", "[[2026-1024-hostbrr-ddos-3-6-tbps-l4-y-l7-incluido]]", "[[2026-1024-flokinet-ddos-1tbps-incluido-en-los-siete-planes]]", "[[2026-1024-alexhost-nueve-ubicaciones-sin-ping-ni-ficha]]"]
---

## Claim
La home de AlexHost publica **dos pares de cifras de capacidad que no coinciden entre sí**. En el bloque de statistics del datacenter: **231 Gbit/s "Total Channel"**, **1.6 MW "Total feeder capacity"**, **3.5 Tbit/s "Anti-DDos attacks"** y **uptime garantizado de 99,99 %**, con el datacenter abierto en **2010**. En el bloque textual de "Ordering services at AlexHost — Basic Advantages", las mismas dos magnitudes aparecen con otros valores: **"Highest speed in the Moldovan hosting services market – 20 Gbit/s"** y **"effective protection against DDoS attacks – 500 Gbit/s"**. Las dos series conviven en la misma página: **3,5 Tbit/s frente a 500 Gbit/s** de protección DDoS (**×7**) y **231 Gbit/s frente a 20 Gbit/s** de velocidad de canal (**×11,55**). Además, el texto afirma que **"The company's hardware infrastructure was last updated in 2018"** mientras la sección "Why Choose Us" vende "The latest hardware" con "We only use our own equipment of proven high quality. All hard drives are SSD".

## Why It Matters
Es una fricción interna del propio proveedor, no una comparación entre proveedores, y eso la hace más limpia que las del thread: **las dos cifras son del mismo datacenter, en la misma página, y no pueden ambas ser operativas**. La lectura más verosímil es que la serie de 3,5 Tbit/s / 231 Gbit/s sea la **capacidad instalada agregada** y la de 500 Gbit/s / 20 Gbit/s la **capacidad por cliente o por línea** — pero la captura **no lo dice**, y el rótulo "Total Channel" no distingue total de por-cliente.

La comparación con el thread importa porque el eje de mitigación es el que el vault ya identificó como la partida que más pesa para un relay expuesto: HostBrr incluye **3,6 Tbps L4+L7 sin coste** ([[2026-1024-hostbrr-ddos-3-6-tbps-l4-y-l7-incluido]]) y FlokiNET **1 Tbps+ en los siete planes** ([[2026-1024-flokinet-ddos-1tbps-incluido-en-los-siete-planes]]). Si la cifra agregada de AlexHost es 3,5 Tbit/s, su posición agregada sería comparable; si la cifra operativa es 500 Gbit/s, queda por debajo de HostBrr pero por encima de FlokiNET y de BuyVM (500+ Gbps cobrados a 3 $/IP). **La ambigüedad es precisamente el punto**: un proveedor que publica dos cifras de DDoS en la misma home no puede usarse como dato comparable en la tabla del thread.

## [FRICTION]
> [[2026-1024-flokinet-ddos-1tbps-incluido-en-los-siete-planes]] (escrita hace ~1 día) sostiene que la mitigación incluida es el activo más comparable entre proveedores y publica 1 Tbps+ como cifra única y verificable, mientras Anubiz y ExtraVM dejan el dato variable por ubicación ([[2026-1024-extravm-ddos-varia-por-ubicacion-y-sydney-sin-proteccion-nativa]]).
> Este átomo añade un caso que ese thread no tenía: **el proveedor que publica el mismo eje dos veces con valores que difieren en un factor ×7**. Si la regla del thread es "la mitigación es comparable cuando es una cifra única y con dirección declarada", AlexHost es la prueba de que la regla necesita una segunda condición: **que la cifra no tenga una gemela contradictoria en otra sección de la misma página**.
> Ambas no pueden ser completamente verdaderas como descripciones del mismo datacenter: o 3,5 Tbit/s es la suma de capacidades que no opera en un solo destino, o 500 Gbit/s es un residuo de copy de otra generación del datacenter. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
La captura **no publica** SLA con créditos, ni si la protección DDoS está incluida en el precio de cada plan, ni capas (L4/L7) ni tiempo de mitigación, ni si el "uptime garantizado de 99,99 %" tiene documento que lo respalde — solo el claim.
