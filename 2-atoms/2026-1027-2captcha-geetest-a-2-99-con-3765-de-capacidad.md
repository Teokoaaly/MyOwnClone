---
id: 2026-1027-2captcha-geetest-a-2-99-con-3765-de-capacidad
type: atom
certainty: solid
sources: [sources/2026-10-26-2captcha-pricing-captcha.md]
links: ["[[2026-1024-2captcha-hcaptcha-y-geetest-ausentes-del-catalogo-publicado]]", "[[2026-1026-anticaptcha-geetest-a-1-80-como-catalogo-publicado]]", "[[2026-1026-capsolver-geetest-v3-v4-y-aws-waf-tipos-que-el-catalogo-de-2captcha-no-publica]]"]
---
## Claim
Con el catálogo ampliado a 48 filas, **GeeTest captcha sí aparece en 2Captcha**: precio **$2.99 por 1000**, **4 sec** de velocidad de resolución y **3,765** de capacidad libre por minuto, con enlace a `2captcha.com/p/geetest` y demo en `/demo/geetest`. **hCaptcha, en cambio, sigue sin aparecer** en ninguna de las 48 filas.

## Why It Matters
El vault tenía una línea de coste marcada como **no cotizable** para Geetest en 2Captcha, y ahora la tiene cotizada: **$2.99 por 1000** es el peldaño alto del catálogo y **$0.00299 por captcha**, con una latencia de **4 segundos**, en la banda baja del catálogo (5 tipos resuelven en 1 sec, 3 en 2 sec, 3 en 3 sec y 3 en 4 sec, este último peldaño compartido con GeeTest). Esto convierte a Geetest en un caso de comparación de tres proveedores: **$1.2 en CapSolver** (< 5S), **$1.8 en AntiCaptcha** (5 s) y **$2.99 en 2Captcha** (4 sec). Es decir, **el mismo tipo está disponible en tres proveedores con un factor ×2,5 entre el más barato y el más caro**, y con la particularidad de que **2Captcha es el más caro y a la vez el único de los tres con una latencia cerrada por debajo de los 5 s** (CapSolver publica "< 5S" y AntiCaptcha exactamente 5 s). Geetest es, con el reCAPTCHA v3, el segundo tipo del corpus donde **precio y latencia se mueven en direcciones opuestas**.

También cierra una comparación que el vault no había hecho: **GeeTest a $2.99 con 3.765 libres/min es el decimoctavo tipo del catálogo por capacidad libre** —diecisiete lo superan (los siete captchas de texto a 12.000/min, los tres reCAPTCHA v2 a 11.273/min y siete tipos interactivos entre 4.500 y 5.673/min)—, lo que lo sitúa en la **banda alta del catálogo pese a estar en el peldaño de precio $2.99**, por encima del $0.5 — $1 de Image Captcha en cuanto a capacidad por unidad de precio. Para un pipeline que resuelve miles de captchas de un mismo tipo, **GeeTest es un tipo bien abastecido a precio de peldaño alto**: el coste unitario se paga, pero la capacidad no estrangula al pipeline.

Y cierra el patrón del "hueco del corpus": **hCaptcha sigue siendo el único tipo que ningún proveedor del corpus publica** —2Captcha, AntiCaptcha y CapSolver—, tres catálogos con 48, 13 y 9 tipos. Para el vault, hCaptcha es **una ausencia verificada sobre tres fuentes**, no un simple hueco de captura.

## [FRICTION]
> [[2026-1024-2captcha-hcaptcha-y-geetest-ausentes-del-catalogo-publicado]] afirma que "**No aparecen hCaptcha ni Geetest** en ninguna parte de la página" y concluye que ambos "**no se pueden comprar como producto de catálogo publicado**".
> Este átomo presiona esa conclusión en la mitad exacta que la captura nueva desmiente: **Geetest SÍ aparece ahora en el catálogo publicado de 2Captcha**, con precio, latencia y capacidad. La conclusión original era correcta para la captura del 2026-10-23, pero su alcance —"no se pueden comprar como producto de catálogo publicado"—, aplicado al corpus, queda desmentido en su mitad de Geetest. Ambas no pueden ser completamente correctas: o el catálogo público de 2Captcha excluye Geetest (y entonces la fila de $2.99 no es una fila de catálogo), o lo incluye (y entonces "Geetest no es cotizable en 2Captcha" es falso y la fila de coste del insumo captcha debe añadir $2.99/1000 a 4 sec). Marcado para juicio humano, no auto-resuelto: la captura no fecha la incorporación de Geetest al catálogo —podría haber estado siempre detrás del "Show more"—, de modo que lo único verificable es que **ahora es visible**.

Nota: la captura **no** publica el precio de Geetest en sus variantes (v3, v4, slider), ni la diferencia entre "GeeTest captcha" y "GeeTest v3/v4", ni condiciones de volumen.
