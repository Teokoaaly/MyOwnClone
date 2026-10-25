# Refinery Report — 2026-10-25

Run: 03:00 shift (scheduled cron). Fuentes capturadas por el Scout del 2026-10-24.

## Estado de partida

`0-raw/` contenía **17 punteros de captura** con `Status: ready` (18 ficheros en el directorio, uno de ellos `reading-list.md`, excluido por definición). Los 17 apuntaban a 17 fuentes en `sources/2026-10-24-*.md`. No había anomalía de procedencia como la del run del 2026-10-24: cada captura traía su campo `Source:` y la ruta existe.

| Métrica | Valor |
|---|---|
| Capturas procesadas | **17** |
| Átomos nuevos | **155** (prefijo `2026-1024-`) |
| Átomos existentes extendidos | **13** (nota fechada al final, sin sobrescribir) |
| Átomos retirados a `2-atoms/archive/` | 0 (11 preexistentes, intactos) |
| Bloques `## [FRICTION]` nuevos en átomos | **29** (en 29 de los 155 átomos nuevos) |
| Fricciones añadidas a `3-threads/` | **29** (10 + 18 + 1) |
| Threads actualizados | **4** |
| Threads creados | 0 |
| Enlaces rotos introducidos | **0** |
| Fuentes huérfanas | 0 (las 17 tienen ≥3 átomos) |
| Ficheros de `sources/` modificados | 0 |
| Capturas modificadas | 0 (verificado byte a byte contra `HEAD`) |
| Átomos eliminados | 0 |

## Capturas procesadas

| # | Fuente | Átomos nuevos | Atoms extendidos |
|---|---|---|---|
| 1 | `flokinet-vps-pricing` | 17 | 0 |
| 2 | `alexhost-home` | 16 | 0 |
| 3 | `brightdata-proxy-pricing` | 15 | 1 |
| 4 | `protonvpn-pricing` | 14 | 1 |
| 5 | `mullvad-pricing` | 11 | 2 |
| 6 | `iproyal-pricing` | 10 | 0 |
| 7 | `1984-hosting-vps` | 8 | 0 |
| 8 | `github-search-chatgpt-account-creator` | 8 | 0 |
| 9 | `gptgrok2api` | 8 | 2 |
| 10 | `internet-bs-domains` | 7 | 0 |
| 11 | `anubizhost-offshore-vps` | 6 | 2 |
| 12 | `hero-sms-pricing` | 6 | 3 |
| 13 | `veridrop-home-leaderboard` | 6 | 1 |
| 14 | `njal-la-domains-vpn` | 8 | 1 |
| 15 | `njalla-com-corporate` | 3 | 0 |
| 16 | `sms-activate-ru-closed` | 3 | 3 |
| 17 | `chatgpt-creator-verssache` | 11 | 0 |

Las 17 capturas se movieron a `0-raw/archive/2026-10-25-2026-10-24-<nombre>.md`. `0-raw/` queda con solo `reading-list.md` y `archive/`.

## Threads actualizados

| Thread | Qué entró | Fricciones |
|---|---|---|
| `escala-de-hosting-barato-y-el-limite-de-4-euros` | §8.12 AlexHost (8.12.1–8.12.9), §8.13 njal.la / njalla.com, §8.14 Internet.bs; frontmatter `sources` 15→19, `links` 15→54 | 27–36 (10) |
| `economia-de-la-verificacion-y-reventa-de-cuentas` | §2 HeroSMS (con nota de caducidad), §6.1 SMS-Activate `.ru`, §7.5 corpus de registro, §8.7 IPRoyal, §8.8 Mullvad, §8.9 ProtonVPN, §10 Bright Data (10.1–10.8), §11 ChatGPT Creator | 18–35 (18) |
| `el-agregador-de-precios-como-producto` | §8 home de VeriDrop y sus cuatro tableros patrocinados (8.1–8.7); la §8 de fricciones pasó a §9 | 11 (1) |
| `myownclone-platform-architecture` | §"Una tercera edición del arquetipo: el gateway que también fabrica la cuenta" (gptGrok2api: gateway unificado, correo iCloud, captcha internalizado, jerarquía WARP/Privoxy/FlareSolverr, cadena proveedor→gateway→relay→reventa) | bloque `## [FRICTION]` en el átomo, referenciado desde el thread |

## Fricciones para juicio humano (29)

### `escala-de-hosting-barato-y-el-limite-de-4-euros` (27–36)

- **27** — AlexHost: el mismo CPU (2x Xeon E5-2699 v3) a $149 y a $224 (×1,50), con specs transcritas idénticas. No son dos tablas distintas como en Evoxt: es el mismo catálogo con el producto duplicado.
- **28** — AlexHost: el configurador de VPS es transaccional solo en 3 de 24 fichas; 21 repiten un ancla `alexhost.com/#` y 7 no muestran importe.
- **29** — AlexHost: el precio no es función de la capacidad (disco en siete variantes: "SSD or SATA HDD", "SSD or NVMe", "SSD", "NVMe SSD", "1TB SSD", "2 x 2TB NVMe", "M2 NVMe, M2 SSD or SATA HDD"), con tarifa de disco alterada en octubre de 2026.
- **30** — `njalla.com` ya no es el servicio de privacidad: la captura del 2026-10-24 lo muestra como web de consultoría sin producto; el servicio está en `njal.la`. El plan maestro `MASTER-DEFINITIVO-2026-07.md` §3 sigue apuntando a la URL antigua y usa "ellos son el dueño legal" como rasgo vigente.
- **31** — "Pago en XMR" no es "pago anónimo": `njal.la` acepta Monero pero no publica nada sobre identidad, reembolso, confirmación ni recargo. Contraste con ExtraVM ("No identity verification is required...") y Skhron, que sí enumeran lo que no piden.
- **32** — `njal.la` publica €15/año sin matriz TLD-a-TLD, sin escalones ni multi-año; 1984 publica DNS anycast gratis pero no la tarifa de registro. Con las dos matrices ausentes no hay comparación posible.
- **33** — `njal.la` no es cotizable (una sola cifra para tres productos) pero es el único dato de registro con precio del vault.
- **34** — El WHOIS privado "FREE for life with all domain name registrations" de Internet.bs no puede ser la misma regla que el "en los TLD que lo permiten" de 1984, capturado el mismo día. Internet.bs no enumera los TLD donde aplica.
- **35** — La promoción de $6.99 es precio de entrada: el primer año, máximo 5 .COM por cliente, con verificación de elegibilidad y derecho del proveedor a cobrar la diferencia. El precio de renovación no aparece en la captura.
- **36** — El precio de dominio del vault es hoy un número, y el mercado lo trata como una escalera con tres variables: descuento por volumen, límite por cliente (5 .COM) y precio de renovación vía tracker externo.

### `economia-de-la-verificacion-y-reventa-de-cuentas` (18–35)

- **18–22** (Bright Data): el precio del proxy se multiplica (×4 frente a DataImpulse en residencial, ×8 en datacenter); el compromiso de capital eclipsa al descuento por volumen ($499/mes mínimo, dos órdenes de magnitud sobre el techo de ≤ €4/mes); KYC obligatorio en residencial y móvil pero no en Web Unlocker; suspensión por saldo perder las IPs; dos tablas de precios por IP sin etiqueta.
- **23** (IPRoyal): el $/GB no es la unidad del sector, es la de DataImpulse. IPRoyal publica cinco líneas con cinco unidades distintas, y una factura por proxy con "unlimited bandwidth" —coste marginal de bytes **cero**—, lo que contradice el diagnóstico del thread de que el proxy es la única partida dependiente de un volumen no controlado.
- **24** (Mullvad): €5/mes IVA incluido sin cambio desde 2009, con pago en efectivo por sobre y token aleatorio; 5 dispositivos por cuenta y sin port-forwarding; sin plan gratuito ni ventas.
- **25** (ProtonVPN): el descuento caduca y la renovación sube a $6,99/mes (30 % off, no 65 %) — el mismo producto a dos precios según el momento de la compra.
- **26** (HeroSMS): el "from" de Whatsapp sube un 20 % en 48 horas ($0,0625 → $0,075) contra el átomo del 2026-10-22 que lo fijaba como dato duro; la quinta tarjeta del selector rota; el rango virtual/físico se comprime de 103x–537x a 81,7x–261,3x; y la ruta `/pricing` devuelve **404**.
- **27–30** (SMS-Activate `.ru`): el aviso de cierre es **byte-idéntico** al del `.org` (mismos 126 palabras, mismo FAQ, mismo buzón `info@sms-activate.org`); la página post-cierre es una lápida sin catálogo, precios, stock, login, balance, bot ni formulario —la ausencia de oferta es la firma observable del cierre, y por tanto el criterio de auditoría que faltaba (cualquier sitio llamado SMS-Activate *que además tenga oferta* es un clon por definición); el aviso se captura meses después de que su propia ventana de contacto haya caducado ("до 30 апреля" sin año, redactado en pasado); y la advertencia anti-fraude del propio proveedor se refiere a los servicios que venden activaciones bajo ese nombre, no al original ya sin negocio.
- **31–33** (ChatGPT Creator): el alta real contra OpenAI no pasa por teléfono —nueve pasos HTTP, verificación por OTP de correo—, corrige la simplificación implícita del thread y de la guía de HeroSMS; el captcha no aparece en esa ruta y el correo lo genera el propio bot, así que la partida dominante del flujo es construcción (TLS fingerprinting con perfiles Chrome aleatorizados, sentinel token, cabeceras de traza Datadog), no compra; y el repositorio lleva 4 commits y 338 estrellas sin mantenimiento visible.
- **34–35** (GitHub Search): el corpus indexado es de 14 repositorios, **cerrado** (`incomplete_results: false`), de los cuales 3 son falsos positivos y 4 de los 11 reales van sin `description`; el 94,1 % de las estrellas está en tres repositorios; y **la categoría entera lleva parada** —10 de 14 publicada su primer push en 24 horas y ninguno había hecho push en los últimos 88 días.

### `el-agregador-de-precios-como-producto` (11)

- **11** — El "Top 10" de la home de VeriDrop no es un ranking: el parámetro `pos` vale siempre `puesto + 10` (de 11 a 20) y `slot` nombra la plaza comprada, con inventario de plazas que varía por modelo (5 en "Opus 5", 10 en los demás). Si `pos` es la posición real, la home muestra los relays clasificados 11.º a 20.º renumerados como #1 a #10. El vault no puede decidirlo con la captura actual: hace falta capturar `/leaderboard` de al menos un relay con su ordenación visible.

## Errores y cosas que necesitan atención humana

1. **Escrituras concurrentes en el thread compartido (resuelto).** El primer lote de subagentes escribió a la vez en `escala-de-hosting-barato-y-el-limite-de-4-euros.md` y las ediciones se pisaron. Se detectó y los subagentes restauraron. Las 12 integraciones posteriores se redirigieron por archivos de propuesta en `1-desk/`, que luego se aplicaron de forma secuencial y verificada. Sin pérdidas.
2. **La premisa del encargo sobre AlexHost era falsa (verificado).** El encargo anticipaba que la captura declararía "bulletproof" / DMCA-ignored / no-KYC. La captura **no dice ninguna de esas cosas**. Lo único que sobrevive del positioning es una ruta de assets heredada (`img/dmca/icons/` para ocho de las nueve banderas), que es diseño de interfaz, no declaración. El átomo `2026-1024-alexhost-sin-postura-dmca-ni-declaracion-de-no-kyc` registra la ausencia.
3. **Fricción pendiente de numeración en el thread B.** La fricción "captcha internalizado frente a coste de catálogo" (gptGrok2api) quedó registrada como bloque `## [FRICTION]` en su átomo canónico y referenciada desde `myownclone-platform-architecture.md`, **sin** número en la §9 de `economia-de-la-verificacion-y-reventa-de-cuentas.md`, para no colisionar con la numeración en curso de ese thread. Es la única fricción de esta tanda sin asiento numerado propio.
4. **Una captura es parcial y así queda declarada.** `hero-sms-pricing` es la página de precios renderizada con un **404** al final: 125 palabras, sin una sola fila de precio. Los 6 átomos se extrajeron solo de lo presente (la URL inexistente, los contadores de stock vivos, la quinta tarjeta rota, la ruta de precios muerta). No se rellenó con conocimiento externo.
5. **Renombrado de las capturas archivadas.** Los subagentes archivaron con prefijo `2026-10-24-` (la fecha de la captura). Los tres runs anteriores usan el prefijo de la fecha de **procesamiento** (`2026-10-24-2026-10-23-*`, `2026-10-23-2026-10-22-*`). Renombradas a `2026-10-25-2026-10-24-*` para restores la convención; el contenido de las 17 es idéntico byte a byte al original en `HEAD`.

## Verificación

- **Enlaces:** los 195 wikilinks nuevos introducidos en `3-threads/` resuelven todos a un fichero existente de `2-atoms/` o `3-threads/`. El único enlace no resoluble del vault (`[[myownclone]]`) es **preexistente** en `HEAD` y no fue introducido aquí.
- **Numeración:** sin números de sección duplicados en ningún thread tocado; sin números de fricción duplicados (1–36, 1–35, 1–11, todos continuos y únicos).
- **Trazabilidad:** los 155 átomos nuevos tienen campo `sources:` y **todas** las rutas citadas existen en disco. Verificado con comprobación programática: 0 átomos sin fuente o con fuente inexistente.
- **Integridad de capturas:** las 17 capturas archivadas son byte a byte idénticas a su versión en `HEAD` (comparación sha256 sobre el blob de git). `0-raw/reading-list.md` intacto.
- **Idiomas:** los caracteres CJK/Cirílico que aparecen en el material nuevo son **citas textuales de las fuentes** (el aviso en ruso de SMS-Activate, la terminología china de VeriDrop), no mojibake de generación.
- **Modificaciones de átomos existentes:** 0 líneas eliminadas en `2-atoms/` — las 13 extensiones son puro añadido.
