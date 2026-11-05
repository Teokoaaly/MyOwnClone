---
id: 2026-1102-lambda-precios-identicos-en-las-tres-capturas
type: atom
certainty: solid
sources: [sources/2026-10-31-lambda-gpu-pricing.md, sources/2026-11-01-lambda-gpu-pricing.md, sources/2026-11-02-lambda-gpu-pricing.md]
links: ["[[2026-1031-lambda-instancias-8x-precio-por-gpu-hr]]", "[[2026-1031-lambda-b200-cluster-precio-por-gpu-hr-segun-tamano]]", "[[2026-1102-lambda-cambia-el-rotulo-de-los-modelos-entre-capturas]]"]
---

## Claim
Las tres capturas de `lambda.ai/pricing` (2026-10-31, 2026-11-01 y 2026-11-02) muestran **exactamente los mismos precios** en las tablas que todas comparten: clusters B200 a $9,86 / $9,36 / $8,87 y las cinco filas de Instances 8x (B200 $6,69, H100 $3,99, A100 80 GB $2,79, A100 40 GB $1,99, V100 $0,79). No hay variación de precio en los tres días, lo que convierte estas capturas en **tres observaciones independientes de un precio estable**, no en tres snapshots con información nueva.

## Why It Matters

Corregir el modo de lectura del corpus: la repetición no es redundante por casualidad, es **evidencia de estabilidad**, y merece quedar registrada como tal porque sostiene dos decisiones del vault: (1) las cifras de Lambda pueden usarse como referencia de mercado vigente en la semana del 3 de noviembre de 2026 sin fechas de caducidad inmediata, y (2) la captura del 2026-11-01 es la única que aporta información estructural (tablas 4x/2x/1x, H100 clusters), mientras que las del 10-31 y del 11-02 son capturas parciales del mismo bloque. La regla operativa que sale: **no duplicar átomos de precio por cada recaptura; duplicar solo cuando cambia la cifra**.

## Nota de extensión 2026-11-03
Comparación fila a fila de `sources/2026-10-31-lambda-gpu-pricing.md`, `sources/2026-11-01-lambda-gpu-pricing.md` y `sources/2026-11-02-lambda-gpu-pricing.md`. El detalle de nomenclatura divergente entre capturas se trata aparte en [[2026-1102-lambda-cambia-el-rotulo-de-los-modelos-entre-capturas]].

## Actualización 2026-11-04
La captura del 2026-11-04 (`sources/2026-11-04-lambda-gpu-pricing.md`) vuelve a mostrar **exactamente las mismas cifras** en todas las tablas que las capturas previas compartían, con dos diferencias ajenas al precio: la nota al pie de Instances anuncia precios vigentes desde el 2026-11-16, y el rótulo HGX aparece solo en la pestaña 8x. Detalle en [[2026-1104-lambda-la-tabla-de-precios-nuevos-muestra-las-mismas-cifras-que-las-capturas-anteriores]] y [[2026-1104-lambda-anuncia-precios-nuevos-con-vigencia-el-16-de-noviembre-de-2026]].
