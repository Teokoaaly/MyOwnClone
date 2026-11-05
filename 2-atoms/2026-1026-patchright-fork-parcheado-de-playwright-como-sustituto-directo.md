---
id: 2026-1026-patchright-fork-parcheado-de-playwright-como-sustituto-directo
type: atom
certainty: solid
sources: [sources/2026-10-25-patchright-playwright.md]
links: ["[[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]]", "[[2026-1024-gptgrok2api-gateway-unificado-gpt-y-grok-en-api-compatible]]"]
---

## Claim
El README define el proyecto en su primera frase: **"Patchright is a patched and undetected version of the Playwright Testing and Automation Framework. It can be used as a drop-in replacement for Playwright."** El repositorio `Kaliiiiiiiiii-Vinyzu/patchright` **no es la librería**: es "This repository serves the Patchright Driver", y el uso se hace desde tres paquetes separados —**Python** (`patchright-python`), **NodeJS** (`patchright-nodejs`) y **.Net** (`patchright-dotnet`), este último marcado explícitamente como *community-driven*. La licencia es **Apache 2.0**, el copyright es de **Vinyzu**, y el mantenimiento está declarado en dos nombres: *Active Maintainer: Vinyzu* y *Co-Maintainer: Kaliiiiiiiiii*.

## Why It Matters
Es la **capa de navegador resuelta como producto, no como proyecto**, y esa distinción es lo que la hace transferible al resto del corpus del vault. El bot Go ya atomizado no usa navegador: implementa un cliente OAuth contra el signup de OpenAI por HTTP puro y por eso necesita **construir** la imitación de huella TLS y de instrumentación ([[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]]). Patchright es la operación contraria: **no construye nada, parchea lo que ya existe** y se ofrece como sustitución directa.
La consecuencia práctica es de coste y de riesgo: una capa de navegador indetectable que se instala como dependencia **no requiere ingeniería propia, ni auditoría de un protocolo, ni mantener un fork** — y además se distribuye en tres lenguajes, lo que la hace utilizable desde el stack Flask/Next.js del producto del vault sin adaptaciones. Frente al gateway de `gptGrok2api`, que expone capacidad ya creada ([[2026-1024-gptgrok2api-gateway-unificado-gpt-y-grok-en-api-compatible]]), aquí la contribución es la **herramienta de producción**, no el producto.
Lo que el vault no puede afirmar desde esta captura: que el drop-in replacement sea real en la práctica. Es una **declaración del README**, sin benchmark ni test propio adjunto.

## Nota de verificación
La definición, la distribución en tres paquetes y la atribución de mantenedores están transcritas literalmente del README. La captura **no incluye** el número de versión de Playwright parcheada, ni la API pública del driver, ni ningún dato de rendimiento. La etiqueta "undetected" es claim del autor.
