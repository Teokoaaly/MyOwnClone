---
id: 2026-1102-backblaze-b2-precio-6-95-por-tb-al-mes
type: atom
certainty: solid
sources: [sources/2026-10-31-backblaze-b2-storage-pricing.md, sources/2026-11-01-backblaze-b2-storage-pricing.md, sources/2026-11-02-backblaze-b2-storage-pricing.md, sources/2026-11-03-backblaze-b2-storage-pricing.md]
links: ["[[2026-1031-backblaze-b2-storage-pricing]]", "[[2026-1031-cloudflare-r2-storage]]", "[[2026-1029-render-postgres-pricing]]"]
---

## Claim
Backblaze B2 cuesta "Starts at **$6.95/TB/mo**" y la FAQ precisa el modo de facturación: "billed monthly, based on the amount of data stored per **byte-hour** over the last month at a rate of **$6.95/TB/30-days**"; además, "**First 10GB storage is always free**".

## Why It Matters
$6.95/TB/mes equivale a ~$0.0068/GB/mes, casi la mitad del $0.015/GB/mes de R2 que documenta [[2026-1031-cloudflare-r2-storage]] y [[2026-10-29-r2-storage]]: **B2 es más barato por GB almacenado, R2 es más barato por GB descargado**. Para el caso de uso que importa en este vault —snapshots de Postgres como destino de backup externo barato— el almacenamiento es la línea que domina: 100 GB de snapshots mensuales en B2 salen a ~$0.68/mes, 1 TB a ~$6.95/mes, muy por debajo del suelo de €5.99/mes de [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]. La comparación con el almacenamiento que Render cobra por la base de datos en sí ($0.30/GB/mes en [[2026-1029-render-postgres-pricing]]) sugiere que mover el almacenamiento *fuera* de la base de datos gestionada es aritméticamente favorable a partir de cierto volumen, siempre que el egreso de una restauración no se dispare (ver [[2026-1102-backblaze-b2-egreso-gratis-hasta-3x-y-0-01-por-gb]]).

## 2026-11-03 — re-verificación
La cuarta captura consecutiva de la misma URL (520 palabras, renderizado reducido) **confirma sin cambios** el precio: "Starts at **$6.95/ TB / mo**" y la FAQ de facturación "billed monthly, based on the amount of data stored per **byte-hour** over the last month at a rate of **$6.95/TB/30-days**". No aparece ninguna cifra de almacenamiento distinta de $6.95/TB en las cuatro capturas (10-31, 11-01, 11-02, 11-03): ver [[2026-1103-backblaze-b2-precios-estables-en-cuatro-capturas-consecutivas]].

**Cautela de renderizado**: la línea "**First 10GB storage is always free**" que este átomo recoge sí estaba en las capturas del 11-01 y del 11-02 pero **no aparece en la del 11-03**, que es un renderizado degradado de la misma página (520 frente a 1.227 palabras). Esto **no** es una retirada de la oferta: ninguna cifra de precio cambió y el resto del bloque de fundamentos sí se conserva. La afirmación sigue vigente pero marcada como no re-verificada en esta captura (véase [[2026-1103-captura-reducida-omite-detalle-ya-documentado]]).

## Actualización 2026-11-04 — re-verificación con render completo
La quinta captura (1.228 palabras, renderizado completo) **confirma y rehabilita** la línea que el 11-03 había dejado sin re-verificar: "**First 10GB storage is always free**" vuelve a renderizarse, junto al precio "Starts at **$6.95/ TB / mo**" y a la FAQ de facturación por byte-hora a $6.95/TB/30-días. La captura del 11-04 es sustantivamente idéntica a la del 11-02. La "cautela de renderizado" que figuraba más arriba queda **superada**: los 10 GB gratis no fueron una retirada de oferta sino una omisión del extractor (véase [[2026-1104-backblaze-b2-render-completo-restaurado-resuelve-la-friccion-del-11-03]] y [[2026-1104-backblaze-b2-precios-estables-en-cinco-capturas-con-un-render-completo]]).
