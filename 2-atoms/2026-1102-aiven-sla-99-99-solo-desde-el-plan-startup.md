---
id: 2026-1102-aiven-sla-99-99-solo-desde-el-plan-startup
type: atom
certainty: solid
sources: [sources/2026-11-02-aiven-postgresql-pricing.md, sources/2026-11-03-aiven-pricing.md]
links: ["[[2026-1102-aiven-escalera-de-precios-postgresql-de-0-a-270-dolares]]", "[[2026-1102-aiven-pitr-2-14-y-30-dias-segun-plan]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---

## Claim
El **SLA de 99,99% de uptime aparece por primera vez en el plan Startup ($75/mes)**; los planes Free, Developer y Hobbyist no lo tienen marcado en la tabla de features, y la fila "99.99% availability" queda vacía en esas tres columnas. La alta disponibilidad llega un escalón más tarde: **Business ($180/mes, 2 VMs) añade "high availability" con failover automático**, y **Premium ($270/mes, 3 VMs) añade un segundo nodo standby**.

## Why It Matters
Traduce la tabla de features en la línea de coste real de la disponibilidad, que es el patrón que el vault ya conoce en VPS ([[2026-1024-skhron-sin-backups-ni-snapshots-gestionados]]): en Aiven la HA no es un extra de configuración sino un plan. Para MyOwnClone, esto fija la regla de que **ningún tenant de pago puede recibir el SLA de 99,99% sin que la base de datos esté en Startup o superior** ($75/mes = más de 18× el presupuesto de ≤ €4/mes), lo que confirma que en el modelo por asiento ([[2026-1022-costes-por-categoria-tenant]]) el coste de cumplimiento es un mínimo fijo, no una línea variable. La coherencia con [[2026-1102-aiven-pitr-2-14-y-30-dias-segun-plan]] es total: SLA, PITR y HA aparecen en los mismos tres escalones.

## 2026-11-03 — re-verificación
La captura del 2026-11-03 mantiene la estructura: **Startup ($75/mes) con "99.99% uptime SLA"**, **Business ($180/mes) con "2 dedicated VMs" y "Everything in Startup, plus high availability"**, **Premium ($270/mes) con "3 dedicated VMs" y "Everything in Business, plus a second standby node"**. Free, Developer y Hobbyist mantienen 1 VM y 1 CPU sin SLA. Re-verificado por cuarta captura: el escalón de disponibilidad sigue costando $75/mes de entrada.
