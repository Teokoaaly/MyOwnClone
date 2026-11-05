---
id: 2026-1101-assemblyai-addons-prerecordado-diarizacion-keyterms-medical
type: atom
certainty: solid
sources: [sources/2026-11-01-assemblyai-pricing.md, sources/2026-11-03-assemblyai-pricing.md]
links: ["[[2026-1101-assemblyai-tarifas-por-hora-no-por-minuto]]", "[[2026-1022-separacion-de-hablantes-en-entrevistas]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---

## Claim
Los add-ons del Pre-recorded Speech-to-Text de AssemblyAI se cobran como **$/hr adicionales al modelo base** y no están incluidos en el precio del modelo salvo indicación explícita: **Speaker Diarization $0.02/hr** (igual en Universal-3.5 Pro y en Universal-2), **Keyterms Prompting $0.05/hr** en Universal-3.5 Pro pero **"Included"** en Universal-2, **Prompting $0.05/hr** en Universal-3.5 Pro y **"Not supported"** en Universal-2, y **Medical Mode $0.15/hr** en ambos (etiquetado "New", "Optimize transcription for medical terminology and healthcare conversations"). Keyterms acepta "up to 1000 words or phrases (maximum 6 words per phrase)".

## Why It Matters
El caso de la diarización es el que más toca al vault: el flujo de entrevistas que describe [[2026-1022-separacion-de-hablantes-en-entrevistas]] necesita "saber quién es el hablante uno y quién eres tú" para que el retrieval no mezcle la voz del entrevistador con la del entrevistado — es exactamente Speaker Diarization. Su coste real es **$0.02/hr por encima del modelo**, o sea +13,3 % sobre Universal-2 ($0.15 → $0.17/hr) y +9,5 % sobre Universal-3.5 Pro ($0.21 → $0.23/hr): una partida pequeña pero **no nula**, y que hay que facturar aparte si el producto la ofrece como feature. El patrón de add-ons por hora también tiene un efecto de arquitectura de costes: cada feature activa multiplica la tarifa base, así que el precio "de entrada" que se comunica al cliente ($0.15/hr) nunca es el precio real de un pipeline con diarización + medical + keyterms. Medical Mode a $0.15/hr, con el mismo peso que el propio modelo Universal-2, es un aviso de que los add-ons pueden llegar a costar tanto como el modelo — y de que la decisión de qué feature se empaqueta y cuál se factura por separado es en sí misma una decisión de pricing del clon, no solo de consumo.

## 2026-11-03 — re-verificación
La captura del 2026-11-03 (`sources/2026-11-03-assemblyai-pricing.md`) vuelve a renderizar **completa** la tabla de add-ons de pre-recorded y reproduce **exactamente** los cuatro importes de este átomo: **Keyterms Prompting $0,05/hr en Universal-3.5 Pro / "Included" en Universal-2** (con el límite textual "Provide up to 1000 words or phrases (maximum 6 words per phrase)"), **Prompting $0,05/hr / "Not supported"**, **Speaker Diarization $0,02/hr en ambos** y **Medical Mode $0,15/hr en ambos** ("New", "Optimize transcription for medical terminology and healthcare conversations with significantly improved accuracy"). Ninguna discrepancia: la tabla de add-ons de pre-recorded lleva cuatro capturas sin mover un centavo, lo que refuerza que el precio de las features —a diferencia de la fila "Custom", que sí cambia de forma de monetizar— es un valor estable ([[2026-1103-assemblyai-columna-custom-tercer-escalon-de-precios]]).
