---
id: 2026-10-25-refinery-gptgrok2api-veridrop
type: briefing
date: 2026-10-25
sources: [sources/2026-10-24-gptgrok2api.md, sources/2026-10-24-veridrop-home-leaderboard.md]
---

# Briefing de Refinery — gptGrok2api (AuuCoder) + home/leaderboard de VeriDrop

**Capturas procesadas:**
- `0-raw/2026-10-24-gptgrok2api.md` → archivada en `0-raw/archive/2026-10-25-2026-10-24-gptgrok2api.md`
- `0-raw/2026-10-24-veridrop-home-leaderboard.md` → archivada en `0-raw/archive/2026-10-25-2026-10-24-veridrop-home-leaderboard.md`

**Fuentes originales:** `sources/2026-10-24-gptgrok2api.md` (README de `https://github.com/AuuCoder/gptGrok2api`, 37827 bytes) y `sources/2026-10-24-veridrop-home-leaderboard.md` (home de `https://veridrop.org/`, 26401 bytes), ambas capturadas el 2026-10-24.

**Átomos creados:** 14, todos con prefijo `2026-1024-` (8 de gptGrok2API, 6 de VeriDrop).
**Átomos existentes extendidos:** 1, con nota fechada (sin sobrescribir ninguna afirmación previa).
**Threads tocados:** ninguno. La actualización se propuso en `1-desk/thread-addition-gptgrok2api-veridrop.md`, con destino separado para cada captura, y se aplicó el 2026-10-25.

## Qué aportan estas dos capturas al vault

Son dos capturas que **tocan extremos opuestos de la misma cadena**. La de gptGrok2API documenta **el productor** —el eslabón que faltaba entre los insumos de un alta y el mercado de cuentas revendidas— y la de VeriDrop documenta **la superficie comercial del detector**, es decir, **la parte del mercado donde la posición se vende y la medición no**. Juntas, cierran el circuito: quién fabrica la capacidad y quién decide qué se ve en la primera pantalla.

## Captura A — `AuuCoder/gptGrok2api`: el gateway que también fabrica la cuenta

**Ocho átomos.** Los tres primeros cubren la arquitectura (gateway unificado, compatibilidad multiprotocolo y despacho por modelo, registro por protocolo con captcha solver integrado); los cinco nuevos cubren el aprovisionamiento y la operación.

### Los hallazgos que cambian algo

1. **El corrector de captcha está internalizado, no comprado.** `captcha-solver/` con navegador real (Chromium/CloakBrowser) dentro de Docker/Xvfb, con concurrencia dinámica, proxy por petición y reciclaje del navegador, su propio venv, su propio `docker-compose.captcha-solver.yml` y su propio servicio systemd. **El coste del captcha deja de ser $/1000 y pasa a ser coste de infraestructura escalado por altas simultáneas.** Es la tercera vía que el thread de economía de la verificación no tenía: comprar por unidad, internalizar, o evitar el destino.

2. **El correo tiene contrato y techo.** Sidecar propio de iCloud Privacy Mail: **20 buzones/hora** (interfaz nueva), **5/hora** (antigua), **25/hora** sumando ambas, y **tope duro de 750 buzones acumulados por cuenta**, con temporizador de 60 minutos. Estado de asignación por plataforma sobre el mismo buzón (verde = GPT, azul = Grok). El correo deja de ser un coste por unidad sin techo: pasa a tener **ciclo de vida y rendimiento decreciente por diseño**.

3. **La taxonomía de tres estados para credenciales.** El sondeo corre cada 60 min en lotes de 50 y distingue **inválido** (relee correo y contraseña, reintenta con backoff 1/2/4/8/16/24 h), **desconocido por timeout** (no toca la cuenta) y **no efectivo por cuota** (un `402` **no** es un fallo de autenticación; reintento a 60/120/300 s). Cada clasificación errónea destruye capacidad — es la pieza transferible a cualquier integración con cuentas de terceros.

4. **La IP es arquitectura, no opción.** Jerarquía de salidas: proxy global, proxy por cuenta, grupos, límite de concurrencia por nodo, salida de reserva, WARP + Privoxy (SOCKS5→HTTP) y FlareSolverr; puertos 40000/40080/8191; **salida sticky compartida entre las tres fases del checkout** y rotación solo en la promoción.

5. **La cadena de valor vista desde el productor.** Tras un registro de Grok exitoso, la cuenta entra en una cola de prioridad de OAuth con 2 workers y **se entrega a NovaApi y a CPA**; la integración con Sub2API usa `Base URL: http://gptgrok2api/v1` y el alias de red `gptgrok2api`. El README advierte que un Sub2API normal puede carecer del tipo OAuth de xAI y que la imagen por defecto `weishaw/sub2api:latest` puede no servir. **Esto abre una fricción**: el "canal de origen" que PriceAI publica describe **el escaparate del relay, no su aprovisionamiento**.

6. **Popularidad sin mantenimiento, y con linaje declarado.** 285 estrellas, 145 forks, 24 commits, 12 tags, MIT, último release v1.2.1 del **27 de julio de 2026** (tres meses sin actividad). Se declara desarrollo secundario de `yukkcat/chatgpt2api` y el primer commit dice "Clean project history owned by AuuCoder" — es decir, **el linaje no es auditable por `git log`**, solo por declaración.

### Superficie de API (para el thread de arquitectura)

`GET /v1/models`, `POST /v1/chat/completions`, `POST /v1/responses`, `POST /v1/messages`, `POST /v1/images/generations`, `POST /v1/images/edits`, `POST /grok/v1/videos`; consola en `/`. `/v1` despacha por modelo entre tres catálogos (GPT, Grok SSO, Grok Build OAuth) y conserva `/grok/v1` como interfaz Grok completa. Token Bearer único. Para MyOwnClone: **otra entrada de `OPENAI_API_BASE`, sin adaptador nuevo**.

## Captura B — `veridrop.org` home + leaderboard: donde la posición se vende y la medición no

**Seis átomos** (cinco nuevos más la extensión fechada del átomo del directorio).

### Los hallazgos que cambian algo

1. **El "Top 10" de la home es un bloque publicitario, y las URLs lo demuestran.** Cada fila lleva `sponsored=1`, un `slot` que nombra la plaza comprada (`t1`…`t10`; solo `t1`…`t5` en "Opus 5"; `apikey_ot1` como marca blanca en la primera fila de "Opus 4.8"), `surface=home_model_board_top_paid` y un parámetro **`pos` que siempre vale "puesto en la home + 10"**, es decir, entre 11 y 20. Hay dos lecturas posibles —posición real en `/leaderboard` o índice de inserción— y **la captura no permite decidir**. Lo que sí es sólido en las dos: **lo que se ve en la home no es la cabeza del ranking**, es un bloque comprado y renumerado. Por eso este átomo va en `tentative`.

2. **"Top 10" no son diez sitios distintos.** Las 35 filas de los cuatro tableros son **14 relays distintos**: "Opus 4.8", 10/10; "GPT 5.6", 10 filas y 8 sitios (`mintpop.ai` tres veces, con cifras idénticas); "Opus 5", **5 filas y 3** (`shushutoken.com` en los puestos 2, 4 y 5); "Fable 5", 10 filas y 5 (`shushutoken.com` cuatro veces, `api.zhaomoxing.com` tres veces).

3. **La disponibilidad es una propiedad del par (sitio, modelo).** `shushutoken.com`: 100 % / 100 % / 100 % / **67 %**; `88api.ai`: 96 % / 87 % / 96 %; `mintpop.ai`: 78 % / 80 % / 84 % / 78 %; `www.hejuapi.com`: 98 % / 89 % / 96 %. Y la latencia se mueve con el modelo (`routerra.ai`: 3,3 s en Opus 4.8 y 5,9 s en GPT 5.6). **Ninguno de estos porcentajes es comparable con la columna de 7 días de PriceAI sin conocer el denominador**; las columnas "última sondeo" y "estado de ejecución" aparecen **vacías en las 35 filas**.

4. **El precio sí está en la home, pero solo en el texto publicitario — y en otra unidad.** La home no tiene columna de precio, pero el bloque de promoción expresa el precio como **descuento sobre la tarifa oficial** (notación china de décimas) y no como el multiplicador compuesto de PriceAI. Valores: `88api.ai` 0,3 y 0,1 del oficial; `cc.yzzt.top` 0,25 y 0,06; `coding.dx.com.ai` 0,2 y 0,15; `ai.wcapis.com` 0,046 y 0,12; `jizhiapi.site` con **multiplicador 0,049** en el propio título del enlace; `shushutoken.com` anunciando **"1,4 %-7,9 % del precio oficial"**; `routerra.ai` $10/$10; `omniakey.com` y `api.zhaomoxing.com` **sin ninguna cifra**. La fila de `shushutoken.com` es **la más extrema y la más difícil de auditar de todo el sector**: un 1,4 % del precio oficial de GPT es un orden de magnitud por debajo de cualquier multiplicador publicado, y la única evidencia pública que ofrece el vendedor es un test de inteligencia que no se publica.

5. **El sitio separa posición de métrica, y ofrece su propio criterio de auditoría.** "El pago no modifica ni la puntuación ni el leaderboard"; la disponibilidad y la latencia de cada fila son datos reales de sondeo. La tabla advierte que **las filas patrocinadas a mano por código se marcarían como "valor de presentación estático"** — y **ninguna de las 35 filas capturadas lo está**. Es una afirmación más fuerte y más útil que "el ranking no se vende", y el vault la registra **con su condicional**: el sitio declara el criterio, la captura no permite verificar que se aplique más allá de estas 35 filas.

6. **El nivel de evidencia varía por modelo.** Los tableros de Claude están etiquetados "cifrado · API Key autorizada del webmaster" (verificación por **firma criptográfica**); el de OpenAI, "nivel de protocolo" (campos de protocolo, uso de tokens y huella de comportamiento). Es decir, **una misma cifra de disponibilidad es una afirmación más fuerte en un tablero de Claude que en uno de OpenAI**, con formato idéntico.

## Fricciones que quedan abiertas (no auto-resueltas)

1. **La ausencia de precio es una propiedad de la página, no del sitio** (fricción registrada en átomo contra `2026-1024-veridrop-directorio-solo-deteccion-sin-precios`). El directorio no publica ni un precio; la home publica una decena de descuentos. El átomo previo sigue siendo cierto **para `/relays`**, pero no puede generalizarse al sitio.
2. **El "canal de origen" de PriceAI describe el escaparate, no el aprovisionamiento** (fricción registrada en átomo contra `2026-1023-priceai-transit-canal-tipo-sub2api-vs-new-api`). El README de gptGrok2API prueba que por detrás de un relay Sub2API puede haber un productor de cuentas que le entrega credenciales por API. La captura de PriceAI no define la semántica del campo.
3. **El significado de `pos` queda sin verificar.** Hace falta capturar `/leaderboard` de al menos un relay con su ordenación visible. Con lo que hay, la formulación honesta es: "el Top 10 de la home es un bloque patrocinado y su relación con el ranking real está sin verificar".

## Advertencia metodológica

Casi todo lo que ambos sitios afirma es **claim del propio autor**: los 17 módulos del README, los siete endpoints, las cifras de buzones por hora, los códigos de error y los backoffs, la cobertura de 12.292 relays, la política de "el pago no cambia la detección". Lo único **medido sobre la captura** son los recuentos: 35 filas, 14 sitios distintos, los valores `pos`/`slot` extraídos de las URLs, las 35 celdas de disponibilidad y latencia, la tabla de metadatos de GitHub (285/145/3/1/12/24). **El vault no ha clonado ni ejecutado `gptGrok2api`** ni ha auditado `captcha-solver/`; no ha capturado `/leaderboard` ni ninguna página de detalle por relay de VeriDrop. De ahí que la lectura de `pos` quede en `tentative` y que la ausencia de precios en `/relays` se documente como resultado de búsqueda literal y no de lectura.

**Sin literales CJK en los átomos.** Las citas en chino se traducen y, cuando la notación es imprescindible (la de décimas de precio), se explica en español. Ningún token, clave ni credencial aparece en las notas: el valor de autenticación queda como `[REDACTED]`.

## Pendiente para el Editor

- Aplicado el 2026-10-25:
  - **Captura A** → `3-threads/myownclone-platform-architecture.md`, sección "El arquetipo tiene dos ediciones" (subsección nueva "Una tercera edición del arquetipo") **y** `3-threads/economia-de-la-verificacion-y-reventa-de-cuentas.md` (§7, fricción 18 sobre internalizar el captcha).
  - **Captura B** → `3-threads/el-agregador-de-precios-como-producto.md`, **§8 nueva** (8.1–8.7) antes de las fricciones, que pasarían a ser §9, **y fricción 11** sobre el parámetro `pos`.
- Actualizar `updated:` en el frontmatter de los dos threads y añadir las dos fuentes a su lista `sources:`.
- Decidir si la §8 del thread del agregador va antes o después del bloque de fricciones, y si renumera las fricciones 6–10.
- Revisar la nota fechada añadida a `2026-1024-veridrop-directorio-solo-deteccion-sin-precios.md`: acota el alcance sin tocar el claim original.
- Si alguien quiere cerrar la fricción 3, la captura pendiente es `/leaderboard/<relay>` con la ordenación visible.

## Fechas

Las notas fechadas están marcadas como `## Nota fechada — 2026-10-25 (Refinery, ...)`. No se sobrescribió ninguna afirmación previa.
