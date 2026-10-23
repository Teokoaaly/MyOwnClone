---
id: 2026-1023-priceai-channels-correo-y-jianma-a-centimos-como-insumo-de-alta
type: atom
certainty: solid
sources: [sources/2026-10-22-priceai-channels.md]
links: ["[[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]", "[[2026-1023-priceai-modulo-kanet-marcas-y-modos-de-entrega]]", "[[2026-1023-priceai-channels-dispersion-de-precios-cuatro-ordenes]]"]
---

## Claim
Las dos categorías de **insumos de alta** del catálogo 卡网 están tabuladas en la tabla de 53 filas, y sus precios son de céntimos: **接码 (códigos de verificación)** — Google / Gemini 接码 **¥0.20** (105 con stock, 20 agotados, 125 canales), **OpenAI / ChatGPT 接码 ¥0.37** (723/66/789, canal "狗儿codex 接🐎未接到可换号 包接马成功100% 福利用 没有售后"), **PayPal 接码 ¥0.49** (11/1/12, "狗儿巴西 PayPal【一次性接马】售出不退 只负责100%接马") y **通用接码 ¥0.57** (195/34/229, "短信 / 手机号验证"). **邮箱 (correo)** — 其他邮箱 **¥0.02** (71/22/93), **iCloud 邮箱 ¥0.02** (56/67/123), **Outlook / Hotmail 邮箱 ¥0.02** (259/36/295, "outlook邮箱带双令牌【二手 注册过部分产品 库存100w】"), **Gmail / Google 邮箱 ¥0.30** (298/127/425, "企业Edu谷歌账号(短效号.可用3天，全新注册)") y **教育邮箱 ¥1.24** (7/3/10). Aparte, **真人 / KYC 验证 ¥10.28** (1 con stock, 2 agotados, 3 canales).

## Why It Matters
La tabla convierte en **precio de mercado, en yuanes y con stock, el insumo visible en la página** que el vault hasta ahora solo conocía vía 5sim ([[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]): el código de verificación. El suelo de **¥0.20–¥0.57 por 接马** está dos órdenes por debajo de la mediana de 5sim ($0.8942 por activación de Telegram) y muy por debajo de su techo de $8.8897. La diferencia no es un dato comparable sin más (5sim vende el número, el 卡网 vende el código ya recibido, y el canal que ofrece el código barato es "狗儿", que declara "没有售后" y "售出不退"), pero sí indica que **existe una capa de proveedor que compra el número en algún sitio y lo revende como código**.
Eso cambia la lectura del coste marginal de alta del vault: el gasto en verificación no es un coste fijo de infraestructura con 5sim, es una **variable de mercado con dos proveedores y una alternativa mucho más barata y mucho más frágil**.
Y encaja con la taxonomía del módulo: la home lista 卡密, CDK y Kiro como parte de lo que el 卡网 vende ([[2026-1023-priceai-modulo-kanet-marcas-y-modos-de-entrega]]), y esta tabla lo confirma con precios: el correo y el 接码 son **la capa de consumibles** del mismo marketplace que luego vende la cuenta ya hecha. Por eso el suelo de céntimos no es un dato raro sino la base estructural del catálogo: todo lo demás (cuentas, suscripciones) se apoya sobre correo y verificación ([[2026-1023-priceai-channels-dispersion-de-precios-cuatro-ordenes]]).
El caso de 真人 / KYC 验证 a ¥10.28 con **1 sola unidad en stock y 3 canales** es el extremo opuesto: un servicio manual de verificación de identidad, con oferta casi nula y precio de tres órdenes de magnitud por encima del 接码 automático. Es la señal de que el cuello de botella del alta con cuenta real no es el SMS, sino el KYC humano.

## [FRICTION]
> [[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]] afirma que la verificación por SMS cuesta **$0.1026 a $8.8897 por unidad** con mediana $0.8942, y que "el coste marginal frente al modelo de costes" solo se optimiza "si se elige el par país-operador correcto".
> Este átomo presiona esa creencia en un punto concreto: la tabla de 卡网 ofrece 接马 de OpenAI/ChatGPT a **¥0.37** con **789 canales** y 723 unidades en stock, y 接码 genérico a **¥0.57** — muy por debajo del suelo de 5sim en dólares. Si el vault usa 5sim como referencia de coste marginal de alta, está usando la capa cara de un mercado que tiene una capa más barata cuyo control de calidad es explícitamente "没有售后" y "售出不退".
> Ambas no pueden ser completamente correctas: o el 接码 de 卡网 no es realmente el mismo servicio (un número propio, no un código cerrado) y por tanto no es comparable, o sí lo es y entonces el precio de referencia del vault está inflado por una decisión de proveedor no justificada por el precio. Marcado para juicio humano, no auto-resuelto.
