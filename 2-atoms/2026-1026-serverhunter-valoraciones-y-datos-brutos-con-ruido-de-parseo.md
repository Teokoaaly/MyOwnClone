---
id: 2026-1026-serverhunter-valoraciones-y-datos-brutos-con-ruido-de-parseo
type: atom
certainty: solid
sources: [sources/2026-10-25-serverhunter-cheap-vps.md]
links: ["[[2026-1024-lowendbox-lowend-score-cinco-estrellas-como-filtro]]", "[[2026-1024-lowendbox-captura-sin-comentarios-ni-barra-lateral]]", "[[2026-1023-priceai-grupo-qq-canal-de-feedback-y-errores-de-datos]]"]
---

## Claim
La tabla de ServerHunter añade a cada fila una **valoración de proveedor con número de reseñas** —Gullo's Hosting **3.7/5 (8 reviews)**, Centerfield Ltd **2.9/5 (25 reviews)**, Priente Cloud **3/5 (16 reviews)**, Scaleway **3.6/5 (2 reviews)**, Ignero Corp **0/5 (0 reviews)**, y el `CV-10` de Voyar Cloud **0/5 (0 reviews)**— y esa valoración **se ordena por proveedor, no por oferta**: las ocho filas de Centerfield Ltd repiten 2.9/5 (25 reviews) y las nueve de Gullo's Hosting repiten 3.7/5 (8 reviews) —es decir, la valoración es una propiedad del **proveedor**, no de la oferta, y se propaga a todas sus filas. La captura además contiene **ruido de parseo en los campos de spec**: el `CV-10` de Voyar Cloud muestra **"NVMe: 0x Infinity TB"** y **"1.97 GB"** de memoria, y la fila de Scaleway muestra **"1x x86\_64"** como nombre de procesador con **"1 core at unknown GHz"**.

## Why It Matters
La valoración es **reputación de terceros, no cumplimiento**: el vault ya catalogó el caso paralelo en LowEndBox, donde cuatro proveedores con specs muy distintas reciben el mismo "LowEnd Score ⭐⭐⭐⭐⭐" y la estrella no discrimina capacidad ni calidad ([[2026-1024-lowendbox-lowend-score-cinco-estrellas-como-filtro]]). Aquí la escala es más fina (3.7 vs 2.9) y tiene **volumen de reseñas**, lo que la hace más informativa: **el proveedor con más reseñas es el peor valorado** (Centerfield, 25 reviews, 2.9/5), mientras Scaleway —la única fila con **2 reseñas**— es también la única cuya especificación de CPU es ilegible. Ninguna de esas cifras es un SLA, un uptime o una garantía de stock, y ninguna viene con la fecha de la reseña.

El ruido de parseo ("0x Infinity TB", "1.97 GB", "unknown GHz") importa por un motivo concreto: **es la marca de un pipeline de agregación que no valida lo que scrapea**. Es el mismo fallo que el vault ya vio en la captura de LowEndBox, donde la tabla de resultados no renderizó y quedaron tokens de plantilla sin resolver ([[2026-1024-lowendbox-captura-sin-comentarios-ni-barra-lateral]]), y la razón por la que PriceAI terminó con un grupo de QQ como canal de corrección de datos ([[2026-1023-priceai-grupo-qq-canal-de-feedback-y-errores-de-datos]]). Un "0x Infinity TB" en una celda de disco es exactamente el tipo de dato que **no puede usarse para comparar specs** aunque la columna exista.

## Nota de verificación
Las valoraciones, los recuentos de reseñas y los strings de spec ("0x Infinity TB", "1.97 GB", "1x x86\_64", "unknown GHz") están transcritos literalmente. La captura **no publica** la metodología de la valoración, ni si las reseñas son de clientes verificados, ni ninguna fecha de reseña; por tanto ninguna cifra de aquí puede tratarse como señal de calidad contractual.
