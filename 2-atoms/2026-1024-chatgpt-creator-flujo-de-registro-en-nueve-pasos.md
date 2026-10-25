---
id: 2026-1024-chatgpt-creator-flujo-de-registro-en-nueve-pasos
type: atom
certainty: solid
sources: [sources/2026-10-24-chatgpt-creator-verssache.md]
links: ["[[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]]", "[[2026-1024-chatgpt-creator-token-sentinel-y-cabeceras-de-traza-datadog]]", "[[2026-1023-hero-sms-flujo-de-cinco-pasos-para-verificar-chatgpt]]"]
---

## Claim
El README documenta el **flujo de alta como una secuencia de nueve pasos HTTP** con su ejemplo de salida real. La traza por trabajador es: **(1) Visit Homepage (Try 1) | 200 → (2) Get CSRF | 200 → (3) Signin | 200 → (4) Authorize | 200 → (5) Register | 200 → (6) Send OTP | 200 → (7) Validate OTP [483291] | 200 → (8) Create Account | 200 → (9) Callback | 200**, y tras el callback el bot imprime `SUCCESS: johndoe8x2kq@smartmail.de`. El árbol de archivos lo confirma en un comentario: `internal/register/flow.go  # Registration flow (CSRF → signup → OTP → callback)`, con `batch.go` como "Batch orchestration, worker pool, retry logic" y `client.go` como "HTTP client with TLS fingerprinting". Los tiempos del ejemplo van de 09 a 33 segundos de reloj entre el primer y el noveno paso, con los saltos más largos en **Create Account (8 s) y Callback (9 s)**.

## Why It Matters
Es la **descripción más concreta que el vault tiene del alta real de una cuenta de ChatGPT por vía web**, y contrasta de forma inmediata con el flujo que el thread documenta para el canal SMS: HeroSMS describe cinco pasos de compra y verificación ([[2026-1023-hero-sms-flujo-de-cinco-pasos-para-verificar-chatgpt]]), y este bot describe nueve pasos HTTP que **no incluyen ningún número de teléfono**. El correo sustituye por completo al SMS en esta ruta: la verificación es por OTP de email, no por número.
De los nueve pasos, dos son los que un lector de producto no puede pasar por alto. **`Get CSRF`** y **`Authorize`** indican que el bot habla con un **servidor de autorización estilo OAuth**: hay token CSRF que obtener y un endpoint `Authorize` antes de `Register`. Y **`Callback`** es el otro extremo de ese mismo flujo: el registro no termina en la creación de la cuenta, termina en un **callback de autorización que el bot tiene que alcanzar con la cookie de sesión correcta**. Quien intente replicar un alta de este tipo sin navegador está, de hecho, implementando un cliente OAuth contra el signup de OpenAI.
Los tiempos de la traza dan, además, la **cadencia real**: unos 25 segundos por cuenta con un solo trabajador, lo que convierte el pool de workers en la palanca de volumen, no el coste de cada paso.

## Nota de verificación
La traza es el bloque "Example Output" del README, con valores concretos de un caso concreto. El vault **no puede afirmar que el flujo actual de OpenAI siga siendo este**: el repositorio arrastra meses sin commits (ver [[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]). Los nombres de endpoint son los que el propio log imprime, no una API documentada por OpenAI.
