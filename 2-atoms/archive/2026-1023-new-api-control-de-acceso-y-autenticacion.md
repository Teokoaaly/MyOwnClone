---
id: 2026-1023-new-api-control-de-acceso-y-autenticacion
type: atom
certainty: retired
sources: [sources/2026-10-22-new-api-github.md]
links: ["[[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]]", "[[2026-1022-myclone-auth-jwt-account-type-creator]]", "[[2026-1022-ia-y-auth-totalmente-servidor]]"]
---

## Claim
La fila "Access control" de la tabla de capacidades define la superficie de control del gateway: **gestión de usuarios, grupos, permisos de grano fino y restricciones de API key**, más **OAuth/OIDC, passkeys, autenticación de dos factores y gestión de sesiones de login**. El historial de commits muestra el cambio de arquitectura que hizo el proyecto: *"refactor(auth): replace dashboard sessions with stateless tokens and session control (#6329)"* — las sesiones de la consola se sustituyeron por **tokens sin estado con control de sesión**, endureciendo la emisión de sesión y la **imposición distribuida**. El README documenta la parte operativa: `SESSION_SECRET` debe ser **persistente y compartido por todos los nodos**, `CRYPTO_SECRET` por defecto deriva de él, y el modo `SESSION_COOKIE_SECURE=true` habilita cookies refresh **Secure** y **comprobaciones estrictas de origen** en refresh y logout.

## Why It Matters
Es la comparación que el vault necesitaba: mientras el producto del vault tiene **NextAuth en el frontend** ([[2026-1022-myclone-auth-jwt-account-type-creator]]) y una arquitectura de "IA y auth totalmente en servidor" ([[2026-1022-ia-y-auth-totalmente-servidor]]), este gateway resuelve el mismo problema en la dirección contraria — **sesiones sin estado**, sin servidor de sesiones, con la scalability como objetivo y el coste en que **el secreto compartido se convierte en punto único de fallo de autenticación** (si dos nodos usan `SESSION_SECRET` distinto, invalidan las sesiones el uno del otro).
Los **passkeys** y el **2FA** son un nivel de acceso que el vault no ofrece hoy, y son un argumento de venta ante clientes corporativos, donde la superficie legal del producto ([[2026-1022-superficie-legal-publica-dpa-clon-terms]]) ya apunta a empresas con datos de clientes finales.
La lección operativa transferible: **la sesión sin estado facilita escalar, pero traslada la seguridad al secreto y a la lista de orígenes de confianza** ([[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]]).


## [RETIRED]
Contenido fusionado dentro de [[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]] por regla de una idea por átomo. Fuente: [[2026-1023-new-api-gateway-unificado-de-modelos]].
