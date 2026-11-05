---
id: 2026-1027-veridrop-thinking-signature-500-a-2000-caracteres-con-peso-25
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1027-veridrop-openai-deteccion-nivel-comportamiento-protocolo-sin-prueba-criptografica]]", "[[2026-1024-veridrop-home-12292-relays-y-cuatro-modelos-con-doble-nivel-de-evidencia]]", "[[2026-1027-veridrop-pesos-de-los-11-detectores-y-el-contexto-largo-de-pago]]"]
---

## Claim
El `thinking signature` es, según la FAQ, **"Claude 启用扩展思考时，响应里 signature 字段返回的服务端加密产物，长度 500-2000 字符"**, generado por el servidor de Anthropic y con **verificación criptográfica**, de modo que **"中转站理论上无法伪造"**. VeriDrop lo usa como **detector principal con peso del 25 %**. La FAQ añade dos consecuencias operativas: (a) los sustitutos **Kiro y Amazon Q** responden por la interfaz simplificada de **AWS Bedrock**, que **no devuelve firma de servidor**, así que VeriDrop **pone 0 en ese detector y hace fallar la detección entera**; (b) el sitio afirma que **"业内目前只有 Veridrop 利用了这个信号"**, es decir, elIndicador criptográfico no es un estándar de mercado sino una captura técnica de esta herramienta.

## Why It Matters
El vault tiene un modelo del sector lleno de "cifrado" publicitario —relays que llaman "1:1 透传" a lo que es una reescritura— y **este es el único caso documentado del corpus donde una afirmación criptográfica es comprobable y no automática**. La asimetría es fuerte: contra una firma de servidor, el intermediario tendría que **dejar de servir** para que la prueba pasara; contra un campo de texto (`model`, `object`, `finish_reason`), puede mentir sin coste.
Y el dato operativo es la contraparte exacta de la documentación del gateway: el vault ya sabe que la conversión entre protocolos **deforma y pierde campos** porque la hace un módulo aparte ([[2026-1023-new-api-relaykit-conversion-perdida-de-campos]]). Una firma criptográfica es, en esa arquitectura, **el campo que la capa de conversión no puede fabricar** — y es también lo que distingue una verificación concluyente ([[2026-1027-veridrop-openai-deteccion-nivel-comportamiento-protocolo-sin-prueba-criptografica]]) de una indicativa ([[2026-1027-veridrop-el-usage-de-la-respuesta-delata-el-trasvase-de-protocolo]]) — de ahí que un relay con conversión de protocolo (Claude↔Bedrock↔OpenAI) sea detectable de forma concluyente por el mismo mecanismo que la delata como relay.

## Nota de verificación
Cifras y pesos son literales de la FAQ. La captura **no** publica la lista de relays que han fallado el test de firma, ni el porcentaje de relays que la pasan, ni con qué modelo se ejecuta la prueba.
