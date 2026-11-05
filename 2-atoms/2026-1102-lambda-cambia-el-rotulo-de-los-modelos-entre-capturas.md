---
id: 2026-1102-lambda-cambia-el-rotulo-de-los-modelos-entre-capturas
type: atom
certainty: solid
sources: [sources/2026-10-31-lambda-gpu-pricing.md, sources/2026-11-01-lambda-gpu-pricing.md, sources/2026-11-02-lambda-gpu-pricing.md]
links: ["[[2026-1102-lambda-precios-identicos-en-las-tres-capturas]]", "[[2026-1031-lambda-h200-en-el-titulo-sin-fila-de-precio]]", "[[2026-1031-lambda-instancias-8x-precio-por-gpu-hr]]"]
---

## Claim
Con precios idénticos, las tres capturas **rotulan las mismas filas de Instances con nombres de producto distintos**: el 2026-10-31 y el 2026-11-01 usan "NVIDIA B200 SXM6 / H100 SXM / A100 SXM" y "NVIDIA Tesla V100", mientras que el 2026-11-02 usa **"NVIDIA HGX B200 / NVIDIA HGX H100 / NVIDIA HGX A100"** para las tres primeras filas (manteniendo "NVIDIA Tesla V100" en la quinta). "HGX" es el nombre de la plataforma de 8 GPUs, no de un modelo de GPU suelta, y las specs (208 vCPU, 2900 GiB, 22 TiB) son las de 8x.

## Why It Matters
Una etiqueta de catálogo que cambia entre capturas sin que cambie el precio es exactamente el tipo de ruido que hace que un corpus de fuentes sea difícil de usar: alguien que cite "NVIDIA HGX H100 a $3,99/GPU-hora" estará describiendo una plataforma de 8 GPUs, no un H100 suelto. La regla operativa para el vault: **al citar un precio de Lambda hay que anclarlo a la etiqueta de la captura y al tamaño (1x/2x/4x/8x)**, porque el mismo número aparece bajo nombres de producto que significan cosas distintas. Es también un recordatorio de por qué en el vault la nomenclatura de GPU/cloud hay que citarla literal, como ya se hizo con el caso Hostkey de "VPS con GPU" ([[2026-1024-hostkey-tres-tipos-vps-vds-y-vds-con-gpu]]).

## Nota de extensión 2026-11-03
Comparación de la columna "Plan" de las tablas de Instances en las tres fuentes. La atribución de "HGX" a plataforma de 8 GPUs es una inferencia del nombre y de las specs (208 vCPU / 2900 GiB / 22 TiB), no una frase de la fuente; la diferencia de rótulo, en cambio, es literal.

## Actualización 2026-11-04
La captura del 2026-11-04 renderiza las cuatro pestañas de Instances en un mismo documento y muestra que el rótulo HGX aparece **solo en la pestaña 8x**, mientras 4x/2x/1x mantienen "B200 SXM6 / H100 SXM / A100 PCIe / A6000". Matiza el encuadre de "cambio entre capturas" a "diferencia por pestaña". Ver [[2026-1104-lambda-el-rotulo-hgx-solo-aparece-en-la-pestana-8x]].
