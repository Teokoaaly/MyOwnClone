---
id: 2026-1031-deepgram-audio-intelligence-por-token-encima-de-transcripcion
type: atom
certainty: solid
sources: [sources/2026-10-31-deepgram-pricing.md, sources/2026-11-03-deepgram-pricing.md]
links: ["[[2026-1031-deepgram-precios-por-minuto-por-modelo]]", "[[2026-1101-assemblyai-speech-understanding-precios-por-funcion]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---

## Claim
El producto **Audio Intelligence** de Deepgram se cobra **por token, por encima de la transcripción**: "Billed per 1,000 input and output tokens in addition to transcription", con **Summarization, Topic Detection, Sentiment Analysis e Intent Recognition** todos al mismo precio — pay-as-you-go **$0,0003/1k tokens in** y **$0,0006/1k out**, Growth **$0,00024/1k in** y **$0,00048/1k out**. La FAQ añade que "They run on purpose-built small language models rather than a general-purpose LLM, which is why the per-unit cost is low."

## Why It Matters
Es el patrón de "feature de IA como coste marginal token a token" que el vault ya tiene en la categoría `categoryCloneResponses` de [[2026-1022-costes-por-categoria-tenant]], y su gran ventaja para el clon es que **la línea no escala con el audio**: el coste de resumir o detectar intenciones depende del texto, no de los minutos. Sobre el monolingual de lista, un minuto de transcripción cuesta $0,0077 mientras que transcribir + resumir + analizar sentimiento sale a $0,0077 + tokens: la parte inteligente es marginal frente al reconocimiento. El orden de magnitud también es revelador: $0,0003/1k tokens in es un precio de SLM purpose-built, muy por debajo de lo que costaría llamar a un LLM general, lo que da una pista de el margen con el que se puede vender "insights" dentro de un clon sin reventar el coste por minuto.

## [FRICTION]
> El bloque de la tabla aparece en las tres capturas, pero el **rótulo cambia** sin que cambie el precio: el 2026-10-31 y el 2026-11-01/02 alternan entre el pie "Billed per 1,000 input and output tokens in addition to transcription" y el pie corto "Billed per token on top of transcription". No es una contradicción de cifras, pero la página no es estable en su redacción entre capturas y eso obliga a citar siempre la fuente y la fecha junto a la cifra.
> Marcado para juicio humano, no auto-resuelto.

## 2026-11-03 — re-verificación
Cuarta captura: los cuatro precios de Audio Intelligence (Summarization, Topic Detection, Sentiment Analysis e Intent Recognition) son idénticos — pay-as-you-go $0,0003/1k in y $0,0006/1k out, Growth $0,00024/1k in y $0,00048/1k out. La alternancia de redacción que este átomo ya había detectado se confirma y se amplía: en esta captura la celda aparece **fusionada** ("$0.0003/ 1k in$0.0006/ 1k out"), igual que en las capturas del 11-01 y 11-02, mientras que la del 10-31 las traía en columnas separadas; y el pie de sección vuelve a aparecer en su forma corta ("Billed per token on top of transcription") mientras la FAQ mantiene la larga ("Billed per 1,000 input and output tokens in addition to transcription"). Ver [[2026-1103-deepgram-precios-estables-en-cuatro-capturas-consecutivas]].
