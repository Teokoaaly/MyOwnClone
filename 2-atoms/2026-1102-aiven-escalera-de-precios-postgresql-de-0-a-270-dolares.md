---
id: 2026-1102-aiven-escalera-de-precios-postgresql-de-0-a-270-dolares
type: atom
certainty: solid
sources: [sources/2026-11-02-aiven-postgresql-pricing.md, sources/2026-11-03-aiven-pricing.md]
links: ["[[2026-1031-aiven-postgresql-pricing]]", "[[2026-1029-render-postgres-pricing]]", "[[2026-1025-heroku-pricing-data-services]]"]
---

## Claim
La escalera de precios de PostgreSQL en Aiven es: **Free $0/month**, **Developer $5/month**, **Hobbyist desde $12/month ($0,02/hour)**, **Startup desde $75/month ($0,10/hour)**, **Business desde $180/month ($0,25/hour)**, **Premium desde $270/month ($0,37/hour)**. Los tres últimos muestran "View 7 plans", es decir, hay siete configuraciones de servicio por debajo de cada plan.

## Why It Matters
Es la tabla completa que el vault no tenía más allá de la mención genérica de [[2026-1031-aiven-postgresql-pricing]], y da tres puntos de referencia comparables: Aiven Hobbyist a $12/mes está en el mismo orden de magnitud que Render ([[2026-1029-render-postgres-pricing]], $0–$11.000/mes) y que Heroku ([[2026-1025-heroku-pricing-data-services]], Postgres desde $5/mes) — es decir, **el suelo de "Postgres gestionado" del mercado está en $5–12/mes**, muy por encima del presupuesto de ≤ €4/mes del vault. Y hay un salto de 2,4× entre Startup ($75) y Business ($180) que solo compra HA: es exactamente el tipo de escalón que un producto multi-tenant debe evitar si su coste de infra está topado, porque los tenants pagan por asiento y la base de datos es fija.

## 2026-11-03 — re-verificación
La cuarta captura de `aiven.io/pricing` (2026-11-03) reproduce **exactamente** la misma escalera: Free $0, Developer $5, Hobbyist desde $12 ($0,02/h), Startup desde $75 ($0,10/h), Business desde $180 ($0,25/h), Premium desde $270 ($0,37/h), con "View 7 plans" en los tres últimos. No hay ninguna variación de precio ni de estructura entre el 10-31 y el 11-03, lo que confirma que la escalera es un dato estable y citable: [[2026-1103-aiven-precios-pitr-y-nubes-estables-en-cuatro-capturas-consecutivas]].
