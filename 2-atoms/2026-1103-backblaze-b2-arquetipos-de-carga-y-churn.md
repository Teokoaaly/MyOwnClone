---
id: 2026-1103-backblaze-b2-arquetipos-de-carga-y-churn
type: atom
certainty: solid
sources: [sources/2026-11-03-backblaze-b2-storage-pricing.md]
links: ["[[2026-1102-backblaze-b2-egreso-gratis-hasta-3x-y-0-01-por-gb]]", "[[2026-1102-backblaze-b2-sin-minimo-de-duracion-ni-de-tamano-de-archivo]]", "[[2026-1102-backblaze-b2-precio-6-95-por-tb-al-mes]]"]
---

## Claim
La página de precios de B2 tabula cuatro **arquetipos de carga** con su patrón de consumo característico: "**Active archive** — Low egress, rare deletion", "**Backup & DR** — Retention-based churn", "**Application storage** — Frequent reads and deletes" y "**Custom** — Start neutral, then tune it"; el modelo B2 se describe como "Purpose-built for active archiving, backup, and recovery with compliance, media, and application workload management".

## Why It Matters
Es el mismo tipo de segmentación por **comportamiento de consumo** que ya usa el vault para el seat ([[2026-1022-costes-por-categoria-tenant]]), pero aplicado al almacenamiento: el precio unitario de $6.95/TB ([[2026-1102-backblaze-b2-precio-6-95-por-tb-al-mes]]) es constante, lo que cambia entre arquetipos es la **mezcla entre volumen, egreso y churn**, y por tanto si la factura sale de la línea de capacidad o de la de egreso. El patrón de backup de Postgres que el vault quiere montar es "Backup & DR" con churn por retención, y ahí la combinación de "sin mínimo de duración" ([[2026-1102-backblaze-b2-sin-minimo-de-duracion-ni-de-tamano-de-archivo]]) y "egreso gratis hasta 3× el almacenamiento medio" ([[2026-1102-backblaze-b2-egreso-gratis-hasta-3x-y-0-01-por-gb]]) es exactamente la que hace que el arquetipo sea barato: se escribe mucho, se lee poco y se borra según retención. "Application storage — Frequent reads and deletes" es el arquetipo caro: sube el egreso por encima de 3× y, a diferencia de los demás, es el que se acerca al mundo del almacenamiento de objetos de uso intensivo. La lectura accionable para el vault: **el lugar barato de un backup de Postgres es la categoría "Backup & DR", y el lugar caro es "Application storage"**, porque en el segundo el mismo euro de almacenamiento se multiplica por lecturas y borrados.

## Nota
La tabla de arquetipos aparece en las tres capturas (2026-11-01, 11-02 y 11-03) con el mismo contenido; la diferencia en esta captura es que la.reduce no incluye los enlaces de navegación ni los iconos, por lo que el bloque queda como texto contiguo legible.
