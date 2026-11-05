---
id: 2026-1031-twilio-sms-pricing
type: atom
certainty: solid
sources: [sources/2026-10-31-twilio-sms-pricing.md]
links: ["[[2026-1031-proton-business-vpn-essentials-6-99-minimo-2-usuarios]]", "[[costes-por-categoria-tenant]]"]
---

## Claim
Twilio SMS pricing is per-message with volume-tiered discounts, creating a usage-based cost model where cost scales with the number of SMS sent rather than per-user seats.

## Why It Matters
Unlike the per-seat cost model validated in `costes-por-categoria-tenant`, Twilio's cost scales with message volume, not user count. For products with SMS notification needs, cost depends on messages per user per month. If each user receives 5 SMS daily, monthly messages per user = 5 × 30 = 150. At Twilio's rates (approximately $0.0075/message), this is $1.13 per user per month — relatively modest, but for high-frequency SMS products, costs can compound rapidly. The friction is in comparing against per-seat models: for low-SMS-frequency products, Twilio cost per user is predictable and modest, but for high-frequency products, a per-user flat-rate SMS service may be more economical, or the product may need to amortize SMS cost into the per-seat model.

## [FRICTION]
> [[2026-1025-refinery-twilio-sms-chatgpt-verification.md]] documents Twilio's per-message pricing with volume discounts, confirming the usage-based model. While the refinery atom focuses on SMS as a cost line item, the `costes-por-categoria-tenant` thread focuses on per-seat SaaS costs. Both are valid in their domains, but a product using Twilio SMS must track messages per active user to accurately project SMS cost within the per-seat framework, otherwise the per-seat model will understate total cost for high-SMS-frequency products.

## Nota de extensión 2026-11-03
Ampliado a partir de `sources/2026-11-01-twilio-sms-pricing.md` y `sources/2026-11-02-twilio-sms-pricing.md`, con cifras verbatim de la página de precios de US (octubre 2026), que **precifican** la estimación "approximately $0.0075/message" del claim anterior:

- El cobro es **por segmento de 160 caracteres**, no por mensaje: $0.0083 base US para long code, toll-free y short code, saliente y entrante. MMS saliente $0.022 por mensaje plano ([[2026-1101-twilio-sms-base-0-0083-por-segmento-de-160-caracteres]]).
- Sobre la base se suman **cargos de operador** por mensaje ($0.0025–$0.005; $0.02 en short codes FTEU), de modo que el coste real por SMS saliente de un segmento es **$0.0108–$0.0133**, no $0.0075 ([[2026-1101-twilio-cargos-de-operador-por-sms-y-costo-real-por-mensaje]]).
- Los **descuentos por volumen no tienen tabla pública**: se negocian con el account manager, y los descuentos por uso comprometido exigen compromiso anual. No hay Free Trial de SMS; solo "Start for free, no credit card required" ([[2026-1101-twilio-addons-de-features-y-descuentos-no-publicados]], [[2026-1101-twilio-no-publica-cuota-gratuita-de-sms-de-prueba]]).
- La página es **por país** (aquí, US): los precios internacionales solo se obtienen del CSV `SMSPricing.csv` ([[2026-1101-twilio-precios-por-pais-viven-en-un-csv-no-en-la-pagina]]).

La fricción con el "$0.0075/message" del claim original queda registrada en [[2026-1101-twilio-sms-base-0-0083-por-segmento-de-160-caracteres]] y no se resuelve aquí.