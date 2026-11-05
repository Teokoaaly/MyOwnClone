# Extensiones a átomos existentes — captura 2026-10-26-hero-sms-api-docs

Fuente: `sources/2026-10-26-hero-sms-api-docs.md` (captura `0-raw/2026-10-26-hero-sms-api-docs.md`), la página `hero-sms.com/en/api` de HeroSMS.
Ninguno de los átomos siguientes se ha modificado: las extensiones se proponen para el Editor.

=== EXTEND 2-atoms/2026-1023-herosms-api-y-partners-de-registro-masivo
## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-hero-sms-api-docs.md` (página `hero-sms.com/en/api`, capturada el 2026-10-26).

Este átomo registró el caso de HeroSMS: la home ofrece botón "Get API key" **sin publicar documento, endpoint, precio ni condiciones**, y de ahí la conclusión de que "en HeroSMS está [la automatización] **fuera**, en un ecosistema de partners y en una API sin documentación pública", con un coste de integración **mayor** que 5sim. La página de API **existe y está publicada**: "Server: **https://hero-sms.com/api/v1**", "**OpenAPI 3.2.0**", descarga del documento en "**json**" y "**yaml**", esquema "**apiKeyAuth**" con cabecera "**Authorization**" y formato "**ApiKey {your_token}**", y una **tabla de trece operaciones de activación** ([[2026-1027-hero-sms-trece-operaciones-de-activacion]], [[2026-1027-hero-sms-openapi-3-2-0-con-api-key-en-la-cabecera-authorization]]).

Consecuencia para el Editor: la afirmación "API sin documentación pública" **queda desactualizada en su premisa** —lo que la captura del 2026-10-22 no vio fue la **página**, no la ausencia de documentación. Lo que **sigue en pie** es lo demás: **precio y condiciones comerciales siguen sin publicarse** —el 404 de `/pricing` se mantiene ([[2026-1024-herosms-url-de-precios-devuelve-404-y-no-publica-precios-propio]])—, de modo que el diagnóstico correcto pasa a ser: **HeroSMS publica su contrato técnico pero no su contrato comercial**, exactamente el patrón de NoOnes invertido ([[2026-1026-noones-dev-noones-sin-precios-ni-limites-ni-documentacion-publica]]). Y hay que añadir el dato nuevo más fuerte: **el proveedor publica una guía de migración de clientes software existentes** ([[2026-1027-hero-sms-compatibilidad-de-wire-con-los-clientes-de-sms-activate]]), lo que confirma que su modelo es **integrar a los registros de alto del ecosistema**, no solo vender saldo.
=== END

=== EXTEND 2-atoms/2026-1023-herosms-sobre-la-infraestructura-de-sms-activate
## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-hero-sms-api-docs.md`.

Este átomo sostiene que HeroSMS es una **fachada white-label sobre SMS-Activate** y que "la inferencia razonable (no declarada por el proveedor) es que el pool de números y la cobertura de país **heredan** del operador de origen". La página de API **publica la compatibilidad de protocolo de forma literal**: "HeroSMS is compatible with **former** SMS-Activate partners", con el paso 3 del procedimiento escrito como "**Replace the host from `https://api.sms-activate.ae` to `https://hero-sms.com`**" y el paso 4 "Enter the API key from your HeroSMS account" ([[2026-1027-hero-sms-compatibilidad-de-wire-con-los-clientes-de-sms-activate]]).

Consecuencia para el Editor: la compatibilidad **wire** es un dato mucho más fuerte que la fórmula de marketing "built on the foundation of SMS-Activate" —dos hosts, una clave, y un procedimiento de cambio publicado. Pero hay que **mantener la distinción** que el átomo ya establece: lo que el proveedor declara es **compatibilidad de protocolo**, no **herencia de pool**. Es decir, la línea "el pool y la cobertura heredan del operador de origen" **sigue siendo inferencia**; lo que ha dejado de ser inferencia es que la API de HeroSMS es **intercambiable con la del operador cerrado**. Esa distinción es la que sostiene la fricción 7 del thread (cierre de SMS-Activate contra "fachada sobre operador vivo"): ahora se puede decir que el receptor **hereda la interfaz** de un operador que cerró, lo cual no prueba que herede su inventario.
=== END

=== EXTEND 2-atoms/2026-1023-sms-activate-cierra-total-el-22-de-diciembre
## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-hero-sms-api-docs.md`.

Este átomo documenta el cierre total de SMS-Activate el 22 de diciembre de 2026 y su calendario de liquidación. La página de API de HeroSMS publica ahora **un destino de migración con procedimiento**: cuatro pasos, host `api.sms-activate.ae` → `hero-sms.com`, API key de HeroSMS en su lugar, y la mención de "**former** SMS-Activate partners" ([[2026-1027-hero-sms-compatibilidad-de-wire-con-los-clientes-de-sms-activate]]).

Consecuencia para el Editor: el cierre deja de ser solo un hecho de mercado y pasa a tener un **receptor de tráfico documentado**. Eso tiene una consecuencia práctica para cualquier software de registro que hoy apunte a `api.sms-activate.ae`: **el coste de migrar es una línea de configuración**, no una reescritura de cliente. Y un matiz que hay que escribir: la migración **no resuelve** la liquidación —el saldo, los números comprados y los plazos del operador saliente siguen sin varias reglas—; HeroSMS es un **destino de integración**, no un sucesor de los derechos de los clientes del operador cerrado.
=== END

=== EXTEND 2-atoms/2026-1023-hero-sms-flujo-de-cinco-pasos-para-verificar-chatgpt
## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-hero-sms-api-docs.md`.

Este átomo documenta el **flujo de panel web de cinco pasos** para verificar ChatGPT en HeroSMS: registrarse, recargar saldo, elegir servicio y país, comprar número, recibir el código. La página de API publica la **versión programática** de ese flujo, con operaciones que corresponden una a una: `post/activations` (comprar), `get/activations` (seguir), `post/activations/{activationId}/finish` (confirmar), `get/activations/offers/{verificationType}` (consultar disponibilidad por tipo), `get/activations/stats` ([[2026-1027-hero-sms-trece-operaciones-de-activacion]]).

Consecuencia para el Editor: el thread puede **dejar de tratar el flujo de cinco pasos como el único flujo de HeroSMS**. El flujo de panel es **humano y de un solo sentido**; el de API es **programático, con vuelta atrás**: `post/activations/{activationId}/replace` (sustituir el número), `post/activations/{activationId}/reactivate` (reactivarlo), `post/activations/{activationId}/prolong` (prolongarlo, con sus `options` y su `history`) y `delete/activations/{activationId}`. Es decir, **la API publica las operaciones de gestión de incidencias que el panel no expone**, y eso convierte el coste del número en un **precio con estructura de duración** y no en un precio unitario opaco ([[2026-1023-hero-sms-modelo-pay-per-use-y-tabla-real-vs-virtual]]).
=== END

=== EXTEND 2-atoms/2026-1023-hero-sms-reembolso-si-no-llega-sms-en-20-minutos
## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-hero-sms-api-docs.md`.

Este átomo fija la política de HeroSMS: **reembolso automático si el SMS no llega en 20 minutos**, con un umbral que no coincide con el de 5sim (15 minutos) ni con el "instant" del marketing ([[2026-1023-5sim-reembolso-instantaneo-si-no-llega-sms]]). La API publica ahora **el estado del reembolso como dato consultable**: el endpoint `get/activations/history` acepta el parámetro de filtrado `statuses[]` junto a `services[]`, `countries[]`, `size`, `page`, `sort[id]` y `search`, con `from` y `to` **obligatorios** ([[2026-1027-hero-sms-el-historial-de-activaciones-exige-ventana-temporal-y-filtros]]).

Consecuencia para el Editor: el reembolso deja de ser una **condición comercial** y pasa a ser una **columna de un histórico consultable**, lo que permite al cliente auditar **cuánto se gastó, en qué servicio, en qué país y con qué resultado** —incluido qué activación se reembolsó. Es la diferencia entre un umbral publicado y una **partida de coste medida**, y es la primera superficie de auditoría de gasto que el vault tiene en el sector de SMS.
=== END

=== EXTEND 2-atoms/2026-1024-noones-limite-diario-suma-de-todas-las-operaciones-en-24h
## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-hero-sms-api-docs.md`.

Este átomo documenta que NoOnes impone un **techo diario agregado de operaciones** y un control de saldo que el vault tiene registrado como "el único control granular de gasto del sector". HeroSMS no publica ningún techo, pero su API publica **la herramienta para que el cliente lo construya**: `get/activations/history` con `from`/`to` obligatorios, `countries[]`, `services[]`, `statuses[]`, `size`, `page`, `sort[id]` y `search` ([[2026-1027-hero-sms-el-historial-de-activaciones-exige-ventana-temporal-y-filtros]]), más `get/activations/stats` y `get/activations/offers/{verificationType}` ([[2026-1027-hero-sms-trece-operaciones-de-activacion]]).

Consecuencia para el Editor: el thread puede **reformular el reparto de responsabilidades** en el control de gasto de SMS. NoOnes **centraliza** el límite y lo oculta detrás de un techo; HeroSMS **externaliza** el control y publica el histórico para que el cliente lo audite. Y hay un matiz que el átomo debe conservar: **HeroSMS no publica ningún techo**, de modo que externalizar el control **transfiere al pipeline una responsabilidad que NoOnes asume** —con un modelo prepago sobre saldo ([[2026-1023-hero-sms-modelo-pay-per-use-y-tabla-real-vs-virtual]]), lo que se quiere vigilar no es el número de operaciones sino **el saldo retenido**.
=== END

=== EXTEND 2-atoms/2026-1023-herosms-vs-5sim-competencia-directa
## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-hero-sms-api-docs.md`.

Este átomo compara HeroSMS y 5sim como competencia directa. La página de API añade **un eje de comparación que antes no era medible**: quién **publica su contrato técnico**. HeroSMS publica OpenAPI 3.2.0 en JSON y YAML, servidor `https://hero-sms.com/api/v1`, `apiKeyAuth` con cabecera `Authorization` y **clientes de ejemplo en Shell, Ruby, Node.js, PHP y Python** ([[2026-1027-hero-sms-openapi-3-2-0-con-api-key-en-la-cabecera-authorization]]); 5sim integra la compra dentro del chat y no expone una especificación equivalente ([[2026-1023-5sim-asistente-ia-integrado]]).

Consecuencia para el Editor: la comparación puede añadir una **columna de documentabilidad** a la tabla de proveedores de SMS, y conviene encuadrarla bien: **publicar la especificación no es publicar el precio**. HeroSMS sigue sin precios públicos ([[2026-1024-herosms-url-de-precios-devuelve-404-y-no-publica-precios-propio]]), de modo que el resultado del cruce es que **el proveedor con el contrato técnico más abierto es también el más opaco en precio** —lo que refuerza, en vez de debilitar, la tesis del thread de que **en SMS el precio solo se obtiene entrando al panel con saldo**.
=== END
