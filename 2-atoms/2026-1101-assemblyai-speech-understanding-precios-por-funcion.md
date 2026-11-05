---
id: 2026-1101-assemblyai-speech-understanding-precios-por-funcion
type: atom
certainty: solid
sources: [sources/2026-11-01-assemblyai-pricing.md]
links: ["[[2026-1022-separacion-de-hablantes-en-entrevistas]]", "[[2026-1022-costes-por-categoria-tenant]]", "[[2026-1101-assemblyai-tarifas-por-hora-no-por-minuto]]"]
---

## Claim
El bloque Speech Understanding de AssemblyAI se factura **por función y por hora**, con dos funciones que tienen dos niveles de esfuerzo: **Speaker Identification $0,02/hr** (low effort, por defecto) o **$0,10/hr** (medium effort, "for harder recordings"), y **Summarization $0,02/hr** (low effort, por defecto) o **$0,07/hr** (medium effort, "for long, multilingual, or detail-critical audio"); el resto a precio fijo: **Translation $0,06/hr**, **Custom Formatting $0,03/hr**, **Entity Detection $0,08/hr**, **Sentiment Analysis $0,02/hr**, **Key Phrases $0,01/hr** y **Topic Detection $0,15/hr**. Speaker Identification "Identify speakers by their actual names or roles", y la FAQ añade que con ella se sustituyen las etiquetas genéricas "Speaker A" y "Speaker B" por nombres o roles reales.

## Why It Matters
Es la pieza que conecta el coste de audio con el valor del producto: el vault ya sabe que separar hablantes es lo que hace viable el entrenamiento con entrevistas ([[2026-1022-separacion-de-hablantes-en-entrevistas]]), y aquí el precio de esa función es de céntimos — $0,02/hr en el modo easy, $0,10/hr en medium. Sobre una hora de transcripción pre-recorded de Universal-2 ($0,15/hr), la identificación de hablantes por nombre cuesta entre **+13 % y +67 %** del total de la hora según el nivel de esfuerzo: es el add-on más barato en términos absolutos y el que más multiplica el precio cuando se sube a medium. El punto estructural para el vault es que cada función de comprensión **se factura por separado y se suma a la hora base**, así que un pipeline de "transcribir + resumir + detectar entidades + Topics" sobre 100 horas/mes con Universal-2 pasa de $15 a **$30** ($15 base + $15 de Topic Detection solo) — el mismo patrón de features-a-la-venta que ya documenta el corte por categoría del vault ([[2026-1022-costes-por-categoria-tenant]]).
