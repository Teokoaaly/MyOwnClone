---
id: 2026-1026-anticaptcha-sin-rama-ia-y-por-eso-precios-planos
type: atom
certainty: tentative
sources: [sources/2026-10-25-anti-captcha-pricing.md]
links: ["[[2026-1024-2captcha-ai-primero-con-fallback-a-trabajadores-humanos]]", "[[2026-1026-anticaptcha-100-por-ciento-de-trabajadores-humanos]]", "[[2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar]]"]
---

## Claim
La arquitectura declarada de AntiCaptcha es **"100% of captchas are solved by human workers from around the world"**, sin ninguna rama de modelo: **no aparece ninguna variante "AI-first" ni "human fallback"** en la página. La única mención a tecnología en la descripción del producto es "our **vast workforce** and premium infrastructure" y, en la API, "our robust API supports **unlimited parallel processing threads**".

## Why It Matters
Es la contraparte estructural del átomo que explica el spread de precios y latencias de 2Captcha por su enrutamiento interno ("Most captchas tasks are solved automatically by AI models... If AI cannot solve a task with enough confidence, it is routed to human workers") ([[2026-1024-2captcha-ai-primero-con-fallback-a-trabajadores-humanos]]). AntiCaptcha, con 100 % humano, publica un catálogo **plano**: 5 s de latencia para los trece tipos ([[2026-1026-anticaptcha-velocidad-uniforme-de-5-segundos]]), 1000/min de capacidad libre para los trece tipos, y precios sin la dispersión 1 s–17 s del otro proveedor.
Para el catálogo de 2Captcha, en cambio, la latencia iba de 1 s a 17 s según el tipo ([[2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar]]). La hipótesis que esto abre —y que el vault **no puede confirmar**— es que **la dispersión de precio y latencia por tipo que se observa en 2Captcha es consecuencia de su arquitectura hybrid, no de la dificultad intrínseca del captcha**: si todo el trabajo es humano y el precio es plano, entonces la dificultad del tipo de captcha **no** se traduce en un recargo de precio ni en más latencia.
Eso tiene un valor de decisión: si el vault elige proveedor, **la architectural (IA con fallback vs 100 % humano) es una variable de coste que explica el spread antes que el tipo de captcha**, y por tanto la elección no se puede hacer con la tabla de precios de un solo proveedor.
Nota: la captura **no** publica si existe algún componente automático previo a la asignación al trabajador, ni la tasa de rechazo humano por tipo, ni por qué los precios de Enterprise y Arkose en este proveedor no se mueven con la latencia.

## [FRICTION]
> [[2026-1024-2captcha-ai-primero-con-fallback-a-trabajadores-humanos]] afirma que "es la explicación interna del spread de precios y latencias: los tipos de 1-2 segundos son los que el modelo resuelve solo, y los de 16-17 segundos son los que caen al humano", y de ahí extrae que la capacidad publicada "es la capacidad del pool humano, no la del modelo".
> Este átomo presiona esa explicación en un punto: **un proveedor 100 % humano tiene menos dispersión de precio y latencia que uno híbrido**, no la esperable si la dificultad del captcha fuera la causa. Si la explicación fuera puramente "el tipo de captcha es difícil", un proveedor sin IA debería mostrar **más** dispersión, no menos.
> Ambas no pueden ser completamente correctas a la vez: o la latencia de 16-17 s de 2Captcha para Arkose y ALTCHA es una propiedad de esos captchas, o es el coste de enrutar al humano lo que se mide. Marcado para juicio humano, no auto-resuelto: **la captura de AntiCaptcha no publica cómo se asigna el trabajo a los trabajadores ni qué hace con los captchas que el humano no puede resolver**, así que el contraste es real pero la causa sigue sin poder decidirse con estas dos fuentes.
