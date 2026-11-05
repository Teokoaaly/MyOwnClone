---
id: 2026-1026-heroku-kafka-desde-100-dolares-con-1-semana-de-retencion
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-pricing.md]
links: ["[[2026-1026-heroku-key-value-store-mini-3-dolares-hasta-12500]]", "[[2026-1023-new-api-gateway-unificado-de-modelos]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---

## Claim
**Apache Kafka on Heroku** publica **21 planes** con una dimensión que ningún otro servicio de la página usa: **"Max Data Retention"**. Los tres **Basic** son **multi-tenant (shared Kafka clusters)**: **Basic 0 $100/mes** (3.73 GB, **1 semana**), **Basic 1 $125** (29.8 GB, 1 semana), **Basic 2 $175** (59.6 GB, 1 semana). Los **standard** son single-tenant con **3 Kafka brokers** y **2 semanas** de retención: **standard-0 $1,500** (150 GB), **standard-1 $1,800** (300 GB), **standard-2 $3,200** (900 GB). Los **extended** suben a **8 brokers** y **6 semanas**: **extended-0 $4,000** (400 GB), **extended-1 $5,000** (800 GB), **extended-2 $8,700** (2.400 GB). Las familias Private van de **$1,800** a **$10,800** y las Shield de **$2,200** a **$13,000**.

## Why It Matters
Es el servicio más caro de la página **en el suelo** ($100/mes, cinco veces el dyno Performance-M) y el primero del vault donde **la retención de datos es un eje de precio con techo explícito**: en el tramo barato solo se puede retener **1 semana**. El vault ya cerró el diagnóstico en otro sitio: **una suscripción de producto no es un paquete de tokens** ni, por extensión, un paquete de datos retenidos; lo que se vende es ventana temporal.
Para el producto del vault, que registra **coste de ingestión** como categoría facturable al tenant ([[2026-1022-costes-por-categoria-tenant]]) y que documenta el **gateway multi-modelo** ([[2026-1023-new-api-gateway-unificado-de-modelos]]), el dato relevante es el **salto ×15** de Basic 0 ($100, compartido, 1 semana) a standard-0 ($1,500, dedicado, 2 semanas). Es decir: **pasar de multi-tenant a single-tenant en Kafka cuesta ×15**, y el segundo salto de precio con la retención (de 2 a 6 semanas) cuesta otro ×2,67 (de $1,500 a $4,000).
El patrón que emerge al cruzar las tres tablas de datos de Heroku es consistente: **multi-tenant es barato y con retención mínima; single-tenant empieza en un orden de magnitud por encima y la retención se compra aparte**. Es el mismo eje de "la partida que se paga dos veces" que el thread de hosting barato detectaba en backups y IPv4, aplicado aquí al plano de datos.

## Nota de verificación
La captura no publica el SLA, los créditos, ni el precio del Private Space; "Max Data Retention" aparece como columna con valores 1 week / 2 weeks / 6 weeks.
