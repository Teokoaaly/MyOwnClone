---
id: 2026-1104-assemblyai-self-hosted-y-voice-ai-cloud-solo-navegacion-sin-precios
type: atom
certainty: solid
sources: [sources/2026-11-04-assemblyai-pricing.md, sources/2026-11-02-assemblyai-pricing.md, sources/2026-11-01-assemblyai-pricing.md]
links: ["[[2026-1101-assemblyai-tarifas-por-hora-no-por-minuto]]", "[[2026-1103-assemblyai-columna-custom-tercer-escalon-de-precios]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]"]
---

## Claim
La página de precios de AssemblyAI ofrece **ocho secciones con tarifa** (Pre-recorded, Realtime, Sync, Dictation, Text-to-Speech, Speech Understanding, Guardrails, LLM Gateway) pero su navegación incluye un grupo "inference" con **Self Hosted** (`assemblyai.com/deployments/self-hosted`) y **Voice AI Cloud** (`assemblyai.com/deployments/cloud`) que **no tienen ninguna sección de precios, tabla ni cifra** en la página: no aparecen en el índice de pestañas del bloque de precios (transcribe / understand / interact) ni en el cuerpo. La página no ofrece ninguna cifra —ni por hora, ni por contrato, ni de licencia— para el despliegue autoalojado: **el precio de Self Hosted no está publicado** y solo es accesible vía "Contact sales" ([ver [[2026-1103-assemblyai-columna-custom-tercer-escalon-de-precios]]]).

## Why It Matters
Es un hueco de información con impacto directo en la decisión de arquitectura que el vault viene postergando: la alternativa "autoalojar los modelos de AssemblyAI" (que resolvería el problema de **residencia de datos en la UE** y el coste variable de inferencia) **no tiene precio público consultable**, igual que no lo tiene el tier Custom. Para el clon de voz, esto cierra por el lado negativo la vía de self-hosting como palanca de coste frente al despliegue en un VPS de ≤ €4/mes ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]): con las APIs en modo pay-as-you-go a $/hr, la única alternativa publicada de self-hosting sería la licencia enterprise negociada, cuyo precio es incuantificable desde la página. Nota de método: el grupo "inference" aparece en la navegación de **las tres capturas completas** (11-01, 11-02 y 11-04) pero no en la reducida del 11-03, de modo que su presencia y su falta de tarifa son ambas estables. Y a la vista del vault, la ausencia de precio de Self Hosted es una **ausencia de dato publicada, no un dato ausente**: la página no retira nada, simplemente no lo ofrece.
