---
id: 2026-1026-heroku-connect-demo-gratis-y-ediciones-enterprise-exclusivas
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-pricing.md]
links: ["[[2026-1026-heroku-postgres-essential-5-a-20-dolares-con-4-horas-de-parada]]", "[[2026-1026-heroku-elements-1-credito-igual-a-1-dolar-solo-enterprise]]", "[[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]]"]
---

## Claim
La sección **Heroku Connect** declara: *"Seamlessly sync data between Heroku Postgres and Salesforce with Heroku Connect. **Start free with the Demo Edition**. Upgrade to Enterprise or Shield Editions—**available exclusively to Heroku Enterprise customers**—for advanced performance and security."* Es decir, tres ediciones (**Demo**, **Enterprise**, **Shield**) con la puerta de entrada gratuita y las dos de pago **reservadas a clientes de Heroku Enterprise**, sin precio publicado para ninguna de ellas.

## Why It Matters
El dato de estructura es más interesante que el producto: **Heroku Connect es un puente de datos bidireccional entre Heroku Postgres y Salesforce**. Para el vault eso describe un **patrón de integración de CRM** sobre la propia base de datos gestionada, es decir, un camino de **sincronización de datos de tenant con un CRM externo** sobre la misma Postgres que sirve a la aplicación — no sobre una réplica.
Y el dato de política comercial: la edición gratuita se llama **"Demo"**, no "Free", y las dos ediciones con rendimiento y seguridad reales están **exclusivamente** para clientes Enterprise. Es el mismo patrón de **segmentación** que el vault ha visto en el precio de los add-ons: lo gratis es una demo, y lo que de verdad se usa tiene una puerta de entrada comercial. Junto con el sistema de créditos del Marketplace ([[2026-1026-heroku-elements-1-credito-igual-a-1-dolar-solo-enterprise]]), dibuja un proveedor donde **el precio de lista público cubre el tracto self-service y el tracto empresarial se cotiza a medida**.
Para el producto del vault, que despliega Postgres + Redis + ClickHouse ([[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]]) y que hereda de Postgres un techo de **20 conexiones en Essential** ([[2026-1026-heroku-postgres-essential-5-a-20-dolares-con-4-horas-de-parada]]), Connect introduce un **consumidor externo de esa base**: un conector de Salesforce contra la misma Postgres es exactamente el patrón que puede agotar el pool de conexiones del tier barato, que es el que el producto de $99/mes compraría.

## Nota de verificación
La página **no publica precios** para ninguna de las tres ediciones de Heroku Connect, ni límites (frecuencia de sync, número de objetos, registros), ni los "advanced performance and security" concretos. El nombre del producto y sus tres ediciones son lo único verificable.
