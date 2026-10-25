# Briefing — Refinery 2026-10-24 (FlokiNET)

## Qué entró

- Captura procesada: `0-raw/2026-10-24-flokinet-vps-pricing.md` (puntero) → fuente `sources/2026-10-24-flokinet-vps-pricing.md` (página de precios de flokinet.net/vps/)
- Atomos creados: **17** (todos `2026-1024-flokinet-*`)
- Atomos extendidos: **0** — no había átomo previo sobre FlokiNET en el vault
- Thread actualizado: **1** (`3-threads/escala-de-hosting-barato-y-el-limite-de-4-euros` — nueva §8.11, filas en la tabla comparativa, fricciones 24–26)
- Atoms retired: **0** · borrados: **0**
- Captura movida a `0-raw/archive/2026-10-25-2026-10-24-flokinet-vps-pricing.md`

## Los átomos

| Átomo | Idea |
|---|---|
| `flokinet-escalera-de-precios-siete-planes` | 7 planes KVM, **€7,99 → €73,90** (×9,25), CPU y RAM 1:1, 3→20 TB, `1 Gbit`, `1 IPv4 + /64 IPv6` |
| `flokinet-ubicaciones-offshore-ripe-e-isnic` | 4 ubicaciones activas (RO, IS, NL, FI), 3 "coming soon"; RIPE + ISNIC member, `.is` registrable por cualquiera, CPanel Authorized Partner, 10 años |
| `flokinet-ddos-1tbps-incluido-en-los-siete-planes` | `DDoS Protection (1Tbps+)` en las 7 filas, todas las capas OSI, sin add-on ni precio separado |
| `flokinet-sin-windows-ni-virtualizacion-anidada` | Linux/BSD solo; sin Windows VPS (Windows = dedicado, sin licencia) y **nested virtualization prohibida** |
| `flokinet-backup-de-snapshot-automatico-varias-veces-por-semana` | Snapshots automáticos incluidos, recuperables y creables a mano desde el panel |
| `flokinet-ram-ampliada-para-picos-pero-no-es-recurso` | El límite real de RAM puede superar lo comprado (margen de picos), **no es un entitlement** |
| `flokinet-aup-prohibe-chia-netscan-y-origenes-de-ddos` | Prohibidos spam, netscan, DDoS, malware, botnet, phishing, doxxing y **Chia mining**; VPN/proxy/blockchain permitidos |
| `flokinet-sin-acceso-del-proveedor-a-los-datos` | "No retain any ability to access your stored data"; **el cifrado pre-boot no aplica en contenedor virtual** |
| `flokinet-trafico-por-plan-y-direccion-no-publicada` | 3/6/9/12/15/18/20 TB, uplink `1 Gbit`; **la dirección del cómputo no se publica** ni el precio del extra |
| `flokinet-ipv4-adicional-hasta-cuatro-y-ipv6-en-todas-ubicaciones` | Hasta 4 IPv4 extra en el pedido; IPv6 en todas las ubicaciones; **precio del IPv4 extra no publicado** |
| `flokinet-upgrade-de-storage-exige-ajustar-particiones-a-mano` | CPU/RAM se actualizan con reboot; **particiones y filesystems se redimensionan a mano** (GParted, backup previo) |
| `flokinet-consola-ipmi-virtual-y-panel-novnc` | Virtual IPMI + noVNC: control con el servidor apagado, único camino para activar contraseña si se desplegó solo con clave SSH |
| `flokinet-sin-prueba-gratuita-y-reembolso-solo-en-creditos` | Sin prueba gratuita, prepago, y el reembolso se devuelve **como crédito interno** vía ticket |
| `flokinet-nombres-servidor-ns1-a-ns4-y-panel-de-dns` | `ns1..ns4.flokinet.net` + cuenta de gestión DNS al contratar VPS o shared hosting |
| `flokinet-migracion-desde-shared-con-cpanel-whm` | Migración asistida **desde shared hosting** vía CPanel/WHM con licencia **no incluida**; sin CPanel es manual |
| `flokinet-nvme-u2-y-nodos-de-20-gbit-como-argumento` | NVMe enterprise PCIe x8/U.2, nodos 10/20 Gbit, claims 5× bandwidth, 1000× I/O, 300× response time |
| `flokinet-no-gestionado-y-reseller-con-carga-legal` | No gestionado con **5 funciones del hypervisor gratis**, y reventa autorizada con el reseller responsable del soporte y de la AUP |

## Lo que aporta al vault

**1. El "offshore con empresa identificable", que es un modelo que el thread no tenía.** Anubiz vende anonimato sin KYC; FlokiNET vende lo contrario — RIPE member, ISNIC member, CPanel Authorized Partner, 10 años de mercado — y llama a su argumento "offshore for greater privacy and protection against censorship". La privacidad que ofrece es **resistencia a la censura, no anonimato**, y eso reordena la escala del thread: para el relay autoalojado del vault importa más el segundo que el primero.

**2. La definición más precisa de "no gestionado" del vault.** No gestiona el sistema operativo (tú haces kernel, repos, firewall, apps) pero **sí da gratis y a mano** las cinco funciones del hypervisor: acceso SSH, acceso a red, instalación de Linux, resolución de particiones tras upgrade y **recuperación de backup**. Cada una es un momento en que un VPS autoalojado se rompe. ExtraVM declara "no gestionado" pero ofrece soporte propio 24/7; FlokiNET no tiene línea gestionada y aun así cubre los cinco puntos calientes de la barra de soporte.

**3. El precio del egreso, calculado.** FlokiNET publica 3 TB en el plan de entrada y 20 TB en el alto, con uplink de 1 Gbit, y **no dice en qué dirección se cuenta el tráfico**. Normalizado: 0,38 TB/€ en la entrada y 0,27 TB/€ en el alto, frente a los **3,34 TB/€** de Hetzner CPX02 — **8,9× peor** y **12,3× peor** respectivamente. El plan que iguala los 20 TB de Hetzner cuesta €73,90 en lugar de €5,99.

**4. La mejor relación "coste de mitigación" del thread.** DDoS de 1 Tbps en todas las ubicaciones y todos los planes, incluidos y sin precio separado, contra los 3,6 Tbps L4+L7 de HostBrr, los $3/IP de BuyVM o la ausencia de Skhron. Sumado a backups incluidos, consola out-of-band, IPv4+/64 IPv6 y cuatro ubicaciones activas, FlokiNET es el único proveedor del lote que publica a la vez las cuatro cosas.

**5. Dos promesas que hay que no confundir.** "No tenemos acceso a tus datos" y "tus datos están cifrados" son afirmaciones distintas: la primera es una declaración explícita de no-retención; la segunda tiene un límite técnico admitido por el propio proveedor (el cifrado pre-boot no es aplicable a un contenedor virtual) y delega en el cliente el cifrado de particiones. Registrado como fricción 26.

## Para el humano

- **FlokiNET no entra en el tramo de ≤ €4/mes.** Su suelo es €7,99 y el plan de 2 GB (el mínimo del stack) es €14,99. Entra en el mapa como **referencia de privacidad documentada y de coste de mitigación**, no como opción de presupuesto.
- **La página no publica tres cifras que harían falta para cotizar**: la dirección del tráfico incluido, el precio del IPv4 adicional (que sí está permitido, hasta 4) y el precio del tráfico extra. Skhron publica €0,65/mes por IPv4; FlokiNET no publica nada. Esto es un punto ciego declarado, no una estimación.
- **Verificaciones pendientes si se quiere cotizar**: si el "soporte gratuito" de las 5 funciones es el mismo canal y con el mismo horario que el ticket de pago, el precio de la licencia CPanel/WHM para la migración asistida, si la reventa tiene tarifa propia, y el comportamiento real del límite de RAM ampliada bajo carga sostenida.
- **Sin modificar**: `sources/` intacto; la captura ya no está en `0-raw/`.

*Refinery run — 2026-10-24. Captura única: `2026-10-24-flokinet-vps-pricing`.*
