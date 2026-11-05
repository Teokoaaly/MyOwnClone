---
id: 2026-1031-deepgram-prerecorded-mas-barrio-pero-sin-cifra-publicada
type: atom
certainty: solid
sources: [sources/2026-10-31-deepgram-pricing.md, sources/2026-11-01-deepgram-pricing.md, sources/2026-11-03-deepgram-pricing.md]
links: ["[[2026-1031-deepgram-precios-por-minuto-por-modelo]]", "[[2026-1101-assemblyai-vs-deepgram-coste-por-hora-de-streaming]]", "[[2026-1031-deepgram-addons-por-minuto-sobre-transcripcion]]"]
---

## Claim
Deepgram ofrece dos modalidades de Speech-to-Text con un conmutador "Streaming | Pre-recorded" en la misma tabla, pero **no publica ninguna tarifa distinta para pre-recorded**: la tabla renderizada muestra una única columna de precios ($0,0077 / $0,0078 / $0,0092 por minuto pay-as-you-go) y la FAQ solo afirma de forma cualitativa "**Pre-recorded runs lower**". Es decir, la diferencia batch vs streaming de Deepgram es una afirmación sin cifra.

## Why It Matters
Es la laguna que dejó abierto [[2026-1101-assemblyai-vs-deepgram-coste-por-hora-de-streaming]] (marcado `tentative` por eso): frente a AssemblyAI, que publica $/hr cerrados y separados para pre-recorded (Universal-2 $0,15/hr, Universal-3.5 Pro $0,21/hr), Deepgram **no permite cotizar el caso batch con su lista de precios**. Para MyOwnClone eso significa que el dimensionamiento de la transcripción asíncrona (grabaciones de reuniones, que es el caso de uso natural de pre-recorded) no se puede cerrar con datos de lista: habría que pedir el precio a ventas o medir con una cuenta de prueba. Regla operativa del vault: no crear una línea de coste con cifras de Deepgram en pre-recorded mientras la fuente no las publique.

## [FRICTION]
> [[2026-1101-assemblyai-vs-deepgram-coste-por-hora-de-streaming]] razona "Deepgram declara $0,0077/min en streaming pay-as-you-go (≈$0,46/hr) y afirma que 'Pre-recorded runs lower' sin publicar la cifra exacta" y marca el átomo como `tentative` por eso.
> Este átomo confirma la laguna en las tres capturas (2026-10-31, 2026-11-01, 2026-11-02) y añade que el conmutador Streaming | Pre-recorded **sí está presente en la página** con dos pestañas, lo que sugiere que existen tarifas distintas detrás de la pestaña no capturada, no que el precio sea el mismo. La afirmación de "más barato" sigue sin cifra verificable. Marcado para juicio humano, no auto-resuelto.

## 2026-11-03 — re-verificación
Cuarta captura de la misma URL: el conmutador "Streaming | Pre-recorded" sigue presente en la tabla de Speech-to-Text y en la de add-ons, la FAQ sigue diciendo solo "Pre-recorded runs lower" y **sigue sin publicarse ninguna cifra de pre-recorded**. El hueco se mantiene abierto por cuarta vez, lo que refuerza la regla operativa de este átomo: no crear una línea de coste con cifras de Deepgram en pre-recorded mientras la fuente no las publique. La comprobación transversal de estabilidad está en [[2026-1103-deepgram-precios-estables-en-cuatro-capturas-consecutivas]].
