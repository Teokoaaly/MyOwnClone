---
id: 2026-1026-brightdata-proxies-excluidos-con-2-dolares-de-prueba-y-5-de-bonus
type: atom
certainty: solid
sources: [sources/2026-10-25-brightdata-free-tier.md]
links: ["[[2026-1024-brightdata-metodos-de-pago-y-verificacion-con-credito-extra]]", "[[2026-1026-brightdata-pool-unico-de-creditos-cinco-productos]]", "[[2026-1024-brightdata-kyc-para-residencial-y-movil-pero-web-unlocker-no]]"]
---

## Claim
Los productos proxy **quedan fuera del free tier**: *"Proxy products (Datacenter, ISP and Residential proxies) are **not** included in the monthly free credits. New accounts receive a separate one-time **$2 trial credit** (valid **7 days**) to test the proxy products, plus an additional **$5 bonus** upon adding a payment method (valid **30 days**)."* Los proxies son **la única excepción** al resto de productos, que sí entran en el pool de 5.000 créditos.

## Why It Matters
Es el dato que separa las dos capas del coste de scraping: **la elusión (Web Unlocker, SERP, Web Scraper, Scraper Studio, Browser API) tiene cuota mensual gratis; la red (Datacenter, ISP, Residential) solo tiene una prueba de $2 con caducidad de 7 días**. Es exactamente la separación que el vault viene registrando en la otra dirección — el pool con mejor tasa de supervivencia (residencial y móvil) está detrás de un KYC con videollamada ([[2026-1024-brightdata-kyc-para-residencial-y-movil-pero-web-unlocker-no]])— pero aquí el dato nuevo es **económico y temporal**: la prueba de red es de **$2 y caduca a los 7 días**, mientras que el bonus de $5 por añadir método de pago dura **30 días**.
Los dos importes son minúsculos y su caducidad es el dato operativo: **una prueba de $2 para 7 días no permite medir el comportamiento del proxy en el tiempo**, que es justamente lo que un pipeline de altas necesita (supervivencia de sesión, reintentos, coste real por GB con cabeceras contadas, [[2026-1024-brightdata-ancho-de-banda-contado-en-dos-sentidos-con-cabeceras]]). Es un cupón de *entrada*, no de *medición*.
Y conecta con el átomo de métodos de pago del 2026-10-24: la página de precios describía un **cargo único de autorización por operación** como verificación, con créditos extra como recompensa ([[2026-1024-brightdata-metodos-de-pago-y-verificacion-con-credito-extra]]); aquí el mismo gesto —añadir método de pago— produce un **$5 de bonus con 30 días de validez**, lo que lo convierte en un incentivo con caducidad, no en un reembolso.

## [FRICTION]
> [[2026-1024-brightdata-metodos-de-pago-y-verificacion-con-credito-extra]] (escrita el 2026-10-24) afirma que Bright Data hace *"a one-time per-authorization charge"* cuyo propósito es comprobar la tarjeta y que **el cliente recibe créditos extra** usables para cualquier consumo de proxy.
> Este átomo presiona esa lectura en un punto: según la documentación de free tier, **añadir un método de pago da un $5 en bonus con 30 días de validez**, y **no se paga nada** —*"Adding a credit card is a verification step only. You will not be charged unless your free credits are exhausted and you have funds deposited in your account."* Es decir, o el bonus de $5 es el mismo mecanismo de "crédito extra por verificación" descrito en la página de precios, o son **dos mecanismos distintos** —un cargo de autorización por operación en la página de precios y un bonus de saldo de un solo uso aquí— que la vault está tratando como uno.
> Ambas no pueden ser completamente correctas: o "añadir método de pago" es un procedimiento único con un único incentivo, o el proveedor ofrece incentivos distintos según por dónde se entre. Marcado para juicio humano, no auto-resuelto: la captura **no** publica el importe de los "créditos extra" por verificación ni sus condiciones.

## Nota de verificación
Textos transcritos literalmente. La captura **no** publica: si el bonus de $5 se renueva mensualmente mientras la cuenta no esté funded, ni si el crédito de $2 y el de $5 son acumulables entre sí.
