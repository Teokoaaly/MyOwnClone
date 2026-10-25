---
id: 2026-1024-alexhost-vps-u1-u2-u4-escalera-de-precios
type: atom
certainty: solid
sources: [sources/2026-10-24-alexhost-home.md]
links: ["[[2026-1024-alexhost-configurador-vps-24-fichas-solo-3-con-precio]]", "[[2026-1024-flokinet-escalera-de-precios-siete-planes]]", "[[2026-1024-evoxt-escalera-de-precios-nueve-planes]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1024-alexhost-dos-cifras-de-ddos-y-dos-de-ancho-de-banda]]"]
---

## Claim
Los tres niveles de VPS de AlexHost son **U1 = 6.00 €/mes** (1 vCore, **1,5 GB DDR4**, **10 GB NVMe**, "Shared 100 Mbps"), **U2 = 10.00 €/mes** (2 vCores, **4 GB DDR4**, **40 GB NVMe**, "Shared 100 Mbps" o "Shared 1 Gbps") y **U4 = 16.00 €/mes** (4 vCores, **8 GB DDR4**, **80 GB NVMe**, "Shared 100 Mbps" o "Shared 1 Gbps"). El nombre del plan codifica la vCPU (**U** = unidad, número = cores), y la progresión de recursos es **×2 en cada escalón de disco** (10 → 40 → 80 GB NVMe) y **casi ×2 en RAM** (1,5 → 4 → 8 GB); los cores van 1→2→4. El precio escala en saltos fijos: **+4.00 €** y **+6.00 €**; en precio por GB de RAM eso da **4,00 €/GB → 2,50 €/GB → 2,00 €/GB**, una mejora del 50 % al pasar de U1 a U4. El rango total es **×2,67**. El ancho de banda declarado **no distingue los tiers**: ocho de las fichas de U2 y ocho de las de U4 ofrecen indistintamente "Shared 100 Mbps" o "Shared 1 Gbps" **al mismo precio**, de modo que **subir de 100 Mbps a 1 Gbps es gratis en el catálogo**.

## Why It Matters
El nombre del plan es la **única pista de qué codifica el número**: "U1" no es una generación de hardware sino un contador de vCPU, lo que convierte la escalera en **directamente comparable con la de FlokiNET** (1/2/4/6/10/12 vCPU con RAM 1:1, [[2026-1024-flokinet-escalera-de-precios-siete-planes]]) y con la de Evoxt (vCore casi gratis, RAM cara, [[2026-1024-evoxt-escalera-de-precios-nueve-planes]]). AlexHost queda **entre ambas**: RAM y vCPU crecen parejo pero no 1:1 (1,5 GB por core en U1, 2 GB en U2 y U4).

Para el stack vivo del vault (nginx + Postgres + Redis, [[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]) el **U2 a 10 €/mes es el primer plan con 4 GB**, y el U1 con 1,5 GB es insuficiente por RAM. Esto sitúa a AlexHost **fuera del umbral de ≤ €4/mes** que el vault fijó como ancla ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]) y también por encima de FlokiNET (€7,99 de suelo) y de todos los proveedores de suscripción mensual del thread. Pero el dato relevante para el vault no es el precio: es que **el suolo de 6 € corresponde a un plan de 1,5 GB con ancho de banda "Shared 100 Mbps"**, es decir, la partida de egreso del producto (audio y vídeo) ya nace con un techo declarado y compartido, antes incluso de saber cuánto tráfico incluye — dato que la captura **no publica**.

El apunte fino: **que 1 Gbps salga al mismo precio que 100 Mbps en U2 y U4 significa que el ancho de banda no es un eje de precio en este catálogo**. Es la razón por la que los ocho "Shared 1 Gbps" no son sub-planes distintos, sino **réplicas de renderizado** del mismo plan (con la posible excepción de la que lleva "Shared 100 Mbps"), lo que encaja con la lectura del configurador como poblado con variantes ([[2026-1024-alexhost-configurador-vps-24-fichas-solo-3-con-precio]]).

## Nota de verificación
Ninguno de los tres planes declara tipo de virtualización, número de IP, tráfico incluido, backup, SLA ni sistema operativo; la captura tampoco indica si el ancho de banda "Shared 100 Mbps" es el mismo para todos los clientes del nodo o un límite contractual por VM, ni qué ocurre al superarlo. El texto "No plans in this price range." que cierra la captura pertenece al bloque de hosting compartido LiteSpeed, no a este.
