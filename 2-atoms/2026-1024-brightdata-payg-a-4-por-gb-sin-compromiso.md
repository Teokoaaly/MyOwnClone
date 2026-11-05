---
id: 2026-1024-brightdata-payg-a-4-por-gb-sin-compromiso
type: atom
certainty: solid
sources: [sources/2026-10-24-brightdata-proxy-pricing.md]
links: ["[[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]", "[[2026-1024-brightdata-cupon-50-off-y-match-del-primer-deposito]]", "[[2026-1024-brightdata-escalera-de-volumen-141-a-798-gb]]"]
---

## Claim
El plan **PAY AS YOU GO** de Bright Data se publica a **$8/GB de precio de lista y $4.00/GB con el 50 % de descuento activo**, con la coletilla **"No commitment"** (literal de la página) y un botón de "Start free trial". Es el único punto de entrada sin compromiso mensual de la página: los otros tres planes son suscripciones con GB incluido facturadas cada mes.

## Why It Matters
Es el dato de entrada más caro de todo lo que el vault tiene registrado sobre proxies: **$4/GB efectivo frente a los $1/GB residencial y $0,50/GB datacenter de DataImpulse** ([[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]) — **4× el residencial y 8× el datacenter** del otro proveedor ya medido. Con la aritmética de sesión que el thread ya tiene establecida (un alta con login y navegación consume el número de sesiones sticky, no 1 GB), 30 MB por sesión en Bright Data son ~$0,12 frente a ~$0,03 en DataImpulse: poco en términos absolutos, pero **el multiplicador se paga en cada sesión y en cada reintento**.
La diferencia relevante no es el precio sino el contrato: Bright Data separa explícitamente la compra sin compromiso de la suscripción con mínimo mensual, de modo que el "coste del proxy" del vault tiene aquí dos formas distintas y no una sola ([[2026-1024-brightdata-escalera-de-volumen-141-a-798-gb]]).

## [FRICTION]
> [[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]] (escrita el 2026-10-24) afirma que el proxy es "el único insumo cuyo coste depende de un volumen que el proveedor controla" y sitúa el precio de entrada en $1/GB residencial.
> Este átomo presiona ese corte porque con un segundo proveedor medido la magnitud del insumo **se multiplica por 4× o 8× según el pool**, no por un factor constante: un modelo de coste que fije "el proxy cuesta $1/GB" describe a DataImpulse, no al sector. El orden "correo ≪ captcha ≪ proxy ≪ SMS" se mantiene, pero la **magnitud del proxy se vuelve una variable de proveedor, no de mercado**.
> Ambas no pueden ser completamente correctas: o el vault trata el $/GB como parámetro del proveedor que se cotiza cada vez, o la aritmética de coste por alta que se derive de él es específica de un solo proveedor. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
Precios transcritos literalmente de la primera tarjeta de la página de precios. La captura **no** publica: si el "50 % OFF" es permanente o una promoción con caducidad, ni el precio de lista real sin descuento aplicado.


## Nota de extensión 2026-10-26
La documentación de billing del 2026-10-25 confirma que el "No commitment" del PAYG es **el único régimen compatible con el free tier** —el free tier "is available to all new accounts" pero "the following account types are **not** eligible: accounts on custom PAYG pricing plans, accounts on pre-commit (subscription) plans"— y añade que **"There is no minimum commitment. You stay on PAYG and only pay for what you use"**, con un **tope duro** (*"never a surprise bill"*) en el wallet prepago. Esto refuerza la lectura de este átomo en un punto: el PAYG de $4/GB no es solo "el más barato por GB", es **el único plan que conserva los 5.000 créditos gratuitos mensuales** (~$7,50/mes de valor), de modo que el coste real de los primeros meses es **$0 en la capa de API**. La comparación con el $4/GB de Decodo queda además con un matiz nuevo: allí el PAYG exige Wallet recargado y **excluye la suscripción mensual** ([[2026-1026-decodo-payg-a-4-por-gb-solo-con-wallet-y-un-gb-a-la-vez]]); aquí el PAYG es el que **no tiene** compromiso y el único que entra en el free tier. Ver [[2026-1026-brightdata-upgrade-a-pre-commit-detiene-los-creditos-gratis]] y [[2026-1026-brightdata-wallet-prepagado-con-tope-duro-y-sin-factura-sobrevenida]].


## Nota de extensión 2026-10-26
El dato de "$4/GB" de este átomo deja de ser una rareza de catálogo de un solo proveedor: la captura de Decodo del 2026-10-25 (`sources/2026-10-25-decodo-residential-pricing.md`) publica **el mismo $4/GB en su plan Pay As You Go** ("Total: $4 + VAT"), es decir **dos proveedores independientes con el mismo precio de entrada flexible**. Pero la comparación no es simétrica: el PAYG de Bright Data es un plan "No commitment" sin saldo previo, mientras que el de Decodo **solo funciona con Wallet recargado**, se compra **en tramos de 1 GB** ("you can purchase only one GB at a time") y **excluye la suscripción mensual** ("you can't have a monthly subscription plan and Pay As You Go simultaneously"). Ver [[2026-1026-decodo-payg-a-4-por-gb-solo-con-wallet-y-un-gb-a-la-vez]]. Consecuencia para la lectura de este átomo: "$4/GB es el precio de la entrada flexible del sector" es una lectura con más respaldo que antes, pero **"$4/GB es la compra flexible" no lo es**, porque el número agrupa dos contratos incompatibles.
