---
id: 2026-10-25-refinery-njalla
type: briefing
date: 2026-10-25
sources: [sources/2026-10-24-njal-la-domains-vpn.md, sources/2026-10-24-njalla-com-corporate.md]
---

# Briefing — Refinery: capturas Njalla (njal.la y njalla.com)

**Qué se procesó:** `0-raw/2026-10-24-njal-la-domains-vpn.md` y `0-raw/2026-10-24-njalla-com-corporate.md` → **11 átomos nuevos** (8 de `njal.la`, 3 de `njalla.com`) + **1 extensión de átomo existente** + **1 propuesta de thread** + este briefing. Las dos capturas se han movido a `0-raw/archive/2026-10-25-2026-10-24-njal-la-domains-vpn.md` y `0-raw/archive/2026-10-25-2026-10-24-njalla-com-corporate.md`.

**Advertencia de nomenclatura:** son **dos entidades distintas con nombre parecido** y así se han atomizado, sin fusionar en ningún momento:
- **`njal.la`** — el servicio de "Privacy as a Service" (dominios, VPN, servidores).
- **`njalla.com`** — la web corporativa de **NJALLA AB**, empresa familiar sueca de consultoría. **No es el servicio.**

## El hallazgo principal

**`njalla.com` ya no es el proveedor de dominios.** La home es la de "Anita Lassinantti Bloms och Anders Bloms familjebolag", una empresa familiar dedicada a asesorar en el cambio de estructuras de trabajo. La captura (208 palabras) **no contiene ningún producto, precio, plan, SLA ni mención a dominios, VPN o servidores** — cinco frases en sueco, un logo de 2021 y el bloque de reCAPTCHA. El plan maestro `research/MASTER-DEFINITIVO-2026-07.md` §3 apunta a `njalla.com` ("XMR, ellos son el dueño legal"): **esa URL está desactualizada**; el servicio real está en `njal.la`.

## Lo que sí se ha transcrito de `njal.la`

| Dato | Cifra / texto | Tipo |
|---|---|---|
| Registro de dominios | **desde €15/año** (única cifra de la página) | precio real |
| Modelo de precio | un precio por TLD, **sin paquetes, sin escalones, sin multi-año** | política |
| Incluido en todo registro | **privacidad whois, DNS anycast, soporte, reenvío de correo** | claim |
| VPN | **Wireguard + OpenVPN**, túnel cifrado, IP real oculta, **"15+ years"** | claim |
| Servidores | VMs con "many Linux distributions" + físicos bajo encargo; **backend de almacenamiento distribuido** | claim |
| Casos de uso | mastodon, matrix, nextcloud, "protest blog" | positioning |
| Pagos | **BTC, LTC, XMR, ETH + PayPal** | método |
| Posicionamiento | "Privacy as a Service", "make privacy extremely normalised"; prueba de stress **judicial** ("go to court to protect them") | positioning |

**Ausencias que hacen la fuente no cotizable:** sin precio de VPN, sin precio de servidores, sin specs, sin SLA, sin ubicaciones, sin egreso, sin política de reembolso, sin dato de identidad en el checkout. `njal.la` **no tiene fila** en la tabla de precios del thread de hosting.

## Los tres hallazgos que aportan al vault

1. **La primera cifra de registro de dominio con privacidad whois y DNS anycast incluidos:** €15/año con todo incluido. Con 1,25 €/mes, **el dominio es una partida fija que no escala con los tenants** — un cliente más no añade dominios — y consume un 31 % del techo de ≤ €4/mes. El bundle comparable en 1984 Hosting (DNS anycast gratis) **no publica tarifa de registro**: la comparación absoluta no puede cerrarse, pero por primera vez hay un **precio cerrado** para "dominio con privacidad y DNS anycast".

2. **La VPN con la trayectoria más larga declarada del vault (15+ años)** y la primera fuente que documenta **Wireguard junto a OpenVPN**. Los servidores aportan **redundancia de plataforma** (backend distribuido), no backup bajo demanda — un tipo de garantía de continuidad que el thread no tenía.

3. **La criptografía aceptada no es prueba de anonimato.** Se acepta Monero, pero la captura **no dice si el alta o el cobro exige identificación**. Aplicando la regla del thread, "pagar en XMR" es un modo de liquidación, no una postura de privacidad verificada.

## Fricciones levantadas (4, para juicio humano)

- **URL desactualizada en el plan maestro:** o `njalla.com` está mal anotado, o "ellos son el dueño legal" es un rasgo histórico. La captura de `njal.la` **no declara quién figura como titular registral**, así que tampoco se puede confirmar desde el servicio.
- **XMR ≠ registro anónimo:** sin dato de identidad en el checkout, no se puede afirmar que el registro sea anónimo.
- **Las dos matrices TLD-a-TLD faltan** (en `njal.la` y en 1984): no se puede comparar "bundle con precio" contra "bundle sin precio".
- **`njal.la` no es cotizable y aun así es el único dato de registro con precio del vault:** una sola cifra para tres productos, con las tres subpáginas sin capturar.

## Ficheros

**Átomos nuevos en `2-atoms/`** (prefijo `2026-1024`):

*De `njal.la` (el servicio):*
- `2026-1024-njal-la-registro-de-dominios-desde-15-euros-con-todas-las-funciones-incluidas.md`
- `2026-1024-njal-la-precios-unicos-por-tld-sin-paquetes-ni-scalones.md`
- `2026-1024-njal-la-privacidad-whois-y-dns-anycast-incluidos-en-el-registro.md`
- `2026-1024-njal-la-vpn-wireguard-y-openvpn-con-tunel-cifrado-y-15-anos-de-experiencia.md`
- `2026-1024-njal-la-servidores-con-almacenamiento-distribuido-y-redundante-para-autohospedar.md`
- `2026-1024-njal-la-cripto-y-paypal-como-metodos-de-pago-aceptados.md`
- `2026-1024-njal-la-privacy-as-a-service-y-la-normalizacion-como-posicionamiento.md`
- `2026-1024-njal-la-precios-no-publicados-para-vpn-y-servidores.md`

*De `njalla.com` (la corporativa, sin producto):*
- `2026-1024-njalla-com-es-la-web-corporativa-de-njalla-ab-y-no-el-servicio-de-dominios.md` *(certainty: solid; incluye bloque `## [FRICTION]` contra `research/MASTER-DEFINITIVO-2026-07.md`)*
- `2026-1024-njalla-ab-empresa-familiar-de-consultoria-entre-norrland-y-lo-internacional.md` *(certainty: tentative)*
- `2026-1024-njalla-com-captura-corporativa-sin-productos-ni-precios-ni-servicios.md`

**Átomo existente extendido** (nota fechada al final, sin sobrescribir ninguna afirmación previa):
- `2-atoms/2026-1024-1984-hosting-freedns-anycast-gratuito-y-registro-de-dominios.md` → nota fechada "2026-10-24 (captura njal.la)" que aporta el contrapunto de precio (€15/año con bundle incluido) sin tocar el claim original.

**Propuesta de thread (NO aplicada a `3-threads/` por paralelismo):**
- `1-desk/thread-addition-njalla.md` → nueva §8.12 "El caso de una marca partida: `njal.la` sirve, `njalla.com` no" + fricciones 27–30 propuestas + nota de método, para pegar en `3-threads/escala-de-hosting-barato-y-el-limite-de-4-euros.md`.

**Capturas movidas:**
- `0-raw/2026-10-24-njalla-com-corporate.md` → `0-raw/archive/2026-10-25-2026-10-24-njalla-com-corporate.md`
- `0-raw/2026-10-24-njal-la-domains-vpn.md` → `0-raw/archive/2026-10-25-2026-10-24-njal-la-domains-vpn.md`

**Briefing:** este archivo, `briefings/2026-10-24-refinery-njalla.md`.
