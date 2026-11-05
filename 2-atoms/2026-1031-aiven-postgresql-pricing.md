---
id: 2026-1031-aiven-postgresql-pricing
type: atom
certainty: solid
sources: [sources/2026-10-31-aiven-postgresql-pricing.md, sources/2026-11-01-aiven-postgresql-pricing.md, sources/2026-11-02-aiven-postgresql-pricing.md, sources/2026-11-03-aiven-pricing.md]
links: ["[[2026-1031-proton-business-vpn-essentials-6-99-minimo-2-usuarios]]", "[[costes-por-categoria-tenant]]"]
---

## Claim
Aiven's plan-based PostgreSQL pricing bills by workload size rather than granular consumption, making costs predictable and workload-size-dependent rather than usage-granular.

## Why It Matters
Compared to consumption-based compounding (charging by ingest volume, partition count, or connector usage), Aiven's per-plan pricing eliminates unpredictable cost compounding as usage grows. This is critical for multi-tenant cost modeling where per-seat cost dominance (validated by the `costes-por-categoria-tenant` thread) makes user count the primary cost variable rather than granular usage metrics.

## [FRICTION]
> [[2026-1024-proton-limites-de-capacidad-por-plan-500-gb-15-correos-y-50-bovedas]] asserts storage grows with the number of seats: adding users buys capacity, and reasignment is done from the admin panel. Both atoms describe the same mechanism from different angles (capacity mechanics vs. cost implications), but the differing emphasis — one on reasignment logistics, the other on cost dominance — could confuse readers unfamiliar with the `costes-por-categoria-tenant` thread. No technical contradiction exists, but the differential focus merits clarification.

## Nota de extensión 2026-11-03
Fuentes: `sources/2026-11-01-aiven-postgresql-pricing.md` y `sources/2026-11-02-aiven-postgresql-pricing.md` (tres capturas consecutivas de la misma página `aiven.io/pricing`; la del 2026-11-01 y la del 2026-11-02 son sustancialmente más ricas que la del 2026-10-31).

**La afirmación original se confirma y se cuantifica.** El modelo por plan no es una descripción marketing: la página publica la escalera completa de PostgreSQL — **Free $0, Developer $5, Hobbyist desde $12 ($0,02/h), Startup desde $75 ($0,10/h), Business desde $180 ($0,25/h), Premium desde $270 ($0,37/h)** — con "starting from" en los tres últimos porque cada plan tiene **7 configuraciones** de servicio. Ver [[2026-1102-aiven-escalera-de-precios-postgresql-de-0-a-270-dolares]].

**Lo que la captura del 10-31 no mostraba: dónde está el coste real.**
- El **coste de red está incluido en los seis planes** ("All networking cost included"), frente a los hyperscalers que miden egreso, backups, HA y monitorización por separado: [[2026-1102-aiven-todo-el-coste-de-red-incluido-en-todos-los-planes]].
- **El SLA de 99,99% solo existe desde Startup ($75/mes)** y la HA desde Business ($180/mes): [[2026-1102-aiven-sla-99-99-solo-desde-el-plan-startup]].
- **El PITR escala 2/14/30 días** y por debajo de $75 no hay PITR, solo un backup de desastres: [[2026-1102-aiven-pitr-2-14-y-30-dias-segun-plan]].
- **El almacenamiento dinámico es una línea de coste aparte** desde Startup: [[2026-1102-aiven-disco-dinamico-cuesta-dinero-extra-desde-startup]].
- **La factura es por hora, facturada al mes, y solo cambia si cambias algo**: la infra es un coste fijo que no escala con los tenants: [[2026-1102-aiven-factura-por-hora-facturada-al-mes-y-solo-cambia-si-cambias-algo]].
- **No hay bundles**: el coste de la plataforma es la suma de los planes de cada servicio: [[2026-1101-aiven-sin-bundles-el-coste-de-plataforma-es-la-suma-de-servicios]].

**Matices nuevos que corrigen la lectura "coste predecible sin sorpresas".**
- Aiven **anuncia** que el billing de Runtime pasará a **consumo con egreso de red y almacenamiento**, lo que erosiona la previsibilidad del modelo por plan: [[2026-1101-aiven-runtime-pasa-a-facturacion-por-uso-con-egreso-de-red]].
- **BYOC es doble facturación** (tarifa de Aiven + factura del proveedor cloud), no un descuento: [[2026-1101-aiven-marketplaces-byoc-y-descuentos-por-compromiso-anual]].
- Los planes **Free** tienen fecha de caducidad por inactividad: Aiven puede apagarlos: [[2026-1101-aiven-planes-gratis-sin-limite-de-tiempo-pero-con-apagado-por-inactividad]].

**Contraste con el resto del vault.** El suelo de "Postgres gestionado" del mercado ($5–12/mes en Aiven, Heroku y Render) está **muy por encima del presupuesto de ≤ €4/mes** que [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]] documenta, y el primer plan con SLA cuesta $75/mes. El argumento del vendor de que auto-gestionar un servicio en producción cuesta $150.000–$300.000+/año ([[2026-1101-aiven-coste-cargado-autogestion-150k-300k-anuales-por-servicio]]) es la contraparte no verificable de la tesis del vault sobre el VPS barato ([[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]]).

## Nota de extensión 2026-11-04 (cuarta captura, 2026-11-03)
Fuentes: `sources/2026-11-03-aiven-pricing.md`. La captura del 11-03 es una **renderización reducida** de la misma página (680 palabras frente a los ~19.000 bytes del 11-02): conserva la tabla de planes y la tabla de features íntegras y cuatro FAQ, pero elimina seis secciones. **Todos los datos numéricos son idénticos** a los de las capturas anteriores —precios, almacenamiento, PITR, SLA, nubes y regiones—, lo que confirma que la página no se ha movido en cuatro días: [[2026-1103-aiven-precios-pitr-y-nubes-estables-en-cuatro-capturas-consecutivas]].

Lo que la cuarta captura **añade de verdad**:
- El **soporte está graduado por plan**: Free solo por documentación, desde Developer correo con respuesta best-effort — [[2026-1103-aiven-soporte-por-plan-documentacion-en-free-y-email-best-effort-desde-developer]].
- La página **se contradice a sí misma** entre tarjeta de plan y tabla de features (connection pooling) — [[2026-1103-aiven-la-tabla-de-features-marca-todo-incluido-pero-las-tarjetas-de-plan-lo-desmenten]].
- El precio mensual y la tarifa horaria **no reconcilian** en horas por plan (600 h frente a 720–750 h) — [[2026-1103-aiven-el-precio-mensual-y-la-tarifa-horaria-implican-horas-distintas-segun-plan]].

## Actualización 2026-11-04
Fuente: `sources/2026-11-04-aiven-pricing.md` (quinta captura, render **completo**, idéntico al del 11-02). Ninguna cifra de la página ha cambiado: la escalera de precios, el almacenamiento, el PITR, el SLA, la HA, las nubes y las nueve regiones son los mismos valores por quinta vez. Lo que la captura restituye son las seis FAQ que el render del 11-03 había eliminado: free plan (con su cláusula de apagado por inactividad y el trial de 30 días), multi-servicio sin bundles, marketplaces/BYOC/compromiso anual, coste cargado de auto-gestión ($150.000–$300.000+/año por servicio), comparación con vendors de una sola tecnología y tiers de soporte. Ver [[2026-1104-aiven-la-captura-vuelve-a-ser-completa-e-identica-a-la-del-11-02]], [[2026-1104-aiven-comparacion-con-vendors-de-una-sola-tecnologia-feature-gating-y-lock-in]] y [[2026-1104-aiven-nueve-regiones-seleccionables-frente-al-claim-de-100-mas]].