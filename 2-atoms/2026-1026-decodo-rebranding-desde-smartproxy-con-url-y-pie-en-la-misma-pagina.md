---
id: 2026-1026-decodo-rebranding-desde-smartproxy-con-url-y-pie-en-la-misma-pagina
type: atom
certainty: solid
sources: [sources/2026-10-25-decodo-residential-pricing.md]
links: ["[[2026-1024-iproyal-premios-y-distintivos-como-sustituto-de-sla]]", "[[2026-1024-brightdata-400m-de-ips-en-195-paises-con-targeting-gratis]]", "[[2026-1026-decodo-escalera-mensual-de-375-a-275-por-gb]]"]
---

## Claim
La página de precios capturada en `smartproxy.com/pricing` se identifica en el pie como **"© 2018-2026 decodo.com (formerly smartproxy.com). All Rights Reserved"**, y la lista de cifras de escala del pie declara **"125M+ IPs from 195+ locations"** con la etiqueta "The most efficient web data collection solutions". La captura conserva **dos identidades de marca en un mismo documento**: el dominio de origen (`smartproxy.com`) y la marca vigente (`decodo.com`), esta última con el rango de antigüedad declarado de 2018.

## Why It Matters
Es un aviso de método que afecta a **cómo el vault cita y deduplica proveedores**: la URL capturada y la marca publicada no coinciden, de modo que un catálogo por dominio (`smartproxy.com`) y un catálogo por marca (`Decodo`) **no son el mismo índice**. Si más adelante aparece `decodo.com/proxies/residential-proxies/pricing` con precios distintos, el vault tiene que saber que es el mismo proveedor y no un quinto actor del sector — exactamente el riesgo que el thread ya resolvió para otro caso: la persistencia de un dominio tras la desaparición del negocio ([[2026-1024-sms-activate-ru-sirve-el-mismo-aviso-que-el-dominio-org]]).
Lo segundo: el pie de página es el único punto donde aparece el "125M+", mientras el cuerpo del producto dice "115M+", y el propio pie usa superlativos de posicionamiento ("The most efficient web data collection solutions") sin metodología. Es decir, **el pie de página de esta captura es la zona menos fiable del documento**: es donde el marketing es más crudo y donde las cifras se contradicen con las del cuerpo (ver [[2026-1026-decodo-pool-de-115m-en-el-cuerpo-y-125m-en-el-pie]]).

## Nota de verificación
Texto del pie transcrito literalmente. La captura **no** publica: la fecha del rebranding, si los precios de `smartproxy.com` y `decodo.com` son idénticos, ni el procedimiento de redirección entre ambos dominios.


## Nota de extensión 2026-10-27
La home **cierra dos huecos** que este átomo declaraba abiertos ("la captura **no** publica: la fecha del rebranding…").

Primero, **la fecha**: el FAQ responde *"Is Decodo the same company as Smartproxy?"* con **"Yes… Smartproxy officially became Decodo in April 2025. It's the same company, team, infrastructure, and proxy network, now under a new name that reflects our broader web data platform."** Es decir, **el rebranding es de abril de 2025**, y no de 2026: la marca lleva más de un año publicada con el nombre nuevo mientras el vault seguía capturando `smartproxy.com`. La sección de la home se titula literalmente **"Smartproxy is now Decodo"** y el FAQ añade **"the same trusted team and solutions you've relied on since 2018"** — el rango de antigüedad declarado es 2018, no 2025.

Segundo, **el aviso de suplantación**: *"Just be careful with the old name: **Smartproxy.org isn't us. It's an impersonator** and has no connection to Decodo, our team, or our infrastructure. **The only official Decodo website is Decodo.com.**"* Es el mismo patrón de persistencia de dominio que el vault ya registró con SMS-Activate ([[2026-1024-sms-activate-ru-sirve-el-mismo-aviso-que-el-dominio-org]]), pero aquí invertido: **no es un negocio que desaparece dejando vivo su dominio**, es una marca que **avisa activamente** del impostor.

Tercero, **una captura más de la doble identidad**: el pie de esta home —capturada en `smartproxy.com`— dice **"© 2018-2026decodo.com (formerly smartproxy.com). All Rights Reserved"**, igual que la página de precios del 2026-10-25. Dos capturas distintas, dos dominios distintos de marca, **un mismo actor**, y una fecha de cambio de nombre que ahora el vault conoce. Ver [[2026-1027-decodo-smartproxy-org-es-un-impostor-y-el-mismo-equipo-desde-2018]].
