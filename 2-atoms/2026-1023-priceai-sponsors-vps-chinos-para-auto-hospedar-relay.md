---
id: 2026-1023-priceai-sponsors-vps-chinos-para-auto-hospedar-relay
type: atom
certainty: tentative
sources: [sources/2026-10-22-priceai-home.md]
links: ["[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1023-priceai-patrocinadores-y-canales-de-reventa-con-multiplicador]]", "[[2026-1023-hetzner-costes-por-categoria-vs-infraestructura-propia]]"]
---

## Claim
El bloque de patrocinadores de la home incluye **servidores VPS de proveedores chinos** con precios declarados en el propio texto del sponsor: **阿里云海外轻量服务器** (Aliyun, overseas lightweight) con **2核2G a partir de 68 元/año** y 85 % de descuento en la primera compra, y **腾讯云境外轻量服务器** (Tencent Cloud, fuera de China) con **2核4G desde 199 元/año**, "新老同享". El copy de Aliyun dice explícitamente que es "适合自用CPA反代、开发测试和 AI 工具备用机" (apto para reverse-proxy CPA propio, pruebas de desarrollo y máquina de reserva para herramientas de IA), y el de Tencent "适合小团队搭建sub2api自用中转、openclaw等" (apto para que un equipo pequeño monte su propio relay sub2api). Son **declaraciones de un patrocinador pagador**, no precios verificados por PriceAI.

## Why It Matters
Es la misma categoría de oferta que el vault ya midió en Hetzner, pero con una magnitud de precio radicalmente distinta: el plan más barato de Hetzner que el vault documentó es **€5,99/mes sin IVA** ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]), mientras que estas declaraciones prometen un VPS de 2 vCPU a **decenas de yuanes al año**. Si el vault ever documentara auto-hospedar un relay, esta sería la variable de coste dominante — y su valor es precisamente la razón por la que el sponsor tiene interés en que se cite.
La conexión con el modelo de negocio del vault es directa: el patron de "mono-proveedor de inferencia sin SLA" que el agregador ya честamente documenta ([[2026-1023-priceai-patrocinadores-y-canales-de-reventa-con-multiplicador]]) es exactamente lo que un relay auto-hospedado sustituye — y lo sustituye por un coste de infraestructura que hoy no aparece en ninguna categoría del back-office ([[2026-1023-hetzner-costes-por-categoria-vs-infraestructura-propia]]).
Advertencia de fiabilidad, explícita: son cifras **de marketing de patrocinador**, con descuento de primera compra, sin SLA declarado y sin verificación de PriceAI (que "no respalda ningún canal"). No son un precio confirmado.

## [FRICTION]
> [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]] afirma que **ningún plan del catálogo de Hetzner Cloud cabe en un presupuesto de ≤ €4/mes** y que el suelo de lista es €5,99/mes sin IVA; su "Why It Matters" concluye que el VPS de €4 tiene que venir "de otro proveedor o de un modelo distinto".
> Este átomo presiona esa creencia en un punto concreto: si se lee como una afirmación sobre **el coste de un VPS de 2 vCPU en general**, es falsa — hay proveedores (aliyun, tencent) que declaran el mismo orden de magnitud de CPU a un coste anual de decenas de yuanes. La conclusión del átomo viejo solo se sostiene **acotada al catálogo de Hetzner**, y el propio texto viejo ya lo dice así ("dentro del catálogo de Hetzner Cloud").
> Ambas no pueden ser completamente correctas en su lectura general: o el suelo de €6/mes es real solo para Hetzner y el vault no ha comparado proveedores, o existe una alternativa de hosting que invalida el presupuesto de referencia del vault. Marcado para juicio humano, no auto-resuelto: la alternativa aquí es un claim de sponsor, no un precio verificado, y no incluye SLA, ancho de banda internacional ni estabilidad.

## Nota de verificación
Las cifras (68 元/año, 199 元/año, 2核2G, 2核4G, 85 % de primera compra) están transcritas literalmente del copy de los patrocinadores. La captura **no** publica: SLA, ancho de banda, región efectiva, ni el precio sin descuento.
