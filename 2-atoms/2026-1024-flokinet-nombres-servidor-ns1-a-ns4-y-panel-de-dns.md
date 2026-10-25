---
id: 2026-1024-flokinet-nombres-servidor-ns1-a-ns4-y-panel-de-dns
type: atom
certainty: solid
sources: [sources/2026-10-24-flokinet-vps-pricing.md]
links: ["[[2026-1024-flokinet-consola-ipmi-virtual-y-panel-novnc]]", "[[2026-1024-flokinet-migracion-desde-shared-con-cpanel-whm]]", "[[2026-1024-flokinet-ubicaciones-offshore-ripe-e-isnic]]"]
---

## Claim
FlokiNET ofrece **cuatro nameservers propios** — **ns1.flokinet.net, ns2.flokinet.net, ns3.flokinet.net, ns4.flokinet.net** — y, al comprar VPS y hosting compartido a la vez, entrega una **"DNS Management account"** con las herramientas para configurar los registros. El modelo DNS es explícito: el dominio debe apuntar con **registro A** (a la IP del VPS) y **registro MX** (al servidor de correo del dominio), y "there are different types of DNS records" sin detallarlos.

## Why It Matters
Es el **único proveedor del vault que publica sus nameservers propios con nombre de host**, lo que permite una comprobación técnica —resolver el dominio contra `ns1.flokinet.net` y leer la IP publicada— en lugar de accepting la declaración de marketing. Y la página también explica qué **no** es un problema de DNS: la IP del VPS y el mapeo del dominio son del cliente, pero el proveedor de *hosting* es quien controla el nameserver, de modo que **cambiar de nameserver puede sacar el dominio de la zona del proveedor**. Para el vault esto importa en un caso concreto: [[myownclone]] tiene dominios con **custom domains y white-label** ([[2026-1022-myclone-custom-domains-whitelabel]]), y moverlos a un servidor autoalojado exige saber de antemano qué nameservers se usarán y si el cliente los va a poder cambiar desde su propio panel. La existencia de una "DNS Management account" separada del panel del VPS es, de hecho, una señal de que el DNS vive en otra parte del producto.

## Nota de verificación
La captura **no** publica: los registros que acepta cada tipo, TTL por defecto, si hay DNSSEC, ni si la "DNS Management account" se entrega automáticamente o es un producto aparte. Los cuatro nameservers están transcritos literalmente del texto.
