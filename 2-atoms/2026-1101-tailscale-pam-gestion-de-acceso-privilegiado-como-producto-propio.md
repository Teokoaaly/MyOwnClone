---
id: 2026-1101-tailscale-pam-gestion-de-acceso-privilegiado-como-producto-propio
type: atom
certainty: solid
sources: [sources/2026-11-01-tailscale-docs.md]
links: ["[[2026-1031-tailscale-docs]]", "[[2026-1101-tailscale-ssh-integrado-con-grabacion-de-sesion]]", "[[2026-1022-myclone-access-control-por-persona]]"]
---

## Claim
La navegación de la documentación incluye una sección propia, **"Tailscale PAM: Govern Privileged Access"** (`/docs/privileged-access-management`), distinta del control de acceso del tailnet. Enumera: "What is Tailscale PAM?", "Architecture and core concepts", "Get started with Tailscale PAM", "Tailscale PAM connectors", "Tailscale PAM services", "Use a custom DNS domain", "Manage PAM resources using Terraform", "Store session recordings in Amazon S3", "Service accounts", "Session logs", "Control access to services" y "Manage secrets and credentials". La captura **solo aporta estos títulos**: ninguna frase descriptiva del contenido de esas páginas.

## Why It Matters
Esto confirma que Tailscale **no es solo una VPN de hosts**: vende también gestión de acceso privilegiado, y ese producto toca exactamente las tres piezas que el vault tiene hoy como deuda —acceso administrativo, credenciales y registro de sesión. "Service accounts" y "Manage secrets and credentials" son la alternativa documentada a las claves sueltas en variables de entorno; "Session logs" y "Store session recordings in Amazon S3" a la ausencia de trazabilidad de acceso al host que el stack de MyOwnClone no cubre (ver [[2026-1101-tailscale-ssh-integrado-con-grabacion-de-sesion]]). Y "Manage PAM resources using Terraform" indica que el plano de privileged access también se declara como código, lo que encaja con el objetivo de infraestructura declarativa. Límite honesto y relevante para el presupuesto: **la captura no dice qué parte de PAM es de pago** ni si está incluido en el mismo plan que la conectividad; es una pregunta abierta para el eje de coste. La relación con el control de acceso por tenant de la app ([[2026-1022-myclone-access-control-por-persona]]) no está resuelta en la fuente: son planos distintos (red vs negocio).
