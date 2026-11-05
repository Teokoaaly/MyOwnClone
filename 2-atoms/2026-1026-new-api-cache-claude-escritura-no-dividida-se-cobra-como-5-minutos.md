---
id: 2026-1026-new-api-cache-claude-escritura-no-dividida-se-cobra-como-5-minutos
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-precios-por-ratio-y-expresion]]", "[[2026-1026-new-api-cache-12h-openai-2-5x-y-precios-gpt-6-astra]]", "[[2026-1023-priceai-transit-dispersion-de-multiplicadores]]"]
---

## Claim
**v1.0.0-rc.47** corrige un hueco de facturación en **Claude**: las escrituras de caché que **no estaban divididas** en tramos de 5 minutos y 1 hora **no se facturaban** (quedaban sin cobrar). A partir de esta versión, **la parte no dividida se cobra como escritura de 5 minutos**.

## Why It Matters
Es un fallo de ingresos, no de funcionalidad: el gateway estaba **dejando de cobrar** tráfico de caché de Claude. La lección para el vault es de auditoría de cobros: un motor de precios con varias capas de caché (5 min, 1 h, 12 h) multiplica los puntos donde un tramo puede **escaparse sin facturar** — y aquí el modo de fallo era silencioso, sin error ni log de discrepancy.
El efecto agregado sobre un relay es exactamente el tipo de dispersión que el vault mide entre canales ([[2026-1023-priceai-transit-dispersion-de-multiplicadores]]): dos despliegues del mismo software con **versiones distintas** facturan distinto sin que ninguna tabla lo refleje, porque la diferencia está en la versión, no en el multiplicador publicado.
Y conecta con el otro hueco de caché de la misma versión ([[2026-1026-new-api-cache-12h-openai-2-5x-y-precios-gpt-6-astra]]): los dos cambios de rc.47 apuntan al mismo sitio —**la caché es donde el multiplicador publicado se convierte en dinero real**, y donde el motor de expresiones ([[2026-1023-new-api-precios-por-ratio-y-expresion]]) tiene que acertar al detalle.
