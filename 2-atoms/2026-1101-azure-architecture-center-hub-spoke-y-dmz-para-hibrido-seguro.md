---
id: 2026-1101-azure-architecture-center-hub-spoke-y-dmz-para-hibrido-seguro
type: atom
certainty: solid
sources: [sources/2026-11-01-azure-architecture-center.md]
links: ["[[2026-1101-azure-architecture-center-arquitecturas-base-de-referencia]]", "[[2026-1022-sin-headers-de-seguridad]]", "[[2026-1022-multi-tenant-slug-unpublished]]"]
---

## Claim
El area de diseño "Secure and connect workloads" ("Design secure network topologies and layered defenses") incluye dos patrones de red concretos: la **topología hub-and-spoke** (`networking/architecture/hub-spoke`) y la **DMZ segura sobre VNet** para red híbrida (`reference-architectures/dmz/secure-vnet-dmz`).

## Why It Matters
Es el patrón de segmentación en dos capas que un SaaS multi-tenant necesita y que el vault hoy no tiene escrito: el hub centraliza la salida y el spoke aísla la carga por tenant. En el caso de MyOwnClone, el aislamiento de tenant está hoy resuelto **a nivel de aplicación** —el slug del tenant decide qué se filtra ([[2026-1022-multi-tenant-slug-unpublished]])—, lo que significa que un fallo de filtrado expone datos de otros tenants. El modelo hub-spoke/segmentación mueve parte de ese aislamiento a la capa de red, donde un error de configuración es visible por topología y no por logs. La otra lectura, más incómoda para el vault: **hub-and-spoke es una topología corporativa**, con un hub que cuesta money por diseño; a escala de ≤ €4/mes el equivalente razonable es una sola red con reglas de egress, no una jerarquía. El patrón importa como checklist (qué segmentar, dónde poner la DMZ), no como diseño a replicar.
