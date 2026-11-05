---
id: 2026-1103-backblaze-b2-soporte-y-migracion-como-add-ons
type: atom
certainty: solid
sources: [sources/2026-11-03-backblaze-b2-storage-pricing.md]
links: ["[[2026-1102-backblaze-b2-commit-anual-1-a-5-anos-pagado-por-adelantado]]", "[[2026-1102-backblaze-b2-overdrive-15-por-tb-con-egreso-ilimitado]]"]
---

## Claim
En la tabla de "Our pricing models have nothing to hide", bajo "Support", los tres servicios van marcados como "**Add-on**": "Implementation support", "Premium support" y "**Universal Data Migration**" — este último con la nota "**With qualifying commitment**"; en la lista de producto de B2 aparece además "Assisted data migration available" y "Discounts available with volume & term commitments".

## Why It Matters
El precio de $6.95/TB documentado en [[2026-1102-backblaze-b2-commit-anual-1-a-5-anos-pagado-por-adelantado]] es el precio **de la capacidad**, no del servicio completo: la migración, la implementación y el soporte se cobran aparte. Para el vault esto fija el coste de cambio real de proveedor: mover un bucket entre S3-compatible no es solo cambiar endpoint, es pagar (o negociar) la asistencia. Y la condición "with qualifying commitment" ata la migración gratuitada al mismo compromiso plurianual que la propia página ya declara como obstáculo de caja para un producto con presupuesto de flujo — es decir, **el único escenario en el que la migración es barata es el escenario en el que el volumen es grande y estable**, exactamente el que el vault ha marcado como improbable. La nota "Assisted data migration available" en la ficha de B2 refuerza que la migración es un servicio comercial actively sold, no una capacidad self-service.

## Nota
La captura del 2026-11-03 conserva tanto la tabla de add-ons con el "With qualifying commitment" como la ficha de B2 con "Assisted data migration available" y "Discounts available with volume & term commitments"; lo que sí pierde esta versión reducida son los enlaces y los bloques con icono que sí estaban en las capturas del 11-01 y del 11-02 (véase [[2026-1103-captura-reducida-omite-detalle-ya-documentado]]).
