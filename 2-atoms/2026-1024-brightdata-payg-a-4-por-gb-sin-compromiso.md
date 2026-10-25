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
