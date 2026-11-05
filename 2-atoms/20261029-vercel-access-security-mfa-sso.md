--- 
id: 20261029-vercel-access-security-mfa-sso
type: atom
certainty: solid
sources: [0-raw/2026-10-29-vercel-pricing.md]
links: ["[[20261029-vercel-hobby-plan-limits]]", "[[20261029-vercel-regional-pricing]]"]
--- 

## Claim
Vercel Access & Deployment Security features are tiered: Multi-Factor Authentication (MFA) is available across all plans, Role-Based Access Control (RBAC) Team level is free, but SAML Single Sign-On costs $300/mo and is Enterprise-grade, while Password Protection costs $20/project/mo. Static IPs (shared pool) cost $100/project/mo with per-GB bandwidth charges starting at $0.15/GB.

## Why It Matters
Security features create a clear progression from basic (MFA, RBAC Team) to advanced (SSO, Static IPs) as teams grow. The $300/mo SSO cost is significant for enterprises requiring centralized identity management, while the $20/project/mo Password Protection is a lower-cost option for individual projects. Static IPs at $100/project/mo + $0.15/GB are for teams needing fixed outbound IPs for outbound connectivity or whitelisting.

## [FRICTION]
> [[20261029-vercel-regional-pricing]] (escrita hace ~21 semanas) indica que los precios varían por región. Este átomo presiona esa creencia porque el SSO a $300/mo y el IP dedicado a $100/project/mo + $0.15/GB podrían tener costos efectivos diferentes dependiendo de la región de facturación — los impuestos y tasas locales podrían incrementar el precio mostrado de $300 a una cantidad superior en regiones con impuestos altos. No hay fricción técnica, pero el costo real "landed price" variaría por región mientras que el precio listado permanece en USD.

> [[20261029-vercel-hobby-plan-limits]] (escrita hace ~21 semanas) afirma que Hobby "$0/mo" no puede comprar uso adicional. Este átomo refuerza el patrón: las características de seguridad también siguen el tiering de planes, y Hobby no incluye SSO, Static IPs, o Password Protection como características nativas — estos son escalas hacia Pro/Enterprise, consistente con la restricción de Hobby de no poder comprar adicionalmente.