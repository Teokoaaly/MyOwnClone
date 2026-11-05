---
id: 2026-1026-bitlaunch-api-publica-cli-y-sdks-para-pago-cripto-programatico
type: atom
certainty: solid
sources: [sources/2026-10-25-bitlaunch-home.md]
links: ["[[2026-1023-hetzner-api-cli-e-integraciones-iac]]", "[[2026-1024-evoxt-api-y-rescue-mode-para-gestion-de-vms]]", "[[2026-1022-myclone-api-rest]]"]
---

## Claim
BitLaunch publica un **Developer API** (`developers.bitlaunch.io/reference`) para "create and manage servers for your project", un **command-line tool** (`blcli`) y **SDKs en Go, Python y PHP** (pkg.go.dev/gobitlaunch, github.com/BitLaunchIO/pybitlaunch, github.com/BitLaunchIO/phpbitlaunch), con Github en `github.com/bitlaunchio`. La home afirma que con la API se puede "Create and even pay for crypto transactions programmatically".

## Why It Matters
Es el **único caso del corpus donde la API de infraestructura incluye el pago programático en criptomoneda como función declarada**, no solo la gestión de recursos. Hetzner publica API + CLI + integraciones de IaC pero su facturación va por factura ([[2026-1023-hetzner-api-cli-e-integraciones-iac]]); Evoxt publica API y Rescue Mode para gestión de VMs ([[2026-1024-evoxt-api-y-rescue-mode-para-gestion-de-vms]]). La diferencia importa para una arquitectura de **gateway autoalojado**: si el pago es programático, un pool de servidores puede crecer y encogerse por máquina sin intervención humana — que es el requisito que el thread de arquitectura de MyOwnClone señala como ausente (proveedor de IA como constante detrás de una variable de entorno, sin router ni failover) ([[2026-1022-myclone-api-rest]]). El contraargumento que el vault ya conoce: automatizar la compra de capacidad con cripto automatiza también el **gasto en un activo que se consume sin contrato**, que es exactamente el patrón de coste no planificado que la tabla de precios del thread de hosting barato tries de hacer visible.

## Nota de verificación
La captura **no publica** límites de rate, autenticación (API keys vs OAuth), versionado, precios de la API, cobertura de la CLI ni si los SDKs están mantenidos. Se toma de las cadenas de texto y enlaces publicados en la home; el contenido de la documentación no fue capturado.
