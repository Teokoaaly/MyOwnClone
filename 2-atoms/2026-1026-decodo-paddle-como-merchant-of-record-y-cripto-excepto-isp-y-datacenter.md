---
id: 2026-1026-decodo-paddle-como-merchant-of-record-y-cripto-excepto-isp-y-datacenter
type: atom
certainty: solid
sources: [sources/2026-10-25-decodo-residential-pricing.md]
links: ["[[2026-1024-dataimpulse-metodos-de-pago-incluye-cripto]]", "[[2026-1023-lzt-topup-mastercard-comision-10]]", "[[2026-1024-brightdata-metodos-de-pago-y-verificacion-con-credito-extra]]"]
---

## Claim
El FAQ de Decodo enumera **siete métodos de pago** (tarjetas de crédito, PayPal, Alipay, Google Pay y Apple Pay; **"You can also pay with cryptocurrency for all products except ISP proxies and datacenter proxies (Pay per IP option)"**) y declara que **todas las órdenes se procesan a través de un revendedor externo**: "All orders are processed by our online reseller **Paddle – The complete payments, tax, and subscriptions solution for SaaS**, which is a **Merchant of Record** for these orders." La seguridad se declara como "Your information is protected by **256-bit SSL**".

## Why It Matters
Dos cosas nuevas en el corpus de proxy. La primera es que **el IVA no lo cobra el proveedor**: los ocho precios de la página están marcados "**+ VAT**" y el Merchant of Record es Paddle, no Decodo. Es decir, **el precio unitario que el vault puede citar es un precio sin impuesto**, y el impuesto se añade arriba en el checkout — lo que convierte cada comparación de $/GB entre proveedores en una comparación condicionalmente incompleta salvo que se declare el tratamiento fiscal.
La segunda es que **Decodo acepta criptomoneda con una exclusión explícita y verificable**: **no para ISP proxies ni para datacenter proxies (Pay per IP)**. Es una postura distinta de la de DataImpulse, donde el icono de cripto es la **única** señal y no hay cadena, ni moneda, ni dirección ([[2026-1024-dataimpulse-metodos-de-pago-incluye-cripto]]), y distinta también de lzt.market, donde el 10 % de comisión con Mastercard es la única comisión medida del sector ([[2026-1023-lzt-topup-mastercard-comision-10]]). Aquí **la restricción es de catálogo, no de pago**: se puede pagar en cripto lo que se consume como tráfico, y no lo que se consume como dirección IP dedicada —que es exactamente la partida que en el vault está ligada a la continuidad de identidad.

## [FRICTION]
> [[2026-1024-dataimpulse-metodos-de-pago-incluye-cripto]] concluye que "el pago en cripto describe el medio, no la postura de datos del proveedor" y que la ausencia de KYC o identidadPublished en el corpus de proxies es la regla.
> Este átomo lo matiza con un dato que esa lectura no tenía: **Decodo sí publica una regla de cripto, pero es de alcance de producto, no de identidad** — el cripto está excluido precisamente para las dos líneas de IP dedicada (ISP y datacenter pay-per-IP), que son las que ligan una identidad a una dirección. Es decir: **la frontera del cripto no es la privacidad del pago, es la continuidad de la identidad**.
> Ambas no pueden ser completamente correctas: o la aceptación de cripto es una señal neutral de método de pago, o el proveedor está segmentando su oferta de forma que **el activo más difícil de reasignar —la IP fija— es el que exige vía convencional**. Marcado para juicio humano, no auto-resuelto: la captura no publica condiciones de KYC, ni justificación de la exclusión, ni comisiones de ningún método.

## Nota de verificación
Frases transcritas literalmente. La captura **no** publica: qué criptomonedas concretas, si hay comisión por método de pago, ni el tipo de cambio o lajurisdicción fiscal que aplica al "+ VAT".
