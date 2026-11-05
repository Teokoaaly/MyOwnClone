---
id: 2026-1103-digitalocean-captura-reducida-sin-tablas-de-backups-ni-precios-de-v5
type: atom
certainty: solid
sources: [sources/2026-11-03-digitalocean-droplets-pricing.md]
links: ["[[2026-1101-digitalocean-backups-por-porcentaje-y-snapshots-006-por-gb]]", "[[2026-1101-digitalocean-v5-droplets-precios-por-hora-y-sin-techo-de-672-horas]]", "[[2026-1103-digitalocean-precios-identicos-en-las-cuatro-capturas-del-31-oct-al-3-nov]]"]
---

## Claim
La captura de `digitalocean.com/pricing/droplets` del **2026-11-03** es un render **reducido** respecto a las del 2026-11-01 y 2026-11-02: **825 palabras y 154 líneas** frente a 3.297 y 351 en la del día anterior. Conserva las **cinco tablas de precios completas** (31 filas, cifras idénticas), el banner de facturación por segundo y seis preguntas de la FAQ final (alertas de facturación, crédito de $5, 1-Click Apps, baja de tarjeta, prepago y reembolsos), pero **sustituye con "…" todo el bloque intermedio**: la sección de detalle de los **v5 Droplets** (precios por hora por workload), la tabla de **"Additional product pricing"** (Backup por porcentaje/por uso y Snapshots a $0.06/GB), y toda la FAQ de "Droplets specific questions" (qué es un Droplet, IPv4, ancho de banda incluido, ubicaciones de datacenters, v5 vs Bundled Plan, formas de pago, impuestos, destrucción de recursos).

## Why It Matters
Es un recordatorio operativo del pipeline de captura: **una captura reducida no es evidencia de que un dato haya desaparecido de la página**, solo de qué parte sobrevivió al render. Consecuencia práctica: las cifras de backups y snapshots ([[2026-1101-digitalocean-backups-por-porcentaje-y-snapshots-006-por-gb]]) y los precios por hora de los v5 ([[2026-1101-digitalocean-v5-droplets-precios-por-hora-y-sin-techo-de-672-horas]]) **no se pueden re-verificar ni refutar con esta captura** — siguen sosteniéndose por las capturas del 11-01 y del 11-02, y esta del 11-03 no las contradice. En cambio, sí hay un resultado limpio y usable: las **31 filas de las cinco tablas coinciden exactamente** con las de las tres capturas anteriores ([[2026-1103-digitalocean-precios-identicos-en-las-cuatro-capturas-del-31-oct-al-3-nov]]), porque las tablas sobrevivieron al render. Es el mismo patrón ya documentado con Auth0 ([[2026-1103-auth0-captura-reducida-sin-tablas-ni-feature-matrix]]) y con Aiven: **la cobertura de una captura es un dato del pipeline, no un dato del proveedor**.
