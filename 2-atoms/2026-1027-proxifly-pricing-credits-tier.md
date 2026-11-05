---
id: 2026-1027-proxifly-pricing-credits-tier
type: atom
certainty: solid
sources: [sources/2026-10-27-proxifly-pricing.md]
links: ["[[2026-1027-proxifly-pricing-proxy-types]]", "[[2026-1027-proxifly-pricing-country-coverage]]"]
---

## Claim
Proxifly uses a credit-based pricing tier system where Free gets 100 credits, Plus gets 500, Pro gets 3,000, and Max gets 10,000 credits, with credits resetting each billing cycle and unused credits not rolling over.

## Why It Matters
The credit allocation creates a steep power gradient between tiers: Free users can only make minimal API calls, while Max plan users have orders of magnitude more capacity. This structure determines not just volume but also access to higher-tier features like dedicated proxies and full API availability, making the credit count the primary discriminator between plans.

## [FRICTION]
> [[2026-1027-proxifly-pricing-proxy-types]] (escrita hace pocas semanas) afirma que el acceso a tipos de proxy depende del plan, y que SOCKS4 solo está en Plus mientras que todos los tipos (incluido SOCKS5) están en Pro y superior. Esta nota no aborda si los créditos también desbloquean tipos específicos o si es solo una cuestión de cuota de API, lo que deja abierta la pregunta de si los créditos son un recurso universal o tienen restricciones protocolares. Ambas afirmaciones pueden ser ciertas: los créditos pueden ser el "combustible" y los tipos de proxy la "válvula", o pueden estar acoplados de manera más estrecha. Marcado para juicio humano, no auto-resuelto.