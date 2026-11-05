---
id: 2026-1026-heroku-key-value-store-upgrade-con-problemas-de-ssl-tls
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-support-home.md]
links: ["[[2026-1026-heroku-key-value-store-mini-3-dolares-hasta-12500]]", "[[2026-1026-heroku-soporte-articulo-mas-tendido-es-instruccion-para-no-abrir-ticket]]", "[[2026-1026-heroku-claims-de-escala-65m-apps-y-65b-requests-con-customer-logos]]"]
---

## Claim
El quinto artículo de "Trending articles" de la home de soporte de Heroku es **"Heroku Key-Value Store Upgrade - SSL/TLS Connection Issues"** (identificador `HC0F8CUS`, que redirige a `help.heroku.com/redis-connection-issues`). Es decir, **una incidencia de conexiones TLS rotas tras una actualización del Redis gestionado está entre los cinco contenidos más leídos del soporte de Heroku**. La home también enlaza, como artículo de tendencia, **"Heroku Security"**, que apunta al documento de política de seguridad en `www.heroku.com/policy/security/`.

## Why It Matters
Es una **fractura de contrato operativa dentro del producto gestionado**: el vault ya tenía el catálogo del Key-Value Store con sus 25 planes desde $3/mes en adelante ([[2026-1026-heroku-key-value-store-mini-3-dolares-hasta-12500]]) y sus distinciones de single-tenant a partir de Premium 7. Esta captura añade el aviso de que **el ciclo de upgrade del servicio gestionado puede romper el canal cifrado de las apps existentes**, y que ese problema llega a la categoría de top-5 de soporte — es decir, **es una situación recurrente, no un incidente aislado**.
Eso tiene un coste que no aparece en el catálogo: **un cliente que migra su base de datos sobre el Redis gestionado de Heroku hereda un riesgo de corte de servicio en cada upgrade del proveedor**, que no aparece en el precio del plan ni en sus "High availability with low-latency failover". Es el mismo tipo de fricción que el vault ya marcaría en un proveedor de VPS: el SLA del hosting no cubre la transición de versiones del software gestionado. Con 65 millones de apps y 200+ add-ons declarados ([[2026-1026-heroku-claims-de-escala-65m-apps-y-65b-requests-con-customer-logos]]), la superficie de apps que puede estar afectada por un mismo cambio de TLS es enorme.
Para el producto propio, que **autoaloja su Redis** ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]), esta es exactamente la clase de dependencia que el vault está tratando de evitar al elegir infraestructura propia.

## [FRICTION]
> [[2026-1026-heroku-key-value-store-mini-3-dolares-hasta-12500]] afirma que **todos** los planes del Key-Value Store, desde Mini $3 hasta Shield-14, declaran **"High availability with low-latency failover"** y "Resource scalability".
> Este átomo presiona esa afirmación en un punto: **la propia home de soporte declara, entre sus cinco contenidos más leídos, que un upgrade del servicio rompe las conexiones SSL/TLS de las apps existentes** ([[2026-1026-heroku-key-value-store-upgrade-con-problemas-de-ssl-tls]]). Disponibilidad y failover no cubren la **transición de versión**, que es un evento único y no un estado. Marcado para juicio humano, no auto-resuelto: la captura **no** reproduce el artículo, así que no se puede saber si el fallo afecta a un rango de versiones concreto, a un plan concreto, a toda la base de clientes de un tiers, o si es un caso ya resuelto por el proveedor. El átomo queda `solid` solo en la existencia y el título del artículo, no en su alcance.

Nota: la captura **no** reproduce el artículo: no publica la versión anterior ni la nueva, ni la fecha, ni el alcance afectado, ni si existe un workaround o si Heroku lo considera problema conocido con un parche.
