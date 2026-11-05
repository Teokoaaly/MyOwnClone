---
id: 2026-1024-2captcha-arkose-funcaptcha-50-dolares-por-1000
type: atom
certainty: solid
sources: [sources/2026-10-23-2captcha-solver.md]
links: ["[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar]]", "[[2026-1023-midjourney-proxy-edicion-plus-ampliada]]"]
---
## Claim
El tipo **más caro y más lento** del catálogo es Arkose Labs captcha (FunCaptcha): precio **$1.45 — $50 por 1000** y velocidad de resolución **16 sec**. La captura lo explica así: se extrae "un set of necessary parameters from the page of its placement" y la respuesta vuelve "in the form of a set of already other parameters" (no es un token único como en reCAPTCHA).

## Why It Matters
FunCaptcha rompe el patrón del resto del catálogo en las dos dimensiones que importan: **precio** (hasta 33 veces el de un reCAPTCHA v2) y **latencia** (16 segundos frente a 1-2). Y mecánicamente es distinto: no devuelve un token, devuelve un conjunto de parámetros que hay que inyectar en los campos correctos. Es decir, requiere **más trabajo de integración**, no solo más dinero.
Para el vault esto fija el coste real de la elusión cuando el proveedor usa Arkose: el que vende proxies sin API oficial ([[2026-1023-midjourney-proxy-edicion-plus-ampliada]]) y tiene que automaticar la verificación de popups está exactamente en esta categoría de coste. Si un producto del vault quisiera atravesar FunCaptcha en volumen, el presupuesto por mil no es comparable con el de reCAPTCHA.
Nota: la captura **no** explica por qué el rango llega a $50 (¿variación por dificultad, por sitio, por tipo de cuenta?) ni si ese techo es alcanzable en un volumen real.


## Nota de extensión 2026-10-26
Este átomo llama a FunCaptcha "el tipo **más caro y más lento** del catálogo" con "**$1.45 — $50 por 1000**" y "**16 sec**", y su nota de cierre confiesa que "la captura **no** explica por qué el rango llega a $50 (¿variación por dificultad, por sitio, por tipo de cuenta?)". La captura de AntiCaptcha no solo deja esa pregunta abierta: **ofrece una contra-cifra**. AntiCaptcha publica **Arkose Labs a $3 por 1000 y 5 s**, precio único y cerrado ([[2026-1026-anticaptcha-arkose-labs-a-3-dolares-por-1000]]). Con eso, el $50 deja de ser una cota del tipo Arkose y pasa a ser **una cota del catálogo de 2Captcha**, y el "33×" que este átomo usa como medida de cuánto encarece Arkose se convierte en una medida de cuánto encarece **ese proveedor**. La parte mecánica del átomo —que FunCaptcha devuelve un conjunto de parámetros en vez de un token, y que eso exige más trabajo de integración— **no se ve afectada**: el tipo de tarea sigue siendo `FunCaptchaTaskProxyless` en ambos catálogos. Lo que cambia es la lectura del coste: elegir proveedor **sí** mueve el precio por mil de Arkose en un factor de hasta 16,7×, de modo que la "elección del tipo de captcha que aparece en el destino" que el átomo propone como criterio de selección tiene que ir acompañada de "y del proveedor que lo resuelve" ([[2026-1026-anticaptcha-sin-rama-ia-y-por-eso-precios-planos]]).


## Nota de extensión 2026-10-27
La captura del 2026-10-26 confirma el precio (**$1.45 — $50 por 1000**) y la capacidad (**578** libres por minuto) de FunCaptcha, pero **cambia su latencia de 16 sec a 18 sec** en tres días. Ver [[2026-1027-2captcha-cuatro-velocidades-cambiaron-en-tres-dias]].

Con la tabla de 48 filas, el assertion central de este átomo —que FunCaptcha es "el tipo **más caro y más lento** del catálogo"— **deja de ser cierto en su parte de latencia**: el tipo más lento es **KeyCAPTCHA a 37 sec**, y le siguen Cutcaptcha y Prosopo Procaptcha a 24 sec y Lemin a 20 sec. Ver [[2026-1027-2captcha-keycaptcha-37-segundos-como-nuevo-techo-de-latencia]]. La parte de **precio** se mantiene intacta: **$50 sigue siendo el techo único del catálogo**, con un factor ×34 sobre el precio de $1.45 de los tipos habituales — y ahora con un dato adicional: **el rango $1.45 — $50 sigue siendo el único rango abierto del catálogo** salvo el de reCAPTCHA v2 y Enterprise ($1 — $2.99), de modo que **FunCaptcha es el único tipo cuyo precio no es una cifra cerrada ni una banda identificada por un criterio**.

La lectura de este átomo sobre el trabajo de integración ("no devuelve un token, devuelve un conjunto de parámetros que hay que inyectar") **no se ve afectada** por la captura, que no publica la mecánica. Y la conclusión sobre el coste real de la elusión cuando el proveedor usa Arkose **cambia de signo en su parte de concurrencia**: **FunCaptcha está en 18 sec y 578/min**, de modo que su techo de capacidad es de **~1.927 unidades/hora (~46.240/día)** — **más del doble que los ~19.488/día de ALTCHA** (203/min, 15 sec), porque la capacidad libre de FunCaptcha es casi tres veces mayor y su latencia solo un 20 % peor. Es decir, **en la partida más cara del catálogo el límite no es la concurrencia sino el precio**: el techo de volumen de FunCaptcha es holgado frente al de los tipos lentos baratos, y quien compra a $50/1000 no está pagando una escasez de capacidad.
