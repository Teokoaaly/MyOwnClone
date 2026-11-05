---
id: 2026-1027-veridrop-el-usage-de-la-respuesta-delata-el-trasvase-de-protocolo
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md, sources/2026-10-26-veridrop-openai-detection.md]
links: ["[[2026-1027-veridrop-openai-deteccion-nivel-comportamiento-protocolo-sin-prueba-criptografica]]", "[[2026-1027-veridrop-una-desviacion-grave-baja-el-veredicto-a-amarillo]]", "[[2026-1023-new-api-relaykit-conversion-perdida-de-campos]]"]
---

## Claim
La huella decisiva de un relay que **vende GPT pero entrega Claude** está en el **shape del campo `usage`**, y la FAQ da la regla exacta: *"原生 OpenAI 只有 prompt_tokens / completion_tokens / total_tokens 三个键。如果出现 claude_cache_creation_5m_tokens、usage_source: anthropic、或 input_tokens / output_tokens(Anthropic 命名),基本可以判定中转站在做协议转换"*. La página OpenAI lo repite en lenguaje llano: *"OpenAI 官方回包里只会出现三个 token 计数字段; 但如果中转站偷偷把你的请求转给了 Claude 后端… Anthropic 那边的字段经常会跟着漏出来"*. VeriDrop marca esa fuga como **problema grave** y, según la FAQ, **"直接拒绝该项 detector"**; la página OpenAI añade que **baja el veredicto global a amarillo**.

## Why It Matters
Es el **mecanismo de Porter de la sustitución**: la capa de traducción no puede ocultar los nombres de campo del proveedor de destino, y por eso el campo `usage` funciona como **huella de origen**. El vault ya documentó que la conversión entre protocolos de gateway **deforma y pierde campos** ([[2026-1023-new-api-relaykit-conversion-perdida-de-campos]]); aquí se ve el reverso útil de ese defecto: **el campo que se pierde es el que delata al intermediario**.
La consecuencia de diseño para el vault es fuerte y va contra la intuición de "cuanto más seamless la capa de traducción, mejor": **una traducción perfecta sería invisible y por tanto verificable solo por comportamiento**. Publicar `usage_source: anthropic` en una respuesta que dice ser GPT no es un descuido del relay, es la **huella de un intermediario que no puede limpiar su propia costura**. El residuo es exactamente la firma de la costura que el módulo de conversión del gateway deja ([[2026-1023-new-api-relaykit-conversion-perdida-de-campos]]), y por eso es la **contrapartida exacta** de la ausencia de prueba criptográfica en el protocolo OpenAI ([[2026-1027-veridrop-openai-deteccion-nivel-comportamiento-protocolo-sin-prueba-criptografica]]). Es un argumento a favor de un principio que el vault puede reaplicar a su propio producto: **el gateway de MyOwnClone no debe intentar "limpiar" campos del proveedor upstream**, porque son la única prueba verificable de que existe un camino real hacia el modelo.

## Nota de verificación
Campos y nombres son literales de las dos fuentes. La captura **no** publica si VeriDrop normaliza o elimina esos campos antes de mostrarlos en el informe, ni con qué tolerancia se acepta un `usage` con claves extra.
