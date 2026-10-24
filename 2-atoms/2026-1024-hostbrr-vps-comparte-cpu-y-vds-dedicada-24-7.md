---
id: 2026-1024-hostbrr-vps-comparte-cpu-y-vds-dedicada-24-7
type: atom
certainty: solid
sources: [sources/2026-10-23-hostbrr-vps-pricing.md]
links: ["[[2026-1024-hostbrr-escalera-de-precios-vps-2-00-3-50-y-3-90]]", "[[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]", "[[2026-1024-hostbrr-value-2gb-1-vcpu-2gb-ram-25-gb-storage]]", "[[2026-1024-hostbrr-categorias-del-configurador-y-escalera-de-ram-sin-precios]]"]
---

## Claim
La FAQ de la página de precios de HostBrr define la diferencia entre las dos familias de recursos: **"Both utilize KVM virtualization for fully dedicated RAM and storage. A standard VPS shares CPU cores with fair usage. A VDS (Virtual Dedicated Server) provides fully dedicated CPU cores for 100% processing utilization, 24/7."** Es decir: **un VPS de HostBrr no tiene vCPU dedicada** (sí RAM y disco dedicados), y la CPU dedicada 24/7 es un producto aparte, el **"Performance VDS"**, accesible en el cuarto modo del configurador ("Dedicated Resources").

## Why It Matters
Es la corrección de fondo que el vault necesitaba: el criterio "compartido vs dedicado" que venía de Hetzner ([[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]) es aquí **más estricto** — un VPS de HostBrr es un nodo KVM con RAM y almacenamiento dedicados pero **CPU compartida con fair use**, o sea exactamente lo que en Hetzner se llamaría un plan compartido. Para el stack de MyOwnClone (nginx + Postgres + Redis + SSE en streaming) eso significa que el vCPU de 1 core del plan de €2 ([[2026-1024-hostbrr-value-2gb-1-vcpu-2gb-ram-25-gb-storage]]) es un recurso compartido con vecinos desconocidos: sirve para validar la hipótesis de carga en beta, no para sostener tenants de producción con SLA. La palanca de salida ya está identificada: el VDS con CPU dedicada 24/7, cuyo precio la captura **no publica**.

## [FRICTION]
> [[2026-1024-hostbrr-escalera-de-precios-vps-2-00-3-50-y-3-90]] (escrita hace unas horas, captura de la home) afirma que el Value VPS de HostBrr ofrece "**Scalable virtual private servers featuring dedicated compute resources** and root access" y usa esa frase como argumento para leer el salto a "nodo enterprise KVM con vCPU dedicado" por **+€1,90 (×1,95)** frente al ×6,70 de Hetzner.
> Esta página de precios del **mismo proveedor** dice lo contrario para el VPS estándar: "**A standard VPS shares CPU cores with fair usage**". Ambas no pueden ser completamente correctas: o el "dedicated compute resources" de la home significaba solo "recursos de cómputo dedicados" en sentido comercial (marketing), o el Value VPS de €2 sí tiene vCPU dedicada y la FAQ de la página de precios es incorrecta. Marcado para juicio humano, no auto-resuelto: la lectura conservadora (CPU compartida salvo VDS) es la que la página de precios sostiene explícitamente, pero la home sigue diciendo "dedicated compute resources" y el vault no puede descartar que el término sea ambiguo dentro del propio proveedor.
