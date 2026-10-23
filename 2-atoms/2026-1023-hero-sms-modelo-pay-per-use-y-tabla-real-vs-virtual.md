---
id: 2026-1023-hero-sms-modelo-pay-per-use-y-tabla-real-vs-virtual
type: atom
certainty: solid
sources: [sources/2026-10-22-hero-sms-home.md]
links: ["[[2026-1023-hero-sms-reembolso-si-no-llega-sms-en-20-minutos]]", "[[2026-1023-5sim-reembolso-instantaneo-si-no-llega-sms]]", "[[2026-1023-hero-sms-flujo-de-cinco-pasos-para-verificar-chatgpt]]"]
---

## Claim
La home de HeroSMS explicita el **modelo de compra por uso** con una tabla comparativa de siete filas entre número real y número virtual ("How is a virtual number different from a real phone number?"): **SIM requerido** (Yes / No), **atado al dispositivo** ("Tied to device", Yes / No), **período de uso** (Long-term / Temporary, **from 20 min**), **anónimo** (No / Yes), **cobertura geográfica** (1 país / **180+ países**), **coste** (Carrier contract / **Pay per use**) y **propósito principal** (Regular communication / One-time verification). Encima, el flujo documentado en cinco pasos: registrarse → **recargar saldo** ("Top up your balance") → elegir servicio y país ("If you don't see your service, choose 'Any Other'") → **comprar el número** → **recibir el código en la cuenta personal** ("Receive the code directly in your personal account"). Y dos condiciones de acceso explícitas: **"Codes are exclusively available to buyers: registration is secure and anonymous"** y la nota "If the desired service is not in the list, then choose 'Any other'".

## Why It Matters
Fija el contrato económico del canal: **prepagado sobre saldo, pago por uso, sin suscripción y sin permanencia**, exactamente el mismo esquema que 5sim ([[2026-1023-5sim-reembolso-instantaneo-si-no-llega-sms]]). La diferencia que la tabla de HeroSMS añade es la comparación explícita con la SIM real, que convierte "pago por uso" en la contrapartida directa de "contrato con operador" — el mismo eje de comparación que usa el vault al distinguir coste absorbido por plataforma de coste por uso en [[2026-1022-costes-por-categoria-tenant]].
Y el punto operativo que más afecta a un pipeline: **"Codes are exclusively available to buyers"** significa que el código no existe hasta que se paga, con lo que el flujo no admite un modo de prueba gratuito del canal SMS (a diferencia del bypass sin registro que sí ofrece 5sim en su catálogo público). El mecanismo de devolución de dinero va en [[2026-1023-hero-sms-reembolso-si-no-llega-sms-en-20-minutos]]; la variante específica del servicio ChatGPT, en [[2026-1023-hero-sms-flujo-de-cinco-pasos-para-verificar-chatgpt]].

## Nota de verificación
La tabla de siete filas y las cinco condiciones del flujo están transcritas literalmente de la captura. La captura **no** publica: importe mínimo de recarga, comisión por recarga, umbral de pedido mínimo ni plan de descuentos (ese dato sí aparece en la landing de ChatGPT, no en la home).
