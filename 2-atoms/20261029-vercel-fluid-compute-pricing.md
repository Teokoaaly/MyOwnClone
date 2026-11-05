--- 
id: 20261029-vercel-fluid-compute-pricing
type: atom
certainty: solid
sources: [0-raw/2026-10-29-vercel-pricing.md]
links: ["[[20261029-vercel-hobby-plan-limits]]", "[[20261029-vercel-flat-rate-cdn]]"]
--- 

## Claim
Fluid Compute pricing is based on actual execution time: "No idle, no waste" — only pay for actual execution time, not idle resources, with 4 hours/mo included on Hobby and Fluid Active CPU starting at $0.128/hr, Fluid Provisioned Memory at $0.0106/GB-hr.

## Why It Matters
Traditional serverless pricing charges for provisioned time regardless of actual usage. Fluid Compute's active CPU pricing means you only pay when code is actually running, which can significantly reduce costs for workloads with sporadic or variable execution patterns. This is particularly valuable for background jobs, webhooks, and infrequent API calls.

## [FRICTION]
> [[20261029-vercel-flat-rate-cdn]] (escrita hace ~21 semanas) ofrece un precio fijo mensual independientemente del uso. Este átomo presiona esa creencia porque Fluid Compute es inherentemente variable — pagas por lo que usas, lo que puede ser menos predecible que el Flat Rate CDN. Sin embargo, pueden coexistir: Flat Rate cubre CDN y recursos de red, mientras que Fluid Compute cubre tiempo de ejecución de funciones, y un equipo Pro puede elegir ambos dependiendo de su patrón de tráfico.