---
id: 2026-1024-evoxt-os-windows-rdp-y-linux
type: atom
certainty: solid
sources: [sources/2026-10-23-evoxt-vps-pricing.md]
links: ["[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]", "[[2026-1024-evoxt-escalera-de-precios-nueve-planes]]", "[[2026-1024-evoxt-apps-un-clic-catalogo-y-stack-de-lamp]]", "[[2026-1024-evoxt-plan-de-entrada-vm-0-5-a-2-99-dolar]]"]
---

## Claim
Evoxt declara una selección de sistemas operativos que va *"from Windows RDP all the way to Linux VPS"*, con los logos de **Windows, Ubuntu, Debian, CentOS, AlmaLinux, Rocky Linux, Fedora y SUSE**. La página no publica la lista de versiones ni el coste de las licencias de Windows.

## Why It Matters
La distribución importa más que el proveedor cuando el servicio es un nginx autoalojado: el despliegue vivo de [[myownclone]] corre `nginx/1.28.3 (Ubuntu)` ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]) — Ubuntu está en la lista, así que una migración a este proveedor no exige cambio de sistema operativo ni recertificación del entorno. Y el dato de Windows RDP con licencia no publicada introduce una partida de coste no cuantificada que hoy no existe en el cálculo del vault: el plan más barato ($2.99, [[2026-1024-evoxt-plan-de-entrada-vm-0-5-a-2-99-dolar]]) solo es utilizable por el stack Linux que el producto ya tiene ([[2026-1024-evoxt-escalera-de-precios-nueve-planes]]), mientras que cualquier alternativa Windows entra con un coste oculto.

## Nota de verificación
Nombres de SO transcritos de los logos de la página. La captura **no** publica: versiones (Ubuntu 22.04 vs 24.04),kernel, si Rocky/Alma son deprecated, coste de la licencia Windows RDP, ni si las imágenes son oficiales o propias.
