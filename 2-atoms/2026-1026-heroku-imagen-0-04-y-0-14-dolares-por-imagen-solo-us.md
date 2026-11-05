---
id: 2026-1026-heroku-imagen-0-04-y-0-14-dolares-por-imagen-solo-us
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-pricing.md]
links: ["[[2026-1026-heroku-inference-region-provisioned-eu-y-us-por-modelo]]", "[[2026-1023-midjourney-proxy-relevancia-para-clones-con-imagen]]", "[[2026-1026-heroku-rerank-1-y-2-dolares-por-1000-consultas]]"]
---

## Claim
La sección **Image Models** de Heroku Managed Inference publica **dos modelos** con unidad **"Price / image"** — ni tokens ni consultas: **Stable-image-core $0.04** y **Stable-image-ultra $0.14**, ambos "Text → Image", ambos de **Stability AI** y ambos con **"Region Provisioned: US"** (la página declara que el filtro de imagen solo ofrece US). El core se describe como "state-of-the-art image generation model... improved resolution, finer details, and greater consistency compared to earlier versions"; el ultra, "state-of-the-art diffusion (image generation) model".

## Why It Matters
Es la **tercera unidad de coste de IA del vault** y la más comparable con el debate de imagen que ya está abierto: **$0.04 o $0.14 por imagen** frente a los bridges no oficiales de Midjourney que el vault ha analizado y cuya comparativa de coste no se podía cerrar porque "no da SLA" ([[2026-1023-midjourney-proxy-relevancia-para-clones-con-imagen]]). Aquí hay un precio de lista, por imagen, de un proveedor que **además** da SLA de plataforma — que es exactamente el eje de la decisión "proveedor oficial vs bridge frágil".
El dato de provider es más importante que el precio: **Stability AI es el proveedor de los dos**, y sus dos gamas están separadas por **×3,5** — la misma lógica de "tier" que en los dynos, donde la diferencia de calidad se paga con un multiplicador y no con una función.
Y la restricción de región es dura: **la imagen es US-only**. Para un clon europeo, generar imagen en Heroku implica **transferencia internacional de datos** de forma obligatoria, sin alternativa dentro del mismo catálogo. Eso convierte a la imagen en la capacidad que **no se puede localizar en la UE** dentro de un proveedor que sí ofrece modelos Claude completos en región EU, y es un dato que debe ir al análisis de privacidad del producto.

## Nota de verificación
La fuente **no publica** el número de imágenes por generación, ni resolución, ni la relación entre el precio por imagen y el número de pasos de generación. Los dos únicos modelos de imagen del catálogo son Stability AI.
