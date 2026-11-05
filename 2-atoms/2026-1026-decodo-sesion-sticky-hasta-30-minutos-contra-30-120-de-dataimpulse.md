---
id: 2026-1026-decodo-sesion-sticky-hasta-30-minutos-contra-30-120-de-dataimpulse
type: atom
certainty: solid
sources: [sources/2026-10-25-decodo-residential-pricing.md]
links: ["[[2026-1024-dataimpulse-sesiones-rotating-y-sticky]]", "[[2026-1023-hero-sms-ip-y-vpn-coincidentes-con-el-pais-del-numero]]", "[[2026-1026-decodo-targeting-a-nivel-de-asn-y-zip-incluido-gratis]]"]
---

## Claim
El paso 3 del setup que publica Decodo en su FAQ dice literalmente: **"Choose session type: rotate IPs per request or keep one for up to 30 min"**. La lista de features lo repite como "Rotating and sticky session options", sin más cifra. El **tope declarado de la sesión sticky es, por tanto, 30 minutos**.

## Why It Matters
Es el parámetro operativo que decide si un flujo de verificación se rompe, y el vault ya lo tiene medido con un rango en DataImpulse: **residencial sticky "30-120 minutes on average"**, y hasta 120 minutos en el cuerpo ([[2026-1024-dataimpulse-sesiones-rotating-y-sticky]]). Con Decodo el tope baja a **30 minutos**, que es **el mínimo del rango del otro proveedor**: es decir, **la unidad de sesión no es una constante del sector ni un detalle de configuración, es un compromiso de proveedor que se paga en la longitud del flujo**.
La consecuencia para el criterio del vault es directa: HeroSMS exige que la IP coincida con el país del número y prohíbe registrar varias cuentas desde la misma IP ([[2026-1023-hero-sms-ip-y-vpn-coincidentes-con-el-pais-del-numero]]); con una sesión sticky de 30 minutos, **un flujo que necesite separar el alta, la verificación por SMS y la confirmación de email en momentos distintos consume tres sesiones, no una** —y si esas tres no caben en 30 minutos, la rotación ocurre entre pasos y rompe la coherencia de IP. Combinado con el targeting por ASN gratis ([[2026-1026-decodo-targeting-a-nivel-de-asn-y-zip-incluido-gratis]]), el proveedor **ofrece la granularidad de selección y la limita en el tiempo**: se puede elegir el ASN exacto y no se puede mantenerlo más de 30 minutos.

## [FRICTION]
> [[2026-1024-dataimpulse-sesiones-rotating-y-sticky]] afirma que "la duración de la sesión sticky es una restricción operativa dura" y usa el rango 30–120 min con "con el límite de 30 minutos por defecto, un flujo más largo que eso se rompe".
> Este átomo **presiona ese dato al revés**: los 30 minutos de DataImpulse son **el valor por defecto**, mientras que en Decodo son **el tope absoluto**. Es decir, la lectura "DataImpulse da 120 minutos" y la lectura "Decodo da 30" no son dos puntos de la misma escala, sino **la diferencia entre un techo y un suelo**.
> Ambas no pueden ser completamente correctas: o la sesión sticky se cotiza por su máximo declarado, o el vault tiene que usar el **peor caso por proveedor** —y con tres proveedores medidos ese peor caso es 30 minutos, lo que fijaría el límite operativo del flujo de verificación en 30 minutos con independencia del proveedor. Marcado para juicio humano, no auto-resuelto: la captura no publica si la renovación de sesión dentro de los 30 minutos es posible ni si hay sesión sticky más larga en planes Enterprise.

## Nota de verificación
Texto transcrito literalmente. La captura **no** publica: si el límite de 30 minutos es el máximo o solo el valor por defecto, si la sesión se renueva al expirar, ni la duración de la sesión rotativa.


## Nota de extensión 2026-10-27
La documentación de DataImpulse permite **precisar el "peor caso de 30 minutos"** que este átomo usa como conclusión operativa. DataImpulse publica que el intervalo de rotación sticky es **configurable de 1 a 120 minutos**, con media y default de 30 —es decir, **30 minutos es el default y la media, no el suelo**: el suelo publicado es **1 minuto**. La comparación del sector que este átomo establece (Decodo 30 min como tope absoluto frente a DataImpulse 30–120 min) se mantiene en el techo, pero el **suelo del rango de DataImpulse baja a 1 minuto**, lo que refuerza la conclusión de este átomo en un sentido que el corpus no tenía: el flujo de verificación debe asumir **la sesión más corta que el cliente pueda pedir, no la más corta que el proveedor por defecto sirva**.
En el marco del thread esto también matiza la fricción 14 de la §9 (la duración sticky móvil sin publicar): la cifra móvil de 120 minutos ([[2026-1027-dataimpulse-sesion-sticky-movil-hasta-120-minutos]]) es **el techo del contrato de intervalo**, no necesariamente una propiedad del pool móvil. Ver [[2026-1027-dataimpulse-intervalo-rotacion-sticky-configurable-1-a-120-minutos]].
La captura **no** publica: si el intervalo mínimo de 1 minuto aplica a todos los pools ni si el límite real por pool es superior.
