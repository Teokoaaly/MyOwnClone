---
id: 2026-1027-veridrop-gpt-6-astra-exige-chat-completions-y-responses-api
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-openai-detection.md]
links: ["[[2026-1027-veridrop-la-sonda-de-contexto-largo-y-la-maxima-por-modelo]]", "[[2026-1026-new-api-cache-12h-openai-2-5x-y-precios-gpt-6-astra]]", "[[2026-1023-new-api-gateway-unificado-de-modelos]]"]
---

## Claim
La página OpenAI de VeriDrop anuncia **"GPT-6 Astra 检测已上线"** con cobertura de **"接口响应、工具调用、结构化输出、流式一致性与 Token 用量"** y **"23"** informes de Astra ese día. El detalle de arquitectura que importa: **"GPT-6 Astra 的函数调用通过 Responses API 检查;中转站需同时支持 Chat Completions 和 Responses"**. Y la lista de **modelos detectables** es de nueve: `gpt-5.6-sol`, `gpt-6-astra`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5.5`, `gpt-5.4`, `gpt-5.3-codex`, `gpt-5.4-nano` y `gpt-5.4-mini`.

## Why It Matters
Es la **evidencia dura de la fricción ya anotada por el scout**: el thread del agregador de precios habla de GPT-6 Astra como modelo, pero **ninguna fuente del thread enumeraba nombres de modelo concretos**, y aquí hay nueve identificadores verbatim de un detector activo —incluida la **nomenclatura de la serie 5.6 con tres variantes (`sol`, `terra`, `luna`)**, que es un esquema de nombres que el vault no tenía registrado en ninguna parte. Para un producto que indexa precios por modelo, la **tabla de nombres de modelo tiene que salir de una fuente que los use de verdad**, y esta es una de las pocas.
El otro contenido del átomo es un **requisito de capacidad de dos superficies**: un relay que anuncie Astra tiene que exponer **Chat Completions y Responses**, y no solo una. Eso es exactamente la clase de requisito que separa "el relay vende el modelo" de "el relay es usable con las herramientas que ese modelo trae" (function calling vía Responses, structured output, streaming coherente). La comprobación de que un camino existe ([[2026-1023-new-api-gateway-unificado-de-modelos]]) no basta: hay que comprobar que **las dos superficies de API que el cliente real usa están vivas**.
Y el "23 informes de Astra hoy" es un dato de **volumen de uso del detector**: sugiere que la detección de la serie GPT-6 es lo que la gente está midiendo ahora mismo, lo que convierte a VeriDrop en el **barómetro de facto del estado de la compatibilidad Astra en el sector de relays**. Y el precio de esa medición no es gratuito: las sondas de contexto largo de Astra están cuantificadas en [[2026-1027-veridrop-la-sonda-de-contexto-largo-y-la-maxima-por-modelo]] y en [[2026-1027-veridrop-el-coste-de-la-sonda-larga-paga-el-usuario]].

## Nota de verificación
Nombres de modelo, el contador 23 y el requisito de doble superficie son literales de la captura. La captura **no** publica el criterio de elegibilidad de la lista de nueve modelos ni si los nombres coinciden con los identificadores del API oficial.
