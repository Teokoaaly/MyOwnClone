---
id: 2026-1026-noones-cuatro-casos-de-uso-como-catalogo-de-integracion
type: atom
certainty: solid
sources: [sources/2026-10-25-noones-developer-api.md]
links: ["[[2026-1026-noones-api-dos-formatos-directo-y-delegado]]", "[[2026-1024-noones-superficie-publica-productos-y-dominios-espejo]]", "[[2026-1023-midjourney-proxy-ecosistema-de-aplicaciones-que-lo-consumen]]", "[[2026-1026-noones-dev-noones-sin-precios-ni-limites-ni-documentacion-publica]]"]
---

## Claim
Los cuatro casos de uso publicados son, con su URL: **bank transfer** (`/case-studies/bank_transfer/`) — "create an automation bot to buy or sell crypto on your behalf, wherever you are"; **buying gift cards** (`/case-studies/buying_bot/`); **greeting app** (`/case-studies/greeting_app/`); y **el cuarto, con el slug `siwp_example`** (`/case-studies/siwp_example/`) — el ejemplo del historial de trading. Cada bloque lleva su propio badge de **Direct Access** o **Delegated Access**: bank transfer, buying bot y greeting app llevan "Direct Access", y el bloque de historial lleva "Direct Access Delegated Access", es decir, es el **único que opera en los dos formatos a la vez**.

## Why It Matters
La matriz badge-por-caso-de-uso es la información más útil de la captura porque **revela el modelo de integración antes que cualquier documento**: los tres casos "operativos" (comprar/vender, comprar gift cards, saludar) se clasifican como Direct Access — uno opera sobre su propia cuenta — y el único que necesita datos de **otros usuarios** es el de historial/auditoría, que por definición exige Delegated. Eso significa que **la superficie que cruza cuentas es estrecha y específica**, no un "haz lo que quieras con mi cuenta". Es el mismo criterio de marketplace de apps que el vault registró en el ecosistema de consumidores de Midjourney Proxy ([[2026-1023-midjourney-proxy-ecosistema-de-aplicaciones-que-lo-consumen]]): el tercero se instala encima, y lo que el proveedor documenta como "caso de uso" es en realidad **la lista de permisos que está dispuesto a ceder** ([[2026-1026-noones-dev-noones-sin-precios-ni-limites-ni-documentacion-publica]]).
