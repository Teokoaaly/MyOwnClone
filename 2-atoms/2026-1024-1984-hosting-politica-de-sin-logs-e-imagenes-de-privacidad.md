---
id: 2026-1024-1984-hosting-politica-de-sin-logs-e-imagenes-de-privacidad
type: atom
certainty: solid
sources: [sources/2026-10-24-1984-hosting-vps.md]
links: ["[[2026-1024-1984-hosting-certificacion-iso-27001]]", "[[2026-1024-1984-hosting-fundada-en-2006-con-105k-clientes-y-etica-independent]]", "[[2026-1024-skhron-tor-onion-facturacion-panel-y-pagos]]", "[[2026-1024-1984-hosting-vps-entry-9-66-1-cpu-1gb-y-25gb-nvme]]"]
---

## Claim
La lista de funcionalidades del VPS de 1984 Hosting incluye **"No Logging Policy"**, **"Privacy Images (Wireguard, etc)"**, **"VNC Console Access"**, **"Root Access"**, **"NVMe SSD Storage"**, **"Instant Setup"** y **"DDoS Protection"**. Es decir: el proveedor ofrece **imágenes de sistema preconfiguradas con WireGuard** y una declaración de no registrar logs, ambas como característica de producto, no como nota legal.

## Why It Matters
Es la postura de privacidad **operativa** del vault en su versión más simple: en lugar de un panel `.onion` como Skhron ([[2026-1024-skhron-tor-onion-facturacion-panel-y-pagos]]) o de una cadena de pagos no custodia, 1984 ofrece "traffic goes through WireGuard" preinstalado. Para un producto como MyOwnClone, cuyo despliegue vivo es nginx + Postgres + Redis autoalojado ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]), el **root + consola VNC + imagen de WireGuard en el mismo plan de $9,66** ([[2026-1024-1984-hosting-vps-entry-9-66-1-cpu-1gb-y-25gb-nvme]]) es un bundle operativo compacto: recuperación en consola sin SSH y túnel cifrado sin configurar.

Lo que la captura **no** permite precisar es el alcance de "No Logging Policy": no dice si aplica a los logs del sistema, a los de red, a los del panel de control ni a las métricas de facturación — y no publica el texto de la política. En paralelo, la página combina esa declaración con una certificación ISO 27001 ([[2026-1024-1984-hosting-certificacion-iso-27001]]) y con un posicionamiento ético de freedom of speech ([[2026-1024-1984-hosting-fundada-en-2006-con-105k-clientes-y-etica-independent]]): **tres señales de privacidad en una sola página, ninguna con documento adjunto salvo el certificado**.

## Nota de verificación
La captura no publica el texto de la política de no-logs, ni el alcance (sistema, red, panel, facturación), ni los términos que la limitan, ni los detalles de las "Privacy Images" más allá de la mención de WireGuard.
