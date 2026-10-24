---
id: 2026-1024-veridrop-cobertura-de-protocolos-por-relay
type: atom
certainty: solid
sources: [sources/2026-10-23-veridrop-relays.md]
links: ["[[2026-1023-new-api-una-sola-api-multiproto]]", "[[2026-1023-new-api-gateway-unificado-de-modelos]]", "[[2026-1024-veridrop-directorio-de-relays-distinto-del-ranking]]"]
---

## Claim
Cada entrada del directorio de VeriDrop lleva etiquetas de **protocolo/modelo soportado** y la cobertura sobre las 50 entradas es desigual. Contando las etiquetas de cada fila: **OpenAI aparece en 42 de 50**, **Claude en 39 de 50** y **Gemini solo en 18 de 50**. Por número de protocolos declarados: **15 relays declaran los tres** (Claude + Gemini + OpenAI), **19 declaran dos** y **16 declaran uno solo** — de esos 16 monoprotocolo, 10 son solo-OpenAI, 5 solo-Claude y 1 solo-Gemini (`codex.zone.id`). El directorio ofrece además filtros por protocolo en `/relays/claude`, `/relays/openai` y `/relays/gemini`, y el bloque de navegación los titula "全部协议".

## Why It Matters
Es el atlas de cobertura de protocolo del mercado de relays, y el dato que más directamente importa a MyOwnClone: si el producto habla OpenAI-compatible por `OPENAI_API_BASE`, la superficie de proveedores utilizables es de **42 entradas**, no de 50; y si en algún momento quiere **Claude nativo o Gemini**, el conjunto cae a 39 y a 18. Solo 15 relays son multi-protocolo completos, lo que confirma que **la compatibilidad multi-protocolo es la excepción y no la norma** en los relays de consumo — pese a que el software que los implementa se diseñó precisamente para eso (normalización a formato OpenAI/Claude/Gemini en [[2026-1023-new-api-gateway-unificado-de-modelos]] y [[2026-1023-new-api-una-sola-api-multiproto]]). Es decir: la capacidad técnica del stack no se está materializando en los despliegues comerciales.
El sesgo es además hacia OpenAI: el directorio de un sitio de monitorización de relays de API texto cubre OpenAI en el 84 % de las filas y Gemini en el 36 %. Cualquier lectura de "el mercado de relays" basada en este directorio está sesgada hacia el ecosistema OpenAI-compatible.

## Nota de verificación
Recuento literal de las etiquetas de protocolo de las 50 filas de la captura. La captura **no** publica: qué modelos concretos hay detrás de cada etiqueta, ni si las etiquetas son autodeclaradas por el relay o detectadas por el propio VeriDrop.
