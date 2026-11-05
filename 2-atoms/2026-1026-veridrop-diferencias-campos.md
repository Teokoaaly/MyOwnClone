---
id: 2026-1026-veridrop-diferencias-campos
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-openai-detection.md]
links: ["[[2026-1026-veridrop-profundidades-deteccion]]", "[[2026-1026-veridrop-firma-usage-field]]"]
---

## Claim
Veridrop registra las diferencias de flujo stream/non-stream y la estructura del campo `usage` para identificar capas de envoltorio y adaptaciones de protocolo. Las capas comunes de empaquetado suelen introducir inconsistencia en el modo streaming y campos `usage` con forma distinta a la especificación oficial de OpenAI, lo que se marca como indicio de relay no auténtico.

## Why It Matters
Las capas de adaptación entre protocolos a menudo dejan "firmas" de su presencia en la inconsistencias de streaming y en la estructura del uso de tokens. Detectar estas anomalías ayuda a distinguir un relay que simplemente traduce el protocolo OpenAI de uno que está haciendo adaptaciones arbitrarias que podrían perder o modificar campos críticos. Esto es relevante para desarrolladores que integran relays y necesitan predecibilidad de la respuesta.

## [FRICTION]
> [[2026-1027-veridrop-json-schema-estricto-y-el-flag-markdown-json-seen]] (escrita hace ~5 semanas) usa el flag de schema estricto como instrumento de diagnóstico diferencial para distinguir fallo de configuración del relay de sustitución de modelo. Este átomo (2026-1026) coincide en la utilidad del flag pero llega a una conclusión distinta sobre el síntoma: la nota de 2026-1027 asocia el flag estrictamente a errores de formato JSON/markdown, mientras que este átomo (2026-1026) lo asocia a inconsistencias de streaming y estructura de usage como señales de adaptación de protocolo, no necesariamente errores de serialización. Ambas pueden ser correctas: el flag de schema estricto puede indicar ambos tipos de problemas, y la distinción depende del contexto del error. Dado que el flag es un booleano diagnóstico diferencial, ambas notas describen aspectos diferentes del mismo herramienta sin contradicción auto-resuelta.