---
title: Synthetic Data Testing
created: 2026-05-25
updated: 2026-05-25
type: concept
tags: [testing, llm, ai, data]
sources: [raw/articles/myownclone-founder-transcript.md]
confidence: medium
---

# Synthetic Data Testing

Metodología usada por [[eugenio-oller]] para probar y refinar [[myownclone]] antes del lanzamiento.

## Enfoque

Crear "simulaciones de cientos de clientes para que hablen con el clon en todos los contextos y sacar data" ^[raw/articles/myownclone-founder-transcript.md]

## Proceso

1. Crear cuentas de clon de prueba
2. Generar datos sintéticos que replican posibles clientes reales
3. Simular conversaciones en múltiples contextos
4. Analizar respuestas, detectar fallos
5. Iterar: "afinar, afinar, afinar hasta que ahora ha quedado muy fino"

## Resultado

Permitió pulir el comportamiento del clon sin exponerlo a usuarios reales, detectando edge cases y mejorando guardrails antes del lanzamiento beta.

## Relevancia

Técnica aplicable a cualquier sistema conversacional con IA: testear con usuarios sintéticos antes de exponer a reales reduce riesgos de mala experiencia y acelera iteración.

## Ver también

- [[myownclone]]
- [[ai-clones]]
