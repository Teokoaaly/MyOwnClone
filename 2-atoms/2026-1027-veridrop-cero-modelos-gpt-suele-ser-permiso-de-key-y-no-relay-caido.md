---
id: 2026-1027-veridrop-cero-modelos-gpt-suele-ser-permiso-de-key-y-no-relay-caido
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-openai-detection.md, sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1027-veridrop-el-usage-de-la-respuesta-delata-el-trasvase-de-protocolo]]", "[[2026-1027-veridrop-openai-deteccion-nivel-comportamiento-protocolo-sin-prueba-criptografica]]", "[[2026-1024-veridrop-ventana-de-actividad-y-frescura-de-deteccion]]"]
---

## Claim
Un resultado de **"0 个 GPT 模型可用"** casi nunca significa que el relay esté caído: la FAQ es explícita —*"大概率不是中转站坏了,而是 **这把 key 没开通 GPT 模型权限**"* — y da la causa estructural: **"很多综合中转站把模型按厂家分组卖,有的客户买的是 Claude 卡、有的是 Gemini 卡,没买就调不出对应模型"**. El detector lo trata con un **preflight** que lista los modelos que la key sí puede usar, y en el caso de la página OpenAI muestra una **tarjeta amarilla** con el recuento por fabricante (*"这把 key 实际能用 X 个 Claude 模型,要去那边测吗?"*) y un enlace a la página del otro protocolo.

## Why It Matters
Es un **desambiguador de causas** con una regla de negocio detrás, y esa regla de negocio es la que hay que copiar al producto: **el acceso a un modelo en un relay multi-fabricante estásegmentado por el tipo de tarjeta que se compró, no por la disponibilidad técnica del relay**. Consecuencia directa: **"0 modelos GPT" es un dato sobre la key, no sobre el relay**, y por tanto **no puede usarse como señal de disponibilidad** — un error de lectura en el que es fácil caer si se agrega "nº de modelos detectados" por relay.
Y en un canal de reventa, esto es aún más relevante: el modelo que un usuario puede invocar depende de **qué clave y qué saldo tiene**, lo que significa que **el mismo relay presenta un catálogo distinto a cada cliente**. Para un agregador de precios, la consecuencia es estructural: **el precio de un modelo no es una propiedad del relay sino del par (relay, tipo de tarjeta del cliente)**. Es una forma de segmentación de precio oculta que el vault no había registrado en el sector de relays, y que se suma a la segmentación por grupos ya documentada en el gateway de referencia ([[2026-1026-new-api-consulta-de-saldo-upstream-y-prioridad-arrastrable]]).
LaFAQtamoco esta idea en la otra dirección, con un matiz que hay que registrar: un relay puede llevar meses "activo" y aun así tener un catálogo que no incluye GPT para ninguna key ([[2026-1024-veridrop-ventana-de-actividad-y-frescura-de-deteccion]]); **disponibilidad del relay y disponibilidad del modelo son dos variables distintas**.

## Nota de verificación
Literal de las dos fuentes. La captura **no** publica la granularidad exacta de la agrupación por fabricante (qué modelos entran en cada "tarjeta"), ni si el preflight es gratuito o cuenta como detección.

## [FRICTION]
> [[2026-1024-veridrop-home-la-disponibilidad-se-mide-por-par-sitio-y-modelo]] (escrita el 2026-10-25) establece que **la disponibilidad es una propiedad del par (sitio, modelo)**, y [[2026-1024-veridrop-ventana-de-actividad-y-frescura-de-deteccion]] que cada fila publica dos denominadores (histórico y ventana). Esta nota presiona esa lectura con un tercer factor: la propia FAQ de VeriDrop admite que **"0 个 GPT 模型可用"** casi nunca es una caída del relay sino **falta de permiso GPT en la key**, porque **"很多综合中转站把模型按厂家分组卖"**. Es decir: el par (sitio, modelo) **no es una clave suficiente** para leer la disponibilidad — falta una tercera dimensión, **el tipo de tarjeta o grupo del cliente** ([[2026-1023-new-api-grupos-como-eje-de-precio-del-relay]]). Si un mismo relay es "100 % disponible en GPT 5.6" en la home y su key de un cliente concreto da "0 modelos GPT", **las dos cifras no se contradicen: miden cosas distintas**. Ambas no pueden ser la misma unidad de disponibilidad. Marcado para juicio humano, no auto-resuelto.
