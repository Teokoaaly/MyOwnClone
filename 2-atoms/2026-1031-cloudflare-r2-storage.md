---
id: 2026-1031-cloudflare-r2-storage
type: atom
certainty: solid
sources: [sources/2026-10-31-cloudflare-r2-storage.md]
links: ["[[2026-1031-proton-business-vpn-essentials-6-99-minimo-2-usuarios]]", "[[costes-por-categoria-tenant]]"]
---

## Claim
Cloudflare R2 Storage offers per-gigabyte storage pricing with no egress fees, creating a predictable storage-cost model distinct from AWS S3's per-GB + per-GB egress pricing structure.

## Why It Matters
The no-egress-fee model means total storage cost = GB stored × $0.015/GB/month, regardless of data retrieval volume. This is a significant cost saving for data-intensive applications that perform frequent reads, contrasting with the per-seat cost dominance model where user count drives cost. For applications with high read-to-write ratios, R2's pricing can be dramatically cheaper than S3, but the cost advantage only materializes when egress volume exceeds a threshold that requires calculating the break-even point against S3's combined storage + egress model.

## Nota de extensión 2026-11-03
Fuente: `sources/2026-11-01-backblaze-b2-storage-pricing.md` y `sources/2026-11-02-backblaze-b2-storage-pricing.md`. El competidor directo de R2 queda ahora cuantificado en la misma página que el vault ya tenía fichada: **Backblaze B2 parte de $6.95/TB/30-días (~$0.0068/GB/mes)**, es decir **más de 2× más barato por GB almacenado que los $0.015/GB/mes de R2**, pero cobra **egreso a $0.01/GB por encima de 3× su almacenamiento medio** ([[2026-1102-backblaze-b2-egreso-gratis-hasta-3x-y-0-01-por-gb]]) y **transacciones de clase D a $0.004 por 10.000 llamadas** ([[2026-1102-backblaze-b2-transacciones-clase-a-b-c-gratis-y-clase-d-cobrada]]). El "no egress fees" de R2 sigue siendo cierto, pero deja de ser un argumento sin contraprestación: la comparación correcta es **coste total = almacenamiento × precio/GB + max(0, egreso − 3× almacenamiento) × $0.01/GB**, y para el caso de backup de Postgres en el vault (muchas escrituras, pocas lecturas) el 3× gratuito cubre las restauraciones, mientras que para un producto que sirva artefactos a usuarios el modelo de R2 gana. Nota adicional: **Cloudflare figura como partner de egreso ilimitado de B2**, así que la combinación B2 + Cloudflare elimina el overage de egreso sin sair del ecosistema ya presente en el vault.

## [FRICTION]
> [[2026-1024-proton-limites-de-capacidad-por-plan-500-gb-15-correos-y-50-bovedas]] caps storage at 500 GB per plan with 15 emails and 50 vaults, while Cloudflare R2 offers effectively unlimited GB at $0.015/GB/month with no egress fees. Both cannot be simultaneously optimal: the Proton plan's fixed 500 GB cap may be insufficient for high-data workloads, while R2's usage-based model could exceed the Proton plan cost if storage grows unchecked. The friction is in choosing between capacity caps (Proton) vs. unbounded usage billing (R2), which depends on projected data growth rates and read patterns.

## Nota de extensión 2026-11-03
Tabla de precios completa tal como aparece en la captura (idéntica en las capturas del 2026-10-31, 2026-11-01 y 2026-11-02 — no hay variación de precios entre las tres):

| Componente | Free | Paid |
|---|---|---|
| Standard Storage | 10 GB-month | $0.015 / GB-month |
| Standard Class A operations | 1 million | $4.50 / million requests |
| Standard Class B operations | 10 million | $0.36 / million requests |
| Infrequent Access Storage | — | $0.01 / GB-month |
| Infrequent Access Class A operations | — | $9.00 / million requests |
| Infrequent Access Class B operations | — | $0.90 / million requests |
| Infrequent Access Data Retrieval | — | $0.01 / GB |

El texto de la página es explícito en que el precio es "Object storage without egress fees" y que R2 "doesn't charge for egress". Los detalles de clases de operación, la capa Infrequent Access y el contraste de egreso con Backblaze B2 se han desglosado en [[2026-1031-r2-clases-de-operacion-a-y-b]], [[2026-1031-r2-infrequent-access-cuesta-al-recuperar]] y [[2026-1031-r2-egress-cero-contrasta-con-egress-de-workers]].

## Actualización 2026-11-04
Cuarta captura de esta URL con la **tabla de precios sin ninguna variación** (10-31, 11-01, 11-02 y 11-04; el 11-03 no capturó el slug). La captura del 11-04 es además **byte a byte idéntica a la del 11-02**, salvo el campo `captured:`. Detalle en [[2026-1104-r2-tabla-de-precios-sin-cambios-en-cuarta-captura-del-slug]] y [[2026-1104-r2-captura-byte-identica-a-la-del-11-02]].