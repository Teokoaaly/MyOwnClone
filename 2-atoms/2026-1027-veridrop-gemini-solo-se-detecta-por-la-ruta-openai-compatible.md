---
id: 2026-1027-veridrop-gemini-solo-se-detecta-por-la-ruta-openai-compatible
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1027-veridrop-el-usage-de-la-respuesta-delata-el-trasvase-de-protocolo]]", "[[2026-1027-veridrop-gemini-3-thinking-por-defecto-y-el-suelo-de-max-tokens]]", "[[2026-1023-new-api-una-sola-api-multiproto]]"]
---

## Claim
VeriDrop **no soporta la ruta nativa de Gemini** (`/v1beta/models/X:generateContent`) y lo justifica por escrito: **"99% 的第三方 Gemini 中转站只暴露 OpenAI 兼容协议"**, y además **Google 官方也提供 el endpoint OpenAI-compatible `/v1beta/openai`**, de modo que **"维护两套独立的检测逻辑成本高且容易引入翻译层导致结果失真"**, así que **"Veridrop 集中在 OpenAI 兼容路径上做透"**. Y la misma lógica aplica a la detección: **"Veridrop 的 Gemini 检测只走 OpenAI 兼容路径(POST /chat/completions)"**.

## Why It Matters
Es la **decisión de arquitectura de un detector** con la misma tesis que el gateway del vault: **una capa de traducción no es gratis ni inocente** — introduce distorsión en el resultado. Y aquí tiene un corolario fuerte: **detectar Gemini por la ruta OpenAI-compatible es una prueba de la compatibilidad del relay con Gemini, no de Gemini**. Si el relay expone Gemini con una forma nativa distinta, el detector no lo ve; si lo expone envuelto, lo que se verifica es el envoltorio.
La consecuencia para el vault es de **dirección de la conversión**: su propio gateway convierte **hacia** los formatos del cliente (Claude, Gemini, OpenAI) desde un upstream heterogéneo ([[2026-1023-new-api-una-sola-api-multiproto]]), y por eso **no puede usar el mismo atajo** que VeriDrop ([[2026-1027-veridrop-el-usage-de-la-respuesta-delata-el-trasvase-de-protocolo]]) —no tiene acceso al camino crudo de Gemini. VeriDrop puede hacer el atajo porque **la ruta que usa es la que el 99 % de los relays ya expone**; el vault, para detectar a sus propios proveedores, tendría que **hablar la ruta nativa o leer el upstream antes de convertir**, que es exactamente lo que la capa de traducción le impide.
Y hay un dato de mercado que abre otra vía: **Google oficial sí expone endpoint OpenAI-compatible**, y la FAQ dice que ese endpoint **"应该全 7 项 100 分,可作为基线对比第三方中转站"**. Eso convierte al proveedor oficial en la **línea base de calibración** del detector, que es el patrón correcto para un producto: **el valor esperado de una detección bien hecha es el del proveedor oficial**.

## Nota de verificación
Literal de la FAQ. La captura **no** publica qué siete detectores son los de la ruta Gemini (dice "全 7 项" sin enumerar), ni si la línea base se ha verificado realmente.
