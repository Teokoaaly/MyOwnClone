---
id: 2026-10-25-refinery-protonvpn
type: briefing
date: 2026-10-25
sources: [sources/2026-10-24-protonvpn-pricing.md]
---

# Briefing — Refinery: `2026-10-24-protonvpn-pricing.md`

**Captura procesada:** `0-raw/2026-10-24-protonvpn-pricing.md` → archivada en `0-raw/archive/2026-10-25-2026-10-24-protonvpn-pricing.md`.
**Fuente (ground truth):** `sources/2026-10-24-protonvpn-pricing.md` — `https://protonvpn.com/pricing`, 1584 palabras, capturada el 2026-10-24.

## Qué es esta captura

La página de precios de **Proton VPN**, con sus tres planes (Free, VPN Plus, Proton Unlimited), la tabla "Compare plans" y la FAQ. Es la **segunda captura del día sobre VPN** (la primera fue Mullvad) y llega con material nuevo: **un plan gratuito real**, **un bundle de ecosistema de siete productos** y **un mecanismo de precio con dos precios contractuales en la misma frase**.

## Átomos creados (14, todos en `2-atoms/`, prefijo `2026-1024-`)

| Átomo | Claim central |
|---|---|
| `2026-1024-protonvpn-plus-3-49-al-mes-65-de-descuento` | VPN Plus a $3,49/mes (65 % off sobre $9,99), $83,76 por 24 meses, "Save $156" |
| `2026-1024-protonvpn-el-descuento-caduza-y-la-renovacion-sube-a-6-99` | La renovación es $83,88/12 = **$6,99/mes** (30 % off, no 65 %); Unlimited renueva a $9,99/mes (23,1 % off) |
| `2026-1024-proton-unlimited-7-99-al-mes-bundle-de-7-productos` | $7,99/mes por siete productos (VPN, Pass, Mail, Calendar, Drive, Docs, Sheets) |
| `2026-1024-proton-unlimited-no-cambia-la-red-pero-cambia-todo-lo-otro` | Plus y Unlimited tienen red idéntica; los $4,50 de diferencia compran servicios anexos, no capacidad |
| `2026-1024-proton-plan-gratuito-1-dispositivo-y-10-paises-al-azar` | Free a $0: 1 dispositivo, velocidad media, 10 países sorteados, sin tarjeta |
| `2026-1024-proton-el-free-declara-sin-limites-ni-velocidad-artificial-y-la-tabla-lo-llama-velocidad-media` | Contradicción interna de la página; certainty `tentative`; lleva bloque `## [FRICTION]` contra el átomo de Mullvad |
| `2026-1024-protonvpn-diez-dispositivos-y-20000-servidores-en-140-paises` | 10 dispositivos simultáneos, 20.000+ servidores en 140+ países, "Highest speed" |
| `2026-1024-proton-limites-de-capacidad-por-plan-500-gb-15-correos-y-50-bovedas` | Drive 5→500 GB, Mail 1→15 buzones, Pass 2→50 bóvedas y alias ilimitados |
| `2026-1024-protonvpn-plus-incluye-planes-free-de-mail-drive-y-pass` | VPN Plus arrastra Mail Free, Drive Free, Pass Free y Calendar limitado |
| `2026-1024-proton-30-dias-de-dinero-devuelto-y-cambio-de-plan-con-credito-prorrateado` | 30 días de reembolso; cambio de plan prorrateado, pero el **downgrade destruye capacidad** (desactiva buzones y calendarios) |
| `2026-1024-proton-postura-de-privacidad-suiza-sin-registros-y-codigo-abierto` | Suiza, no-logs, 100 % open source, Kill Switch y secure streaming como *premium feature*, VPN Accelerator hasta 400 % |
| `2026-1024-proton-metodos-de-pago-tarjetas-paypal-y-creditos-comprables-con-bitcoin` | Pago directo solo fiat; **Bitcoin compra saldo, no el servicio** |
| `2026-1024-proton-captura-con-placeholders-xx-y-tabla-en-neerlandes` | Marcadores `$XX.XX` / `XX%` sin renderizar y tabla en neerlandés |
| `2026-1024-proton-ofrece-vpn-para-empresas-sin-precio-publicado` | Línea B2B sin precio, sin SLA y sin ficha en la captura |

## Átomos existentes ampliados (notas fechadas, sin sobrescribir nada)

- `2026-1024-mullvad-cripto-con-10-de-descuento` → nota **Proton**: tercera política cripto del sector (ExtraVM = mismo precio / Mullvad = −10 % / Proton = prepago de saldo).
- `2026-1024-mullvad-cinco-dispositivos-por-cuenta-y-sin-port-forwarding` → nota **Proton**: 5 dispositivos como tope de capacidad frente a 10 como prestación del plan.

## Hallazgos que merecen atención

1. **El "65 % off" es un precio de captación, no el coste.** La frase "Billed at $83.76 for the first 24 months, then renews at $83.88 every 12 months" da **$6,99/mes** en la renovación — el doble del titular, y un 30 % de descuento en lugar del 65 %. Cualquier coste plurianual del vault debe usar $6,99 (Plus) y $9,99 (Unlimited), no $3,49 ni $7,99.
2. **$3,49/mes es el precio de salida a Internet sin registro más bajo del vault**, por debajo de los €5 de Mullvad y de cualquier VPS documentado. Pero su unidad es el mes y el recurso es el dispositivo, no el GB ni la vCPU.
3. **El bundle vende servicios, no red.** Plus y Unlimited comparten servidores, velocidad, dispositivos, streaming y no-logs; los $4,50 de diferencia compran 500 GB, 15 buzones y 50 bóvedas. Es el caso más neto del vault de un precio que no compra infraestructura.
4. **Proton tiene plan gratuito y eso contradice la doctrina de Mullvad** ("free services nearly always come at some cost... by limiting the functionality"): aquí el peaje es el alcance —1 dispositivo y 10 países sorteados—, no la publicidad ni los datos. Fricción abierta, marcada, no auto-resuelta.
5. **El downgrade es destructivo.** Subir de plan es prorrateado; bajar obliga a desactivar buzones y calendarios o a reducir el almacenamiento. El prorrateo no es evidencia de reversibilidad.
6. **El cripto no compra el servicio**, solo saldo interno a precio nominal —tercer modelo cripto del vault, el más restrictivo.
7. **La captura está parcialmente renderizada**: el modal de upsell y la FAQ de descuentos muestran "$XX.XX" y "XX%", y la tabla comparativa aparece **traducida al neerlandés**. No se ha afirmado ninguna cifra que venga de esos huecos; en particular, **el supuesto "VPN a 1 $" del que habla la URL (`ref=free-plan-upsell-modal-1-usd`) no se ha afirmado**, porque la cifra no aparece.

## Thread

Propuesta escrita en `1-desk/thread-addition-protonvpn.md` (aplicada a `3-threads/` el 2026-10-25). Destino propuesto: `3-threads/economia-de-la-verificacion-y-reventa-de-cuentas.md`, nueva §8.8 "El VPN como partida ausente: precio plano frente a precio de captación" + una fricción en §9. La sección se plantea como **alternativa a la §8.7 de Mullvad** (mismo producto, mismo día, modelos de precio opuestos), no como sección acumulativa. El thread `escala-de-hosting-barato-y-el-limite-de-4-euros.md` queda fuera salvo una línea en su §10, porque esta captura **no aporta un proveedor de hosting**.

## Nota de método

- Una idea por átomo; 14 átomos para 1584 palabras. Los cálculos derivados (equivalencias de renovación, ratios, ahorro) van marcados como cálculo del átomo, no como dato de la fuente.
- Los precios en dólares se mantienen en su unidad original; no se han convertido a euros ni se les ha aplicado IVA o tipo de cambio. Nota: la página muestra un conmutador **CHF/EUR/USD** y la captura corresponde a la vista en USD.
- Nada se ha escrito en `sources/` ni se ha editado `0-raw/` (la captura solo se ha movido a `0-raw/archive/`).
- Verificación pendiente del humano: la captura **no** publica los precios de los planes de 1 mes y 1 año, ni los porcentajes de descuento que su propia FAQ promete (aparecen como "XX%"), ni precio/SLA de la línea de empresa, ni la política de no-logs, ni el texto de los términos de la garantía de 30 días.
- Se ha comprobado que ninguno de los archivos creados contiene caracteres fuera del repertorio latino (sin mojibake ni CJK/árabe residuales).
