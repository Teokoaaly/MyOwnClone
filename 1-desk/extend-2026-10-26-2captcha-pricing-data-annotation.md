# Extensiones a átomos existentes — captura 2026-10-26-2captcha-pricing-data-annotation (2026-10-26)

Fuente: `sources/2026-10-26-2captcha-pricing-data-annotation.md` (captura `0-raw/2026-10-26-2captcha-pricing-data-annotation.md`).
Ninguno de los átomos siguientes se ha modificado: las extensiones se proponen para el Editor.

=== EXTEND 2-atoms/2026-1024-2captcha-servicio-dual-cliente-paga-y-trabajador-cobra
## Nota de extensión 2026-10-27
Este átomo documenta el modelo de **doble cara** de 2Captcha: por un lado, el cliente paga por el captcha resuelto; por otro, el trabajador cobra por resolverlo, y el margen del proveedor está en esa diferencia. La página `/pricing/data-annotation` del 2026-10-26 **añade una tercera venta sobre el mismo pool**: la página ofrece, en el menú oficial de precios, "**Scale smarter: Tap into a global workforce and automated workflows to handle massive data annotation projects with speed and precision**" y "**Maximize efficiency: Save time and money with flexible deadlines, customizable budgets**" ([[2026-1027-2captcha-data-annotation-sin-precio-publico-solo-contacto]]).

**La consecuencia es directa sobre este átomo: la fuerza laboral que 2Captcha usa como insumo de su producto barato es también un producto que se vende a precio de proyecto.** El átomo ya decía que el captcha es, en el fondo, **trabajo humano commoditizado** —y la página de anotación confirma que ese trabajo no es un efecto colateral del modelo, sino **una línea de negocio explícita con su propio apartado en la carta de precios**. La asimetría se vuelve más legible: el trabajo se compra al worker **por unidad a $0,5–$2,99 por 1000** y se revende al cliente final **por proyecto con presupuesto negociable**, sin cifra ni unidad. La diferencia entre el precio del input y el del output es exactamente el margen que este átomo ya había identificado, y ahora tiene un segundo mercado donde se aplica.

**Y hay un dato de encuadre que este átomo no tenía**: la página es una de las **siete pestañas** del menú de precios, y es una de las **dos que no publica ninguna cifra** ([[2026-1027-2captcha-menu-de-precios-con-7-lineas-y-dos-sin-cifra]]). Es decir, **la misma compañía que publica 48 tipos de captcha con precio cerrado por mil no publica el precio de su servicio de trabajo humano por proyecto**. La opacidad está donde está el margen, y el vault puede decirlo con dos capturas del mismo proveedor y el mismo día.

Nota de verificación: la captura **no** publica unidad, volumen mínimo, plazo, SLA ni ninguna cifra de la línea de anotación; el texto "customizable budgets" es la única mención económica y no es una cifra.
=== END

=== EXTEND 2-atoms/2026-1024-2captcha-ai-primero-con-fallback-a-trabajadores-humanos
## Nota de extensión 2026-10-27
Este átomo documenta que 2Captcha es **"AI-first con fallback a trabajadores humanos"**: el proveedor resuelve primero con su modelo y recurren a su red humana cuando el automatismo falla. La página `/pricing/data-annotation` del 2026-10-26 **confirma la existencia y la escala de esa red humana**, pero desde el otro lado de la operación: la página vende "**a global workforce**" y "**automated workflows**" **en la misma frase** ("Tap into a global workforce and automated workflows to handle massive data annotation projects"), y ofrece "**API-powered automation that fits your process: Create fully automated data annotation workflows**" ([[2026-1027-2captcha-data-annotation-sin-precio-publico-solo-contacto]]).

**La lectura que esta extensión abre es que la compañía ya es —y se cotiza como— un proveedor de mano de obra de IA en las dos direcciones.** La misma plantilla comercial —"global workforce" + "automated workflows" + "API-powered automation"— que describe cómo 2Captcha **resuelve** captchas describe ahora cómo **anota datos** para terceros: el proveedor vende el flujo híbrido (automatismo primero, humano cuando hace falta) como producto, con su fuerza laboral global como la parte que garantiza el resultado. Eso convierte la cadena de elusión en una cadena más ancha: **el vault está del lado del cliente de un proveedor que monetize tanto la automatización como el trabajo humano que la complementa**, y el trabajo humano se le compra más barato por unidad ($0,5–$2,99 por 1000 captchas) de lo que cualquier cliente paga por un proyecto de anotación.

**La consecuencia práctica para el thread: el "fallback humano" de 2Captcha es un insumo con demanda propia.** El vault hasta ahora lo registraba como un mecanismo interno de calidad; ahora puede registrar que es **una capacidad comercializable, con su propia pestaña en la carta de precios y sin precio publicado**. Es la misma tesis de la fricción 37 del thread —"la línea de empresa es la única partida del vault cuyo precio no existe en ninguna captura"— pero aplicada a un proveedor del corpus y con un mecanismo interno visible.

Nota de verificación: la captura **no** publica si la "global workforce" que se vende para anotación es la misma red que resuelve captchas para 2Captcha; la identidad de las dos capacidades es **inferencia del vault** a partir del marketing común de la compañía.
=== END

=== EXTEND 2-atoms/2026-1026-capsolver-enterprise-con-uptime-garantizado-sin-cifra-ni-precio
## Nota de extensión 2026-10-27
Este átomo registra la línea enterprise de CapSolver: "**uptime garantizado**" **sin cifra, sin precio y sin periodo de medición**, y la localiza como un caso de empresa dentro del corpus. La página `/pricing/data-annotation` de 2Captcha del 2026-10-26 **añade un segundo caso, y uno más severo**: la línea de **anotación de datos** de 2Captcha **no publica ni siquiera una promesa** —ni precio, ni SLA, ni uptime, ni unidad—, solo "Contact our sales team", tres puntos de valor ("global workforce", "flexible deadlines, customizable budgets", "API-powered automation") y un formulario ([[2026-1027-2captcha-data-annotation-sin-precio-publico-solo-contacto]]).

**La diferencia entre los dos casos es lo que esta extensión registra como progreso del conocimiento del vault.** CapSolver publica una **garantía sin número**; 2Captcha no publica nada. Ambos coinciden en que la línea de servicios —la que de verdad necesita un cliente que integra su producto en un pipeline— es **la que carece de información de precio**, y ambos coinciden en que la infraestructura sí la tiene. La regla que el vault puede extraer, ahora con dos proveedores del corpus y no uno: **la opacidad de precio no se concentra en el proveedor enterprise de un sector, se concentra en la función enterprise de todos los proveedores de infraestructura de acceso a web**, porque es ahí donde el precio se negocia y donde el proveedor retiene el margen.

**El dato estructural que cierra el caso es que las dos pestañas opacas de 2Captcha comparten un único formulario de contacto**, con el desplegable de temas que incluye "Enterprise / VIP request" ([[2026-1027-2captcha-menu-de-precios-con-7-lineas-y-dos-sin-cifra]]). Es decir, no hay dos procesos de venta: hay uno, y la pestaña del menú solo decide qué argumentario precede al formulario.

Nota de verificación: la captura **no** publica ninguna cifra; la ausencia es una medición sobre la página y no implica que no exista precio en contrato offline.
=== END
