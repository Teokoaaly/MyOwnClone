---
id: 2026-1104-backblaze-b2-tramos-de-necesidad-de-almacenamiento-en-el-formulario-de-ventas
type: atom
certainty: solid
sources: [sources/2026-11-04-backblaze-b2-storage-pricing.md]
links: ["[[2026-1102-backblaze-b2-overdrive-15-por-tb-con-egreso-ilimitado]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1103-backblaze-b2-soporte-y-migracion-como-add-ons]]"]
---

## Claim
El formulario "B2 Cloud Storage Sales Contact" de la página de precios cualifica al posible cliente por **seis tramos de necesidad de almacenamiento**, transcritos tal cual: "Under 20TB", "20TB - 50TB", "50TB - 250TB", "250TB - 1PB", "1PB - 20PB" y "Over 20PB". El formulario exige además nombre, empresa, email, teléfono y mensaje, y declara que el cliente acepta ser contactado por el equipo comercial y recibir el newsletter.

## Why It Matters
Es la **segmentación comercial de Backblaze hecha explícita por la propia página**, y es el único sitio del vault donde el proveedor declara dónde acaba el autoservicio y empieza la venta. Los tres primeros tramos (hasta 250 TB) son el territorio natural del producto base a **$6.95/TB/mo** documentado en [[2026-1102-backblaze-b2-precio-6-95-por-tb-al-mes]]: se contrata online con "Start Free" y sin adder. Los tres últimos (desde 250 TB hasta más de 20 PB) son donde la página empuja a la conversación comercial, y es exactamente la escala en la que empieza a bitear el resto del catálogo: **Overdrive exige "Multi-petabyte commitment required"** a **$15/TB/mo** ([[2026-1102-backblaze-b2-overdrive-15-por-tb-con-egreso-ilimitado]]) y la migración asistida solo es un add-on "With qualifying commitment" ([[2026-1103-backblaze-b2-soporte-y-migracion-como-add-ons]]). El dato útil para el vault es la **frontera**: el umbral de 250 TB es donde el "Start Free" deja de ser suficiente y el precio deja de ser una cifra pública de autoservicio. Para el caso de uso del hilo de almacenamiento barato —backups de Postgres de decenas de GB — el producto base es suficiente y no hay ninguna conversación comercial que forzar; el de ≤ €4/mes de [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]] sigue sin tener ni un competitor en este tramo, porque el primer tramo del formulario arranca en "Under 20TB", muy por debajo de cualquier compromiso enterprise.

## Nota
Esta lista de tramos ya era visible en las capturas del 2026-11-02 y había sido señalada como **elemento omitido** en el render reducido del 11-03 (ver [[2026-1103-captura-reducida-omite-detalle-ya-documentado]]); la captura del 11-04 la vuelve a renderizar y la deja citable por primera vez como atom con fuente propia.
