---
id: 2026-1027-2captcha-una-misma-cuenta-factura-captcha-y-proxy
type: atom
certainty: solid
sources: [sources/2026-10-26-2captcha-pricing-captcha.md, sources/2026-10-26-2captcha-pricing-residential-proxy.md]
links: ["[[2026-1027-2captcha-menu-de-precios-con-7-lineas-y-dos-sin-cifra]]", "[[2026-1027-2captcha-catalogo-completo-de-48-filas-de-captcha]]", "[[2026-1027-2captcha-proxy-residencial-de-399-a-125-por-gb-en-nueve-escalones]]"]
---
## Claim
Las dos capturas del 2026-10-26 comparten **una sola cuenta, un solo hub de precios y una sola familia de integración**, y esa cuenta **cobra dos partidas distintas del modelo de coste del vault con unidades distintas**: el captcha **por 1000** (48 tipos, tres unidades de precio dentro de la fila) y el proxy residencial **por GB** (nueve planes prepagados por volumen). La línea de **Data annotation** aparece en ese mismo hub, pero **sin cifra publicada** —solo formulario de contacto ([[2026-1027-2captcha-menu-de-precios-con-7-lineas-y-dos-sin-cifra]]).

## Why It Matters
El modelo de coste del thread tiene partidas —captcha, proxy, correo, SMS, hosting— que hasta ahora el vault había contabilizado como **compras en proveedores distintos**, y el thread los comparaba fila a fila como si fueran un mercado. Esta captura muestra el caso límite: **un solo proveedor factura dos de esas partidas a la vez**, con **unidades de cobro que no se pueden sumar** ($/1000 y $/GB), y por tanto **la comparación "captcha contra proxy" que el thread hacía fila a fila se convierte en una comparación dentro de la misma factura**. Eso tiene una consecuencia metodológica concreta: **el coste marginal de pasar de "resolver el captcha" a "resolver el captcha y además parecer un usuario residencial"** no se puede estimar con dos proveedores distintos, porque con un proveedor único la combinación **compite por el mismo presupuesto y la misma integración**.

La segunda consecuencia es de naturaleza del negocio, y es la que no estaba en el vault: **"Data annotation" es la misma capacidad humana que 2Captcha revendía como captcha resuelto, ahora vendida como dataset a clientes de IA.** Es decir, **el proveedor ha convertido su coste de producción interno en una línea de producto con clientes distintos**. Esto conecta el modelo de elusión con el modelo de datos: **la mano de obra que resuelve captchas es exactamente la mano de obra que etiqueta datos**, y en un proveedor que hace las dos cosas, **la frontera entre "commodity de evasión" y "servicio de datos" desaparece**. Para el thread, esto importa porque la §11 sostiene que la capa dominante de un flujo de alta es una construcción, no una compra: **el proveedor está vendiendo la construcción como producto, con su pool humano incluido**.

Y hay un apunte de modelo que conviene no perder: **las dos líneas sin cifra son exactamente las dos que el vault no puede cotizar**, de modo que **el "precio del catálogo" de 2Captcha es un precio de las cinco pestañas medibles**, no de la carta completa. La partida de annotation —que es la que más se parece a la reventa de trabajo humano que el thread analiza— **es precisamente la que no tiene precio público**.

Nota: la captura **no** publica si el saldo de proxy y el consumo de captcha comparten el mismo monedero, si una misma clave de API sirve para ambas líneas, ni si el tráfico de proxy y el cómputo de captcha se facturan en una sola factura.
