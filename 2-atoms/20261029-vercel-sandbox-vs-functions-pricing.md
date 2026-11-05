--- 
id: 20261029-vercel-sandbox-vs-functions-pricing
type: atom
certainty: solid
sources: [0-raw/2026-10-29-vercel-pricing.md]
links: ["[[20261029-vercel-fluid-compute-pricing]]", "[[20261029-vercel-ai-gateway-token-pricing]]"]
--- 

## Claim
Vercel offers two distinct function runtimes with separate pricing: Functions (Fluid Compute with Active CPU at $0.128/hr and Provisioned Memory at $0.0106/GB-hr, 1M invocations included at $0.60/1M) and Sandbox (separate Active CPU at $0.128/hr, Provisioned Memory at $0.0212/GB-hr, 5K included creations at $0.60/1K creations), with Sandbox creations priced independently from Function invocations.

## Why It Matters
Teams can choose between Functions and Sandbox based on their needs: Sandbox provides isolated execution environment useful for certain workloads, but carries separate pricing. The "Sandbox Creations" cost (per 1,000 creations) is distinct from "Function Invocations" (per 1M invocations), meaning the cost model changes depending on whether you're running long-running daemons vs. on-demand functions. This split requires careful modeling when migrating or designing architecture.

## [FRICTION]
> [[20261029-vercel-ai-gateway-token-pricing]] (escrita hace ~21 semanas) cubre el costo de requests de AI Gateway a $3.00/1K. Este átomo observa que AI Gateway es un servicio de capa superior independiente de ambos runtimes de funciones — no hay fricción técnica, pero el modelo de tres capas (Sandbox/Functions pricing + AI Gateway pricing) añade complejidad de costos que los equipos deben trackear por separado en lugar de unificar bajo un solo costo de ejecución.

> [[20261029-vercel-fluid-compute-pricing]] (escrita hace ~21 semanas) describe Fluid Active CPU y Provisioned Memory pricing. Este átomo aclara que Sandbox comparte los mismos precios base de Active CPU ($0.128/hr) pero diverge en Provisioned Memory ($0.0212/GB-hr frente a $0.0106/GB-hr de Functions) y creations ($0.60/1K creations frente a $0.60/1M invocations), lo que significa que migrar de Functions a Sandbox o viceversa no es un cambio de pricing lineal y requiere re-modelado de costos por caso de uso.