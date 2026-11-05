---
id: 2026-1027-veridrop-detectar-agua
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1027-veridrop-tres-formas-de-dilucion-o-concubamiento]]", "[[2026-1027-veridrop-el-usage-de-la-respuesta-delata-el-trasvase-de-protocolo]]"]
---

## Claim

La detección de **掺水** (watering/dilution) se realiza en tres pasos verificables: (1) **验模型** — verificar la signature de thinking de Claude o las firmas de campo de uso en GPT para detectar modelos fuente inesperados; (2) **验token** —发送 requests controlados y comparar la entrada de tokens esperada vs. reportada, verificando consistencia entre modo stream y non-stream; (3) **验能力** —insertar 3 puntos de información en un contexto largo y verificar si pueden recuperarse, además de probar tool calling y output estructurado. El modo standard de Veridrop cubre los primeros dos pasos en ~45 segundos; el modo full añade el tercer paso.

## Why It Matters

Una prueba naive de una sola llamada no detecta watering, porque un relay diluido responde con normalidad ante preguntas simples. La detección requiere patrones de prueba específicas: variación de contexto, consistencia de tokens en múltiples llamadas y verificación de capacidades avanzadas (thinking, tool use, multimodal). Esto conecta directamente con el protocolo antifraude del vault, que ya sabía que las pruebas de compra pequeñas solo confirman que el canal entrega algo, no que mantiene fidelidad completa.

## Nota de verificación

Los tres pasos de detección son literales de la sección «掺水与降智» de la FAQ, específicamente el subtítulo «怎么检测中转站有没有掺水(纯度测试)?». La captura no publica umbrales numéricos que separen "token inflado" de "token real", ni las cifras de prevalencia de cada forma de dilución en el mundo real.