---
id: 2026-1101-aiven-postgresql-plan-gratuito-1gb-sin-region
type: atom
certainty: solid
sources: [sources/2026-11-01-aiven-postgresql-pricing.md, sources/2026-11-03-aiven-pricing.md]
links: ["[[2026-1031-aiven-postgresql-pricing]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]]"]
---

## Claim
El plan Free de PostgreSQL en Aiven cuesta **$0/month** con **1 VM dedicada, 1 CPU por VM, 1 GB RAM por VM y 1 GB de almacenamiento total**, y además **no permite seleccionar nube o región concreta** ni incluye integraciones o connection pooling.

## Why It Matters
Es el suelo de coste del componente de persistencia del stack vivo: Postgres a $0 es compatible con el presupuesto duro de ≤ €4/mes que [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]] tracking, pero solo a cambio de 1 GB de RAM y 1 GB de disco — insuficiente para multi-tenancy real y, sobre todo, sin elección de nube/región, lo que impide fijar residencia de datos o peering con el resto del stack. El plan Developer ($5/mes) sube solo el almacenamiento a 8 GB manteniendo 1 GB de RAM, así que el salto de 1 GB a 4 GB de RAM exige el plan Hobbyist ($12/mes): para [[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]] (app + Postgres + Redis) el escalón real de precio está en el RAM, no en el disco. Esto confirma el modelo descrito en [[2026-1031-aiven-postgresql-pricing]]: el precio lo fija el tamaño del plan, no el uso granular.

## 2026-11-03 — re-verificación
La tarjeta del plan Free en la captura del 2026-11-03 sigue diciendo **$0/month, 1 dedicated VM, 1 CPU per VM, 1 GB RAM per VM, 1 GB total storage, "Cannot select a specific cloud or region", "No integrations or connection pooling"** — sin variación. La de Developer mantiene 1 VM / 1 CPU / 1 GB RAM y **8 GB total storage**, con las mismas dos exclusiones. El umbral de 1 GB de almacenamiento del plan gratuito queda confirmado por una cuarta captura. Nota: la tabla de features marca "Connection pooling" en las seis columnas, lo que contradice la tarjeta de Free y Developer — [[2026-1103-aiven-la-tabla-de-features-marca-todo-incluido-pero-las-tarjetas-de-plan-lo-desmenten]].
