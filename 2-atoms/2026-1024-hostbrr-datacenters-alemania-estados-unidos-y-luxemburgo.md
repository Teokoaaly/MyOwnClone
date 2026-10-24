---
id: 2026-1024-hostbrr-datacenters-alemania-estados-unidos-y-luxemburgo
type: atom
certainty: solid
sources: [sources/2026-10-23-hostbrr-home.md, sources/2026-10-23-hostbrr-vps-pricing.md]
links: ["[[2026-1023-hetzner-regiones-y-zonas-de-disponibilidad]]", "[[2026-1022-superficie-legal-publica-dpa-clon-terms]]", "[[2026-1022-i18n-es-first-jurisdiccion-es]]"]
---

## Claim
HostBrr opera en **tres países**: "Our infrastructure runs in premium datacenters in **Germany**, the **United States**, and **Luxembourg**." La FAQ (pregunta 06) añade que "The available locations for each product are shown on its plan page" — es decir, la disponibilidad es **por producto**, no uniforme: el catálogo de la home no publica qué ubicaciones corresponden a cada producto (ni si los Storageboxes, por ejemplo, están solo en una).

## Why It Matters
Es el dato que hace comparables las cifras de precio: una entrada de "€2,00/mes" en un datacenter alemán (dentro de la UE, con el marco GDPR del que habla el Aviso Legal del producto, [[2026-1022-superficie-legal-publica-dpa-clon-terms]]) y una entrada de "€2,00/mes" en uno estadounidense no son la misma unidad de coste cuando hay egreso transatlántico o requisitos de residencia de datos. El vault ya tenía el mismo problema con las zonas de Hetzner ([[2026-1023-hetzner-regiones-y-zonas-de-disponibilidad]]), así que la regla del vault es la misma: **el precio sin ubicación no es comparable**. Para un producto con foco es-first y jurisdicción ES ([[2026-1022-i18n-es-first-jurisdiccion-es]]), tener una sede en la UE entre las tres declaradas es un argumento de cumplimiento que el proveedor no expresa en la home pero que es verificable en la página de planes.

## Nota de verificación
La captura no publica el desglose de ubicaciones por producto, ni los precios por ubicación, ni los nombres de los datacenters, ni si las cifras de la home están calculadas para una región concreta.

## [NOTA 2026-10-24 — página de precios]
Fuente: `sources/2026-10-23-hostbrr-vps-pricing.md`. La página de precios **responde a la pregunta que la home dejaba abierta** sobre la disponibilidad por producto: el plan de entrada "Value 2GB" (€2,00) muestra la bandera y la ubicación **"Frankfurt, Germany"**. Es decir, el precio de suelo del catálogo es **explícitamente alemán y europeo**, lo que lo hace directamente comparable con el argumento de residencia de datos del vault ([[2026-1022-superficie-legal-publica-dpa-clon-terms]], [[2026-1022-i18n-es-first-jurisdiccion-es]]) sin tener que asumir que el precio corresponde a la región menos restrictiva. Pero la página **no** publica el desglose por producto para las demás familias ni los precios por ubicación: sigue sin saberse si Estados Unidos y Luxemburgo tienen el mismo precio o el mismo lineup de planes.
