---
id: 2026-1024-buyvm-slices-modelo-dedicado-fraccionado-con-cpu-fair-share
type: atom
certainty: solid
sources: [sources/2026-10-23-buyvm-kvm-slices.md]
links: ["[[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]", "[[2026-1024-hostbrr-vps-comparte-cpu-y-vds-dedicada-24-7]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]"]
---
## Claim
BuyVM vende sus "Dedicated KVM Slice Servers" con el lema "All the performance benefits of a dedicated server, minus the costs and complexity", pero la especificación de CPU es **"Fair Share CPU Usage"** en los slices 512, 1024 y 2048 y **solo pasa a "Dedicated CPU Usage" en el slice 4096**. Todos los slices declaran "**1 Core** @ 3.50+ GHz", "**Pure SSD Storage**" y la página afirma "Absoutely no overselling means no \"noisy\" neighbor issues that plague so many of our competitors".

## Why It Matters
Es el eslabón que al vault le faltaba: **el "dedicado barato" existe, pero con una bisagra de CPU compartida en tres de sus cuatro escalones**. El criterio que el vault tenía ([[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]) era binario — compartido para desarrollo y pruebas, dedicado para carga sostenida — y BuyVM añade una categoría intermedia que ese binario no captura: un plan **vendido como dedicado** cuyo core es fair-share. El mismo patrón ya se había detectado en HostBrr, donde "A standard VPS shares CPU cores with fair usage" y la CPU dedicada 24/7 es un producto aparte, el VDS ([[2026-1024-hostbrr-vps-comparte-cpu-y-vds-dedicada-24-7]]): **tres proveedores del eje barato (Hetzner, HostBrr, BuyVM) ponen "dedicated" en el nombre y "fair share" en la ficha técnica**, lo que convierte la etiqueta en un término que hay que verificar plan por plan. Para MyOwnClone eso significa que el precio de un "dedicado" barato no compra aislamiento de CPU por debajo del slice 4096, lo que encaja con un despliegue vivo que crece por escalones ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]).

## [FRICTION]
> [[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]] afirma que los servidores dedicados de Hetzner "asignan vCPU dedicadas al proyecto, con rendimiento no compartido" frente a los planos compartidos con "vecinos", y de ahí se deriva el criterio de que "dedicado" significa CPU no compartida.
> La página de BuyVM usa la palabra **"Dedicated"** en el nombre del producto y en el copy ("Dedicated KVM Slice Servers", "All the performance benefits of a dedicated server"), y afirma **"Absolutely no overselling"**, pero su propia tabla de specs especifica **"Fair Share CPU Usage"** en 3 de los 4 slices. Ambas cosas no pueden ser literalmente ciertas a la vez: o "dedicated" en BuyVM significa "hardware propio fraccionado" y no "CPU dedicada", o el claim de "no overselling" es marketing y el fair-share sigue siendo CPU compartida. Marcado para juicio humano, no auto-resuelto: la lectura conservadora (fair-share hasta el 4096 inclusive) es la que sostiene la tabla de specs, y el nombre de producto no debe usarse como evidencia de aislamiento.
