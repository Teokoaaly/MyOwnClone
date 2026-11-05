---
id: 2026-1026-decodo-reembolso-14-dias-con-limite-del-20-y-10-de-trafico
type: atom
certainty: solid
sources: [sources/2026-10-25-decodo-residential-pricing.md]
links: ["[[2026-1024-mullvad-garantia-de-reembolso-14-dias-excepto-efectivo-por-aml]]", "[[2026-1024-brightdata-prorrateo-por-dias-activos-en-el-mes-de-alta]]", "[[2026-1024-dataimpulse-payg-sin-suscripcion-ni-caducidad]]"]
---

## Claim
Decodo publica una **garantía de 14 días** ("14-day money-back") y, a diferencia del resto de proveedores de proxy del corpus, **publica también sus condiciones**. El FAQ acota el alcance: "**Only our self-service products have a refund option**". Enumera después seis requisitos acumulativos: (1) solo la **primera compra**; (2) **no haber usado la prueba gratuita de 3 días**; (3) solicitud **dentro de los 14 días naturales** desde la primera transacción; (4) **no haber consumido más del 20 % del tráfico** del plan residencial regular — **o más del 10 %** del plan Enterprise; (5) cuenta no suspendida por incumplimiento; (6) sin contracargo. Y el propio FAQ lo separa: la garantía de 14 días **no aplica** cuando se ha usado la prueba de 3 días.

## Why It Matters
Es la **política de reembolso más completa que el vault tiene registrada en todo el sector de proxy**, donde hasta ahora la única garantía comparable era la de Mullvad —que también es de 14 días pero **sin ninguna condición de uso**, solo la excepción del efectivo por AML ([[2026-1024-mullvad-garantia-de-reembolso-14-dias-excepto-efectivo-por-aml]]). Aquí el número "14 días" es **la misma cifra con un contrato completamente distinto**: el umbral de uso del 20 % es la condición que de verdad decide, porque un pipeline que consume proxy **usa tráfico**, y 20 % de 3 GB son 600 MB.
La diferencia con el modelo prepago ya medido es de fondo: DataImpulse declara "No expiry, no subscription" y **"7-day Refund Policy"** como característica, sin condiciones ([[2026-1024-dataimpulse-payg-sin-suscripcion-ni-caducidad]]); Bright Data, con compromiso mínimo de $499, no publica política de reembolso en absoluto y **cobra el compromiso íntegro por adelantado aunque no se use** ([[2026-1024-brightdata-prorrateo-por-dias-activos-en-el-mes-de-alta]]). Decodo es el único de los tres que publica **una condición de uso que acota el riesgo del comprador** — y es una condición que protege al proveedor, no al cliente.

## [FRICTION]
> [[2026-1024-mullvad-garantia-de-reembolso-14-dias-excepto-efectivo-por-aml]] afirma que "14-day money-back" es una garantía cuyo único límite publicado es la vía no reembolsable por AML, y lee ese conjunto como la contrapartida que hace coherente un servicio sin lock-in.
> Este átomo presiona esa lectura en un punto: **en el sector de proxy, "14-day money-back" significa lo contrario** — es una garantía **condicionada al uso**: solo la primera compra, sin prueba gratuita previa, y con un **techo de tráfico consumido (20 % o 10 %)**. Es decir, la misma etiqueta comercial cubre dos contratos incompatibles según el sector.
> Ambas no pueden ser completamente correctas: o "14 días de devolución" es una unidad interpretable de forma común entre proveedores, o es una etiqueta reutilizada con condiciones distintas y **el vault no puede citarla como garantía equivalente al comparar proveedores**. Marcado para juicio humano, no auto-resuelto: la captura no publica qué ocurre con el tráfico ya consumido ni con qué se devuelve el importe.

## Nota de verificación
Condiciones transcritas literalmente del FAQ. La captura **no** publica: plazo de resolución del reembolso, si el reembolso es total o parcial, ni el tratamiento del tráfico consumido dentro del umbral.


## Nota de extensión 2026-10-27
La página de precios de la Web Data API incluye entre las features de **todos** los planes la línea **"14-day money-back"**, y el FAQ de la home confirma que la API **no exige tarjeta** ("You can start using Web Data API with a free starter plan without a credit card. Sign up, test your requests, and upgrade when you need more capacity"). Es decir: **la línea de scraping hereda la etiqueta de garantía de la línea de proxy, pero las condiciones de esa garantía no se trasladan** — este átomo documenta que la garantía de proxies está condicionada a **primera compra, no haber usado la prueba de 3 días, 20 % del tráfico residencial o 10 % del Enterprise, cuenta no suspendida y sin contracargo**, condiciones pensadas para un consumo medido en gigabytes.

En la línea de scraping, donde la unidad es **crawl o página**, **ninguna de esas condiciones tiene equivalente**: ¿qué sería el "20 % del tráfico" de un plan cuyo límite son 9,9M páginas? La captura **no** publica las condiciones aplicables a la API, solo la etiqueta. El vault debe citar **"14-day money-back" como etiqueta sin condiciones para la API**, y no extenderle por analogía las de la línea residencial. Ver [[2026-1027-decodo-plan-gratuito-de-la-web-data-api-con-5-de-credito-y-10k-solicitudes-sin-tarjeta]].
