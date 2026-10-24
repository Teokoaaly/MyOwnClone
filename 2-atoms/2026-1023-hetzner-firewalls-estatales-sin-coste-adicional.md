---
id: 2026-1023-hetzner-firewalls-estatales-sin-coste-adicional
type: atom
certainty: solid
sources: [sources/2026-10-22-hetzner-cloud.md, sources/2026-10-23-evoxt-vms.md]
links: ["[[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]", "[[2026-1022-ausencia-csp-xss-sin-mitigacion]]", "[[2026-1022-live-verify-superficie-dns-reducida-a-dos-hosts]]"]
---

## Claim
La página afirma que los **firewalls stateful de Hetzner permiten asegurar la infraestructura "sin costes adicionales"**: bloquean tráfico entrante y saliente no deseado según reglas definidas y, una vez configurados, se pueden asignar a **tantos servidores cloud como se quiera**. Las **Networks** (red privada entre servidores, con topologías complejas) vienen igualmente incluidas en el conjunto "Everything you need, included".

## Why It Matters
Cierra el círculo de coste: los elementos que en otros proveedores son un extra —red privada, firewall, imágenes del sistema, API/CLI ([[2026-1023-hetzner-api-cli-e-integraciones-iac]])— aquí están **incluidos sin sobrecoste**, de modo que el precio base de €5,99/mes ([[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]) cubre una superficie de seguridad completa. Eso tiene lectura directa sobre los riesgos que el vault ya tiene documentados: sin cabeceras de seguridad y sin CSP ([[2026-1022-ausencia-csp-xss-sin-mitigacion]]), el control de red pasa a ser la capa de mitigación disponible sin tocar código. Y encaja con la superficie DNS medida, hoy reducida a dos hosts públicos ([[2026-1022-live-verify-superficie-dns-reducida-a-dos-hosts]]): un firewall stateful en la frontera del VPS es la forma de cerrar por reglas lo que el DNS ya cerró por ausencia.

## Nota de verificación
La captura no publica el número máximo de firewalls, el número de reglas por firewall, ni el precio de las redes privadas por encima de algún umbral. "Sin costes adicionales" es la formulación literal de la página, sin desglose.

## [NOTA 2026-10-24 — Evoxt]
Fuente: `sources/2026-10-23-evoxt-vms.md`. Contrapunto de granularidad: Evoxt describe su firewall como **"enterprise-level layer 3"** con "better DDoS protection with layer 3 firewall", y lo gestiona **sin necesidad de conectarse a la VM** ("set firewall rules without even needing to connect to your virtual machine"), con protección DDoS incluida como argumento. Frente al firewall stateful de Hetzner, la diferencia de modelo es de **capa**: L3 filtra paquetes y no cubre capa 7, que es donde quedan expuestos los endpoints HTTP del clon (ver [[2026-1024-evoxt-firewall-capa-3-sin-conexion-al-servidor]]). La ventaja operativa —reglas gestionadas desde el panel, no dentro del sistema— sí es real y comparable al "sin coste adicional" que este átomo documenta para Hetzner.
