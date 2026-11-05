---
id: 2026-1102-aiven-disco-dinamico-cuesta-dinero-extra-desde-startup
type: atom
certainty: solid
sources: [sources/2026-11-02-aiven-postgresql-pricing.md, sources/2026-11-03-aiven-pricing.md]
links: ["[[2026-1102-aiven-pitr-2-14-y-30-dias-segun-plan]]", "[[2026-1022-costes-por-categoria-tenant]]", "[[2026-1031-backblaze-b2-storage-pricing]]"]
---

## Claim
El "Dynamic disk sizing" (añadir o quitar almacenamiento según crece el negocio) aparece como **"Not available"** en los planes Free, Developer y Hobbyist, y como **"Available at an additional cost"** en Startup, Business y Premium. La tabla aclara además que "Data retention is only limited by storage, with the exception of Free plan".

## Why It Matters
Separa el precio del plan del precio del crecimiento: en Aiven **el plan no incluye el almacenamiento que el uso necesita**, y ampliarlo cuesta una línea extra. Esto es directamente relevante para el modelo de costes del vault ([[2026-1022-costes-por-categoria-tenant]]), donde el coste por tenant crece con el uso: el almacenamiento es la partida que **sí** escala con los datos por cliente mientras el plan fijo no baja, y por tanto el coste de un tenant que usa mucho se sale del modelo "coste por asiento". Es la misma divergencia de modelos que [[2026-1031-backblaze-b2-storage-pricing]] registra para el almacenamiento por GB: Aiven no es un "coste por byte" limpio, es "plan base + almacenamiento dinámico facturado aparte".

## 2026-11-03 — re-verificación
La captura del 2026-11-03 repite "Dynamic disk sizing" como **"Not available"** en Free, Developer y Hobbyist y **"Available at an additional cost"** en Startup, Business y Premium, y vuelve a incluir la frase "Data retention is only limited by storage, with the exception of Free plan". Confirma además que los tres planes de pago son los únicos con **7 configuraciones de servicio** cada uno ("View 7 plans"), lo que explica por qué el almacenamiento del plan va de 80 GB a 11 TB: el dimensionado dentro de un plan se ajusta, pero el ajuste fino se factura aparte.
