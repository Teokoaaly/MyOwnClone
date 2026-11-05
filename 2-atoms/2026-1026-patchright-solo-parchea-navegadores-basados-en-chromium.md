---
id: 2026-1026-patchright-solo-parchea-navegadores-basados-en-chromium
type: atom
certainty: solid
sources: [sources/2026-10-25-patchright-playwright.md]
links: ["[[2026-1024-dataimpulse-gateway-unico-y-protocolos]]", "[[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]]"]
---

## Claim
El README lleva la restricción en un bloque **"Important"** destacado, separado de la nota anterior: **"Patchright only patches CHROMIUM based browsers. Firefox and Webkit are not supported."** Todo el mecanismo de elusión del proyecto —el parcheo del driver, los `driver_patches`, el `patchright.patch` y el `patchright_driver_patch.ts`— está pensado para una sola familia de motor.

## Why It Matters
La restricción acota **el espacio de destinos donde esta técnica sirve**, y el vault tiene un caso concreto donde el límite duele: la integración de DataImpulse declara compatibilidad con **Puppeteer, Selenium, Playwright, Multilogin, AdsPower, GoLogin, Octoparse, Zapier, Postman, Proxifier y SwitchyOmega** ([[2026-1024-dataimpulse-gateway-unico-y-protocolos]]), es decir, la capa de proxy se integra igual con cualquier navegador. El parcheo no: **solo Chromium**.
Eso significa que en un pipeline con navegador, la elección de motor **deja de ser una decisión de rendimiento o de compatibilidad y pasa a ser una decisión de riesgo de detección**: la misma API de Playwright sobre Firefox o WebKit no está cubierta por ninguno de los parches, y por tanto hereda la detección de un navegador automatizado estándar. Es exactamente el tipo de criterio que el thread ya aplicó para los captchas —"elegir por el tipo de señal que aparece en el destino"— aplicado ahora al motor.
Y hay un contraste de arquitectura con el bot Go: aquel camino **no usa navegador en absoluto** ([[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]]), de modo que hereda la limitación de la imitación de protocolo en lugar de la del motor. Son dos carencias distintas y no intercambiables.

## Nota de verificación
La restricción está transcrita literalmente del bloque "Important" del README. La captura **no** explica qué ocurre con Firefox o WebKit en la práctica (si fallan, si se lanzan sin parchear o si no se lanzan), ni qué versión de Chromium se parchea, ni si existe un Chromium propio parcheado en el repositorio — el parcheo ocurre sobre el navegador que el usuario instala o descarga.
