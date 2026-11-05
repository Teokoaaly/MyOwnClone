---
id: 2026-1026-heroku-rerank-1-y-2-dolares-por-1000-consultas
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-pricing.md]
links: ["[[2026-1023-priceai-codificacion-por-requests-vs-prompts-vs-creditos]]", "[[2026-1026-heroku-embeddings-0-10-y-0-12-por-millon-de-tokens-de-entrada]]", "[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]"]
---

## Claim
La sección **Text-to-Score Models** de Heroku publica **dos modelos de reranking** con unidad **"Price / 1,000 Queries"** — no por token: **Amazon Rerank 1.0 $1.00** y **Cohere Rerank 3.5 $2.00** por 1.000 consultas. Ambos son "Text → Score" y "Region Provisioned: US | EU". El de Cohere declara "enhanced reasoning, broad data compatibility, and multilingual support for over 100 languages"; el de Amazon, "ideal for enhancing retrieval-augmented generation (RAG) systems and semantic search applications".

## Why It Matters
Es un **quinto tipo de unidad de cuota** documentado en el vault, y el más limpio de todos: **la consulta**. No tokens, no peticiones HTTP, no prompts, no créditos — **consultas de reordenación**. Y el precio por 1.000 es exactamente la misma convención de granularidad que usa el catálogo de captchas del vault (**$0.5–$2.99 por 1000** en [[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]), lo que da una **referencia de comparación directa**: un captcha cuesta entre $0.5 y $2.99 por 1000 unidades, y **1000 rerankings cuestan $1.00 o $2.00** — el mismo orden de magnitud, aunque la unidad sea radicalmente distinta.
La razón por la que esto importa al producto: el reranking es **una etapa adicional del pipeline RAG**, y por tanto una partida de coste que hoy **no aparece en el corte por categoría** del vault (que separa respuestas de clon e ingestión, [[2026-1023-priceai-codificacion-por-requests-vs-prompts-vs-creditos]]). Si un clon indexa 96.891 chunks ([[2026-1022-myclone-viaje-embeddings-voyage]]) y reranquea en cada consulta, **el número de consultas, no el tamaño del índice, es lo que factura**.
Y el dato de proveedor: **el rerank más barato es de Amazon y el más caro de Cohere (×2)**, lo que invierte la intuición habitual de que "la empresa de modelos conocida es la cara cara" — aquí el incumbent del rerank más conhecido es el doble de caro que el hiperescalador.

## Nota de verificación
La fuente **no publica** cuántos documentos se reordenan por consulta ni el desglose entre queries y documentos reordenados, por lo que no es posible derivar de ella un coste por documento reranqueado. La equivalencia de granularidad con el catálogo de captchas es lectura propia de este átomo.
