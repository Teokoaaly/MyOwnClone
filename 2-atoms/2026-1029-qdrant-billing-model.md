---
id: 2026-1029-qdrant-billing-model
type: atom
certainty: solid
sources: [0-raw/2026-10-29-qdrant-cloud-pricing.md]
links: ["[[2026-1029-qdrant-free-tier]]", "[[2026-1029-qdrant-standard-tier]]"]
---

## Claim

El modelo de billing de Qdrant Cloud se calcula sobre el uso real de recursos durante el período de facturación, incluyendo vCPU, memoria GB, storage GB consumido por clusters, storage GB de backups y tokens de inference de modelos pagados, facturado hourly y monitorizable desde el dashboard.

## Why It Matters

El modelo de uso real permite scaling flexible donde los costos reflejan la consumo efectivo, pero requiere monitorización activa para evitar sorpresas en la factura mensual. A diferencia de planes con precios fijos, el billing hourly y consumption-based significa que picos de uso se traducen directamente en costos mayores, lo que hace importante establecer alertas y presupuestos.

## [FRICTION]

> [[2026-1029-qdrant-standard-tier]] (escrita hace ~21 semanas) afirma que el Standard Tier es "usage-based pricing" para "production workloads", pero no especifica los rangos mínimos de compromiso ni cómo se transiciona del consumo hourly a planes con commitments mensuales —el modelo de billing hourly puede generar facturas variables que son difíciles de predecir para workloads con patrones estacionales o impredecibles, mientras que el Standard Tier promise flexibility sin claridad sobre los costos límite. Ambas describen el mismo tier pero desde perspectivas de modelado de costos distintas sin una respuesta sobre los límites de predictable. Marcado para juicio humano, no auto-resuelto.