---
id: 2026-1026-ivpn-wireguard-resistente-a-cuantico-y-clientes-abiertos-en-cinco-plataformas
type: atom
certainty: solid
sources: [sources/2026-10-25-ivpn-pricing.md]
links: ["[[2026-1024-njal-la-vpn-wireguard-y-openvpn-con-tunel-cifrado-y-15-anos-de-experiencia]]", "[[2026-1026-bitlaunch-vpn-wireguard-multiregion-y-multihop-como-producto]]", "[[2026-1024-proton-postura-de-privacidad-suiza-sin-registros-y-codigo-abierto]]"]
---

## Claim
El bloque «IVPN features» declara **«Quantum-resistant WireGuard connections»** y **«Open-source clients (Android, iOS, macOS, Windows, Linux/CLI)»**, además de **«Obfuscation protocols (v2Ray, obfsproxy)»**, **«SOCKS5 proxy service»**, **«Kill switch with network firewall integration»**, **«Private DNS resolvers (no third-party logging)»**, **«DNS-based AntiTracker with configurable blocklists»** y **«Router and NAS deployment support»**.

## Why It Matters
El resto del corpus de VPN del vault documentaba WireGuard como protocolo ([[2026-1024-njal-la-vpn-wireguard-y-openvpn-con-tunel-cifrado-y-15-anos-de-experiencia]]) y BitLaunch como el único que lo vendía como producto propio [[2026-1026-bitlaunch-vpn-wireguard-multiregion-y-multihop-como-producto]]; **IVPN es el primer proveedor del corpus que combina WireGuard con declaración de resistencia a cuántico**, y lo hace junto con **ofuscación explícita (v2Ray, obfsproxy)**, que es el requisito de los proveedores de VPN que operan en jurisdicciones con bloqueo de protocolo. El corolario operativo es el más importante para el vault: **«Router and NAS deployment support»** significa que el cliente de IVPN se puede instalar en el propio servidor, de modo que el producto podría obtener una salida con IP fija propia sin arrendar un nodo ajeno — lo que es justamente el patrón que el corpus ya tiene marcado como problemático en el contexto del alta por SMS ([[2026-1023-hero-sms-ip-y-vpn-coincidentes-con-el-pais-del-numero]]).

## Nota de verificación
«Quantum-resistant» es una **claim del proveedor sin cipher suite ni referencia a auditoría**; la captura no publica qué algoritmo post-cuántico usa, ni los clientes concretos (el código de cada plataforma), ni las condiciones del despliegue en router y NAS.
