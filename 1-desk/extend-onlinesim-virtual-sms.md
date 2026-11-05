=== EXTEND 2-atoms/2026-1023-herosms-sobre-la-infraestructura-de-sms-activate
## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-onlinesim-virtual-sms.md`. Este átomo afirma que HeroSMS es una fachada white-label sobre SMS-Activate e infiere que "el pool de números y la cobertura de país **heredan** del operador de origen", dejando la herencia como inferencia no declarada.

La captura de OnlineSim añade un **segundo candidato de infraestructura independiente**: su FAQ declara "We have our own **equipment that holds the SIM cards** and our own **software**" ([[2026-1026-onlinesim-equipo-propio-de-sim-y-software-propio]]). Si eso es cierto, el corpus deja de tener un único linaje de hardware con varios escaparates: habría al menos dos operadores con SIM cards propias, y el stock no sería un recurso único heredado de SMS-Activate.

Refuerza el punto desde el lado de la geografía: el selector de pago de OnlineSim sirve **Bielorrusia +375, Ucrania +380, Kazajistán +77, Kirguistán +996 y Uzbekistán +998** pero **no Rusia ni China**, mientras el módulo de números gratuitos sí incluye China ([[2026-1026-onlinesim-sin-rusia-ni-china-en-el-selector-de-pago]]). Un proveedor que hereda el pool de un operador ruso y **excluye precisamente el mercado doméstico de ese operador** no puede ser simplemente su fachada: o son dos pools distintos, o la herencia no es el mecanismo.

Nota de alcance: es una declaración de marketing del propio OnlineSim, sin verificación de hardware. La inferencia que queda abierta es si "own equipment" es un hecho o parte del mismo patrón de claims sin evidencia que el vault ya registró en 5sim y HeroSMS.
=== END

=== EXTEND 2-atoms/2026-1023-sms-activate-cierra-total-el-22-de-diciembre
## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-onlinesim-virtual-sms.md` (capturada **tres días después** del aviso de cierre). El hecho que este átomo documenta —que SMS-Activate cesó toda su actividad por completo y sin excepciones— tiene ahora una **contraprueba de vigencia en el mercado**: la home de OnlineSim, capturada el 2026-10-25, sigue usando a SMS-Activate como **ejemplo vivo y actual** del sector, en presente y sin ningún matiz: "**Normally, SMS activation services (such as SMS-Activate)** are used to register on social networks (VK, OK, Facebook, Instagram), confirm messengers (Telegram, WhatsApp, Viber, WeChat), and emails (Yandex, Mail.ru, Gmail, Yahoo)" ([[2026-1026-onlinesim-faq-nombra-sms-activate-como-ejemplo-de-activacion]]).

Dos lecturas posibles que este átomo deja abiertas para el Editor: (a) el texto del competidor es **copy de plantilla sin actualizar**, lo que significa que ninguna referencia nominal a un proveedor en el corpus es fiable como dato de mercado; (b) la marca SMS-Activate sobrevivió como **etiqueta comercial** aunque la empresa haya dejado de existir — lo que encaja con que HeroSMS, su heredero technology-wise,sea el único linaje vivo.

La consecuencia para el thread: la afirmación "el mercado perdió un actor" debe matizarse a "**el mercado perdió una empresa y conservó su nombre como referencia sectorial**", y el FAQ de OnlineSim es la prueba de esa persistencia.
=== END

=== EXTEND 2-atoms/2026-1023-5sim-numero-de-un-solo-uso-una-verificacion
## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-onlinesim-virtual-sms.md`. Este átomo documenta, con dos citas de 5sim, que el número temporal "cannot be reused after the order has been completed" y que cada número sirve para **una** verificación.

OnlineSim añade la advertencia que **faltaba en el corpus** y que corrige la lectura de este átomo en un punto: la no reutilización es una propiedad de **la orden**, no del número. Su FAQ dice: "**the telecom operator can reissue SIM cards** (the same thing happens with regular citizen numbers) **two to three months after the number is inactive** and give them to its new customers, so we advise you **not to link payment methods or store important data on the add account 2FA** or other security measures" ([[2026-1026-onlinesim-reexpedicion-de-sim-a-los-2-3-meses-y-no-vincular-2fa]]).

Es decir: un número de 15 minutos deja de estar protegido a los dos o tres meses, y en ese momento puede pertenecer a otra persona —con su historial de SMS y cualquier OTP que lo haya atravesado. La formulación correcta para el vault pasa a ser: **"un número = una orden"**, no "un número = una identidad permanente".

Esto no contradice a 5sim, que no hace esa promesa en ningún sitio, pero sí **endurece** el límite: el riesgo no es que el proveedor te dé dos veces el mismo número, sino que el operador te lo reemita a un tercero tras la ventana.
=== END

=== EXTEND 2-atoms/2026-1023-5sim-reembolso-instantaneo-si-no-llega-sms
## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-onlinesim-virtual-sms.md`. Este átomo describe el régimen de garantía de 5sim ("Instant refunds — if no SMS is received, your money is refunded automatically") y lo generaliza en su §"Comparación con HeroSMS" como: "Los dos proveedores mueven riesgo al comprador de la misma forma (reembolso si la unidad no cumple), pero solo uno hace auditable el plazo".

Con OnlineSim aparece un **tercer régimen, más débil que "5sim sin plazo"**: el reembolso **no es automático en absoluto**. Su FAQ dice "**you can close the phone number and order another**, money from your balance in this case is not debited" y "you can **deactivate the phone number and the funds will return to the balance** so that you can order a new virtual mobile number" ([[2026-1026-onlinesim-reembolso-al-saldo-al-cerrar-el-numero]]).

Tres rasgos que lo distinguen: (1) requiere **una acción del comprador** — cerrar el número — y por tanto no ocurre si nadie interviene; (2) **no tiene plazo** — ni de 20 minutos como HeroSMS, ni de "hasta 15" como la página de producto de 5sim ([[2026-1023-5sim-reembolso-hasta-15-minutos]]); (3) devuelve **al saldo**, no al medio de pago.

Consecuencia para el thread: el reembolso no es una propiedad del sector sino un **dato por proveedor**, y el tiempo de saldo inmovilizado es la variable de coste real en los tres casos. Esta captura añade el extremo más desfavorable de la escala.
=== END

=== EXTEND 2-atoms/2026-1023-5sim-catalogo-153-paises-contra-180-de-la-home
## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-onlinesim-virtual-sms.md`. Este átomo documenta tres cifras de cobertura para 5sim (180 en la home, 153 en el catálogo, 111 en el CSV de `telegram`) y propone como explicación que "**180 cuenta cobertura potencial y no stock vendible**".

La captura de OnlineSim **invierte la dirección** de esa discrepancia y por tanto presiona la explicación. En OnlineSim hay cuatro cifras el mismo día: "110+ Countries for Numbers" en la cabecera, "107 countries" en el bloque de tarifas, "98 countries available" en la tarifa de 15 minutos, **107 entradas enumeradas en el pie** y **132 páginas de país en el módulo gratuito** ([[2026-1026-onlinesim-cifras-de-cobertura-98-107-110-y-132]]).

La diferencia estructural es que aquí el conjunto **mayor (132) es el gratuito** y el **menor (98) es un producto de pago concreto**, mientras el marketing (110) queda en medio. En 5sim el rango iba de 180 (marketing) a 76 (producto real). Es decir, la cobertura varía **por producto y en ambos sentidos**, y no es solo marketing inflado por encima del stock vendible.

Refuerza el mismo punto el caso de China: China está en el módulo de números gratuitos de OnlineSim y **no** en el selector de pago ([[2026-1026-onlinesim-sin-rusia-ni-china-en-el-selector-de-pago]]) — no falta el país, falta el stock pagable. Con esto, la cobertura se lee mejor como **propiedad del par (proveedor, producto)** que como propiedad del proveedor.
=== END

=== EXTEND 2-atoms/2026-1023-5sim-catalogo-28-servicios-ia
## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-onlinesim-virtual-sms.md`. Este átomo cuenta los 28 servicios de IA del catálogo de 5sim (2,3 % de 1221 nombres) y concluye que la verificación por SMS de cuentas de IA es "una categoría de primer orden del proveedor" con "inventario propio".

OnlineSim es el **contraste de capa** que faltaba: su carrusel de escaparate enumera 15 marcas — WeChat, Google, LINE, Netflix, Amazon, Proton, AliExpress, Tinder, Instagram, eBay, Taobao, WhatsApp, Facebook, Uber, Steam— y **ninguna es un servicio de IA** ([[2026-1026-onlinesim-escaparate-de-15-marcas-sin-servicios-de-ia]]). Su claim de cabecera es "1000+ SMS Receiving Services", es decir, un catálogo que la página no muestra en ninguna parte.

El valor del contraste para el thread: **el coste de una identidad de IA verificada no se puede acotar con la oferta de OnlineSim**, porque su catálogo no incluye el destino. Y la dirección inversa también se confirma: el valor de OnlineSim está en los servicios de consumo y de correo (Yandex, Mail.ru, Gmail, Yahoo según su FAQ) — la pata de mensajería y correo del mercado de altas masivas, no la de identidad de IA.
=== END

=== EXTEND 2-atoms/2026-1023-5sim-ventana-5-30-minutos-y-cancelacion-a-5-min
## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-onlinesim-virtual-sms.md`. Este átomo acota la ventana operativa de 5sim (5-30 minutos, cancelación automática a los cinco) y la conecta con la tasa de entrega como métrica de ventana.

OnlineSim añade dos precisiones que el vault no tenía para ningún proveedor:
(1) la ventana **depende del país**: "you get a virtual number for a short time **from 10 minutes to 1 hour**. The exact time depends on the selected country" — y la restricción "**only from a single selected website or app**" ([[2026-1026-onlinesim-ventana-de-10-minutos-a-1-hora-segun-pais]]).
(2) la **misma página da tres ventanas incompatibles**: "10 minutes to 1 hour" (FAQ), "15-minute Number" (nombre de la tarifa) y "for 15 minutes" (bullet). Es decir, la duración efectiva de una orden es **un dato de la página que publica el proveedor**, y hay que leerla servicio a servicio — igual que la cobertura.

Y el matiz nuevo: OnlineSim **no declara ningún plazo de reembolso** ni de auto-cancelación, solo la ventana de alquiler por país ([[2026-1026-onlinesim-reembolso-al-saldo-al-cerrar-el-numero]]). En 5sim el plazo de auto-cancelación a los 5 minutos es lo que hace el reembolso automático una consecuencia de la expiración de la orden; sin plazo, no se puede acotar el coste temporal de un reintento.
=== END

=== EXTEND 2-atoms/2026-1023-5sim-smart-buy-y-tasa-entrega-visible
## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-onlinesim-virtual-sms.md`. Este átomo describe el "Smart Buy" de 5sim (elegir automáticamente el par país-operador con mejor tasa de entrega, con opción de fijar precio máximo) y lo describe como "una **regla de desempate** sobre precio y tasa, no un óptimo de tasa absoluto".

OnlineSim es el extremo opuesto del corpus en materia de auditabilidad de la entrega: **no publica ninguna tasa de entrega**, ni tabla por par (país, operador), ni contador de stock, ni CSV. Su bloque de tarifas solo dice "To see exact prices, **please select your country**" y los CTA apuntan a `onlinesim.io/auth/register?redirect=/v2/numbers/` y `/v2/rent/` ([[2026-1026-onlinesim-precios-ocultos-tras-seleccionar-pais-y-cta-de-registro]]).

Lo que sí publica OnlineSim como prueba de vida es un carrusel de SMS de ejemplo que **repite códigos entre marcas** (AliExpress y Taobao comparten "561318"; Instagram y Facebook comparten "645 829"), con un texto de OkCupid bajo la etiqueta Tinder y el bloque entero repetido ([[2026-1026-onlinesim-codigos-de-ejemplo-duplicados-entre-marcas]]). Es una demostración de marketing, no tráfico real ni evidencia de cobertura.

La consecuencia metodológica: en la jerarquía de evidencia del corpus, **OnlineSim es el proveedor con menos dato verificable de los tres, no el más grande**. Su único dato duro es el pie de 107 países enumerados y el módulo gratuito de 132 páginas, ambos contables.
=== END
