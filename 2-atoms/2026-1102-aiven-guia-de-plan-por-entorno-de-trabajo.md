---
id: 2026-1102-aiven-guia-de-plan-por-entorno-de-trabajo
type: atom
certainty: solid
sources: [sources/2026-11-02-aiven-postgresql-pricing.md, sources/2026-11-03-aiven-pricing.md]
links: ["[[2026-1102-aiven-escalera-de-precios-postgresql-de-0-a-270-dolares]]", "[[2026-1102-aiven-sla-99-99-solo-desde-el-plan-startup]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---

## Claim
La guía oficial de selección de plan de Aiven es: **Free** para learning, demos y tutoriales ("A real Aiven experience at no cost"); **Developer** para desarrollo, servicio gestionado affordable y no productivo, ideal para experimentar y prototipar; **Startup** para producción, "Best for lightweight staging or smaller workloads"; **Business** para producción cuando importan alta disponibilidad y mayor throughput; **Premium** para "optimized performance, speed, and availability for enterprise-grade work".

## Why It Matters
Traduce la escalera de precios ([[2026-1102-aiven-escalera-de-precios-postgresql-de-0-a-270-dolares]]) en fases de producto, y por tanto dice cuándo el producto del vault puede migrar de free tier a pago: mientras el producto es una demo, Free/Developer bastan ($0–5/mes); en cuanto hay un cliente que paga y se promete SLA, el salto mínimo es **Startup a $75/mes** (ver [[2026-1102-aiven-sla-99-99-solo-desde-el-plan-startup]]). Esto encaja con la lógica de [[2026-1022-costes-por-categoria-tenant]]: el coste de la base de datos es el que se activa con el primer cliente de pago, no con el primer usuario.

## 2026-11-03 — re-verificación
La tabla de guía de plan de la captura del 2026-11-03 es idéntica: **Free** (learning, demos, tutorials — "A real Aiven experience at no cost"), **Developer** (desarrollo — "Affordable, non-production managed service"), **Startup** (producción — "Best for lightweight staging or smaller workloads"), **Business** (producción — "when high availability and greater throughput matter"), **Premium** (producción — "optimized performance, speed, and availability for enterprise-grade work"). La FAQ que la acompaña añade el argumento de fondo: "buyers are often in a different stage of adoption or maturity", con el contraste explícito entre un developer experimenting con PostgreSQL y un banco corriendo Kafka en producción. Es la misma lógica de fases de producto que ya describe [[2026-1031-aiven-postgresql-pricing]].
