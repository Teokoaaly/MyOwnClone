---
id: 2026-1027-veridrop-pesos-de-los-11-detectores-y-el-contexto-largo-de-pago
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1027-veridrop-thinking-signature-500-a-2000-caracteres-con-peso-25]]", "[[2026-1027-veridrop-los-pesos-de-la-deteccion-suman-110-y-no-100]]", "[[2026-1024-veridrop-metodo-de-la-puntuacion-mediana-publica]]"]
---

## Claim
La FAQ publica la **tabla de pesos de la detección de Claude**: **11 comprobaciones regulares más 1 detección de contexto largo activada por el usuario y de pago**. El reparto literal es: **thinking signature (25 %) > behavioral signature (15 %) > structured output (12 %) > consistency / knowledge / token usage (10 % cada uno) > pdf (8 %) > identity / protocol / integrity / message_id (5 % cada uno)**. Y publica los tiempos: **standard corre 9 comprobaciones regulares en ~45 s; full corre las 11 completas en ~75 s**, con la **resultado de contexto largo mostrado de forma independiente, sin ser sustituido por el score normal** ("长上下文结果独立显示,不由普通总分代替").

## Why It Matters
Es la **tabla de pesos de un producto de detección de intermediarios**, algo que el vault no tenía: hasta ahora solo sabía que VeriDrop publicaba una mediana agregada sin definiciones ([[2026-1024-veridrop-metodo-de-la-puntuacion-mediana-publica]]). Con esta tabla, un score deja de ser un número opaco y pasa a ser **un vector con pesos publicados** — se puede descomponer, comparar detectores entre protocolos y, sobre todo, **auditar por qué una fila baja**.
Y hay una decisión de diseño que es directamente transferible al producto del vault: **el contexto largo es un ítem aparte, de pago, y no se mezcla en el total**. Es la respuesta correcta al problema de que "un único número no puede mezclar cosas heterogéneas" que el thread del agregador lleva tres secciones ([[2026-1023-priceai-codificacion-por-requests-vs-prompts-vs-creditos]]): la comprobación cara se **segrega y se etiqueta**, en lugar de diluirse en un promedio ponderado.
El reparto en sí también dice algo: **la identidad pesa el 5 % y la firma el 25 %** — una proporción 5:1 entre "lo que el modelo dice de sí mismo" y "lo que el servidor firma".

## Nota de verificación
Pesos, tiempos y número de ítems son literales. La captura **no** publica la fórmula de agregación (cómo se combinan los pesos en el score) ni el umbral que considera "problema grave".
