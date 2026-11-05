---
id: 2026-1102-aiven-funciones-operativas-estandar-en-todos-los-planes
type: atom
certainty: solid
sources: [sources/2026-11-02-aiven-postgresql-pricing.md, sources/2026-11-03-aiven-pricing.md]
links: ["[[2026-1102-aiven-escalera-de-precios-postgresql-de-0-a-270-dolares]]", "[[2026-1031-aiven-postgresql-pricing]]", "[[2026-1029-render-postgres-pricing]]"]
---

## Claim
Las siguientes funciones están marcadas como incluidas en **los seis planes** de Aiven PostgreSQL, del Free al Premium: **All networking cost included**, seamless upgrade/downgrade entre planes, **one-click version upgrade**, extensiones (PostGIS, PL/v8, etc.), performance graphs, **data encrypted on disk and network**, real-time backups a ubicación remota, **VPC peering en AWS, GCP y Microsoft Azure**, **múltiples bases de datos lógicas por instancia**, **database forks** y **connection pooling**. Las dos únicas exclusiones o condicionamientos de la tabla son PITR y dynamic disk sizing.

## Why It Matters
El "todo incluido" de Aiven es real en la capa funcional, y esto es lo que sostiene [[2026-1031-aiven-postgresql-pricing]]: no hay gating de features por tier como en los vendors de una sola tecnología (Conectores, audit logs, RBAC premium). Para el stack del vault esto importa por dos puntos concretos: **multiple logical databases per instance** permite servir multi-tenancy en una sola instancia (encaja con el patrón de [[2026-1022-costes-por-categoria-tenant]]) y **database forks** da cloning de entornos sin coste adicional. Contraste con [[2026-1029-render-postgres-pricing]], donde los backups lógicos solo existen en planes de pago y el almacenamiento escala a $0,30/GB: Aiven es más caro en la base y más barato en las líneas satélite.

## 2026-11-03 — re-verificación
La captura del 2026-11-03 reproduce la misma tabla de features con las mismas filas y los mismos seis planes, **incluida la fila "Read-only access to DB replica nodes"**, que este átomo no recogía. Las diez filas marcadas en las seis columnas (networking incluido, seamless upgrade/downgrade, one-click version upgrade, extensiones, performance graphs, cifrado en disco y red, backups en tiempo real a ubicación remota, VPC peering en AWS/GCP/Azure, múltiples bases de datos lógicas, database forks y connection pooling) siguen apareciendo **sin distinción entre planes**, mientras que la fila de soporte **sí** diferencia Free (solo documentación) del resto (correo con respuesta best-effort). La lectura de "incluido en los seis planes" queda por tanto en discusión: [[2026-1103-aiven-la-tabla-de-features-marca-todo-incluido-pero-las-tarjetas-de-plan-lo-desmenten]].
