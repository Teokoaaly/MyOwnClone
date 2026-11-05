---
id: 2026-1027-veridrop-riesgo-legal-gris-y-tres-peligros-practicos-del-relay
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1024-veridrop-relays-con-dominios-efimeros-y-riesgo-de-contraparte]]", "[[2026-1023-priceai-faq-antifraude-y-prueba-pequena]]", "[[2026-1027-veridrop-cinco-indicadores-duros-para-elegir-relay]]"]
---

## Claim
La FAQ sitúa el uso de relays en una **zona gris legal** (*"法律上灰色地带,看具体合作模式"*) y declara **tres riesgos prácticos concretos**: **① 跑路风险** — el relay **puede dejar de servir, subir precios o desaparecer con el saldo**, por lo que **"大额充值要慎重"**; **② 模型响应跟官方不一致** — el relay puede alterar el modelo, retirar capacidades o **falsear el recuento de tokens**, con impacto directo en la estabilidad del negocio que consume; **③ prompt 内容被记录** — **"涉及商业机密 / 用户数据的对话最好避开来路不明的中转站"**. La recomendación operativa es: **pequeña prueba, operador de confianza, y conexión directa a oficial para escenarios grandes**. La FAQ añade el quinto riesgo de la lista de trampas: **"规则说变就变"** — la misma key puede pasar de funcionar a pedir **"升级套餐"**, **"分组失效"** o **直接封号** sin previo aviso.

## Why It Matters
Es la **descripción de los riesgos por el lado del comprador**, complemento del perfil de contraparte de [[2026-1024-veridrop-relays-con-dominios-efimeros-y-riesgo-de-contraparte]], y es el complemento exacto del que el vault ya tenía: los átomos existentes de VeriDrop caracterizaban el **riesgo de contraparte** (dominios efímeros, 48 de 50 foráneos, TLDs de baja fricción), es decir, **que el relay puede desaparecer**; esta FAQ añade **que el saldo puede desaparecer con él** y que **las reglas pueden cambiar sin aviso**, lo que convierte el prepago en la partida más expuesta. La diferencia es de grado y no de naturaleza: **no es un proveedor con SLA al que se le reclama, es un saldo que se pierde**.
El riesgo ② es el que el vault ha estado midiendo por otros medios (detectores, veredictos, verificaciones de tokens), y el riesgo ③ es el que **no se puede verificar con un detector**: es un riesgo de **custodia de datos**, no de calidad de servicio. El vault lo tenía registrado en otras capas del producto (correos desechables, proxies, números de SMS), pero no en la capa de inferencia: **un relay recibe el prompt completo del usuario final**, que en el caso de MyOwnClone incluye material de conversación. La receta de la FAQ — **prueba pequeña, operador conocido, directo para volumen** — se solapa con el protocolo antifraude de [[2026-1023-priceai-faq-antifraude-y-prueba-pequena]] y con el cribado de [[2026-1027-veridrop-cinco-indicadores-duros-para-elegir-relay]] — es exactamente la política de minimización de exposición que el vault viene aplicando en las capas de coste por insumo.
Y el dato de la "regla que cambia sin aviso" tiene una lectura de arquitectura: **el contrato implícito con un relay no es un contrato**, es una configuración que el otro puede editar. Para el producto, eso significa que **la lista de proveedores de `OPENAI_API_BASE` necesita un plan de sustitución, no solo un plan de elección**.

## Nota de verificación
Los tres riesgos y el quinto punto de la lista de trampas son literales de la FAQ. La captura **no** publica un ejemplo concreto de relay que haya "跑路", ni cifras de prevalencia, ni el marco legal concreto que se considera en zona gris.
