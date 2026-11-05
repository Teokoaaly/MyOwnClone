---
id: 2026-1101-hetzner-lineas-de-dedicados-gpu-y-almacenamiento-propio
type: atom
certainty: solid
sources: [sources/2026-11-01-hetzner-cloud.md]
links: ["[[2026-1023-hetzner-escalera-de-precios-y-salto-a-dedicados]]", "[[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]", "[[2026-1031-lambda-gpu-pricing]]"]
---

## Claim
El menú del sitio de Hetzner en la captura del 2026-11-01 expone **un catálogo de servidores dedicados por línea de producto**, ausente en las capturas de Cloud: **AX-Line** (rendimiento basado en AMD), **EX-Line** (basado en Intel), **GPU-Line** ("Maximum workloads & ai"), **SX-Line** ("For large amounts of data") y **DX-Line** (servidor Dell para computación intensiva), más un **"Server Finder"** para elegir servidor, y una sección **Storage** con **Object Storage (S3-compatible)**, **Storage Box** y **Storage Share**, un producto **"European Cloud"** ("Lower costs, more data sovereignty") y **Load Balancer** y **Managed Server** como servicios separados.

## Why It Matters
Es la respuesta a la pregunta que el vault dejó abierta en [[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]: el criterio compartido-vs-dedicado de la página de Cloud es binario, pero el catálogo real de Hetzner tiene **al menos cinco líneas dedicadas y una línea GPU explícitamente orientada a IA** — es decir, existe una vía de cómputo acelerado dentro del mismo proveedor. Para MyOwnClone eso importa por el lado del coste de inferencia: el vault ya documenta que el cómputo se paga por uso contra APIs ([[2026-1031-lambda-gpu-pricing]]), y una GPU dedicada de Hetzner es la alternativa de coste fijo a esa factura por token; pero la captura **no publica ningún precio de GPU-Line**, así que el dato que falta es precisamente el que decidiría si esa alternativa cabe en el presupuesto. Del lado del producto, la existencia de Object Storage S3-compatible y Load Balancer como productos separados significa que **cargar el coste del stack completo de infraestructura** (compute + object storage + balanceo) es posible dentro de un solo proveedor, sin sumar el coste de Object Storage de terceros que hoy documenta el vault.

## Nota de verificación
La captura **no publica precios de ninguna de estas líneas** (GPU-Line, AX/EX/SX/DX, Object Storage, Storage Box, Load Balancer, Managed Server, European Cloud): solo nombres, etiquetas y enlaces. El único precio del menú es el de la Server Auction (ver [[2026-1101-hetzner-server-auction-refurbished-desde-72-70]]). No se afirma ninguna cifra para estos productos.
