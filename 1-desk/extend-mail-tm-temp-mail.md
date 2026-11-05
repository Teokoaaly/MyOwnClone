=== EXTEND 2-atoms/2026-1024-notletters-tres-vias-de-consumo-api-http-imap-y-web
## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-mail-tm-temp-mail.md` (home de `https://mail.tm/`, 698 palabras, capturada el 2026-10-25).

Este átomo sostiene que NotLetters **publica tres vías de consumo sin documentar ninguna**: web, HTTP API en `api.notletters.com` e IMAP en `imap.notletters.com` por el 993 con SSL. Mail.tm invierte el patrón en un punto exacto: **publica menos vías y además enlaza la documentación** —el nav lleva `API` → **`https://docs.mail.tm/`**, una URL de documentación, no un rótulo— y, en el bloque "Flexible", declara la capacidad que faltaba en NotLetters: "The latter [power users] get **API access** and a **quick way to register disposable mailboxes in bulk**" ([[2026-1026-mail-tm-alta-masiva-de-buzones-y-api-declaradas-en-la-home]]).

Consecuencia para el Editor: la observación "superficies sin especificación" del átomo **no es una regla del sector del correo**, sino de NotLetters y EmailOnDeck. Con tres capturas del sector, la formulación defendible pasa a ser: **el corpus de correo del vault tiene tres proveedores con tres comportamientos de documentación opuestos** —NotLetters (tres vías, cero documentación), EmailOnDeck (cero vías programables, cero especificación) y mail.tm (una vía enlazada a documentación, aunque sin cifras ni condiciones en la home). El matiz que **no** cambia: **el vault no ha abierto `docs.mail.tm/`**, de modo que sigue sin poder cotizar ninguna de las tres.
=== END

=== EXTEND 2-atoms/2026-1024-notletters-precio-005-rubles-por-correo-y-contadores-de-escala
## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-mail-tm-temp-mail.md`.

Este átomo fija **0.05 ₽ por correo** como precio de referencia del buzón de registro del corpus, con contadores de escala ("> 5 000 000" comprados, "> 30 000 000" recibidos) y tiempo medio de recepción de **573 Ms**. Mail.tm **no publica ningún precio** —el bloque "Free" dice "Every user gets full access to their temporary mailbox and an unlimited number of new ones. **No hidden conditions, no paid extras**"— y **no publica ningún tiempo de recepción**; lo único que ofrece es "Your temporary mailbox is **generated instantly**" y, en el nav, la línea de financiación: "You can support us by **disabling your ad blocker** on our site" ([[2026-1026-mail-tm-gratis-sin-cifras-con-financiacion-por-anuncios]]).

La consecuencia para el Editor es de **unidad de comparación**, no de precio: mail.tm introduce un **cuarto régimen de correo** en el corpus —**gratis, automatizable, y financiado con publicidad**— frente a los tres ya registrados (función de biblioteca del bot, NotLetters pago y automatizable, EmailOnDeck gratuito y manual). Mail.tm es el **único** que combina las dos propiedades que el thread usa para decidir si el correo es una partida cotizable: **coste monetario cero y superficie programable declarada**. Y con eso, el dato de los 573 Ms de NotLetters queda todavía más aislado: es el **único tiempo de recepción medido del corpus**, y la alternativa gratuita no publica ninguno.
=== END

=== EXTEND 2-atoms/2026-1024-chatgpt-creator-correo-temporal-y-otp-automatico-con-generator-email
## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-mail-tm-temp-mail.md`.

Este átomo establece la **función de biblioteca** del correo: el bot genera el buzón con `generator.email` —"Auto Email Generation — Generates temporary emails via generator.email or custom domains"—, recoge el OTP por polling y **no hay partida de correo que cotizar**. Mail.tm es el **proveedor externo que hace lo mismo sin código**, y además lo publica: el alta es un efecto colateral de abrir la página —"gives you an email address and a password for it **the moment you open the site**", "**no personal details required**", "**The mailbox is created automatically**"— y la credencial es "a **unique, automatically generated password**" ([[2026-1026-mail-tm-buzon-y-contrasena-nacen-al-abrir-el-sitio]]).

Consecuencia para el Editor: el átomo debe precisar su frase "el coste marginal de un buzón es cero". Con mail.tm, ese coste marginal cero **deja de ser una inferencia de diseño del bot y pasa a ser un hecho de mercado** —un proveedor lo ofrece gratis, con API y con documentación enlazada ([[2026-1026-mail-tm-alta-masiva-de-buzones-y-api-declaradas-en-la-home]]). Pero el coste no es cero en todas las dimensiones: mail.tm declara **40 MB de cuota por buzón** como única cifra de la página ([[2026-1026-mail-tm-unica-cifra-de-la-captura-40-mb-de-cuota]]) y **"kept forever" con "no limit" de unidades** ([[2026-1026-mail-tm-buzon-conservado-para-siempre-y-sin-limite-de-unidades]]), lo que convierte el buzón en **activo acumulativo** y no en consumible —la diferencia decisiva frente al modelo del bot, que retira y tira.
=== END

=== EXTEND 2-atoms/2026-1024-chatgpt-creator-blacklist-de-dominios-persistida-en-archivo
## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-mail-tm-temp-mail.md`.

Este átomo documenta la memoria de fallos del bot: un archivo `blacklist.json` donde persisten los dominios de correo que no funcionan. Mail.tm **no publica ni un solo dominio** en los 698 palabras de su home —ni en el texto, ni en el ejemplo de dirección, ni en los bloques de marketing— de modo que **el pool de dominios de mail.tm no es contable desde la captura** ([[2026-1026-mail-tm-unica-cifra-de-la-captura-40-mb-de-cuota]]).

Lo que mail.tm sí publica es **una segunda marca de dominio**: el nav enlaza **`Mail.gw`** (`https://mail.gw/`) junto a "Privacy Manager", `API` → `docs.mail.tm/`, FAQ, Privacy, Feedback y Contacts ([[2026-1026-mail-tm-mail-gw-como-marca-hermana-en-la-navegacion]]). Es decir, el sector tiene un proveedor cuya superficie se expresa **en marcas de dominio** y no en países ni en idiomas. Consecuencia para el Editor: la blacklist de dominios del bot y la lista de marcas del sector son **el mismo problema visto desde dos lados** —el bot persiste los dominios que fallan porque **un solo pool de dominios es un punto único de bloqueo**—, y mail.tm publica dos marcas precisamente como rotación de superficie. El matiz que hay que mantener: **la captura no dice qué es `mail.gw`**, no afirma que comparta operador ni dominios con mail.tm, y **no se ha visitado** `mail.gw/` ni `docs.mail.tm/`.
=== END

=== EXTEND 2-atoms/2026-1024-gptgrok2api-icloud-privacy-mail-fabrica-de-correo-con-techo-decreciente
## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-mail-tm-temp-mail.md`.

Este átomo sostiene que el sidecar de iCloud Privacy Mail es el **único ciclo de vida de buzón explícito del corpus** —20 buzones/hora en la interfaz nueva, 5/hora en la antigua, 25/hora sumando ambas, **tope de 750 buzones acumulados por cuenta**, temporizador de 60 minutos por ronda— y de ahí la tesis de que allí el correo es "un módulo con contrato".

Mail.tm publica el **modelo de ciclo de vida exactamente opuesto**, y de forma explícita: "The mailbox itself is **kept forever**; or delete it yourself, if that gives you more peace of mind" y "an **unlimited number** of new ones… **no limit** on how many disposable addresses you create" ([[2026-1026-mail-tm-buzon-conservado-para-siempre-y-sin-limite-de-unidades]]).

Consecuencia para el Editor: la tesis de "el contrato explícito es una feature del repo, no la norma del sector" **se refuerza y se complica**. Mail.tm no es silencioso como NotLetters ni contradictorio como EmailOnDeck —es **explícito y sin techo**, y lo declara en su home gratis. Así que hay **tres ciclos de vida declarados, no uno ausente**: techo y temporizador (sidecar), borrado constante con página de recuperación (EmailOnDeck), y conservación indefinida sin límite de unidades (mail.tm). Y el dato de seguridad que se sigue de esto es nuevo para el vault: **el buzón "kept forever" con clave propia es una credencial persistente, no un consumible** —Mail.tm promete que "Nobody but you can see what's inside", y eso solo es sostenible si la clave es realmente única y aleatoria, cosa que la captura **no** garantiza y que el uso que el propio vault tiene registrado de mail.tm **no cumple** ([[2026-1026-mail-tm-el-farm-del-vault-ya-lo-usa-con-dominio-propio-y-clave-determinista]]).
=== END

=== EXTEND 2-atoms/2026-1026-emailondeck-captura-minima-344-palabras-y-cero-especificacion-operativa
## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-mail-tm-temp-mail.md`.

Este átomo generaliza, tras dos capturas del sector, que "**una home de correo temporal no es una fuente de coste ni de rendimiento**" y la usa como **fuente de categoría**. La tercera captura del sector **obliga a matizar esa generalización en tres puntos verificables**:

1. **Una capacidad cuantificada aparece**: "**0 B/40 MB**", única cadena numérica de los 698 palabras ([[2026-1026-mail-tm-unica-cifra-de-la-captura-40-mb-de-cuota]]). No es precio ni rendimiento, pero sí es un límite de capacidad.
2. **Una documentación enlazada aparece**: `docs.mail.tm/`, y con ella la mención explícita de "API access" y de "a quick way to register disposable mailboxes in bulk" ([[2026-1026-mail-tm-alta-masiva-de-buzones-y-api-declaradas-en-la-home]]).
3. **Un ciclo de vida explícito aparece**: "kept forever", "unlimited number", "no limit" ([[2026-1026-mail-tm-buzon-conservado-para-siempre-y-sin-limite-de-unidades]]).

La formulación que el Editor debería dejar escrita: **"las homes de correo desechable no son fuentes de coste ni de rendimiento" sigue siendo cierto, pero ya no es cierto que no publiquen especificación operativa**. La regla correcta pasa a ser: **el coste sigue sin publicarse en ningún proveedor del sector**; lo que se publica es capacidad, documentación y ciclo de vida. Y el matiz metodológico que hay que conservar: la captura **no etiqueta** la cadena "0 B/40 MB", de modo que el vault puede citarla como **capacidad observada**, no como especificación.
=== END

=== EXTEND 2-atoms/2026-1026-emailondeck-casos-de-uso-de-consumo-y-no-de-registro-masivo
## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-mail-tm-temp-mail.md`.

Este átomo establece que EmailOnDeck **no menciona ni una vez** el registro masivo, el mercado de cuentas, la automatización ni una API, y que sus cinco usos declarados son de consumo (QA testing de emails, free trials, perfiles de citas, cripto). Mail.tm presenta **el otro extremo del mismo sector desde la propia home**: el bloque "Flexible" declara, para los "power users", "**API access** and a **quick way to register disposable mailboxes in bulk**", y enuncia como casos de uso "**running multiple accounts in online games, social networks** and elsewhere" —más "works for signing up on any website or service" y "Receive messages and **account activation codes**" ([[2026-1026-mail-tm-alta-masiva-de-buzones-y-api-declaradas-en-la-home]], [[2026-1026-mail-tm-correo-temporal-como-canal-de-codigos-de-activacion]]).

Consecuencia para el Editor: el corpus ya tiene **tres proveedores que sí declaran el registro masivo** (NotLetters con su banner "Great for Lolzteam Market", mail.tm con API y alta masiva, el bot con su generador propio) y **uno que no** (EmailOnDeck). La segmentación que este átomo documenta —consumo frente a alta— **es real, pero es una segmentación de los proveedores, no del producto técnico**: los dos extremos se sirven por el mismo tipo de objeto. Y el dato nuevo que hay que sumar es que mail.tm **declara el caso de uso "account activation codes"**, que es exactamente la partida que el vault necesita y que el bot resuelve por polling de OTP. El límite metodológico sigue igual: **no se ha abierto `docs.mail.tm/`**, de modo que la existencia y el alcance de la API son un **claim de home**.
=== END
