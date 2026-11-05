---
id: 2026-1102-backblaze-b2-egreso-gratis-hasta-3x-y-0-01-por-gb
type: atom
certainty: solid
sources: [sources/2026-10-31-backblaze-b2-storage-pricing.md, sources/2026-11-01-backblaze-b2-storage-pricing.md, sources/2026-11-02-backblaze-b2-storage-pricing.md, sources/2026-11-03-backblaze-b2-storage-pricing.md]
links: ["[[2026-1031-backblaze-b2-storage-pricing]]", "[[2026-1031-cloudflare-r2-storage]]", "[[2026-10-29-data-egress]]"]
---

## Claim
Backblaze B2 da "**Free egress up to 3x storage**": "All B2 Cloud Storage users get free egress up to 3x their average monthly storage… Egress beyond 3x is just **$0.01/GB**", con el promedio mensual calculado sobre byte-horas del ciclo de facturación; el pie del calculador lo repite: "*Up to 3x of average monthly data stored, then $0.01/GB for additional egress*".

## Why It Matters
Es el punto exacto donde B2 y R2 se separan: el modelo de coste de R2 documentado en [[2026-1031-cloudflare-r2-storage]] es "costo total = GB × $0.015, **independientemente del volumen de lectura**", mientras que B2 acota el egreso gratuito a 3× el almacenamiento medio y luego cobra $0.01/GB. Para un backup de Postgres el patrón de uso es asimétrico y favorable a B2: se escriben muchos snapshots (barato, sin coste de egreso) y se restaura pocas veces, así que la allowance gratuita (3×) cubre las restauraciones con holgura; el riesgo real es el **inverse**: restaurar masivamente un backup (p. ej. disaster recovery completo de 1 TB) cuesta 1 TB × $0.01 = ~$10 en egreso, y ese coste no existe en R2. El umbral de decisión no es "B2 o R2" sino "cuántas restauraciones completas al mes toleramos pagar". Es también el punto donde el eje abierto del vault —[[2026-1022-costes-por-categoria-tenant]]— se juega en la práctica: el egreso es una categoría de coste de plataforma (categoryPlatformOps) que hoy no aparece en el corte.

## [FRICTION]
> [[2026-1031-backblaze-b2-storage-pricing]] afirma que B2 es un "**pure capacity-cost model** where cost scales with stored data volume rather than number of users". La página de precios añade una línea que ese modelo no captura: el egreso por encima de 3× el almacenamiento medio se cobra a $0.01/GB, y las transacciones de clase D también se cobran (ver [[2026-1102-backblaze-b2-transacciones-clase-a-b-c-gratis-y-clase-d-cobrada]]). El coste de B2 sigue sin depender del número de asientos —eso no se contradice— pero **no es una función de la capacidad almacenada solamente**: hay un componente de egreso y otro de operaciones. Ambas no pueden ser completamente correctas a la vez. Marcado para juicio humano, no auto-resuelto.

## 2026-11-03 — re-verificación
La regla 3× / $0.01 por GB se re-verifica **sin cambios**: la ficha de B2 mantiene "Free egress up to 3x storage", el pie del calculador mantiene "* Up to 3x of average monthly data stored, then **$0.01/GB** for additional egress" y la FAQ mantiene "All B2 Cloud Storage users get free egress up to 3x their average monthly storage… Egress beyond 3x is just **$0.01/GB**—no surprise fees, no penalties". El promedio sigue calculándose sobre byte-horas del ciclo de facturación.

**Nota de renderizado**: la viñeta explicativa "Egress above 3x monthly average storage is also free through many CDN and compute partners; otherwise, overage is billed at $0.01 per GB" no aparece en la captura del 11-03 (sí en las del 11-01 y 11-02). Esa omisión afecta a [[2026-1102-backblaze-b2-egreso-gratis-ilimitado-via-cdn-y-partners]], no a la regla 3×/$0.01, que queda íntegramente re-verificada aquí (véase [[2026-1103-captura-reducida-omite-detalle-ya-documentado]]).

## Actualización 2026-11-04 — re-verificación
La regla 3× / $0.01 por GB se re-verifica **sin cambios** en la quinta captura (render completo): la ficha de B2 mantiene "Free egress up to 3x storage", el pie del calculador "*Up to 3x of average monthly data stored, then $0.01/GB for additional egress*" y la FAQ "Egress beyond 3x is just $0.01/GB—no surprise fees, no penalties". La **nota de renderizado** que figuraba en la sección anterior queda superada: la viñeta de los fundamentos "Egress above 3x monthly average storage is also free through many CDN and compute partners; otherwise, overage is billed at $0.01 per GB" **vuelve a renderizarse** en el 11-04 (véase [[2026-1104-backblaze-b2-render-completo-restaurado-resuelve-la-friccion-del-11-03]]).
