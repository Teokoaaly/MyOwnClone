---
id: 2026-1104-r2-tabla-de-precios-sin-cambios-en-cuarta-captura-del-slug
type: atom
certainty: solid
sources: [sources/2026-11-04-cloudflare-r2-storage.md]
links: ["[[2026-1031-cloudflare-r2-storage]]", "[[2026-1031-r2-clases-de-operacion-a-y-b]]", "[[2026-1031-r2-infrequent-access-cuesta-al-recuperar]]", "[[2026-1031-r2-egress-cero-contrasta-con-egress-de-workers]]"]
---

## Claim
La captura del 2026-11-04 de la página de producto R2 de Cloudflare vuelve a renderizar la tabla de precios completa **sin una sola variación** respecto a la del 2026-11-02: Standard Storage 10 GB-month gratis / **$0.015 / GB-month**; Standard Class A operations 1 millón gratis / **$4.50 / million requests**; Standard Class B operations 10 millones gratis / **$0.36 / million requests**; Infrequent Access Storage — / **$0.01 / GB-month**; Infrequent Access Class A operations — / **$9.00 / million requests**; Infrequent Access Class B operations — / **$0.90 / million requests**; Infrequent Access Data Retrieval — / **$0.01 / GB**. Es la **cuarta captura de esta URL** que muestra la misma tabla (2026-10-31, 2026-11-01, 2026-11-02 y 2026-11-04); el 2026-11-03 no capturó este slug, de modo que no hay quinta captura intermedia que comparar.

## Why It Matters
La tabla de R2 queda como **banda de referencia estable y citable** dentro del vault: los precios ya registrados en [[2026-1031-cloudflare-r2-storage]], [[2026-1031-r2-clases-de-operacion-a-y-b]] y [[2026-1031-r2-infrequent-access-cuesta-al-recuperar]] no son un snapshot que caduca al día siguiente, y el contraste con el competidor ya cuantificado en [[2026-1031-r2-egress-cero-contrasta-con-egress-de-workers]] sigue siendo el mismo: R2 a $0.015/GB-month sin coste de egreso frente a Backblaze B2 a $6.95/TB/mes con sobrecoste de egreso de $0.01/GB.

Resuelve además, con la fuente a la vista, el matiz que había quedado abierto sobre "egreso gratis": la página **sí renderiza las clases de operaciones y sus precios** en la misma tabla, junto al titular "Object storage without egress fees". Es decir, el coste marginal de R2 no es cero: es cero **por transferencia de salida**, pero cada lectura o escritura se factura como operación de clase B o clase A. La ausencia de cargo de egreso no equivale a ausencia de coste por uso.

## [FRICTION]
> [[2026-1031-r2-clases-de-operacion-a-y-b]] afirma que "las operaciones se clasifican en A (escritura/listado) y B (lectura)". La página de producto **no dice eso en ningún punto**: la tabla solo nombra "Standard Class A operations" y "Standard Class B operations" con sus precios y sus tramos gratuitos, sin definir qué cae en cada clase. La captura del 11-04, cuarta repetición de la misma tabla, confirma que esa definición no está en la fuente. Ambas no pueden ser completamente correctas: o el vault debe atribuir la definición A/B a la documentación de R2 (no a esta página), o debe marcarla como inferencia propia. Marcado para juicio humano, no auto-resuelto.
