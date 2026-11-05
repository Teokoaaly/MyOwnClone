---
id: 2026-1029-render-bandwidth-overage
type: atom
certainty: solid
sources: [sources/2026-10-29-render-pricing.md]
links: ["[[2026-1022-admin-bandeja-global-y-spam]]", "[[2026-1022-auth-flask-nextauth-desconectados]]"]
---

## Claim
Render includes bandwidth with their workspace plans (5 GB/mo for Hobby, 25 GB/mo for Pro, 1 TB/mo for Scale) and charges $0.15 per GB overage thereafter, with Enterprise having custom bandwidth terms.

## Why It Matters
The $0.15/GB overage rate creates a meaningful cost multiplier for bandwidth-intensive applications, particularly those serving large files, video, or high-traffic web traffic. A site receiving 100 GB of monthly bandwidth would pay $22.50 in overage on top of the plan fee, potentially doubling the effective cost of the Scale plan for high-traffic workloads.

## [FRICTION]
> [[2026-1023-lzt-captura-parcial-sin-precios-ni-stock]] observes that some pricing pages render partial capture where bandwidth costs are not transparently listed, creating a information asymmetry where users cannot predict overage costs without examining the fine print. Render's explicit $0.15/GB rate is more transparent than sites that omit overage pricing entirely, but the rate still requires traffic volume forecasting to avoid surprise charges.

## Nota de extensión 2026-11-03
Verificado contra `sources/2026-10-29-render-pricing.md`: los tres importes son correctos (5 GB Hobby, 25 GB Pro, 1 TB Scale, luego $0,15/GB; Enterprise "Custom"). Dato adicional del mismo source: el tráfico saliente por AWS private link se cobra a $0,03/GB en Pro y Scale, la mitad que el overage de ancho de banda público — detalle en [[2026-1029-render-extras-de-red]]. El overage se factura sobre el ancho de banda incluido, y los Static Sites no consumen cómputo ni ancho de banda facturable ([[2026-1029-render-static-sites-gratis]]).