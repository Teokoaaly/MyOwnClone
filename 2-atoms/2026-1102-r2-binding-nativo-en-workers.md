---
id: 2026-1102-r2-binding-nativo-en-workers
type: atom
certainty: solid
sources: [sources/2026-11-02-cloudflare-r2-storage.md]
links: ["[[2026-1031-cloudflare-r2-storage]]", "[[2026-10-29-workers-compute-requests]]", "[[2026-10-29-d1-database]]"]
---

## Claim
Cloudflare Workers accede a los buckets de R2 mediante una API nativa sin gestionar claves de API ni SDKs: el código de ejemplo escribe con `await env.MY_BUCKET.put(key, request.body)` y lee con `const object = await env.MY_BUCKET.get(key)`, sin endpoint S3 ni credenciales en el código.

## Why It Matters
Elimina el coste operativo de la capa de credenciales: no hay keys que rotar, ni endpoint que hardcodear, ni librería S3 que mantener en el backend. Para MyOwnClone (Flask + Next.js) esto significa que servir los artefactos de un clone —o el histórico de una conversación— desde el edge no exige un segundo camino de código con SDK S3, sino simplemente lógica dentro de la función. El coste por lectura no desaparece: sigue aplicando la operación de clase B de [[2026-1031-r2-clases-de-operacion-a-y-b]], aunque el propio request de Worker ya se factura aparte según [[2026-10-29-workers-compute-requests]], así que la lectura de un objeto en R2 puede generar dos partidas de coste distintas.
