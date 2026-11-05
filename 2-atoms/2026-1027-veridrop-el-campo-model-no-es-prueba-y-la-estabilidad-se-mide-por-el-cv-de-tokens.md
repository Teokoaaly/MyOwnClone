---
id: 2026-1027-veridrop-el-campo-model-no-es-prueba-y-la-estabilidad-se-mide-por-el-cv-de-tokens
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1027-veridrop-una-desviacion-grave-baja-el-veredicto-a-amarillo]]", "[[2026-1024-veridrop-home-la-disponibilidad-se-mide-por-par-sitio-y-modelo]]", "[[2026-1023-priceai-transit-formula-del-multiplicador-compuesto]]"]
---

## Claim
El campo `model` de la respuesta **no es evidencia de nada**: *"model 字段只是字符串,中转站可以填任何值"*. VeriDrop lo sustituye por tres señales indirectas: **①** el detector de **conformidad de protocolo**, que escanea la huella de `usage`; **②** la **diferencia de comportamiento** (*"GPT 偏简洁,Claude 偏礼貌啰嗦"*); **③** el **coeficiente de variación del número de tokens** entre llamadas repetidas, que da nombre al detector **"model consistency"**. La FAQ da el umbral que usa como criterio de selección: **"多次请求 completion_tokens CV < 0.10(稳定性)"**.

## Why It Matters
El vault ha estado guardando el `model` devuelto como si fuera la identidad del modelo. Esta es la corrección formal de esa práctica: **una cadena que el intermediario escribe no puede ser la prueba**, y la prueba tiene que salir de la **variabilidad estadística de la carga**, no de una etiqueta.
La métrica es elegante y reutilizable: **el CV de `completion_tokens` en peticiones repetidas mide la consistencia del modelo que realmente ejecuta** (una tabla de lookup, un routing determinista, un modelo fijo dan CV bajo; un enrutador que alterna entre modelos o una degradación da CV alto) y al mismo tiempo **detecta el "掺水" de multiplicar tokens**, porque un relay que infla el contador de forma no determinista también eleva el CV. El vault ya sabe que el multiplicador de precio solo significa algo si el contador de tokens es real ([[2026-1023-priceai-transit-formula-del-multiplicador-compuesto]]); **el CV es la prueba barata de esa condición**, y el umbral 0,10 es una cifra que se puede copiar directamente al producto.
Y hay una lectura estructural: la granularidad de la evidencia es **por par (relay, modelo)**, igual que la disponibilidad de la home ([[2026-1024-veridrop-home-la-disponibilidad-se-mide-por-par-sitio-y-modelo]]). Un detector que compara，请求 idénticos solo puede producir un veredicto de (sitio, modelo, protocolo) — nunca de "el relay".

## Nota de verificación
Umbral y nombres de detector son literales de la FAQ. La captura **no** publica cuántas peticiones compone el cálculo del CV ni si el umbral 0,10 es el mismo para todos los modelos y protocolos.
