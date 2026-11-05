---
id: 2026-1024-2captcha-servicio-dual-cliente-paga-y-trabajador-cobra
type: atom
certainty: solid
sources: [sources/2026-10-23-2captcha-solver.md]
links: ["[[2026-1023-5sim-catalogo-plataformas-de-microtareas-y-datasets]]", "[[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]", "[[2026-1023-midjourney-proxy-ecosistema-de-aplicaciones-que-lo-consumen]]"]
---
## Claim
2Captcha opera con **dos caras en la misma web**: la de cliente (paga por captcha resuelto, con registro en `auth/register?userType=customer`) y la de **trabajador** (`userType=worker`), que ofrece "Captcha typing job", "Work from home", "Earn money without registration fees" y "Daily payment". Es decir, la capacidad de resolución del servicio no es solo software: es trabajo humano repartido que se paga por tarea.

## Why It Matters
Confirma que el precio del captcha es el precio de **mano de obra**, no de cómputo: quien compra resolución de captchas está contratando en realidad a personas a escala. Es la misma lógica de microtareas por la que 5sim financia su catálogo ([[2026-1023-5sim-catalogo-plataformas-de-microtareas-y-datasets]]) y por la que el coste de verificación es un coste marginal de alta ([[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]).
Para el vault esto fija el techo del negocio de eludir controles anti-bot: hay un **insumo de trabajo humano baratísimo y distribuido** detrás, lo que significa que la resolución de captchas no es una tecnología que se construya, es una operación de compras. Y conecta con el ecosistema del proxy de imagen, donde el captcha aparece como pieza de software casera ([[2026-1023-midjourney-proxy-ecosistema-de-aplicaciones-que-lo-consumen]]): aquí la misma pieza se compra como servicio con SLA.
Nota: la captura **no** publica la tarifa por captcha resuelto al trabajador, ni el mínimo de pago ni los países donde hay verificadores.


## Nota de extensión 2026-10-26
Este átomo afirma que "el precio del captcha es el precio de **mano de obra**, no de cómputo" y cierra con la ausencia que el vault no podía cerrar: "la captura **no** publica la tarifa por captcha resuelto al trabajador, ni el mínimo de pago ni los países donde hay verificadores". La captura de AntiCaptcha **cierra dos de esos tres huecos**: publica que "**100% of captchas are solved by human workers from around the world**" y que "an average worker earns about **$100 per month**, which is considered a good salary in developing countries such as **Bangladesh, Pakistan, and Venezuela** among others" ([[2026-1026-anticaptcha-100-por-ciento-de-trabajadores-humanos]]). Es la **primera retribución de trabajador del corpus**, y tiene un matiz de instrumento que hay que decir: es una cifra **del lado de la oferta**, no del cliente, y no es auditable —la captura no publica el número de trabajadores ni el volumen resuelto—, de modo que sirve para entender la naturaleza del coste, no para cotizarlo. Lo que **no** aporta es la cara de trabajador del portal: AntiCaptcha muestra una sola cara (cliente), mientras que la de 2Captcha tenía `userType=worker`. Y hay una diferencia de arquitectura de la que este átomo no dice nada porque no podía: 2Captcha es "AI-first" con fallback humano, AntiCaptcha es **100 % humano** ([[2026-1026-anticaptcha-sin-rama-ia-y-por-eso-precios-planos]]).


## Nota de extensión 2026-10-27
Este átomo documenta el modelo de **doble cara** de 2Captcha: por un lado, el cliente paga por el captcha resuelto; por otro, el trabajador cobra por resolverlo, y el margen del proveedor está en esa diferencia. La página `/pricing/data-annotation` del 2026-10-26 **añade una tercera venta sobre el mismo pool**: la página ofrece, en el menú oficial de precios, "**Scale smarter: Tap into a global workforce and automated workflows to handle massive data annotation projects with speed and precision**" y "**Maximize efficiency: Save time and money with flexible deadlines, customizable budgets**" ([[2026-1027-2captcha-data-annotation-sin-precio-publico-solo-contacto]]).

**La consecuencia es directa sobre este átomo: la fuerza laboral que 2Captcha usa como insumo de su producto barato es también un producto que se vende a precio de proyecto.** El átomo ya decía que el captcha es, en el fondo, **trabajo humano commoditizado** —y la página de anotación confirma que ese trabajo no es un efecto colateral del modelo, sino **una línea de negocio explícita con su propio apartado en la carta de precios**. La asimetría se vuelve más legible: el trabajo se compra al worker **por unidad a $0,5–$2,99 por 1000** y se revende al cliente final **por proyecto con presupuesto negociable**, sin cifra ni unidad. La diferencia entre el precio del input y el del output es exactamente el margen que este átomo ya había identificado, y ahora tiene un segundo mercado donde se aplica.

**Y hay un dato de encuadre que este átomo no tenía**: la página es una de las **siete pestañas** del menú de precios, y es una de las **dos que no publica ninguna cifra** ([[2026-1027-2captcha-menu-de-precios-con-7-lineas-y-dos-sin-cifra]]). Es decir, **la misma compañía que publica 48 tipos de captcha con precio cerrado por mil no publica el precio de su servicio de trabajo humano por proyecto**. La opacidad está donde está el margen, y el vault puede decirlo con dos capturas del mismo proveedor y el mismo día.

Nota de verificación: la captura **no** publica unidad, volumen mínimo, plazo, SLA ni ninguna cifra de la línea de anotación; el texto "customizable budgets" es la única mención económica y no es una cifra.
