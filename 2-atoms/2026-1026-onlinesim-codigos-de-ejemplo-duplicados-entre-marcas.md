---
id: 2026-1026-onlinesim-codigos-de-ejemplo-duplicados-entre-marcas
type: atom
certainty: solid
sources: [sources/2026-10-25-onlinesim-virtual-sms.md]
links: ["[[2026-1023-5sim-catalogo-servicios-precios-y-stock]]", "[[2026-1023-5sim-claim-500k-numeros-y-piso-0008]]", "[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]"]
---

## Claim
Los SMS de ejemplo del carrusel **repiten el mismo código entre marcas distintas**: AliExpress y Taobao muestran ambos "Verification Code: **561318**. Valid for 5 minutes"; Instagram y Facebook muestran ambos "Use **645 829** to verify your ... account". Además el texto bajo la etiqueta Tinder es el de otro servicio ("Your **OkCupid** code is 449940"), y el bloque entero **se repite**: WeChat (003835), Google (G-585019), LINE (493425) y Netflix (295206) aparecen dos veces con los mismos códigos. Es un carrusel estático, no tráfico real.

## Why It Matters
El carrusel es la **prueba de vida** que el proveedor ofrece en su home, y es un argumento de marketing, no evidencia: un mismo código no puede validar dos servicios a la vez, y un texto de OkCupid bajo la marca Tinder es un error de curaduría. La consecuencia metodológica para el vault es la misma que ya se registró con los contadores de 5sim replicados byte a byte en tres URL ([[2026-1023-5sim-catalogo-servicios-precios-y-stock]]): **el escaparate de un proveedor de números no es un dato de inventario ni de tasa de entrega** ([[2026-1023-5sim-claim-500k-numeros-y-piso-0008]]).
El vault ya tiene, en cambio, cifras de entrega **medidas** —65 % en una tabla y 56 % como techo en la página de OpenAI de 5sim ([[2026-1023-5sim-openai-tasa-entrega-65-de-100]], [[2026-1023-5sim-openai-tasa-entrega-techo-56]])— frente a las que ofrece OnlineSim, que es **cero**. En la jerarquía de evidencia del corpus, OnlineSim es el proveedor con menos dato verificable de los tres, no el más grande.
