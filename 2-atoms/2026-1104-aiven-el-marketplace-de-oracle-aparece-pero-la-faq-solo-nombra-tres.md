---
id: 2026-1104-aiven-el-marketplace-de-oracle-aparece-pero-la-faq-solo-nombra-tres
type: atom
certainty: tentative
sources: [sources/2026-11-04-aiven-pricing.md]
links: ["[[2026-1101-aiven-marketplaces-byoc-y-descuentos-por-compromiso-anual]]", "[[2026-1104-aiven-la-captura-vuelve-a-ser-completa-e-identica-a-la-del-11-02]]"]
---

## Claim
Dentro de la misma página de precios de Aiven, la sección **"Available marketplaces"** muestra cuatro logos de marketplace —**AWS marketplace, Google marketplace, Microsoft marketplace, Oracle marketplace**—, mientras que la FAQ "Does Aiven offer BYOC pricing, marketplace purchasing, annual commitments, or prepaid discounts?" describe la vía de compra como "Purchase Aiven through **AWS, Google Cloud, or Azure** marketplaces", sin mencionar Oracle. La página sí presenta Oracle de forma explícita en otra parte —la cabecera de la FAQ lo empieza con **"Yes to all of the above"**, que incluye "marketplace purchasing"— pero el texto enumerativo solo nombra tres.

## Why It Matters
Es una inconsistencia menor pero con consecuencia operativa: si el vault llegara a comprar infra vía marketplace de Oracle, **la vía no está descrita en la propia página de precios**, lo que significa que el precio y las condiciones del marketplace de Oracle no son públicos en la fuente que el vault usa para el cálculo de coste. Para la comparación de TCO que [[2026-1101-aiven-marketplaces-byoc-y-descuentos-por-compromiso-anual]] ya describe (el gasto en marketplace cuenta para los compromisos cloud existentes), la cobertura real de la vía de compra es **cuatro marketplaces en la página, tres en la prosa**. Y de nuevo, la captura completa no corrige la discrepancia: [[2026-1104-aiven-la-captura-vuelve-a-ser-completa-e-identica-a-la-del-11-02]].

## [FRICTION]
> [[2026-1101-aiven-marketplaces-byoc-y-descuentos-por-compromiso-anual]] afirma que Aiven ofrece "marketplaces de nube (AWS, Google Cloud, Microsoft Azure y Oracle —el gasto cuenta para los compromisos cloud existentes y va por la relación de facturación habitual)", es decir, cuatro vías de compra por marketplace. La FAQ de esta captura solo enumera tres ("AWS, Google Cloud, or Azure marketplaces"), de modo que la afirmación del átomo viejo no está respaldada por la prosa de la página, solo por los cuatro logos. Ambas no pueden ser completamente correctas: o Oracle es un marketplace de compra real omitido en la redacción de la FAQ, o el logo es un residuo de diseño de la sección. Marcado para juicio humano, no auto-resuelto.
