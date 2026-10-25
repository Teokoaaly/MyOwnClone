---
id: 2026-1023-sms-activate-contacto-hasta-el-30-de-abril-con-plazo-de-7-dias
type: atom
certainty: solid
sources: [sources/2026-10-22-sms-activate-closed.md]
links: ["[[2026-1023-sms-activate-retiradas-hasta-el-5-de-febrero]]", "[[2026-1023-sms-activate-cierra-total-el-22-de-diciembre]]", "[[2026-1023-hero-sms-openai-bloquea-numeros-voip-y-reintento-en-un-minuto]]"]
---

## Claim
Tras el cierre, SMS-Activate mantiene **una única vía de contacto, por email** (`info@sms-activate.org`), y solo para "las preguntas más importantes" (по самым важным вопросам), **hasta el 30 de abril**. El aviso fija además un **plazo de respuesta declarado de hasta 7 días** ("Время ответа — до 7 дней"). El resto de canales (bot, chat, soporte) dejan de existir como interlocutor: el cierre es total y la única ventana es un buzón de email con fecha de caducidad.

## Why It Matters
El calendario del aviso es la forma más legible del modelo de cierre del sector: actividad cesada el 22 de diciembre → retiradas cortadas el 5 de febrero → **ventana de contacto hasta el 30 de abril con SLA de 7 días** ([[2026-1023-sms-activate-retiradas-hasta-el-5-de-febrero]]). Cuatro meses de plazo de respuesta es un SLA de una organización ya en liquidación práctica, no de una empresa operando.
Para el vault, el dato relevante es el **silencio posterior**: después del 30 de abril no queda ningún canal. Eso significa que cualquier disputa de saldo, cualquier reclamación o cualquier duda sobre la migración de tecnología a HeroSMS deja de tener destinatario. Es un recordatorio de que en aprovisionamiento de infraestructura crítica, la ventana de soporte de un proveedor es un activo que se agota y que hay que usar antes del cierre, no después.

## [FRICTION]
> [[2026-1023-hero-sms-openai-bloquea-numeros-voip-y-reintento-en-un-minuto]] (escrita hoy, desde la página de verificación de HeroSMS) documenta que HeroSMS gestiona sus incidencias operativas con un mecanismo de **reintento en un minuto** para números rechazados por OpenAI, es decir, un soporte reactivo con SLA corto.
> Este átomo presiona esa creencia porque la estructura de soporte de HeroSMS es la de un **proveedor en crecimiento**, y el contraste con SMS-Activate (buzón de email, hasta 7 días de respuesta, ventana de 4 meses, luego silencio) muestra que el SLA corto de HeroSMS es una ventaja de proveedor vivo, no una propiedad estructural del sector: en este sector los SLAs de soporte se degradan a **correo sin respuesta** cuando el operador entra en liquidación, con independencia del producto que se distribuya.
> Ambas no pueden ser completamente correctas como una única regla del sector: o el SLA de un minuto de HeroSMS es representativo de cómo funcionan estos servicios, o es un efecto de la escala y el respaldo del operador, y el caso base del sector es el silencio. Marcado para juicio humano, no auto-resuelto.

## [NOTA 2026-10-24 — captura `sms-activate.ru`]
Fuente: `sources/2026-10-24-sms-activate-ru-closed.md` (mismo aviso, servido además en el dominio `.ru`). **Sin sobrescribir nada de lo anterior.**

Dos precisiones que esta segunda captura añade sobre el calendario de cierre:

1. **La ventana de contacto que este átomo describe como activa ya había caducado.** El aviso se captura el **2026-10-24** y sigue diciendo "до 30 апреля" sin año, con el texto íntegro en pasado ("прекратили", "были доступны"), de modo que el 5 de febrero y el 30 de abril son anteriores a la fecha de captura, sea cual sea el año del 22 de diciembre. El "hasta 7 días" es por tanto una **etiqueta histórica de un SLA ya vencido**, no un compromiso exigible. Ver [[2026-1024-el-plazo-de-contacto-del-aviso-ya-habia-caducado-al-capturarse]].

2. **La página oficial es un texto congelado, no un estado vivo.** Servida sin cambios en dos dominios (`.org` el 2026-10-22 y `.ru` el 2026-10-24, cuerpo byte-idéntico), no ofrece catálogo, ni precios, ni stock, ni login, ni bot: solo la lápida y la recomendación de HeroSMS. Ver [[2026-1024-los-dominios-oficiales-solo-muestran-el-aviso-y-ningun-catalogo]] y [[2026-1024-sms-activate-ru-sirve-el-mismo-aviso-que-el-dominio-org]].

La regla operativa que sale de esto: **una web de proveedor cerrado documenta un estado pasado, no el presente**; hay que fechar la lectura contra la fecha de captura.

## Nota de verificación
La dirección `info@sms-activate.org` y la fecha del 30 de abril están transcritas del aviso; el aviso no indica año para ninguna de las dos fechas. El "hasta 7 días" es una declaración del proveedor sobre su propio tiempo de respuesta, sin histórico que lo respalde.
