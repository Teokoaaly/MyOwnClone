---
id: 2026-1104-lambda-la-nota-de-precios-nuevos-no-aparece-en-las-tablas-de-clusters
type: atom
certainty: solid
sources: [sources/2026-11-04-lambda-gpu-pricing.md]
links: ["[[2026-1104-lambda-anuncia-precios-nuevos-con-vigencia-el-16-de-noviembre-de-2026]]", "[[2026-1031-lambda-b200-cluster-precio-por-gpu-hr-segun-tamano]]", "[[2026-1101-lambda-cluster-h100-precio-por-gpu-hr-segun-tamano]]"]
---

## Claim
En la captura del 2026-11-04, el aviso de precios nuevos **se aplica solo a las tablas de Instances**: sus cuatro pies repiten *"Plus applicable sales tax/VAT/GST. New prices take effect November 16, 2026, at 00:00 UTC. Until then, log in to your Lambda Cloud account to see current pricing."*, mientras que las dos tablas de 1-Click Clusters (NVIDIA HGX B200 y NVIDIA H100) conservan el pie corto *"\\* plus applicable sales tax/VAT/GST"*, sin fecha de vigencia ni mención a la cuenta. Los precios de cluster ($9,86/$9,36/$8,87 en B200; $6,16/$5,85/$5,54 en H100) quedan por tanto **fuera del anuncio**.

## Why It Matters
Obliga a separar el aviso en dos: solo la mitad del catálogo público de Lambda (Instances, la línea self-serve) tiene un cambio de precio fechado, mientras que la línea de clusters —que es la que tiene los CTA "Talk to our team" y la que el vault usa como referencia del formato premium ([[2026-1101-lambda-cluster-mas-caro-que-la-instancia-del-mismo-gpu]])— no lo anuncia. Para el vault la lectura correcta es: **el 16 de noviembre de 2026 solo se recolocan los precios de Instances; los de cluster se publican como "sin cambio anunciado", que no es lo mismo que "sin cambio"**, porque el tramo reservado "1 year+" sigue sin cifra publicada ([[2026-1101-lambda-precio-reservado-1-ano-sin-publicar]]). Es un recordatorio del criterio ya aplicado en el corpus: la ausencia de un aviso es un hueco, no un dato.

## Nota de método
Pies de tabla verbatim en `sources/2026-11-04-lambda-gpu-pricing.md`: la nota larga aparece 4 veces (pestañas 8x, 4x, 2x y 1x de Instances) y la corta 2 veces (tablas de clusters B200 y H100).
