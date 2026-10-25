---
id: 2026-10-25-refinery-mullvad
type: briefing
date: 2026-10-25
sources: [sources/2026-10-24-mullvad-pricing.md]
---

# Briefing — Refinery: `2026-10-24-mullvad-pricing.md`

**Captura procesada:** `0-raw/2026-10-24-mullvad-pricing.md` → archivada en `0-raw/archive/2026-10-25-2026-10-24-mullvad-pricing.md`.
**Fuente (ground truth):** `sources/2026-10-24-mullvad-pricing.md` — `https://mullvad.net/en/pricing`, 411 palabras, capturada el 2026-10-24.

## Qué es esta captura

La página de precios de **Mullvad**, un proveedor de VPN. Es material nuevo para el vault en dos sentidos: **el producto no estaba en el corpus** (todo lo anterior era hosting, proxy, SMS o exchange) y **la unidad de precio es nueva**: un precio plano mensual, sin escala de consumo ni periodicidad Forcing.

## Átomos creados (9, todos en `2-atoms/`, prefijo `2026-1024-`)

| Átomo | Claim central |
|---|---|
| `2026-1024-mullvad-precio-plano-5-euros-iva-incluido-sin-cambio-desde-2009` | €5/mes IVA incluido, sin cambio desde 2009; equivalentes $5.60 / £4.19 / SEK 55.64 / A$7.97 / CA$7.84 |
| `2026-1024-mullvad-mismo-precio-para-1-mes-1-ano-o-1-decada` | 1 mes, 1 año y 1 década al mismo €/mes, por no lock-in |
| `2026-1024-mullvad-metodos-de-pago-incluyendo-efectivo-por-correo` | Doce vías: efectivo, BTC, BCH, XMR, wire, tarjeta, PayPal, Swish, EPS, Bancontact, iDEAL\|Wero, Przelewy24 |
| `2026-1024-mullvad-pago-en-efectivo-por-sobre-con-token-aleatorio` | Efectivo postal con token aleatorio y 9 monedas — el modo de pago más ciego a la identidad del vault |
| `2026-1024-mullvad-cripto-con-10-de-descuento` | Cripto con 10 % de descuento → €4,50/mes, con razón declarada |
| `2026-1024-mullvad-garantia-de-reembolso-14-dias-excepto-efectivo-por-aml` | 14 días de garantía; el efectivo es la única vía excluida (AML) |
| `2026-1024-mullvad-cinco-dispositivos-por-cuenta-y-sin-port-forwarding` | 5 dispositivos por cuenta; port forwarding retirado explícitamente |
| `2026-1024-mullvad-sin-plan-gratuito-ni-ventas-y-por-que` | Sin plan gratuito y sin rebajas, con el argumento declarado |
| `2026-1024-mullvad-modelo-sostenible-rechaza-el-euro-y-la-membresia-vitalicia` | "No €1/month rate or lifetime membership could ever support that" |

## Átomos existentes ampliados (notas fechadas, sin sobrescribir nada)

- `2026-1024-extravm-mismo-precio-que-tarjeta-sin-recargo-cripto` → nota **Mullvad**: tercera política de precio cripto del vault (ExtraVM = mismo precio / Mullvad = −10 % / HostBrr = conmutador EUR/USD).
- `2026-1024-extravm-pago-cripto-sin-kyc-ni-identidad` → nota **Mullvad**: el modo más anónimo del vault es el efectivo postal, y la exclusividad del reembolso se aplica en dirección opuesta a la de ExtraVM.

## Hallazgos que merecen atención

1. **El pago en efectivo postal es un escalón de minimización que no existe en ninguna otra captura.** Token generado aleatoriamente en el sitio, sobre por correo, nueve monedas. Ningún otro proveedor del vault documenta una forma de pago no digital.
2. **El reembolso funciona como palanca de trazabilidad en los dos extremos, en direcciones opuestas.** En ExtraVM/HostBrr la vía reembolsable es la identificable y el cripto es la ciega; en Mullvad la vía reembolsable es la identificable y el **efectivo** es la ciega (excluido por AML). Ninguno de los dos publica marco AML/CTF.
3. **Mullvad es la tercera política de precio cripto documentada** y la única con descuento explícito (−10 % por "lower fees and less administration"), lo que fija €4,50/mes como precio efectivo.
4. **El precio incluye IVA; ningún otro precio del thread lo hace** (Hetzner es *excl. VAT*). €4,50 con cripto queda **justo por encima del umbral de ≤ €4/mes** del vault — pero es una línea de red, no un VPS, y no debe entrar en la escalera de hosting.
5. **El argumento de sostenibilidad ("No €1/month rate... could ever support that") es la primera enunciación explícita de la relación entre precio y coste de servicio** por parte de un proveedor del corpus; es el contrapunto útil a los cupones LEB del 75–80 %.
6. **La captura no publica ni los países de los servidores ni los países a los que sirve.** Es un hueco material: la capa que manda en la verificación por SMS es la de jurisdicción, no la de red, y sin cobertura publicada el precio plano no se puede auditar contra ella. Queda como fricción abierta.

## Thread

Propuesta escrita en `1-desk/thread-addition-mullvad.md` (aplicada a `3-threads/` el 2026-10-25). Destino propuesto: `3-threads/economia-de-la-verificacion-y-reventa-de-cuentas.md`, nueva §8.7 "El VPN como partida ausente" + una fricción en §9. El otro thread candidato (`escala-de-hosting-barato-y-el-limite-de-4-euros.md`) queda fuera salvo una línea en su §10, porque esta captura **no aporta un proveedor de hosting**.

## Nota de método

- Una idea por átomo; 9 átomos para 411 palabras de FAQ, todas las ideas con contenido económico o de posture de identidad, sin duplicar la misma cifra en varios átomos salvo cuando el ángulo es distinto (precio vs. periodicidad vs. descuento).
- Nada se ha escrito en `sources/` ni en `0-raw/` (la captura solo se ha movido a `0-raw/archive/`).
- Verificación pendiente de hacer por el humano: la página **no** publica SLA, número de servidores, cobertura geográfica, política de registro ni términos de servicio. El "no logging" que se le suele atribuir a Mullvad **no aparece en esta captura** y por tanto no se ha afirmado en ningún átomo.
