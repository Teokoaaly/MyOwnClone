---
id: 2026-1104-r2-captura-byte-identica-a-la-del-11-02
type: atom
certainty: solid
sources: [sources/2026-11-04-cloudflare-r2-storage.md]
links: ["[[2026-1104-r2-tabla-de-precios-sin-cambios-en-cuarta-captura-del-slug]]", "[[2026-1102-r2-binding-nativo-en-workers]]", "[[2026-1102-r2-ecosistema-plataforma-que-se-vende-junto]]"]
---

## Claim
La captura del 2026-11-04 de `cloudflare.com/developer-platform/products/r2/` (316 líneas, `word_count: 1280`) es **idéntica byte a byte a la del 2026-11-02**, con la única diferencia del campo `captured:` y del salto de línea final. Ambas renderizan el catálogo de productos de la plataforma en formato "una etiqueta por línea" (Compute, Storage, AI, Security, Network & Content Delivery) y **omiten el mega-menú de pie de página** que sí aparecía en la captura del 2026-11-01 (`word_count: 1311`: secciones "Getting started", "Company", "Resources", "Developers", "Solutions", copyright "© 2026 Cloudflare, Inc.", aviso de privacidad y enlace a Cloudflare AI Search). El orden de los dos bloques de producto también se invierte respecto al 11-01: "Build applications using Workers and R2" aparece **después** de "Query Data in R2" en 11-02 y 11-04, y antes en 11-01.

## Why It Matters
La secuencia de renders de este slug es **completo → reducido → reducido**: la captura del 11-01 (con navegación y footer entero) y la del 11-02/11-04 (solo cuerpo de producto, sin footer) no se contradicen en contenido de R2 —la tabla de precios y los tres bloques de código son los mismos—, sino en el ruido de navegación arrastrado por el pipeline. Consecuencia operativa: la diferencia de `word_count` entre capturas de esta página **no mide riqueza de información**, y una captura "delgada" de este slug no debe leerse como una página que perdió información.

También deja el inventario de primitivas de la plataforma estable en el render actual, lo que sostiene sin fisuras el mapa de producto que ya está en el vault: el binding nativo de R2 dentro de Workers ([[2026-1102-r2-binding-nativo-en-workers]]) y la lista de primitivas que Cloudflare vende juntas —KV, Queues, Durable Objects, D1, Hyperdrive, K2, Artifacts, Basin, Vectorize— ([[2026-1102-r2-ecosistema-plataforma-que-se-vende-junto]]) se leen igual en la captura del 11-04.

## Nota
El slug **no fue capturado el 2026-11-03**: no existe `sources/2026-11-03-cloudflare-r2-storage.md`. Las capturas disponibles de esta URL son 2026-10-31, 2026-11-01, 2026-11-02 y 2026-11-04. Para las cifras de precio, el vault tiene además una quinta mención anterior en [[2026-10-29-r2-storage]], pero esa procede de otra página (`0-raw/2026-10-29-cloudflare-workers-pricing.md`), no de la página de producto de R2.
