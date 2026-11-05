--- 
id: 20261029-vercel-ai-gateway-token-pricing
type: atom
certainty: solid
sources: [0-raw/2026-10-29-vercel-pricing.md]
links: ["[[20261029-vercel-hobby-plan-limits]]", "[[20261029-vercel-fluid-compute-pricing]]"]
--- 

## Claim
AI Gateway token requests cost $3.00 per 1,000 requests with pass-through token costs added on top, providing observability, spend monitoring, load balancing, automatic retries, and embedding support for AI features built on Vercel.

## Why It Matters
AI Gateway is the pricing entry point for AI features on Vercel. At $3.00 per 1,000 requests plus the underlying model token costs, it represents a measurable operational cost for AI-powered applications. The included 500 requests/month on the base plan and custom pricing for higher volume make it important to model costs when building AI-assisted features.

## [FRICTION]
> [[20261029-vercel-fluid-compute-pricing]] (escrita hace ~21 semanas) cubre el costo de ejecución de funciones serverless. Este átomo presiona esa creencia porque AI Gateway token requests ($3.00/1K) son un costo operativo separado y adicional al costo de ejecución de funciones — no hay fricción técnica, pero representan una capa de gasto distinto que los equipos que no contemplan IA como parte de su stack pueden pasar por alto al estimar costos totales de Vercel.