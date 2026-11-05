---
id: 2026-1104-backblaze-b2-precios-estables-en-cinco-capturas-con-un-render-completo
type: atom
certainty: solid
sources: [sources/2026-11-04-backblaze-b2-storage-pricing.md]
links: ["[[2026-1103-backblaze-b2-precios-estables-en-cuatro-capturas-consecutivas]]", "[[2026-1102-backblaze-b2-precio-6-95-por-tb-al-mes]]", "[[2026-1102-backblaze-b2-calculadora-1738-dolares-53-menos-que-aws-s3]]", "[[2026-1104-backblaze-b2-render-completo-restaurado-resuelve-la-friccion-del-11-03]]"]
---

## Claim
Las **cinco** capturas de `backblaze.com/cloud-storage/pricing` (2026-10-31, 11-01, 11-02, 11-03 y 11-04) muestran **las mismas cifras de precio sin ninguna variación**: B2 "Starts at **$6.95/TB/mo**" facturado por byte-hora a $6.95/TB/30-días, Overdrive "Starts at **$15/TB/mo**" con "Multi-petabyte commitment required", egreso "up to 3x storage" y "then **$0.01/GB**", clase D a "**$0.004 per 10,000 calls**" con "the first **2,500 calls per day are free**", y el estimador en **$1,738** / "**$1,964** lower than AWS S3" / "**53%**" con **750 TB** de egreso gratuito. La novedad de esta quinta captura es que la estabilidad queda por primera vez **verificada sobre un renderizado completo**: el contenido sustantivo es idéntico al de la captura del 11-02, y en ella se renderiza además la línea "First 10GB storage is always free" y la viñeta de egreso por partners.

## Why It Matters
La diferencia entre "el precio no cambió" y "el precio no cambió **y además lo sabemos porque esta vez vimos la página entera**" no es retórica: las cuatro capturas anteriores mezclaban dos renders reducidos (10-31 y 11-03) con dos completos (11-01 y 11-02), lo que dejaba abierta la hipótesis de que la página hubiera cambiado precisamente en los bloques que los renders reducidos no mostraban (véase [[2026-1104-backblaze-b2-render-completo-restaurado-resuelve-la-friccion-del-11-03]]). La quinta captura **elimina esa duda**: comparada línea a línea con la del 11-02, la página de precios es la misma, con los mismos bloques y las mismas cifras. Con esto, las cifras de B2 dejan de ser un snapshot con fecha y pasan a ser **banda de referencia citable** dentro del vault: [[2026-1102-backblaze-b2-precio-6-95-por-tb-al-mes]] (~$0.0068/GB/mes frente a $0.015/GB/mes de R2) y [[2026-1102-backblaze-b2-calculadora-1738-dolares-53-menos-que-aws-s3]] (comparativa con AWS S3, GCS, Azure Blob y R2) son números que no caducan al día siguiente, con lo que un cambio de tarifa futuro es un **evento a vigilar**, no una incógnita estructural.
