---
id: 2026-1024-evoxt-sub-cuentas-por-rol-para-equipos
type: atom
certainty: solid
sources: [sources/2026-10-23-evoxt-vps-pricing.md]
links: ["[[2026-1022-myclone-access-control-por-persona]]", "[[2026-1024-evoxt-api-y-rescue-mode-para-gestion-de-vms]]", "[[2026-1022-platform-admin-tenants-costes-mrr]]"]
---

## Claim
Evoxt ofrece **sub-cuentas con roles** dentro de una misma cuenta para equipos: *"Require access to be given for each Administrator, Technical Team, Billing Team, Support Team? We've got that covered for you"*. Los roles citados son **Administrator, Technical Team, Billing Team y Support Team**, con el panel como mecanismo de delegación de acceso.

## Why It Matters
Es la primitiva de **RBAC a nivel de infraestructura**, distinta del RBAC a nivel de producto. El vault ya tiene el segundo documentado en MyClone.is —`access-control` por persona, `request-access`, `verify-access`, `init-session` ([[2026-1022-myclone-access-control-por-persona]])— pero en el lado de la plataforma el acceso es plano: hoy [[myownclone]] se opera desde un nginx autoalojado sin separación de roles, y el back-office de tenants y costes ([[2026-1022-platform-admin-tenants-costes-mrr]]) no tiene noción de "técnico" frente a "facturación". Cuando el producto crezca a varios tenants, la pregunta "quién puede desplegar, quién puede ver la factura, quién habla con el cliente" se resuelve en el panel del proveedor sin tocar la aplicación — un argumento de coste operativo a favor de un VPS gestionado frente a uno self-hosted.

## Nota de verificación
Texto transcrito literalmente. La captura **no** publica: la granularidad real de permisos por rol, si los roles son editables, ni si hay auditoría de acciones por sub-cuenta.
