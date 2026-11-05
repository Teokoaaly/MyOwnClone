---
id: 2026-1026-veridrop-probedor-contexto-ventana
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-openai-detection.md]
links: ["[[2026-1026-veridrop-profundidades-deteccion]]", "[[2026-1026-veridrop-firma-usage-field]]"]
---

## Claim
Veridrop verifica la autenticidad de la ventana de contexto del middlebox enviando sondas de 32k → 100k → 200k tokens. Si el relay censura o ruta el request a un modelo de ventana pequeña, la detección falla inmediatamente. Esto expone relays que anuncian contextos grandes pero entregan modelos truncados.

## Why It Matters
Los relays a menudo anuncian ventanas de contexto amplias (hasta 100k o 1M tokens) para competir, pero en la práctica pueden estar limitando el contexto efectivo. Esta prueba es la única forma práctica de verificar si el relay realmente honra su anuncio de contexto. Si falla, el usuario sabe que debe ajustar sus expectativas o cambiar de relay. Es especialmente crítica para flujos de trabajo que requieren largo contexto (documentos extensos, código grande, etc.).

## [FRICTION]
> [[2026-1027-veridrop-el-coste-de-la-sonda-larga-paga-el-usuario]] (escrita hace ~5 semanas) señala que la sonda de contexto largo se factura aparte y no entra en el total de la tabla de pesos, similar a la separación entre magnitudes heterogéneas que este átomo (2026-1026) también defiende: el costo de la prueba de contexto largo es una magnitud distinta a la de los pesos de detección, y no debería mezclarse en tablas comparativas de "precio por detección". Ambas coinciden en el principo de separación, pero difieren en el ámbito de aplicación: este átomo (2026-1026) lo enmarca en la verificación de contexto de ventana, mientras que la nota de 2026-1027 lo enmarca en la estructura de precios del vault. Dado que abordan dimensiones distintas (verificación de contexto vs. estructura de precios), no hay contradicción auto-resuelta.