---
id: 2026-1101-tailscale-gestion-de-dispositivos-y-autenticacion-por-identidad
type: atom
certainty: solid
sources: [sources/2026-11-01-tailscale-docs.md]
links: ["[[2026-1031-tailscale-docs]]", "[[2026-1101-tailscale-plano-de-control-centralizado-por-politica-y-dispositivos]]", "[[2026-1022-myclone-access-control-por-persona]]"]
---

## Claim
El índice de Tailscale enumera las páginas que gobiernan **el alta y el ciclo de vida de los dispositivos**: "Manage devices" (`/docs/features/access-control/device-management`), "Manage access control" (`/docs/features/access-control`), "Manage just-in-time access" (`/docs/features/access-control/just-in-time-access`), "Tailnet Lock" (`/docs/features/tailnet-lock`), "Set up an identity provider" (`/docs/integrations/identity`) y, en la sección de servidor, "Use auth keys" + "Automate key expiry" + "Use tags". La aprobación de dispositivos no aparece con ese nombre en ninguna de las tres capturas: la palabra disponible es "device management" más "just-in-time access".

## Why It Matters
El control de acceso de MyOwnClone está hoy ligado a la persona ([[2026-1022-myclone-access-control-por-persona]]); Tailscale propone un segundo nivel, ligado al **dispositivo**, con tres palancas separables: identidad del nodo (auth key, tags, proveedor de identidad), acceso temporal (just-in-time access) y bloqueo del tailnet (Tailnet Lock). Es el modelo que permite que el worker y el api se autentiquen como máquinas sin que eso equivalga a convertirlos en usuarios del panel. Límite honesto y relevante: **la captura no nombra ninguna página de "device approval" ni describe el flujo de aprobación**; quien lo necesite tiene que capturar `/docs/features/access-control/device-management` y la sección de onboarding, que no están en este corpus. Por eso este átomo es un mapa de control, no una descripción del proceso de alta.
