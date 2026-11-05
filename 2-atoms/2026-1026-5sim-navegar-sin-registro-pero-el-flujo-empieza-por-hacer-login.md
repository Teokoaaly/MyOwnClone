---
id: 2026-1026-5sim-navegar-sin-registro-pero-el-flujo-empieza-por-hacer-login
type: atom
certainty: tentative
sources: [sources/2026-10-25-5sim-home.md]
links: ["[[2026-1023-5sim-smart-buy-y-tasa-entrega-visible]]", "[[2026-1023-5sim-casos-de-uso-qa-y-privacidad]]", "[[2026-1023-5sim-catalogo-servicios-precios-y-stock]]"]
---

## Claim
La home de 5sim afirma en su sección competitiva "**No registration needed to browse** — check every country, service, price and success rate before creating an account", pero el apartado "How to receive an SMS using a virtual number" empieza literalmente por "**Start off by [Logging in](https://5sim.net/login) or [Signing up](https://5sim.net/signup)**" y a continuación exige tres pasos: 1) "Choose country, service and get a virtual phone number", 2) "Use the virtual phone number to receive an SMS", 3) "Use SMS for successful completion". Es decir: **la página promete registro cero para navegar y describes el registro como el paso cero del flujo de compra**, y el paso 1 incluye elegir país y servicio, que es exactamente lo que el propio bloque "browse" dice que se puede consultar sin cuenta.

## Why It Matters
Distingue dos cosas que la página no separa: **consultar el catálogo** (sin cuenta, con precios y tasas) y **comprar** (con cuenta). El vault ya tiene el dato del catálogo: 1329 servicios, 153 países, ocho precios "from" y contadores de stock visibles ([[2026-1023-5sim-catalogo-servicios-precios-y-stock]]), y los precios reales del CSV de `telegram` ([[2026-1023-5sim-smart-buy-y-tasa-entrega-visible]]) — todo consultable sin cuenta. Eso significa que **la promesa "no registration needed to browse" es verificablemente cierta como función de precios** y es exactamente lo contrario de un funnel cerrado: el comprador puede cotizar el insumo antes de crear nada.
Para un producto propio con alta por email y código mágico, esto es la **política opuesta** al patrón de baja fricción que el vault sigue: registrar primero (para luego cotizar) es el patrón de SaaS; cotizar primero y registrar solo para pagar es el patrón de marketplace de insumos ([[2026-1023-5sim-casos-de-uso-qa-y-privacidad]]). Y es la diferencia real entre un producto que **vende una suscripción** y uno que **vende unidades**.

## [FRICTION]
> [[2026-1023-5sim-smart-buy-y-tasa-entrega-visible]] (escrita el 2026-10-23) afirma que "**la home afirma además que no hace falta registrarse para navegar**: se puede consultar cada país, servicio, precio y tasa de éxito antes de crear cuenta", y lo lee como "el patrón opuesto al funnel de [[myownclone]], donde el alta exige cuenta".
> Este átomo presiona esa creencia en un matiz que el átomo anterior no registraba: **la propia página contradice la promesa dentro de la misma URL**, porque el flujo de compra documentado empieza por "Logging in or Signing up" y el paso 1 es elegir país y servicio. O la promesa de "browse sin registro" se refiere solo a una **capa de consulta superficial** (precios "from" y tasas del selector) mientras que elegir país, servicio y operador —la compra— sí exige cuenta, o la página es incoherente y el registro no es un requisito real.
> Ambas no pueden ser completamente correctas: o "browse" cubre también la elección de par país-servicio-operador, o el flujo documentado contradice su propia promesa. Marcado para juicio humano, no auto-resuelto: la captura **no** muestra qué se ve antes y después de identificarse, ni publica un modo de prueba sin cuenta, así que no hay forma de medir la frontera.
