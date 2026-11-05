---
id: 2026-1102-aiven-disponibilidad-de-nube-y-region-por-plan
type: atom
certainty: solid
sources: [sources/2026-11-02-aiven-postgresql-pricing.md, sources/2026-11-03-aiven-pricing.md]
links: ["[[2026-1102-aiven-escalera-de-precios-postgresql-de-0-a-270-dolares]]", "[[2026-1031-aiven-postgresql-pricing]]", "[[2026-1031-hetzner-cloud]]"]
---

## Claim
La selección de nube depende del plan: **Free y Developer tienen "Limited"** en la fila Clouds y además **no pueden elegir nube ni región**; **Hobbyist** queda en **DigitalOcean, Google Cloud y OVH**; **Startup, Business y Premium** dan acceso a las seis nubes (**AWS, DigitalOcean, Google Cloud, Microsoft Azure, OVH, UpCloud**). Las regiones listadas en la página son diez: blr, sgp, tor, fra, lon, ams, syd, nyc, sfo — y la FAQ afirma que Aiven opera en **"100+ regions"** sobre AWS, Google Cloud y Azure.

## Why It Matters
La Atomicidad de la regla de cloud se paga en forma de precio: **la primera decisión real (dónde vive el dato) solo es posible a partir de $12/mes**, y el multi-nube completo (AWS + Azure + GCP) solo desde $75/mes. Para un vault que compara proveedores de infraestructura en una sola región europea ([[2026-1031-hetzner-cloud]]), el plan Hobbyist con DigitalOcean/Google/OVH y regiones de Frankfurt, Ámsterdam y Londres es el encaje más barato — pero con 1 GB de RAM. El argumento de portabilidad multi-nube de [[2026-1031-aiven-postgresql-pricing]] es real (100+ regiones) y a la vez irrelevante para el producto: lo que importa es si el plan de $75 aporta el multi-nube que el cliente enterprise pediría.

## 2026-11-03 — re-verificación
La fila "Clouds" de la captura del 2026-11-03 es idéntica: **Limited** para Free y Developer, **DigitalOcean, Google Cloud, OVH** para Hobbyist y las **seis nubes (AWS, DigitalOcean, Google Cloud, Microsoft Azure, OVH, UpCloud)** para Startup, Business y Premium. El selector de la tarjeta de PostgreSQL vuelve a listar las mismas nueve regiones nombradas (blr, sgp, tor, fra, lon, ams, syd, nyc, sfo). El recuento de "diez regiones" de este átomo queda en discusión: [[2026-1103-aiven-precios-pitr-y-nubes-estables-en-cuatro-capturas-consecutivas]].
