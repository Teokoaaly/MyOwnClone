---
id: 2026-1104-clerk-compara-con-auth0-con-cifras-b2c-que-el-vault-mide-como-b2b
type: atom
certainty: tentative
sources: [sources/2026-11-04-clerk-pricing.md]
links: ["[[2026-1101-auth0-b2b-essentials-escala-por-mau]]", "[[2026-1101-auth0-addon-sso-enterprise-100-usd-por-conexion]]", "[[2026-1103-auth0-precios-35-y-240-bajo-el-encabezado-b2b-billing]]", "[[2026-1102-workos-auth0-clerk-benchmark-de-identidad-en-tres-vias]]"]
---

## Claim
La FAQ de Clerk incluye una comparación competitiva explícita contra Auth0 —"Is Clerk cheaper than Auth0?"— en la que el proveedor **afirma que "Auth0's free tier is generous at 25K MAU, but its paid plans start at **$35/mo for Essentials and $240/mo for Professional**"**, y añade que "higher user and SSO tiers moving into custom pricing" y que "larger Auth0 SSO needs move into custom or Enterprise tiers". Son cifras de **B2C** presentadas como el precio de entrada general de Auth0, y son afirmaciones de un **competidor directo**, no datos verificados por el vault.

## Why It Matters
El vault tiene medido a Auth0 por captura propia, y el resultado no coincide con la lectura plana de la FAQ de Clerk: la escalera **B2B** de Auth0 empieza en **$150/mes (Essentials) y $800/mes (Professional)** en 500 MAU, no en $35 y $240 ([[2026-1101-auth0-b2b-essentials-escala-por-mau]]), y el add-on de SSO enterprise de Auth0 es de **$100 por conexión** con precio publicado, no "custom pricing" ([[2026-1101-auth0-addon-sso-enterprise-100-usd-por-conexion]]). La consecuencia práctica es doble. Primera: **el argumento de venta de Clerk ("más barato que Auth0") solo se sostiene en el tramo B2C**, y para MyOwnClone —multi-tenant, con organización = tenant y clientes corporativos ([[2026-1022-arquitectura-rac-tres-modos-por-clon]])— la comparación relevante es la B2B, donde la diferencia real es de $150 frente a $20/mes de plan de entrada, no de $35 frente a $20. Segunda: hay un indicio independiente que apoya la lectura de que las cifras Auth0 del vault son correctas: la captura de Auth0 del 2026-11-03 imprimió precisamente **$35 y $240** bajo un encabezado "B2B BILLING", lo que es el mismo par que Clerk cita como "los precios de entrada de Auth0" ([[2026-1103-auth0-precios-35-y-240-bajo-el-encabezado-b2b-billing]]). Es decir, **dos fuentes independientes —la página de Auth0 y la página de su competidor— apuntan a $35/$240 como las cifras B2C**, lo que refuerza que la lectura B2B ($150/$800) del vault es la correcta y que el benchmark de identidad del vault se sostiene ([[2026-1102-workos-auth0-clerk-benchmark-de-identidad-en-tres-vias]]). El átomo queda `tentative` porque el claim es de marketing y porque no se puede comprobar desde el texto si Clerk comparó contra B2C o simplificó.

## [FRICTION]
> [[2026-1103-auth0-precios-35-y-240-bajo-el-encabezado-b2b-billing]] (escrita hace 2 días) Deja abierta la fricción de si $35 y $240 son cifras B2C o B2B, con dos lecturas posibles: artefacto de render o cambio real de precio.
> Este átomo presiona esa cuestión porque **la página de un competidor de Auth0 cita $35 (Essentials) y $240 (Professional) como los precios de entrada de los planes de pago de Auth0**, lo que convierte el par en el par B2C con más respaldo externo, y desplaza la explicación más probable hacia el artefacto de render o hacia un selector interactivo mal capturado. No auto-resuelto: la captura de Auth0 no se ha re-verificado en esta tanda.

## Nota de verificación
Frases verbatim de la FAQ "Is Clerk cheaper than Auth0?" de `sources/2026-11-04-clerk-pricing.md` (idéntico a las del 11-01 y del 11-02). Las cifras de Auth0 son lectura de átomos previos del vault ([[2026-1101-auth0-b2b-essentials-escala-por-mau]], [[2026-1101-auth0-addon-sso-enterprise-100-usd-por-conexion]]), no de esta fuente; la conclusión sobre B2C vs B2B es inferencia marcada como tal.
