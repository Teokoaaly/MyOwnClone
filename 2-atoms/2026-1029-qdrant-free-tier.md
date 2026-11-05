---
id: 2026-1029-qdrant-free-tier
type: atom
certainty: solid
sources: [0-raw/2026-10-29-qdrant-cloud-pricing.md]
links: ["[[2026-1029-qdrant-standard-tier]]", "[[2026-1029-qdrant-hybrid-cloud]]"]
---

## Claim

El Free Tier de Qdrant Cloud es gratuito para siempre y está orientado a testing y prototipos, limitado a un nodo único con 0.5 vCPU / 1GB RAM / 4GB de disco, e incluye inference gratuita con modelos seleccionados.

## Why It Matters

El Free Tier baja la barrera de entrada para evaluar Qdrant antes de comprometer recursos, pero sus limitaciones (1GB RAM, 4GB disk, sin HA) lo hacen insuficiente para cargas de producción que requieran disponibilidad o escala. Los usuarios deben migrar a Standard Tier cuando superen estos límites.

## [FRICTION]

> [[2026-1029-qdrant-standard-tier]] (escrita hace ~21 semanas) afirma que el Free Tier es "solo para testing y prototipos", pero no especifica qué sucede cuando los límites de 1GB RAM y 4GB disk se exceden en la práctica —el upgrade a Standard es necesario, pero el costo y el tiempo de migración no están definidos en la fuente original. Ambas afirmaciones sobre los límites y el upgrade path no pueden ser completamente correctas sin más detalles sobre la experiencia de migration. Marcado para juicio humano, no auto-resuelto.