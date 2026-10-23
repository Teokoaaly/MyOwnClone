---
id: 2026-1023-priceai-channels-53-productos-y-minimo-con-stock
type: atom
certainty: solid
sources: [sources/2026-10-22-priceai-channels.md]
links: ["[[2026-1023-priceai-modulo-kanet-marcas-y-modos-de-entrega]]", "[[2026-1023-priceai-home-como-radar-y-no-como-vendedor]]", "[[2026-1023-priceai-faq-antifraude-y-prueba-pequena]]"]
---

## Claim
La página `https://priceai.cc/channels` es la vista **卡网订阅比价** (comparativa de canales 卡网) y su cabecera declara tres cosas literales: **"最近更新：6分钟前"**, **"53 个商品"** y la regla de precio **"主价格优先取有货最低价，缺货会明显标注"** — el precio principal es el más bajo *con stock*, y el agotamiento se marca de forma visible. Debajo, el descargo de la página es explícito: **"PriceAI 聚合 AI 订阅卡网渠道报价。本站不卖货、不担保，价格仅供参考，实际交易和售后规则以原平台为准。"** La captura cierra con el bloque **"购买前先看：渠道与售后判断"** y la nota **"本工具不构成购买建议"**.

## Why It Matters
Es el弥补 formal del módulo 卡网 que la home solo anunciaba: la tabla existe, con una regla de mínimo explícita y con un descargo de responsabilidad tan duro como el de la página de API ([[2026-1023-priceai-descargo-de-responsabilidad-sin-sla]]). Lo que cambia respecto a lo que el vault tenía ([[2026-1023-priceai-home-como-radar-y-no-como-vendedor]]) es que aquí **sí hay precios en yuanes**: el agregador no solo enruta, en esta herramienta entrega una cifra de mercado para cuentas y suscripciones revendidas.
La regla del mínimo importa para modelar: "cheapest" significa "cheapest **disponible**", no "más barato nunca". Una fila sin stock muestra **"暂无价格"** y su columna de canal dice **"暂无最低渠道"**, es decir, el agregador distingue explícitamente *no hay precio* de *no hay oferta*. Y el recordatorio de la FAQ —verificar la entrega y el servicio postventa del tienda original antes de comprar ([[2026-1023-priceai-faq-antifraude-y-prueba-pequena]])— convive con el hecho de que esta tabla es **el lugar donde PriceAI más se parece a un vendedor**, sin serlo.
