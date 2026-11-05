---
id: 2026-1026-anticaptcha-custom-tasks-y-object-coordinates
type: atom
certainty: solid
sources: [sources/2026-10-25-anti-captcha-pricing.md]
links: ["[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1024-2captcha-flujo-api-en-cinco-pasos-con-captcha-id]]", "[[2026-1026-anticaptcha-trece-tipos-con-precio-por-1000]]"]
---

## Claim
Dos filas del catálogo de AntiCaptcha no son "resolución de un captcha conocido" sino **capacidad genérica**: **Custom Tasks** (`AntiGateTask`) a **$2 por 1000** y **Object Coordinates** (`ImageToCoordinatesTask`) a **$2 por 1000**, ambas a 5 s. Object Coordinates devuelve **coordenadas de un objeto en la imagen**, no un texto.

## Why It Matters
Es la diferencia entre "resolver un captcha" y "**resolver una tarea visual arbitraria**", y tiene consecuencia de producto: Object Coordinates es exactamente la primitive que necesita un pipeline de **scraping de catálogo o de scraping visual con LLM** — no hay que identificar el texto, hay que devolver *dónde* está el objeto para poder hacer clic. A $2 por 1000 es un dato de coste comparable al de un reCAPTCHA v2, es decir **el scraping visual de coordenadas cuesta lo mismo que resolver un captcha**, lo que vuelve el dato muy barato frente al trabajo de visión que evita.
Y Custom Tasks (`AntiGateTask`) es la pieza que **descomoditiza la tarea**: un proveedor de captchas que acepta "custom tasks" a precio de catálogo es, de hecho, un **proveedor de trabajo humano de visión bajo demanda**. Es la operación que el vault ya identificó en 2Captcha ([[2026-1024-2captcha-servicio-dual-cliente-paga-y-trabajador-cobra]]) pero llevándola al formato de API sin captura de la cara de trabajador.
Para el modelo del vault esto abre una línea que no existía: **tareas visuales genéricas por $0.002 la unidad**, que es el mismo orden de magnitud que la corrección/anotación de datos de bajo nivel y muy por debajo del coste de un modelo de visión ([[2026-1024-2captcha-flujo-api-en-cinco-pasos-con-captcha-id]] muestra que el patrón de entrega es el mismo job-id + polling, con lo que un lote de coordenadas se integra como cualquier otro trabajo encolado).
Nota: la captura **no** publica qué tareas caben en `AntiGateTask` (¿imágenes arbitrarias? ¿instrucciones en texto?), ni el formato de la respuesta de Object Coordinates, ni si el precio es el mismo por subtipo.
