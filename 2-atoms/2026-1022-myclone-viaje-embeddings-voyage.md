---
id: 2026-1022-myclone-viaje-embeddings-voyage
type: atom
certainty: solid
sources: [raw/articles/myclone-deep-api-osint-2026-06-24.md]
links: ["[[2026-1022-myclone-knowledge-library-fuentes]]", "[[2026-1022-myclone-api-superficie-227-endpoints]]", "[[retrieval-augmented-cognition]]"]
---
## Claim
MyClone.is vectoriza con **Voyage AI** (`voyage_embeddings`): el endpoint `GET /api/v1/embeddings/stats` devolvió `{"voyage_embeddings": 96891, "total_embeddings": 96891}` — es decir, **96.891 embeddings de plataforma, todos de Voyage**, sin restos de otro proveedor. La API incluye además `POST /embeddings/migrate` y `POST /embeddings/fix-voyage-metadata`, que son señales de una migración de proveedor ya ejecutada y de deuda de metadatos en los índices.

## Why It Matters
Es el número de escala del RAG de MyClone.is: 96.891 chunks es una base vectorial de tamaño medio-grande para un producto de clones, lo que sugiere volumen real de ingesta, no un escaparate vacío. El 100 % en Voyage confirma que no hay un vector store paralelo heredado.
Los endpoints `migrate` y `fix-voyage-metadata` son la clase de deuda que [[myownclone]] heredaría al elegir proveedor: conviene decidir el proveedor de embeddings antes de indexar, porque cambiarlo después obliga a reindexar el corpus de cada creator (ver [[retrieval-augmented-cognition]] y [[2026-1022-myclone-knowledge-library-fuentes]]).
Nota: la cifra es platform-wide y fue obtenida con una sola cuenta, así que no es atribuible a un creator concreto.
