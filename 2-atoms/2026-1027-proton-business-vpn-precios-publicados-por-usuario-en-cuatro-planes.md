---
id: 2026-1027-proton-business-vpn-precios-publicados-por-usuario-en-cuatro-planes
type: atom
certainty: solid
sources: [sources/2026-10-26-proton-business-vpn-pricing.md]
links: ["[[2026-1024-proton-ofrece-vpn-para-empresas-sin-precio-publicado]]", "[[2026-1026-ivpn-licencias-de-equipo-para-planes-vpn-sin-precio-publicado]]", "[[2026-1024-mullvad-precio-plano-5-euros-iva-incluido-sin-cambio-desde-2009]]"]
---

## Claim
La página de precios B2B de Proton **sí publica precios, por usuario y por mes**, para cuatro planes con un conmutador `MonthlyYearly`: **VPN Essentials $6.99/user per month** ("Minimum 2 users"), **VPN Professional $9.99/user per month** ("Minimum 2 users"), **VPN and Pass Professional $10.99/user per month** ("Minimum 3 users") y **Workspace Standard $12.99/user per month** (sin mínimo declarado). Los enlaces de compra de las cuatro tarjetas llevan `billing=12` y el número de usuarios ya fijado en la URL (`users=2`, `users=2`, `users=3`, y sin `users` en Workspace), es decir **el proveedor precarga el mínimo de licenses y la facturación anual en el propio enlace**.

## Why It Matters
Esta es la **primera línea de empresa del corpus con precios cotizables**, y por tanto la primera vez que el vault puede poner número a la partida que hasta ahora era un dato faltante: el coste de salida a Internet de un producto multi-tenant ([[2026-1022-costes-por-categoria-tenant]]). El dato estructural es que **la unidad de venta cambia**: el VPN de consumo se paga por cuenta con 10 dispositivos ([[2026-1024-protonvpn-diez-dispositivos-y-20000-servidores-en-140-paises]]) y el B2B se paga **por usuario**, con un mínimo de 2 o 3 licencias. Para un producto con N tenants, el suelo de la partida de red pasa de "una suscripción plana" (€5/mes de Mullvad, [[2026-1024-mullvad-precio-plano-5-euros-iva-incluido-sin-cambio-desde-2009]]) a "N × precio de asiento con un mínimo de usuarios": **$13,98/mes como suelo de dos licencias en Essentials** y $155,88/año como precio de una sola licencia en Workspace Standard.

## [FRICTION]
> [[2026-1024-proton-ofrece-vpn-para-empresas-sin-precio-publicado]] (escrita el 2026-10-24) afirma que la página de precios de Proton cierra con un bloque comercial **sin cifras** para la línea de empresa, y que "**la captura no publica ningún precio, número de dispositivos, SLA ni cobertura**" de la línea B2B.
> Este átomo presiona eso de forma directa: **la línea de empresa de Proton sí tiene precio publicado** —$6,99 a $12,99 por usuario y mes, con mínimos de 2, 2, 3 y ninguno— en `sources/2026-10-26-proton-business-vpn-pricing.md`. La ausencia registrada era, por tanto, **una ausencia de esa captura concreta** (la página de precios de consumo), no un rasgo del proveedor, y la lectura correcta es que **Proton cotiza su línea B2B y IVPN no**: la fricción 37 del thread («la línea de empresa es la única partida del vault cuyo precio no existe en ninguna captura») queda **desmentida para uno de los dos proveedores** y reformulada para el otro ([[2026-1026-ivpn-licencias-de-equipo-para-planes-vpn-sin-precio-publicado]]).
> Ambas no pueden ser completamente correctas. Marcado para juicio humano, no auto-resuelto: el átomo viejo no se modifica; la extensión se propone en `1-desk/extend-2026-10-26-proton-business-vpn-pricing.md`.
