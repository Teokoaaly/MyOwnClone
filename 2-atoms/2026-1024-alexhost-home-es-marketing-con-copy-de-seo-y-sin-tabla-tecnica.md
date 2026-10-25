---
id: 2026-1024-alexhost-home-es-marketing-con-copy-de-seo-y-sin-tabla-tecnica
type: atom
certainty: solid
sources: [sources/2026-10-24-alexhost-home.md]
links: ["[[2026-1024-alexhost-catalogo-de-servicios-y-casos-de-uso]]", "[[2026-1024-evoxt-captura-sin-tabla-de-precios-ni-specs]]", "[[2026-1024-lowendbox-captura-sin-comentarios-ni-barra-lateral]]", "[[2026-1024-alexhost-configurador-vps-24-fichas-solo-3-con-precio]]"]
---

## Claim
La home de AlexHost es, en su mitad inferior, **copy de SEO en lugar de documentación técnica**: el texto *"AlexHost hosting provider's services"* afirma que la compañía *"guarantees success and dynamic growth for any web project"* y que sus servicios *"ensure a high level of security, stable operation, and respectable performance"*. Los claims de escala son **"Founded 2008"** y **"40000+ Happy Customers"**, sin año de corte ni definición de cliente. El bloque de ventajas repite el lenguaje de posicionamiento (**"leader in the field of hosting services in Moldova"**, **"Over 10 years in the Moldavian market"**) y cierra con **"AlexHost hosting company and its competent, friendly team have no plans to rest on their laurels"**. La página sí ofrece dos herramientas de verificación: un **Looking Glass** (`lg.alexhost.com`) y un enlace a la página de datacenter y ubicación; y una sección de News con tres entradas fechadas.

## Why It Matters
El vault ya tiene el patrón bautizado con la captura de Evoxt, **"captura sin tabla de precios ni specs"** ([[2026-1024-evoxt-captura-sin-tabla-de-precios-ni-specs]]): una home cuyo contenido es marketing y cuyos datos técnicos solo existen en otra página. AlexHost es un caso híbrido: **sí trae tabla de precios con specs (17 fichas de dedicados + 24 fichas de VPS + 4 planes shared)**, pero esa tabla está **construida por duplicación**: solo **3 de las 24 fichas de VPS enlazan a un botón de compra real** y 21 repiten una ancla inerte a `alexhost.com/#`, y **siete de las 24 no muestran importe** ([[2026-1024-alexhost-configurador-vps-24-fichas-solo-3-con-precio]]). Y **ninguna de las fichas incluye SLA, egreso, backups, IPv4 ni virtualización**. El bloque de copy, en cambio, es denso.

La observación de método: **la densidad de texto-promesa es inversamente proporcional a la densidad de dato verificable**. AlexHost publica más prosa de marketing que el resto de proveedores del thread juntos, y su tabla de specs es la más pobre en metadatos operativos: ni una sola mención de SLA, de tráfico incluido o de número de IP en toda la página. Es el espejo exacto del patrón de LowEndBox, donde lo que faltaba era el contexto alrededor del dato ([[2026-1024-lowendbox-captura-sin-comentarios-ni-barra-lateral]]).

Lo que sí cambia el diagnóstico: **el Looking Glass público (`lg.alexhost.com`) es la herramienta de verificación que este thread no tenía para ningún proveedor del tramo barato**. Es el punto de entrada correcto para convertir la tabla en dato: BGP, test IP y latencia real por ubicación, que es exactamente lo que las nueve banderas del selector dejan vacío ([[2026-1024-alexhost-nueve-ubicaciones-sin-ping-ni-ficha]]).

## Nota de verificación
La captura **no** reproduce el contenido del Looking Glass ni de la página de datacenter y ubicación: son enlaces, no páginas capturadas. Tampoco publica el año de corte del dato "40000+ Happy Customers", ni define "Happy Customer", ni da cifras de cartera de clientes por producto. Los contadores de noticias ("91+12 min", "224+112 min", "44012 min") aparecen sin separación posible entre likes y minutos de lectura.
