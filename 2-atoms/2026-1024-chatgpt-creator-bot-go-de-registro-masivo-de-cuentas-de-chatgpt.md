---
id: 2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt
type: atom
certainty: solid
sources: [sources/2026-10-24-chatgpt-creator-verssache.md]
links: ["[[2026-1024-chatgpt-creator-flujo-de-registro-en-nueve-pasos]]", "[[2026-1023-lzt-categoria-llm-accounts-para-reventa]]", "[[2026-1023-herosms-api-y-partners-de-registro-masivo]]"]
---

## Claim
`verssache/chatgpt-creator` se titula **"ChatGPT Account Registration Bot"** y se describe en su primera línea como un **"Automated bulk ChatGPT account registration bot built with Go"** con cinco rasgos declarados: *concurrent workers, TLS fingerprint spoofing, automatic email generation, OTP verification, and retry-until-success logic*. La lista de features del README enumera siete: registro concurrente con **pool de workers configurable**, **TLS fingerprinting** con perfiles Chrome aleatorizados, generación automática de correo temporal, **verificación OTP** automática, **bucle de reintento hasta alcanzar el objetivo**, **proxy HTTP/SOCKS opcional** para todas las peticiones y configuración en **archivo JSON con overrides por prompt interactivo**. Requisito: **Go 1.21+**; licencia **MIT**; el repositorio está mantenido por el usuario `verssache`. El propio README incluye un descargo explícito: el software es "for educational and research purposes only" y **"Use of this tool to create accounts in violation of OpenAI's Terms of Service is solely at your own risk"**.

## Why It Matters
Es la **pieza de código abierto que más directamente documenta la capa (b) del mercado** que el thread viene describiendo: la de la producción de cuentas de IA a escala. Hasta ahora el vault tenía el *mercado* de esa capa —lzt.market vendiendo `LLM Accounts` con carga masiva ([[2026-1023-lzt-categoria-llm-accounts-para-reventa]])— y los *insumos* (números, correo, captcha, proxy), pero no la **herramienta** que convierte esos insumos en cuentas terminadas. Este repo es esa herramienta, publicada y con 338 estrellas.
Eso completa la cadena de valor del thread de punta a punta: **insumo desechable → bot que lo consume → cuenta creada → mercado de reventa**. Y lo hace de una forma que no encaja con el producto del vault: MyOwnClone compite por el tramo de conversación con IA, no por la fábrica de identidades ([[2026-1023-herosms-api-y-partners-de-registro-masivo]]).
El descargo de responsabilidad es la otra mitad del dato: **el propio autor declara que el uso viola los ToS de OpenAI**. No es una inferencia del vault; es una frase del README. Eso fija un límite explícito al tipo de proyecto que este repositorio representa y da al thread un hecho duro donde antes solo había una lectura de mercado.

## Nota de verificación
La captura es la página del repositorio tal como la renderiza GitHub (README + tabla de archivos + metadatos). El vault no ha ejecutado el código ni auditado el flujo más allá de lo que el README y el árbol de archivos declaran.
