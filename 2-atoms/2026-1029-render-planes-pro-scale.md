---
id: 2026-1029-render-planes-pro-scale
type: atom
certainty: solid
sources: [sources/2026-10-29-render-pricing.md]
links: ["[[2026-1029-render-hobby-plan]]", "[[2026-1029-render-compute-per-second]]", "[[2026-1029-render-enterprise-compliance]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]"]
---

## Claim
Render ofrece cuatro planes de workspace: Hobby $0/mes, Pro $25/mes, Scale $499/mes y Enterprise a precio personalizado, todos etiquetados "+ compute"; Pro añade asientos y servicios ilimitados, 25 GB de ancho de banda, previews full-stack, autoscaling horizontal, entornos aislados y autenticación OIDC, y Scale añade 1 TB de ancho de banda, workspaces múltiples, SAML SSO, SCIM, RBAC avanzado y workspaces HIPAA.

## Why It Matters
El salto Hobby → Pro es de $25/mes solo de suscripción, es decir 6,25× el presupuesto duro de ≤ 4 EUR/mes del vault, y el compute se cobra aparte: para MyOwnClone (Flask + Next.js + Postgres + Redis + Weaviate) el primer servicio real ya pagaría una instancia de $7/mes o más encima. Render solo es viable en la configuración Hobby con instancias gratuitas, y solo como prototipos o para el pipeline de inferencia intermitente. La comparación relevante es contra [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]: un CPX02 de Hetzner a 5,99 EUR/mes ya no cabe en 4 EUR, y Render escala peor desde ese suelo. El plan Pro importa más por su propio eje de coste: [[2026-1029-render-compute-per-second]] muestra que el cómputo se prorratea al segundo, así que la suscripción fija es el piso real del gasto.

## [FRICTION]
> [[2026-1029-render-hobby-plan]] afirma que Hobby no incluye dominios custom ni firewall ("no custom domains or firewall, no DDoS mitigation"). La captura de 2026-10-29 lista en las features de Hobby "Custom domains" y "Firewall & DDoS mitigation", y la tabla da 2 dominios custom incluidos en Hobby y mitigación automática de DDoS. Ambas no pueden ser completamente correctas. Marcado para juicio humano, no auto-resuelto.
