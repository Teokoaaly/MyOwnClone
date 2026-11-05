---
id: 2026-1024-veridrop-relays-con-dominios-efimeros-y-riesgo-de-contraparte
type: atom
certainty: solid
sources: [sources/2026-10-23-veridrop-relays.md]
links: ["[[2026-1023-lzt-categoria-llm-accounts-para-reventa]]", "[[2026-1024-veridrop-concentracion-de-muestras-en-tres-relays]]", "[[2026-1023-priceai-transit-canal-tipo-sub2api-vs-new-api]]"]
---

## Claim
Los 50 relays del directorio de VeriDrop viven en **dominios casi todos de perfil volátil**: solo **17 de 50** son `.com`, y el resto se reparte en `.top` (5), `.ai` (5), `.xyz` (3), `.dev` (2), `.cn` (2), `.shop` (2), `.cc` (2) y una unidad en cada uno de `.net`, `.id`, `.me`, `.pro`, `.lol`, `.fun`, `.chat`, `.skin`, `.org`, `.si`, `.cloud` y `.cd`. Entre los nombres listados hay `ddos.skin`, `xgapi.lol`, `666six.top`, `qwer069.com`, `sub.lk1950.xyz`, `freepro20x.fun`, `api.nachoneko.chat`, `token.mewinyou.shop`. Solo **2 dominios son `.cn`** (`fluxlane.cn`, `api.a77ai.cn`) frente a **48 foráneos**, y ninguno de los dominios listados es un nombre de marca de proveedor de modelo.

## Why It Matters
Para MyOwnClone, que consume un LLM vía `OPENAI_API_BASE`, la contraparte de cada relay es **un dominio pequeño, en su mayoría sin marca y con un TLD de baja fricción**, no una empresa. El riesgo no es teórico: el nombre `ddos.skin` es literalmente el de un sitio dedicado a DDoS, y un TLD `.lol` o `.fun` no impone ninguna verificación. Es el mismo patrón de contraparte efímera que el vault ya caracterizó en el mercado de cuentas de IA ([[2026-1023-lzt-categoria-llm-accounts-para-reventa]]): hay una oferta abundante, barata y sin continuidad.
Esto fija también un límite a cualquier tabla de "mejores relays": el activo que el vault está a punto de pagar por es **acceso a un endpoint en un dominio que puede dejar de existir**, y esa pérdida no la cubre ningún multiplicador ni ninguna insignia PRO. El hecho de que la mitad de las entradas acumulen ≤ 6 tests refuerza que la cola del directorio es material de un solo día ([[2026-1024-veridrop-concentracion-de-muestras-en-tres-relays]]).

## Nota de verificación
Recuento literal de TLD sobre los 50 dominios de la captura; la captura **no** publica: fecha de alta de cada dominio, quién opera cada relay, ni si alguno está detrás de una empresa identificable.


## Nota de extensión 2026-10-27
La FAQ añade el **lado del comprador** del riesgo de contraparte, con tres riesgos prácticos declarados: **① 跑路风险** — el relay puede dejar de servir, subir precios o **desaparecer con el saldo** (**"大额充值要慎重"**); **② 模型响应跟官方不一致** — cambio de modelo, retirada de capacidades o **falsificación del recuento de tokens**; **③ prompt 内容被记录** — **"涉及商业机密 / 用户数据的对话最好避开来路不明的中转站"**. Y un quinto punto de la lista de trampas: **"规则说变就变"**, con la misma key pasando de funcionar a **"升级套餐"**, **"分组失效"** o **直接封号** sin previo aviso. Es la confirmación textual de que **el contrato implícito con un relay no es un contrato**, sino una configuración que el otro puede editar. Véanse [[2026-1027-veridrop-riesgo-legal-gris-y-tres-peligros-practicos-del-relay]] y [[2026-1027-veridrop-cinco-indicadores-duros-para-elegir-relay]].
