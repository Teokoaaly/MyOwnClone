---
id: 2026-1024-flokinet-ram-ampliada-para-picos-pero-no-es-recurso
type: atom
certainty: solid
sources: [sources/2026-10-24-flokinet-vps-pricing.md]
links: ["[[2026-1024-flokinet-escalera-de-precios-siete-planes]]", "[[2026-1024-skhron-vcpu-fraccional-garantizado-y-bursts-hasta-el-nucleo]]", "[[2026-1024-evoxt-precios-transparentes-2-99-sin-cargos-ocultos]]", "[[2026-1024-flokinet-trafico-por-plan-y-direccion-no-publicada]]"]
---

## Claim
FlokiNET declara explícitamente un **margen de RAM por encima de lo contratado**: *"Our VPS service will limit your RAM to a slightly higher value than what you have purchased, to accomodate peaks, though this should not be considered an available resource."* Es decir, el límite real del contenedor es **ligeramente superior** a los GB comprados (1 GB, 2 GB, 4 GB, 6 GB, 8 GB, 10 GB, 12 GB según el plan), pero ese excedente existe solo para absorber picos y **el proveedor lo descarta explícitamente como recurso**.

## Why It Matters
Es la versión más cuidadosa del patrón "burst" que el vault ya tiene documentado en Skhron, donde el 0,06 vCPU garantizado bursting a 1 se presenta como **techo, no como garantía** ([[2026-1024-skhron-vcpu-fraccional-garantizado-y-bursts-hasta-el-nucleo]]). FlokiNET invierte el signo: **el margen existe, se declara, y se invalida por contrato** ("should not be considered an available resource"), lo que es más honesto que no decirlo y también más inútil — un margen que el proveedor cuenta como no disponible no se puede cotizar ni presupuestar. La consecuencia para el dimensionamiento del stack es directa: **la RAM efectiva garantizada es la comprada**, y para Postgres + Redis + Flask/Next.js ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]) el umbral sigue siendo 2 GB reales ([[2026-1024-hostbrr-value-2gb-1-vcpu-2gb-ram-25-gb-storage]]), que en FlokiNET es el **VPS II a €14,99**, no el de entrada. Es también un recordatorio de la regla del thread: **el precio de catálogo no es la especificación contratada** —aquí la propia página lo dice en su propio eje.

## Nota de verificación
"slightly higher" no se cuantifica: la captura **no** publica cuántos MB o GB de más se asignan por plan. El texto es una declaración de política de asignación, no una ficha técnica, y no se acompaña de SLA que la respalde.
