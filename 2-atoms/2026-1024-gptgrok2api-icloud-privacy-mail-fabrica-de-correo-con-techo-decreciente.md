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


## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-emailondeck-temp-mail.md`. Este átomo documenta el **único ciclo de vida de buzón explícito del corpus**: 20 buzones/hora en la interfaz nueva, 5/hora en la antigua, 25/hora sumando ambas, **tope de 750 buzones acumulados por cuenta**, temporizador de 60 minutos por ronda, y "la retirada de correos para registro se hace **aislada por plataforma objetivo**". Su tesis es que allí el correo es "un módulo con contrato".

EmailOnDeck ofrece el **contraste de ciclo de vida sin contrato**, y con una contradicción interna que este átomo no tenía: la home incluye entre sus cinco ventajas, con icono propio, **"Emails are constantly being securely deleted"**, y al mismo tiempo ofrece en la navegación un enlace **"RECOVER EMAIL"** → `www.emailondeck.com/recover_email_address.php` ([[2026-1026-emailondeck-borrado-seguro-y-pagina-de-recuperacion]]). La captura **no describe** el mecanismo de recuperación: ni datos que pide, ni plazo, ni condiciones, ni si aplica a cualquier buzón.

Dos consecuencias para el Editor:

1. **El "ciclo de vida con contrato" del sidecar no es la norma del sector, es la excepción.** Un proveedor con 11 años de operación y 215 millones de correos declarados ([[2026-1026-emailondeck-contador-215158204-correos-procesados]]) **no publica ni un plazo de retención ni un límite de buzón**. El contrato explícito (20/5/25 por hora, 750 de por vida) es una feature del repo, no del mercado.

2. **La fricción borrado-vs-recuperación es real y hay que dejarla abierta.** Si "constantly being securely deleted" y "RECOVER EMAIL" se refieren al mismo buzón, no pueden ser ciertas a la vez; si la recuperación cubre solo un subconjunto de casos, la captura no lo dice. Esto **no es** un problema para el sidecar del bot —que consume y retira el correo él mismo— pero sí lo es para cualquier diseño que asuma "el buzón desechable es un recurso de un solo uso". **No se ha visitado `recover_email_address.php`**, así que el vault no puede arbitrarlo.


## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-mail-tm-temp-mail.md`.

Este átomo sostiene que el sidecar de iCloud Privacy Mail es el **único ciclo de vida de buzón explícito del corpus** —20 buzones/hora en la interfaz nueva, 5/hora en la antigua, 25/hora sumando ambas, **tope de 750 buzones acumulados por cuenta**, temporizador de 60 minutos por ronda— y de ahí la tesis de que allí el correo es "un módulo con contrato".

Mail.tm publica el **modelo de ciclo de vida exactamente opuesto**, y de forma explícita: "The mailbox itself is **kept forever**; or delete it yourself, if that gives you more peace of mind" y "an **unlimited number** of new ones… **no limit** on how many disposable addresses you create" ([[2026-1026-mail-tm-buzon-conservado-para-siempre-y-sin-limite-de-unidades]]).

Consecuencia para el Editor: la tesis de "el contrato explícito es una feature del repo, no la norma del sector" **se refuerza y se complica**. Mail.tm no es silencioso como NotLetters ni contradictorio como EmailOnDeck —es **explícito y sin techo**, y lo declara en su home gratis. Así que hay **tres ciclos de vida declarados, no uno ausente**: techo y temporizador (sidecar), borrado constante con página de recuperación (EmailOnDeck), y conservación indefinida sin límite de unidades (mail.tm). Y el dato de seguridad que se sigue de esto es nuevo para el vault: **el buzón "kept forever" con clave propia es una credencial persistente, no un consumible** —Mail.tm promete que "Nobody but you can see what's inside", y eso solo es sostenible si la clave es realmente única y aleatoria, cosa que la captura **no** garantiza y que el uso que el propio vault tiene registrado de mail.tm **no cumple** ([[2026-1026-mail-tm-el-farm-del-vault-ya-lo-usa-con-dominio-propio-y-clave-determinista]]).


## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-mail-tm-api-docs.md`.

Este átomo sostiene que el valor del sidecar de iCloud Privacy Mail es su **contrato explícito** —20/5/25 buzones por hora, tope de 750 acumulados por cuenta, temporizador de 60 minutos— y que sin contrato el buzón es un coste sin techo. mail.tm publica ahora **un contrato de otro tipo**: "The general quota limit is **8 queries per second (QPS) per IP address**", con el flujo de alta en **cuatro peticiones** ([[2026-1027-mail-tm-limite-de-8-qps-por-ip-address]], [[2026-1027-mail-tm-flujo-de-cuatro-peticiones-para-obtener-un-buzon]]).

Consecuencia para el Editor: el thread puede **comparar dos clases de contrato de recurso**, que antes no tenía. El del sidecar **acota unidades** y deja el ritmo sin techo; el de mail.tm **acota la cadencia y deja las unidades virtualmente ilimitadas** ("no limit" de unidades, [[2026-1026-mail-tm-buzon-conservado-para-siempre-y-sin-limite-de-unidades]]). Derivado del segundo contrato, que es aritmética del vault y no cifra del proveedor: **8 QPS ÷ 4 llamadas = 2 buzones/s y 7.200 buzones/hora por IP**, o **2,67 buzones/s y 9.600 buzones/hora** si `GET /domains` se cachea —frente a los **20 buzones/hora** del sidecar, es decir, **360 veces más rápido con una IP y sin contrato de unidades**. La hipótesis operativa que hay que dejar escrita: **el contrato útil es el que acota unidades**, y por eso el 8 QPS no sustituye al techo de 750, sino que lo hace irrelevante frente a un pasivo acumulativo sin cadencia de gasto.


## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-mail-tm-api-domains-live.md`.

Este átomo sostiene que el sidecar de iCloud Privacy Mail es valuable por su **contrato explícito** de 20/5/25 buzones por hora y tope de 750 acumulados, y que sin contrato el buzón es un coste sin techo. La captura de mail.tm añade la pieza que faltaba en la comparación: **el contrato de cadencia sin contrato de unidades no se sostiene solo**, porque el pool de dominio disponible es de **uno** ([[2026-1027-mail-tm-un-solo-dominio-publicado-en-la-api-en-vivo]]).

Consecuencia para el Editor: el átomo puede **cerrar una tesis** que estaba abierta. El argumento de que "el contrato útil es el que limita unidades" queda respaldado por un caso donde el contrato público limita **lo otro** —la cadencia— y aun así el recurso no es gobernable, porque **un techo de 8 QPS con un pool de un dominio no limita nada de lo que importa**: ni las unidades, ni el riesgo de que el único dominio se bloquee. Es la lectura de governance completa: **cadencia, unidades y diversidad de pool son tres ejes de contrato distintos**, y un proveedor puede publicar uno y callar los otros dos.
