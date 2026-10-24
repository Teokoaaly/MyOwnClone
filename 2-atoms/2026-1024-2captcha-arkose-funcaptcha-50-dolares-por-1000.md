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
