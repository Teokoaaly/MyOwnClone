---
id: 2026-1029-weaviate-self-hosted-misma-base-de-datos-que-weaviate-cloud
type: atom
certainty: solid
sources: [sources/2026-10-29-weaviate-deployment-options.md, sources/2026-10-29-weaviate-cloud-pricing.md]
links: ["[[2026-1029-weaviate-seis-vias-de-despliegue-y-cual-aplica-al-vps]]", "[[2026-1029-weaviate-cloud-flex-minimo-45-dolares-al-mes]]", "[[2026-1029-qdrant-migration-oss]]"]
---
## Claim
Las instancias self-managed de Weaviate **usan la misma base de datos Weaviate que Weaviate Cloud**: *"Self-managed instances use the same Weaviate Database as WCD"*, y la FAQ de precios confirma que *"Weaviate Cloud uses the Weaviate open-source project, wrapped in a managed service that removes administration overhead and adds features like the Embedding Service, Query Agent, and Data Import"*. La diferencia entre self-managed y Cloud no es el motor, sino **el envoltorio de administración** y tres servicios añadidos: **Embedding Service, Query Agent y Data Import**.

## Why It Matters
Esta es la afirmación que convierte el self-hosting en una alternativa de verdad y no en un plan B: **el motor que ya está corriendo en el stack del vault no cambia al dejar de pagar los $45/mes** — lo que se pierde al autoalojar son exactamente tres cosas (el servicio de embeddings, el Query Agent y la importación de datos), no la búsqueda vectorial. La comparación con el competidor de categoría es explícita: Qdrant publica una herramienta de **migración de OSS a Cloud** como argumento de venta ([[2026-1029-qdrant-migration-oss]]), mientras que Weaviate declara la **identidad del motor** como argumento a favor del self-hosting. Consecuencia operativa directa para el vault: si el precio de la parte vectorial del stack es el que domina ([[2026-1029-weaviate-cloud-flex-minimo-45-dolares-al-mes]]), entonces **la decisión no es "Weaviate o Qdrant" sino "quién paga la operación del vector store"** — el self-hosting de Weaviate elimina la factura y transfiere el coste a la RAM del VPS, que es un presupuesto ya cerrado en ≤ €4/mes ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]).

## Nota de verificación
La equivalencia "mismo motor, distinto envoltorio" es lectura literal de las dos frases citadas de las fuentes. La fuente **no** publica requisitos de RAM/CPU mínimos para una instancia self-managed: el dato de memoria disponible en la captura de precios es el del **plan Free gestionado (1 GB de memoria para 100.000 objetos)**, que no es una especificación de self-hosting.
