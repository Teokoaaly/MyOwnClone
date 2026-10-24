---
id: 2026-1024-extravm-modelo-de-red-puerto-1gbps-5gbps-y-tráfico-de-3-a-40-tb
type: atom
certainty: solid
sources: [sources/2026-10-23-extravm-vps-pricing.md]
links: ["[[2026-1024-extravm-escalera-de-precios-14-planes-de-4-50-a-192]]", "[[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]", "[[2026-1024-hostbrr-ancho-de-banda-2-5-tb-a-10-gbps]]"]
---

## Claim
La columna "Network" de la tabla de ExtraVM declara explícitamente su modelo: **"This is the monthly traffic allocation and network port speed. We only limit outbound port speed, inbound is 10Gbps."** Es decir, **el tráfico de salida está limitado y el de entrada no** (10 Gbps sin límite). Los 14 planes asignan **3 TB a 40 TB/mes** en seis tramos (3, 5, 10, 20, 30, 40 TB) y la **velocidad de puerto sube una sola vez**: 1 Gbps en los planes de 1 y 2 GB, y **5 Gbps desde el plan de 3 GB en adelante** hasta el de 64 GB.

## Why It Matters
El modelo es cualitativamente distinto del de Hetzner: allí el egreso está **ilimitado hasta 20 TB y luego se cobra €1.00/TB** ([[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]); aquí el egreso está **topado desde el primer mes** (3 TB en el plan de entrada) y no se publica ningún recargo por exceso. Para un producto que sirve respuestas de clon con audio y vídeo, el techo mensual es un límite de diseño, no un susto de factura: si el vault autoaloja en ExtraVM, el egreso es una **restricción de capacidad** (cuánto contenido puede servir al mes) y no una variable de coste. El salto de 1 a 5 Gbps ya en 3 GB de RAM es generoso para el stack del despliegue vivo ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]) y comparable al 10 Gbps que publica HostBrr con solo 2,5 TB de tráfico ([[2026-1024-hostbrr-ancho-de-banda-2-5-tb-a-10-gbps]]).

## Nota de verificación
La captura no publica qué ocurre al superar el tráfico asignado (ni si hay overage, ni su precio), ni si el límite de 5 Gbps es agregado por nodo o por servidor, ni política de abuso.
