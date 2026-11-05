---
id: 2026-1031-brightdata-pricing
type: atom
certainty: solid
sources: [sources/2026-10-31-brightdata-pricing.md, sources/2026-11-01-brightdata-pricing.md, sources/2026-11-02-brightdata-pricing.md]
links: ["[[2026-1031-proton-business-vpn-essentials-6-99-minimo-2-usuarios]]", "[[costes-por-categoria-tenant]]", "[[2026-1101-brightdata-el-hub-de-precios-no-publica-ninguna-cifra]]", "[[2026-1101-brightdata-datasets-con-opcion-de-suscripcion-y-cuenta-dedicada]]"]
---

## Claim
Bright Data's pricing is proxy/infrastructure-tier based, where cost scales by the type of residential, datacenter, or ISP proxy and volume of traffic, creating a usage-based cost model distinct from per-seat SaaS pricing.

## Why It Matters
Unlike the per-seat cost model validated in `costes-por-categoria-tenant`, Bright Data's cost scales with traffic volume and proxy type, not user count. For AI/ML data pipeline projects, this means costs can compound rapidly with data volume rather than headcount. The friction arises when combining Bright Data with per-seat priced services: total infrastructure cost depends on both data volume (Bright Data) and user count (per-seat services), requiring a dual-cost-model framework rather than a single per-seat model.

## [FRICTION]
> [[2026-1025-refinery-brightdata-proxy-pricing.md]] documents Bright Data's tiered pricing by proxy type and traffic volume, confirming the usage-based model. While the refinery atom focuses on proxy cost as a line item, the `costes-por-categoria-tenant` thread focuses on per-seat SaaS costs. Both are valid in their domains, but a project using both Bright Data infrastructure and per-seat SaaS tools must track two separate cost dimensions, and conflating them into a single per-seat model would understate total infrastructure expenditure.
## Nota de extensión 2026-11-03
Tres capturas consecutivas del mismo URL (`sources/2026-10-31-`, `sources/2026-11-01-` y `sources/2026-11-02-brightdata-pricing.md`) confirman y delimitan este átomo. La página de precios de Bright Data es un **catálogo de ocho fichas de producto sin ninguna cifra publicada** —Proxy Networks, Web Scraper API, Scraper Studio, Scraping Browser, SERP API, Web Unlocker, Datasets y Bright Insights—, cada una con un enlace "See Pricing" a su propia subpágina. Ninguna de las tres capturas contiene un precio, un umbral o una unidad de cobro; el único número del hub es "400M+ monthly Residential IPs" y el titular "Trusted by 50,000+ customers worldwide". Detalle en [[2026-1101-brightdata-el-hub-de-precios-no-publica-ninguna-cifra]].

El modelo de coste por uso que este átomo describe sigue siendo correcto, pero **el hub añade una variante que no es medible en unidades automáticas**: la ficha de Datasets es la única del catálogo con modelo de suscripción y *dedicated account manager* ([[2026-1101-brightdata-datasets-con-opcion-de-suscripcion-y-cuenta-dedicada]]), y la ficha de Scraper Studio es la única que declara "Only pay for successful requets" —cobro por request exitoso en lugar de por carga de página ([[2026-1101-brightdata-scraper-studio-cobra-solo-por-requests-exitosos]]). Ambas empujan la tesis del eje abierto del vault: **el coste de Bright Data no es solo infraestructura medida en GB, también tiene una capa de coste por personas y por resultado**, que es exactamente la categoría que el corte por categorías del tenant no puede absorber ([[costes-por-categoria-tenant]]).

Nota de verificación: el bloque `[FRICTION]` anterior enlaza a `2026-1025-refinery-brightdata-proxy-pricing.md`, un archivo que no existe hoy en `2-atoms/`. Se deja el enlace intacto por regla de no sobrescribir creencias previas, pero queda apontando a una nota ausente.
