---
id: 2026-1027-proxifly-pricing-proxy-types
type: atom
certainty: solid
sources: [sources/2026-10-27-proxifly-pricing.md]
links: ["[[2026-1027-proxifly-pricing-credits-tier]]", "[[2026-1027-proxifly-pricing-country-coverage]]"]
---

## Claim
Proxy type access escalates across Proxifly tiers: Free offers HTTP only, Plus adds SOCKS4, Pro unlocks all proxy types (including SOCKS5 and premium), and Max adds dedicated proxies alongside all other types.

## Why It Matters
The protocol escalation means that scraping workflows requiring SOCKS5 or dedicated IPs are locked behind higher-priced plans. Developers starting with HTTP-only needs can begin on Free, but any requirement for SOCKS protocol or IP exclusivity forces an upgrade path that can double or triple the monthly cost.

## [FRICTION]
> [[2026-1027-proxifly-pricing-credits-tier]] (escrita hace pocas semanas) afirma que los créditos son el recurso principal que determina el acceso a features, y que la distribución de créditos crea un gradiente de poder entre tiers. Sin embargo, esta nota trata el acceso a tipos de proxy como una cuestión de límite de API por tipo, no como una restricción de créditos. Ambas pueden ser ciertas: los créditos pueden ser el "combustible" y los tipos de proxy la "válvula", o pueden estar acoplados de manera más estrecha donde ciertos tipos requieren créditos mínimos por request. La fricción radica en si los créditos son un recurso universal o tienen restricciones protocolares — si un request SOCKS5 consume más créditos que un request HTTP equivalente. Marcado para juicio humano, no auto-resuelto.