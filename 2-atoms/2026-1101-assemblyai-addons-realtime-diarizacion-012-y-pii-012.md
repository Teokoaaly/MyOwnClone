---
id: 2026-1101-assemblyai-addons-realtime-diarizacion-012-y-pii-012
type: atom
certainty: solid
sources: [sources/2026-11-01-assemblyai-pricing.md]
links: ["[[2026-1101-assemblyai-addons-prerecordado-diarizacion-keyterms-medical]]", "[[2026-1101-assemblyai-realtime-3-6-pro-045-y-streaming-015]]", "[[2026-1022-separacion-de-hablantes-en-entrevistas]]"]
---

## Claim
En el Realtime Speech-to-Text de AssemblyAI los add-on cues mucho más caros que en pre-recorded: **Speaker Diarization $0.12/hr** (en ambos modelos, frente a $0.02/hr en pre-recorded, exactamente **6×**), **PII Text Redaction $0.12/hr** (en ambos), **Voice Focus $0.10/hr** ("New", solo en Universal-3.6 Pro Realtime, "Not supported" en Universal-Streaming), **Keyterms Prompting $0.04/hr** (solo en Universal-Streaming; "Included" en 3.6 Pro, con límite de 100 palabras frente a las 1000 del pre-recorded), **Prompting $0.05/hr** (solo 3.6 Pro) y **Medical Mode $0.15/hr** (ambos).

## Why It Matters
La comparación entre las dos modalitys es la que importa para el vault: la diarización cuesta **$0.02/hr** si el audio ya está grabado (el flujo de entrevista de [[2026-1022-separacion-de-hablantes-en-entrevistas]]) y **$0.12/hr** si la misma función se aplica en directo. Sobre el modelo realtime barato (Universal-Streaming $0.15/hr) la diarización casi duplica el precio: $0.15 → $0.27/hr. Sobre 3.6 Pro Realtime ($0.45/hr) la suma de diarización + Voice Focus + PII redaction lleva a **$0.79/hr**, un 76 % sobre el precio del modelo. Y PII Text Redaction no es un extra opcional en un producto multi-tenant: [[2026-1022-costes-por-categoria-tenant]] separa qué consume la plataforma y qué se factura al tenant, y la redacción de PII a $0.12/hr es exactamente el tipo de coste variable que debe ir en la categoría facturable al cliente, con su propia línea en el panel de costes.
