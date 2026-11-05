---
id: 2026-1101-r2-migracion-progresiva-legacy
type: atom
certainty: solid
sources: [sources/2026-11-01-cloudflare-r2-storage.md]
links: ["[[2026-1031-cloudflare-r2-storage]]", "[[2026-1031-r2-api-compatible-s3-cambio-de-endpoint]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]"]
---

## Claim
Cloudflare R2 puede situarse delante del proveedor de object storage existente y copiar los objetos progresivamente a medida que se solicitan ("R2 can sit in front of your legacy object storage provider and progressively copy objects as they are requested"), permitiendo el beneficio de cero egreso sin gestionar una migración masiva de datos.

## Why It Matters
Esto convierte una migración de storage —potencialmente la operación más cara y lenta de un cambio de proveedor— en una tarea sin coste de transferencia: no hay que mover el dataset, solo cambiar el endpoint y dejar que los objetos se copien bajo demanda. Combinado con la API compatible con S3 (ver [[2026-1031-r2-api-compatible-s3-cambio-de-endpoint]]), permite entrar en Cloudflare sin asumir el coste de salida que hoy se paga en los proveedores con egreso, lo que encaja con el objetivo de infraestructura barata del vault ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]). Para MyOwnClone tiene una lectura directa: los artefactos de los clones y el histórico de conversaciones podrían empezar a escribirse en R2 sin tener que mover primero nada de un proveedor anterior, con el coste de egreso eliminado desde el primer día ([[2026-1031-cloudflare-r2-storage]]).
