---
id: 2026-1024-hostbrr-ancho-de-banda-2-5-tb-a-10-gbps
type: atom
certainty: solid
sources: [sources/2026-10-23-hostbrr-vps-pricing.md]
links: ["[[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]", "[[2026-1024-hostbrr-value-2gb-1-vcpu-2gb-ram-25-gb-storage]]", "[[2026-1024-hostbrr-ddos-3-6-tbps-l4-y-l7-incluido]]"]
---

## Claim
El ancho de banda del plan de entrada de HostBrr es **2.5 TB @ 10Gbps**, y la página de característica lo presenta como Connectivity de red: "**10 Gbps Connectivity** — Massive network uplinks ensure your high-performance server handles traffic spikes without choking". La cifra es de **salida incluida en el plan**, no de un recargo: la página no publica sobrecoste por TB ni política de abuso.

## Why It Matters
Convierte el precio en **egreso por TB comparable**: €2,00 por 2,5 TB son **€0,80/TB incluidos**, frente a los 20 TB incluidos del plan más barato de Hetzner a €5,99 ([[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]) — allí el egreso extra cuesta €1,00/TB y el incluido es 8 veces mayor. Es decir: **HostBrr es más barato en el servidor pero peor en el byte**, y para un producto que sirve respuestas de clon con streaming SSE, audio y vídeo el egreso, no la CPU, es la partida que dispara la factura. Los 10 Gbps de uplink son capacidad de pico, no volumen mensual: no cubren el caso de un tenant que genere vídeo de forma sostenida. El contraste con el DDoS de 3,6 Tbps incluido ([[2026-1024-hostbrr-ddos-3-6-tbps-l4-y-l7-incluido]]) es la asimetría clave del plan: **la protección es mucho más grande que el ancho de banda contratada**.

## [FRICTION]
> [[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]] (escrita hace 1 día) establece el marco del vault para el coste marginal del egreso: 20 TB incluidos y €1,00/TB extra en la UE.
> Este átomo presiona ese marco en un punto: con HostBrr el coste **por byte incluido** es €0,80/TB frente a los 20 TB de Hetzner, es decir que la ventaja de precio del servidor de HostBrr (€2,00 vs €5,99, ver [[2026-1024-hostbrr-value-2gb-1-vcpu-2gb-ram-25-gb-storage]]) **se invierte si el producto mueve más de ~2,5 TB/mes**. Ambas no pueden ser simultáneamente la base de la decisión: o el vault fija el criterio "egreso incluido" como el que manda (y entonces el HostBrr de 2,5 TB es un mal negocio a partir del primer mes de producción), o fija el criterio "coste total de servidor" (y entonces el recargo de Hetzner no es el relevante). Marcado para juicio humano, no auto-resuelto: la captura no publica qué cuenta el 2,5 TB (¿egreso? ¿tráfico agregado servidor?) ni si hay límite de uso justo.
