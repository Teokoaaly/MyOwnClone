---
id: 2026-1024-hostbrr-escalera-de-precios-vps-2-00-3-50-y-3-90
type: atom
certainty: solid
sources: [sources/2026-10-23-hostbrr-home.md, sources/2026-10-23-hostbrr-vps-pricing.md]
links: ["[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1023-hetzner-escalera-de-precios-y-salto-a-dedicados]]", "[[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]", "[[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]"]
---

## Claim
HostBrr publica tres familias de VPS con precio de entrada explícito: **Value VPS desde €2.00/mes** (marcado como "Popular", "Scalable virtual private servers featuring dedicated compute resources and root access", CPU AMD de alta frecuencia y protección DDoS incluida), **Performance VPS desde €3.90/mes** ("Enterprise KVM nodes powered by AMD EPYC™ and Threadripper™ for maximum core performance") y **Storage VPS desde €3.50/mes** ("Massive KVM-based storage capacity utilizing redundant arrays and fast NVMe writeback caching", con "Full Root Access"). Los tres son KVM; el precio del que se parte es un "From", no un precio cerrado.

## Why It Matters
Es la referencia de precio del vault para un VPS que **sí cabe** en el objetivo de ≤ €4/mes que el presupuesto de Hetzner declaraba inalcanzable ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]): €2.00/mes de entrada en Value VPS frente a los €5.99/mes del CPX02 más barato de Hetzner ([[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]), y el Performance VPS a €3.90 queda justo por debajo del umbral sin IVA. La comparación estructural con la escalera de Hetzner ([[2026-1023-hetzner-escalera-de-precios-y-salto-a-dedicados]]) es relevante porque aquí el salto de "compartido" a "nodo enterprise KVM con vCPU dedicado" cuesta +€1.90 (×1,95), no el ×6,70 que costaba el salto a dedicados de Hetzner: aquí el término "dedicated resources" se usa para planes de €2. El criterio compartido-vs-dedicado del vault ([[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]) hay que releerlo con esa diferencia de magnitud en mente.

## [FRICTION]
> [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]] (escrita hace 1 día) afirma que **ningún plan del catálogo de Hetzner Cloud cabe en un presupuesto de ≤ €4/mes** y que, por tanto, "el VPS de €4 tiene que venir de otro proveedor o de un modelo distinto".
> Este átomo presiona esa creencia en un punto concreto: la alternativa de proveedor existe y es **más barata**, no más cara. HostBrr declara Value VPS desde €2.00/mes y Performance VPS desde €3.90/mes, ambos por debajo del suelo de €5,99 de Hetzner y dentro del rango de €4.
> Ambas no pueden ser completamente correctas si se leen como una afirmación sobre *el coste de un VPS en general*: o el suelo de ~€6/mes es real solo dentro de Hetzner y el presupuesto de referencia del vault **es alcanzable** en otro proveedor, o el criterio "proveedor con SLA, GDPR e ISO 27001" ([[2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001]]) tiene un sobrecoste que HostBrr no publica y que es el precio real a comparar. Marcado para juicio humano, no auto-resuelto: la captura de HostBrr es una home de marketing, no una página de planes con SLA, ancho de banda ni especificación de CPU.

## Nota de verificación
La captura de la home no publica: número de vCPU, RAM, ancho de banda incluido, IPv4, SLA en texto, ni las condiciones del "50 % OFF" con código NEWLAUNCH. Todos los importes son precios de entrada "From" declarados en la home.

## [NOTA 2026-10-24 — página de precios]
Fuente: `sources/2026-10-23-hostbrr-vps-pricing.md`. La página de precios **confirma el suelo de €2,00** y le pone nombre y ficha: el nodo se llama **"Value 2GB"** y cuesta **€2.00 Monthly Total** con **1 Core @ 3.4 GHz, 2 GB DDR4 ECC, 25 GB de storage y 2.5 TB @ 10Gbps de bandwidth**, en **Frankfurt, Germany** (ver [[2026-1024-hostbrr-value-2gb-1-vcpu-2gb-ram-25-gb-storage]]). Pero **no confirma los otros dos peldaños**: la página solo publica el precio de ese nodo; los €3,50 (Storage) y €3,90 (Performance) de la home **no tienen ficha ni precio verificables** en esta captura, y el proveedor renombra las familias a ejes ("Value Optimized", "Balanced (Memory)", "Performance", "Dedicated Resources" → "Performance VDS", ver [[2026-1024-hostbrr-categorias-del-configurador-y-escalera-de-ram-sin-precios]]). La escalera de la home queda, por tanto, **parcialmente verificada**: un peldaño de tres confirmado con specs, dos sin confirmar.
