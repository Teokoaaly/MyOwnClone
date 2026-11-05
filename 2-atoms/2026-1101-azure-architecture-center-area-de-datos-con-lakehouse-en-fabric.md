---
id: 2026-1101-azure-architecture-center-area-de-datos-con-lakehouse-en-fabric
type: atom
certainty: solid
sources: [sources/2026-11-01-azure-architecture-center.md]
links: ["[[2026-1101-azure-architecture-center-arboles-de-decision-para-elegir-servicios]]", "[[2026-1022-neon-postgres-serverless]]", "[[2026-1023-hetzner-costes-por-categoria-vs-infraestructura-propia]]"]
---

## Claim
El area "Learn about Azure data solutions" publica tres entradas: `databases/database-get-started` ("Get started with data architecture"), `guide/technology-choices/data-stores-getting-started` ("Choose an Azure data service") y `example-scenario/data/greenfield-lakehouse-fabric` ("Greenfield lakehouse on Microsoft Fabric"). El escenario de referencia para datos nuevos es **un lakehouse sobre Microsoft Fabric**, no una base transaccional.

## Why It Matters
La elección por defecto de Microsoft para una carga de datos greenfield es analítica/lakehouse (Fabric, Databricks), mientras que la elección por defecto del vault para el mismo problema es **Postgres serverless** ([[2026-1022-neon-postgres-serverless]]) — la base transaccional, no el almacén analítico. La divergencia es reveladora: MyOwnClone tiene un doble perfil de datos (transaccional multi-tenant + vectorial para retrieval) y ninguna de las dos es lakehouse, así que la "greenfield recommendation" del hyperscaler no aplica. Lo transferible es el **método de las dos capas**: separar almacenamiento transaccional de almacén analítico/vectorial en lugar de meter ambos en el mismo motor. Y lo que no aplica a ≤ €4/mes es el pricing de Fabric, que es exactamente el tipo de línea de coste que el eje [[2026-1023-hetzner-costes-por-categoria-vs-infraestructura-propia]] intenta evitar.
