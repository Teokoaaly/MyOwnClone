---
id: 2026-1026-heroku-suelo-5-dolares-eco-con-sleep-y-7-dolares-basic-always-on
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-pricing.md, sources/2026-10-25-heroku-dyno-sizes.md]
links: ["[[2026-1023-midjourney-proxy-despliegue-java17-y-paas-sin-servidor]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]"]
---

## Claim
El catálogo de **dynos Cedar** de Heroku arranca en **Eco a $5/mes**: 0.5 GB de RAM, compute **1x-4x**, **sin** Private Space, **2 process types**, "Deploy with Git and Docker", "Custom domains", "Unified logs", "Container orchestration", "Automatic OS patching", "Automated certificate management", "**Personal accounts only**" y "**Sleeps after 30 minutes of inactivity**". El siguiente escalón es **Basic a $7/mes**: 0.5 GB, 1x-4x, sin Private Space, "Includes all Eco features", "**Free SSL**", "**10 process types**", "**Always on**", "**0.28 Dyno Units / Month**".

## Why It Matters
Es la primera vez que el vault tiene el **suelo de catálogo de un PaaS gestionado con precio de lista y sin abstracción**: $5/mes por la compute mínima y $7/mes por la mínima que no se duerme. Ese suelo está **por encima** del techo de ≤ €4/mes que fijó [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]] y muy por encima del suelo de $0.83/mes de las ofertas de un año de LowEndBox: pagar "sin ops" tiene un mínimo de lista, y ese mínimo es una decisión de arquitectura, no de proveedor.
La comparación operativa con el stack vivo del vault ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]] — nginx + Postgres + Redis autoalojados) es que Heroku **duplica el precio de la compute** en cuanto se quiere el proceso siempre vivo: el "always on" cuesta $2/mes más y solo se paga el dyno, sin la base de datos ni el Redis, que se cobran aparte ([[2026-1026-heroku-postgres-essential-5-a-20-dolares-con-4-horas-de-parada]], [[2026-1026-heroku-key-value-store-mini-3-dolares-hasta-12500]]).

## [FRICTION]
> [[2026-1023-midjourney-proxy-despliegue-java17-y-paas-sin-servidor]] (escrita hace ~4 semanas) afirma que un PaaS permite levantar el proxy "**por 0 € de servidor**", y añade como nota de verificación que la fuente **no publica los precios de Railway ni de Zeabur** ni si tienen plan gratuito.
> Este átomo presiona esa creencia con un dato de la misma clase: el PaaS más caro de documentar —Heroku, con la tabla de precios más completa del sector— **no publica ningún plan gratuito**. Su suelo es **$5/mes** en un dyno que se duerme a los 30 minutos de inactividad, y **$7/mes** para uno que está siempre encendido. Sumando el dato gestionado más barato de cada capa (compute $5 + Postgres Essential $5 + Key-Value Mini $3), el suelo de un stack PaaS completo publicado es **$13/mes**.
> Ambas no pueden ser completamente correctas a la vez: o "PaaS = 0 € de servidor" es una propiedad de los PaaS del tipo Railway/Zeabur —con credit o free tier no publicados— o es una generalización no sostenida por el único PaaS del vault con precios verificables. Marcado para juicio humano, no auto-resuelto: la fuente de Heroku no permite afirmar nada sobre Railway ni Zeabur.

## Nota de extensión 2026-10-26
Fuente adicional: `sources/2026-10-25-heroku-dyno-sizes.md` (página "Technical Specifications by Dyno Size"). La tabla de specs publica **la letra pequeña del precio de Eco**, que la captura de precios no traía: "**Eco dynos require a $5 flat fee monthly subscription that covers a pool of 1000 hours shared by all Eco dynos in an account. Eco dynos are not available for Heroku Enterprise customers.**" Es decir, los **$5 no son el precio de un dyno** sino el precio de un **pool de 1000 horas compartido por toda la cuenta**, y Eco es el **único plan con la columna "Sleeps" marcada** (✔) y el **único con "Dyno Units Consumed: N/A"**. La misma página añade que "**Heroku charges for dynos based on usage, except for the Eco Dynos Plan**": el resto del catálogo **se cobra por uso**, no por suscripción. Detalle completo en [[2026-1026-heroku-eco-5-dolares-con-pool-de-1000-horas-compartidas]].
También queda confirmado aquí que **Basic es el único plan con 0,28 Dyno Units** y que Standard-1X cuesta **$25/mes por 1 DU** — el mismo $25 por unidad que la tabla de precios ya tenía, ahora con su columna de compute "1x-4x" al lado.
