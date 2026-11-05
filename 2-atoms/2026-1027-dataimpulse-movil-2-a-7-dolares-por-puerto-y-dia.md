---
id: 2026-1027-dataimpulse-movil-2-a-7-dolares-por-puerto-y-dia
type: atom
certainty: solid
sources: [sources/2026-10-26-dataimpulse-mobile-proxies.md]
links: ["[[2026-1024-iproyal-cinco-lineas-y-cinco-unidades-de-precio]]", "[[2026-1024-iproyal-movil-117-al-mes-y-45m-de-ips]]", "[[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]", "[[2026-1027-dataimpulse-tabla-comparativa-con-el-promedio-movil]]"]
---

## Claim
El FAQ "What is the cheapest mobile proxy provider?" publica una **tercera unidad de precio del sector móvil**, distinta del gigabyte: **"Some providers charge per port per day ($2–7/day), others per gigabyte."** Y define la posición de DataImpulse dentro de ese spectrum: **"DataImpulse uses pay-per-GB pricing starting from $2/GB with no monthly commitment – you pay only for the traffic you actually use. It's one of the cheapest models on the market."**

## Why It Matters
El thread ya tenía registrado que el proxy **no tiene una unidad única**: por GB, por proxy, por mes y por mil de solicitudes ([[2026-1024-iproyal-cinco-lineas-y-cinco-unidades-de-precio]]). Esta captura añade una quinta forma, y es la más relevante para el caso de uso del vault: **por puerto y por día**, con un rango de **$2 a $7 diarios** por puerto.
Esa unidad tiene una consecuencia aritmética que el resto no tiene: **el coste del móvil deja de ser marginal y pasa a ser fijo recurrente por puerto**, igual que el móvil de IPRoyal a $117/mes ([[2026-1024-iproyal-movil-117-al-mes-y-45m-de-ips]]). Para un flujo de handful de altas, un puerto a $2/día **supera con creces** el suelo de $5 del plan Intro por 2,5 GB de DataImpulse —que es exactamente la razón por la que el propio proveedor se posiciona en el extremo de $2/GB. Es decir: **el "uno de los modelos más baratos del mercado" es una afirmación relativa a la unidad de su competidor, no al coste absoluto de la partida**.
Y hay un detalle de estructura que importa: un **puerto** es una posición en un servidor, no una IP. Cobrar por puerto y por día significa que la granularidad del control de gasto es de un día, no de un byte: es el patrón de coste que el thread ya había marcado como incompatible con un presupuesto de ≤ €4/mes ([[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]).

## Why It Matters (segunda lectura)
La frase "starting from $2/GB" es, en el sector móvil, **el precio de una de las unidades más baratas ya medidas** — comparable con el móvil de DataImpulse ($2/GB) — pero está en la misma frase que un rango de $2–7 **diarios por puerto**. La consecuencia para la tabla de coste por insumo del thread es directa: **la fila de proxy móvil no puede cerrarse con un $/GB**, porque hay al menos tres unidades en juego en el mismo tipo de producto (GB, puerto-día y mes) y el vault solo tiene medida de dos.

## Nota de verificación
Frase transcrita literalmente del FAQ "What is the cheapest mobile proxy provider?". La captura **no** publica: cuántos puertos incluye un plan, qué es un "puerto" en la implementación, ni si esos $2–7/día son del pool de DataImpulse o de terceros. La afirmación "one of the cheapest models on the market" es **claim del proveedor**, no medición.
