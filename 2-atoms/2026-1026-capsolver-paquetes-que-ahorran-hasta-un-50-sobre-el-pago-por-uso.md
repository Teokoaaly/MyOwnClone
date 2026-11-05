---
id: 2026-1026-capsolver-paquetes-que-ahorran-hasta-un-50-sobre-el-pago-por-uso
type: atom
certainty: solid
sources: [sources/2026-10-25-capsolver-home.md]
links: ["[[2026-1024-2captcha-solo-se-paga-por-captcha-resuelto]]", "[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1026-capsolver-nueve-tipos-con-precio-y-latencia]]"]
---

## Claim
La sección de precios de la home de CapSolver publica, junto a la tabla por 1000, el claim **"Check our popular packages — save up to 50% compared to pay per use!"** y la frase **"We offer both pay-per-use and package options"**, con un enlace a un **"Package Market"** (`dashboard.capsolver.com/dashboard/market`). La tabla visible es, por tanto, el precio de la modalidad de pago por uso.

## Why It Matters
Es el primer dato de **descuento estructural** del corpus de captchas: hasta un **50 %** sobre el precio de lista. Toda la aritmética de captchas del thread —$0.0005 a $0.00299 por captcha en 2Captcha ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]])— es un cálculo sobre **precio de lista**, y este claim significa que el precio efectivo de un volumen alto puede ser la mitad.
La consecuencia metodológica es la misma que ya registró el thread para HeroSMS: **un precio solo vale con su unidad, su fecha y sus condiciones comerciales**, y aquí hay que añadir una tercera: **la modalidad de compra**. Con un -50 % declarado, el precio por 1000 de la home **no es un techo ni un suelo**: es la referencia del modo más caro.
Y el canal de packages introduce un elemento nuevo en el modelo de contrato del sector: un **"Package Market"** dentro del panel de cliente, es decir, un mercado secundario de crédito prepagado dentro del propio dashboard, no un simple plan mensual.

## [FRICTION]
> [[2026-1024-2captcha-solo-se-paga-por-captcha-resuelto]] fija el contrato del sector de captchas en tres condiciones —"The server load does not affect the price", "Pay only for solved captchas" y "99.9% uptime"— y de ahí sale que el coste marginal de una operación fallida es cero porque solo se paga por lo resuelto.
> Este átomo presiona ese contrato en un punto: **CapSolver no publica ninguna de las tres condiciones**. Su tabla publica precio y latencia, y su sección comercial publica un descuento por volumen, pero la captura **no** contiene "pay only for solved captchas" ni SLA de uptime ni la frase de que la carga no afecta al precio. Es decir: el único modelo de cobro que el vault puede leer aquí es **precio por 1000 y descuento por volumen**, y el "solo se paga por lo resuelto" que el thread da por característica de sector **no está verificado en este proveedor**. Marcado para juicio humano, no auto-resuelto: la ausencia en una home no es una negativa; la captura no incluye las páginas de producto ni los términos.

Nota: la captura **no** publica los precios de los paquetes, sus umbrales de volumen, ni si el descuento se aplica a todos los tipos.
