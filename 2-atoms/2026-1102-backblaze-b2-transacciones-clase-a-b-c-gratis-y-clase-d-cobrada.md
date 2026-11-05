---
id: 2026-1102-backblaze-b2-transacciones-clase-a-b-c-gratis-y-clase-d-cobrada
type: atom
certainty: solid
sources: [sources/2026-10-31-backblaze-b2-storage-pricing.md, sources/2026-11-01-backblaze-b2-storage-pricing.md, sources/2026-11-02-backblaze-b2-storage-pricing.md, sources/2026-11-03-backblaze-b2-storage-pricing.md]
links: ["[[2026-1102-backblaze-b2-precio-6-95-por-tb-al-mes]]", "[[2026-1029-render-postgres-pricing]]"]
---

## Claim
Las llamadas API de **clase A, B y C son gratuitas para clientes pay-as-you-go** en Backblaze B2; las **transacciones de clase D cuestan $0.004 por 10.000 llamadas**, con "the first **2,500 calls per day are free**".

## Why It Matters
Es la línea de coste que separa "object storage" de "base de datos" en la factura de infraestructura de MyOwnClone. Un snapshot de Postgres es un `pg_dump` subido por PUT (clase B) y una restauración es un GET (clase B) — ninguna de las dos cuesta nada en B2 pay-as-you-go. Lo que sí cuesta son las **clase D**, que en la clasificación de Backblaze son las lecturas masivas de datos y listados de bucket: un inventario que recorre todos los objetos de un bucket para el cálculo de retención genera clase D y, con 2.500 llamadas/día gratuitas, cualquier script de housekeeping que liste objetos a diario empieza a facturar pronto. La consecuencia práctica para el vault: un backup *incremental con listados completos* puede costar más en operaciones que el propio almacenamiento. Es un recordatorio de que el coste de "guardar datos" incluye las operaciones de inventario, igual que en [[2026-1029-render-postgres-pricing]] el backup lógico no está incluido en el plan gratuito.

## 2026-11-03 — re-verificación
La tabla de transacciones se re-verifica **sin cambios** en la cuarta captura: "Class A, B, and C API calls are free for pay-as-you-go customers. Class D transactions cost **$0.004 per 10,000 calls** plus the first **2,500 calls per day are free**". El bloque de lista de producto de B2 mantiene además la viñeta "Free transactions".

**Lo que sí cambia en esta captura**: el enlace a la página de detalle de tarifas de API (`backblaze.com/cloud-storage/transaction-pricing`) aparece ahora como texto plano —"View API call rate details here"— sin URL, igual que el resto de enlaces de navegación. La URL efectiva es la misma que se cita en [[2026-1102-backblaze-b2-api-compatible-s3-sin-lock-in-de-proveedor]], y se conserva en las capturas del 11-01 y del 11-02; es el mismo artefacto de renderizado reducido descrito en [[2026-1103-captura-reducida-omite-detalle-ya-documentado]].
