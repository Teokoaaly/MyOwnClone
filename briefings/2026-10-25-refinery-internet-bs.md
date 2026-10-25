# Briefing de Refinery — captura Internet.bs (2026-10-24)

> **Alcance:** una sola captura, `0-raw/2026-10-24-internet-bs-domains.md` (home de `internet.bs`, 1206 palabras de fuente). Atomizada el 2026-10-24.
> **Thread afectado:** [[escala-de-hosting-barato-y-el-limite-de-4-euros]]. La propuesta de actualización (`1-desk/thread-addition-internet-bs.md`) se aplicó a `3-threads/` el 2026-10-25.

---

## Qué se procesó

`0-raw/2026-10-24-internet-bs-domains.md` → fuente `sources/2026-10-24-internet-bs-domains.md`.

Internet.bs es un **registrador de dominios**, no un proveedor de hosting. Su home publica un único titular de precio (`.com at $6.99`, welcome offer), un bundle de cinco servicios "free for life", los términos promocionales completos, un buscador con una máquina de estados de disponibilidad, y un bloque de datos históricos sobre el mercado de inversión de dominios.

## Átomos creados (7)

| Átomo | Idea | Certeza |
|---|---|---|
| [[2026-1024-internet-bs-com-a-6-99-y-cinco-servicios-gratis-de-por-vida]] | .com a $6.99 + cinco servicios de por vida (WHOIS, DNS, tracker, reenvío URL y correo) | solid |
| [[2026-1024-internet-bs-promocion-com-cinco-dominios-y-fraude-de-multicuenta]] | Solo primer año, solo clientes nuevos, máx. 5 .COM, y fingerprinting por IP/dispositivos/pago para unificar cuentas | solid |
| [[2026-1024-internet-bs-whois-gratuito-de-por-vida-con-2fa-y-alertas-de-login]] | WHOIS privado "for life with all domain name registrations" + 2FA + alertas de login + edad mínima 16 | solid |
| [[2026-1024-internet-bs-tracker-de-dominios-externos-y-renovaciones]] | Tracker de cartera de dominios ajenos + descuentos por volumen | solid |
| [[2026-1024-internet-bs-soporte-24-7-con-95-de-respuesta-en-dos-horas]] | "95 % de peticiones en dos horas" (primera respuesta, no resolución) + 9 idiomas + 6 monedas | tentative |
| [[2026-1024-internet-bs-buscador-de-dominios-con-premiums-preorder-y-filtros-idn]] | Estados Available/Reserved/Preorder/Taken/Not supported, filtros de premium e IDN, catálogo de ccTLD y punycode | solid |
| [[2026-1024-precios-de-dominio-como-activo-y-gtld-2011-con-ronda-prevista-en-2026]] | Precios de salida (Porno.com $8.9M, Yun Ye 100.000 dominios por $164M, shop.com $3.5M, Freedom.com $2M, meet.me $450.000) y gTLDs 2011 / ronda prevista 2026 | tentative |

**Átomos extendidos:** ninguno. No se sobrescribió ninguna creencia previa.

## Fricción levantada (1)

- **Privacidad WHOIS universal vs. condicional por TLD.** El átomo de Internet.bs afirma "FREE private WHOIS for life **with all domain name registrations**"; el átomo de 1984 Hosting, de la **misma fecha de captura**, registra "privacidad whois **en los TLD que lo permiten**". La captura de Internet.bs no enumera los TLD donde el "FreeWHOIS" es aplicable, así que la universalidad no es verificable. Marcada con bloque `## [FRICTION]` en el átomo nuevo, apuntando al viejo, sin tocar el viejo.

## Lo que la captura NO contiene (y por qué los átomos son tentativos donde lo son)

- La tabla de resultados del buscador **no renderizó**: los tokens `tld`, `price` y `renewalPrice` aparecen sin resolver. **$6.99 es el único precio de dominio capturado.** El resto de la matriz de TLD es superficie, no dato.
- No se publica el **precio estándar de renovación** de un .COM, ni la duración del periodo promocional, ni el procedimiento de verificación de elegibilidad.
- Los precios de salida de dominios son **datos de terceros reproducidos por un registrador**, con "reportedly" y "around", sin documento de operación.
- "95 % en dos horas" es **primera respuesta**, no resolución; sin SLA ni créditos.
- El soporte no se declara subcontratado ni con horario por canal.

## Lectura para el humano

1. **El precio de dominio del vault pasa de un número a un eje.** Ya no hay un solo dato: hay precio de entrada ($6.99 primer año), precio cerrado recurrente de otro proveedor (€15/año en `njal.la`), precio de TLD barato (¥4.55/año en los .xyz de Spaceship), **tope por cliente**, **descuento por volumen** y **precio de renovación como producto a observar** (el tracker externo). Todo eso es una partida de coste que el back-office del vault todavía no tiene ([[2026-1022-costes-por-categoria-tenant]]).
2. **Internet.bs no compite en el tramo de ≤ €4/mes y no debe tener fila en la §1 de la tabla de precios.** Aporta la línea de dominio, no un servidor.
3. **El anti-abuso por fingerprinting (IP, dispositivos, medios de pago) es el reverso del KYC explícito de HOSTKEY.** Dos respuestas incompatibles al mismo problema de abuso, y la del registrador es más difícil de evadir.
4. **Un nombre barato y una marca fuerte son cosas distintas.** Los $1.640 por dominio de la cartera de Yun Ye y los TLD de baja fricción de los relays de VeriDrop son las dos caras del mismo hecho.

## Archivos

- Creados: 7 átomos en `2-atoms/` (prefijo `2026-1024`).
- Creado: `1-desk/thread-addition-internet-bs.md` (propuesta de thread, **aplicada el 2026-10-25**).
- Creado: `briefings/2026-10-24-refinery-internet-bs.md` (este briefing).
- Movido: `0-raw/2026-10-24-internet-bs-domains.md` → `0-raw/archive/2026-10-25-2026-10-24-internet-bs-domains.md`.
- No se tocó `sources/`, ni `3-threads/`, ni ningún átomo preexistente.

## Pendiente de otro agente

Aplicado el 2026-10-25: la sección **§8.14** y las fricciones **34–36** (numeración final) quedaron en `3-threads/escala-de-hosting-barato-y-el-limite-de-4-euros.md`, con la fuente añadida al frontmatter `sources:` del thread.
