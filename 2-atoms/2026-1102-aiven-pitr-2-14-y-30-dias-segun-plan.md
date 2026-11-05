---
id: 2026-1102-aiven-pitr-2-14-y-30-dias-segun-plan
type: atom
certainty: solid
sources: [sources/2026-11-02-aiven-postgresql-pricing.md, sources/2026-11-03-aiven-pricing.md]
links: ["[[2026-1102-aiven-escalera-de-precios-postgresql-de-0-a-270-dolares]]", "[[2026-1024-skhron-sin-backups-ni-snapshots-gestionados]]", "[[2026-1029-sentry-pricing-data-retention]]"]
---

## Claim
La retención de "restore to any point in time" (PITR) escala con el plan de Aiven: **Free, Developer y Hobbyist solo tienen "Single backup only for disaster recovery"**, **Startup da 2 días**, **Business da 14 días** y **Premium da 30 días**. En todos los planes, en cambio, "Real-time backups to a remote location" está marcado como incluido.

## Why It Matters
Define el mínimo de recuperabilidad vendible: por debajo de $75/mes no existe PITR, solo un backup de desastres. Para un producto SaaS multi-tenant con datos de clientes, la ventana de recuperación es un requisito contractual, no un extra — y el primer plan que la ofrece cuesta $75/mes, lo que empuja el suelo de infraestructura muy por encima del presupuesto de ≤ €4/mes que [[2026-1024-skhron-sin-backups-ni-snapshots-gestionados]] documenta como la alternativa de "ni backups ni snapshots gestionados". Es el mismo eje de coste que [[2026-1029-sentry-pricing-data-retention]] mide para observabilidad: **retención como línea de precio separada**.

## 2026-11-03 — re-verificación
La captura del 2026-11-03 repite la fila de PITR sin variación: **"Single backup only for disaster recovery"** en Free, Developer y Hobbyist, **2 días** en Startup, **14 días** en Business y **30 días** en Premium. Confirma también que "Real-time backups to a remote location" sigue marcado en los seis planes. La escala de retención es estable entre capturas: [[2026-1103-aiven-precios-pitr-y-nubes-estables-en-cuatro-capturas-consecutivas]].
