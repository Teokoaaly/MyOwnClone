---
id: 2026-10-26-refinery-ivpn
type: briefing
date: 2026-10-26
sources: [sources/2026-10-25-ivpn-pricing.md]
---

# Briefing — Refinery: captura IVPN pricing

**Qué se procesó:** `0-raw/2026-10-25-ivpn-pricing.md` → **12 átomos nuevos** (todos con prefijo `2026-1026-ivpn-*`) + **0 átomos existentes modificados** + **6 extensiones propuestas** en `1-desk/extend-ivpn-pricing.md` + **1 propuesta de thread** en `1-desk/thread-prop-ivpn-pricing.md` + este briefing. La captura se ha movido a `0-raw/archive/2026-10-26-2026-10-25-ivpn-pricing.md`.

**Fuente de verdad:** `sources/2026-10-25-ivpn-pricing.md` — página de precios de `ivpn.net/en/pricing/`, 415 palabras, 177 líneas. Es la **tercera página de checkout de proveedor** de VPN del corpus, después de Mullvad (`2026-10-24-mullvad-pricing.md`) y Proton VPN (`2026-10-24-protonvpn-pricing.md`).

## El hallazgo principal

**IVPN introduce un tercer modelo de precio, y es el primero en el que la periodicidad es la variable de precio con descuento explícito.** Nueve precios en USD, tres niveles × tres periodicidades: Standard $2/$6/$60, Plus $3/$8/$80, Pro Suite $4/$10/$100 (semana/mes/año). **El año vale exactamente diez meses** en los tres niveles: 16,7 % menos que doce meses sueltos. Y la semana cuesta **$8,67/mes equivalente** frente a $6 del mes y $5 del año. El orden de compromiso es inverso al de precio.

Esto rompe la generalización que el thread arrastraba desde Mullvad: «el precio del VPN es plano, la duración del pago es una variable libre». En el corpus hay ahora **tres modelos incompatibles**: precio invariante (Mullvad), precio de captación con renovación al doble (Proton) y precio por compromiso temporal (IVPN).

## Las cifras transcritas

| Dato | Cifra | Tipo |
|---|---|---|
| Standard / Plus / Pro Suite (1 mes) | **$6 / $8 / $10** | precio de lista |
| Standard / Plus / Pro Suite (1 año) | **$60 / $80 / $100** | precio de lista |
| Standard / Plus / Pro Suite (1 semana) | **$2 / $3 / $4** | precio de lista |
| Dispositivos | **5** (Standard, Plus) / **10** (Pro Suite) | límite por plan |
| Cobertura | **58 ubicaciones / 41 países** | claim |
| Auditorías | **anuales desde 2019**, warrant canary, informes de transparencia | claim |
| Alta | **sin email**, **30 días de reembolso** | condición |
| Pagos | Credit Card, PayPal, Bitcoin, **BTC Lightning**, Monero, **Cash** | método |
| Servicios | **4 standalone**, todos open source, **Unlinked Access** (sin account ID) | claim |
| Equipo | «Team licensing for **VPN-only** plans», **sin precio** | ausencia |

**Ausencias que impiden cotizar la línea completa:** no se declara **IVA** (solo «Pricing in USD»), no hay política de renovación, no hay lista de los 41 países, no se enlaza ni una sola auditoría ni se nombra al auditor, no se documenta el mecanismo del efectivo, y **la página de precios de equipo (`/en/pricing-teams/`) y la de servicios (`/en/services/`) no están capturadas**.

## Los cuatro aportes al vault

1. **«No email required for signup»** — el identificador de la cuenta del VPN no nace como dirección de correo. Es la primera vez que el corpus documenta esa separación, y reduce en una capa el vector de correlación entre servicio de salida y cuenta de correo del producto.
2. **Unlinked Access** — «Additional services authorise access without receiving your IVPN account ID». Es la primera vez que el corpus documenta **desacoplamiento de identidad entre servicios del mismo proveedor**, y lo hace verificable en la página, no deducido de un slogan de posture como el «open source» de Proton.
3. **Mailx ($8/mes)** — primer producto de alias de correo con precio del corpus. **Portmaster Pro ($10/mes)** — primer firewall de red vendido por un proveedor de VPN y no por un host (Hetzner lo daba como función de la plataforma cloud sin coste adicional).
4. **«Router and NAS deployment support»** con cliente Linux/CLI — abre la opción de alojar la salida en el propio VPS del producto, con IP fija y geolocalizada a elección. Es la variable que el proxy por gigabyte no resolvía a coste estable, y a la vez el patrón que HeroSMS declara que dispara el bloqueo.

## Fricciones levantadas (7 en átomos, 4 propuestas al thread)

**En los átomos (7):**
- Precio por compromiso vs. precio plano (Mullvad).
- Límite de dispositivos por plan y precio marginal no plano (Proton, atomizado).
- 30 días de reembolso **sin exclusión de efectivo** vs. patrón de Mullvad (irreembolsable por AML).
- Auditoría de producto y canary vs. certificación de sistema de gestión (Hetzner) — dos ejes de cumplimiento, no uno.
- Cobertura de 41 países sin lista enumerada vs. enumeración de NoOnes.
- Aviso en ruso de no garantía de conexión (único aviso de fiabilidad de proveedor del corpus).
- Línea de equipo sin precio: la ausencia ya no es un caso único sino un rasgo del sector.

**Propuestas al thread `economia-de-la-verificacion-y-reventa-de-cuentas` (fricciones 39–42):** periodicidad como palanca de precio; el dispositivo como unidad de capacidad no escala de forma plana; «lo más anónimo es lo irremeable» es idiosincrasia de Mullvad, no del sector; y la línea de empresa sin precio deja de ser caso único. Se propone una **§8.11** nueva y una nota de método (séptima tanda) en `1-desk/thread-prop-ivpn-pricing.md` — **no aplicada**, por el turno de «no editar 3-threads/».

## Ficheros

**Átomos nuevos en `2-atoms/`** (prefijo `2026-1026-ivpn-*`, todos con `sources: [sources/2026-10-25-ivpn-pricing.md]` y ≥2 wikilinks):
- `2026-1026-ivpn-nueve-precios-en-tres-niveles-y-tres-periodicidades.md`
- `2026-1026-ivpn-cinco-dispositivos-en-standard-y-plus-diez-en-pro-suite.md`
- `2026-1026-ivpn-plus-y-pro-suite-anaden-moddns-mailx-y-portmaster-pro.md`
- `2026-1026-ivpn-alta-sin-email-y-30-dias-de-reembolso.md`
- `2026-1026-ivpn-efectivo-monero-bitcoin-y-lightning-sin-descuento-declarado.md`
- `2026-1026-ivpn-cuatro-servicios-standalone-open-source-activados-por-separado.md`
- `2026-1026-ivpn-auditorias-anuales-desde-2019-y-canary-de-ordenes.md`
- `2026-1026-ivpn-58-ubicaciones-en-41-paises-sin-port-forwarding-ni-streaming.md`
- `2026-1026-ivpn-avisa-en-russo-que-no-garantiza-conexion-y-recomienda-el-plan-semanal.md`
- `2026-1026-ivpn-wireguard-resistente-a-cuantico-y-clientes-abiertos-en-cinco-plataformas.md`
- `2026-1026-ivpn-despliegue-en-router-y-nas-para-salida-propia.md`
- `2026-1026-ivpn-licencias-de-equipo-para-planes-vpn-sin-precio-publicado.md`

**Extensiones propuestas** (`1-desk/extend-ivpn-pricing.md`, ningún fichero de `2-atoms/` modificado):
`2026-1024-mullvad-cinco-dispositivos-por-cuenta-y-sin-port-forwarding` · `2026-1024-mullvad-metodos-de-pago-incluyendo-efectivo-por-correo` · `2026-1024-mullvad-garantia-de-reembolso-14-dias-excepto-efectivo-por-aml` · `2026-1024-mullvad-cripto-con-10-de-descuento` · `2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001` · `2026-1024-proton-ofrece-vpn-para-empresas-sin-precio-publicado`

**Propuesta de thread (NO aplicada):** `1-desk/thread-prop-ivpn-pricing.md` → `THREAD: economia-de-la-verificacion-y-reventa-de-cuentas`.

**Captura movida:** `0-raw/2026-10-25-ivpn-pricing.md` → `0-raw/archive/2026-10-26-2026-10-25-ivpn-pricing.md`.
