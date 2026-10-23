---
id: 2026-1023-lzt-topup-mastercard-comision-10
type: atom
certainty: solid
sources: [sources/2026-10-22-lzt-market-home.md]
links: ["[[2026-1023-5sim-claim-500k-numeros-y-piso-0008]]", "[[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]", "[[2026-1023-lzt-captura-parcial-sin-precios-ni-stock]]"]
---

## Claim
lzt.market anuncia una **nueva opción de pago**: el banner "New Payment Option" declara literalmente "You can now top up your balance using MasterCard with 10% comission" (con la errata en la propia página) y enlaza a "Top Up Now" (`/market/payment/balance/deposit`). Es la **única cifra económica** que la captura de lzt.market publica: no hay precios de cuentas, pero sí hay un número de coste explícito, y es del 10 % sobre el saldo recargado.

## Why It Matters
La comisión de recarga no es un detalle de checkout: se aplica al saldo, así que multiplica el precio efectivo de cada unidad comprada con ese saldo. Sobre el suelo de precio del sector esto no es ruido: un número de $0,008 con un 10 % de comisión sobre el saldo recarga a $0,0088, y a escala de miles de verificaciones la comisión se convierte en una partida propia del modelo de coste marginal del alta ([[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]). El dato es además comparable: 5sim afirma en su home "Add funds to your 5SIM balance while spending as little as you can on commission fees" **sin publicar ninguna cifra** ([[2026-1023-5sim-claim-500k-numeros-y-piso-0008]]), mientras lzt.market sí publica el 10 %. "Comisión baja" no es una categoría homogénea entre proveedores: es un número, y aquí es 10 %.
Para el producto del vault la lectura es de coste de entrada al canal verificado: recargar con tarjeta es un pasivo de caja del comprador, no del proveedor de cuentas, y por tanto una barrera de entrada en la parte del mercado que compite por la identidad verificada ([[2026-1023-lzt-captura-parcial-sin-precios-ni-stock]]).

## [FRICTION]
> [[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]] (escrita hoy, a partir del CSV de precios de 5sim) afirma que añadir SMS como canal de verificación es "aritméticamente viable a escala" y lo lee como un **coste marginal** frente al modelo de costes por categoría, con un coste por alta entre $0.1026 y $8.8897 ([[2026-1023-5sim-piso-de-precio-telegram-01026-usd]]).
> Este átomo presiona ese cálculo porque el coste de una verificación no es solo el precio del número: hay una **capa de comisión de recarga** que multiplica todo lo comprado con ese saldo, y en el competidor directamente observable es del **10 %**. Con el suelo de $0.1026, un 10 % de comisión son $0.0103 por alta; con el claim de $0.008 del sector son $0.0008. La conclusión "aritméticamente viable" no cambia, pero el modelo del vault no tiene partida de comisión de recarga, y 5sim solo publica "as little as you can on commission fees" sin cifra ([[2026-1023-5sim-claim-500k-numeros-y-piso-0008]]).
> Ambas no pueden ser completamente correctas: o la comisión de recarga del vault es marginal porque se compra en lote con otros insumos, o falta una cuarta categoría de coste en el modelo de [[2026-1022-costes-por-categoria-tenant]]. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
El texto del banner y el destino del enlace están transcritos literalmente. La captura **no** publica: importe mínimo de recarga, otros métodos de pago, si el 10 % es el único cargo o uno entre varios, ni tipos de cambio.
