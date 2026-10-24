---
id: 2026-1024-evoxt-dos-precios-distintos-para-el-mismo-plan
type: atom
certainty: solid
sources: [sources/2026-10-23-evoxt-vps-pricing.md]
links: ["[[2026-1024-evoxt-escalera-de-precios-nueve-planes]]", "[[2026-1024-evoxt-plan-de-entrada-vm-0-5-a-2-99-dolar]]", "[[2026-1024-evoxt-precios-transparentes-2-99-sin-cargos-ocultos]]"]
---

## Claim
La página de precios de Evoxt publica **dos precios distintos para el mismo plan** en dos bloques de la misma página. En la tabla "Plans": **VM-1 $5.99, VM-2 $11.99, VM-4 $23.99, VM-8 $47.99**. En la tabla "Benchmark Score": **VM-1 $9.99, VM-2 $19.99, VM-4 $39.99, VM-8 $79.99** — con specs idénticas en ambos bloques (VM-1: 1 vCore / 2 GB / 20 GB; VM-8: 8 vCore / 16 GB / 80 GB). Solo **VM-0.75 ($4.99)** coincide en las dos tablas. La tabla de benchmark excluye **VM-0.5, VM-1.5, VM-3 y VM-6**.

## Why It Matters
Contradice frontalmente la promesa de "precios transparentes" del propio proveedor — *"Si pides un plan de $2.99, pagarás $2.99. No cobramos cargos extra por ancho de banda ni cargos por CPU burst"* ([[2026-1024-evoxt-precios-transparentes-2-99-sin-cargos-ocultos]]): la transparencia falla no por cargos ocultos sino por **la propia página dando dos cifras distintas para el mismo SKU**. Para el vault esto es operativo, no semántico: cualquier comparación de coste que se haga con la tabla de benchmark (la que incluye los scores) arrastrará un precio inflado de hasta ×1.67 (VM-8: $47.99 vs $79.99) frente al precio realmente anunciado en el catálogo. Es una razón práctica para usar siempre la tabla "Plans" como referencia y para no tratar la segunda tabla como lista de precios.

## [FRICTION]
> [[2026-1024-evoxt-precios-transparentes-2-99-sin-cargos-ocultos]] afirma que Evoxt declara **precios transparentes** y que "el precio publicado es el precio facturado, sin cargos variables ocultos".
> Este átomo presiona esa creencia con evidencia de la misma página de precios del proveedor: para 4 de los 5 planes comparables, el "precio publicado" aparece con dos valores incompatibles.
> Ambas no pueden ser completamente correctas: o la tabla de benchmark muestra precios de otra campaña/región/periodicidad (y entonces no es el precio del catálogo), o la transparencia solo se refiere a no añadir cargos, no a que el catálogo tenga un precio único. Marcado para juicio humano, no auto-resuelto: la captura no explica la discrepancia.

## Nota de verificación
Los dos juegos de precios están transcritos literalmente de la captura. No se infiere cuál es el vigente: la página no indica periodicidad, región ni si una de las dos tablas corresponde a otro contexto.
