---
id: 2026-1026-new-api-video-con-duracion-atomica-y-grok-imagine-por-resolucion
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1026-new-api-facturacion-de-video-por-duracion-y-resolucion-reportadas]]", "[[2026-1023-new-api-precios-por-ratio-y-expresion]]", "[[2026-1023-new-api-grupos-como-eje-de-precio-del-relay]]", "[[2026-1026-new-api-imagenes-seedream-por-task-plugin-y-tarificacion-por-tiers]]"]
---

## Claim
**v1.0.0-rc.43** añade la **duración automática (`-1`)** para **Seedance 1.5 Pro, Seedance 2.x y Wan 3.0**: la petición **reserva la duración máxima del modelo** — **12 segundos** para Seedance 1.5 Pro, **15** para 2.0, **30** para 2.5 y Wan 3.0 — y **cobra la duración que reporta el upstream**. Un `duration` en JSON en `/v1/videos` **ya llega a Ark**, y la **duración inteligente de Wan 3.0 funciona en `/v1/video/generations`** (PR #7700). En **rc.47** se corrige que **Kling generaba con la duración del `metadata` pero cobraba con la de fuera**.

## Why It Matters
El patrón de **reservar el máximo y liquidar lo reportado** es la misma arquitectura de **pre-autorización + liquidación** que aparece en el reintento de tareas ([[2026-1026-new-api-reintento-de-tarea-reserva-el-sobrante-y-no-sale-si-no-alcanza]]): se bloquea por el peor caso y se cobra por el real. Eso resuelve un problema real de los relays de vídeo, donde **el precio se paga por segundo de generación** y el cliente no sabe de antemano cuánto va a durar.
Los números concretos (12/15/30 s) son el tipo de dato que un producto de reventa necesita para **publicar precios por segundo**: sin conocer la duración máxima reservable por modelo, no se puede cotizar un trabajo de vídeo. Y con una duración reservada por modelo, **el precio deja de ser un múltiplo de un token y pasa a tener una unidad propia** — el mismo problema de unidades que el vault ya tenía abierto con la codificación por requests, prompts, créditos o dólares ([[2026-1023-priceai-codificacion-por-requests-vs-prompts-vs-creditos]]).
El arreglo de **Kling** es, en cambio, un **descuadre entre lo generado y lo cobrado** — el peor tipo de bug de facturación, porque produce una factura que el cliente no puede reproducir. Es el mismo patrón que el arreglo de Vidu en rc.45 ([[2026-1026-new-api-facturacion-de-video-por-duracion-y-resolucion-reportadas]]): la batería de correcciones de esta captura está concentrada en **que lo cobrado coincida con lo entregado**.
Y la aparición de **`-1` como valor mágico** en la API es una señal de diseño que el vault debería registrar: un enumerado de duraciones válido **no es "0, 5, 10"**, es "o el número exacto, o `-1` para que lo decida el modelo". Es el mismo estilo de convención por sufijo que ya se había visto en los modificadores de **esfuerzo** (`-none`, `-low`, `-max`) del mismo release, y que conecta con la idea de que **el gateway traduce modificadores de cliente al upstream correcto** ([[2026-1023-new-api-tokenkit-conteo-de-tokens-calibrado]]).
