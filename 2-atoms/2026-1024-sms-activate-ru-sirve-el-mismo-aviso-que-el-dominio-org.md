---
id: 2026-1024-sms-activate-ru-sirve-el-mismo-aviso-que-el-dominio-org
type: atom
certainty: solid
sources: [sources/2026-10-24-sms-activate-ru-closed.md, sources/2026-10-22-sms-activate-closed.md]
links: ["[[2026-1024-los-dominios-oficiales-solo-muestran-el-aviso-y-ningun-catalogo]]", "[[2026-1023-sms-activate-cierra-total-el-22-de-diciembre]]", "[[2026-1023-sms-activate-nombre-retirado-cualquier-servicio-igual-es-fraude]]"]
---

## Claim
El aviso de cierre de SMS-Activate **no vive en un solo dominio**: el 2026-10-24 el sitio `https://sms-activate.ru/` —el dominio orientado a Rusia, distinto del `.org` capturado el 2026-10-22— sirve un **cuerpo de aviso byte-idéntico** al de `https://sms-activate.org/`: mismos 126 palabras, mismas cuatro preguntas del FAQ, mismo cierre "С 22 декабря мы полностью прекратили свою деятельность", mismo "10 años", misma recomendación de HeroSMS y mismo buzón `info@sms-activate.org`. La verificación línea por línea de ambos archivos de `sources/` solo encuentra una diferencia: la URL del encabezado y un salto de línea final. Es decir, el operador —o quien mantiene sus dominios— despliega **el mismo aviso estático en al menos dos TLD**, y el canal de contacto sigue siendo el del `.org` aunque se entre por el `.ru`.

## Why It Matters
El vault tenía el cierre como **un hecho único con una URL única**, y por tanto como un evento localizado. Esta captura lo convierte en un **estado persistente y replicado por dominio**: dos días después del aviso original, el `.ru` sigue en pie, con el mismo texto y sin nada más. Dos consecuencias para el vault:
1. **La auditoría de dominio deja de ser binaria.** Un tercero que se encuentre con `sms-activate.ru` no está ante un clon: ante el propio proveedor, ya sin negocio. La señal que separa "proveedor cerrado" de "suplantación" es el **contenido** de la página (un aviso sin catálogo), no el nombre del dominio — criterio que queda desarrollado en [[2026-1024-los-dominios-oficiales-solo-muestran-el-aviso-y-ningun-catalogo]].
2. **La marca sigue ocupando espacio DNS aunque el negocio haya muerto.** El aviso afirma que "el nombre se va con nosotros" ([[2026-1023-sms-activate-nombre-retirado-cualquier-servicio-igual-es-fraude]]), pero los dominios que llevan ese nombre siguen bajo control y sirven el aviso: el nombre no se ha retirado del DNS, se ha retirado del negocio. La advertencia antiestafa solo es coherente si se entiende como "cualquier **servicio** con ese nombre es un clon", no como "cualquier **dominio** con ese nombre".
Para el resto del thread, la confirmación de que la recomendación a HeroSMS viaja con el aviso en ambos dominios refuerza que el traspaso de tecnología es la única vía de continuidad del linaje ([[2026-1023-sms-activate-cierra-total-el-22-de-diciembre]]).

## [FRICTION]
> [[2026-1023-sms-activate-nombre-retirado-cualquier-servicio-igual-es-fraude]] (escrita el 2026-10-23) toma la advertencia al pie de la letra y la generaliza: "cualquier servicio que se llame SMS-Activate a partir de ahora es un fraude", lo que abre un espacio de suplantación con la confianza heredada de 10 años de marca.
> Este átomo presiona esa creencia en un punto literal: **el 2026-10-24 existe un servicio llamado SMS-Activate —`sms-activate.ru`— que no es un fraude**, es el aviso oficial del operador cerrado. La generalización solo sobrevive si se leen "servicio" como "servicio **que vende activaciones**" y no como "cualquier sitio con el nombre"; la frase rusa se refiere al servicio que ofrece números, no al dominio reservado que solo publica una lápida.
> Ambas no pueden ser completamente correctas tal como están redactadas: o el aviso vale para todo lo que se llame SMS-Activate (y entonces el propio `.ru` es un fraude, absurdo), o vale solo para los servicios que operen bajo ese nombre (y entonces el átomo anterior debe acotarse). Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
El cuerpo idéntico se verificó comparando `sources/2026-10-22-sms-activate-closed.md` y `sources/2026-10-24-sms-activate-ru-closed.md` línea por línea: la única diferencia es la URL del frontmatter (`sms-activate.org` vs `sms-activate.ru`) y un salto de línea final. La captura **no** indica quién controla hoy el `.ru` (misma empresa, un tercero que compró el dominio, o un agente de dominio sin relación), ni si el `.org` y el `.ru` son del mismo titular registral. Tampoco da la razón por la que existe un `.ru` en paralelo ni si hay más TLD. La coincidencia de contenido es un indicio fuerte de continuidad, no una prueba de identidad registral.
