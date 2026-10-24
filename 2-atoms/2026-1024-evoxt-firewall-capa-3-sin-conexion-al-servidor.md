---
id: 2026-1024-evoxt-firewall-capa-3-sin-conexion-al-servidor
type: atom
certainty: solid
sources: [sources/2026-10-23-evoxt-vms.md, sources/2026-10-23-evoxt-vps-pricing.md]
links: ["[[2026-1023-hetzner-firewalls-estatales-sin-coste-adicional]]", "[[2026-1022-ausencia-csp-xss-sin-mitigacion]]", "[[2026-1024-evoxt-kvm-aislamiento-y-hardware-enterprise]]", "[[2026-1024-evoxt-plan-de-entrada-vm-0-5-a-2-99-dolar]]"]
---

## Claim
Evoxt ofrece un **firewall de nivel 3 (capa 3)**, descrito como "enterprise-level layer 3 security firewall", con la particularidad de que **las reglas se pueden configurar sin necesidad de conectarse a la máquina virtual** ("Set firewall rules without even needing to connect to your virtual machine") y con "better DDoS protection with layer 3 firewall".

## Why It Matters
Contrasta directamente con el modelo de Hetzner que el vault ya registra: allí los firewalls son **stateful y sin coste adicional**, aplicables a tantos servidores como se quiera ([[2026-1023-hetzner-firewalls-estatales-sin-coste-adicional]]); Evoxt habla de **capa 3**, es decir, filtrado de paquetes sin seguimiento de conexión, con protección DDoS como argumento de venta. La diferencia importa para el modelo de producto: sin cabeceras de seguridad y sin CSP ([[2026-1022-ausencia-csp-xss-sin-mitigacion]]), el control de red es la única capa de mitigación disponible sin tocar código — y un firewall de capa 3 no cubre attacks de capa 7 (inyección, XSS, abuso de API), que es donde quedan expuestos los endpoints del clon. Que las reglas se gestionen fuera de la VM sí es una ventaja operativa real para un despliegue en nginx autoalojado.

## Nota de verificación
La captura **no** publica el número máximo de reglas, ni el precio del firewall, ni el detalle de qué es exactamente "layer 3" en su implementación (¿reglas de iptables/nftables gestionadas en el host? ¿red NAT?). No se afirma ninguno de esos datos.

## [NOTA 2026-10-24]
La página de precios (`sources/2026-10-23-evoxt-vps-pricing.md`) repite la misma fórmula del firewall —*"Set firewall rules without even needing to connect to your virtual machine"*— y añade el dato que faltaba: el firewall es **una de las siete funciones de gestión** listadas en el panel (Monitoring, IP Management, Firewall, Cloning, Sub Accounts, Backups, VNC), sin coste ni precio separado publicado para él. Es decir, la gestión de reglas va de la mano del resto del panel y **no aparece como línea de gasto**: el único precio del catálogo es el del plan (desde $2.99 en [[2026-1024-evoxt-plan-de-entrada-vm-0-5-a-2-99-dolar]]). La captura tampoco publica en ningún punto ancho de banda incluido, lo que deja el egreso sin cuantificar — el punto ciego que el vault ya tiene medido en Hetzner a €1,00/TB extra.
