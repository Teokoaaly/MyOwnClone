---
id: 2026-1026-serverhunter-precio-por-nucleo-y-por-gb-como-claves-de-ordenacion
type: atom
certainty: solid
sources: [sources/2026-10-25-serverhunter-cheap-vps.md]
links: ["[[2026-1024-extravm-disco-proporcional-15-gb-nvme-por-gb-de-ram]]", "[[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]", "[[2026-1026-serverhunter-88559-servidores-de-971-proveedores]]"]
---

## Claim
La lista de filtros y claves de ordenación de ServerHunter publica **unidades de precio normalizadas por recurso**, no solo precio absoluto: **"Price per CPU Core"**, **"Price per CPU Speed"**, **"Price per CPU Benchmark"**, **"Price per GB of Memory"**, **"Price per TB of Storage"**, **"Price per TB of HDD"** y **"Price per TB of SSD"**, además de "Monthly price" y "Setup fee" como claves de precio bruto. En paralelo aparecen como filtros la **virtualization type**, el **uplink speed**, el **traffic** y la **cantidad de CPU/memoria/disco**. El orden por defecto de la captura es "Lowest price" y la tabla visible **no muestra ninguna de las columnas normalizadas**: solo Nombre, Procesador, Producto, Memoria, Storage, Stock y Precio.

## Why It Matters
Es la **misma normalización que el thread de hosting viene exigiendo** —el thread propone comparar "TB de salida equivalentes" y no "TB incluidos" ([[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]])— pero resuelta por el agregador y no por el vault: ServerHunter ya ofrece el precio por GB de RAM y por TB de SSD como criterio de orden, y el resultado visible es que **el plan con mejor $/GB no es el más barato**. Es el caso de ExtraVM con su regla de **15 GB NVMe por cada GB de RAM** ([[2026-1024-extravm-disco-proporcional-15-gb-nvme-por-gb-de-ram]]): dos proveedores pueden tener el mismo $/mes y muy distinto $/GB, y el orden por precio absoluto no lo revela.

El límite del dato es igualmente importante: **la captura no trae valores de esas columnas**, solo la lista de claves. Es un **instrumento declarado, no medido** — el vault puede usar la existencia de la normalización como criterio de hipótesis (el $/GB ordena distinto que el $/mes) pero no puede citar cifras de ella sin una segunda captura con la columna visible.

## Nota de verificación
Los nombres de las claves están transcritos literalmente de la línea de filtros de la captura. La fuente **no publica los valores** de esas columnas ni un ejemplo de ordenación por ellas; ninguna cifra de este átomo procede de ellas. La inferencia "el $/GB ordena distinto que el $/mes" es una lectura del átomo, apoyada en el caso ya medido de ExtraVM, no una frase de la fuente.
