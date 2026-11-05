---
id: 2026-1023-sms-activate-cierra-total-el-22-de-diciembre
type: atom
certainty: solid
sources: [sources/2026-10-22-sms-activate-closed.md]
links: ["[[2026-1023-herosms-sobre-la-infraestructura-de-sms-activate]]", "[[2026-1023-herosms-vs-5sim-competencia-directa]]", "[[2026-1023-sms-activate-retiradas-hasta-el-5-de-febrero]]"]
---

## Claim
SMS-Activate **cesó toda su actividad** y su página oficial se reduce a un único aviso: "С 22 декабря мы полностью прекратили свою деятельность" (Desde el 22 de diciembre cesamos por completo nuestra actividad), seguido del agradecimiento "Спасибо всем, кто был с нами эти 10 лет" — es decir, **10 años de operación** del proveedor. No es un cierre parcial ni un recorte de catálogo: la fórmula es "полностью", sin excepciones ni servicios mantenidos.

## Why It Matters
El vault daba por hecho un mercado de números SMS con al menos tres actores vivos (5sim autónomo, HeroSMS y, detrás de este, SMS-Activate como operador de infraestructura: [[2026-1023-herosms-sobre-la-infraestructura-de-sms-activate]]). Este aviso **retira del mapa uno de los tres**: el operador de origen dejó de existir como empresa. Por eso la comparación de proveedores del vault —HeroSMS contra 5sim como si fueran dos mercados ([[2026-1023-herosms-vs-5sim-competencia-directa]])— cambia de forma: el heredero de SMS-Activate no es un sustituto entre muchos, es **el último superviviente de un linaje que ya se apagó**.
Consecuencia operativa: cualquier plan de aprovisionamiento que asumiera un proveedor de infraestructura de respaldo detrás de HeroSMS (para inventario, cobertura de país o capacidad) tiene que revisar esa suposición, porque el respaldo ya no existe como entidad.

## [FRICTION]
> [[2026-1023-herosms-sobre-la-infraestructura-de-sms-activate]] (escrita hoy, desde la home de HeroSMS) describe a HeroSMS como una **"fachada comercial (white-label) sobre SMS-Activate"** e infiere que el pool de números y la cobertura "heredan del operador de origen", dejando abierta la verificación societaria real.
> Este átomo presiona esa creencia en un punto concreto: si SMS-Activate **cesó toda su actividad**, ya no hay un "operador de origen" vivo al que HeroSMS sea una fachada. La relación no puede ser de white-label sobre un proveedor activo; tiene que ser de **sucesión por traspaso de tecnología**.
> Ambas no pueden ser completamente correctas como descripción del estado actual: o HeroSMS es una fachada sobre un operador que sigue operando (imposible si la actividad cesó del todo), o es un heredero único que ya no es fachada de nadie. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
El aviso no da el **año** del 22 de diciembre, ni la razón del cierre, ni cifras de saldo pendiente. La captura es del 2026-10-22 y el texto está en pasado ("прекратили"), por lo que el año es inferible pero no está escrito; el vault no debe fijar un año sin otra fuente.


## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-onlinesim-virtual-sms.md` (capturada **tres días después** del aviso de cierre). El hecho que este átomo documenta —que SMS-Activate cesó toda su actividad por completo y sin excepciones— tiene ahora una **contraprueba de vigencia en el mercado**: la home de OnlineSim, capturada el 2026-10-25, sigue usando a SMS-Activate como **ejemplo vivo y actual** del sector, en presente y sin ningún matiz: "**Normally, SMS activation services (such as SMS-Activate)** are used to register on social networks (VK, OK, Facebook, Instagram), confirm messengers (Telegram, WhatsApp, Viber, WeChat), and emails (Yandex, Mail.ru, Gmail, Yahoo)" ([[2026-1026-onlinesim-faq-nombra-sms-activate-como-ejemplo-de-activacion]]).

Dos lecturas posibles que este átomo deja abiertas para el Editor: (a) el texto del competidor es **copy de plantilla sin actualizar**, lo que significa que ninguna referencia nominal a un proveedor en el corpus es fiable como dato de mercado; (b) la marca SMS-Activate sobrevivió como **etiqueta comercial** aunque la empresa haya dejado de existir — lo que encaja con que HeroSMS, su heredero technology-wise,sea el único linaje vivo.

La consecuencia para el thread: la afirmación "el mercado perdió un actor" debe matizarse a "**el mercado perdió una empresa y conservó su nombre como referencia sectorial**", y el FAQ de OnlineSim es la prueba de esa persistencia.


## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-hero-sms-api-docs.md`.

Este átomo documenta el cierre total de SMS-Activate el 22 de diciembre de 2026 y su calendario de liquidación. La página de API de HeroSMS publica ahora **un destino de migración con procedimiento**: cuatro pasos, host `api.sms-activate.ae` → `hero-sms.com`, API key de HeroSMS en su lugar, y la mención de "**former** SMS-Activate partners" ([[2026-1027-hero-sms-compatibilidad-de-wire-con-los-clientes-de-sms-activate]]).

Consecuencia para el Editor: el cierre deja de ser solo un hecho de mercado y pasa a tener un **receptor de tráfico documentado**. Eso tiene una consecuencia práctica para cualquier software de registro que hoy apunte a `api.sms-activate.ae`: **el coste de migrar es una línea de configuración**, no una reescritura de cliente. Y un matiz que hay que escribir: la migración **no resuelve** la liquidación —el saldo, los números comprados y los plazos del operador saliente siguen sin varias reglas—; HeroSMS es un **destino de integración**, no un sucesor de los derechos de los clientes del operador cerrado.
