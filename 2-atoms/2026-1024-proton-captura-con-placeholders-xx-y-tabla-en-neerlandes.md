---
id: 2026-1024-proton-captura-con-placeholders-xx-y-tabla-en-neerlandes
type: atom
certainty: solid
sources: [sources/2026-10-24-protonvpn-pricing.md]
links: ["[[2026-1024-protonvpn-plus-3-49-al-mes-65-de-descuento]]", "[[2026-1024-proton-plan-gratuito-1-dispositivo-y-10-paises-al-azar]]", "[[2026-1024-evoxt-captura-sin-tabla-de-precios-ni-specs]]"]
---

## Claim
La captura de la página de precios de Proton **no está completamente renderizada**. Contiene marcadores de plantilla sin sustituir: el modal de venta says "**Get VPN Plus for only $XX.XX**", "Save **XX%** off our premium plan" y "$XX.XX for the first month. Renews at $XX.XX"; la FAQ de descuentos repite el patrón ("up to a XX% discount on the monthly price", tres veces). Además, el bloque de la tabla "Compare plans" aparece **traducido al neerlandés** ("Neem Proton Free", "1 maand / 1 jaar / 2 jaar", "Neem VPN Plus", "voor de eerste maand"), con el interruptor de divisa en CHF/EUR/USD.

## Why It Matters
Es una advertencia de **calidad de fuente** del mismo tipo que ya registró el vault con Evoxt y NotLetters: hay que saber **qué parte de la página falta**. Consecuencias concretas y verificables: (a) **los porcentajes de descuento de la FAQ no son publicables** —la página no dice cuánto descuenta el plan de 1 año ni el de 1 mes, solo el de 2 años (65 %) y el de Unlimited (38 %), que sí aparecen en las tarjetas; (b) la **traducción al neerlandés filtrada en la tabla indica que la página es multiidioma y que el renderizado es dinámico**, lo que significa que los precios de 1 mes y 1 año probablemente no se capturaron y **la periodicidad completa del catálogo VPN del vault queda sin documentar**; (c) el modal de "$XX.XX for the first month" sugiere que **existe una oferta de primer mes a precio de un dólar** —la URL del enlace lleva `coupon=VPNPLUSFREE2024` y `ref=free-plan-upsell-modal-1-usd`— pero **la cifra no es verificable en esta captura** y por tanto no se ha afirmado en ningún átomo.

## [FRICTION]
> [[2026-1024-protonvpn-el-descuento-caduza-y-la-renovacion-sube-a-6-99]] afirma el mecanismo de renovación de VPN Plus sobre la base de la tarjeta de plan ("then renews at $83.88 every 12 months"). Esta nota no lo contradice, pero **acota su alcance**: la frase viene de la tarjeta del plan de 24 meses y la página ofrece además un modal de 1 mes cuyo precio es un placeholder. La cifra de $6,99/mes en la renovación es sólida **para el plan de 24 meses**; no hay dato para la renovación de un eventual plan de 1 mes o 1 año.
