---
id: 2026-1024-evoxt-firewall-desde-el-panel-sin-conectar
type: atom
certainty: retired
sources: [sources/2026-10-23-evoxt-vps-pricing.md]
links: ["[[2026-1023-hetzner-firewalls-estatales-sin-coste-adicional]]", "[[2026-1022-ausencia-csp-xss-sin-mitigacion]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]"]
---

## [RETIRED 2026-10-24]
Superseded por el átomo canónico del mismo proveedor (misma afirmación, capturada de la home en `sources/2026-10-23-evoxt-vms.md`). Conservado por trazabilidad, no cuenta como átomo vigente.

## Claim
Evoxt declara que su firewall se configura **sin necesidad de conectarse a la máquina virtual**: *"Easily secure your virtual machine with Evoxt's firewall system. Set firewall rules without even needing to connect to your virtual machine"*. El panel de control agrupa además **Monitoring, IP Management, Firewall, Cloning, Sub Accounts, Backups y VNC** como las siete funciones de gestión declaradas.

## Why It Matters
Es el mismo patrón de **control de red como capa de mitigación sin tocar código** que el vault ya registró para Hetzner, donde los firewalls stateful se incluían "sin costes adicionales" ([[2026-1023-hetzner-firewalls-estatales-sin-coste-adicional]]). La diferencia relevante para [[myownclone]] es de orden de aplicación: el despliegue vivo es un nginx autoalojado ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]) que el vault ya registró **sin cabeceras de seguridad ni CSP** ([[2026-1022-ausencia-csp-xss-sin-mitigacion]]); un firewall de plataforma que se configura desde el panel de control, sin SSH y sin tocar la máquina, es la forma más barata de endurecer el perímetro mientras el código sigue igual — y de hacerlos desde un panel en lugar de con una sesión root.

## Nota de verificación
Texto transcrito literalmente. La captura **no** publica: si el firewall es stateful o stateless, número de reglas, protocolos soportados, si hay coste adicional por regla, ni el modelo (iptables/nftables) — nada de eso se infiere aquí.
