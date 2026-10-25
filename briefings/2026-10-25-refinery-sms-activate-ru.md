---
id: 2026-10-25-refinery-sms-activate-ru
type: briefing
date: 2026-10-25
sources: [sources/2026-10-24-sms-activate-ru-closed.md]
---

# Briefing — Refinery: captura SMS-Activate `.ru` (aviso de cierre, segunda vía)

**Qué se procesó:** `0-raw/2026-10-24-sms-activate-ru-closed.md` → 3 átomos nuevos + 2 notas fechadas en átomos existentes + 1 propuesta de thread + este briefing. La captura se ha movido a `0-raw/archive/2026-10-25-2026-10-24-sms-activate-ru-closed.md`.

**Fuente:** `sms-activate.ru/`, 126 palabras, 32 líneas. Es la **segunda captura del mismo aviso** — el vault ya tenía el `.org` del 2026-10-22 (`sources/2026-10-22-sms-activate-closed.md`).

## El hallazgo central: el aviso es byte-idéntico, solo cambia el dominio

Comparación línea por línea de las dos fuentes: **la única diferencia es la URL del frontmatter (`sms-activate.org` vs `sms-activate.ru`) y un salto de línea final**. Mismos 126 palabras, mismas cuatro preguntas de FAQ, mismo cierre, mismo "10 años", misma recomendación de HeroSMS, mismo buzón `info@sms-activate.org` (el del `.org`, aunque se entre por el `.ru`).

Eso significa que esta captura **no aporta una declaración nueva**, sino **una segunda observación sobre la misma página**, y por eso no se ha creado ningún átomo que duplique los tres que ya existían sobre el aviso. Lo que sí aporta son tres lecturas que solo se pueden hacer con la fecha de captura en la mano.

## Los tres átomos nuevos

1. **`2026-1024-sms-activate-ru-sirve-el-mismo-aviso-que-el-dominio-org`** — el aviso no vive en un solo dominio: el estado de cierre es **persistente y replicado por TLD**. Dos días después del `.org`, el `.ru` sigue en pie con el mismo texto. Consecuencia: la auditoría de dominio deja de ser binaria (un `.ru` no es un clon, es el propio proveedor ya sin negocio) y la marca sigue ocupando espacio DNS aunque el negocio haya muerto.

2. **`2026-1024-los-dominios-oficiales-solo-muestran-el-aviso-y-ningun-catalogo`** — la página post-cierre es una lápida estática: **cero catálogo, cero precios, cero stock, cero login, cero balance, cero bot, cero formulario de compra**. La ausencia de oferta es la **firma observable del cierre** y, por tanto, el criterio de auditoría que faltaba: cualquier sitio llamado SMS-Activate *que además tenga oferta* es un clon por definición.

3. **`2026-1024-el-plazo-de-contacto-del-aviso-ya-habia-caducado-al-capturarse`** — el aviso capturado el 2026-10-24 sigue anunciando "до 30 апреля" con SLA de 7 días, y "Выводы были доступны до 5 февраля". Ninguna fecha lleva año y el texto está en pasado, así que el 22 de diciembre es un diciembre **ya transcurrido**: 5 de febrero y 30 de abril son anteriores a la captura, **sea cual sea el año**. La "ventana de contacto" ya estaba cerrada cuando el vault la leyó como abierta.

## Fricciones levantadas (3 en los átomos + 2 propuestas al thread, para juicio humano)

- **La advertencia antiestafa, tomada al pie de la letra, se contradice con la captura.** El aviso dice que todo servicio llamado SMS-Activate es un fraude; pero el 2026-10-24 existe uno que no lo es: `sms-activate.ru`, el operador legítimo ya sin negocio. La frase rusa se refiere a los servicios que **venden activaciones** bajo ese nombre. El átomo existente del 2026-10-23 necesita esa acotación.
- **El calendario de liquidación tiene una ventana que el vault leía como abierta y estaba cerrada.** El "hasta 7 días" no es un SLA exigible: no hay a quién escribirle. La ventana de contacto pasa de "activa con SLA" a "etiqueta histórica de un plazo vencido".
- **La identidad registral de los dominios no está zanjada.** La captura no dice quién controla hoy el `.ru` (misma empresa, un tercero que lo compró, un agente de dominio sin relación) ni si `.org` y `.ru` son del mismo titular. El cuerpo idéntico es un indicio fuerte de continuidad, **no** una prueba. El vault registra "el mismo aviso se sirve en dos dominios", no "SMS-Activate conserva dos dominios".

## Nota sobre el año del 22 de diciembre

La captura **no resuelve** el año del cierre, y no hay que leerlo como resuelto. El átomo anterior lo dejó explícitamente abierto; aquí se mantiene abierto. Lo único que se afirma es la **caducidad** de las dos ventanas (5 de febrero y 30 de abril) respecto de la fecha de captura, que es independiente del año.

## Lo que la captura NO da

Ni cifras, ni catálogo previo (la captura de cierre no permite saber si SMS-Activate tenía un catálogo comparable al de 5sim o HeroSMS antes del 22 de diciembre), ni estado de las APIs internas o del bot, ni subdominios operativos (`api.`, `bot.`), ni responsable registral de los dominios, ni más TLD. La captura cubre solo la home.

## Ficheros

**Átomos nuevos en `2-atoms/`** (prefijo `2026-1024`):
- `2026-1024-sms-activate-ru-sirve-el-mismo-aviso-que-el-dominio-org.md`
- `2026-1024-los-dominios-oficiales-solo-muestran-el-aviso-y-ningun-catalogo.md`
- `2026-1024-el-plazo-de-contacto-del-aviso-ya-habia-caducado-al-capturarse.md`

**Átomos existentes ampliados** (nota fechada `[NOTA 2026-10-24 — captura sms-activate.ru]`, sin sobrescribir ninguna afirmación previa):
- `2-atoms/2026-1023-sms-activate-contacto-hasta-el-30-de-abril-con-plazo-de-7-dias.md` → la ventana ya había caducado; la página oficial es texto congelado.
- `2-atoms/2026-1023-sms-activate-nombre-retirado-cualquier-servicio-igual-es-fraude.md` → acotación literal de la advertencia antiestafa; la señal es el contenido, no el nombre de dominio.

**Propuesta de thread (NO aplicada a `3-threads/` por paralelismo):**
- `1-desk/thread-addition-sms-activate-ru.md` → nueva §6.1 "El cierre era un estado replicado, no un evento único" (6.1.1–6.1.4) + fricciones nº23–26 + nota de método, para pegar en `3-threads/economia-de-la-verificacion-y-reventa-de-cuentas.md` (§6).

**Briefing:** este archivo, `briefings/2026-10-24-refinery-sms-activate-ru.md`.
