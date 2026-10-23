---
id: 2026-1023-priceai-channels-39-tiendas-y-una-larga-cola-de-revendedores
type: atom
certainty: solid
sources: [sources/2026-10-22-priceai-channels.md]
links: ["[[2026-1023-priceai-channels-stock-por-fila-y-seis-productos-muertos]]", "[[2026-1023-lzt-categoria-llm-accounts-para-reventa]]", "[[2026-1023-priceai-mecanismo-de-denuncia-y-baja-de-productos]]"]
---

## Claim
La columna `最低渠道` nombra **39 tiendas distintas** (47 filas con canal nombrado; 6 filas sin oferta muestran "暂无最低渠道"). La concentración es baja pero no nula: **siete tiendas aparecen en más de una fila** — **AI海外账号** en 3 (ChatGPT Pro 200刀档, Claude Max 20x, X / 推特账号), y **大个儿---欢迎分销--对接：97dg**, **小久**, **稳中求胜**, **狗儿**, **优质AI科技** y **皮特小铺** en 2 cada una. Los nombres de tienda son descriptivos del negocio, no marcas: "大个儿---欢迎分销--对接：97dg" (busca revendedores, publica su WeChat de contacto), "沐风AI codex源头 诚招代理", "奶龙Gemini订阅(源头招代理)", "AI批发站｜渠道供货｜自助下单", "海外批发【人工发货】", "优质AI科技", "CIM 对接马CIMCIM" y "商家8719" (un número sin marca). Varias declaran explícitamente el modelo de negocio: **"源头"** (proveedor de origen), **"招代理"** (busca revendedores), **"分销"** (distribuye), **"对接：97dg"** (contacto para integrarse).

## Why It Matters
Es un **mercado de intermediarios con cola larga**, no un marketplace con vendedores concentrados: 39 tiendas para 11.874 canales significa que la mayoría de los "canales" son SKUs o listings de un mismo vendedor, no vendedores distintos. El agregador está, de hecho, indexando **listas de precios publicadas por tiendas** — muchas de ellas con perfil de *dropshipper* (广告, 招代理, 分销, 对接).
Para el vault esto tiene dos consecuencias. Primera, **la selección de proveedor no es un problema de marca**: cuando el producto del vault compre del lado de la reventa, no hay "el proveedor" — hay 39 vendedores anónimos con nombres de WeChat, y la ruta de calidad es el propio texto del título y el contador de canales. Segunda, la presencia literal de "招代理" y "分销" confirma el mecanismo que la home ya describía: el canal de reventa **quiere revendedores** que le compren, o sea, el mercado de cuentas de IA tiene una capa mayorista por encima de la minorista.
El detalle de "商家8719" (un identificador numérico como nombre de tienda) sugiere además que PriceAI indexa **marketplaces discretos con IDs**, no solo tiendas con marca — lo que implica que la columna de canal mezcla fuentes heterogéneas sin normalizar.
Y es también el límite del recurso de moderación que el agregador ofrece: el botón de 举报 opera **por producto y por canal**, y baja la entrada anómala del índice ([[2026-1023-priceai-mecanismo-de-denuncia-y-baja-de-productos]]). Con 39 tiendas y 11.874 canales, esa es la única vía para limpiar un vendedor malo — no hay un score de proveedor, solo una baja reactiva por queja de comprador.
El agregado que cierra el cálculo es el de los contadores por fila: **9.147 unidades con stock repartidas entre 47 filas con canal nombrado** ([[2026-1023-priceai-channels-stock-por-fila-y-seis-productos-muertos]]).

## [FRICTION]
> [[2026-1023-lzt-categoria-llm-accounts-para-reventa]] afirma que el mercado de "cuentas de IA ya hechas" es "un segundo mercado, el de la cuenta revocada o de stock ya exista, **cuyo precio la captura no publica**", y su propio bloque de fricción sostiene que "el insumo de identidad verificada del vault tiene un precio de mercado que no es el del SMS y que **todavía no está medido**".
> Este átomo presiona esa creencia en un punto concreto: el precio **sí** está medido y es público. La tabla de 卡网 de PriceAI publica 53 filas de cuentas y suscripciones revendidas con precio en yuanes, stock, número de canales y timestamp, desde **ChatGPT 普号 a ¥0.05** hasta **Claude Max 20x a ¥1,027.94**, con el desglose de entrega (成品号, 速刷, CDK, 官方充值) en el propio título. La captura de lzt.market no lo publicaba; la de PriceAI sí.
> Ambas no pueden ser completamente correctas: o la tabla de PriceAI no mide el mismo objeto que la categoría `LLM Accounts` de lzt (cuentas de reventa vs. cuentas created-and-verified en marketplace), o el precio de ese insumo ya no está sin medir y el vault tiene un precio de referencia público que no estaba usando. Marcado para juicio humano, no auto-resuelto.
