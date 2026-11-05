---
id: 2026-1102-assemblyai-facturacion-mensual-sin-minimos-ni-contratos
type: atom
certainty: solid
sources: [sources/2026-11-02-assemblyai-pricing.md, sources/2026-11-03-assemblyai-pricing.md]
links: ["[[2026-1101-assemblyai-tarifas-por-hora-no-por-minuto]]", "[[2026-1022-platform-admin-tenants-costes-mrr]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---

## Claim
El modelo de facturación de AssemblyAI en pay-as-you-go es **mensual, sobre uso real y sin compromisos**: "We bill monthly based on your actual usage. There are no minimum commitments, upfront fees, or contracts on the pay-as-you-go plan. Invoices are generated at the start of each month for the previous month's usage." Los descuentos por volumen **no están publicados**: "We offer custom pricing for customers with high-volume usage. Contact our sales team to discuss tiered pricing, volume discounts, and enterprise agreements tailored to your needs." El cabecero lo dice igual: "Looking for volume-based pricing? We'll build a solution tailored to your needs." La FAQ añade una vía de compra alternativa: "AssemblyAI is available on the AWS Marketplace, allowing you to consolidate billing through your existing AWS account. Contact our sales team for details on setting this up."

## Why It Matters
Cierra el modelo de coste con la pieza que faltaba en la tabla de precios: la factura llega **mes a mes, con un mes de retraso** (se emite a principio de mes por el uso del mes anterior), lo que significa que el primer mes de uso real no se factura hasta el mes siguiente. Para un panel de costes por tenant como el de [[2026-1022-platform-admin-tenants-costes-mrr]], que ya separa coste facturable al cliente y coste de plataforma ([[2026-1022-costes-por-categoria-tenant]]), esto significa que el coste de audio de un tenant aparece en el MRR con un mes de retraso respecto al uso: no se puede cerrar un mes con la cifra real, hay que estimarla. Y sobre los descuentos por volumen, la conclusión operativa es nítida: **no existe un precio público que baje del $0.15/hr sin hablar con ventas**, así que cualquier proyección de coste a volumen en el vault tiene que hacerse sobre el precio de lista, sin margen de descuento asumible.

## 2026-11-03 — re-verificación
La captura del 2026-11-03 (`sources/2026-11-03-assemblyai-pricing.md`) vuelve a traer el hero "Start free, pay-as-you-go after that – no commitments required." y los botones "Try our API for free" / "Contact sales" — idénticos, palabra por palabra, a los del 11-01 y del 11-02. Confirma que el mensaje de entrada **sin compromisos** no ha cambiado; la FAQ de facturación (factura mensual, sin mínimos, descuentos por volumen vía ventas) **no aparece** en esta captura porque el bloque correspondiente no se renderizó (ver [[2026-1103-assemblyai-captura-reducida-solo-pre-recorded-expandido]]), así que queda sin re-verificar hoy, no contradicha.
