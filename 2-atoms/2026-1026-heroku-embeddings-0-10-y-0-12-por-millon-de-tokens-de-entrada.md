---
id: 2026-1026-heroku-embeddings-0-10-y-0-12-por-millon-de-tokens-de-entrada
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-pricing.md]
links: ["[[2026-1022-myclone-viaje-embeddings-voyage]]", "[[2026-1022-pgvector-embeddings-openai-inferidos]]", "[[2026-1026-heroku-inference-region-provisioned-eu-y-us-por-modelo]]"]
---

## Claim
La sección **Embedding Models** de Heroku Managed Inference publica solo **dos modelos**, con unidad **"Price / 1M Input Token"** —sin columna de salida: **cohere-embed-v4 $0.12** y **cohere-embed-multilingual $0.10**. Ambos son **"Text → Embedding"**, **"Region Provisioned: US | EU"** y de fuente **Cohere**. El cohere-embed-v4 declara "industry-leading accuracy with support for over 100 languages" y el multilingual, "state-of-the-art embedding model that supports multiple languages", ambos "helpful for developing Retrieval Augmented Generation (RAG) search".

## Why It Matters
Es la **tercera fuente de embeddings que el vault documenta**, y con precio de lista: el competidor de referencia (MyClone.is) vectoriza con **Voyage AI** y tiene **96.891 embeddings ya migrados** ([[2026-1022-myclone-viaje-embeddings-voyage]]); el otro clon usa **PGvector + OpenAI text-embedding-3** sobre Neon ([[2026-1022-pgvector-embeddings-openai-inferidos]]). Aquí aparece un **tercer proveedor con precio público por 1M de tokens de entrada**, y por tanto una comparación posible: **$0.10–$0.12 por millón de tokens de entrada** para embeddings multilingües de Cohere, frente a un Voyage cuyo precio de lista el vault **no ha verificado**.
La consecuencia práctica es de **coste de cambio de proveedor de embeddings**, que es la lección que el propio vault ya extrajo de MyClone.is: los endpoints `migrate` y `fix-voyage-metadata` son señales de que cambiar de proveedor obliga a reindexar el corpus de cada creator. Con esta tabla, el vault puede cuantificar el coste mensual del embedding en función del volumen en lugar de tratarlo como un coste oculto.
Y hay un detalle de modelo de negocio que encaja con la arquitectura del vault: **el embedding se cobra por token de entrada, no por documento indexado ni por tenant**, es decir, es un coste que escala con el uso del cliente y no con el número de clientes — que es exactamente la distinción entre coste de ingestión y coste de respuesta que separa las dos categorías del corte por categoría del vault.

## Nota de verificación
La fuente **no publica** precios de embedding de Voyage, OpenAI ni de ningún otro proveedor, ni documenta el número de tokens por documento, por lo que la comparación con MyClone.is no es cuantificable con este material.
