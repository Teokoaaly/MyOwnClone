---
id: 2026-1024-chatgpt-creator-el-flujo-no-resuelve-captcha-de-manera-explicita
type: atom
certainty: tentative
sources: [sources/2026-10-24-chatgpt-creator-verssache.md]
links: ["[[2026-1024-chatgpt-creator-flujo-de-registro-en-nueve-pasos]]", "[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1024-chatgpt-creator-tls-fingerprinting-con-perfiles-chrome-aleatorios]]"]
---

## Claim
La traza de ejemplo del flujo de alta **no contiene ningún paso de captcha**. Los nueve pasos son Visit Homepage, Get CSRF, Signin, Authorize, Register, Send OTP, Validate OTP, Create Account y Callback, y **todos devuelven 200**. El README no menciona captchas en ningún punto: no hay cliente de 2Captcha, ni API de resolución, ni ningún módulo en el árbol de archivos. Las siete features declaradas incluyen **TLS fingerprinting** ("Randomized Chrome TLS profiles to avoid detection") como la única medida anti-detección nombrada. Es decir, **la elusión que el bot implementa es de transporte, no de puzzle**.

## Why It Matters
Es la pieza que cierra la aritmética del thread por el lado que faltaba. El §7 del thread establece que el captcha es **la partida más barata y la más fácil de cotizar** —de milésimas de dólar a céntimos por captcha, resuelto en 1–2 segundos ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]])— y que el orden de coste de las patas es "correo ≪ captcha ≪ proxy ≪ SMS". Esta fuente dice algo más: **en la ruta de alta por correo contra OpenAI, el captcha ni siquiera aparece en el camino**, y la partida cara no es la resolución del puzzle sino la **ingeniería de la huella TLS** ([[2026-1024-chatgpt-creator-tls-fingerprinting-con-perfiles-chrome-aleatorios]]).
La consecuencia es una inversión del criterio de selección que el thread estaba construyendo. Si el captcha no aparece, **la partida dominante de un flujo de alta contra este proveedor no es una compra, es una construcción**: hay que saber imitar al cliente. Eso significa que un vault con presupuesto de ≤ €4/mes no podría "comprar su camino" hasta la elegibilidad: el proxy se paga, el captcha se paga, pero **el fingerprint no se compra en ninguna parte**.
Y la lectura honesta es también una advertencia: **el bot no resuelve captcha porque el flujo de registro de ChatGPT que el bot explota en 2026 quizá no lo exige**, o porque el punto de fallo está antes y no llega a plantearse. La captura no permite distinguir entre las dos. Un flujo que funciona sin captcha puede dejar de funcionar en cuanto el proveedor lo añada, y el bot no tiene ninguna pieza preparada para eso.

## Nota de verificación
El átomo es `tentative` por una razón concreta: **la ausencia de captcha en la traza y en el README es una prueba negativa sobre una captura parcial**. El repositorio no está auditado línea a línea (no hay `go.mod` capturado, no hay código), y el README no promete compatibilidad futura con captcha. El vault no puede afirmar que el registro de ChatGPT no exija captcha; solo que este bot, en su versión de abril de 2026 y en la ruta que documenta, no lo gestiona.
