---
id: 2026-1026-veridrop-firma-usage-field
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-openai-detection.md]
links: ["[[2026-1026-veridrop-ocho-checks-protocol-chatcompletions]]", "[[2026-1026-veridrop-profundidades-deteccion]]"]
---

## Claim
Veridrop identifica posibles sustituciones de backend analizando el campo `usage` en las respuestas Chat Completions: si aparecen campos extraños o ajenos a la forma oficial de OpenAI (por ejemplo, campos de Anthropic), se marca como "problema grave", ya que indica que el relay podría estar transfiriendo la petición a otro modelo y retornando campos que se le escaparon.

## Why It Matters
El fármaco de fingerprinting de uso es el mecanismo que permite distinguir un relay "honesto" que simplemente traduce el protocolo de OpenAI, de uno que en realidad está ejecutando otro modelo detrás. Sin esta verificación, un relay podría anunciarse como OpenAI mientras ejecuta Claude o Gemini internamente, y la detección solo miraría la forma externa, no la sustancia del backend.

## [FRICTION]
> [[2026-1027-veridrop-openai-deteccion-nivel-comportamiento-protocolo-sin-prueba-criptografica]] (escrita hace ~5 semanas) menciona que los campos de Anthropic "a veces salen" en respuestas envueltas. Este átomo (2026-1026) coincide en el síntoma pero llega a una conclusión operativa diferente: la presencia de campos ajenos no es un error de forma, es una señal de que el relay está haciendo túnel a otro proveedor. La regla de veto del vault ("cualquier detector reporta problema grave, el veredicto se pone amarillo aunque el score alcance 70") valida esta interpretación operativa.
> Ambas notas describen el mismo síntoma (campos extraños en la respuesta), pero la implicación práctica es opuesta: una dice "carece de valor sin firma criptográfica", la otra dice "es una señal de alarma operativa que activa el círculo amarillo". Dado que la regla de veto del vault ya trata este caso como decisión humana, ambas pueden coexistir sin contradicción auto-resuelta.