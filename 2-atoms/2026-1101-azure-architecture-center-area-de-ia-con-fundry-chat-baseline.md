---
id: 2026-1101-azure-architecture-center-area-de-ia-con-fundry-chat-baseline
type: atom
certainty: solid
sources: [sources/2026-11-01-azure-architecture-center.md]
links: ["[[2026-1101-azure-architecture-center-arquitecturas-base-de-referencia]]", "[[2026-1101-azure-architecture-center-devops-mlops-y-genaiops-como-ciclo-de-vida]]", "[[2026-1022-myownclone-dos-repos-flask-nextjs]]"]
---

## Claim
El area de diseño "Learn about AI and Machine Learning solutions" ofrece tres entradas: `ai-ml/ai-get-started` ("Get started with AI architecture"), `data-guide/technology-choices/ai-services` ("Choose an AI service") y `ai-ml/architecture/baseline-microsoft-foundry-chat` ("Microsoft Foundry chat baseline architecture"). Es la **única baseline de chat** que el center publica de forma nominal, y está anclada a un producto concreto: Microsoft Foundry.

## Why It Matters
Para MyOwnClone —plataforma de clones IA conversacionales— esta es la categoría del center que más se le parece: una app de chat con memoria, historial y retrieval, pero **con la gestión de estado y el histórico resueltos por la plataforma de IA**, no por el Postgres del proyecto. La diferencia no es de stack sino de **propiedad del dato**: en la baseline de Foundry el historial de conversación vive en el servicio del proveedor; en el stack del vault vive en Postgres y el modelo de datos es del vault. Eso importa porque el eje abierto del vault es quién domina el TCO: si el historial queda en un servicio de IA gestionado, su coste escala con el uso por tenant y se comporta como coste por asiento, no como coste de infraestructura fijo ([[2026-1022-costes-por-categoria-tenant]]). Mantener el historial en la base propia es una decisión de coste, no solo de arquitectura — y es exactamente la que un "Choose an AI service" de Azure induciría a cuestionar.
