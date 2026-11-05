# Propuesta de hilo — captura `2026-10-25-heroku-support-home.md`

Fuente: `sources/2026-10-25-heroku-support-home.md` (`https://support.heroku.com/`, capturada 2026-10-25).
Átomos nuevos de esta captura: 11 (todos en `2-atoms/`, prefijo `2026-1026-`).
Extensiones propuestas: 2 (en `1-desk/extend-heroku-support-home.md`).

---

## Propuesta A — `escala-de-hosting-barato-y-el-limite-de-4-euros`

```markdown
### El soporte como línea de producto: lo que no cabe en 4 € y no tiene precio en ninguna parte

La captura de `https://support.heroku.com/` (2026-10-25) documenta la parte del PaaS enterprise que ninguna tabla de precios captura: **la línea de soporte**, con sus catorce categorías, sus puertas de acceso y sus tres canales.

Lo primero que hay que registrar es que **esta captura no publica un solo euro**. Ni del soporte, ni de los planes, ni de nada. Publica una **taxonomía**: catorce categorías con identificador numérico estable —General Platform Features (236), Account Management (5), Domains & Routing (8), Security (12), Billing, Verification & Payments (2), Heroku Postgres (3), Heroku Connect (10), Heroku Key-Value Store (22), Apache Kafka on Heroku (21), Heroku AppLink (538), CI, Pipelines & Review apps (15), Platform Error Codes (248), Command Line Tools (268) y Add-on Provider (533)— ([[2026-1026-heroku-soporte-catorce-categorias-con-identificadores-numericos]]). Y el reparto es el dato: **cuatro categorías son de datos gestionados y dos son de identidad y facturación**, es decir, la misma línea que el vault ya midió en euros ([[2026-1026-heroku-postgres-essential-5-a-20-dolares-con-4-horas-de-parada]], [[2026-1026-heroku-kafka-desde-100-dolares-con-1-semana-de-retencion]]) es la línea que más soporte come.

Lo segundo, y es la corrección de fondo para este thread: **el soporte de Heroku no es un extra sobre el precio del servidor, es un producto con su propio circuito comercial**. Tres planes nombrados —Standard, Premier, Signature— con la única promesa "faster response times", sin precio, sin SLA y sin tiempo de respuesta publicado ([[2026-1026-heroku-soporte-basico-gratis-y-success-plans-enterprise]]); un directorio propio para clientes Enterprise, `help.heroku.com/enterprise`, distinto de "My tickets" y de "Create a ticket" ([[2026-1026-heroku-enterprise-resources-como-seccion-propia-del-soporte]]); y el estado Enterprise aparece además en el Marketplace de add-ons, donde un crédito equivale a $1 y solo es usable por clientes Enterprise ([[2026-1026-heroku-elements-1-credito-igual-a-1-dolar-solo-enterprise]]), y en Heroku Connect, donde las ediciones Enterprise y Shield son exclusivas de ese estado ([[2026-1026-heroku-connect-demo-gratis-y-ediciones-enterprise-exclusivas]]). **En Heroku, "enterprise" no es un escalón de precio: es un estado de cuenta, y el conjunto de puertas que se abren por tenerlo es lo que se compra — y ninguna de esas puertas tiene precio publicado.**

Y el dato de modelo de servicio que este thread necesita: **el mostrador de Heroku tiene una puerta disuasoria en su propio artículo más leído**. El primer "trending article" del portal es "Before opening a support ticket" ([[2026-1026-heroku-soporte-articulo-mas-tendido-es-instruccion-para-no-abrir-ticket]]), y las dos alternativas al ticket son la documentación pública y **Stack Overflow con la etiqueta `heroku`**, que la página ofrece *antes* que la vía de ticket ([[2026-1026-heroku-soporte-canales-externos-stackoverflow-y-pagina-de-estado]]). El modelo es: **documentación pública + comunidad pública indexable + ticket de pago enrutado a "the best person"**, con la inspección previa como filtro. Frente al ticket 24/7 con chat en horario de un hosting de 1,25 €/mes, la lectura de coste es incómoda: **el tramo barato del vault compra el servidor; el tramo enterprise paga por no tener que operar y por una prioridad de cola que no está cuantificada en ninguna página.**

Una consecuencia operativa que solo aparece en el soporte: **el ciclo de upgrade del producto gestionado puede romper el canal cifrado de las apps**. "Heroku Key-Value Store Upgrade - SSL/TLS Connection Issues" está entre los cinco contenidos más leídos de Heroku ([[2026-1026-heroku-key-value-store-upgrade-con-problemas-de-ssl-tls]]). Los 25 planes del Key-Value Store, desde Mini $3, declaran todos "High availability with low-latency failover" ([[2026-1026-heroku-key-value-store-mini-3-dolares-hasta-12500]]) — pero la alta disponibilidad no cubre la transición de versión, que es un evento único. Para el producto propio, que autoaloja su Redis sobre nginx ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]), esa es exactamente la clase de dependencia que el choix de infraestructura propia elimina.

Y el dato de cadencia que cierra la escala: **Heroku decide cuándo un runtime deja de soportarse**. Entre los cinco artículos más leídos está el "Heroku-22 End-of-Life FAQ" ([[2026-1026-heroku-22-end-of-life-faq-como-articulo-de-tendencia]]), y el changelog del portal publica números de versión con el default de las apps nuevas como métrica separada —Ruby 3.4.12, seis SDK de .NET de 8.0.133 a 10.0.403, seis JDK de 1.8.0_512 a 27.0.1 ([[2026-1026-heroku-changelog-de-runtimes-ruby-3-4-12-opjdk-y-dotnet]]). **El precio del PaaS no es solo el dyno: es el derecho a seguir usando un runtime que el proveedor puede cerrar.** Es la versión enterprise de la obsolescencia forzada, y no aparece en ninguna tabla.
```

THREAD: escala-de-hosting-barato-y-el-limite-de-4-euros

---

## Propuesta B — `economia-de-la-verificacion-y-reventa-de-cuentas`

```markdown
### La otra mitad del alta: la credencial no la crea el formulario, la crea el mostrador

La captura de `https://support.heroku.com/` (2026-10-25) cierra la historia del alta de Heroku que quedó abierta en la captura de `signup.heroku.com`, y la cierra en la dirección más incómoda para la reventa de cuentas.

El dato duro es que **el soporte de Heroku ofrece "Reset my MFA" como una de sus tres acciones de primer nivel** —junto a "General query" y "Account & billing"— y que entre los cinco artículos más leídos del portal está **"What should I do if I'm locked out of my Heroku account?"** ([[2026-1026-heroku-lockout-de-cuenta-entre-los-cinco-articulos-mas-leidos]], [[2026-1026-heroku-soporte-tres-acciones-rapidas-general-query-reset-mfa-y-account-billing]]).

Con eso, la secuencia queda así: el alta en `signup.heroku.com` **no pide contraseña** y no publica verificación de correo ([[2026-1026-heroku-alta-en-signup-y-login-en-id-dominio-separado]], [[2026-1026-heroku-alta-sin-plan-ni-precio-ni-dyno-ni-verificacion-de-correo]]); el login vive en `id.heroku.com`, otro dominio ([[2026-1026-heroku-alta-en-signup-y-login-en-id-dominio-separado]]); el alta está cerrada por un reCAPTCHA Enterprise de imágenes que **reemite el desafío** ([[2026-1026-heroku-recaptcha-enterprise-con-re-desafio-dinamico-de-imagenes]]); y la credencial y su segundo factor se gestionan en `id.heroku.com` con el soporte como punto de recuperación. **La cadena de identidad de una cuenta de infraestructura enterprise no está en la página del alta: está repartida entre un dominio de identidad, un captcha de re-desafío y un mostrador de tickets.**

La consecuencia para este thread es directa y es la parte que la §7 no tenía: **la verificación de una cuenta Heroku no es un coste de entrada que se pueda pagar y olvidar — es un proceso vivo con categoría propia en el manual** ("Billing, Verification & Payments", `n/2`) ([[2026-1026-heroku-soporte-categoria-billing-verification-y-payments]]). Es la diferencia entre el modelo de NoOnes, donde la identidad verificada **es** la capacidad y se paga como producto ([[2026-1024-noones-verificacion-basica-l1plus-revision-manual-hasta-72h]]), y el de un PaaS, donde la verificación se sostiene con soporte humano y **no tiene precio porque su función es condicionante de la facturación del plan**.

Y de aquí sale la objeción más dura que este thread puede hacer al business de la reventa de cuentas: **una cuenta cuyo lockout es un top-5 de soporte y cuyo MFA se resetea en el mostrador del proveedor no es un activo transferible**. La primera línea de defensa del titular es la que bloquea, y el desbloqueo es una petición al original. Comprar una cuenta de infraestructura es comprar una **posición en una cola de recuperación ajena** — exactamente la clase de pasivo que el corpus de reventa de cuentas de IA ya asume en su forma más blanda ([[2026-1023-lzt-categoria-llm-accounts-para-reventa]]).

Hay una última pieza, de capa legal, que cierra el argumento: **no hay entidad legal bajo la que un comprador pueda reclamar**. Los Términos de Servicio de Heroku se sirven como PDF desde `trailblazer.me` —el dominio de Trailhead, la plataforma de formación de Salesforce—, la Privacidad y las Cookies cuelgan de `salesforce.com`, el copyright es "© 2026 Salesforce.com" y el formulario de derechos de dato es `salesforce.com/form/other/privacy-request/` ([[2026-1026-heroku-soporte-superficie-legal-en-trailblazer-y-salesforce]]). El pie del alta ya declaraba que "your personal data will be processed by Salesforce" ([[2026-1026-heroku-tres-variantes-de-privacy-por-region-y-consentimiento-de-marketing]]). Es el simétrico exacto del caso del producto propio, cuyo Aviso Legal declara "Vercel Inc." mientras la infraestructura real es nginx en una IP ([[2026-1023-live-verify-aviso-legal-aun-declara-vercel]]): **la capa legal va por detrás del stack real**, y en el caso de Heroku el desfase es de processor, no de proveedor de infraestructura. La asimetría reveladora es que **Heroku sí publica política de seguridad bajo su marca** (`heroku.com/policy/security/`), pero condiciones y datos bajo la de Salesforce.
```

THREAD: economia-de-la-verificacion-y-reventa-de-cuentas

---

## Propuesta C — `myownclone-platform-architecture`

```markdown
### La capa de soporte como parte de la arquitectura: qué pasa cuando el PaaS te rompe el canal cifrado

La captura de `https://support.heroku.com/` (2026-10-25) aporta a este thread una evidencia que no es de código sino de **contrato operativo**, y que toca una decisión de arquitectura ya tomada: **autoalojar los datos gestionados**.

El caso es concreto y está en la propia home de soporte de Heroku: **"Heroku Key-Value Store Upgrade - SSL/TLS Connection Issues" está entre los cinco contenidos más leídos del portal** ([[2026-1026-heroku-key-value-store-upgrade-con-problemas-de-ssl-tls]]). Es decir, **el ciclo de upgrade de un servicio de datos gestionado puede romper el canal cifrado de las apps existentes**. Y el catálogo del Key-Value Store, con sus 25 planes desde Mini $3 hasta Shield-14, declara en todos ellos "High availability with low-latency failover" ([[2026-1026-heroku-key-value-store-mini-3-dolares-hasta-12500]]). **La alta disponibilidad y el failover son estados; la transición de versión es un evento, y los eventos no están cubiertos por el estado.** Eso no lo dice el proveedor: lo dice la foto de su propia pantalla de soporte.

La lección de arquitectura, aplicada a este producto: **el riesgo no está en el runtime del dato, está en el canal y en quién puede cambiarlo**. Una app que habla con Redis por TLS tiene, en un PaaS gestionado, **dos variables de versión en producción**: la suya y la del proveedor, y la segunda la mueve un tercero en un día que el cliente no controla. Con nginx + Postgres + Redis autoalojados ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]) esa segunda variable no existe, y el vault no tiene que presupuestar el riesgo de un corte de servicio por cambio de versión del Redis de otro.

La segunda observación es de ciclo de vida, y va en la misma dirección: **Heroku declara EOL de runtime como contenido de soporte de primer nivel** —el "Heroku-22 End-of-Life FAQ" está entre los cinco artículos más leídos ([[2026-1026-heroku-22-end-of-life-faq-como-articulo-de-tendencia]])— y el changelog del portal publica el runtime por defecto de las apps nuevas como métrica separada (Ruby 3.4.12, seis SDK de .NET, seis JDK de 1.8.0_512 a 27.0.1) ([[2026-1026-heroku-changelog-de-runtimes-ruby-3-4-12-opjdk-y-dotnet]]). Es la misma forma de obsolescencia que ya se midió en las generaciones de cómputo: las familias Private/Shield de Cedar no valen para los espacios Fir ([[2026-1026-heroku-fir-dynos-kubernetes-todos-requieren-private-space-desde-25]]). **La diferencia con el stack propio es que aquí no hay nadie que pueda declarar EOL sobre la infraestructura**: no hay versión del runtime que una plataforma pueda retirar, ni una ventana de migración que el proveedor defina. Para un producto que vende clones de personas y cuyo activo es el corpus y el modelo, esa estabilidad del substrate es una decisión de arquitectura, no un detalle de despliegue.

Y el tercer elemento, que es de proceso y no de stack: **el soporte de un PaaS enterprise no es un extra, es un producto con circuito comercial propio** —tres planes Standard/Premier/Signature sin precio ni SLA publicado ([[2026-1026-heroku-soporte-basico-gratis-y-success-plans-enterprise]]), un directorio propio `help.heroku.com/enterprise` para clientes Enterprise ([[2026-1026-heroku-enterprise-resources-como-seccion-propia-del-soporte]]) y una puerta disuasoria en el propio artículo más leído del portal: "Before opening a support ticket" ([[2026-1026-heroku-soporte-articulo-mas-tendido-es-instruccion-para-no-abrir-ticket]]). La versión interna del producto es la contraria: **soporte gratis, asistido por IA, con SLA declarado** ([[2026-1022-soporte-al-cliente-separado-y-escalado]]). Es la diferencia entre un producto que compra su servicio de soporte y uno que lo es.
```

THREAD: myownclone-platform-architecture

---

## Nota para el editor

- No se ha modificado ningún fichero en `3-threads/`.
- Las tres propuestas son texto para insertar en los hilos indicados; los `THREAD:` de arriba identifican a cuál corresponde cada bloque.
- Átomos de la captura: `2026-1026-heroku-soporte-catorce-categorias-con-identificadores-numericos`, `2026-1026-heroku-soporte-tres-acciones-rapidas-general-query-reset-mfa-y-account-billing`, `2026-1026-heroku-soporte-articulo-mas-tendido-es-instruccion-para-no-abrir-ticket`, `2026-1026-heroku-soporte-canales-externos-stackoverflow-y-pagina-de-estado`, `2026-1026-heroku-soporte-categoria-billing-verification-y-payments`, `2026-1026-heroku-enterprise-resources-como-seccion-propia-del-soporte`, `2026-1026-heroku-soporte-superficie-legal-en-trailblazer-y-salesforce`, `2026-1026-heroku-changelog-de-runtimes-ruby-3-4-12-opjdk-y-dotnet`, `2026-1026-heroku-22-end-of-life-faq-como-articulo-de-tendencia`, `2026-1026-heroku-lockout-de-cuenta-entre-los-cinco-articulos-mas-leidos`, `2026-1026-heroku-key-value-store-upgrade-con-problemas-de-ssl-tls`.
- Extensiones propuestas (en `1-desk/extend-heroku-support-home.md`): `2026-1026-heroku-soporte-basico-gratis-y-success-plans-enterprise` y `2026-1026-heroku-tres-variantes-de-privacy-por-region-y-consentimiento-de-marketing`.
- Fricciones planteadas (3 pares, todas en átomos nuevos): `2026-1026-heroku-alta-en-signup-y-login-en-id-dominio-separado` ↔ `2026-1026-heroku-soporte-tres-acciones-rapidas-general-query-reset-mfa-y-account-billing`; `2026-1026-heroku-soporte-basico-gratis-y-success-plans-enterprise` ↔ `2026-1026-heroku-soporte-canales-externos-stackoverflow-y-pagina-de-estado`; `2026-1026-heroku-key-value-store-mini-3-dolares-hasta-12500` ↔ `2026-1026-heroku-key-value-store-upgrade-con-problemas-de-ssl-tls`; `2026-1026-heroku-alta-sin-plan-ni-precio-ni-dyno-ni-verificacion-de-correo` ↔ `2026-1026-heroku-soporte-categoria-billing-verification-y-payments`.
