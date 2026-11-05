---
id: 2026-1031-deepgram-modelos-legacy-nova2-enhanced-base-por-hora
type: atom
certainty: solid
sources: [sources/2026-10-31-deepgram-pricing.md, sources/2026-11-03-deepgram-pricing.md]
links: ["[[2026-1031-deepgram-precios-por-minuto-por-modelo]]", "[[2026-1031-deepgram-growth-4000-anuales-y-sobreconsumo-10]]", "[[2026-1022-myclone-voice-clone]]"]
---

## Claim
Deepgram mantiene en catálogo los modelos antiguos **solo para despliegues existentes**, a tarifas por hora que se declaran literalmente en la FAQ: "Nova-2 streaming **$0.35 an hour**, Enhanced **$0.99**, Base **$0.87**. Growth is about **12.5% lower**. New projects should start with Nova-3 for general transcription or Flux for real-time voice agents." Es decir, Enhanced ($0,99/hr) y Base ($0,87/hr) son **más caros** que Nova-3/Flux en streaming ($0,46/hr).

## Why It Matters
Fixado en $/hr, este es el punto donde el desglose de precio de Deepgram mezcla unidades: la tabla principal va en $/min y la FAQ de modelos legacy en $/hr, sobre la misma página. Para un vault que acaba de resolver la fricción de unidades min vs hora ([[2026-1101-assemblyai-tarifas-por-hora-no-por-minuto]]), esto es una señal de que hay que normalizar a $/hr antes de comparar proveedores: Nova-3 monolingual son $0,462/hr, Flux English $0,462/hr, Flux Multilingual $0,468/hr y Nova-3 Multilingual $0,552/hr. Y el mensaje comercial ("new projects should start with Nova-3") confirma que las cifras de legacy no sirven para cotizar MyOwnClone: un clon de voz nuevo ([[2026-1022-myclone-voice-clone]]) debe presupuestarse con Nova-3 o Flux, no con las tarifas heredadas.

## [FRICTION]
> La FAQ afirma "Growth is about **12.5% lower**" para estos modelos, pero el descuento medido sobre las tarifas nuevas de STT es de ~15,6 % (Nova-3 Monolingual, $0,0077 → $0,0065) y el titular de la web promete "up to 20%" (ver [[2026-1031-deepgram-growth-4000-anuales-y-sobreconsumo-10]]).
> No es una contradicción dura — el 12,5 % corresponde a la familia legacy y el 20 % es un techo comercial — pero son tres cifras distintas de "descuento Growth" en la misma página sin indicar a qué productos se aplica cada una. Marcado para juicio humano, no auto-resuelto.

## 2026-11-03 — re-verificación
Cuarta captura: la FAQ de modelos antiguos se repite sin variación — "Nova-2 streaming $0.35 an hour, Enhanced $0.99, Base $0.87. Growth is about 12.5% lower. New projects should start with Nova-3 for general transcription or Flux for real-time voice agents." La fricción con el "up to 20 %" del titular de Growth y con el ~15,6 % real de las tablas de STT sigue exactamente igual de abierta, tal y como se documenta en [[2026-1031-deepgram-growth-4000-anuales-y-sobreconsumo-10]].
