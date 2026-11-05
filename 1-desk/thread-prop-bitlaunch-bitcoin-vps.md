# Propuesta de hilo — captura `2026-10-25-bitlaunch-bitcoin-vps.md`

Fuente: `sources/2026-10-25-bitlaunch-bitcoin-vps.md` (`https://bitlaunch.io/bitcoin-vps`, capturada 2026-10-25, 823 palabras).
Átomos nuevos de esta captura: 8 (todos en `2-atoms/`, prefijo `2026-1026-`).
Átomos extendidos de esta captura: 5.

---

## Propuesta A — `escala-de-hosting-barato-y-el-limite-de-4-euros`

```markdown
### Una fila más en la tabla de postura de identidad: BitLaunch declara email, contraseña y ni una cookie

La captura de `https://bitlaunch.io/bitcoin-vps` (2026-10-25) añade a este thread **el primer proveedor del corpus que publica una declaración de recolección de datos en su propia página de producto**. La sección "Keep your privacy" dice literalmente: **"We ask for just an email and password when you sign up and don't run trackers or store cookies across our site"**, y añade que **"you can completely destroy your VPS and account data at any point to have it with permanently removed"** ([[2026-1026-bitlaunch-alta-con-email-y-password-sin-trackers-ni-cookies]], [[2026-1026-bitlaunch-destruccion-definitiva-de-vps-y-datos-de-cuenta]]).

La fila que esto propone para la tabla de la §6 es:

| Proveedor | Postura declarada | Detalle |
|---|---|---|
| **BitLaunch** | **email + contraseña, sin trackers ni cookies** — y silencio sobre KYC | "We ask for just an email and password"; "don't run trackers or store cookies"; destrucción total de VPS y datos de cuenta a demanda. **No declara** KYC, verificación, retención, logs, entidad legal ni domicilio |

Lo que cambia en la lectura de la §6 es la **distinción entre silencio y postura declarada**, que hasta ahora el thread trataba como la misma categoría. La tabla listaba a 1984 Hosting como "silencio" y a ExtraVM, Skhron, Anubiz y Evoxt como declaraciones; BitLaunch es un caso intermedio que no cabía: **declara una recolección mínima (lo que pide y lo que no guarda en el navegador) y calla sobre lo que retiene** ([[2026-1026-bitlaunch-sin-tabla-de-precios-ni-specs-ni-sla]]). La conclusión de la §6 se refuerza y se delimita al mismo tiempo: **pagar en cripto no es una postura de privacidad, es un modo de liquidación** — y la postura del proveedor, cuando existe, no dice nada de la del titular de la moneda.

Y aquí está el dato que más aprieta esa conclusión, porque es del propio proveedor: la **FAQ del producto recomienda cinco vías para comprar Bitcoin** — **PayPal, Coinbase, un cajero automático de Bitcoin, un exchange (Binance) y el trueque con amigos y familia** ([[2026-1026-bitlaunch-faq-recomienda-vias-de-compra-de-bitcoin-con-kyc]]). Tres de las cinco son on-ramps con KYC obligatorio. Es decir: el proveedor que vende "anonymous VPS" y "no restrictions" **enlaza desde su propia web a Coinbase y Binance**, y el anonimato se rompe aguas arriba, en el exchange, no en el checkout del hosting.

Dos lecturas más que este thread necesita de esta captura:

**La primera, sobre la superficie operativa de la §8: la única puerta de entrada al producto es una persona.** La prueba gratuita no es un botón: es **"signing up for a BitLaunch account and talking to our support team. They'll credit your account with enough balance for a few hours of functioning"** ([[2026-1026-bitlaunch-prueba-gratuita-con-saldo-tras-hablar-con-soporte]]). El abono es **saldo**, la unidad es **horas de funcionamiento**, y no hay specs ni condiciones publicadas. Frente a ExtraVM (despliegue en 15-30 min tras confirmación), Evoxt (2,5 min) y HostBrr (garantía de devolución de 30 y 7 días), BitLaunch es el único del corpus cuya prueba gratuita **no es programable**: un smoke test del stack no se puede automatizar contra un proveedor cuya única puerta es un chat.

**La segunda, sobre la §1 y la §4: la página de producto tampoco cotiza.** Ni tarifa por hora, ni specs, ni SLA, ni stock — solo el rótulo "pay hourly" y el claim de stack **"We only use SSD drives and KVM technology"** ([[2026-1026-bitlaunch-solo-ssd-y-kvm-en-todos-los-servicios]]), que no son specs porque no dicen CPU, RAM, disco ni IOPS. El argumento que esta captura sí sostiene es de **superficie, no de precio**: el catálogo de apps de un clic publica WireGuard, OpenVPN y Shadowsocks R **"without the need to worry about config files or pre-requisites"** y WordPress o LAMP/LEMP **"without running a single command"** ([[2026-1026-bitlaunch-apps-un-clic-de-privacidad-y-amplio-catalogo-de-productos]]), más una línea de VPN propia multi-región y multi-salto ([[2026-1026-bitlaunch-vpn-wireguard-multiregion-y-multihop-como-producto]]). Es el proveedor que mejor documenta el **plano de control** y el que menos permite cotizarlo: el mismo patrón que ya dejó registrado la home ([[2026-1026-bitlaunch-facturacion-por-hora-y-pago-cripto-propio]]).

Y un aviso de método, porque la FAQ de esta página contiene una entrada titulada "What is the difference between Bitcoin and Ethereum?" que afirma que **"Ethereum plans to switch to Proof of Stake (PoS) in 2022"** — cuatro años antes de la captura, en una página capturada en 2026 ([[2026-1026-bitlaunch-faq-contenido-seo-desactualizado-sobre-ethereum]]). Cuando el contenido evergreen de una página oficial de proveedor está desactualizado, **sus claims de producto ("instant setup", "zero confirmation payments") deben tratarse como claims y no como hechos verificados**, que es la distinción que este thread ya usa entre medición y claim.
```

THREAD: escala-de-hosting-barato-y-el-limite-de-4-euros

---

## Propuesta B — `economia-de-la-verificacion-y-reventa-de-cuentas`

```markdown
### El coste del alta cripto: la espera de confirmación que el corpus no había medido

La captura de `https://bitlaunch.io/bitcoin-vps` (2026-10-25) documenta el extremo más rápido —y más difícil de alcanzar— del coste del alta en cripto: **"BitLaunch's in-house payment system eliminates middle-men and fees while enabling zero confirmation payments"** ([[2026-1026-bitlaunch-pagos-cripto-con-cero-confirmacion]]).

La §7 de este thread ordena el coste del alta por insumos —correo, captcha, proxy, identidad— y hasta ahora el cripto no tenía una partida propia porque ExtraVM y HOSTKEY lo trataban como un factor de **tiempo**, no de dinero: ExtraVM despliega en **15-30 minutos** tras 1-3 confirmaciones y HOSTKEY reconoce que "cryptocurrency payments require blockchain confirmation, so processing may take some time" ([[2026-1024-extravm-despliegue-tras-confirmacion-en-15-30-minutos]], [[2026-1024-hostkey-pago-cripto-pendiente-hasta-confirmacion-de-blockchain]]). Con BitLaunch aparece la hipótesis contraria: **la latencia de confirmación puede ser un parámetro del proveedor y no una propiedad del medio de pago**. Si "zero confirmation" es real, es la primera vía de pago cripto del vault sin espera, y una compra programada por script deja de depender de un polling de estado.

Marcado para juicio humano, no auto-resuelto: la captura **no publica** ventana de confirmación, número de confirmaciones, política de reemisión ni mecanismo de liquidación, así que "zero confirmation" es un claim sin cifra — y la página que lo contiene también afirma que "Ethereum plans to switch to Proof of Stake (PoS) in 2022" ([[2026-1026-bitlaunch-faq-contenido-seo-desactualizado-sobre-ethereum]]). O la latencia es eliminable y el corpus de ExtraVM/HOSTKEY mide una decisión de diseño, o "zero confirmation" es marketing.

La segunda corrección de esta captura es de **geografía del KYC**, y es la que más pesa para un producto que opera español-primero desde España ([[2026-1022-i18n-es-first-jurisdiccion-es]]). BitLaunch promete que **"Cryptocurrency removes borders and allows you to buy a Bitcoin VPS from anywhere in the world with no restrictions"** ([[2026-1026-bitlaunch-compra-desde-cualquier-pais-sin-restricciones]]), mientras NoOnes no da de alta a residentes de los 30 países de MiCA —**España entre ellos**— desde el 1 de julio de 2026, y devuelve además un muro literal por IP ([[2026-1024-noones-mica-30-paises-no-servidos-desde-julio-2026]], [[2026-1024-noones-jurisdicciones-globalmente-restringidas]]). Las dos cosas son ciertas y la contradicción es de método: **la lista de jurisdicciones globalmente restringidas no es global, es el filtro de un proveedor**, y un proveedor cuyo argumento de venta es "sin restricciones" no es necesariamente más abierto — puede ser simplemente **el que no publica dónde no opera**. Su Terms y su Acceptable Use están enlazados en el pie y no reproducidos en la captura.

Y la tercera, la que cierra el círculo con la §7: **la identidad del cliente se decide antes que el pago, en el exchange**. La propia FAQ del producto recomienda comprar Bitcoin en **PayPal, Coinbase, un ATM o Binance** ([[2026-1026-bitlaunch-faq-recomienda-vias-de-compra-de-bitcoin-con-kyc]]). **PayPal, Coinbase y Binance** son vías con KYC obligatorio —y el cajero automático lo exige en la mayoría de países—, y el exchange es además el punto donde el vault ya identificó que el KYC se convierte en capacidad ([[2026-1024-hostkey-kyc-obligatorio-y-procesamiento-via-bitpay]]). La regla operativa que este thread está construyendo se afina así: **la minimización de datos del lado del proveedor no se propaga aguas arriba**; un hosting que pide un email y ni una cookie sigue dejando la identidad en el exchange, y ese es el coste de alta que un producto español-primero no puede meter en el budget del VPS.
```

THREAD: economia-de-la-verificacion-y-reventa-de-cuentas

---

## Nota para el editor

- No se ha modificado ningún fichero en `3-threads/`.
- Las dos propuestas son texto para insertar en los hilos indicados; los `THREAD:` de arriba identifican a cuál corresponde cada bloque.
- Átomos nuevos: `2026-1026-bitlaunch-alta-con-email-y-password-sin-trackers-ni-cookies`, `2026-1026-bitlaunch-pagos-cripto-con-cero-confirmacion`, `2026-1026-bitlaunch-compra-desde-cualquier-pais-sin-restricciones`, `2026-1026-bitlaunch-solo-ssd-y-kvm-en-todos-los-servicios`, `2026-1026-bitlaunch-prueba-gratuita-con-saldo-tras-hablar-con-soporte`, `2026-1026-bitlaunch-destruccion-definitiva-de-vps-y-datos-de-cuenta`, `2026-1026-bitlaunch-faq-recomienda-vias-de-compra-de-bitcoin-con-kyc`, `2026-1026-bitlaunch-faq-contenido-seo-desactualizado-sobre-ethereum`.
- Átomos extendidos (nota fechada `## Nota de extensión 2026-10-26`): `2026-1026-bitlaunch-linux-o-windows-con-ubuntu-desktop-y-windows-rdp`, `2026-1026-bitlaunch-apps-un-clic-de-privacidad-y-amplio-catalogo-de-productos`, `2026-1026-bitlaunch-facturacion-por-hora-y-pago-cripto-propio`, `2026-1026-bitlaunch-sin-tabla-de-precios-ni-specs-ni-sla`, `2026-1024-1984-hosting-acepta-bitcoin-y-monero`.
- Fricciones planteadas (5 pares): `2026-1024-1984-hosting-acepta-bitcoin-y-monero` ↔ `2026-1026-bitlaunch-alta-con-email-y-password-sin-trackers-ni-cookies`; `2026-1024-extravm-despliegue-tras-confirmacion-en-15-30-minutos` ↔ `2026-1026-bitlaunch-pagos-cripto-con-cero-confirmacion`; `2026-1024-noones-jurisdicciones-globalmente-restringidas` ↔ `2026-1026-bitlaunch-compra-desde-cualquier-pais-sin-restricciones`; `2026-1024-extravm-registro-contable-sin-vinculo-a-wallets` ↔ `2026-1026-bitlaunch-destruccion-definitiva-de-vps-y-datos-de-cuenta`; `2026-1024-hostkey-kyc-obligatorio-y-procesamiento-via-bitpay` ↔ `2026-1026-bitlaunch-faq-recomienda-vias-de-compra-de-bitcoin-con-kyc`.