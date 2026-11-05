---
id: 2026-1101-auth0-addon-agentes-ai-suma-50-por-ciento
type: atom
certainty: solid
sources: [sources/2026-11-01-auth0-pricing.md, sources/2026-11-03-auth0-pricing.md, sources/2026-11-04-auth0-pricing.md]
links: ["[[2026-1101-auth0-precios-por-mau-no-por-evento]]", "[[2026-1101-auth0-b2c-essentials-escala-por-mau]]", "[[2026-1023-ai-security-tools-agente-como-categoria-dominante]]", "[[2026-1103-auth0-workflows-agentes-ai-incluidos-en-plan-free]]", "[[2026-1103-auth0-header-precios-flexibles-hasta-millon-de-usuarios]]", "[[2026-1031-auth0-catalogo-de-addons-enterprise]]"]
---

## Claim
El add-on **"Auth0 for AI Agents" cuesta +50% sobre el precio base** (redondeado al dólar), e incluye Token Vault ilimitado y todas las formas de CIBA. En B2C Essentials a 500 MAU son $18/mes sobre una base de $35; en B2C Professional a 500 MAU, $120 sobre $240; en B2B Essentials a 500 MAU, $75 sobre $150.

## Why It Matters
Es un multiplicador **no negociable y no por uso**: el 50% se aplica al precio base del plan, así que el coste de identidad para agentes de IA **duplica** silenciosamente la factura en vez de ser un uso medible. Para un producto que vende clones de IA (MyOwnClone), esto significa que permitir que un tenant conecte su agente vía MCP con la identidad del producto cuesta, como mínimo, +$18/mes (B2C) o +$75/mes (B2B) en el escalón de 500 MAU — es decir, entre 4 y 18 veces el presupuesto de infra de ≤ €4/mes. La observación estructural que aporta al vault: Auth0 es el único de los tres proveedores de identidad documentados cuyo precio **crece por capabilities** (agentes, conexiones SSO, MFA) y no solo por usuarios; Clerk incluye todo sin gating ([[2026-1031-clerk-pricing]]) y WorkOS cobra por producto/API ([[2026-1031-workos-pricing]]). Y encaja con la tendencia que el vault ya registra en [[2026-1023-ai-security-tools-agente-como-categoria-dominante]]: la capa de identidad de los agentes es la que se está pagando.

## Nota de verificación
El "50%" y las cifras del add-on son lectura literal de la sección "B2C/B2B Add-ons" de la captura del 2026-11-01; el cálculo en euros frente al presupuesto de ≤ €4/mes es lectura de este átomo.

## 2026-11-03 — re-verificación (con matiz)
Fuente: `sources/2026-11-03-auth0-pricing.md` (render reducido de 540 palabras de auth0.com/pricing).

Esta captura **no publica precios de add-on**, así que no re-verifica el +50 %. Lo que sí aporta es una distinción que este átomo no hacía y que hay que registrar: la tarjeta del plan **Free incluye "Secure Agentic AI workflows"**, es decir, hay workflows agénticos **sin add-on de pago**, mientras que el add-on "Auth0 for AI Agents" (+50 %) es lo que añade Token Vault ilimitado y CIBA (ver [[2026-1103-auth0-workflows-agentes-ai-incluidos-en-plan-free]]).

La página reinforce el encuadre de agentes en dos puntos: el encabezado "Flexible pricing for all your apps and AI agents from user 1 to 1,000,000+" (ver [[2026-1103-auth0-header-precios-flexibles-hasta-millon-de-usuarios]]) y el add-on **AI Identity for B2B & AI Identity for Commerce**, que es el que conecta agentes con apps, APIs y servidores MCP (ver [[2026-1031-auth0-catalogo-de-addons-enterprise]]).

## Actualización 2026-11-04
Fuente: `sources/2026-11-04-auth0-pricing.md` (render completo restaurado, byte a byte idéntico al del 2026-11-01 — ver [[2026-1104-auth0-render-completo-restaurado-tras-el-reducido-del-11-03]]).

La regla del +50 % se ha **verificado de forma exhaustiva**: se comprobó `ceil(0,5 × precio_base)` contra las dos tablas de add-on de AI Agents en **los 30 pares (plan × escalón) publicables** (17 en B2C y 13 en B2B) y **no hay ni una sola excepción**. Ejemplos: B2C Essentials 2.500 MAU, base $175 → add-on $88 (50 % = $87,5, redondeado al alza); B2C Essentials 7.500 MAU, base $525 → $263 ($262,5 → $263); B2B Essentials 7.500 MAU, base $1.725 → $863 ($862,5 → $863); B2B Professional 2.500 MAU, base $1.200 → $600 (exacto).

Dos consecuencias nuevas:

1. El add-on de AI Agents es una **función pura del precio base**, sin escalones propios: no introduce ninguna partida que cotizar aparte, la factura es 1,5× la base con redondeo al alza al dólar. Como el redondeo es al alza, en los escalones impares el sobrecoste real supera el 50 % exacto (500 MAU B2C: 50 % = $17,50 → se cobran $18, +2,9 % sobre la base); en B2B a 500 MAU es exacto ($75).
2. En la facturación **anual** el add-on sí es exactamente **11× el mensual** en todos los escalones (verificado sobre las dos tablas yearly de AI Agents), pero **no** coincide con el 50 % del precio base anual, porque el redondeo al alza se aplica al valor mensual y luego se multiplica por 11. Ejemplo: B2C 500 MAU, base anual $385, add-on anual $198 — el 50 % de $385 serían $193.

Ver también [[2026-1104-auth0-guia-de-cotizacion-en-7-pasos-incorporada-a-la-pagina]]: la propia página define el cálculo como "Total = Base Price + sum of all applicable add-on prices", lo que confirma que el add-on de IA es la partida más auditable de todo el catálogo.
