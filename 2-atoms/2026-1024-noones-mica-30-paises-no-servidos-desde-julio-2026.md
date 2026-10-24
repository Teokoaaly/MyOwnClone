---
id: 2026-1024-noones-mica-30-paises-no-servidos-desde-julio-2026
type: atom
certainty: solid
sources: [sources/2026-10-23-noones-blocked-jurisdictions.md]
links: ["[[2026-1024-noones-jurisdicciones-globalmente-restringidas]]", "[[2026-1022-i18n-es-first-jurisdiccion-es]]", "[[2026-1024-noones-bloquea-ip-estadounidense-con-mensaje-explicito]]", "[[2026-1023-5sim-catalogo-desviado-hacia-india-y-asia]]"]
---
## Claim
La sección **"2. MiCA-Regulated Countries (Effective July 1, 2026)"** declara: *"effective July 1, 2026, we do not serve users residing in countries regulated under the MiCA framework"*, con la razón explícita: *"Because we operate outside of this specific framework, we cannot onboard users or facilitate any services for individuals located within these jurisdictions."* El artículo anuncia **"30 countries"** y la tabla los enumera: **27 Estados miembros de la UE** (Austria, Germany, Netherlands, Belgium, Greece, Poland, Bulgaria, Hungary, Portugal, Croatia, Ireland, Romania, Cyprus, Italy, Slovakia, Czech Republic, Latvia, Slovenia, Denmark, Lithuania, Spain, Estonia, Luxembourg, Sweden, Finland, Malta, France) más **3 del EEE** (Iceland, Liechtenstein, Norway). La captura es de 2026-10-23, es decir **posterior a la fecha de entrada en vigor**.

## Why It Matters
El recorte MiCA es **auto-implicado, no discrecional**: NoOnes declara no estar dentro del marco y, por tanto, no poder dar de alta a sus residentes. El bloqueo de la UE entera (27+3) es el contrapeso regulatorio de haber elegido operar fuera del marco, y hace que la cobertura de NoOnes quede estructuralmente en el eje **emergente** — India, Nigeria, Ghana, Vietnam, China, México — que es exactamente el sesgo que el vault ya vio en 5sim ([[2026-1023-5sim-catalogo-desviado-hacia-india-y-asia]]). Para el phone farm la consecuencia es doble: (a) **el proveedor no es utilizable desde la jurisdicción donde el vault está estructurado** (España está en la lista, [[2026-1022-i18n-es-first-jurisdiccion-es]]), lo que obliga a que toda la operación con NoOnes ocurra desde una entidad y un residence en un país servido — un requisito de socks más un requisito de identidad, no solo de red; y (b) el bloqueo por IP de la home ([[2026-1024-noones-bloquea-ip-estadounidense-con-mensaje-explicito]]) y el de por residencia ([[2026-1024-noones-jurisdicciones-globalmente-restringidas]]) son dos capas distintas que un VPN por sí solo no resuelve: el propio proveedor advierte de no eludir las restricciones "such as by obscuring your IP address".

## [FRICTION]
> [[2026-1022-i18n-es-first-jurisdiccion-es]] afirma que MyOwnClone opera **español-primero** con "origen y contratos en España".
> Este átomo lo presiona: desde el 1 de julio de 2026, España está entre los 30 países MiCA donde NoOnes **no da de alta a nadie**, y NoOnes cierra el acceso en la home por IP con el mensaje literal de jurisdicción restringida. Es decir, la jurisdicción del vault no solo no es servida —es el punto de bloqueo declarado.
> Ambas no pueden ser simultáneamente operativas: o el proveedor de cripto es irrelevante para la operación española (y este átomo queda como contexto), o la operación necesita un residence y una entidad en un país no listado (México, Nigeria, Ghana, Vietnam, India…), lo que es una decisión estructural, no un ajuste de configuración.
> Marcado para juicio humano, no auto-resuelto.
