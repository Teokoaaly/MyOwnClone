---
id: 2026-1023-priceai-transit-guia-previa-y-verificacion-de-modelo-pendiente
type: atom
certainty: solid
sources: [sources/2026-10-22-priceai-api-transit.md]
links: ["[[2026-1023-priceai-faq-antifraude-y-prueba-pequena]]", "[[2026-1023-priceai-transit-canal-tipo-sub2api-vs-new-api]]", "[[2026-1023-priceai-descargo-de-responsabilidad-sin-sla]]"]
---

## Claim
La página de tránsito tiene una sección **使用前说明** ("notas antes de usar") con tres preguntas que remiten a guías: **"使用前先看充值系数和综合倍率"**, **"模型真假怎么判断"** (cómo juzgar si un modelo es auténtico) y **"为什么要小额试用"** (por qué probar con un importe pequeño), más la advertencia **"价格榜只做购买前参考，充值前仍要回原站确认余额、退款和售后规则"** (la tabla solo sirve como referencia previa a la compra; antes de recargar hay que volver al canal original a confirmar saldo, reembolsos y reglas de postventa). La función **模型检测 (detección de modelos)** aparece dos veces marcada **"即将开放"** (próximamente disponible), junto con **检测**.

## Why It Matters
El vault tiene ahora la cadena completa de precauciones para comprar en un relay, y coincide con el protocolo antifraude que ya había registrado para el módulo 卡网 —pedido pequeño de prueba, volver al canal original, no quedarse en el precio más bajo ([[2026-1023-priceai-faq-antifraude-y-prueba-pequena]])— pero con dos añadidos específicos del relay: **el coeficiente de recarga** (que hay que mirar *antes* que el precio final) y **la autenticidad del modelo**, que es el riesgo propio de este mercado: un canal puede vender a precio bajo un modelo que no es el que dice ser.
El estado **"即将开放"** de 模型检测 es una verificación pendiente: hoy el agregador **no** puede confirmar qué modelo hay detrás de un multiplicador, solo monitorizar disponibilidad. Por tanto cualquier relay de 0.05x es, hoy, una caja negra declarada ([[2026-1023-priceai-descargo-de-responsabilidad-sin-sla]]).
Aplica también a la lectura del ranking: si el multiplicador se publica sin verificación de modelo y el 号池 es compartido, el precio del relay puede estar describiendo otra cosa ([[2026-1023-priceai-transit-canal-tipo-sub2api-vs-new-api]]).
