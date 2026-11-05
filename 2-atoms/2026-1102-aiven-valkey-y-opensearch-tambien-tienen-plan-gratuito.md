---
id: 2026-1102-aiven-valkey-y-opensearch-tambien-tienen-plan-gratuito
type: atom
certainty: solid
sources: [sources/2026-11-02-aiven-postgresql-pricing.md, sources/2026-11-03-aiven-pricing.md]
links: ["[[2026-1101-aiven-planes-gratis-sin-limite-de-tiempo-pero-con-apagado-por-inactividad]]", "[[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]]", "[[2026-1029-qdrant-free-tier]]"]
---

## Claim
Los planes gratuitos de Aiven no se limitan a PostgreSQL: hay **Free plan para PostgreSQL, OpenSearch, Kafka y Valkey**, y además Aiven ofrece un **trial gratuito de 30 días** para quien necesite más memoria o funciones avanzadas. La página de precios lista además servicios de pago con su propia página: MySQL, Valkey, OpenSearch, Apache Kafka, Kafka Connect, MirrorMaker 2, ClickHouse, DataHub, Runtime, Metrics y Grafana.

## Why It Matters
Permite construir el stack completo del vault en Aiven a coste cero de licencia durante la fase de evaluación: Postgres + Valkey (el sustituto de Redis) + OpenSearch como vector store, es decir el mismo trío que [[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]] despliega hoy en Docker, pero con backups, PITR, VPC peering y upgrades gestionados desde el primer día. Salvedad: **no hay free tier para el motor vectorial si se elige Qdrant o Weaviate** (ver [[2026-1029-qdrant-free-tier]]), así que ese es el componente que quedaría fuera del presupuesto cero — y recordatorio de que el apagado por inactividad de [[2026-1101-aiven-planes-gratis-sin-limite-de-tiempo-pero-con-apagado-por-inactividad]] aplica a los cuatro servicios gratuitos por igual.

## 2026-11-03 — re-verificación
La captura del 2026-11-03 **elimina la FAQ "Does Aiven offer a free plan?"**, así que no repite ni la lista de servicios con plan gratuito (PostgreSQL, OpenSearch, Kafka, Valkey) ni la cláusula de apagado por inactividad: esa evidencia sigue corriendo en las capturas del 11-01 y del 11-02. La versión reducida **sí mantiene** la lista de pestañas de producto de la página: PostgreSQL, MySQL, Valkey, OpenSearch, Apache Kafka, Kafka Connect, MirrorMaker 2, ClickHouse, Aiven DataHub, Runtime, Metrics y Grafana — es decir, la oferta es de doce productos, pero la tabla de precios que se renderiza en detalle es solo la de PostgreSQL.
