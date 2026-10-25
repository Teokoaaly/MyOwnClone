---
id: 2026-1024-gptgrok2api-icloud-privacy-mail-fabrica-de-correo-con-techo-decreciente
type: atom
certainty: solid
sources: [sources/2026-10-24-gptgrok2api.md]
links: ["[[2026-1024-gptgrok2api-registro-protocolo-sin-navegador-y-captcha-solver-integrado]]", "[[2026-1024-notletters-correo-masivo-para-registros-y-lolzteam]]", "[[2026-1024-notletters-tres-vias-de-consumo-api-http-imap-y-web]]"]
---

## Claim
El repositorio incluye un **sidecar propio de iCloud Privacy Mail** que se ejecuta como servicio interno de Docker Compose, **sin puerto propio en el host y sin cuenta de sidecar**, y que **crea buzones de privacidad de Apple** usando la sesión de Apple del administrador: la interfaz nueva hace login de Apple, 2FA y **crea** buzones; la antigua hace login, 2FA y **sincroniza** buzones existentes; el **App Password de iCloud sirve solo para la retrieval de códigos por IMAP**. El techo de producción es explícito y decreciente: la interfaz nueva **20 buzones/hora por cuenta**, la antigua **5/hora**, y **25/hora** contando ambas sesiones; **cada cuenta se detiene automáticamente al llegar a 750 buzones acumulados**, y el temporizador corre por defecto **cada 60 minutos**. La integración con el registro se hace por **etiquetas de plataforma sobre el mismo buzón**: **verde = GPT registrado, azul = Grok registrado**, y un buzón solo cuenta como usado si tiene **ambos** etiquetas; la retirada de correos para registro se hace **aislada por plataforma objetivo** (al fallar, se libera la etiqueta de esa plataforma).

## Why It Matters
Es la **partida de correo resuelta dentro del propio producto**, y el vault ya tiene el modelo contrario documentado: NotLetters publica 172 palabras de home, sin dominios, sin límites ni condiciones, y el vault tuvo que concluir que **no puede usarse como fuente de coste**, solo como fuente de categoría ([[2026-1024-notletters-correo-masivo-para-registros-y-lolzteam]], [[2026-1024-notletters-tres-vias-de-consumo-api-http-imap-y-web]]). Aquí el correo es **un módulo con contrato**: límites por cuenta, tope de vida, ventana horaria, modo de retrieve (IMAP con App Password) y **estado de asignación por plataforma** — el mismo estado que el mercado chino de cuentas ya publica en el título de venta, y que el bot de Go no transportaba en absoluto en su fichero `email|password`.
El dato estructural más interesante para el vault es el **techo decreciente**: 20/hora en la interfaz nueva, 5/hora en la antigua y 750 de por vida. Eso convierte la producción de buzones en una curva de rendimiento con **rendimientos decrecientes por diseño**, no por falta de demanda: aunque la cuenta esté sana, el rendimiento se reduce. Y el **750 como tope duro por cuenta** es una cota de volumen que ningún proveedor de correo del vault publica: NotLetters no publica ningún límite.
Para MyOwnClone esto es un dato de **coste de insumo y de vida de la identidad**: si alguna vez el producto registrara cuentas por su cuenta, el correo dejaría de ser un coste por unidad sin techo y pasaría a tener **un ciclo de vida de cuenta con caducidad efectiva**, igual que el resto de credenciales de este repo.

## Nota de verificación
Las cifras (20/5/25 por hora, 750 acumulados, 60 minutos por ronda) están transcritas literalmente del README. La captura **no** publica: el coste de las cuentas de Apple que sustentan el sidecar, cuántos buzones se necesitan por alta completada, ni qué ocurre con los buzones cuando se alcanza el tope de 750.
