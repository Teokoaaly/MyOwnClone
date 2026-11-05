---
id: 2026-1026-brightdata-cinco-tipos-de-red-en-docs-contra-cuatro-en-faq
type: atom
certainty: solid
sources: [sources/2026-10-25-brightdata-docs-intro.md]
links: ["[[2026-1024-brightdata-cuatro-tipos-de-red-y-solo-tres-pestanas-de-precio]]", "[[2026-1024-brightdata-400m-de-ips-en-195-paises-con-targeting-gratis]]", "[[2026-1026-brightdata-una-sola-api-key-para-todos-los-productos]]"]
---

## Claim
La sección "Proxy networks" de la documentación abre con **"Five network types for routing traffic at scale"** y enumera cinco: **Residential** ("400M+ real-user IPs"), **Datacenter** ("Fast, low-cost IPs"), **ISP** ("Static residential-grade IPs"), **Proxy Manager** ("Open-source proxy routing") y **Browser Extension** ("Proxies in Chrome"). La red **Mobile**, que el FAQ de precios sí describe como cuarta red con rotación 3G/4G/5G, **no aparece** en esta lista, y las dos entradas adicionales son **herramientas de cliente, no redes de IP**.

## Why It Matters
La contradicción con el átomo del FAQ es literal y verificable: el mismo proveedor, en dos páginas del mismo dominio, declara **cuatro redes de IP** —Datacenter, ISP, Residential y **Mobile** ([[2026-1024-brightdata-cuatro-tipos-de-red-y-solo-tres-pestanas-de-precio]])— y **cinco "network types"** donde solo tres son redes y las otras dos son software. Para el vault esto importa porque el conteo de "tipos" se estaba usando para cerrar la tabla de coste por insumo: **si la red móvil desaparece del catálogo de documentación, el tramo más caro de la tabla no tiene siquiera página de producto visible en la documentación oficial**.
Y hay un segundo dato en la misma línea: aquí el pool residencial se describe como **"400M+ real-user IPs"**, sin el matiz **"monthly"** que el FAQ sí usa ("400M+ monthly IPs") ([[2026-1024-brightdata-400m-de-ips-en-195-paises-con-targeting-gratis]]). El matiz importa: "400M+ reales" y "400M+ rotativas al mes" son magnitudes distintas de capacidad y de coste de rotación.

## [FRICTION]
> [[2026-1024-brightdata-cuatro-tipos-de-red-y-solo-tres-pestanas-de-precio]] afirma que el proveedor declara **cuatro redes de IP** y que el pool **Mobile** es "el más caro por gigabyte y el más resistente a bloqueo" —y que su ausencia en las pestañas de precio deja "la tabla de coste por insumo incompleta en su tramo superior".
> Este átomo presiona ese límite y lo empeora: en la **documentación** el pool móvil **no aparece en absoluto**, y el lugar que ocupa la quinta posición es un producto de software (Proxy Manager) que es **open-source**. Es decir, el recuento oficial de "tipos" mezcla dos taxonomías —redes de IP y utilidades de integración— exactamente el problema que el átomo ya señalaba dentro de la página de precios. Y la frase "400M+ real-user IPs" sin el "monthly" del FAQ sugiere que la cifra **se presenta con dos alcances distintos según la página**. Ambas no pueden ser simultáneamente la taxonomía oficial: o hay cinco redes (y entonces el móvil es una quinta), o hay cuatro (y entonces el quinto "network type" es una herramienta). Marcado para juicio humano, no auto-resuelto: la captura no publica el precio de la red móvil en ninguna de las dos páginas.
