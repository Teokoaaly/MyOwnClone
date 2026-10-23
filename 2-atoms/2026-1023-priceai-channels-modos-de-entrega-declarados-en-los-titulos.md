---
id: 2026-1023-priceai-channels-modos-de-entrega-declarados-en-los-titulos
type: atom
certainty: solid
sources: [sources/2026-10-22-priceai-channels.md]
links: ["[[2026-1023-priceai-channels-53-productos-y-minimo-con-stock]]", "[[2026-1023-priceai-modulo-kanet-marcas-y-modos-de-entrega]]", "[[2026-1023-priceai-channels-doble-columna-minimo-y-minimo-con-garantia]]"]
---

## Claim
El modo de entrega de cada oferta no está en una columna, sino **escrito dentro del título del canal más barato**, y la captura permite enumerar el vocabulario real: **官方充值** (recharge oficial, 8 apariciones), **卡冲官方充值** (2), **直冲个人账号** (1), **成品号** (12), **速刷** (5), **CDK** (3), **卡密** (1), **提链** (3), **邀请码** (2), **账密+2FA** (2), **自助**下单/发货 (9+2), **扫码** (2), **拼车** (2), **家庭组车位** (2). La columna `最低渠道` reproduce el título comercial del canal junto a la descripción literal de la entrega: por ejemplo "沐风AI…【官方充值】Codex Go [埃及] CDK 质保订阅30天", "大个儿…plus官方充值月卡（质保30天）----直冲个人账号---自动发货-(24h全自动充值)", "AI海外账号…claude max x20 速刷号！9.22开始，日产300，平均存活3天，包首登", "稳中求胜…GroK Super heavy速刷成品号", "商家8719…Claude 6.25X【质保订阅】封号不保（母号被封/被退也不保）席位成品号/直充（需要等）" y "牟利ai…（封禁账号需申诉使用）无售后…Gemini Pro 12个月pixel成品号需要绑定手机".

## Why It Matters
Esto confirma empíricamente lo que la home solo afirmaba en abstracto: el módulo 卡网 compara **stock y forma de entrega** ([[2026-1023-priceai-modulo-kanet-marcas-y-modos-de-entrega]]). La captura muestra que la forma de entrega está **codificada en el texto del canal más barato**, no en un campo estructurado — no hay columna de entrega, hay prosa de marketplace chino. Consecuencia práctica para el vault: no se puede automatizar la comparación de entregas leyendo columnas; hay que parsear títulos, y el título mezcla marketing con términos técnicos (CDK, 提链, 2FA, 拼车) y con advertencias de riesgo. La propia tabla no tiene columna de entrega: la cabecera solo declara el eje estructural "主价格优先取有货最低价，缺货会明显标注" ([[2026-1023-priceai-channels-53-productos-y-minimo-con-stock]]), es decir, precio y disponibilidad, nada más.
Las advertencias son el material más valioso: los propios vendedores declaran **"封号不保（母号被封/被退也不保）"**, **"无售后"**, **"平均存活3天"**, **"日产300"**, **"封禁账号需申诉使用"**, **"需要绑定手机"**, **"兑换后有效期两小时"** (tarjeta virtual VISA). Es decir, el riesgo de la reventa no lo oculta el agregador: lo escribe el canal, y quien lo lee rápido se lo pierde. Estas declaraciones explican por qué la columna `质保最低价` puede multiplicar el precio hasta ×1.659 ([[2026-1023-priceai-channels-doble-columna-minimo-y-minimo-con-garantia]]).
Para el producto del vault, la implicación es de diseño: un flujo de alta que dependa de cuentas revendidas necesita modelar explícitamente **caducidad esperada y riesgo de bloqueo**, porque esos dos números vienen en el texto del canal, no en el precio.
