---
id: 2026-1103-backblaze-b2-precios-estables-en-cuatro-capturas-consecutivas
type: atom
certainty: solid
sources: [sources/2026-11-03-backblaze-b2-storage-pricing.md]
links: ["[[2026-1102-backblaze-b2-precio-6-95-por-tb-al-mes]]", "[[2026-1102-backblaze-b2-calculadora-1738-dolares-53-menos-que-aws-s3]]", "[[2026-1102-backblaze-b2-transacciones-clase-a-b-c-gratis-y-clase-d-cobrada]]"]
---

## Claim
Las cuatro capturas consecutivas de `backblaze.com/cloud-storage/pricing` (2026-10-31, 11-01, 11-02 y 11-03) muestran **exactamente las mismas cifras de precio**: B2 "Starts at **$6.95/TB/mo**" facturado por byte-hora a $6.95/TB/30-días, B2 Overdrive "Starts at **$15/TB/mo**" con "Multi-petabyte commitment required", egreso "up to 3x storage" y "then **$0.01/GB**", transacciones "Class D transactions cost **$0.004 per 10,000 calls** plus the first **2,500 calls per day are free**", y el estimador en **$1,738** mensuales / "**53%** lower than AWS S3" / "**$1,964**" de ahorro con **750 TB** de egreso gratuito incluido. Ninguna cifra cambió en los cuatro días.

## Why It Matters
Convierte la página de precios de Backblaze en una **referencia estable y citable** dentro del vault: los números que ya están anclados en [[2026-1102-backblaze-b2-precio-6-95-por-tb-al-mes]], [[2026-1102-backblaze-b2-calculadora-1738-dolares-53-menos-que-aws-s3]] y [[2026-1102-backblaze-b2-transacciones-clase-a-b-c-gratis-y-clase-d-cobrada]] no son un snapshot temporal que caduca al día siguiente, así que pueden usarse como banda de referencia fija al comparar proveedores de object storage. La contradicción práctica del vault —[[2026-1031-backblaze-b2-storage-pricing]] frente a [[2026-1031-cloudflare-r2-storage]]— se convierte en un hecho cuantificado y repetible: **B2 más barato por GB almacenado ($6.95/TB ≈ $0.0068/GB/mes) y con sobrecoste de egreso ($0.01/GB) y de clase D ($0.004/10.000)**, frente a **R2 a $0.015/GB/mes sin coste de egreso**. La estabilidad también acota el riesgo de decisión: si el precio no se movió en la semana, un cambio de tarifa futura es un evento a vigilar, no una incógnita estructural.

## Nota
La captura del 2026-11-03 es un **renderizado reducido** (520 palabras frente a 1.227 de la del 11-02): conserva todas las cifras de precio pero omite varios bloques secundarios. Véase [[2026-1103-captura-reducida-omite-detalle-ya-documentado]].
