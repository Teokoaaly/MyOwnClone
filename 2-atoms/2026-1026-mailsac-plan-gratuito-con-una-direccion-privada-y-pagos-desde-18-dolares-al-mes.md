---
id: 2026-1026-mailsac-plan-gratuito-con-una-direccion-privada-y-pagos-desde-18-dolares-al-mes
type: atom
certainty: solid
sources: [sources/2026-10-25-mailsac-test-email.md]
links: ["[[2026-1024-notletters-precio-005-rubles-por-correo-y-contadores-de-escala]]", "[[2026-1026-emailondeck-gratis-con-paso-pro-sin-cifras]]", "[[2026-1023-priceai-channels-correo-y-jianma-a-centimos-como-insumo-de-alta]]"]
---

## Claim
La única cifra de precio de la captura es un **piso de suscripción**: "the free plan includes one private address, and **paid plans from $18 a month** add custom test domains that only your team can read". El plan gratuito —"create a free account: it includes an API key and one private address"— no publica ningún precio, ninguna cifra de buzones, ni ningún límite de retención o de volumen. La página de precios (`mailsac.com/pricing`) está enlazada desde la home ("View Pricing") pero **no ha sido visitada**: la captura no contiene la tabla de planes, ni los nombres de los tiers, ni el número de buzones privados incluido en cada plan.

## Why It Matters
Es el **tercer modelo de precio del sector de correo** que el vault puede contrastar, y el que más se aleja de la tabla de coste por insumo de la §7 del thread:

| Proveedor | Unidad de compra | Cifra |
|---|---|---|
| NotLetters | por correo | **0.05 ₽** ([[2026-1024-notletters-precio-005-rubles-por-correo-y-contadores-de-escala]]) |
| 卡网 PriceAI | por buzón revendido | **¥0.02 – ¥1.24** ([[2026-1023-priceai-channels-correo-y-jianma-a-centimos-como-insumo-de-alta]]) |
| EmailOnDeck | **gratis**, sin cifras | ([[2026-1026-emailondeck-gratis-con-paso-pro-sin-cifras]]) |
| **MailS.ac** | **por suscripción de equipo, desde $18/mes** | este átomo |

La diferencia no es de magnitud sino de **estructura**: MailS.ac no vende buzones, vende **acceso de equipo a dominios de prueba propios**. Para el vault esto significa que un correo QA con dominio propio no tiene precio unitario sino **coste fijo recurrente**, lo que es incompatible con la forma del modelo de coste por alta que el thread construye en la §7 (donde el correo es la partida más barata y marginal). Es también el patrón que el thread ya vio en el proxy móvil de IPRoyal —coste fijo recurrente en lugar de marginal ([[2026-1024-iproyal-movil-117-al-mes-y-45m-de-ips]])— aplicado ahora al correo.

## [FRICTION]
> [[2026-1024-notletters-precio-005-rubles-por-correo-y-contadores-de-escala]] fija **0.05 ₽ por correo** como la cifra que "fija un precio de referencia para el buzón de registro" y sostiene que el correo queda por debajo del suelo medido del SMS ($0.1026).
> Este átomo presiona esa lectura en un punto: **ese 0.05 ₽ no es un precio de referencia del sector, sino el precio de un canal con una unidad distinta**. MailS.ac, del mismo sector, cotiza **por suscripción de equipo desde $18/mes** y su producto es el dominio de prueba privado, no el buzón anónimo. Es decir, hay al menos **tres unidades de compra distintas** en el mismo sector —correo, buzón revendido y suscripción de equipo— y "el precio del correo" no es una magnitud única sino tres, una de ellas **recurrente**.
> Ambas no pueden ser completamente correctas: o el 0.05 ₽ es el suelo real del sector porque el resto de los modos (gratis, suscripción) son marginales para el caso de uso del vault —el registro masivo—, o entonces la fila "correo de registro" de la tabla de coste del thread está mezclando unidades y necesita separarlas. Marcado para juicio humano, no auto-resuelto: la captura no publica la tabla de planes de MailS.ac, así que no se puede comparar el coste por buzón efectivo de la suscripción.
