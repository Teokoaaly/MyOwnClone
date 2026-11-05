--- 
id: 20261029-vercel-waf-custom-rules
type: atom
certainty: solid
sources: [0-raw/2026-10-29-vercel-pricing.md]
links: ["[[20261029-vercel-hobby-plan-limits]]", "[[20261029-vercel-access-security-mfa-sso]]"]
--- 

## Claim
Vercel Firewall custom firewall rules are tiered by plan: Hobby gets 0, Pro gets up to 3, and Enterprise gets up to 250 custom rules, with all plans including OWASP Core Ruleset (managed) and Bot Management features.

## Why It Matters
Custom firewall rule capacity is a key differentiator between plans. Hobby sites have no custom rule capability, Pro sites are limited to 3 rules (sufficient for basic IP blocking or simple adjustments), and Enterprise sites can deploy 250 rules for complex security policies. This tiering affects the security posture possible for each plan level.

## [FRICTION]
> [[20261029-vercel-hobby-plan-limits]] (escrita hace ~21 semanas) afirma que Hobby "$0/mo" tiene "strict usage caps" y "no permite comprar uso adicional". Este átomo no entra en fricción directa, pero refuerza el patrón de tiering: al igual que Hobby no puede comprar uso adicional, tampoco puede obtener reglas de firewall personalizadas, ambos siendo límites de "base plan" que empujan a los usuarios hacia Pro o Enterprise para funcionalidades avançadas.