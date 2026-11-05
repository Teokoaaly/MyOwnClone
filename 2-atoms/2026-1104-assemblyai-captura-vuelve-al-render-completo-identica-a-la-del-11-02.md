---
id: 2026-1104-assemblyai-captura-vuelve-al-render-completo-identica-a-la-del-11-02
type: atom
certainty: solid
sources: [sources/2026-11-04-assemblyai-pricing.md, sources/2026-11-02-assemblyai-pricing.md, sources/2026-11-03-assemblyai-pricing.md]
links: ["[[2026-1103-assemblyai-captura-reducida-solo-pre-recorded-expandido]]", "[[2026-1101-assemblyai-tarifas-por-hora-no-por-minuto]]"]
---

## Claim
La quinta captura de `https://www.assemblyai.com/pricing` (**2026-11-04**) vuelve al **render completo** —4.663 palabras, 42.954 bytes, 1.038 líneas— y es **idéntica línea a línea a la del 2026-11-02**: un `diff` normalizando el hash de despliegue de Vercel (`dpl_G5Bf9LrY3zVCFR26Bb2FNSYBjDpL` → `dpl_5ge5AjnmEruCNULSvpd9Koir4UXG`, en las dos URLs de imágenes del bloque Security y Playground) no devuelve **ninguna** diferencia de contenido. La captura del 11-03 (720 palabras, 3.446 bytes, solo Pre-recordado con el resto colapsado a "...") queda así como un **fallo puntual de renderizado**, no como un estado estable de la página.

## Why It Matters
El precedente del vault era que el recorte del 11-03 era interpretable como "la página ya solo renderiza Pre-recorded" (ver [[2026-1103-assemblyai-captura-reducida-solo-pre-recorded-expandido]]). El 11-04 lo refuta de forma fuerte: **el mismo día del ciclo devuelve el mismo contenido exacto que el 11-02**, con una única diferencia —el hash de build de las imágenes—, lo que confirma que el pipeline de captura es **intermitente y no determinista** y que la fuente vigente del catálogo completo es `sources/2026-11-04-assemblyai-pricing.md` (o, equivalentemente, la del 11-02). La lección operativa es la misma que ya se extrajo del caso 5sim y Azure Architecture Center: **el `word_count` de una captura es un indicador de calidad de captura antes que un metadato**, y una captura reducida nunca puede sostener una afirmación sobre el resto del catálogo, ni en el sentido de "el precio se ha retirado" ni en el de "la sección ha desaparecido". Para el hilo de voz y transcripción, esto significa que las cifras de Realtime, Sync, Dictation, TTS, Speech Understanding, Guardrails y LLM Gateway pueden volver a reverificarse hoy contra la fuente (ver [[2026-1101-assemblyai-tarifas-por-hora-no-por-minuto]]).
