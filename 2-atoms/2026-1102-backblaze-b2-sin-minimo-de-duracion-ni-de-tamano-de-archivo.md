---
id: 2026-1102-backblaze-b2-sin-minimo-de-duracion-ni-de-tamano-de-archivo
type: atom
certainty: solid
sources: [sources/2026-10-31-backblaze-b2-storage-pricing.md, sources/2026-11-01-backblaze-b2-storage-pricing.md, sources/2026-11-02-backblaze-b2-storage-pricing.md, sources/2026-11-03-backblaze-b2-storage-pricing.md]
links: ["[[2026-1102-backblaze-b2-precio-6-95-por-tb-al-mes]]", "[[2026-1029-sentry-pricing-data-retention]]", "[[2026-1024-buyvm-backups-al-10-del-precio-base-y-cinco-snapshots-gratis]]"]
---

## Claim
Backblaze B2 no cobra **coste mínimo de tamaño de archivo** ni **coste mínimo de duración de almacenamiento** ("No minimum file size fees", "No minimum storage duration fees"), y "**First 10GB storage is always free**".

## Why It Matters
La ausencia de retención mínima es la diferencia estructural frente a las clases *glacier* de AWS, donde un snapshot queda retenido y facturado durante 90 días como mínimo. Para el vault esto importa porque el patrón de backup de Postgres que se quiere montar es de **snapshots diarios con retención corta**: si cada uno de esos objetos incurriese un mínimo de 90 días, 30 snapshots diarios de una base de 20 GB facturarían 30 × 20 GB × 90 días de retención en vez de 30 días reales, y el presupuesto de ≤ €4/mes se desmoronaría. Con B2, sin mínimo, el coste de retención se paga exactamente por los bytes realmente guardados — que es la misma economía que el addon de backups de BuyVM al 10 % del precio base ([[2026-1024-buyvm-backups-al-10-del-precio-base-y-cinco-snapshots-gratis]]) pero en una escala que depende del volumen y no del servidor. Compárese también con el modelo de retención por plan de [[2026-1029-sentry-pricing-data-retention]]: allí la retención se compra subiendo de plan; aquí no hay nada que subir.

## 2026-11-03 — re-verificación
El bloque de fundamentos se re-verifica **sin cambios** en la cuarta captura: "No minimum file size or storage duration fees" y, en la lista de la ficha B2, "No minimum file size or storage duration fees".

**Lo que esta captura no permite re-verificar**: la línea "**First 10GB storage is always free**" sí estaba presente en el 11-01 y el 11-02 y **no aparece en el 11-03**, que es un renderizado degradado de la misma página (520 frente a 1.227 palabras). Al no haber cambiado ninguna cifra de precio, la interpretación correcta es **omisión del extractor, no retirada de la oferta**; el átomo permanece vigente y la línea queda marcada como no re-verificada en esta captura (véase [[2026-1103-captura-reducida-omite-detalle-ya-documentado]]).
