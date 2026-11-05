=== EXTEND 2-atoms/2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible
## Nota de extensión 2026-10-26
La captura del 2026-10-25 de `berstend/puppeteer-extra` (7.4k estrellas, 604 commits, 559 tags, 783 forks) aporta el **contrapunto de escala** que a este átomo le faltaba: el patrón "popularidad sin mantenimiento" no es unívoco, y hay que distinguir dos formas de él.

Este átomo mide `verssache/chatgpt-creator` en **338 estrellas, 90 forks, 4 commits, 1 branch, 0 tags, 0 releases** — es decir, un proyecto que **nunca publicó un artefacto versionado**. El caso de `puppeteer-extra` es el reverso exacto en el eje del versionado: **604 commits, 559 tags, 5 branches**, con un commit de publicación explícito ("Publish", `39248f1`, 1 de marzo de 2023) que enumera seis paquetes con su versión — `puppeteer-extra@3.3.6`, `puppeteer-extra-plugin-recaptcha@3.6.8`, `@extra/proxy-router@3.1.6`, `extract-stealth-evasions@2.7.3`, `puppeteer-extra-plugin-anonymize-ua@2.4.6`, `puppeteer-extra-plugin-devtools@2.4.6` —([[2026-1026-puppeteer-extra-seis-paquetes-y-esus-versiones-en-el-commit-de-publicacion]]).

**La extensión es de matiz, no de corrección.** La lección que este átomo extrae ("7.4k estrellas no son mantenimiento") se mantiene intacta: `puppeteer-extra` está **congelado desde marzo de 2023**, tres años y medio antes de la captura, y su `package.json` no se toca desde el **21 de septiembre de 2021** ([[2026-1026-puppeteer-extra-604-commits-559-tags-y-ultimo-commit-en-marzo-de-2023]]). Pero hay que añadir una distinción que este átomo no hacía: **"popularidad sin mantenimiento" y "sin proceso de release" son dos defectos distintos, y no se pueden tratar como el mismo**. Un proyecto con 559 tags y sin commits nuevos deja al consumidor con **un último artefacto conocido y auditable**; un proyecto con 4 commits y 0 tags deja al consumidor **sin ninguna versión a la que anclarse**, siempre en `main`.

Eso importa para el vault porque las dos situaciones piden **políticas de consumo opuestas**: en el primer caso, fijar la última versión y aceptar que no habrá más; en el segundo, clonar y auditar el código entero. La formulación que conviene evitar es "código congelado = riesgo equivalente" ([[2026-1026-puppeteer-extra-flujo-de-publicacion-por-lerna-con-npm-y-no-yarn]]).
=== END

=== EXTEND 2-atoms/2026-1024-github-search-noventa-y-cuatro-por-ciento-de-las-estrellas-en-tres-repos
## Nota de extensión 2026-10-26
La captura del 2026-10-25 de `berstend/puppeteer-extra` **confirma desde el extremo opuesto** la lectura que este átomo hace del ratio forks/estrellas, y le añade un punto de referencia que el corpus no tenía.

Este átomo mide el ratio en tres repositorios de la consulta: **0,51** en `gptGrok2api` (145/285), **0,50** en `wahdalo/chatgpt-account-creator` (69/139) y **0,27** en `verssache/chatgpt-creator` (90/338), y lo lee como señal de que "el uso dominante de estas herramientas es copiar y modificar, no instalar y mantener". `puppeteer-extra` da **783 forks sobre 7.4k estrellas, un ratio de 0,11** — el más bajo del corpus y **2,6 a 4,8 veces menor** que los tres anteriores ([[2026-1026-puppeteer-extra-783-forks-sobre-7-4k-estrellas-un-ratio-de-0-11]]).

**La extensión es de alcance, no de corrección.** El indicador funciona: donde hay paquete publicado, el ratio de forks baja porque la gente **instala**; donde hay un script suelto, sube porque la gente **copia**. Pero hay que añadir la **variable que este átomo no controlaba**: el ratio por sí solo no dice nada si no se acompaña del **modelo de distribución** del proyecto. En `puppeteer-extra` el ratio 0,11 convive con 604 commits y 559 tags, es decir, con un ciclo de release real por paquete; en los tres repos de la consulta convive con 4 commits y 0 tags. La regla operativa que sale de las dos capturas juntas es: **ratio bajo + versionado = proyecto que se instala y se fija; ratio alto + sin versionado = plantilla que se copia**.

Dato de precisión: 7.4k es una cifra redondeada por la propia GitHub, de modo que el 0,11 es una aproximación calculada por el vault sobre valores publicados, y la captura no expone `stargazers_count` en entero.
=== END

=== EXTEND 2-atoms/2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha
## Nota de extensión 2026-10-26
La captura del 2026-10-25 de `berstend/puppeteer-extra` **no añade precios**, pero añade una alternativa de arquitectura que este átomo no tenía en cuenta, y por tanto obliga a matizar la frase "el captcha es la partida más barata y la más fácil de cotizar" en un punto preciso: **el captcha no es siempre una partida**.

Entre los diez paquetes que la captura permite nombrar del ecosistema (`puppeteer-extra`, `puppeteer-extra-plugin`, `puppeteer-extra-plugin-stealth`, `puppeteer-extra-plugin-recaptcha`, `puppeteer-extra-plugin-adblocker`, `puppeteer-extra-plugin-user-data-dir`, `@extra/proxy-router`, `puppeteer-extra-plugin-anonymize-ua`, `puppeteer-extra-plugin-devtools`, `extract-stealth-evasions`) hay un **`puppeteer-extra-plugin-recaptcha@3.6.8`** con su propio número de versión ([[2026-1026-puppeteer-extra-catalogo-de-plugins-numerados-en-la-captura]]). Es decir: existe una **vía de resolución de captcha publicada como paquete con licencia MIT**, en la que el coste marginal por captcha resuelto no es el de un catálogo, sino el de la instalación.

**La extensión es de alcance y lleva la discusión al plano de la decisión, no del precio.** La tabla de precios de este átomo sigue siendo válida y sigue siendo la única forma de cotizar el captcha **comprado**; lo que hay que añadir es que **"el captcha se paga" solo es cierto si la arquitectura de elusión es la del bot HTTP**, donde el captcha hay que resolverlo con un servicio externo. En una arquitectura de navegador con plugins, el captcha es un módulo más y su coste no está en ninguna tabla.

La fricción queda abierta y para juicio humano, porque **la captura no documenta qué hace el plugin recaptcha**: ni qué tipos resuelve, ni si usa un solver de pago por debajo, ni su tasa de éxito. El vault **no puede** afirmar que la vía gratuita cubra los mismos casos que el catálogo de $0.5 — $50 por 1000. Lo que sí puede afirmar es que **el catálogo de precios mide el coste de una elección de arquitectura y no el de una necesidad** ([[2026-1026-puppeteer-extra-stealth-y-extract-stealth-evasions-como-paquetes-separados]]).
=== END

=== EXTEND 2-atoms/2026-1024-chatgpt-creator-tls-fingerprinting-con-perfiles-chrome-aleatorios
## Nota de extensión 2026-10-26
La captura del 2026-10-25 de `berstend/puppeteer-extra` **acota el alcance de la afirmación "el fingerprinting no se compra en ninguna parte"**, que este átomo sostiene para el cliente HTTP del bot, extendiéndola a un nivel de señal distinto.

El README del monorepo describe una granularidad de evasions que **no existe en el bot Go**: cada evasión es un artefacto con nombre, ruta y **test propio** —el bloque de desarrollo incluye `cd packages/puppeteer-extra-plugin-stealth` y `yarn ava -v ./evasions/user-agent-override/index.test.js`— y además existe un sub-paquete aparte, **`extract-stealth-evasions@2.7.3`**, con su propio ciclo de versión ([[2026-1026-puppeteer-extra-stealth-y-extract-stealth-evasions-como-paquetes-separados]]).

**La extensión es de capa, no de refutación.** Lo que este átomo mide —"TLS Fingerprinting — Randomized Chrome TLS profiles to avoid detection", y la conclusión de que la huella del transporte HTTP no está en ningún catálogo— **sigue en pie** para el nivel que el bot tiene que construir a mano: el cliente HTTP con perfiles TLS aleatorizados no se compra en ninguna parte, y `puppeteer-extra` no lo vende. Lo que la captura añade es que **el nivel del navegador es distinto**: ahí la elusión sí está publicada como commodity con versión, y con un test por evasión, lo que indica que la pieza es tratable como unidad.

La distinción que conviene dejar escrita para el vault: **"la huella no se compra" es una afirmación sobre un nivel concreto de señal —el transporte y la instrumentación del cliente— y no sobre el nivel del navegador**, donde existe commodity abierta. Y el matiz decisivo: **la granularidad de las evasions no equivale a cobertura**. La captura **no enumera qué evasions existen** ni su cobertura de señales, de modo que no puede sostenerse que el paquete MIT resuelva lo mismo que el fingerprinting del bot.
=== END

=== EXTEND 2-atoms/2026-1024-dataimpulse-sesiones-rotating-y-sticky
## Nota de extensión 2026-10-26
La captura del 2026-10-25 de `berstend/puppeteer-extra` muestra que **el enrutado de proxy —el trabajo que este átomo describe como geometría de sesión a resolver— existe además como plugin publicado y versionado**: `@extra/proxy-router@3.1.6`, añadido el **8 de agosto de 2022** con el commit "feat: Add plugin proxy-router (#693)" ([[2026-1026-puppeteer-extra-plugin-proxy-router-anadido-en-agosto-de-2022]]).

**La extensión es de alcance y no altera el átomo.** Este átomo mide la geometría de sesión en el proveedor comercial —rotating frente a sticky, con la sesión como unidad real de trabajo y no el gigabyte— y eso no cambia: la captura no publica el comportamiento del plugin, ni los esquemas de proxy que admite, ni los proveedores que soporta. Lo que añade es un dato de **reutilización**: la parte del pipeline que en una implementación propia es "cablear rotación de IPs y autenticación por URL" **tiene una implementación publicada con número de versión**, y por tanto es un `npm install` en lugar de código que escribir y mantener.

Eso redondea una observación que el vault ya tenía en piezas sueltas (el captcha como commodity abierta, el fingerprint como construcción obligatoria, el proxy como partida y como código): **la capa de elusión tiene un reparto distinto en cada nivel**, y ese reparto es el que debería decidir la arquitectura, no el precio unitario de ningún insumo.
=== END
