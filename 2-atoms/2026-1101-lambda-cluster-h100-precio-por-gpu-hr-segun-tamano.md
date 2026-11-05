---
id: 2026-1101-lambda-cluster-h100-precio-por-gpu-hr-segun-tamano
type: atom
certainty: solid
sources: [sources/2026-11-01-lambda-gpu-pricing.md]
links: ["[[2026-1031-lambda-b200-cluster-precio-por-gpu-hr-segun-tamano]]", "[[2026-1101-lambda-cluster-mas-caro-que-la-instancia-del-mismo-gpu]]", "[[2026-1031-lambda-gpu-pricing]]"]
---

## Claim
La tabla "NVIDIA H100 systems" de 1-Click Clusters de Lambda publica **$6,16/GPU/hora con 16 GPUs, $5,85 con 64 GPUs y $5,54 con 256 GPUs**, en el tramo "2 weeks – 1 year"; el descuento por escala es de ~10 %, igual que en B200. La fila "1 year+ / 16+" aparece sin cifra.

## Why It Matters
Da el precio de referencia del H100 **en el formato de cluster**, que es donde Lambda concéntricamente coloca a sus clientes de/training: el mismo chip que en formato de instancia 8x cuesta $3,99/GPU-hora sale a $6,16 en cluster de 16 GPUs. La conclusión operativa para el vault es que **el formato de cluster no es una opción económica, es un formato premium con funcionalidades de red y orquestación** que no están cuantificadas en la fuente. Comparado con el eje de hosting barato del vault ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]), el H100 más barato del catálogo cuesta ~15.000 veces más por hora que el suelo de €4/mes del vault.

## Nota de extensión 2026-11-03
Cifras verbatim de la tabla "NVIDIA H100 systems" en `sources/2026-11-01-lambda-gpu-pricing.md`; esta tabla **no aparece** en las capturas del 2026-10-31 ni del 2026-11-02, que solo capturaron la tabla de B200.
