---
id: 2026-1026-veridrop-ocho-checks-protocol-chatcompletions
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-openai-detection.md]
links: ["[[2026-1026-veridrop-firma-usage-field]]", "[[2026-1026-veridrop-profundidades-deteccion]]"]
---

## Claim
Veridrop detecta middleboxes de OpenAI/GPT realizando 8 verificaciones del protocolo Chat Completions: presencia de `chatcmpl-`, `chat.completion`, choices, finish_reason, usage, y la estructura oficial de la respuesta.

## Why It Matters
Esta cobertura de 8 puntos es la base de todos los modos de detección de Veridrop (profundidad, estándar, completa). Sin verificar estos campos, no es posible discernir si un relay está cumpliendo el protocolo oficial de OpenAI o simplemente envolviendo respuestas de otro modelo. Es el nivel fundamental de garantía comportamental antes de pasar a fingerprinting de uso o exploración de contexto.

## [FRICTION]
> [[2026-1027-veridrop-openai-deteccion-nivel-comportamiento-protocolo-sin-prueba-criptografica]] (escrita hace ~5 semanas) afirma que OpenAI no puede dar una prueba matemática de autenticidad, solo evidencias conductuales. Este átomo (2026-1026) coincide en el diagnóstico conductual pero contradeice en la conclusión: la ausencia de firma criptográfica no equivale a que la detección sea inútil, pues las 8 verificaciones protocolares forman un conjunto suficiente para señalar relays sospechosos, incluso si no hay certeza absoluta.
> Ambas pueden ser correctas: la firma criptográfica sería prueba concluyente, pero su ausencia no invalida las 8 verificaciones de comportamiento. Marcado para juicio humano, no auto-resuelto.