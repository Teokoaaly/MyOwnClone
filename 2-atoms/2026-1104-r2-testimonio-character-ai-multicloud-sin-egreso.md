---
id: 2026-1104-r2-testimonio-character-ai-multicloud-sin-egreso
type: atom
certainty: tentative
sources: [sources/2026-11-04-cloudflare-r2-storage.md]
links: ["[[2026-1031-cloudflare-r2-storage]]", "[[2026-1031-r2-egress-cero-contrasta-con-egress-de-workers]]", "[[2026-1104-r2-tabla-de-precios-sin-cambios-en-cuarta-captura-del-slug]]"]
---

## Claim
La página de producto de R2 publica un testimonio de cliente firmado por **Myle Ott, Founding Researcher de Character.AI**: "R2 has been the glue behind our multi-cloud architecture for training and processing requests. We are now able to store our training and production data in R2 for access by any cloud, without egress fees, and get the best prices and performance across multiple cloud providers." Es el caso de uso de datasets de entrenamiento de IA —la página lo refuerza en el bloque "Store AI datasets and model artifacts"— como argumento de venta del producto.

## Why It Matters
Es el único caso de uso con nombre propio y con una cita atribuida que el vault tiene de R2, y encaja con la línea "Store AI datasets and model artifacts" / "Keep training data, model weights, and analytics datasets accessible from any cloud provider without transfer fees". Para el objetivo de infraestructura barata del vault ([[2026-1031-cloudflare-r2-storage]]) el patrón es el mismo que el de B2 (ver [[2026-1031-r2-egress-cero-contrasta-con-egress-de-workers]]): **el egreso es la variable que decide el proveedor**, y quien almacena datos que otro proveedor tiene que leer —datasets de entrenamiento, artefactos servidos a usuarios— es quien paga esa factura si el storage no la tiene. La cifra que el testimonio no da es precisamente la que el vault necesita: **cuánto egreso mensual tenía Character.AI antes de migrar a R2**, sin lo cual la cita sigue siendo un claim de marketing y no un cálculo.

## Nota de caveat
El testimonio es material de marketing del propio proveedor: la página no aporta contexto adicional (volumen, precio anterior, número de proveedores), y la atribución depende de un único nombre y cargo. Se registra como `tentative` por eso. La captura del 11-04 es la cuarta en la que aparece el mismo bloque, así que no aporta novedad de contenido respecto al 11-01 — lo que aporta es que el vault deje de tener este dato sin atomizar.
