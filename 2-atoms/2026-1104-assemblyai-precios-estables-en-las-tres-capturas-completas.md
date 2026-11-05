---
id: 2026-1104-assemblyai-precios-estables-en-las-tres-capturas-completas
type: atom
certainty: solid
sources: [sources/2026-11-04-assemblyai-pricing.md, sources/2026-11-02-assemblyai-pricing.md, sources/2026-11-01-assemblyai-pricing.md]
links: ["[[2026-1101-assemblyai-tarifas-por-hora-no-por-minuto]]", "[[2026-1101-assemblyai-realtime-3-6-pro-045-y-streaming-015]]", "[[2026-1103-assemblyai-captura-reducida-solo-pre-recorded-expandido]]"]
---

## Claim
El catálogo de precios de AssemblyAI lleva **tres capturas completas consecutivamente sin mover un centavo** (11-01, 11-02 y 11-04): un `diff` línea a línea entre `sources/2026-11-02-assemblyai-pricing.md` y `sources/2026-11-04-assemblyai-pricing.md` solo devuelve la fecha de captura y el hash de despliegue de Vercel en dos URLs de imagen. Se re-verifican literalmente: pre-recorded **Universal-3.5 Pro $0,21/hr** y **Universal-2 $0,15/hr**; realtime **Universal-3.6 Pro Realtime $0,45/hr**, **Universal-Streaming $0,15/hr** y **Universal-Streaming Multilingual $0,15/hr**; **Sync API $0,30/hr**; **Dictation API $0,62/hr**; **AssemblyAI-TTS-1 $15/1M caracteres**; add-ons de pre-recorded (Keyterms $0,05/hr vs "Included", Prompting $0,05/hr vs "Not supported", Diarization $0,02/hr en ambos, Medical Mode $0,15/hr en ambos); add-ons de realtime (Keyterms "Included" vs $0,04/hr, Diarization $0,12/hr, PII Text Redaction $0,12/hr, Voice Focus $0,10/hr, Prompting $0,05/hr, Medical Mode $0,15/hr); Speech Understanding; Guardrails; y el LLM Gateway con sus 58 modelos.

## Why It Matters
Tres renders completos idénticos es el umbral razonable para declarar **estabilidad de tarifa** y no solo "sin novedad detectada": a partir de aquí cualquier cambio futuro en la página de precios es un cambio real y no ruido de captura. Es el mismo patrón de verificación que el vault ya aplicó a Backblaze y Deepgram, y sirve de contrapeso al átomo anterior sobre el recorte del 11-03 ([[2026-1103-assemblyai-captura-reducida-solo-pre-recorded-expandido]]), que dejó el catálogo sin verificar un día: hoy queda **re-verificado en su totalidad** contra la fuente vigente. Consecuencia operativa: la palabra "Pay as you go" de la columna de precios es literalmente el precio de lista que puede usarse en cualquier proyección de coste del vault —$0,15/hr de suelo en Universal-2, $0,45/hr de techo de realtime ([ver [[2026-1101-assemblyai-realtime-3-6-pro-045-y-streaming-015]]])— sin margen de descuento asumible, porque los descuentos por volumen siguen sin publicarse.
