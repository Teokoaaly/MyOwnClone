---
id: 2026-1024-evoxt-precios-transparentes-2-99-sin-cargos-ocultos
type: atom
certainty: solid
sources: [sources/2026-10-23-evoxt-vms.md, sources/2026-10-23-evoxt-vps-pricing.md]
links: ["[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1023-priceai-sponsors-vps-chinos-para-auto-hospedar-relay]]", "[[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]", "[[2026-1024-evoxt-backup-semanal-offsite-gratuito]]", "[[2026-1024-evoxt-plan-de-entrada-vm-0-5-a-2-99-dolar]]", "[[2026-1024-evoxt-dos-precios-distintos-para-el-mismo-plan]]"]
---

## Claim
Evoxt declara **precios transparentes** con la fórmula literal: *"Si pides un plan de $2.99, pagarás $2.99. No cobramos cargos extra por ancho de banda ni cargos por CPU burst"*. Es decir, el punto de entrada anunciado es de **$2.99** y el precio publicado es el precio facturado, sin cargos variables ocultos de egreso ni de bursting de CPU.

## Why It Matters
El vault tiene un presupuesto de referencia de **≤ €4/mes** para el VPS, y ya lo había usado como eje en dos direcciones: dentro de Hetzner el suelo es €5,99/mes ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]) y fuera los patrocinadores chinos de PriceAI prometen VPS de 2 vCPU a decenas de yuanes al año ([[2026-1023-priceai-sponsors-vps-chinos-para-auto-hospedar-relay]]). Evoxt es un tercer punto de comparación, y el más limpio metodológicamente de los tres porque **es la página del propio proveedor y no un sponsor pagando por aparecer**. La diferencia clave con Hetzner es el modelo de coste: allí el egreso es una partida con recargo explícito de **€1,00/TB extra en la UE** ([[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]), mientras que aquí se afirma que no hay cargos extra por ancho de banda ni por CPU burst — lo que, si se cumple, convierte el egreso en coste marginal cero para un producto que sirve respuestas de clon y streaming SSE.

## [FRICTION]
> [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]] afirma que **"ningún plan del catálogo de Hetzner Cloud cabe en un presupuesto de €4/mes"** y concluye que "el VPS de €4 tiene que venir de otro proveedor o de un modelo distinto".
> Este átomo presiona esa creencia en su conclusión operativa: si el precio de $2,99 de Evoxt se confirmara como plan real con specs utilizables, la segunda mitad de la conclusión ("de otro proveedor") se cumple y el objetivo de ≤ €4/mes **deja de ser una aspiración y pasa a tener un candidato de mercado**, con la ventaja de un precio declarado sin cargos variables.
> Ambas no pueden ser completamente correctas en su lectura completa: o el suelo de €6/mes es una verdad que solo aplica al catálogo de Hetzner (y el vault no estaba comparando proveedores, como ya implica la nota de los patrocinadores chinos), o la cifra de $2,99 no es un plan realmente disponible. Marcado para juicio humano, no auto-resuelto: la fuente es la home comercial del propio proveedor, no una tabla de precios verificable, y no publica specs del plan de $2,99.

## Nota de verificación
La captura **no** muestra la tabla de precios: el texto de "Transparent Pricing" menciona $2.99 y el benchmark se refiere al "VM-1 Plan", pero no se afirma que VM-1 sea el plan de $2.99. Tampoco se publica moneda de facturación en euros, IVA, ni si el precio es por mes o por año.

## [NOTA 2026-10-24]
La página de precios del proveedor (`sources/2026-10-23-evoxt-vps-pricing.md`) sí publica la tabla que faltaba, y **aclara quién es el plan de $2.99: no es el VM-1, sino el VM-0.5** (1 vCore, 512 MB RAM, 5 GB Storage), mientras que el VM-1 cuesta **$5.99** (1 vCore, 2 GB RAM, 20 GB). La "transparencia" se confirma en la parte del catálogo, pero la propia página se contradice en el detalle: la tabla "Plans" y la tabla "Benchmark Score" dan **precios distintos para el mismo plan** (VM-1: $5.99 vs $9.99; VM-8: $47.99 vs $79.99) — ver [[2026-1024-evoxt-dos-precios-distintos-para-el-mismo-plan]]. El plan de $2.99 real es el de specs másallas ([[2026-1024-evoxt-plan-de-entrada-vm-0-5-a-2-99-dolar]]), insuficiente para el stack del producto.
