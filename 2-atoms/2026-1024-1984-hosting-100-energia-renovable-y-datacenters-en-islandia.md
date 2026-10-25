---
id: 2026-1024-1984-hosting-100-energia-renovable-y-datacenters-en-islandia
type: atom
certainty: solid
sources: [sources/2026-10-24-1984-hosting-vps.md]
links: ["[[2026-1024-1984-hosting-vps-entry-9-66-1-cpu-1gb-y-25gb-nvme]]", "[[2026-1024-1984-hosting-fundada-en-2006-con-105k-clientes-y-etica-independent]]", "[[2026-1024-hostkey-catorce-datacenters-europa-y-norteamerica]]"]
---

## Claim
1984 Hosting declara **"100% Green Energy: Powered by Icelandic geothermal and hydroelectric energy"** y sitúa **toda** su infraestructura en Islandia: "Run your website on 100% renewable energy in reliable Icelandic data centers", "reliable virtual private servers in Iceland", "highly secure Icelandic data centers". La página **no publica número de datacenters, ni direcciones, ni países alternativos**.

## Why It Matters
La geografía de 1984 es el **caso extremo opuesto** al del resto del mercado documentado. El vault viene midiendo providers de 2 a 17 ubicaciones: Evoxt con 17 regiones y peering IX por ciudad, HOSTKEY con 14 datacenters ([[2026-1024-hostkey-catorce-datacenters-europa-y-norteamerica]]), ExtraVM con 8, BuyVM con 3, Skhron con 2, LowEndBox casi enteramente norteamericano. **1984 publica una sola geografía: Islandia.** Operativamente, eso significa que **toda la superficie de un tenant está en un solo país del EEE** — lo que simplifica el análisis de transferencias internacionales para un producto con Aviso Legal y DPA ([[2026-1022-superficie-legal-publica-dpa-clon-terms]]) — y también significa que **no hay failover geográfico posible dentro del proveedor**: un incidente en los datacenters islandeses es un incidente total.

El argumento de "100 % energía renovable" es un claim de marketing de sustainability, no un dato de capacidad; lo que sí tiene consecuencia es que **la energía geotérmica + hidroeléctrica islandesa es un argumento de costes de energía y de imagen regulatoria**, y encaja con el silencio del vault sobre si ese mismo criterio de "verde" es una señal de calidad técnica o solo de posicionamiento. El thread ya vio un caso análogo con la calificación editorial de LowEndBox ("LowEnd Score ⭐⭐⭐⭐⭐"), que media presencia y no calidad.

## Nota de verificación
La captura no publica recuentos de datacenters, ni ASN, ni Test IP, ni throughput de red, ni el mix real de energía, ni ninguna certificación ambiental (ningún estándar tipo ISO 14001 o Climate Neutral se menciona).
