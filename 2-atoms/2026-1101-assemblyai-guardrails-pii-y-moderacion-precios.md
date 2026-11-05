---
id: 2026-1101-assemblyai-guardrails-pii-y-moderacion-precios
type: atom
certainty: solid
sources: [sources/2026-11-01-assemblyai-pricing.md]
links: ["[[2026-1022-guardarrail-no-alucinar]]", "[[2026-1022-costes-por-categoria-tenant]]", "[[2026-1022-superficie-legal-publica-dpa-clon-terms]]"]
---

## Claim
El bloque Guardrails de AssemblyAI se factura por hora y por función: **Profanity Filtering $0,01/hr**, **PII Audio Redaction $0,05/hr** ("Identify and remove PII from the audio file before it is returned to you"), **PII Text Redaction $0,08/hr** ("Identify and remove PII from the transcription text before it is returned to you" — en el bloque Guardrails; en la tabla de add-ons de Realtime la misma función aparece a $0,12/hr, ver [[2026-1101-assemblyai-addons-realtime-diarizacion-012-y-pii-012]]) y **Content Moderation $0,15/hr** ("Detect sensitive content in your audio and video files"). La página lo describe como "Guardrails ensures only high-quality, safe, and compliant content flows through your applications".

## Why It Matters
Es la partida que protege al clon de sus dos riesgos legales más citados en el vault: la exposición de datos personales en material de terceros y la superficie legal que el producto ya declara en [[2026-1022-superficie-legal-publica-dpa-clon-terms]]. El coste es bajo en términos absolutos pero **no trivial en el pipeline completo**: redacción de PII en el texto ($0,08) más en el audio ($0,05) más moderación ($0,15) suman $0,28/hr, es decir **casi el doble del modelo de transcripción** (Universal-2 a $0,15/hr). Sobre 100 horas/mes el bloque completo pasa de $15 a $43. La lectura para el modelo de coste multi-tenant es que los guardrails son infrastructure de seguridad que **debe facturarse al tenant o absorber como categoryPlatformOps** ([[2026-1022-costes-por-categoria-tenant]]): si se factura al tenant, es una línea variable más en el MRR; si se absorbe, es una línea fija que se multiplica por el número de tenants activos, igual que el hosting que ya se sabe que no cabe en ≤ €4/mes. Y en el eje de calidad, guardrails está en la misma familia que el guardarrail de no-alucinación del producto ([[2026-1022-guardarrail-no-alucinar]]): costea directamente contra la promesa.
