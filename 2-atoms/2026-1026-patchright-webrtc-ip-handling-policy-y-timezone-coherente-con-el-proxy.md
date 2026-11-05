---
id: 2026-1026-patchright-webrtc-ip-handling-policy-y-timezone-coherente-con-el-proxy
type: atom
certainty: solid
sources: [sources/2026-10-25-patchright-playwright.md]
links: ["[[2026-1023-hero-sms-ip-y-vpn-coincidentes-con-el-pais-del-numero]]", "[[2026-1024-dataimpulse-sesiones-rotating-y-sticky]]"]
---

## Claim
El bloque de patrocinio de ProxyLane incluye la única recomendación de configuración técnica de todo el README, con un fragmento de código y una advertencia explícita. **"To match the reported timezone to your proxy, give each profile its own sticky IP pinned to a city and set the same timezone"** — con `launch_persistent_context(user_data_dir=..., channel="chrome", headless=False, no_viewport=True, proxy={...}, timezone_id="America/Chicago", locale="en-US")` y el comentario *one sticky IP per profile* / *match the proxy city*. Y la advertencia: **"Tip: set `--webrtc-ip-handling-policy=disable_non_proxied_udp`, otherwise WebRTC exposes your real IP"**, con enlace al issue 47 del repositorio Python.

## Why It Matters
Este es el **dato operativo más accionable de toda la captura**, y cierra una laguna que el thread tenía abierta desde la §7. La regla del vault era "país real de la IP == país de la identidad usada" ([[2026-1023-hero-sms-ip-y-vpn-coincidentes-con-el-pais-del-numero]]); esta fuente añade dos dimensiones que el thread no tenía: **coherencia de zona horaria y de locale con la ciudad del proxy**, y **fuga por WebRTC**.
La coherencia horaria es el mismo criterio de la §7 aplicado un nivel más fino: si la IP dice Chicago, el `timezone_id` debe decir Chicago y el `locale` debe ser `en-US`. Es un emparejamiento de tres campos contra una ciudad, no de un país. Y la coherencia de sticky session es lo que hace que la coherencia tenga sentido: una IP rotatoria hace imposible mantener el trío IP-zona-locale fijo, de modo que **el modo de sesión decide si la coherencia es siquiera implementable** ([[2026-1024-dataimpulse-sesiones-rotating-y-sticky]]).
El flag de WebRTC es un caso aparte y muy distinto: **no es un ajuste de coherencia, es una fuga de la IP real a través de un canal que el proxy no cubre**. Es decir, el presupuesto de IP del pipeline —la IP que el destino ve— puede no coincidir con la IP que el proxy entrega, y esa discrepancia es invisible en la config. La captura no dice en qué navegador se rompe ni con qué versión.

## Nota de verificación
El fragmento de código, los tres campos y la advertencia están transcritos literalmente. La captura **no** incluye el contenido del issue 47, ni explica el mecanismo por el que WebRTC expone la IP, ni indica el valor por defecto de `--webrtc-ip-handling-policy`. Que el flag se declare en la sección de patrocinio de un proveedor —y no en la documentación del driver— es un matiz que conviene tener presente: la fuente es un bloque comercial dentro del README.
