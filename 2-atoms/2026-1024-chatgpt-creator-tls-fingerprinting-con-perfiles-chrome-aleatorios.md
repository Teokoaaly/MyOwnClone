---
id: 2026-1024-chatgpt-creator-tls-fingerprinting-con-perfiles-chrome-aleatorios
type: atom
certainty: solid
sources: [sources/2026-10-24-chatgpt-creator-verssache.md]
links: ["[[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]]", "[[2026-1023-hero-sms-ip-y-vpn-coincidentes-con-el-pais-del-numero]]", "[[2026-1024-dataimpulse-sesiones-rotating-y-sticky]]"]
---

## Claim
Una de las siete features declaradas es **"TLS Fingerprinting — Randomized Chrome TLS profiles to avoid detection"**. La estructura de archivos le da un módulo propio: `internal/chrome/profiles.go  # Chrome TLS profile randomization`, consumido por `internal/register/client.go  # HTTP client with TLS fingerprinting`. El README también declara **"Proxy Support — Optional HTTP/SOCKS proxy for all requests"**, y la sección de configuración confirma que la variable de entorno **`PROXY` sobrescribe el valor del proxy del archivo de configuración**. El README es explícito sobre el propósito declarado: el perfil TLS se aleatoriza **"to avoid detection"**.

## Why It Matters
Este es el **mecanismo de elusión de primer orden del sector**, y es distinto del que el thread venía documentando. Todo lo que había en el thread era elusión de **red y de identidad**: IP que coincida con el país del número, VPN, proxy ([[2026-1023-hero-sms-ip-y-vpn-coincidentes-con-el-pais-del-numero]]), sesiones rotating o sticky ([[2026-1024-dataimpulse-sesiones-rotating-y-sticky]]). Aquí aparece la capa que está **por debajo de la IP**: la huella TLS del cliente.
La consecuencia es precisa y no es trivial: **cambiar de IP no basta si el cliente HTTP sigue siendo el mismo**. Un fingerprint TLS identificable es una señal estable que sobrevive al cambio de proxy, y el propio autor del bot lo ha colocado como feature de primer nivel en un repositorio con 338 estrellas. Eso significa que el coste real de un flujo de alta a escala no es solo el del proxy por gigabyte, sino también el de **construir o untruear un cliente que no se parezca a Go por defecto**.
Para el vault, esto cierra el círculo con el resto del thread en un punto que ya estaba abierto: la §8 del thread decía que **el número de altas, no el de bytes, es lo que escala**; esta fuente añade que el proxy por sí solo no desactiva la detección, y que hay una capa de software entre el proxy y el registro.
Y es el mismo tipo de razonamiento que el vault ya aplicó al captcha —"elegir por el tipo de captcha que aparece en el destino" en vez de por precio—: aquí el criterio de selección sería el del **tipo de señal de detección que aparece en el destino**, no el del país del proxy.

## Nota de verificación
El README declara la feature y el árbol de archivos confirma los dos módulos. La captura **no revela qué librería o biblioteca se usa** para la aleatorización de perfiles TLS (el `go.mod` no está capturado), ni los valores de los perfiles, ni su número. El vault no puede afirmar que la aleatorización sea eficaz contra la detección actual de OpenAI.


## Nota de extensión 2026-10-26
La captura del 2026-10-25 de `https://github.com/Kaliiiiiiiiii-Vinyzu/patchright` (README del repositorio, 2442 palabras) **añade una segunda vía de elusión de cliente** que este átomo no contemplaba, y la vía es de una naturaleza distinta: aquí la huella no se imita en el cliente HTTP, **se elimina en el navegador**.

Patchright no aleatoriza perfiles TLS: **parchea el driver de Playwright**. Su parche principal —"the biggest Patch Patchright uses"— consiste en **no usar nunca `Runtime.enable`** y ejecutar el JavaScript en ExecutionContexts aislados ([[2026-1026-patchright-evita-runtime-enable-con-contextos-de-ejecucion-aislados]]). A eso se suman el ajuste de command flags (`--disable-blink-features=AutomationControlled` añadido, `--enable-automation` eliminado) ([[2026-1026-patchright-command-flags-automation-controlled-y-habilitacion-de-funciones]]), la **deshabilitación total de la Console API** —con el coste explícito de que "console functionality will not work in Patchright" ([[2026-1026-patchright-deshabilita-la-api-de-console-como-parche]])— y el soporte de shadow roots cerrados con XPath ([[2026-1026-patchright-closed-shadow-roots-con-xpath]]).

**Lo que esto corrige en este átomo es el alcance de la frase "la huella del cliente no se compra en ninguna parte".** Es cierto en la capa de transporte: el `chatgpt-creator` tiene que construir la imitación TLS en Go porque su cliente es Go. Pero existe una **capa de navegador** donde esa ingeniería **ya está hecha, publicada y es gratuita**: Patchright es Apache 2.0, con 1.036 commits, 5.0k estrellas y releases automáticas tras cada versión de Playwright ([[2026-1026-patchright-mil-commits-y-cinco-mil-estrellas-actividad-activa]]), y se distribuye en Python, NodeJS y .Net ([[2026-1026-patchright-fork-parcheado-de-playwright-como-sustituto-directo]]).

**La conclusión operativa que hay que corregir en el vault:** el coste de la elusión no es "no existe", sino que **cambia de forma según la arquitectura del cliente**. Un bot HTTP puro tiene que construir la huella TLS porque no hay navegador que parchear; un pipeline con navegador la compra como dependencia open source. La consecuencia para el modelo de coste del thread es que **la partida "ingeniería de evasión" no es un coste fijo de la operación, es un coste condicional a la arquitectura que se elija** — y por tanto **no puede aparecer en la tabla de coste por insumo como si fuera una línea más**.


## Nota de extensión 2026-10-26
La captura del 2026-10-25 de `berstend/puppeteer-extra` **acota el alcance de la afirmación "el fingerprinting no se compra en ninguna parte"**, que este átomo sostiene para el cliente HTTP del bot, extendiéndola a un nivel de señal distinto.

El README del monorepo describe una granularidad de evasions que **no existe en el bot Go**: cada evasión es un artefacto con nombre, ruta y **test propio** —el bloque de desarrollo incluye `cd packages/puppeteer-extra-plugin-stealth` y `yarn ava -v ./evasions/user-agent-override/index.test.js`— y además existe un sub-paquete aparte, **`extract-stealth-evasions@2.7.3`**, con su propio ciclo de versión ([[2026-1026-puppeteer-extra-stealth-y-extract-stealth-evasions-como-paquetes-separados]]).

**La extensión es de capa, no de refutación.** Lo que este átomo mide —"TLS Fingerprinting — Randomized Chrome TLS profiles to avoid detection", y la conclusión de que la huella del transporte HTTP no está en ningún catálogo— **sigue en pie** para el nivel que el bot tiene que construir a mano: el cliente HTTP con perfiles TLS aleatorizados no se compra en ninguna parte, y `puppeteer-extra` no lo vende. Lo que la captura añade es que **el nivel del navegador es distinto**: ahí la elusión sí está publicada como commodity con versión, y con un test por evasión, lo que indica que la pieza es tratable como unidad.

La distinción que conviene dejar escrita para el vault: **"la huella no se compra" es una afirmación sobre un nivel concreto de señal —el transporte y la instrumentación del cliente— y no sobre el nivel del navegador**, donde existe commodity abierta. Y el matiz decisivo: **la granularidad de las evasions no equivale a cobertura**. La captura **no enumera qué evasions existen** ni su cobertura de señales, de modo que no puede sostenerse que el paquete MIT resuelva lo mismo que el fingerprinting del bot.


## Nota de extensión 2026-10-26
La captura de `sources/2026-10-25-rebrowser-patches.md` añade un **contraplante a la misma categoría**: el bot de Go evade con **huella TLS del cliente HTTP** (construcción desde cero, en Go, sin navegador), mientras que `rebrowser/patches` evade parcheando **el código fuente de Puppeteer y Playwright** —otra capa, la del protocolo CDP, y no la del transporte. La fuente enumera la fuga que el parche neutraliza: el uso del comando CDP `Runtime.Enable`, *"used by all major anti-bot software such as Cloudflare, DataDome"*, detectable con *"a few lines of JavaScript on the page"*. Añadir al *Why It Matters*: **la huella del cliente y la del navegador son señales distintas con capas de coste distintas** — la primera se construye, la segunda se neutraliza parcheando, y el parche se paga en **mantenimiento por release**, no en ingeniería. Ver [[2026-1026-rebrowser-parchea-el-codigo-fuente-porque-no-hay-configuracion-que-lo-arregle]] y [[2026-1026-rebrowser-runtime-enable-la-fuga-que-usan-todos-los-antibot]].
