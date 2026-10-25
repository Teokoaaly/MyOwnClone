---
id: 2026-1024-los-dominios-oficiales-solo-muestran-el-aviso-y-ningun-catalogo
type: atom
certainty: solid
sources: [sources/2026-10-24-sms-activate-ru-closed.md, sources/2026-10-22-sms-activate-closed.md]
links: ["[[2026-1024-sms-activate-ru-sirve-el-mismo-aviso-que-el-dominio-org]]", "[[2026-1023-sms-activate-nombre-retirado-cualquier-servicio-igual-es-fraude]]", "[[2026-1024-el-plazo-de-contacto-del-aviso-ya-habia-caducado-al-capturarse]]"]
---

## Claim
Las páginas de SMS-Activate tras el cierre son **una lápida estática y nada más**: la captura completa del 2026-10-24 son 126 palabras en total —un encabezado, un párrafo de cierre, una imagen (`racoon`, embebida en base64 y eliminada en la captura) y cuatro respuestas de FAQ—, **sin catálogo de servicios, sin precios, sin contador de stock, sin acceso a cuenta, sin balance, sin bot y sin ningún formulario de compra**. La respuesta sobre el futuro de la actividad es un "no" rotundo ("Наше имя уходит вместе с нами"), y la única acción que ofrece a un usuario es **migrar a HeroSMS** ("Рекомендуем попробовать его") o **escribir a un buzón hasta el 30 de abril**. La ausencia de catálogo es, por tanto, **la firma observable del cierre**: no un residuo de una web que sigue vendiendo con una cabecera de aviso.

## Why It Matters
Este es el criterio que el vault necesitaba para distinguir a un proveedor cerrado de un suplantador en la práctica. La advertencia del emisor ("si ha encontrado un servicio que se llame SMS-Activate, es una estafa") no identifica ningún clon ni publica ninguna lista —es una advertencia sin destinatario concreto ([[2026-1023-sms-activate-nombre-retirado-cualquier-servicio-igual-es-fraude]])—, pero **la forma del sitio sí es verificable**: los dominios oficiales (`sms-activate.org` y `sms-activate.ru`) **no ofrecen nada**, y cualquier sitio que se llame SMS-Activate **y además tenga catálogo, precios y stock es un clon**, por definición. La marca, al menos en su dominio de origen, quedó vacía de contenido.
Consecuencia operativa para el vault: una comprobación de proveedor que se apoye solo en el nombre de dominio **falla en los dos sentidos**. En un sentido, porque el nombre ya no identifica al operador original ([[2026-1024-sms-activate-ru-sirve-el-mismo-aviso-que-el-dominio-org]]); en el otro, porque la ausencia total de oferta es exactamente el rasgo de la página legítima, mientras que la oferta —precios, stock, catálogo— es la señal de fraude. La versión final del sector que el vault registra no es "el proveedor se fue y dejó un hueco": es "el proveedor se fue y **su propio hueco es ahora el molde del clon**".

## [FRICTION]
> [[2026-1023-sms-activate-cierra-total-el-22-de-diciembre]] (escrita el 2026-10-23) afirma que el cierre fue "total, sin excepciones ni servicios mantenidos" y lo apoya en la fórmula "полностью", pero lo apoya en **la declaración del emisor**, no en un inventario de la web.
> Este átomo presiona esa creencia en el lado contrario: la página no tiene **nada** que inventariar —cero servicios, cero precios, cero stock, cero acceso a cuenta—, así que la afirmación de "totalidad" no necesita la declaración del emisor para sostenerse. Pero ese mismo vacío introduce una ambigüedad que el átomo anterior no registra: **"total" y "vacío" son cosas distintas**, y el vault no puede afirmar que SMS-Activate no tuviera, antes del 22 de diciembre, un catálogo comparable al de 5sim o HeroSMS, porque de la captura de cierre no se puede reconstruir el catálogo previo.
> Ambas no pueden ser completamente correctas al mismo tiempo: o la web nunca tuvo catálogo público (y entonces la comparación con 5sim/HeroSMS del thread parte de una base falsa), o lo tuvo y la captura no lo dice. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
Todo lo afirmado es observable en la captura completa (32 líneas de fuente, 126 palabras): no hay enlace a catálogo, ni a login, ni a panel, ni a bots, ni a página de servicios. Lo que **no** puede verificarse desde aquí es el estado de las APIs internas o del bot —el propio aviso da por hecho que el bot ya no responde ("больше некому обрабатывать ваши запросы")— ni si existieron subdominios operativos (por ejemplo `api.`, `bot.`) que aún respondieran. La captura solo cubre la home.
