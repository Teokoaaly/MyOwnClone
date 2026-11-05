---
id: 2026-1101-azure-architecture-center-arboles-de-decision-para-elegir-servicios
type: atom
certainty: solid
sources: [sources/2026-11-01-azure-architecture-center.md]
links: ["[[2026-1101-azure-architecture-center-cuatro-puntos-de-entrada]]", "[[2026-1022-neon-postgres-serverless]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]"]
---

## Claim
La vía "Make technology choices" del Azure Architecture Center no ofrece comparativas de precio sino **árboles de decisión explícitos** para elegir servicio: `guide/technology-choices/compute-decision-tree` ("Choose an Azure compute service"), `guide/technology-choices/data-stores-getting-started` ("Choose an Azure data service") y `data-guide/technology-choices/ai-services` ("Choose an AI service").

## Why It Matters
Es el mismo formato de decisión que el vault necesita para su propio stack: **elegir por criterios (tamaño, workload, stateless/stateful) en lugar de por precio unitario**. MyOwnClone ya resolvió dos de esos árboles por su cuenta — Postgres serverless ([[2026-1022-neon-postgres-serverless]]) para la base y un VPS de ≤ €4/mes ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]) para el cómputo — pero no los tiene escritos como criterio: son decisiones heredadas de capturas de precios, no de un árbol. La observación estructural que aporta este center es que **la decisión de cómputo y la de datos están separadas en dos árboles distintos**, lo que fuerza a evaluar el cómputo sin razonar sobre el almacenamiento y viceversa: un error típico cuando el coste total depende de ambos (egreso hacia el origen de datos, I/O entre tiers).
