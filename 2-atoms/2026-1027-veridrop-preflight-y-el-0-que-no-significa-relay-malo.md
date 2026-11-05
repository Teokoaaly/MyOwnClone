---
id: 2026-1027-veridrop-preflight-y-el-0-que-no-significa-relay-malo
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1027-veridrop-cero-modelos-gpt-suele-ser-permiso-de-key-y-no-relay-caido]]", "[[2026-1027-veridrop-gemini-3-thinking-por-defecto-y-el-suelo-de-max-tokens]]", "[[2026-1027-veridrop-tres-formas-de-dilucion-o-concubamiento]]"]
---

## Claim
La FAQ define el **preflight** como una comprobación previa a la detección y explica qué evita: **"Veridrop 在你提交检测前会先帮你试一下,免得你白等半分钟拿到一份全 0 分的报告"**, y para Gemini **"会做 preflight,500ms 内识别死模型并给出可用列表替代"**; si el relay **no soporta el modelo elegido**, el preflight lo rechaza antes con **422**. Y da las **tres causas de un 0** que hay que distinguir leyendo los `details` de cada detector en lugar del total: **① key inválida o cuota agotada** (con un **banner de detección inválida**), **② el relay no soporta el modelo seleccionado** (preflight, 422), **③ el relay es realmente malo** (*"真的是非常垃圾的中转站"*).

## Why It Matters
Es la **regla de desambiguación de un 0**, y evita un error de lectura caro: **un 0 no es un veredicto, es un síntoma con tres causas distintas**, y solo una de ellas habla del relay. Es la misma disciplina que el vault ha aplicado a las cifras de disponibilidad sin denominador ([[2026-1024-veridrop-ventana-de-actividad-y-frescura-de-deteccion]]) y a los veredictos con tercer estado ([[2026-1024-veridrop-tercer-estado-edge-y-su-dispersion]]): **la cifra más extrema es la que más a menudo es un artefacto de la medición**.
El detalle de diseño del preflight tiene además una lectura económica: **es un ahorro de tokens para el usuario**, porque la detección real cuesta entre $0.012 y $0.20 por detección estándar y hasta $27.06 en la sonda máxima. Es decir, **el preflight es la barrera de entrada que hace viable el resto**, y es la razón por la que el sector puede ofrecer detección gratuita sin que el usuario pague una detección que no iba a concluir nada ([[2026-1027-veridrop-el-coste-de-la-sonda-larga-paga-el-usuario]]).
Y el principio general que el vault puede reutilizar tal cual: **un detector debe tener un banner de "resultado inválido" distinto de un veredicto de cero**. Confundir "no pude medir" con "medí y es malo" es la forma más común de tomar una decisión de compra incorrecta en este mercado, y el umbral de 0 de Gemini 3 con `max` insuficiente —**respuesta vacía con `finish_reason=length`**— es exactamente el tipo de artefacto que un detector sin banner convertiría en una acusación de fraude.

## Nota de verificación
Literal de la FAQ, incluidos el 422, el 500ms y las tres causas de 0. La captura **no** publica el texto exacto del banner de detección inválida ni el número de llamadas que consume el preflight.
