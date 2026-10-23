---
id: 2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo
type: atom
certainty: solid
sources: [sources/2026-10-22-new-api-github.md]
links: ["[[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]]", "[[2026-1022-cookie-next-locale-sin-httponly-ni-secure]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]", "[[2026-1022-myclone-auth-jwt-account-type-creator]]", "[[2026-1022-ia-y-auth-totalmente-servidor]]"]
---

## Claim
El README tabula las variables de entorno de sesión y proxy, y declara sus requisitos:

| Variable | Requisito declarado |
| --- | --- |
| `SESSION_SECRET` | Secreto persistente de autenticación; **todos los nodos deben usar el mismo valor** |
| `CRYPTO_SECRET` | Por defecto vale `SESSION_SECRET`; los nodos que compartan Redis deben compartir el valor efectivo |
| `SESSION_COOKIE_SECURE` | `true` para consola HTTPS; habilita cookies refresh **Secure** y comprobaciones estrictas de origen en refresh/logout |
| `SESSION_COOKIE_TRUSTED_URL` | Obligatoria en modo Secure: orígenes HTTPS exactos separados por comas, **sin paths ni wildcards** |
| `TRUSTED_PROXIES` | IPs/CIDRs de proxy inverso de confianza, o `none`; debe configurarse explícitamente |

Avisos operativos del README: para producción, **consola detrás de HTTPS** y proxy inverso configurado para streaming y upgrade a WebSocket; **los despliegues multi-nodo deben compartir base de datos principal y secretos de autenticación**; y **"separate Redis instances or in-memory rate limiters count limits independently per node"** — los límites se cuentan por nodo si no hay Redis compartido. Además: *"copying `.env.example` alone does not inject variables into the container"*.

## Why It Matters
El caso del **rate limit contado por nodo** es la avería clásica de un gateway autoalojado que crece: el mismo usuario recibe N veces el límite al añadir réplicas, y el operador descubre el problema cuando ve el abuso. El README lo dice explícitamente — es un límite de diseño documentado, no un bug.
La disciplina de cookies es la referencia que le falta al producto del vault: el sitio vive hoy en nginx sin cabeceras de cookie seguras ([[2026-1022-cookie-next-locale-sin-httponly-ni-secure]]), mientras que este proyecto exige `Secure` + lista blanca de orígenes exactos + proxies de confianza declarados. Es un checklist de hardening directamente aplicable a la consola del vault.
Y la trampa de `.env.example` ("copiar el archivo no inyecta variables") es exactamente el tipo de detalle que hace que un despliegue self-hosted en VPS falle en silencio ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]).

## Extensión (control de acceso y autenticación)
La fila "Access control" de la tabla de capacidades define la superficie: **gestión de usuarios, grupos, permisos de grano fino y restricciones de API key**, más **OAuth/OIDC, passkeys, autenticación de dos factores y gestión de sesiones de login**. El historial de commits documenta el cambio de arquitectura: *"refactor(auth): replace dashboard sessions with stateless tokens and session control (#6329)"* — las sesiones de la consola se sustituyeron por **tokens sin estado con control de sesión**, endureciendo la emisión y la **imposición distribuida**.
Mientras el producto del vault tiene **NextAuth en el frontend** ([[2026-1022-myclone-auth-jwt-account-type-creator]]) y una arquitectura de "IA y auth totalmente en servidor" ([[2026-1022-ia-y-auth-totalmente-servidor]]), este gateway resuelve el problema en dirección contraria: **sesiones sin estado**, sin servidor de sesiones, con la scalability como objetivo y el coste en que **el secreto compartido se convierte en punto único de fallo de autenticación** (dos nodos con `SESSION_SECRET` distinto invalidan las sesiones mutuas). Los **passkeys** y el **2FA** son un nivel de acceso que el vault no ofrece hoy y un argumento de venta ante clientes corporativos, donde la superficie legal del producto ([[2026-1022-superficie-legal-publica-dpa-clon-terms]]) ya apunta a empresas con datos de clientes finales.
La lección operativa transferible: **la sesión sin estado facilita escalar, pero traslada la seguridad al secreto y a la lista de orígenes de confianza**.
