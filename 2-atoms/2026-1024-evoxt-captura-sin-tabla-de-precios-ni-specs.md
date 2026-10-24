---
id: 2026-1024-evoxt-captura-sin-tabla-de-precios-ni-specs
type: atom
certainty: tentative
sources: [sources/2026-10-23-evoxt-vms.md, sources/2026-10-23-evoxt-vps-pricing.md]
links: ["[[2026-1023-lzt-captura-parcial-sin-precios-ni-stock]]", "[[2026-1024-evoxt-precios-transparentes-2-99-sin-cargos-ocultos]]", "[[2026-1024-evoxt-plan-de-entrada-vm-0-5-a-2-99-dolar]]", "[[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]"]
---

## Claim
La **home de Evoxt** (`sources/2026-10-23-evoxt-vms.md`) es una captura de marketing sin datos tabulares: el único importe visible es la mención a **$2.99** en el párrafo de "Transparent Pricing", y los bloques de **"VM-1 Plan CPU / Memory / Disk Benchmark"** aparecen **sin cifras** (solo el encabezado y la nota "these benchmark scores are for reference only and may differ slightly depending on the system and configurations"). No hay vCPU, RAM, disco, ancho de banda incluido, SLA en texto ni periodicidad. La tabla de planes con specs solo existe en la **página de precios** (`sources/2026-10-23-evoxt-vps-pricing.md`), que es una captura distinta: [[2026-1024-evoxt-plan-de-entrada-vm-0-5-a-2-99-dolar]].

## Why It Matters
Es la misma limitación estructural que el vault ya registró con la captura parcial de LZT ([[2026-1023-lzt-captura-parcial-sin-precios-ni-stock]]) y marca el techo de lo que la home puede sostener por sí sola: **Evoxt no era comparable en coste con Hetzner sobre la base de esta captura**, porque en Hetzner la calculadora daba un plan concreto y verificable —CPX02, 1 vCPU AMD, €5.99/mes o €0.0096/h, excl. VAT ([[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]])— y aquí solo había un número suelto en un párrafo de marketing. La consecuencia metodológica es reutilizable: **una home de proveedor no es una fuente de precios**; el precio hay que sacarlo de la calculadora o de la tabla de planes. En este caso la tabla llegó desde la segunda captura, y al hacerlo quedó claro que el $2.99 corresponde al plan más pequeño (512 MB), no al "VM-1" que la home usa como ejemplo de benchmark.

## Nota de verificación
La ausencia de precios y benchmarks es una observación sobre **lo capturado en la home**, no una afirmación de que Evoxt no los publique — la página de precios sí los publica. Ninguna spec, plan o cifra de benchmark se ha inferido aquí.
