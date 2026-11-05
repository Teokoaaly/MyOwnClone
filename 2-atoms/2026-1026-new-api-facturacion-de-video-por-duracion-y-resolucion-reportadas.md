---
id: 2026-1026-new-api-facturacion-de-video-por-duracion-y-resolucion-reportadas
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-plugins-de-tareas-js-en-sandbox]]", "[[2026-1023-priceai-codificacion-por-requests-vs-prompts-vs-creditos]]", "[[2026-1026-new-api-reembolso-tareas-video-a-72-horas]]"]
---

## Claim
Varias versiones alinean la **facturación de vídeo con lo que el upstream realmente generó**, no con lo que pidió el cliente:

- **rc.43**: Doubao 1.3.0 y Alibaba Bailian 1.4.2 aceptan duración **"-1"** para Seedance 1.5 Pro, Seedance 2.x y Wan 3.0. La petición **reserva la duración máxima del modelo** (**12 s** para Seedance 1.5 Pro, **15 s** para 2.0, **30 s** para 2.5 y Wan 3.0) y **cobra la duración que reporta el upstream**.
- **rc.45**: **Vidu** se factura por el **modelo, la duración y la resolución que realmente generó**, no por lo pedido.
- **rc.47**: se corrige que **Kling** generaba con la duración de `metadata` pero **cobraba la duración exterior**; además el plugin de Grok Imagine 1.1.0 factura ediciones y extensiones de vídeo a la **resolución de salida**, leyendo la cabecera del fichero (480p si el lado corto es de 480 px o menos; 720p en caso contrario, y también cuando no se puede leer la cabecera).

## Why It Matters
Es el mismo patrón que el vault ya identificó en el motor de precios del gateway: **el plugin declara sus propios hechos de uso y el gateway los acota** ([[2026-1023-new-api-plugins-de-tareas-js-en-sandbox]]), y aquí se ve el extremo concreto: **la unidad de la factura es "segundos de vídeo realmente generados" y "píxeles de salida"**, que no son tokens ni requests ni prompts.
La lección de caja es la de la **reserva frente a la liquidación**: el gateway **reserva lo peor (la duración máxima del modelo)** y **cobra lo real**. Un operador que solo liquidara lo pedido podría estar regalando o cobrando de más según el caso; y la reserva afecta a la cuota disponible, no solo al importe final — por eso el plazo de reembolso de 72 h ([[2026-1026-new-api-reembolso-tareas-video-a-72-horas]]) es la otra cara de esta misma política.
Para el modelo de coste del vault, este es un recordatorio de que **el vídeo no se puede comparar con el texto en la misma columna**: la unidad depende del proveedor (segundos × resolución), y eso es una fuente más de heterogeneidad junto a las que ya están catalogadas ([[2026-1023-priceai-codificacion-por-requests-vs-prompts-vs-creditos]]).
