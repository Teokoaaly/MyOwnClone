---
id: 2026-1101-aiven-planes-gratis-sin-limite-de-tiempo-pero-con-apagado-por-inactividad
type: atom
certainty: solid
sources: [sources/2026-11-01-aiven-postgresql-pricing.md, sources/2026-11-03-aiven-pricing.md]
links: ["[[2026-1031-aiven-postgresql-pricing]]", "[[2026-1029-qdrant-free-tier]]", "[[2026-10-29-neon-pricing-freeplan]]"]
---

## Claim
Los planes Free de Aiven existen para **PostgreSQL, OpenSearch, Kafka y Valkey**, **no tienen límite de tiempo**, pero Aiven **se reserva el derecho de apagar servicios** que incumplan la acceptable use policy o que **queden sin uso durante un periodo prolongado**; para más memoria o funciones avanzadas hay un **trial gratuito de 30 días**.

## Why It Matters
Convierte el "free tier" de Aiven en una solución de desarrollo/evaluación, no en un hosting permanente: un serviciofree que nadie toca durante semanas puede ser apagado, lo que en el patrón multi-tenant del vault ([[2026-1022-costes-por-categoria-tenant]]) significa que un tenant con baja actividad puede perder su instancia sin aviso. Es el mismo tipo de límite que la vault ya registró para otros free tiers ([[2026-1029-qdrant-free-tier]], [[2026-10-29-neon-pricing-freeplan]]) y refuerza la regla de [[2026-1031-aiven-postgresql-pricing]]: el coste cero de la capa de datos es real pero tiene letra pequeña de continuidad.

## 2026-11-03 — re-verificación
La captura del 2026-11-03 **elimina la FAQ "Does Aiven offer a free plan?"**, de modo que **no re-verifica** ni la ausencia de límite de tiempo, ni la cláusula de apagado por inactividad, ni el trial de 30 días: esa evidencia sigue corriendo en la captura del 11-01 (y del 11-02, que sí la recogía). La versión reducida sí mantiene, en la tarjeta del plan Free, la ausencia de límite temporal explícito —no aparece ninguna nota de duración— y el límite de **1 GB de almacenamiento total** con "Cannot select a specific cloud or region" ([[2026-1101-aiven-postgresql-plan-gratuito-1gb-sin-region]]). Conclusión operativa: **el "free" de Aiven sigue siendo condicional, y su cláusula de continuidad no aparece en la cuarta captura**.

## Actualización 2026-11-04
Fuente: `sources/2026-11-04-aiven-pricing.md` (quinta captura). La FAQ "Does Aiven offer a free plan?" **vuelve a renderizarse íntegra**: se repiten los cuatro servicios con plan gratuito (**PostgreSQL, OpenSearch, Kafka, Valkey**), la ausencia de límite temporal ("Free plans do not have any time limitations"), la reserva de apagado por incumplimiento de la acceptable use policy o por inactividad prolongada, y el **trial gratuito de 30 días** para quien necesite más memoria o funciones avanzadas. La captura añade además un matiz que el 11-03 no mostraba: el free plan incluye **"capped resources and access to the Aiven experience, including management through the Console, CLI, API, Terraform Provider, plus metrics and logs"**. La cláusula de continuidad queda por tanto **re-verificada** en la quinta captura; el 11-03 fue una omisión de render. Ver [[2026-1104-aiven-la-captura-vuelve-a-ser-completa-e-identica-a-la-del-11-02]].
