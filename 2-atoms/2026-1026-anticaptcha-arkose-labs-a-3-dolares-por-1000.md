---
id: 2026-1026-anticaptcha-arkose-labs-a-3-dolares-por-1000
type: atom
certainty: solid
sources: [sources/2026-10-25-anti-captcha-pricing.md]
links: ["[[2026-1024-2captcha-arkose-funcaptcha-50-dolares-por-1000]]", "[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1026-anticaptcha-trece-tipos-con-precio-por-1000]]"]
---

## Claim
AntiCaptcha publica **Arkose Labs a $3 por 1000**, precio único y cerrado, con velocidad de resolución de **5 s**. La tarea es `FunCaptchaTaskProxyless` (`/apidoc/task-types/FunCaptchaTaskProxyless`).

## Why It Matters
Es una **cifra de mercado para Arkose distinta de la del vault**: 2Captcha publica FunCaptcha en **$1.45 - $50 por 1000** con 16 sec ([[2026-1024-2captcha-arkose-funcaptcha-50-dolares-por-1000]]), y AntiCaptcha lo vende a **$3**, sin rango, a **5 s**. Es decir: el mismo tipo de captcha —que en 2Captcha era el más caro y el más lento del catálogo— es aquí un tipo **de precio medio y de latencia uniforme**, y el techo de $50 no aparece en ningún proveedor del corpus.
La consecuencia operativa es que **el coste y la latencia de Arkose dependen del proveedor, no del tipo de captcha**: si el destino usa Arkose, la elección de solver es una decisión de precio con un rango observado de 16,7× entre los dos proveedores del vault ($3 vs $50).

## [FRICTION]
> [[2026-1024-2captcha-arkose-funcaptcha-50-dolares-por-1000]] afirma que "El tipo **más caro y más lento** del catálogo es Arkose Labs captcha (FunCaptcha): precio **$1.45 — $50 por 1000** y velocidad de resolución **16 sec**", y el átomo de precios ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]) usa ese $50 como techo del mercado de elusión ("un FunCaptcha puede llegar a $50 por mil") y calcula sobre él un factor de dispersión de 33× frente a reCAPTCHA v2.
> Este átomo presiona eso en dos puntos. (i) El techo de $50 **no es una propiedad del tipo Arkose**: el mismo tipo se compra a $3 en otro proveedor, de modo que el "33×" que el vault usa como medida de la dispersión del mercado es en realidad una medida de la dispersión **de un catálogo**, no del mercado. (ii) El argumento económico del átomo viejo —"FunCaptcha rompe el patrón en precio y latencia porque requiere más trabajo de integración"— no se sostiene si hay un proveedor que lo entrega a precio medio y latencia uniforme: el trabajo de integración adicional (devolver parámetros en vez de token) es **mecánico y no depende del proveedor**, mientras que el $50 sí lo es.
> Ambas no pueden ser completamente correctas a la vez: o el $50 es un rasgo estructural del tipo Arkose, o es un rasgo del proveedor que lo vende. Marcado para juicio humano, no auto-resuelto: la captura de 2Captcha no explica por qué su rango llega a $50 (¿variación por dificultad, por sitio, por tipo de cuenta?), así que la comparación no puede cerrarse.
