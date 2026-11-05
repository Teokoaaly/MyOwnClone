---
id: 2026-1027-veridrop-cctest-y-hvoy-como-competidores-con-alcances-distintos
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1027-veridrop-openai-deteccion-nivel-comportamiento-protocolo-sin-prueba-criptografica]]", "[[2026-1027-veridrop-informe-publico-anonimo-y-la-key-cifrada-en-la-cola]]", "[[2026-1024-veridrop-directorio-de-relays-distinto-del-ranking]]"]
---

## Claim
La FAQ compara el sector de herramientas de detección en tres bloques. **CCTest** *"以 Claude 检测为主,现在也可以选 ChatGPT"* y ofrece **solo dos comprobaciones**: **"模型是否被替换"** y **"Token 用量是否异常"**; además **"也声称不上传 key,但代码闭源无法验证"**. **hvoy.ai** *"也支持三协议,但检测维度浅(主要是协议合规)"*. VeriDrop se diferencia en **Claude con verificación criptográfica**, en la **detección de huellas de conversión de protocolo en OpenAI** (`usage_source` etc.) y en **adaptarse a los modelos Gemini con thinking por defecto**, además de ser **completamente open source**. La FAQ también clasifica el ecosistema en **tres categorías** de sitios: **① ranking y recomendación** (aiapipk.com, 禾维 AI) para encontrar candidatos; **② directorio y monitorización** (LMSpeed, TokenAPI Scan, AI中转站监视者, OkkMax) para ver precios, latencia y ranking; **③ detección** (VeriDrop, CCTest, Ofox, 真测) para verificar la autenticidad. Y prescribe el flujo: **primero buscar candidatos en el ranking, después verificarlos con un detector**.

## Why It Matters
Es el **mapa del sector de verificación**, y el vault solo tenía una de sus tres capas. La observación con más valor para el producto es que **el sector se ha estratificado por función, no por calidad**: los sitios de ranking, los de directorio y los de detección **no compiten entre sí**, y el flujo correcto es **encadenarlos**. Es la misma arquitectura de dos inventarios que el vault ya vio en el hilo del agregador, pero aquí con un tercer eslabón ([[2026-1024-veridrop-directorio-de-relays-distinto-del-ranking]]).
El dato de **CCTest es la pieza más dura**: **dos comprobaciones y código cerrado**. Dos comprobaciones —modelo sustituido y anomalía de tokens— cubren **dos de las tres formas de dilución** ([[2026-1027-veridrop-tres-formas-de-dilucion-o-concubamiento]]), pero no la capacidad. Y **la objeción a CCTest no es funcional sino de auditoría**: "también afirma que no sube la key, pero el código es cerrado y no se puede verificar". Es exactamente el argumento que el vault ha aplicado a los agregadores del sector, y su corolario es brutal para el diseño del producto: **en un mercado donde el objeto es una credencial, la apertura del código es la única prueba de la promesa de privacidad** ([[2026-1027-veridrop-informe-publico-anonimo-y-la-key-cifrada-en-la-cola]]).
Y hay un dato de competencia que el vault debe registrar: **existen al menos seis herramientas de detección*y dos directorios* de relays**. Para el producto, eso significa que **construir la propia función de verificación es más difícil de lo que parecía** — no se trata de hacer una comprobación más, sino de competir en un espacio ya poblado. La alternativa racional no es construir otro detector, sino **usar el detector y construir la capa de precio encima**, que es exactamente la posición que el hilo del agregador ya ha alcanzado.

## Nota de verificación
Las características de CCTest, hvoy.ai, la taxonomía de tres categorías de sitios y el flujo recomendado son literales de la FAQ. La captura **no** publica los precios de ninguna de las herramientas, ni las métricas de auditoría comparadas, ni la fecha de la referencia a Ofox y 真测.
