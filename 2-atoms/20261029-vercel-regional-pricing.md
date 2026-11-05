--- 
id: 20261029-vercel-regional-pricing
type: atom
certainty: solid
sources: [0-raw/2026-10-29-vercel-pricing.md]
links: ["[[20261029-vercel-hobby-plan-limits]]", "[[20261029-vercel-waf-custom-rules]]"]
--- 

## Claim
Vercel offers regional pricing variations where prices differ by geography, with dedicated links for regional pricing ↗ available throughout the pricing page, indicating that the same plan features can cost different amounts depending on the customer's billing region.

## Why It Matters
Regional pricing affects the effective cost of Vercel plans for international teams and businesses. A plan listed at $20/mo in one region may have a different price in another due to local taxes, purchasing power parity, or regulatory requirements. This is particularly relevant for distributed teams or companies with billing addresses in different countries.

## [FRICTION]
> [[20261029-vercel-hobby-plan-limits]] (escrita hace ~21 semanas) define los caps de Hobby en "$0/mo". Este átomo nota que los regional pricing links aparecen a lo largo de la página de precios, lo que sugiere que incluso el plan Hobby de $0/mo podría tener variaciones regionales — aunque la FAQ Q1 aclara que "All prices shown are in USD and exclude value-added tax (VAT), goods and services tax (GST), and other applicable taxes. Taxes are calculated based on your billing address and added to your invoice where required by law." No hay fricción contradictoria, pero la presencia de links de regional pricing en todas las secciones plantea la pregunta de si los $0/mo de Hobby son truly globales o también sujetos a impuestos locales por región.

> [[20261029-vercel-waf-custom-rules]] (escrita hace ~21 semanas) describe límites de reglas personalizadas por plan. Este átomo observa que los regional pricing links pueden afectar la efectividad de los límites de reglas: un límite de 3 reglas personalizadas en Pro podría interpretarse diferente dependiendo de la región de facturación, aunque la documentación técnica de límites no varía por región. El fricción es menor: los límites técnicos son fijos, pero el costo para alcanzarlos varía por región.