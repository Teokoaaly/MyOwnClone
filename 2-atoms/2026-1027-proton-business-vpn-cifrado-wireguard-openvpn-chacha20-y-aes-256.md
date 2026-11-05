---
id: 2026-1027-proton-business-vpn-cifrado-wireguard-openvpn-chacha20-y-aes-256
type: atom
certainty: solid
sources: [sources/2026-10-26-proton-business-vpn-pricing.md]
links: ["[[2026-1024-proton-postura-de-privacidad-suiza-sin-registros-y-codigo-abierto]]", "[[2026-1026-ivpn-wireguard-resistente-a-cuantico-y-clientes-abiertos-en-cinco-plataformas]]", "[[2026-1024-1984-hosting-certificacion-iso-27001]]"]
---

## Claim
La FAQ de la página de precios B2B responde a "How do I know my organization's data is secure?" con: "Proton VPN only uses the **strongest VPN encryption protocols (like WireGuard® and OpenVPN)**, which are secured using proven encryption standards like **ChaCha20, Ploy1305, and AES-256**". La captura escribe literalmente "Ploy1305" (en lugar de Poly1305). No se publica ninguna versión de WireGuard ni de OpenVPN, ni longitud de clave, ni auditoría de la implementación.

## Why It Matters
Es la **cifra técnica que la línea de consumo no daba**: el vault tenía la postura suiza, el no-logs y el código abierto ([[2026-1024-proton-postura-de-privacidad-suiza-sin-registros-y-codigo-abierto]]), pero no los **algoritmos concretos**. La enumeración importa porque separa dos cosas que el marketing suele fundir: **los protocolos de tunelización** (WireGuard, OpenVPN) y **los primitivos de cifrado** (ChaCha20, Poly1305, AES-256) —el segundo grupo es lo que puede auditarse con una implementación concreta, y **Poly1305 aparece junto a ChaCha20 como el AEAD de WireGuard**, lo que es coherente con la infraestructura del protocolo. Pero el vault tiene ya el contraejemplo documentado en el mismo eje: IVPN declara WireGuard **resistente a cuántico** y clientes abiertos en cinco plataformas ([[2026-1026-ivpn-wireguard-resistente-a-cuantico-y-clientes-abiertos-en-cinco-plataformas]]), es decir **una afirmación criptográfica verificable que Proton no hace**. Ninguna de las dos páginas publica una auditoría, de modo que la comparación sigue siendo entre claims de proveedor, no entre hechos.
