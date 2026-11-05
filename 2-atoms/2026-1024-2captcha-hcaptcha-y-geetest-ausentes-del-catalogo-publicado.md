---
id: 2026-1024-2captcha-hcaptcha-y-geetest-ausentes-del-catalogo-publicado
type: atom
certainty: solid
sources: [sources/2026-10-23-2captcha-solver.md]
links: ["[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1024-2captcha-capacidad-libre-por-minuto-como-proxy-de-cola]]", "[[2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar]]"]
---
## Claim
La lista "Supported captchas" de la captura enumera **diez tipos**: reCAPTCHA v2, reCAPTCHA v2 Callback, reCAPTCHA v2 Invisible, Image Captcha, Cloudflare Turnstile, reCAPTCHA v3, reCAPTCHA Enterprise, Arkose Labs captcha (FunCaptcha), Amazon captcha y ALTCHA. **No aparecen hCaptcha ni Geetest** en ninguna parte de la página, y la tabla de precios solo muestra **ocho filas** (las dos ausentes son las variantes Callback e Invisible, que sí figuran en la lista de soportados) tras un botón "Show more".

## Why It Matters
Dos consecuencias prácticas para el vault. Primera: **la captura es parcial** — hay un "Show more" sin expandir, así que el catálogo real de precios y capacidades es al menos más grande que ocho filas; el vault solo puede atomizar lo visible. Segunda: **hCaptcha y Geetest no están en el escaparate**, lo que no significa que no se resuelvan (pueden estar tras el "Show more" o en páginas de producto no capturadas), pero sí que **no se pueden comprar como producto de catálogo publicado**.
Esto importa al elegir proveedor: si un destino de scraping usa hCaptcha, el coste y la latencia de esa resolución no se pueden cotizar con esta fuente. Para los tipos visibles, en cambio, la dispersión es enorme: de $0.5 a $50 por mil ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]), de 1 a 17 segundos ([[2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar]]), de 203 a 12.000 de capacidad por minuto ([[2026-1024-2captcha-capacidad-libre-por-minuto-como-proxy-de-cola]]).
Nota: la captura **no** permite afirmar que hCaptcha o Geetest no se soporten; solo que no constan en la página capturada.


## Nota de extensión 2026-10-26
Este átomo registra que "hCaptcha y Geetest **no aparecen en ninguna parte** de la página" y concluye que "**no se pueden comprar como producto de catálogo publicado**", con la cautela explícita de que "la captura **no** permite afirmar que hCaptcha o Geetest no se soporten; solo que no constan en la página capturada". La captura de AntiCaptcha **resuelve la mitad de esa laguna**: AntiCaptcha publica **GeeTest a $1.8 por 1000**, con 5 s y tarea `GeeTestTaskProxyless`, como fila de catálogo con precio cerrado ([[2026-1026-anticaptcha-geetest-a-1-80-como-catalogo-publicado]]). La observación original del átomo sigue siendo literalmente cierta —la página de 2Captcha no lo mostraba— pero la **conclusión operativa que el vault extrapuso queda desmentida**: Geetest **sí es cotizable** con una cifra de lista, de modo que el vault puede dejar de tratarlo como línea no cotizable y añadirlo a la fila "captcha" de la tabla de coste por insumo. El límite correcto no es "no se puede cotizar", sino "**no se puede cotizar con la captura de 2Captcha**". Y el hueco que **sí** queda abierto es **hCaptcha**: ninguno de los dos proveedores del corpus lo publica, lo cual sí es una ausencia del corpus —aunque, con dos capturas, tampoco es un inventario.


## Nota de extensión 2026-10-26
La captura del 2026-10-25 de `https://www.capsolver.com/` **reduce el alcance de este átomo a un solo tipo**: **Geetest sí es cotizable**, a **$1.2 por 1000** con latencia **< 5S**, en el catálogo publicado de CapSolver ([[2026-1026-capsolver-geetest-v3-v4-y-aws-waf-tipos-que-el-catalogo-de-2captcha-no-publica]]). Lo que la captura de 2Captcha sigue sosteniendo es que, **con esa fuente**, Geetest no aparecía ni en la lista de "Supported captchas" ni en la tabla de precios.

**La corrección necesaria es de redacción, no de hecho.** La formulación vigente "hCaptcha y Geetest no se pueden comprar como producto de catálogo publicado" es **demasiado amplia** y debe pasar a "no se pueden comprar **como producto de catálogo publicado en la captura de 2Captcha**". La lección que este átomo extraía —que la no cotizabilidad de un tipo es una propiedad del catálogo, no del tipo— **sale reforzada**, no debilitada: Geetest cuesta en CapSolver ($1.2) **menos** que la única fila comparable de 2Captcha ("Amazon captcha" a $1.45), y aun así era incotizable con esa fuente.
El tipo que **sigue sin cotizar en todo el corpus** —2Captcha, AntiCaptcha y CapSolver— es **hCaptcha**: no aparece en ninguno de los tres catálogos publicados ([[2026-1026-anticaptcha-trece-tipos-con-precio-por-1000]], [[2026-1026-capsolver-nueve-tipos-con-precio-y-latencia]]). CapSolver sí añade **AWS WAF a $2.0/1k** (< 3S), un tipo que 2Captcha no listaba con ese nombre.


## Nota de extensión 2026-10-27
La captura del 2026-10-26 resuelve **la mitad de este átomo**: **GeeTest captcha SÍ aparece en el catálogo publicado de 2Captcha**, con precio **$2.99 por 1000**, **4 sec** y **3.765** libres por minuto, con página de producto `/p/geetest` y demo en `/demo/geetest`. Ver [[2026-1027-2captcha-geetest-a-2-99-con-3765-de-capacidad]]. La conclusión original ("**no se pueden comprar como producto de catálogo publicado**") queda desmentida en su mitad de Geetest y debe reformularse como "no se pueden comprar **como producto de catálogo publicado en la captura del 2026-10-23**".

El patrón se confirma con el resto del corpus y hay que dejarlo escrito: **Geetest queda disponible en tres proveedores con tres precios —$1.2 en CapSolver (< 5S), $1.8 en AntiCaptcha (5 s) y $2.99 en 2Captcha (4 sec)—**, un factor ×2,5 entre extremos y con la particularidad de que **2Captcha es el más caro y el único de los tres con una latencia cerrada por debajo de 5 s**, lo que refuerza la conclusión ya registrada en el vault de que **precio y latencia no están correlacionados dentro de un mismo catálogo**.

La otra mitad del átomo **sigue en pie y se refuerza**: **hCaptcha no aparece en ninguna de las 48 filas**, de modo que, con tres catálogos medidos (2Captcha 48 tipos, AntiCaptcha 13, CapSolver 9), **hCaptcha es una ausencia verificada sobre tres fuentes**, no un simple hueco de captura. La frase "la captura **no** permite afirmar que hCaptcha o Geetest no se soporten" del átomo original **queda definitivamente superada para Geetest** (ahora se publica con precio) **y se mantiene literal para hCaptcha** (no hay precio ni mención en ningún catálogo del corpus).

Nota de método: la captura **no fecha** la incorporación de Geetest al catálogo —podría haber estado siempre detrás del "Show more"—, de modo que lo verificable es que **ahora es visible y cotizable**, no que sea una incorporación reciente.
