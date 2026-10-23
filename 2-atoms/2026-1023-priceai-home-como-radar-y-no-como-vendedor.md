---
id: 2026-1023-priceai-home-como-radar-y-no-como-vendedor
type: atom
certainty: solid
sources: [sources/2026-10-22-priceai-home.md]
links: ["[[2026-1023-priceai-descargo-de-responsabilidad-sin-sla]]", "[[2026-1023-priceai-cuatro-modulos-y-home-solo-desvia]]", "[[2026-1023-lzt-categoria-llm-accounts-para-reventa]]"]
---

## Claim
PriceAI se define en su propia home como un **"AI 低价卡网订阅与中转 API 比价雷达"** — un radar de comparación de precios de suscripciones y APIs de reventa — y su FAQ lo dice sin ambigüedad: **"PriceAI 不卖货、不收款、不参与交易"** (no vende goods, no cobra, no participa en la transacción); solo **agrega** los precios, fuentes, inventario, hora de actualización y enlaces originales que se pueden verificar antes de comprar. La home es además **pura分流** (enrutamiento): *"首页只负责分流。具体价格、库存、来源和购买链接，回到对应工具页完成."* La transacción final ocurre en la plataforma de origen, no en PriceAI.

## Why It Matters
Es la declaración de estatuto comercial del agregador: **no es un vendor ni un marketplace transaccional**, es una capa de descubrimiento y comparación. Eso lo coloca en una categoría distinta de lzt.market, que sí es un marketplace con venta de cuentas y tickets de disputa ([[2026-1023-lzt-categoria-llm-accounts-para-reventa]]), y también distinta del back-office del producto del vault, que es la única superficie donde hoy se registra el gasto real por proveedor ([[2026-1022-costes-por-categoria-tenant]]).
Para el vault la consecuencia práctica es de Epistemicidad: todo lo que salga de PriceAI es **precio de referencia declarado por un tercero**, nunca precio confirmado por el proveedor. El descargo de la página de API ya lo formaliza en un solo sentido —*只整理公开文档和公开页面中的 API 渠道信息，不售卖 API，不承诺可用性，不替任何渠道提供 SLA*— ([[2026-1023-priceai-descargo-de-responsabilidad-sin-sla]]).
Y hay un matiz de producto que importa para el diseño del vault: la home **no muestra un solo precio**. Sirve para decidir *a qué módulo ir*, no para modelar coste. Quien necesite cifras tiene que entrar en las cuatro páginas de herramienta ([[2026-1023-priceai-cuatro-modulos-y-home-solo-desvia]]), que es exactamente el patrón de agregador sin precios en la portada.
