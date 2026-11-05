---
id: 2026-1026-new-api-skip-upstream-tls-verification-por-canal
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]]", "[[2026-1026-new-api-cve-2026-111943-corregido-con-go-1-26-10]]", "[[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]]"]
---

## Claim
Desde **v1.0.0-rc.43**, cada canal tiene un interruptor **"Skip Upstream TLS Verification"** en sus ajustes HTTP, para poder conectar con upstreams que usan **certificados autofirmados**. El alcance es amplio: cubre las peticiones de relay, los **WebSocket de Responses y Realtime**, el **envío y el sondeo de tareas**, los **fetch de plugins**, las consultas de **saldo, uso y lista de modelos** y los **medios proxied** por el canal.

Excepciones explícitas: el **refresh de OAuth de Codex** y los **tokens de cuenta de servicio de Vertex o de plugins** **sí verifican** el certificado aunque el interruptor esté activo.

## Why It Matters
Es el switch que hace que el gateway sea utilizable contra upstreams chinos autoalojados o contra relays con certificados propios — es decir, es una **puerta de entrada real en el mercado de reventa** ([[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]]).
Pero es también un **interruptor de verificación desactivada por canal**, en un producto cuyo README pone el listón de seguridad en "HTTPS obligatorio, `Secure` en cookies, `TRUSTED_PROXIES` explícito, secretos compartidos entre nodos" ([[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]]). El matiz útil es que el diseño **no es "desactivar la verificación para todo"** sino "desactivarla por canal, y solo para las rutas de ese canal", con excepciones explícitas para los flujos de identidad — un modelo de **excepción acotada** que es exactamente el que el vault debería aplicar a su propio dominios y cookies ([[2026-1022-live-verify-csp-y-headers-ahora-presentes]]).
Y entra en tensión directa con la corrección de seguridad de la versión siguiente: rc.46 endurece la validación de certificados en el runtime ([[2026-1026-new-api-cve-2026-111943-corregido-con-go-1-26-10]]) mientras rc.43 ofrece el camino para **no validar**. Ver la fricción de ese átomo.

## [FRICTION]
> [[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]] describe la postura de seguridad del README como **estricta y declarativa**: consola detrás de HTTPS, cookies `Secure`, `TRUSTED_PROXIES` explícito, secretos compartidos entre nodos, y la advertencia de que copiar `.env.example` no inyecta variables — es decir, **todo se declara explícitamente y nada se relaja por omisión**.
> Este átomo presiona esa creencia en un punto: **un canal puede tener la verificación de TLS del upstream desactivada**, y esa desactivación **cubre también** la salida de balance, el sondeo de tareas, los fetch de plugins y los medios proxied — no solo la llamada de inferencia. Es decir, existe una **relajación deliberada y silenciosa** en el camino más sensible (el que lleva credenciales y datos de cliente), coexistiendo con una postura de "declara todo explícitamente".
> Ambas no pueden ser completamente correctas en su lectura general: o la postura de seguridad del README es **"todo explícito salvo el upstream, que es territorio del operador"** (y entonces este switch no contradice sino delimita), o el README omite un interruptor de desactivación de verificación con el mismo peso que `TRUSTED_PROXIES`. Marcado para juicio humano, no auto-resuelto: la captura de releases **no muestra el README** y por tanto no permite saber si el switch está documentado ahí, y no dice si queda traza de que un canal tiene la verificación desactivada (es decir, si es **auditable**).

