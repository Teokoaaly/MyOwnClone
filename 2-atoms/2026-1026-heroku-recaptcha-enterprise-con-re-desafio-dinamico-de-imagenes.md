---
id: 2026-1026-heroku-recaptcha-enterprise-con-re-desafio-dinamico-de-imagenes
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-signup.md]
links: ["[[2026-1026-heroku-alta-protegida-por-recaptcha-enterprise-de-imagenes]]", "[[2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar]]", "[[2026-1024-2captcha-capacidad-libre-por-minuto-como-proxy-de-cola]]"]
---

## Claim
El reCAPTCHA del alta de Heroku **reemite el desafío en vez de aceptarlo o rechazarlo de forma terminal**. La captura reproduce **cinco cadenas de error distintas** del componente, todas presentes a la vez: **"Recaptcha requires verification."**, **"Please try again."**, **"Please select all matching images."**, **"Please also check the new images."** y **"Please select around the object, or reload if there are none."** Las dos últimas son la firma literal del re-desafío: la imagen ya resuelta **vuelve a entrar en la cola** ("check the new images") y el usuario puede tener que **delimitar un objeto** o **recargar el conjunto** ("reload if there are none").

## Why It Matters
Para el vault esto es un **dato de coste de elusión**, no un detalle de interfaz. La thread de verificación mide la resolución de captcha por unidad y por latencia, con la conclusión de que **el captcha es la partida más barata y la más fácil de cotizar** —1 a 2 segundos en los tipos estándar y $0,5 a $2,99 por mil ([[2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar]])— y con la profundidad de pool medida como "Free capacity, per minute" ([[2026-1024-2captcha-capacidad-libre-por-minuto-como-proxy-de-cola]]). Este átomo muestra que **el captcha de una página de alta real no es un token que se pide una vez**: es un proceso con re-emisiones, con reintentos del usuario y con un modo de fallo distinto ("reload") que puede no tener solución en la tanda actual.
La consecuencia operativa es que **la unidad de coste no es "captcha resuelto" sino "captcha resuelto a la primera"**: un desafío que vuelve a pedir imágenes convierte cada re-emisión en una unidad adicional, y el proveedor —no el automatizador— decide cuándo termina la ronda. Es el mismo patrón de reloj y de unidad de trabajo que el vault ya registró en el flujo de alta de ChatGPT, donde **el fallo es una unidad de trabajo y el coste se calcula sobre intentos, no sobre cuentas**.
Y hay un segundo efecto, más incómodo: el modo **"reload if there are none"** describe un desafío en el que **el objetivo puede no estar presente**. Es decir, hay un camino en el que **no hay solución que comprar** porque la instancia es insatisfacible. Eso es un tipo de coste que ninguna tabla de precios de captcha del vault tiene.

## [FRICTION]
> [[2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar]] afirma que "reCAPTCHA v2, Cloudflare Turnstile, reCAPTCHA Enterprise y Amazon captcha" se resuelven en **2 segundos**, y de ahí el thread concluye que el captcha **no es un cuello de botella de tiempo**.
> Este átomo presiona esa creencia en un punto concreto: **el tiempo de resolución es por desafío, y un desafío puede no ser resoluble en absoluto** ("Please select around the object, or reload if there are none"), y el sistema **reemite** ("Please also check the new images") en lugar de aceptar. Si el precio por 1000 se paga por captcha resuelto, el re-desafío no está en la unidad de compra; si se paga por **intento de resolución**, entonces la cifra de "2 segundos" describe el mejor caso de un producto cuyo coste real escala con el número de rondas.
> Ambas no pueden ser completamente correctas a la vez: o la latencia publicada es la del camino feliz y el coste unitario real incluye re-emisiones, o el captcha de una página de alta concreta es un producto distinto del que el catálogo mide. Marcado para juicio humano, no auto-resuelto: la captura de 2Captcha no publica si el precio es por solución o por intento.
