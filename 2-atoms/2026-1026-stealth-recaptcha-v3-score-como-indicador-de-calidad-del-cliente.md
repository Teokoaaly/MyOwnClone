---
id: 2026-1026-stealth-recaptcha-v3-score-como-indicador-de-calidad-del-cliente
type: atom
certainty: solid
sources: [sources/2026-10-25-puppeteer-extra-stealth.md]
links: ["[[2026-1026-capsolver-recaptcha-v3-con-score-de-0-7-o-0-9-solo-por-contacto]]", "[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1026-anticaptcha-plugin-de-navegador-gratuito]]"]
---

## Claim
El README tiene una sección "**Improved reCAPTCHA v3 scores**" con la afirmación "Using stealth also seems to help with maintaining a normal reCAPTCHA v3 score", apoyada en **dos capturas de pantalla** (Regular Puppeteer vs Stealth Puppeteer) y con el descargo explícito: "The official test is to be taken with a grain of salt, as the score is calculated individually per site and multiple other factors (past behaviour, IP address, etc). Based on anecdotal observations it still seems to work as a rough indicator". Y cierra con una recomendación: "Have a look at the recaptcha plugin if you have issues with reCAPTCHAs".

## Why It Matters
Es la primera vez que el vault ve **el score de reCAPTCHA v3 tratado como indicador de la calidad del cliente y no como producto de catálogo**. Y es una afirmación con una estructura argumentative que el vault ya conoce de otra fuente: CapSolver vende reCAPTCHA v3 a **$1.0 por 1000** pero declara que el **score es una variable que se negocia por contacto** —"Please contact us if you can't get a higher score of 0.7 or 0.9" ([[2026-1026-capsolver-recaptcha-v3-con-score-de-0-7-o-0-9-solo-por-contacto]]). Es decir: **el score es lo que de verdad se compra, y se compra fuera de la tabla de precios** ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]).
Lo que aporta esta fuente es una **tercera posición para el score**: no un producto con score garantizado, ni una cifra cotizada, sino **un indicador del estado del cliente**. Si el navegador es indetectable, el score sale normal "por efecto secundario". Eso convierte el score de reCAPTCHA v3 en algo que se puede **medir para diagnosticar el cliente**, no solo para comprar una respuesta —y por tanto en un **termómetro de la calidad de la evasión**, gratis.
El recuadro metodológico del propio autor ("anecdotal observations", "rough indicator", el score depende de la IP y del comportamiento pasado) es lo que hace que este átomo sea más valioso que la afirmación: **el propio README admite que la prueba oficial no es concluyente**. Eso es un precedente de rigor dentro del sector, y el vault debería citarlo cuando evalúe cualquier otra afirmación de score.

Nota de verificación: el texto es transcripción literal. La captura **no** publica los valores numéricos de los scores de las dos capturas de pantalla (son imágenes), ni la fecha de la medición, ni el número de sitios.
