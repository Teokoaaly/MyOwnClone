---
id: 2026-1026-mailsac-subdominios-en-segundos-y-idioma-de-dominio-propio
type: atom
certainty: solid
sources: [sources/2026-10-25-mailsac-test-email.md]
links: ["[[2026-1022-gap-custom-domains-campo-inactivo]]", "[[2026-1022-email-inbound-contacto-sin-dominio-propio]]", "[[2026-1024-notletters-captura-minima-sin-dominios-ni-limites-ni-condiciones]]"]
---

## Claim
MailS.ac vende **dos capas de dominio de prueba** por encima del `@mailsac.com` compartido. La primera es el **"Zero Setup Subdomain service"**: "Create subdomains in seconds, thanks to our Zero Setup Subdomain service", con la descripción "Separate applications within their own domain with our zero-setup subdomain feature. Categorize workflows, email testing phases or different testing teams with our ability to quickly generate and assign email subdomains". La segunda es explícitamente **BYOD**: "**BYOD - You can also bring your own domain!**", es decir, dominio propio del cliente como namespace de test. La sección de venta lo resume en "Subdomains in seconds" y "Hassle Free Subdomains".

## Why It Matters
Es la **tercera vía** del dominio en el sector, después del dominio compartido del proveedor (NotLetters y 卡网 no publican ni un dominio; [[2026-1024-notletters-captura-minima-sin-dominios-ni-limites-ni-condiciones]]) y del dominio propio autoalojado del producto (que en el vault está como campo inactivo o "Coming soon", [[2026-1022-gap-custom-domains-campo-inactivo]]). MailS.ac cubre las dos: **subdominio generado sin configuración** y **dominio propio del cliente traído con BYOD**.

La lectura para el vault es de arquitectura, no de precio: el mecanismo "zero setup subdomain" es una **externalización de la configuración DNS y MX** —justo la parte que un producto con dominio inbound por tenant tendría que resolver para cada cliente ([[2026-1022-email-inbound-contacto-sin-dominio-propio]]). El proveedor de correo de QA ya lo vende como producto; lo que el vault no tiene es la **parte de la marca**: el subdominio de un proveedor no es el dominio del cliente.

Nota: la captura **no** publica cuántos subdominios incluye cada plan, ni el procedimiento técnico de "zero setup", ni las condiciones de BYOD (si exige verificación DNS, si puede delegar MX, qué registros crea).
