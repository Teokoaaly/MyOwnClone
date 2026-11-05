---
id: 2026-10-29-supabase-compute-pricing
type: atom
certainty: solid
sources: [sources/2026-10-29-supabase-pricing.md]
links: ["[[2026-10-29-neon-pricing-scaleplan]]", "[[2026-10-29-workers-compute-cpu]]"]
---

## Claim

Supabase Compute pricing ranges from Micro at $10/month (1 GB RAM, shared compute, 60 direct / 200 pooler connections) to 16XL at $3,730/month (64 vCPUs, 256 GB RAM); paid plans include $10/month in compute credits sufficient to cover one Micro instance.

## Why It Matters

The compute credit inclusion and granular instance sizing allow projects to scale from tiny prototypes to large workloads, but the $10 credit covers only the Micro size — larger projects bear full compute costs, making instance selection a critical cost-determination decision.

## [FRICTION]

> [[2026-10-29-neon-pricing-scaleplan]] has a typical monthly spend of $701 based on high load with 100 GB storage, offering $0.222 per CU-hr, while Supabase Micro at $10/mo is based on shared compute with 1 GB RAM — the pricing models differ in what is included (Supabase credits vs. Neon's CU-based metering) and the unit economics (flat monthly vs. per-CU-hr), making direct comparison difficult without mapping compute units to concrete workloads.

> Ambas describen costos de compute para cargas de trabajo altas, pero Neon cobra por CU-hrs consumidos mientras Supabase cobra una tarifa plana mensual con créditos incluidos — el modelo de Neon es pay-per-use y el de Supabase es subscribe-and-credit, lo que means that sustained high usage may favor one model over the other depending on usage patterns. Marcado para juicio humano, no auto-resuelto.