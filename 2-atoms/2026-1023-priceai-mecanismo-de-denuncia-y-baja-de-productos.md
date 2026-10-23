---
id: 2026-1023-priceai-mecanismo-de-denuncia-y-baja-de-productos
type: atom
certainty: solid
sources: [sources/2026-10-22-priceai-home.md]
links: ["[[2026-1023-priceai-faq-antifraude-y-prueba-pequena]]", "[[2026-1023-priceai-limite-de-verificacion-y-responsabilidad]]", "[[2026-1023-lzt-superficie-de-avisos-faq-y-tickets]]"]
---

## Claim
PriceAI no solo publica precios: tiene un **procedimiento de baja** con tres escalones y un control de calidad sobre su propio catálogo. La cadena de escalado documentada es: primero **contactar con la postventa de la tienda**; si la postventa no responde, **quejarse en la plataforma 卡网 correspondiente**; y solo después **volver a PriceAI, pulsar el botón 举报 (denunciar) a la derecha del producto,補充 evidencia, y esperar la revisión**: *"审核通过后会下架异常商品或渠道"* — si la revisión se aprueba, se **bajan del catálogo el producto anómalo o el canal entero**. La FAQ lo justifica con el límite de responsabilidad: al no participar en la transacción, PriceAI no resuelve disputes, pero sí modera su propio índice.

## Why It Matters
Convierte al agregador en un **tercer nivel de disputas**, por encima del vendedor y del marketplace. Es la diferencia entre un índice estático y una superficie con estados de moderation: la baja existe, y una entrada retirada es un hecho auditable.
La consecuencia para el vault es un **proceso de calidad de proveedor de terceros**, que es lo que hace falta cuando el coste de inferencia del producto depende de canales externos sin SLA ([[2026-1023-priceai-descargo-de-responsabilidad-sin-sla]]). El caso de uso directo: si el producto comprara una cuenta de IA de reventa ([[2026-1023-lzt-categoria-llm-accounts-para-reventa]]) y esa cuenta se revoca o es un fraude, el recurso es exactamente esta secuencia de tres pasos.
Y hay un matiz de diseño interesante: la evidencia la aporta **quien compró**, no el agregador. El botón de denuncia vive junto al producto y el proceso de baja lo decide PriceAI con la evidencia del comprador — un mecanismo de crowd-moderation ligero que no necesita aparecer en el ticket del marketplace ([[2026-1023-lzt-superficie-de-avisos-faq-y-tickets]]).

## Nota de verificación
La captura **no** publica: el plazo de revisión, el ratio real de aprobaciones, ni si los Retiree de canal son permanentes o provisionales.
