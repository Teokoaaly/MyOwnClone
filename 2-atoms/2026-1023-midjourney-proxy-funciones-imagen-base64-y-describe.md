---
id: 2026-1023-midjourney-proxy-funciones-imagen-base64-y-describe
type: atom
certainty: solid
sources: [sources/2026-10-22-midjourney-proxy-github.md]
links: ["[[2026-1023-midjourney-proxy-convierte-discord-en-api-rest]]", "[[2026-1023-midjourney-proxy-edicion-plus-ampliada]]", "[[2026-1022-gap-dify-como-capa-inferencia-prompts]]"]
---

## Claim
La sección **"主要功能"** (funciones principales) de la edición de código abierto enumera exactamente siete capacidades: **"支持 Imagine 指令和相关动作"** (soporta la instrucción Imagine y sus acciones relacionadas), **"Imagine 时支持添加图片base64，作为垫图"** (durante Imagine admite añadir una imagen en base64 como imagen de referencia), **"支持 Blend(图片混合)、Describe(图生文) 指令"** (soporta Blend —mezcla de imágenes— y Describe —imagen a texto—), **"支持任务实时进度"** (soporta el progreso de la tarea en tiempo real), **"支持中文prompt翻译，需配置百度翻译或gpt"** (traduce prompts de chino al inglés, configurable con Baidu Translate o GPT), **"prompt 敏感词预检测，支持覆盖调整"** (predetección de palabras sensibles en el prompt, con posibilidad de sobrescribir el ajuste) y **"user-token 连接 wss，可以获取错误信息和完整功能"**.

## Why It Matters
La lista revela qué significa "API" para un generador de imágenes: no solo enviar un prompt y recibir un PNG, sino **reproducir el vocabulario de botones del bot de Discord** (Imagine, Blend, Describe, imagen de referencia, progreso en vivo). Y añade dos capas que no son de imagen sino de **producto multilingüe y de cumplimiento**: traducción de prompt (con dependencia externa configurable) y filtrado previo de palabras sensibles con override manual.
Para el vault, esto es una señal de arquitectura: el proxy **no traduce ni filtra por sí mismo** en su forma base — delega la traducción a Baidu o GPT según `mj.translate-way` ([[2026-1023-midjourney-proxy-config-tareas-y-autenticacion]]). Es exactamente el patrón de "capa de inferencia externa" que el vault ya usa con Dify ([[2026-1022-gap-dify-como-capa-inferencia-prompts]]): el núcleo del proxy no es el modelo, es el **orquestador de capacidades ajenas**.
Este patrón tiene dos piezas: el puente hacia el proveedor ([[2026-1023-midjourney-proxy-arquitectura-token-discord-y-wss]]) y la envoltura de producto (traducción, filtrado, cuentas, progreso) que es lo que se vende ([[2026-1023-midjourney-proxy-convierte-discord-en-api-rest]]).
El detalle de "tareas en tiempo real" importa para cualquier producto que necesite mostrar progreso asíncrono sin polling a ciegas. Y el reparto de funciones entre esta edición y la ampliada es explícito: todo lo que va más allá de Imagine/Blend/Describe (Pan, Zoom, Vary, Remix, seed) queda fuera ([[2026-1023-midjourney-proxy-edicion-plus-ampliada]]).

## Nota de verificación
El README no documenta la firma HTTP de ninguna de estas operaciones (viven en `docs/api.md`, no capturado) ni el número de pasos de los flujos de Blend o Describe.
