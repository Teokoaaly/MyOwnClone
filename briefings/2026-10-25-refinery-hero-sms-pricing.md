---
id: 2026-10-25-refinery-hero-sms-pricing
type: briefing
date: 2026-10-25
sources: [sources/2026-10-24-hero-sms-pricing.md]
---

# Briefing — Refinery: captura HeroSMS `/pricing`

**Qué se procesó:** `0-raw/2026-10-24-hero-sms-pricing.md` → 6 átomos nuevos + 3 extensiones de átomos existentes + 1 propuesta de thread + este briefing. La captura se ha movido a `0-raw/archive/2026-10-25-2026-10-24-hero-sms-pricing.md`.

**Fuente:** `hero-sms.com/pricing`, 125 palabras. **La captura es un 404**: la página termina en "404 / Page not found / To the main page" y todo lo anterior es el selector de la home re-renderizado. No hay ni una fila de precio por servicio, país u operador. Es la captura más pequeña y más pobre del vault, y aun así la que produce el hallazgo más fuerte, porque es la **primera medición longitudinal de HeroSMS**: dos capturas del mismo selector separadas por 48 horas.

## El hallazgo central

**En 48 horas cambian el precio, la composición del escaparate y el reparto de stock.** Comparado contra los átomos del 2026-10-22:

| Magnitud | 2026-10-22 | 2026-10-24 | Cambio |
|---|---|---|---|
| `Whatsapp` "from" | $0.0625 | **$0.075** | **+20 %** |
| Quinta tarjeta | `Instagram+Threads` ($0.0075) | **`facebook` ($0.0075)** | rota, hereda el precio |
| Rango virtual/físico | 103x–537x | **81,7x–261,3x** | compresión |
| Físicos (4 tarjetas) | 1 948 / 98 850 / 133 403 / 104 283 | 2 044 / 127 912 / 146 558 / 109 016 | suben todos |
| Virtuales (4 tarjetas) | 0 / 10 162 287 / 21 064 192 / 25 319 129 | 0 / 10 449 189 / 26 527 953 / 28 485 193 | suben todos |

El resultado contraintuitivo: **en HeroSMS el dato menos fiable es el precio y el más fiable es el inventario**. Es exactamente al revés de la jerarquía que el thread asumía ("5sim auditable, HeroSMS opaco"). Los contadores de stock se mueven de forma coherente con un inventario real (los cuatro comparables suben en físico y en virtual, `Full rent` sigue con 0 virtuales y siendo el más caro a $0.8551), mientras el "from" se mueve un 20 % porque refleja el suelo de una combinación concreta, no un precio nominal de servicio.

## Fricciones levantadas (4, para juicio humano)

- **El "from" de `Whatsapp` sube un 20 % en 48 horas** ([[2026-1024-herosms-precio-de-whatsapp-sube-de-00625-a-0075]]) contra [[2026-1023-herosms-precios-escapate-entre-0059-y-08551]], que lo fijaba en $0.0625 como dato duro. O los "from" son valores vivos que solo valen con fecha + servicio, o el proveedor publica datos que se contradicen en 48 horas. Lo que no es admisible es citar "$0.0059-$0.8551" como rango de HeroSMS sin fechar.
- **La quinta tarjeta rota** ([[2026-1024-herosms-el-quinto-servicio-del-selector-cambia-en-dos-dias]]) contra [[2026-1023-herosms-catalogo-cinco-servicios-visibles]]: el conjunto de servicios visibles tampoco es estable, no solo el orden. El átomo previo queda como foto fechada.
- **El rango virtual/físico se comprime de 103x-537x a 81,7x-261,3x** ([[2026-1024-herosms-el-stock-virtual-comprime-su-ventaja-sobre-el-fisico]]) contra [[2026-1023-hero-sms-stock-fisico-y-virtual-por-servicio]]. El cociente es propiedad del par (tarjeta, fecha), no del proveedor. La lectura cualitativa (el físico es entre el 0,4 % y el 1,2 % del total) se sostiene.
- **La ruta de precios es un 404** ([[2026-1024-herosms-url-de-precios-devuelve-404-y-no-publica-precios-propio]]): el intento más directo de auditar precios falla por inexistencia de la ruta, no por ocultación. Confirma que la comparación de coste con 5sim sigue siendo asimétrica por construcción.

## Los tres átomos de contexto

- **El 404 no es el único hallazgo de la captura**: la página de precios incluye pestañas `Numbers`, `Emails`, `Favorites` y dos avisos "Log in" (favoritos y últimas activaciones) delante de un selector que se presenta como público. `Emails` es el único indicio de que HeroSMS vende también email. *Tentative* ([[2026-1024-herosms-la-ruta-de-precios-tambien-es-un-engano-de-cuentas]]).
- **Los contadores son vivos** ([[2026-1024-herosms-los-contadores-de-stock-siguen-vivos-dos-dias-despues]]): strengthens la crítica a los claims "500K+ números diarios" / "700+ servicios" sin necesidad de derogarlos, porque los claims son lo que no cuadra, no los contadores.
- **El "from" es la cifra más volátil del sector medido**: +20 % en dos días sobre el mismo servicio, con los cuatro vecinos clavados.

## Lo que la captura NO da

Ni una fila de precio por servicio, ni por país, ni por operador; ni el precio de un número de ChatGPT; ni la lista de países; ni plan, mínimo, forma de pago ni reembolso; ni el número de servicios detrás del `Show more` (que sigue **sin contador**). La captura es una segunda confirmación de que la ruta más obvia para auditar a HeroSMS no lleva a ningún sitio.

## Ficheros

**Átomos nuevos en `2-atoms/`** (prefijo `2026-1024`):
- `2026-1024-herosms-url-de-precios-devuelve-404-y-no-publica-precios-propio.md`
- `2026-1024-herosms-el-quinto-servicio-del-selector-cambia-en-dos-dias.md`
- `2026-1024-herosms-precio-de-whatsapp-sube-de-00625-a-0075.md`
- `2026-1024-herosms-los-contadores-de-stock-siguen-vivos-dos-dias-despues.md`
- `2026-1024-herosms-el-stock-virtual-comprime-su-ventaja-sobre-el-fisico.md`
- `2026-1024-herosms-la-ruta-de-precios-tambien-es-un-engano-de-cuentas.md` *(certainty: tentative)*

**Átomos existentes extendidos** (nota fechada al final, sin sobrescribir nada):
- `2-atoms/2026-1023-herosms-precios-escapate-entre-0059-y-08551.md` → §"Extensión (captura `/pricing`, 2026-10-24)".
- `2-atoms/2026-1023-hero-sms-stock-fisico-y-virtual-por-servicio.md` → §"Extensión (captura `/pricing`, 2026-10-24)".
- `2-atoms/2026-1023-herosms-catalogo-cinco-servicios-visibles.md` → §"Extensión (captura `/pricing`, 2026-10-24)".

**Propuesta de thread (NO aplicada a `3-threads/` por paralelismo):**
- `1-desk/thread-addition-hero-sms-pricing.md` → nueva subsección en `3-threads/economia-de-la-verificacion-y-reventa-de-cuentas.md` ("HeroSMS dos días después: la página de precios no existe y las cifras se mueven"), fricción nueva nº19 propuesta, nota de método de cuarta tanda y cuatro avisos de caducidad sobre el texto ya escrito.

**Briefing:** este archivo, `briefings/2026-10-24-refinery-hero-sms-pricing.md`.
