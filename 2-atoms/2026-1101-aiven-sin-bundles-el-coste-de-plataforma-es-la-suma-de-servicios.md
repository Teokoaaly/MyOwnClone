---
id: 2026-1101-aiven-sin-bundles-el-coste-de-plataforma-es-la-suma-de-servicios
type: atom
certainty: solid
sources: [sources/2026-11-01-aiven-postgresql-pricing.md, sources/2026-11-03-aiven-pricing.md]
links: ["[[2026-1031-aiven-postgresql-pricing]]", "[[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]]", "[[2026-1029-qdrant-cloud-types]]"]
---

## Claim
En Aiven **no hay bundles**: el coste de una plataforma multi-servicio se calcula **prezando cada servicio por separado** (nube, región y plan) y sumando — "no bundle fees, no cross-service licensing, and no separate contracts per service". Los patrones que la propia página sugiere: **PostgreSQL + Kafka + Valkey** para plataforma de aplicación en tiempo real, **Kafka + OpenSearch** para búsqueda y analítica de logs, **Kafka + ClickHouse** para analítica en tiempo real, **PostgreSQL + Kafka + ClickHouse** para analítica orientada a cliente, **OpenSearch o Metrics + Grafana** para observabilidad.

## Why It Matters
Da la fórmula de coste del stack multi-tenant del vault: en Aiven, el patrón "Postgres + Redis + vector store" del [[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]] se pagaría como Postgres ($12–270/mes) + Valkey (el fork de Redis) + un motor vectorial (Qdrant/OpenSearch, ver [[2026-1029-qdrant-cloud-types]]) **sumados, sin descuento** — es decir, el precio de la plataforma crece linealmente con el número de piezas del stack, sin palanca de bundle. Refuerza [[2026-1031-aiven-postgresql-pricing]]: el precio depende del tamaño del plan de cada servicio, y añadir componentes es añadir facturas, no compartir infraestructura.

## 2026-11-03 — re-verificación
La captura del 2026-11-03 **elimina la FAQ "Can I run multiple Aiven services together?"** y con ella la fórmula de "prezando cada servicio por separado y sumando", los patrones de stack (PostgreSQL + Kafka + Valkey, Kafka + OpenSearch, Kafka + ClickHouse, PostgreSQL + Kafka + ClickHouse, OpenSearch o Metrics + Grafana) y la frase "no bundle fees, no cross-service licensing, and no separate contracts per service". La afirmación de no-bundles **no queda refutada por esta captura** — simplemente no aparece —; su evidencia vive en las capturas del 11-01 y del 11-02. La versión reducida sí mantiene, en cambio, la lista de pestañas de producto: PostgreSQL, MySQL, Valkey, OpenSearch, Apache Kafka, Kafka Connect, MirrorMaker 2, ClickHouse, Aiven DataHub, Runtime, Metrics y Grafana.

## Actualización 2026-11-04
Fuente: `sources/2026-11-04-aiven-pricing.md` (quinta captura). La FAQ "Can I run multiple Aiven services together?" **vuelve a renderizarse íntegra**: "price each service independently for your chosen cloud, region, and plan — then add them together. There are no bundle fees, no cross-service licensing, and no separate contracts per service", más los cinco patrones de stack (PostgreSQL + Kafka + Valkey; Kafka + OpenSearch; Kafka + ClickHouse; PostgreSQL + Kafka + ClickHouse; OpenSearch o Metrics + Grafana). La evidencia de la ausencia de bundles queda por tanto **re-verificada en la quinta captura**. Matiz de coherencia interna: la misma página afirma en otra FAQ que Aiven da toda la pila "under one platform, one contract, and one invoice", lo que es una comodidad de facturación y **no un bundle con descuento** — ver [[2026-1104-aiven-comparacion-con-vendors-de-una-sola-tecnologia-feature-gating-y-lock-in]] y su fricción con este átomo.
