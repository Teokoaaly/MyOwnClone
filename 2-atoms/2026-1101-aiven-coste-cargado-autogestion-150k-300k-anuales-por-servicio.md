---
id: 2026-1101-aiven-coste-cargado-autogestion-150k-300k-anuales-por-servicio
type: atom
certainty: solid
sources: [sources/2026-11-01-aiven-postgresql-pricing.md, sources/2026-11-03-aiven-pricing.md]
links: ["[[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1023-hetzner-costes-por-categoria-vs-infraestructura-propia]]"]
---

## Claim
Aiven afirma que el **coste totalmente cargado de auto-gestionar un clúster de base de datos o streaming en producción es de 150.000–300.000+ USD al año por servicio**, contando salario, guardia e incidentes; el desglose que da es compute y storage, tiempo de ingeniería, carga de guardia, upgrades de versión, parcheo de seguridad, infraestructura de backup y configuración de replicación/HA.

## Why It Matters
Es el argumento comercial del vendor, no un hecho del vault, pero merece quedar registrado porque es la contraparte exacta de la tesis del vault: [[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]] sostiene que la topología de referencia (app + Postgres + Redis) cabe en un VPS barato, y [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]] que ≤ €4/mes es alcanzable. La cifra de Aiven no refuta esa lectura (habla de *producción con guardia y compliance*, no de un VPS de 2 vCPU), pero marca el salto de precio entre "operar un demo" y "operar producción": para MyOwnClone, la decisión no es "¿pago a Aiven o no?", sino "el coste de que nadie sea dueño del incidente es invisible en el MVP y aparece entero en el mes en que hay un cliente de pago".

## 2026-11-03 — re-verificación
La captura del 2026-11-03 **elimina la FAQ "What does Aiven cost compared to running open source yourself?"**, que era la única fuente de la cifra de $150.000–$300.000+/año por servicio y de su desglose (compute y storage, tiempo de ingeniería, guardia, upgrades, parcheo, backups, replicación/HA). La versión reducida conserva solo el cierre argumental ("Aiven bundles the software, infrastructure, and the operational expertise into a single, predictable hourly rate") y la FAQ de comparación con hyperscalers con su frase "the gap closes quickly, and often inverts". La cifra sigue siendo **un dato de la captura del 11-01, no re-verificado** por la del 11-03: no la cita como hecho vigente.

## [FRICTION]
> [[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]] (escrita hace ~5 semanas) afirma que el docker-compose de referencia (New API + PostgreSQL + Redis) "no cabe en un presupuesto de 4 €/mes", mientras que este átomo recoge la afirmación de Aiven de que el coste engineering de auto-gestionar **un solo** servicio en producción es de $150.000–$300.000+/año. Ambas no pueden ser completamente correctas a la vez: o el stack del vault es tan trivial que no cuenta como "producción", o la cifra del vendor corresponde a un nivel de rigor operativo (guardia 24/7, HA multi-AZ, compliance) que el producto no necesita. Marcado para juicio humano, no auto-resuelto.

## Actualización 2026-11-04
Fuente: `sources/2026-11-04-aiven-pricing.md` (quinta captura). La FAQ "What does Aiven cost compared to running open source yourself?" **vuelve a renderizarse íntegra** y la frase es **literalmente idéntica** a la del 2026-11-01 y a la del 2026-11-02: "Studies consistently put the fully-loaded engineering cost of self-managing a production database or streaming cluster at $150,000–$300,000+ per year per service, when you factor in salary, on-call, and incident time." El desglose de las siete categorías (cloud compute and storage, engineering time, on-call burden, version upgrades, security patching, backup infrastructure, replication and HA setup) también se reproduce sin cambios. La cifra queda por tanto **re-verificada por tercera captura** y la salvedad del 11-03 ("no re-verificado por la del 11-03") queda superada: el 11-03 fue una captura de render reducido, no una retirada del dato. Ver [[2026-1104-aiven-la-captura-vuelve-a-ser-completa-e-identica-a-la-del-11-02]].
