---
id: 2026-1024-extravm-ddos-varia-por-ubicacion-y-sydney-sin-proteccion-nativa
type: atom
certainty: solid
sources: [sources/2026-10-23-extravm-vps-pricing.md]
links: ["[[2026-1024-extravm-8-datacenters-facilities-asn-y-test-ip]]", "[[2026-1024-hostbrr-ddos-3-6-tbps-l4-y-l7-incluido]]", "[[2026-1024-hostbrr-mitigacion-in-house-sin-scrubbing-externo]]"]
---

## Claim
La protección DDoS **no es uniforme entre ubicaciones** y depende de terceros con nombres distintos: **Global Secure Layer** aporta "high capacity" en Dallas y Los Angeles; **Datapacket** la aporta en Miami, Singapore y Tokyo; **Royale Hosting** en Amsterdam ("high capacity") pero en Secaucus NJ solo "basic". En todas se suma filtrado local con filtros propietarios **eBPF/XDP**. **Sydney AU es la excepción declarada**: "Sydney does not come with native network DDoS protection. However we do provide basic local DDoS filtering less than 10 Gbps using proprietary eBPF/XDP filters." La FAQ lo confirma: "most locations include enterprise-grade DDoS protection at no extra cost. Protection levels vary by location".

## Why It Matters
Convierte el "Anti-DDoS" que aparece como columna de la tabla de precios en una **columna vacía de contenido uniforme**: el término es cierto en siete de ocho ubicaciones y claramente degradado en la octava. Eso importa para el vault porque Sydney es la única opción de Oceanía y la que un proveedor con presencia en Asia-Pacífico (Evoxt vía US/UK, HostBrr en DE/US/LU) no ofrece: para un producto con usuarios en la región Asia-Pacífico, elegir Sydney **es elegir el nodo sin mitigación de red**, y la FAQ lo admite sin disguise ("no viene con protección nativa"). La comparación con el resto del vault: HostBrr publica **3.6 Tbps L4 y L7** con mitigación in-house ([[2026-1024-hostbrr-ddos-3-6-tbps-l4-y-l7-incluido]], [[2026-1024-hostbrr-mitigacion-in-house-sin-scrubbing-externo]]) — una cifra verificable frente a la aquí no cuantificada, solo cualitativa ("high capacity").

## Nota de verificación
La captura no publica cifras de capacidad de mitigación, SLA de DDoS, ni si el filtrado eBPF/XDP es el mismo binario en todas las ubicaciones. "Basic" y "high capacity" no están definidos.
