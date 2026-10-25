---
id: 2026-1024-njal-la-vpn-wireguard-y-openvpn-con-tunel-cifrado-y-15-anos-de-experiencia
type: atom
certainty: solid
sources: [sources/2026-10-24-njal-la-domains-vpn.md]
links: ["[[2026-1024-njal-la-precios-no-publicados-para-vpn-y-servidores]]", "[[2026-1024-mullvad-cripto-con-10-de-descuento]]", "[[2026-1024-njal-la-cripto-y-paypal-como-metodos-de-pago-aceptados]]"]
---

## Claim
El servicio de VPN de `njal.la` es un **túnel cifrado desde el equipo del cliente a Internet**, con la **IP real oculta detrás de una IP del proveedor**: "We hide your real IP address behind one of ours. This means your online activity can't instantly be seen by service providers, governments or others". Los **protocolos declarados son dos: Wireguard y OpenVPN**. La experiencia se vende con una antigüedad explícita: **"We've done this for 15+ years"**. El posicionamiento comercial es explícito sobre el destinatario: "If you're an activist, a soccer mom or just hiding your obsession with cross-stitching we're used to dealing with weird situations".

## Why It Matters
Es la **primera fuente del vault que documenta Wireguard como protocolo de una VPN de código abierto** junto a OpenVPN, y la que ancla el eje de antigüedad: **15+ años** es la trayectoria más larga declarada por una VPN del vault (Mullvad declara "sin cambio desde 2009" en precio, pero su captura es de precios, no de protocolos). La combinación **Wireguard + OpenVPN** importa operativamente: son los dos protocolos que el stack autoalojado del vault ya usa como referencia (el relay de [[myownclone-platform-architecture]]), y dual-protocol significa que **se puede cambiar de cliente sin cambiar de proveedor**.

El límite de la fuente es la ausencia de cifras: **no hay precio de VPN, ni número de servidores o ubicaciones, ni ancho de banda, ni política de logs, ni interruptor de corte (kill switch), ni cifras de auditoría**. Con un precio no publicado, la VPN de `njal.la` **no es cotizable** frente a la de Mullvad (€5/mes IVA incluido, con **10 % de descuento en cripto** según [[2026-1024-mullvad-cripto-con-10-de-descuento]]): el vault puede saber que ofrece Wireguard y 15 años, y **no puede saber cuánto cuesta**.
