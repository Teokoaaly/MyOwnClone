---
id: 2026-1102-backblaze-b2-calculadora-1738-dolares-53-menos-que-aws-s3
type: atom
certainty: tentative
sources: [sources/2026-10-31-backblaze-b2-storage-pricing.md, sources/2026-11-01-backblaze-b2-storage-pricing.md, sources/2026-11-02-backblaze-b2-storage-pricing.md, sources/2026-11-03-backblaze-b2-storage-pricing.md]
links: ["[[2026-1102-backblaze-b2-precio-6-95-por-tb-al-mes]]", "[[2026-1031-cloudflare-r2-storage]]"]
---

## Claim
El estimador de la página, para un escenario fijo (750 TB de egreso mensual incluido como gratis), arroja "Your Backblaze B2 estimate **$1,738**" mensual y afirma "B2 is modeled **$1,964 lower than AWS S3**… **53%**" más barato; la captura del 2026-10-31 muestra el selector de comparativa con **AWS S3, Google Cloud Storage, Azure Blob Storage y Cloudflare R2**, y la nota al pie aclara que "This chart features published rates for the **U.S. West region**. Backblaze competitors' rates can vary by region, amount stored, and other factors".

## Why It Matters
El vault ya tiene un modelo de coste propio por categoría ([[2026-1022-costes-por-categoria-tenant]]) y sabe que el coste dominante es el asiento SaaS, no la infraestructura; por eso una comparativa de proveedor publicada por el propio proveedor es **insumo de marketing, no referencia de precio**. Su utilidad real es indirecta: confirma que Cloudflare R2 aparece en la comparativa oficial de Backblaze — es decir, que el competidor con el modelo de coste que el vault ya prefiere ([[2026-1031-cloudflare-r2-storage]]) es reconocido como rival en la propia página de B2, no en una nota nuestra. La cifra de $1.738 y el "53 %" están atadas a un escenario de 750 TB que no se corresponde con el perfil de MyOwnClone, y el pie de (región US West) impide extrapolar a la UE sin más; por eso el átomo queda como **tentative**.
## 2026-11-03 — re-verificación
Los valores del estimador son **idénticos** a los de las capturas del 10-31, 11-01 y 11-02: "Your Backblaze B2 estimate **$1,738**", "B2 is modeled **$1,964 lower than AWS S3**", "**53%**", "Free egress included this month **750 TB**" y la nota de alcance "This chart features published rates for the **U.S. West region**. Backblaze competitors' rates can vary by region, amount stored, and other factors". La captura del 11-03 añade, sin contradecirlo, la advertencia explícita de la FAQ "How accurate are your rate comparisons?": "The comparison charts are accurate based on published rates and **select assumptions at the time of the publication**… it is wise of you to apply further diligence based on your data set, workflow, and needs". El propio proveedor acota su comparativa, lo que refuerza la lectura de **insumo de marketing** que ya sostenía este átomo como `tentative` (ver [[2026-1103-backblaze-b2-precios-estables-en-cuatro-capturas-consecutivas]]).
