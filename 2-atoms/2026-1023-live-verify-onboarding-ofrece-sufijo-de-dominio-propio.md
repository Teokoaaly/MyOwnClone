---
id: 2026-1023-live-verify-onboarding-ofrece-sufijo-de-dominio-propio
type: atom
certainty: solid
sources: [0-raw/archive/2026-10-23-2026-10-22-myownclone-live-reverification.md]
links: ["[[2026-1022-gap-custom-domains-campo-inactivo]]", "[[2026-1022-myclone-custom-domains-whitelabel]]", "[[2026-1022-multi-tenant-slug-unpublished]]", "[[2026-1022-live-verify-alta-y-precios-ya-publicos]]"]
---

## Claim
El onboarding vivo de [[myownclone]] incluye los placeholders de URL `slugSuffix: ".myownclone.yourdomain.com"` y `urlSuffix: ".myownclone.com"`, junto con los cuatro pasos ya verificados (`name` → `personality` → `language` → `confirm`). Es decir, la UI de alta ofrece **al usuario elegir el sufijo de su slug**, con una plantilla de dominio propio (`tunombre.myownclone.yourdomain.com`) como valor por defecto, y el dominio del producto (`.myownclone.com`) como sufijo alternativo. El flujo es ahora self-service y público (ver [[2026-1022-live-verify-alta-y-precios-ya-publicos]]), de modo que la elección del subdominio ocurre sin intervención de la plataforma.

## Why It Matters
Convierte el "custom domain" de nota de roadmap a **superficie de producto expuesta al cliente**: el tenant ve la mecánica del dominio propio en la propia pantalla de alta, aunque el backend que la resuelve sigue sin existir (no hay verificación DNS ni SSL, ver [[2026-1022-gap-custom-domains-campo-inactivo]]). Para el competidor [[2026-1022-myclone-custom-domains-whitelabel]] esto marca la dirección de la carrera: MyClone.is ya expone `POST /custom-domains` con verificación y cuota por tier; MyOwnClone muestra el hueco en el formulario pero no lo cierra.

## [FRICTION]
> [[2026-1022-gap-custom-domains-campo-inactivo]] afirma que el campo `custom_domain` en `CloneConfig` "existe y no se usa activamente: no hay flujo de verificación DNS, ni SSL, ni resolución del dominio en el serving del clon", y sitúa el dominio propio en Fase 4 con prioridad 🟢 BAJA; [[2026-1022-multi-tenant-slug-unpublished]] afirma por su parte que "el dominio personalizado es una capacidad ya activa del producto" y que la URL pública es `subdomain.myownclone.com`.
> Este átomo presiona la primera creencia porque la UI viva ofrece literalmente el sufijo `.myownclone.yourdomain.com` al usuario final en el alta self-service — el control está expuesto aunque la resolución no. Y matiza la segunda: la URL pública observada es el slug bajo `.myownclone.com`, no un dominio propio ya operativo.
> Ambas no pueden ser completamente correctas: o el dominio propio es solo una plantilla de texto sin efecto, o el marketing del onboarding va por delante de la infraestructura. La lectura más consistente es la primera: es un placeholder, no un flujo.
> Marcado para juicio humano, no auto-resuelto.
