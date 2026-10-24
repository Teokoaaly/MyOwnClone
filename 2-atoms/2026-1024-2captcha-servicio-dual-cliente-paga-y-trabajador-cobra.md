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
