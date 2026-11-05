---
id: 2026-1029-qdrant-migration-oss
type: atom
certainty: solid
sources: [0-raw/2026-10-29-qdrant-cloud-pricing.md]
links: ["[[2026-1029-qdrant-free-tier]]", "[[2026-1029-qdrant-standard-tier]]"]
---

## Claim

Qdrant proporciona una herramienta de documentación y migration para migrar desde Qdrant OSS a Qdrant Cloud, permitiendo a los usuarios trasladar sus despliegues autogestionados al modelo fully managed con mínimos cambios en la configuración.

## Why It Matters

La migration from OSS to Cloud elimina la carga operativa de mantener la infraestructura propia mientras se conservan las mismas APIs y funcionalidades. Esto es particularmente relevante para equipos que comienzan con OSS para luego escalar a Cloud cuando necesitan HA, backup & DR o features gestionadas que no están disponibles o son complejas de operar en OSS.

## [FRICTION]

> [[2026-1029-qdrant-standard-tier]] (escrita hace ~21 semanas) afirma que el upgrade desde Free Tier a Standard "es fácil" y proporciona "a dedicated cluster", pero el proceso de migration desde OSS a Cloud puede implicar más de lo que la fuente indica —export/import de datos, compatibilidad de schemas, y posibles diferencias en el comportamiento de los queries entre OSS y la versión managed pueden crear fricción oculta que no quede documentada en el upgrade path descrito. Ambas pueden ser ciertas en diferentes grados dependiendo de la complejidad del deployment OSS existente, pero la experiencia real de usuario puede variar significativamente. Marcado para juicio humano, no auto-resuelto.