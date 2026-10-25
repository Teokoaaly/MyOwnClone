---
id: 2026-1024-chatgpt-creator-alta-por-correo-sin-telefono-en-el-flujo
type: atom
certainty: solid
sources: [sources/2026-10-24-chatgpt-creator-verssache.md]
links: ["[[2026-1024-chatgpt-creator-flujo-de-registro-en-nueve-pasos]]", "[[2026-1023-hero-sms-flujo-de-cinco-pasos-para-verificar-chatgpt]]", "[[2026-1023-5sim-chatgpt-verificacion-stock-13-7-millones]]"]
---

## Claim
El flujo de alta documentado por el bot **no contiene ningún paso de número de teléfono**. Los nueve pasos son Homepage, CSRF, Signin, Authorize, Register, Send OTP, Validate OTP, Create Account y Callback, y la verificación es **exclusivamente por correo**: el bot genera el buzón, recoge el OTP y lo introduce. En el README **no aparece "phone", "SMS" ni "number"** en ninguna feature, ni en los prompts, ni en la configuración. La única variable de red es el proxy.

## Why It Matters
Este dato reordena la tabla de coste por insumo del thread para la ruta de alta por correo. El §7 del thread establece el orden **correo ≪ captcha ≪ proxy ≪ SMS** y leía que el cuello de botella del alta con identidad real era el KYC humano a ¥10.28 ([[2026-1023-5sim-chatgpt-verificacion-stock-13-7-millones]]). Esta fuente añade que **el SMS no es una pata obligatoria del alta contra ChatGPT**: hay una ruta documentada, publicada y con 338 estrellas que llega a `Create Account` sin teléfono, con la verificación hecha por correo.
Eso no invalida el mercado de SMS —que vende para otras plataformas y cuyo stock de OpenAI/ChatGPT es real ([[2026-1023-5sim-chatgpt-verificacion-stock-13-7-millones]])— pero **le fija el techo**: si un flujo se resuelve con correo temporal, el pago del código por SMS solo tiene sentido cuando el proveedor exige teléfono, es decir, en la parte del mercado donde la verificación es un producto de pago, no en la del alta web de ChatGPT.
Y hay un efecto colateral que el vault tiene que ver: **el correo pasa a ser la única pieza de identidad del flujo**, con la Temporalidad de un buzón desechable detrás. Eso conecta con el dato que ya tenía registrado de HeroSMS: el número desechable **verifica el alta pero no sostiene la cuenta** ([[2026-1023-hero-sms-flujo-de-cinco-pasos-para-verificar-chatgpt]]). En la ruta de correo la pérdida de continuidad es peor: el buzón desaparece con el alta y no hay ningún canal de recuperación.

## [FRICTION]
> [[2026-1023-hero-sms-flujo-de-cinco-pasos-para-verificar-chatgpt]] (escrita el 2026-10-23, de la guía SEO de HeroSMS) describe el alta verificada de ChatGPT como un flujo de cinco pasos donde el paso 4 es **introducir el número temporal** y el paso 5 es meter el código de 6 dígitos que aparece en el panel del proveedor.
> Este átomo presiona esa creencia en un punto concreto: **ese flujo no es el flujo de alta de ChatGPT**. El bot publica el flujo real del signup web de OpenAI —nueve pasos, sin teléfono, con CSRF y `Authorize`— y lo hace sin número en ningún punto. La guía de HeroSMS describe un camino alternativo (verificación por teléfono en el flujo de alta) y es perfectamente posible que ambos convivan en 2026, según el punto de entrada o el estado de la cuenta.
> Ambas no pueden ser completamente correctas si se leen como "el flujo de alta de ChatGPT". Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
La ausencia de teléfono se ha comprobado sobre el texto completo del README capturado (features, requisitos, instalación, uso, prompts, ejemplo de salida, configuración, formato de salida, estructura del proyecto, disclaimer y licencia). No se ha clonado ni ejecutado el repositorio, así que el vault no puede afirmar que el flujo *real* de OpenAI no exija teléfono: solo que la ruta que este bot automatiza no lo usa.
