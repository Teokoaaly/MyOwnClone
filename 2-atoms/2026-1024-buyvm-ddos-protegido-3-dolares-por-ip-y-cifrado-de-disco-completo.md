---
id: 2026-1024-buyvm-ddos-protegido-3-dolares-por-ip-y-cifrado-de-disco-completo
type: atom
certainty: solid
sources: [sources/2026-10-23-buyvm-kvm-slices.md]
links: ["[[2026-1024-hostbrr-ddos-3-6-tbps-l4-y-l7-incluido]]", "[[2026-1024-extravm-ddos-varia-por-ubicacion-y-sydney-sin-proteccion-nativa]]", "[[2026-1024-hostkey-ipv4-e-ipv6-dedicados-por-servidor]]"]
---
## Claim
La protección DDoS de BuyVM **no viene incluida en el plan**: es un addon de **$3.00 / month por cada IP protegida**, con "BuyVM's DDoS filtered IPv4 addresses protect your server from Layer 4 - 7 DDoS attacks" y capacidad declarada de **500+ GIGABITS PER SECOND** y **700+ MILLION PACKETS/SEC**; filtra "ICMP, SYN, SYN Spoofed, UDP, reflection attacks". Las IPs protegidas están disponibles en **todas** las ubicaciones BuyVM. En paralelo, la página ofrece **Full Disk Encryption (FDE) out of the box** vía KVM: "allowing you to make sure that your data is safe and only accessible by those that have the encryption passphrase". La gestión de IP incluye **failover / floating IP addresses**, asignación de **IPv6** y de **Anycast IP addresses**, y reverse DNS, desde el panel Stallion.

## Why It Matters
Es el eje de **seguridad de red como coste variable**, y BuyVM queda en un punto intermedio que no coincide con ningún otro proveedor del vault: HostBrr **incluye** mitigación DDoS L4+L7 de hasta 3,6 Tbps sin coste adicional ([[2026-1024-hostbrr-ddos-3-6-tbps-l4-y-l7-incluido]]), mientras ExtraVM hace depender la protección de la ubicación y deja a Sídney sin protección nativa ([[2026-1024-extravm-ddos-varia-por-ubicacion-y-sydney-sin-proteccion-nativa]]); BuyVM cobra $3.00/IP/mes en todas partes. Para el relay autoalojado del vault —cuyo caso de uso es exactamente un endpoint expuesto que reenvía tráfico y que puede ser objeto de amplificación ([[2026-1023-priceai-sponsors-vps-chinos-para-auto-hospedar-relay]])— **la protección no es opcional en la práctica**: $3.00/mes es un 20 % del slice de $15.00/mes. El **FDE out of the box** importa por otro motivo: el vault registra mercados adyacentes como la verificación SMS y los relays, donde el cliente final entrega datos sensibles y el operador del nodo no debe poder leerlos.

## Nota de verificación
Cifras y frases transcritas literalmente. La captura **no** publica SLA, política de crédito por DDoS, ventana de mitigación, ni el precio de las IPs Anycast o del IPv6 (solo se afirma que se pueden asignar).
