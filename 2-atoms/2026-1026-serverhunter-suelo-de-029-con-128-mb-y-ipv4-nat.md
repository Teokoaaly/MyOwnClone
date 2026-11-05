---
id: 2026-1026-serverhunter-suelo-de-029-con-128-mb-y-ipv4-nat
type: atom
certainty: solid
sources: [sources/2026-10-25-serverhunter-cheap-vps.md]
links: ["[[2026-1024-lowendbox-vps-anuales-de-10-a-11-dolares-no-mensuales]]", "[[2026-1024-lowendbox-cuarto-escalon-de-precio-10-dolares-al-ano]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]"]
---

## Claim
El precio más bajo visible en la tabla de ServerHunter es **$ 0.29 USD**, y aparece en **cinco filas distintas**: cuatro planes `NAT-128` de Gullo's Hosting (**FR, CA, DE, FIN**) con **128 MB de RAM, 1 core y 3 GB** (SSD en FR, HDD en CA/DE/FIN), y `NanoVPS-II 384 Low-Cost Special US` de Centerfield Ltd con **384 MB, 1 core Xeon Gold 6138 y NVMe 8 GB**. Todos llevan la etiqueta **"NAT IPv4"** y "Free setup". Las cuatro filas NAT-128 son **facturación anual**; la de Centerfield aparece con "Annual billing" y, además, la **misma oferta reaparece a $ 0.33** sin etiqueta de facturación anual. La celda de precio **no imprime periodo** (la columna se titula simplemente "Price" y la celda dice "$ 0.29 USD"); lo que sostiene la lectura mensual es que el panel de ordenación incluye la clave **"Monthly price"**, junto a "Setup fee" y a las claves de precio por unidad.

## Why It Matters
El suelo de hosting medido en el vault era de **$10–11,28/año** ([[2026-1024-lowendbox-vps-anuales-de-10-a-11-dolares-no-mensuales]] y [[2026-1024-lowendbox-cuarto-escalon-de-precio-10-dolares-al-ano]]), es decir ~$0,83–0,88/mes. Si $0,29 es un precio **mensual** —lo que sostiene la clave de ordenación "Monthly price" del panel, no un "/mes" impreso en la celda—, el suelo baja a **$3,48/año**—un 65 % por debajo del suelo de LowEndBox— y con él baja la escala entera, muy por debajo del umbral de ≤ €4/mes que el vault venía usando como techo de referencia ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]). Pero **la capacidad es symbolicamente distinta**: 128 MB de RAM y 3 GB de disco no alojan el stack Postgres + Redis + Flask/Next.js del despliegue vivo; y el precio se paga en la restricción que ya mide el thread —dirección IPv4 no dedicada (NAT) y stock no confirmado (tres de las cinco filas a $0,29 están en "Stock unknown")—. Es decir: **el suelo de precio real del mercado está en un producto que el producto no puede usar**.

## [FRICTION]
> [[2026-1024-lowendbox-vps-anuales-de-10-a-11-dolares-no-mensuales]] afirma que "el suelo real de hosting medido es de **~$120/año**, no $12/año" y en su propio [FRICTION] reconoce que esa cifra **no encaja** con los precios publicados de las listas hermanas.
> ServerHunter publica precios **anuales** implícitos de **$3,48/año** ($0,29 × 12) para planes de 128 MB con IPv4 NAT. Si el suelo del vault era $10–11,28/año, y luego se corrigió a ~$120/año, esta captura añade un tercer valor: **$3,48/año**, por debajo de ambos. Y la premisa de que $0,29 es mensual no está impresa en la celda: la sostiene la clave de ordenación **"Monthly price"** del panel de filtros, no un "/mes" junto al importe.
> Las tres cifras no pueden ser a la vez el suelo del mercado: o la de $120/año es un error de escala que arrastra al resto del thread, o esta fuente mide otra cosa (NAT micro-VPS sin SLA, sin stock verificable y con specs de 128 MB, que no son comparables con un KVM de 1 GB), o el suelo real del mercado está donde dice ServerHunter y el thread compara peras con manzanas. Marcado para juicio humano, no auto-resuelto: la captura **no publica el importe anual facturado**, solo el precio de una oferta etiquetada "Annual billing" cuya celda no dice "/mes".

## Nota de verificación
Los cinco $0,29 y sus specs (128 MB/384 MB, 1 core, 3 GB/8 GB, NAT IPv4, Free setup, "Stock unknown" en tres filas) están transcritos literalmente. El equivalente **$3,48/año es cálculo del átomo** (0,29 × 12), no una cifra de la fuente; la fuente no publica el total anual ni la tarifa de renovación.
