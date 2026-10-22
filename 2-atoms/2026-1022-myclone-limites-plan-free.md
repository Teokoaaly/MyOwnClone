---
id: 2026-1022-myclone-limites-plan-free
type: atom
certainty: solid
sources: [raw/articles/myownclone-technical-deep-dive-2026-06-23.md, raw/articles/myclone-deep-api-osint-2026-06-24.md]
links: ["[[2026-1022-myclone-knowledge-library-fuentes]]", "[[2026-1022-myclone-widget-embed-modos]]", "[[2026-1022-precio-99-mensual]]", "[[myownclone]]", "[[2026-1022-myclone-tier-plans-usage-api]]"]
---
## Claim
El plan Free de MyClone.is tiene límites verificados en tiempo real (23 jun 2026): 2 personas máximo (1 activa), 5 archivos de texto raw (50MB total), 3 documentos (150MB total), 3 archivos audio/video (500MB total, 1h de duración), 0 transcripciones de YouTube, 500 mensajes de texto al mes, 10 minutos de voz al mes, solo modo embed `bubble` y 0 API tokens (Pro+). Los contadores se reinician el día 1 de cada mes.

## Why It Matters
Es un freemium de bajo coste y de conversión rápida: el consumo real (500 mensajes + 10 min de voz) es lo que una persona hace en minutos si el embed está en producción, lo que empuja la conversión a Pro casi de inmediato. Para [[myownclone]], cuyo plan más barato es 99 €/mes ([[2026-1022-precio-99-mensual]]), el suelo de entrada de MyClone.is fija un ancla de precio muy por debajo. La existencia de contadores en tiempo real con fecha de reset visible es la "transparencia de uso" que el informe señala como anti-churn, y [[myownclone]] solo expone uso en `/admin/usage` interno, sin fecha de reset.

## Extensión (API OSINT 2026-06-24)
El endpoint `/tier/usage` devuelve los contadores del Free con `reset_date` explícito `2026-07-01T00:00:00+00:00` para texto y voz, desglosados por categoría (`raw_text`, `documents`, `multimedia`, `youtube`, `voice`, `text`, `personas`). Matiz: la categoría `youtube` aparece con `videos.limit 5` y `duration.limit_hours 2` — es decir, el límite de 0 transcripciones de YouTube de la nota anterior se refiere al contenido ya ingerido, no al cupo del contador. Ver [[2026-1022-myclone-tier-plans-usage-api]] para el modelo de planes escribibles por el creator.
