---
id: 2026-1101-r2-data-catalog-iceberg-consulta-sql
type: atom
certainty: solid
sources: [sources/2026-11-01-cloudflare-r2-storage.md]
links: ["[[2026-1031-cloudflare-r2-storage]]", "[[2026-10-29-r2-storage]]", "[[2026-10-29-neon-pricing-objectstorage]]"]
---

## Claim
Cloudflare R2 incluye un catálogo de datos nativo compatible con Apache Iceberg ("R2's native Iceberg-compatible Data Catalog") que gestiona esquemas y permite consultar los datos estructurados almacenados en R2 con DuckDB, Spark, Trino o Snowflake; el ejemplo oficial conecta un secreto de tipo ICEBERG y hace ATTACH del catálogo con SHOW ALL TABLES y SELECT sobre una tabla Iceberg.

## Why It Matters
Convierte R2 de un blob store opaco en un lakehouse consultable con SQL estándar, lo que evita la trampa habitual de pagar dos veces: el almacenamiento de objetos y luego un warehouse o base de datos analítica aparte. Para MyOwnClone es relevante porque los logs de uso de los clones y los artefactos de training quedan consultables con DuckDB (barato, local) sin añadir un componente de data warehouse al presupuesto de ≤ €4/mes. También marca un límite frente a la alternativa ya registrada en el vault: R2 tiene su capa de catálogo y S3 no, mientras que Neon Object Storage factura los GB sin cargo por operación (ver [[2026-10-29-neon-pricing-objectstorage]]) — el precio del almacén y el precio de la capa de consulta son dos ejes distintos, igual que ocurre en [[2026-1031-cloudflare-r2-storage]].
