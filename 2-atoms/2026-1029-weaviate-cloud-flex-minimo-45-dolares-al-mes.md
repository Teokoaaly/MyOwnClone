---
id: 2026-1029-weaviate-cloud-flex-minimo-45-dolares-al-mes
type: atom
certainty: solid
sources: [sources/2026-10-29-weaviate-cloud-pricing.md]
links: ["[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1029-weaviate-cloud-free-tier-100000-objetos-1gb-memoria]]", "[[2026-1026-heroku-key-value-store-mini-3-dolares-hasta-12500]]"]
---
## Claim
El plan **Flex** de Weaviate Cloud es "Pay-as-you-go" mensual sin compromiso y **empieza en $45/mo**, como **cluster cloud compartido**. La FAQ precisa el desglose: *"The minimum covers the baseline cluster cost and includes charges for Vector Dimensions and Storage: $45/month on Flex"* y **los backups se cobran aparte, sobre el volumen de datos y la retención**. En la tabla de comparación, Flex trae **objetos ilimitados**, **1.000 colecciones**, **retención de backup de 7 días**, HA/replicación ✓, **RBAC** ✓, **sin SSO/SAML**, disponibilidad **99,5 %**, respuesta **Sev 1 en 1 día hábil**, y **Query Agent con límite de 30.000 req/mes** (gratis hasta 1.000) más **Embeddings por uso**.

## Why It Matters
$45/mes es **una partida que no cabe en el presupuesto de ≤ €4/mes**: al cambio de referencia de ~1,10 USD/EUR que ya usa el vault en las capturas en dólares, son **≈ €40,91/mes**, es decir **~10× el techo de infraestructura** y **más que el suelo de €5,99 de Hetzner** ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]). La comparación relevante para el vault no es con el VPS sino con las otras piezas del stack gestionado: **$45 del vector store frente a $5 de Heroku Postgres Essential o $3 de Heroku Key-Value Mini** ([[2026-1026-heroku-postgres-essential-5-a-20-dolares-con-4-horas-de-parada]], [[2026-1026-heroku-key-value-store-mini-3-dolares-hasta-12500]]) — el motor vectorial sería **la pieza más cara del stack por un orden de magnitud**, y además con un mínimo fijo que no baja por debajo aunque el uso real sea cero. Eso es exactamente el patrón que el vault ya detecta en los PaaS: el precio que se paga por no tener ops. Aquí la alternativa no es un PaaS cualquiera: es **autoalojar Weaviate**, que la documentación de despliegue declara usar **la misma base de datos Weaviate** que el servicio gestionado, con lo que el saving de $45/mes es real **a cambio de la RAM del VPS**.

## Nota de verificación
La conversión a euros (≈ €40,91) y el multiplicador "~10× el techo de €4" son **cálculo de este átomo** a ~1,10 USD/EUR; la fuente publica **solo en dólares** y no en ningún momento tipo de cambio ni IVA.
