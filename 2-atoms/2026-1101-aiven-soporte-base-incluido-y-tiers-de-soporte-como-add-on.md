---
id: 2026-1101-aiven-soporte-base-incluido-y-tiers-de-soporte-como-add-on
type: atom
certainty: solid
sources: [sources/2026-11-01-aiven-postgresql-pricing.md, sources/2026-11-03-aiven-pricing.md]
links: ["[[2026-1031-aiven-postgresql-pricing]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1029-render-postgres-pricing]]"]
---

## Claim
Cada plan de Aiven incluye un **tier base de soporte sin coste adicional** (equipo de soporte, documentación y comunidad); existen además **Business support** (tiempos de respuesta garantizados) y **Enterprise support** (contacto dedicado y SLAs más fuertes) **como add-on de pago** al plan de servicio. Aiven lo contrasta explícitamente con los hyperscalers, donde "even basic technical support often costs a fixed monthly percentage of your cloud bill".

## Why It Matters
Es la diferencia entre soporte como coste variable que escala con el consumo y soporte como línea fija: para el vault, cuyo presupuesto de infra es ≤ €4/mes ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]), el soporte incluido de serie en el plan base evita una partida que en AWS/GCP/Azure crecería con la factura — relevante en la comparación de coste total que [[2026-1031-aiven-postgresql-pricing]] ya plantea frente a [[2026-1029-render-postgres-pricing]].

## 2026-11-03 — re-verificación
La fila "Support" de la captura del 2026-11-03 matiza el "tier base sin coste" con el detalle por plan: **Free solo tiene "Support via documentation"**, y desde **Developer hasta Premium** el soporte es "through email with best-effort responses during the same or next business day"; la fila añade además "three additional support tiers with separate charge that include faster response times and phone support". Es decir, el soporte incluido **existe pero degrada en los dos planes gratuitos**, y el escalón real (respuestas garantizadas y teléfono) es un add-on de pago también en el plan base. Ver [[2026-1103-aiven-soporte-por-plan-documentacion-en-free-y-email-best-effort-desde-developer]].

## Actualización 2026-11-04
Fuente: `sources/2026-11-04-aiven-pricing.md` (quinta captura). La FAQ "What does support cost, and is it included?" **vuelve a renderizarse íntegra** y añade la **tabla de tres tiers con su público objetivo**: **Included (default)** — "Development, staging, and workloads where best-effort response is acceptable"; **Business support** — "Production workloads needing guaranteed response times"; **Enterprise support** — "Mission-critical production with dedicated support and tighter SLAs". Confirma que el tier base "covers access to Aiven's support team, documentation, and the Aiven community" a coste cero, y que los tiers mejorados "are priced as an add-on to your service plan". La captura del 11-03 no mostraba ninguna de las dos piezas (ni la FAQ ni la tabla); ver [[2026-1104-aiven-la-captura-vuelve-a-ser-completa-e-identica-a-la-del-11-02]].
