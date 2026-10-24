---
id: 2026-1024-extravm-disco-proporcional-15-gb-nvme-por-gb-de-ram
type: atom
certainty: solid
sources: [sources/2026-10-23-extravm-vps-pricing.md]
links: ["[[2026-1024-extravm-escalera-de-precios-14-planes-de-4-50-a-192]]", "[[2026-1024-lowendbox-serverhost-leb-1gb-kvm-11-dolares-al-ano]]", "[[2026-1024-hostbrr-value-2gb-1-vcpu-2gb-ram-25-gb-storage]]"]
---

## Claim
En los 14 planes de ExtraVM el almacenamiento es **exactamente 15 GB NVMe por cada GB de RAM**, sin excepción: 1 GB → 15 GB, 2 → 30, 3 → 45, 4 → 60, 5 → 75, 6 → 90, 8 → 120, 10 → 150, 12 → 180, 16 → 240, 24 → 360, 32 → 480, 48 → 720 y 64 → 960 GB. La página añade que **todo el almacenamiento es NVMe local espejado** ("All servers utilize local mirrored NVMe flash storage"). La CPU no sigue esa regla: los cores van de 1 a 10 con saltos (1, 1, 2, 2, 3, 4, 4, 6, 6, 6, 6, 8, 10, 10), es decir **10 cores para 64 GB** y 6 cores para planes de 10 a 24 GB.

## Why It Matters
Una relación disco/RAM perfectamente lineal significa que **el dimensionamiento del stack es predecible a partir de la RAM**: el mínimo del vault (1 GB → 15 GB de NVMe) y el máximo (64 GB → 960 GB) no dejan huecos de capacidad, lo que evita el problema de otros catálogos donde el disco se queda corto en un escalón intermedio. También fija un rasgo de diseño útil para MyOwnClone: **mucho disco NVMe local por poco dinero**, útil para el pipeline de ingesta/scraping y la biblioteca de conocimiento (que guarda y vectoriza material del cliente) sin pagar almacenamiento de bloque aparte, algo que en el vault no aparece hoy como partida separada ([[2026-1022-costes-por-categoria-tenant]]). El contraste con el resto del vault: la oferta LowEndBox de 1 GB da 15 GB de storage pero a precio **anual** ([[2026-1024-lowendbox-serverhost-leb-1gb-kvm-11-dolares-al-ano]]), y HostBrr rompe la linealidad (2 GB → 25 GB) y añade planes de storage separados ([[2026-1024-hostbrr-value-2gb-1-vcpu-2gb-ram-25-gb-storage]]).

## Nota de verificación
La captura no publica IOPS, ancho de banda de disco, modelo exacto de NVMe, ni si el "local mirrored" implica RAID1 y cuál es su tolerancia a fallo.
