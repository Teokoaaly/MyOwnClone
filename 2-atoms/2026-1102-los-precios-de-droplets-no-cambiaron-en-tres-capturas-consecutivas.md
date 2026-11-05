---
id: 2026-1102-los-precios-de-droplets-no-cambiaron-en-tres-capturas-consecutivas
type: atom
certainty: solid
sources: [sources/2026-10-31-digitalocean-droplets-pricing.md, sources/2026-11-01-digitalocean-droplets-pricing.md, sources/2026-11-02-digitalocean-droplets-pricing.md]
links: ["[[2026-1031-digitalocean-entrada-basic-512-mib-4-dolares-al-mes]]", "[[2026-1101-digitalocean-el-precio-mensual-es-exactamente-672-horas-de-tarifa-horaria]]", "[[2026-1024-buyvm-comparativa-precios-15-al-mes-contra-aws-do-linode-y-vultr]]"]
---

## Claim
Las tres capturas consecutivas de `digitalocean.com/pricing/droplets` (2026-10-31, 2026-11-01 y 2026-11-02) publican **precios idénticos**: el conjunto completo de importes de las tablas Basic, CPU-Optimized, General Purpose, Memory-Optimized y Storage-Optimized coincide cifra por cifra entre las tres. Las diferencias entre capturas son de **cobertura de texto**, no de precio: la del 2026-10-31 es una captura recortada (153 líneas, con el bloque central —la sección v5— omitido y resumido), la del 2026-11-01 trae la v5 completa pero con dos preguntas de FAQ sin respuesta ("Can I prepay for my resources?" y "How do I destroy my resources?"), y la del 2026-11-02 es la más completa (351 líneas, con esas dos respuestas y la de reembolso).

## Why It Matters
Convierte las tres capturas en **una sola medición con tres confirmaciones**, y da al vault un punto de confianza metodológico: los precios de DO son estables en la ventana medida, de modo que **el churn de las cifras detectado en la tabla de BuyVM ($40/mes para DO) no es atribuible a una subida reciente del proveedor** — si el precio hubiera subido, el 2026-11-02 lo mostraría. La lectura que sostiene es la inversa: **o el precio de DO bajó antes de esta ventana, o la cifra de BuyVM nunca correspondió al plan actual**. Además fija un patrón de captura que conviene replicar: cuando una página de precios se captura en fechas distintas, la comparación debe hacerse sobre el **conjunto de cifras**, no sobre el texto, porque el recorte del scraper cambia por completo la sección de FAQ sin tocar un solo número.

## Nota de verificación
Comparación por extracción del conjunto de importes con dos decimales en los tres archivos de `sources/`. Los conjuntos son idénticos salvo dos valores ausentes en la captura del 2026-10-31 ($0.05 y $0.36), atribuibles al **bloque v5 recortado** en esa captura, no a un cambio de precio — los mismos valores aparecen en las capturas completas del 2026-11-01 y 2026-11-02. La estabilidad está medida **solo dentro de la ventana 2026-10-31 → 2026-11-02**; no hay ninguna afirmación sobre el precio fuera de ella.
