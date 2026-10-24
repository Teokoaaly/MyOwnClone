---
id: 2026-1024-evoxt-ipv6-y-red-privada-sin-cargos
type: atom
certainty: solid
sources: [sources/2026-10-23-evoxt-vms.md, sources/2026-10-23-evoxt-vps-pricing.md]
links: ["[[2026-1023-hetzner-ipv4-primario-incluido-o-costo-cero]]", "[[2026-1024-evoxt-precios-transparentes-2-99-sin-cargos-ocultos]]", "[[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]", "[[2026-1024-evoxt-plan-de-entrada-vm-0-5-a-2-99-dolar]]"]
---

## Claim
La sección de funciones adicionales de la home de Evoxt declara dos capacidades de red internas que no aparecen en la página de precios: **"IPv6 Ready — Future proof, all VMs have an IPv6 address included"** (todas las VMs incluyen dirección IPv6) y **"Private IP Address — Build your infrastructure on Evoxt. Communicate between VMs without any extra bandwidth charges"** (comunicación entre VMs por IP privada **sin cargos extra de ancho de banda**).

## Why It Matters
Son las dos partidas que hacen que la infraestructura multi-VM no dispare la factura: la red privada sin cargos de egreso es la diferencia estructural frente a Hetzner, donde el egreso tiene recargo explícito de **€1,00/TB extra en la UE** ([[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]), y el IPv6 incluido de serie es un plus frente al conmutador "IPv6 only / Primary IPv4" de la calculadora de Hetzner, donde el IPv4 primario aparece a €0,00 pero con lectura tentativa ([[2026-1023-hetzner-ipv4-primario-incluido-o-costo-cero]]). Para [[myownclone]], que hoy sirve respuestas de clon y streaming SSE desde un único nginx autoalojado, la comunicación entre VMs sin coste es lo que permitiría separar ingest, web y workers sin introducir una partida de egreso nueva.

## Nota de verificación
La captura **no** publica el número de IPs privadas por VM, el prefijo IPv6 asignado, ni si la red privada tiene límite de ancho de banda. La ausencia de cargos es la formulación literal de la home ("without any extra bandwidth charges"), sin desglose. La gestión de IPs flotantes y la reasignación entre servidores ya está atómizada aparte en [[2026-1024-evoxt-ip-management-floating-ip-y-reasignacion]].

## [NOTA 2026-10-24]
La página de precios (`sources/2026-10-23-evoxt-vps-pricing.md`) confirma la gestión de IP con la misma fórmula —*"Easily swap and reassign IP address between servers... Order additional Floating IP Address"*— y la sitúa como **una de las siete funciones de gestión del panel** (Monitoring, IP Management, Firewall, Cloning, Sub Accounts, Backups, VNC), **sin línea de precio propia**: el catálogo solo publica el precio del plan (desde $2.99 en [[2026-1024-evoxt-plan-de-entrada-vm-0-5-a-2-99-dolar]]) y ninguna partida por IP. La página de precios **tampoco** publica el ancho de banda incluido, de modo que el coste real de un pool de IPs (necesario para el patrón una-IP-por-cuenta que exige el flujo de verificación SMS) queda sin cuantificar.
