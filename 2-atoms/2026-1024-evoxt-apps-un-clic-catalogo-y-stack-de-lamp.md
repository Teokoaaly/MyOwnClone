---
id: 2026-1024-evoxt-apps-un-clic-catalogo-y-stack-de-lamp
type: atom
certainty: solid
sources: [sources/2026-10-23-evoxt-vms.md]
links: ["[[2026-1023-hetzner-apps-un-clic-gratuitas-incluidas]]", "[[2026-1024-evoxt-kvm-aislamiento-y-hardware-enterprise]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]", "[[2026-1022-myclone-stack-tecnologico]]"]
---

## Claim
Evoxt publica un catálogo de **17 apps de un clic** (la captura muestra 17 tarjetas): WordPress con LiteSpeed, Magento, Drupal, LAMP (Linux, Apache, MySQL & PHP), LEMP (Linux, NGINX, MySQL & PHP), OpenLiteSpeed, Joomla, PrestaShop, Chevereto (hosting de imágenes autoalojado), Nextcloud, Docker, GitLab, CyberPanel, cPanel, VestaCP, HestiaCP y Minecraft. La home ofrece además un enlace a la **lista completa de aplicaciones** ("Visit here for full 1-click apps list") y un apartado de guías organizado en tres categorías: **WordPress Guides, 1-Click Apps Guides y Evoxt Related Guides**, con las 5 guías más populares destacadas (*Why choose Evoxt?*, *How to run Android Emulator on VPS*, *How to use Evoxt's VNC*, *Disable IPv6 on Windows Server*, *How to increase Windows VPS size after VPS plan upgrade*).

## Why It Matters
El solapamiento con el catálogo de Hetzner que el vault ya registró (Coolify, Docker CE, GitLab CE, Grafana, Nextcloud, Owncast, WordPress…) es parcial pero revelador: **Evoxt se posiciona en hosting/panel, no en PaaS de desarrollo** — ofrece stacks LAMP/LEMP y paneles (cPanel, VestaCP, HestiaCP, CyberPanel) que Hetzner no lista, y no ofrece Coolify ni Prometheus/Grafana. Para [[myownclone]], que corre Next.js detrás de nginx en un VPS propio ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]), el stack relevante es Docker + LEMP, no el catálogo de CMS: la utilidad real de esta lista es como **alternativa de proveedor con despliegue en un clic para un cliente que llega sin perfil técnico** (uno de los testimonios de la página es exactamente eso: "no tenía conocimientos de programación y lo monté todo fácilmente"), y como catálogo del stack de hosting tradicional que el vault no tenía registrado. Las guías destacadas son la otra cara: el proveedor compite **también por documentación**, con un "Android Emulator on VPS" entre las 5 más populares — señal del perfil de cliente al que apunta (self-hosting, bots, emulación).

## Nota de verificación
La captura **no** publica requisitos mínimos de RAM/CPU por app, versiones soportadas, ni si Windows se factura aparte. La lista de apps está transcrita de las tarjetas visibles: la captura muestra 17 tarjetas más el enlace a la lista completa, que podría contener más. La lista de sistemas operativos (AlmaLinux, Ubuntu, Debian, CentOS, Windows) de la home ya está atómizada aparte desde la página de precios en [[2026-1024-evoxt-os-windows-rdp-y-linux]].
