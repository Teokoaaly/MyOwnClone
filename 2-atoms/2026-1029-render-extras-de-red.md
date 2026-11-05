---
id: 2026-1029-render-extras-de-red
type: atom
certainty: solid
sources: [sources/2026-10-29-render-pricing.md]
links: ["[[2026-1029-render-planes-pro-scale]]", "[[2026-1029-render-bandwidth-overage]]", "[[2026-1029-render-enterprise-compliance]]"]
---

## Claim
Render cobra como extras de red las IPs dedicadas a $100/mes por cada conjunto de IPs (solo Pro y Scale, "Custom" en Enterprise), los AWS Private Links a $30/mes incluyendo hasta 3 enlaces (Pro y Scale), el tráfico saliente por private link a $0,03/GB (Pro y Scale) y los dominios custom adicionales a $0,25/dominio/mes tras los incluidos (2 en Hobby, 15 en Pro, 25 en Scale).

## Why It Matters
Ninguno de estos extras cabe en el presupuesto de ≤ 4 EUR/mes, pero cada uno revela una presión de coste concreta. Las IPs dedicadas a $100/mes exigen aislamiento de reputación de envío: es un coste fijo que se paga aunque el volumen sea cero, exactamente el tipo de partida que el eje "coste por asiento frente a coste de infraestructura" del vault quiere separar del gasto variable. Los dominios a $0,25/mes sí son baratos y son relevantes para un modelo multi-tenant donde cada tenant quiere su propio dominio de envío — 25 incluidos en Pro cubren 25 tenants sin coste adicional. Los private links a $30/mes solo tienen sentido para alcanzar infra propia en AWS, lo que no encaja con una estrategia de infraestructura en la UE y con el límite de 4 EUR/mes documentado en [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]].

## [FRICTION]
> No conflicting atom found. This is an add-on price atom with no direct contradiction in the current vault. No [FRICTION] block added.
