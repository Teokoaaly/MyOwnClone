---
id: 2026-10-25-refinery-chatgpt-creator
type: briefing
date: 2026-10-25
sources: [sources/2026-10-24-chatgpt-creator-verssache.md]
---

# Briefing de Refinery — chatgpt-creator (verssache)

**Captura procesada:** `0-raw/2026-10-24-chatgpt-creator-verssache.md` → archivada en `0-raw/archive/2026-10-25-2026-10-24-chatgpt-creator-verssache.md`
**Fuente original:** `sources/2026-10-24-chatgpt-creator-verssache.md` (https://github.com/verssache/chatgpt-creator, 250 líneas, capturada el 2026-10-24)
**Átomos creados:** 11, todos con prefijo `2026-1024-chatgpt-creator-`
**Átomos existentes extendidos:** 2, con nota fechada (sin sobrescribir ninguna afirmación previa)
**Thread tocado:** ninguno. La actualización (ya aplicada el 2026-10-25) se propuso en `1-desk/thread-addition-chatgpt-creator.md` y quedó integrada en `3-threads/economia-de-la-verificacion-y-reventa-de-cuentas.md` (§10 nueva + fricciones 23–25).

## Qué aporta esta captura al vault

**El eslabón que faltaba en la cadena de valor que el thread viene midiendo.** Hasta ahora el vault tenía los **insumos** de un alta (número SMS, correo, captcha, proxy, identidad verificada) y el **destino** (lzt.market revendiendo cuentas de IA por lotes). Esta captura es el **productor**: `verssache/chatgpt-creator`, MIT, Go 1.21+, 338 estrellas, 90 forks, un bot de registro masivo de cuentas de ChatGPT publicado en código abierto.

## Los cinco hallazgos que cambian algo

1. **El alta real de ChatGPT no pasa por teléfono.** El bot documenta el flujo de signup web de OpenAI en nueve pasos HTTP —Homepage, Get CSRF, Signin, Authorize, Register, Send OTP, Validate OTP, Create Account, Callback— y **ninguno es un número de teléfono**: la verificación es por OTP de correo. Esto corrige una simplificación implícita del thread y de la guía de HeroSMS, que describía el alta verificada como "número + código de 6 dígitos".

2. **En esa ruta, el captcha no aparece y el correo no se compra.** Los nueve pasos devuelven todos 200 y no hay ningún cliente de resolución; el correo lo genera el propio bot con `generator.email`. La partida cara del flujo **no se compra en ninguna parte**: es la ingeniería de imitación del cliente —TLS fingerprinting con perfiles Chrome aleatorizados, "sentinel token" y cabeceras de traza con formato Datadog. **La capa dominante de un flujo de alta contra OpenAI no es una compra, es una construcción.**

3. **El fallo es una unidad de trabajo, no un error.** El pool de workers configurable (defecto 3) con reintento hasta el objetivo, y un resumen de lote que separa `Attempts` de `Success` (6 intentos, 5 cuentas, 1 fallo, 1m45s). La unidad de éxito es la cuenta, y el coste hay que calcularlo sobre intentos. Es un modelo de coste distinto del de la tabla por insumo del thread, donde cada pata se mide por unidad.

4. **El producto es un fichero de credenciales sin estado de calidad.** `results.txt`, formato `email|password`, pipe, sin JSON y sin metadatos: no hay campo de país, de verificación ni de caducidad, mientras que el mercado chino sí declara todo eso en el título de venta. El pipeline de producción no transporta la garantía que el mercado luego vende.

5. **Popularidad sin mantenimiento.** 338 estrellas y 90 forks contra **4 commits, 0 releases, 0 tags, 1 branch**: la única forma de consumirlo es `git clone` + `go run` desde `main`. Mismo patrón que el vault ya había registrado para Midjourney-Proxy, con una diferencia de escala que no cambia la lección. Y 90 forks sobre 4 commits es la proporción de un proyecto de plantilla: la línea de "cómo evadir" sigue en fase manual, no de producto.

## Advertencia metodológica

Casi todo lo que el repo afirma es **claim del propio autor**: las siete features, los prompts con sus valores por defecto, el ejemplo de salida y el resumen de lote. Lo único medido sobre la captura son las cifras de la cabecera (338/90/1, 4 commits, 1 branch, 0 tags, releases y packages vacías) y la transcripción literal de los nueve pasos con su código de estado. El vault **no ha clonado ni ejecutado el repositorio** y no ha auditado el código línea a línea: el `go.mod` no está capturado. Por eso dos átomos quedan en `tentative` —la blacklist de dominios (solo se ve por el mensaje de commit y el `.gitignore`) y la ausencia de captcha (prueba negativa sobre captura parcial)— y el token sentinel se registra como lo que es: un nombre de commit y un nombre de archivo, sin contenido capturado.

## Fricciones añadidas (para el §9 del thread)

23. El flujo real de alta de ChatGPT no pasa por teléfono, pero el marketplace de SMS vende código de teléfono: el vault no puede escribir "el alta de ChatGPT es número + código" sin matizarlo.
24. 5sim afirma que usar número virtual para OpenAI es "Yes" sin citar norma; el propio fabricante de la cadena declara que su uso viola los ToS de OpenAI. No pueden ser ambas ciertas en el sentido que cada una implica.
25. La captura permite afirmar que este bot no gestiona captcha, no que el registro de ChatGPT no lo exija: si se usa el repo como referencia de arquitectura, falta una parte que no existe en él.

## Fechas

Las notas fechadas añadidas a átomos existentes son del 2026-10-24 y están marcadas con `## [NOTA 2026-10-24 — ...]`. No se sobrescribió ninguna afirmación previa: la nota del átomo de HeroSMS y la del átomo de lzt.market se limitan a apuntar al átomo nuevo que las matiza.

## Pendiente para el Editor

- Aplicado el 2026-10-25: `1-desk/thread-addition-chatgpt-creator.md` quedó integrado en `3-threads/economia-de-la-verificacion-y-reventa-de-cuentas.md` (§11 + fricciones 31–33, renumeradas) y la nota de método recoge esta cuarta tanda de capturas.
- Decidir si la §10 va antes o después de la §9 de fricciones, y si renumera las fricciones.
- Revisar si los tres "referencias cruzadas" del final del bloque (§2 fila de SMS, §4 subsección c, §7 fila de captcha) se tocan o se dejan como nota del Editor.
- Nota: el Scout del 2026-10-24 dejó esta captura y dos vecinas en el mismo lote (`2026-10-24-gptgrok2api.md`, `2026-10-24-github-search-chatgpt-account-creator.md`) que siguen en `0-raw/` con `Status: ready`; la segunda es la búsqueda de GitHub que da contexto a esta, y probablemente merece un átomo propio cuando se procese.
