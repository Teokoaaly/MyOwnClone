---
id: 2026-1026-anticaptcha-tareas-proxyless-en-todo-el-catalogo
type: atom
certainty: solid
sources: [sources/2026-10-25-anti-captcha-pricing.md]
links: ["[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1024-brightdata-web-unlocker-resuelve-captcha-y-no-requiere-kyc]]", "[[2026-1024-iproyal-web-unblocker-ia-a-1-dolar-por-1000-solicitudes]]"]
---

## Claim
Los enlaces de tarea del catálogo de AntiCaptcha apuntan a tipos **`*Proxyless`**: `RecaptchaV2TaskProxyless`, `RecaptchaV3TaskProxyless`, `RecaptchaV2EnterpriseTaskProxyless`, `GeeTestTaskProxyless`, `FunCaptchaTaskProxyless`, `TurnstileTaskProxyless`, `ProsopoTaskProxyless`, `FriendlyCaptchaTaskProxyless`, `AmazonTaskProxyless`, `AltchaTaskProxyless`. Los dos tipos no-proxyless del catálogo son `ImageToTextTask` y `ImageToCoordinatesTask`, más el `AntiGateTask` ("Custom Tasks").

## Why It Matters
Es un dato de **arquitectura de producto** que la tabla de precios no dice pero los enlaces sí: el proveedor resuelve el captcha **sin aportar proxy**, es decir, el cliente conserva su propia IP y su propio contexto de geolocalización, y el precio publicado es **solo el coste de resolución**.
Eso separa esta categoría del producto de proxy que ya está en el vault. El Web Unlocker de Bright Data "fully handles all of the unblocking, including CAPTCHA solving and automated retries" y usa "either a Datacenter or Residential IP" ([[2026-1024-brightdata-web-unlocker-resuelve-captcha-y-no-requiere-kyc]]); el Web Unblocker de IPRoyal es una línea **propia, con unidad propia** de $1.00/1000 requests ([[2026-1024-iproyal-web-unblocker-ia-a-1-dolar-por-1000-solicitudes]]). AntiCaptcha, en cambio, **no vende el proxy**: vende la resolución, y quien la compra sigue necesitando su propia línea de red —que es exactamente la partida que el thread identifica como la única cuyo coste depende de un volumen que nadie del vault controla.
La consecuencia de modelo es útil: **solver y proxy son dos partidas separadas en este proveedor, y eso las hace comparables** — se puede cotizar "captcha" y "red" por separado, como hace ya el thread con la tabla de coste por insumo ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]).
Y explica por qué el precio de reCAPTCHA v3 "depends on the V3 quality score": en proxyless, la calidad no depende del modelo sino del contexto que envía el cliente, así que el proveedor puede graduar por score.
Nota: la captura **no** publica si existen variantes **con** proxy (con su precio), ni si el precio de la tarea proxyless incluye o excluye el tráfico del worker.
